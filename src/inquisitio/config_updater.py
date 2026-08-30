"""Config Updater — applies test mutations and bumps balance versions in game_config.yaml."""
from __future__ import annotations

import re
import shutil
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml

from inquisitio.config import CONFIG, _CONFIG_PATH


def bump_version_string(current: str) -> str:
    """Bumps version string: v0.19 -> v0.20, v1.2 -> v1.3, etc."""
    m = re.search(r"(\d+)$", current)
    if m:
        num_str = m.group(1)
        next_num = int(num_str) + 1
        prefix = current[: m.start(1)]
        return f"{prefix}{next_num}"
    return f"{current}_next"


def _apply_offset_to_item(item: Any, offset: int, min_val: int = 1) -> Any:
    """Apply offset to scalar or dict with 3p/4p/5p keys."""
    if isinstance(item, dict):
        new_d = {}
        for k, v in item.items():
            new_d[k] = max(min_val, int(v) + offset)
        return new_d
    return max(min_val, int(item) + offset)


def _nudge_gc_falls(falls: Any, offset: int) -> Any:
    """Scalar falls, or legacy default/no_oficjum dict — both keys move together."""
    if isinstance(falls, dict):
        out = dict(falls)
        for k in ("default", "no_oficjum"):
            if k in out:
                out[k] = max(1, int(out[k]) + offset)
        if "default" in out and "no_oficjum" in out and out["default"] == out["no_oficjum"]:
            return out["default"]
        return out
    return max(1, int(falls) + offset)


def apply_mutation_to_config(
    raw_cfg: dict[str, Any],
    rule_id: str,
    rule_params: dict[str, Any],
) -> tuple[dict[str, Any], str]:
    """Applies a rule's parameter override directly to the raw config dict.
    Supports single mutations, multi-card overrides, and composite 2D/3D mutations.
    Returns (modified_raw_config, human_readable_description).
    """
    sys_cfg = raw_cfg.get("system", {})
    vic_cfg = raw_cfg.get("victory", {})
    var_cfg = raw_cfg.get("variants", {})
    cards_cfg = raw_cfg.get("cards", {})

    descriptions: list[str] = []

    # --- Level 1: System Parameters (Global & Per-Format) ---
    for p_key in ("3p", "4p", "5p"):
        k = f"threshold_{p_key}_offset"
        if k in rule_params:
            off = rule_params[k]
            if not isinstance(sys_cfg.get("accusation_threshold"), dict):
                cur = int(sys_cfg.get("accusation_threshold", 7))
                sys_cfg["accusation_threshold"] = {"3p": cur, "4p": cur, "5p": cur}
            sys_cfg["accusation_threshold"][p_key] = max(1, int(sys_cfg["accusation_threshold"].get(p_key, 7)) + off)
            descriptions.append(f"Próg oskarżenia ({p_key}): offset {off:+d} (nowy: {sys_cfg['accusation_threshold'][p_key]})")

        k = f"start_gold_{p_key}_offset"
        if k in rule_params:
            off = rule_params[k]
            if not isinstance(sys_cfg.get("start_gold"), dict):
                cur = int(sys_cfg.get("start_gold", 4))
                sys_cfg["start_gold"] = {"3p": cur, "4p": cur, "5p": cur}
            sys_cfg["start_gold"][p_key] = max(0, int(sys_cfg["start_gold"].get(p_key, 4)) + off)
            descriptions.append(f"Startowe złoto ({p_key}): offset {off:+d} (nowe: {sys_cfg['start_gold'][p_key]}zł)")

        k = f"hand_limit_{p_key}_offset"
        if k in rule_params:
            off = rule_params[k]
            if not isinstance(sys_cfg.get("hand_limit"), dict):
                cur = int(sys_cfg.get("hand_limit", 5))
                sys_cfg["hand_limit"] = {"3p": cur, "4p": cur, "5p": cur}
            sys_cfg["hand_limit"][p_key] = max(1, int(sys_cfg["hand_limit"].get(p_key, 5)) + off)
            descriptions.append(f"Limit kart na ręce ({p_key}): offset {off:+d} (nowy: {sys_cfg['hand_limit'][p_key]})")

    if "threshold_offset" in rule_params:
        off = rule_params["threshold_offset"]
        sys_cfg["accusation_threshold"] = _apply_offset_to_item(sys_cfg["accusation_threshold"], off, min_val=1)
        descriptions.append(f"Próg oskarżenia: offset {off:+d}")
    if "observed_threshold_offset" in rule_params:
        off = rule_params["observed_threshold_offset"]
        sys_cfg["observed_threshold"] = max(1, int(sys_cfg.get("observed_threshold", 4)) + off)
        descriptions.append(f"Próg Obserwowanej: offset {off:+d} (nowy: {sys_cfg['observed_threshold']})")
    if "observed_threshold" in rule_params:
        sys_cfg["observed_threshold"] = max(1, int(rule_params["observed_threshold"]))
        descriptions.append(f"Próg Obserwowanej: {sys_cfg['observed_threshold']}")
    if "cards_per_era_offset" in rule_params:
        off = rule_params["cards_per_era_offset"]
        sys_cfg["cards_per_era"] = max(1, int(sys_cfg.get("cards_per_era", 2)) + off)
        descriptions.append(f"Karty/Erę: offset {off:+d} (nowy: {sys_cfg['cards_per_era']})")
    if "era_income_offset" in rule_params:
        off = rule_params["era_income_offset"]
        sys_cfg["era_income"] = max(0, int(sys_cfg.get("era_income", 1)) + off)
        descriptions.append(f"Dochód Ery: offset {off:+d} (nowy: {sys_cfg['era_income']})")
    if "intrigue_gold_offset" in rule_params:
        off = rule_params["intrigue_gold_offset"]
        sys_cfg["intrigue_gold"] = max(0, int(sys_cfg.get("intrigue_gold", 1)) + off)
        descriptions.append(f"Akcja Gospodarcza: offset {off:+d} (nowy: {sys_cfg['intrigue_gold']})")
    if "max_eras_offset" in rule_params:
        off = rule_params["max_eras_offset"]
        sys_cfg["max_eras"] = max(1, sys_cfg.get("max_eras", 8) + off)
        descriptions.append(f"Limit Er: offset {off:+d} (nowy: {sys_cfg['max_eras']})")
    if "start_gold_offset" in rule_params:
        off = rule_params["start_gold_offset"]
        sys_cfg["start_gold"] = _apply_offset_to_item(sys_cfg["start_gold"], off, min_val=1)
        descriptions.append(f"Startowe złoto: offset {off:+d}")
    if "agents_offset" in rule_params:
        off = rule_params["agents_offset"]
        sys_cfg["agents_per_player"] = max(1, sys_cfg.get("agents_per_player", 3) + off)
        descriptions.append(f"Liczba agentów: offset {off:+d} (nowa: {sys_cfg['agents_per_player']})")
    if "hand_limit_offset" in rule_params:
        off = rule_params["hand_limit_offset"]
        sys_cfg["hand_limit"] = _apply_offset_to_item(sys_cfg["hand_limit"], off, min_val=1)
        descriptions.append(f"Limit kart na ręce: offset {off:+d}")
    if "cooldown_offset" in rule_params:
        off = rule_params["cooldown_offset"]
        sys_cfg["autodafe_cooldown"] = max(0, sys_cfg.get("autodafe_cooldown", 3) + off)
        descriptions.append(f"Cooldown Autodafé: offset {off:+d} (nowy: {sys_cfg['autodafe_cooldown']})")
    if "autodafe_cooldown" in rule_params:
        sys_cfg["autodafe_cooldown"] = max(0, int(rule_params["autodafe_cooldown"]))
        descriptions.append(f"Cooldown Autodafé: {sys_cfg['autodafe_cooldown']}")
    if "start_gold" in rule_params:
        sys_cfg["start_gold"] = max(0, int(rule_params["start_gold"]))
        descriptions.append(f"Startowe złoto: {sys_cfg['start_gold']}zł")
    if "max_eras" in rule_params:
        sys_cfg["max_eras"] = max(1, int(rule_params["max_eras"]))
        descriptions.append(f"Limit Er: {sys_cfg['max_eras']}")

    # --- Level 2: Victory Conditions (Global & Per-Format) ---
    for p_key in ("3p", "4p", "5p"):
        k = f"so_stacks_{p_key}_offset"
        if k in rule_params:
            off = rule_params[k]
            so = vic_cfg.setdefault("swiete_oficjum", {})
            if not isinstance(so.get("stacks"), dict):
                cur = int(so.get("stacks", 7))
                so["stacks"] = {"3p": cur, "4p": cur, "5p": cur}
            so["stacks"][p_key] = max(1, int(so["stacks"].get(p_key, 7)) + off)
            descriptions.append(f"Święte Oficjum: Stosy ({p_key}) offset {off:+d} (nowe: {so['stacks'][p_key]})")

        k = f"so_condemns_{p_key}_offset"
        if k in rule_params:
            off = rule_params[k]
            so = vic_cfg.setdefault("swiete_oficjum", {})
            if not isinstance(so.get("condemns"), dict):
                cur = int(so.get("condemns", 3))
                so["condemns"] = {"3p": cur, "4p": cur, "5p": cur}
            so["condemns"][p_key] = max(1, int(so["condemns"].get(p_key, 3)) + off)
            descriptions.append(f"Święte Oficjum: Skazania ({p_key}) offset {off:+d} (nowe: {so['condemns'][p_key]})")

        k = f"gc_falls_{p_key}_offset"
        if k in rule_params:
            off = rule_params[k]
            gc = vic_cfg.setdefault("gildia_cieni", {})
            if not isinstance(gc.get("falls"), dict):
                cur = int(gc.get("falls", 9))
                gc["falls"] = {"3p": cur, "4p": cur, "5p": cur}
            gc["falls"][p_key] = max(1, int(gc["falls"].get(p_key, 9)) + off)
            descriptions.append(f"Gildia Cieni: Upadki ({p_key}) offset {off:+d} (nowe: {gc['falls'][p_key]})")

        k = f"caa_relics_{p_key}_offset"
        if k in rule_params:
            off = rule_params[k]
            caa = vic_cfg.setdefault("cienie_al_andalus", {})
            if not isinstance(caa.get("relics"), dict):
                cur = int(caa.get("relics", 2))
                caa["relics"] = {"3p": cur, "4p": cur, "5p": cur}
            caa["relics"][p_key] = max(1, int(caa["relics"].get(p_key, 2)) + off)
            descriptions.append(f"Cienie Al-Andalus: Relikwie ({p_key}) offset {off:+d} (nowe: {caa['relics'][p_key]})")

        k = f"kb_decrees_{p_key}_offset"
        if k in rule_params:
            off = rule_params[k]
            kb = vic_cfg.setdefault("korona_borgiowie", {})
            if not isinstance(kb.get("decrees"), dict):
                cur = int(kb.get("decrees", 2))
                kb["decrees"] = {"3p": cur, "4p": cur, "5p": cur}
            kb["decrees"][p_key] = max(1, int(kb["decrees"].get(p_key, 2)) + off)
            descriptions.append(f"Korona Borgiowie: Dekrety ({p_key}) offset {off:+d} (nowe: {kb['decrees'][p_key]})")

        k = f"kb_hooks_{p_key}_offset"
        if k in rule_params:
            off = rule_params[k]
            kb = vic_cfg.setdefault("korona_borgiowie", {})
            if not isinstance(kb.get("hooks"), dict):
                cur = int(kb.get("hooks", 2))
                kb["hooks"] = {"3p": cur, "4p": cur, "5p": cur}
            kb["hooks"][p_key] = max(0, int(kb["hooks"].get(p_key, 2)) + off)
            descriptions.append(f"Korona Borgiowie: Haki ({p_key}) offset {off:+d} (nowe: {kb['hooks'][p_key]})")

        k = f"kt_frags_{p_key}_offset"
        if k in rule_params:
            off = rule_params[k]
            kt = vic_cfg.setdefault("kabala_toledo", {})
            if not isinstance(kt.get("fragments"), dict):
                cur = int(kt.get("fragments", 3))
                kt["fragments"] = {"3p": cur, "4p": cur, "5p": cur}
            kt["fragments"][p_key] = max(1, int(kt["fragments"].get(p_key, 3)) + off)
            descriptions.append(f"Kabała Toledo: Fragmenty ({p_key}) offset {off:+d} (nowe: {kt['fragments'][p_key]})")

    if "so_stacks_offset" in rule_params:
        off = rule_params["so_stacks_offset"]
        vic_cfg["swiete_oficjum"]["stacks"] = _apply_offset_to_item(vic_cfg["swiete_oficjum"]["stacks"], off, min_val=1)
        descriptions.append(f"Święte Oficjum: Stosy offset {off:+d}")
    if "so_condemns_offset" in rule_params:
        off = rule_params["so_condemns_offset"]
        vic_cfg["swiete_oficjum"]["condemns"] = _apply_offset_to_item(vic_cfg["swiete_oficjum"]["condemns"], off, min_val=1)
        descriptions.append(f"Święte Oficjum: Skazania offset {off:+d}")
    if "caa_relics_offset" in rule_params:
        off = rule_params["caa_relics_offset"]
        vic_cfg["cienie_al_andalus"]["relics"] = _apply_offset_to_item(vic_cfg["cienie_al_andalus"]["relics"], off, min_val=1)
        descriptions.append(f"Cienie Al-Andalus: Relikwie offset {off:+d}")
    if "kb_era_offset" in rule_params:
        kb = vic_cfg["korona_borgiowie"]
        if "era" in kb:
            off = rule_params["kb_era_offset"]
            kb["era"] = _apply_offset_to_item(kb["era"], off, min_val=1)
            descriptions.append(f"Korona Borgiowie: Era zwycięstwa offset {off:+d}")
    if "kb_decrees_offset" in rule_params:
        off = rule_params["kb_decrees_offset"]
        vic_cfg["korona_borgiowie"]["decrees"] = _apply_offset_to_item(vic_cfg["korona_borgiowie"]["decrees"], off, min_val=1)
        descriptions.append(f"Korona Borgiowie: Dekrety offset {off:+d}")
    if "kb_hooks_offset" in rule_params:
        off = rule_params["kb_hooks_offset"]
        kb = vic_cfg["korona_borgiowie"]
        kb["hooks"] = _apply_offset_to_item(kb.get("hooks", 0), off, min_val=0)
        descriptions.append(f"Korona Borgiowie: Haki offset {off:+d}")
    if "kt_frags_offset" in rule_params:
        off = rule_params["kt_frags_offset"]
        vic_cfg["kabala_toledo"]["fragments"] = _apply_offset_to_item(vic_cfg["kabala_toledo"]["fragments"], off, min_val=1)
        descriptions.append(f"Kabała Toledo: Fragmenty Kodeksu offset {off:+d}")
    if "kt_era_offset" in rule_params:
        off = rule_params["kt_era_offset"]
        vic_cfg["kabala_toledo"]["era"] = _apply_offset_to_item(vic_cfg["kabala_toledo"]["era"], off, min_val=1)
        descriptions.append(f"Kabała Toledo: Era zwycięstwa offset {off:+d}")
    if "kt_heresy_band" in rule_params:
        band = list(rule_params["kt_heresy_band"])
        vic_cfg["kabala_toledo"]["heresy_band"] = band
        descriptions.append(f"Kabała Toledo: Pasmo Herezji {band[0]}–{band[1]}")
    if "gc_falls_offset" in rule_params:
        off = rule_params["gc_falls_offset"]
        vic_cfg["gildia_cieni"]["falls"] = _nudge_gc_falls(vic_cfg["gildia_cieni"]["falls"], off)
        descriptions.append(f"Gildia Cieni: Upadki offset {off:+d}")
    if "gc_falls_default_offset" in rule_params or "gc_falls_no_oficjum_offset" in rule_params:
        off = int(rule_params.get("gc_falls_default_offset", 0) or 0) + int(
            rule_params.get("gc_falls_no_oficjum_offset", 0) or 0
        )
        if off:
            vic_cfg["gildia_cieni"]["falls"] = _nudge_gc_falls(vic_cfg["gildia_cieni"]["falls"], off)
            descriptions.append(f"Gildia Cieni: Upadki (złożony offset) {off:+d}")

    # --- Level 3: Card Parameters (Supports multiple card overrides!) ---
    if "card_overrides" in rule_params:
        for cid, p_dict in rule_params["card_overrides"].items():
            for p_name, new_val in p_dict.items():
                if cid in cards_cfg:
                    c_name = cards_cfg[cid].get("name", cid)
                    cards_cfg[cid][p_name] = new_val
                    descriptions.append(f"Karta `{cid}` ({c_name}): `{p_name}` → `{new_val}`")
                else:
                    cards_cfg[cid] = {p_name: new_val}
                    descriptions.append(f"Karta `{cid}`: `{p_name}` → `{new_val}`")

    # --- Level 4: Variants & Economy ---
    if "card_cost_offset" in rule_params:
        eco_cfg = raw_cfg.setdefault("economy", {})
        eco_cfg["card_cost_offset"] = int(rule_params["card_cost_offset"])
        descriptions.append(f"Ekonomia: Offset kosztu kart = {eco_cfg['card_cost_offset']}")
    if "sig_cost_offset" in rule_params:
        eco_cfg = raw_cfg.setdefault("economy", {})
        eco_cfg["sig_cost_offset"] = int(rule_params["sig_cost_offset"])
        descriptions.append(f"Ekonomia: Offset kosztu sygnatur = {eco_cfg['sig_cost_offset']}")
    if "time_deck_freq" in rule_params:
        var_cfg["time_deck_freq"] = rule_params["time_deck_freq"]
        descriptions.append(f"Wariant: Częstotliwość Talii Czasu = co {var_cfg['time_deck_freq']} Erę")
    if "sea_route_era" in rule_params:
        var_cfg["sea_route_era"] = rule_params["sea_route_era"]
        descriptions.append(f"Wariant: Otwarcie Szlaku Morskiego = Era {var_cfg['sea_route_era']}")
    if "sea_route_era_offset" in rule_params:
        off = int(rule_params["sea_route_era_offset"])
        var_cfg["sea_route_era"] = max(1, int(var_cfg.get("sea_route_era", 4)) + off)
        descriptions.append(f"Wariant: Szlak Morski offset {off:+d} (nowy: Era {var_cfg['sea_route_era']})")
    if "inquisitor_speed" in rule_params:
        var_cfg["inquisitor_speed"] = rule_params["inquisitor_speed"]
        descriptions.append(f"Wariant: Prędkość Ruchu Inkwizytora = {var_cfg['inquisitor_speed']}")
    if "no_time_deck" in rule_params:
        var_cfg["no_time_deck"] = bool(rule_params["no_time_deck"])
        descriptions.append(f"Wariant: Kronika Dziejów wyłączona = {var_cfg['no_time_deck']}")

    desc = " + ".join(descriptions) if descriptions else f"Zastosowano regułę {rule_id}"
    return raw_cfg, desc


def save_config_and_bump_version(
    raw_cfg: dict[str, Any],
    config_path: Path | None = None,
    bump_version: bool = True,
) -> tuple[str, Path]:
    """Saves raw_cfg to YAML, optionally bumps version and updates date.
    Reloads CONFIG singleton and returns (new_version, config_path).
    """
    p = config_path or _CONFIG_PATH
    old_version = raw_cfg.get("version", "v0.19")

    if bump_version:
        new_version = bump_version_string(old_version)
        raw_cfg["version"] = new_version
    else:
        new_version = old_version

    raw_cfg["date"] = datetime.now().strftime("%Y-%m-%d")

    # Create backup before write
    backup_path = p.with_suffix(".yaml.bak")
    shutil.copy2(p, backup_path)

    with open(p, "w", encoding="utf-8") as f:
        yaml.safe_dump(
            raw_cfg,
            f,
            sort_keys=False,
            allow_unicode=True,
            default_flow_style=False,
        )

    # Reload singleton
    CONFIG.reload(p)
    return new_version, p
