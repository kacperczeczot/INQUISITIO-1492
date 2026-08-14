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


def apply_mutation_to_config(
    raw_cfg: dict[str, Any],
    rule_id: str,
    rule_params: dict[str, Any],
) -> tuple[dict[str, Any], str]:
    """Applies a rule's parameter override directly to the raw config dict.
    Returns (modified_raw_config, human_readable_description).
    """
    sys_cfg = raw_cfg.get("system", {})
    vic_cfg = raw_cfg.get("victory", {})
    var_cfg = raw_cfg.get("variants", {})
    cards_cfg = raw_cfg.get("cards", {})

    desc = f"Zastosowano regułę {rule_id}"

    # --- Level 1: System Parameters ---
    if "threshold_offset" in rule_params:
        off = rule_params["threshold_offset"]
        sys_cfg["accusation_threshold"] = _apply_offset_to_item(sys_cfg["accusation_threshold"], off, min_val=1)
        desc = f"Próg oskarżenia: offset {off:+d}"
    elif "max_eras_offset" in rule_params:
        off = rule_params["max_eras_offset"]
        sys_cfg["max_eras"] = max(1, sys_cfg.get("max_eras", 8) + off)
        desc = f"Limit Er: offset {off:+d} (nowy: {sys_cfg['max_eras']})"
    elif "start_gold_offset" in rule_params:
        off = rule_params["start_gold_offset"]
        sys_cfg["start_gold"] = _apply_offset_to_item(sys_cfg["start_gold"], off, min_val=1)
        desc = f"Startowe złoto: offset {off:+d}"
    elif "agents_offset" in rule_params:
        off = rule_params["agents_offset"]
        sys_cfg["agents_per_player"] = max(1, sys_cfg.get("agents_per_player", 3) + off)
        desc = f"Liczba agentów: offset {off:+d} (nowa: {sys_cfg['agents_per_player']})"
    elif "hand_limit_offset" in rule_params:
        off = rule_params["hand_limit_offset"]
        sys_cfg["hand_limit"] = _apply_offset_to_item(sys_cfg["hand_limit"], off, min_val=1)
        desc = f"Limit kart na ręce: offset {off:+d}"
    elif "cooldown_offset" in rule_params:
        off = rule_params["cooldown_offset"]
        sys_cfg["autodafe_cooldown"] = max(0, sys_cfg.get("autodafe_cooldown", 3) + off)
        desc = f"Cooldown Autodafé: offset {off:+d} (nowy: {sys_cfg['autodafe_cooldown']})"

    # --- Level 2: Victory Conditions ---
    elif "so_stacks_offset" in rule_params:
        off = rule_params["so_stacks_offset"]
        vic_cfg["swiete_oficjum"]["stacks"] = _apply_offset_to_item(vic_cfg["swiete_oficjum"]["stacks"], off, min_val=1)
        desc = f"Święte Oficjum: Stosy offset {off:+d}"
    elif "so_condemns_offset" in rule_params:
        off = rule_params["so_condemns_offset"]
        vic_cfg["swiete_oficjum"]["condemns"] = _apply_offset_to_item(vic_cfg["swiete_oficjum"]["condemns"], off, min_val=1)
        desc = f"Święte Oficjum: Skazania offset {off:+d}"
    elif "caa_relics_offset" in rule_params:
        off = rule_params["caa_relics_offset"]
        vic_cfg["cienie_al_andalus"]["relics"] = _apply_offset_to_item(vic_cfg["cienie_al_andalus"]["relics"], off, min_val=1)
        desc = f"Cienie Al-Andalus: Relikwie offset {off:+d}"
    elif "caa_era_offset" in rule_params:
        off = rule_params["caa_era_offset"]
        vic_cfg["cienie_al_andalus"]["path_era"] = _apply_offset_to_item(vic_cfg["cienie_al_andalus"]["path_era"], off, min_val=1)
        desc = f"Cienie Al-Andalus: Minimalna Era offset {off:+d}"
    elif "kb_era_offset" in rule_params:
        off = rule_params["kb_era_offset"]
        vic_cfg["korona_borgiowie"]["era"] = _apply_offset_to_item(vic_cfg["korona_borgiowie"]["era"], off, min_val=1)
        desc = f"Korona Borgiowie: Era zwycięstwa offset {off:+d}"
    elif "kb_decrees_offset" in rule_params:
        off = rule_params["kb_decrees_offset"]
        vic_cfg["korona_borgiowie"]["decrees"] = _apply_offset_to_item(vic_cfg["korona_borgiowie"]["decrees"], off, min_val=1)
        desc = f"Korona Borgiowie: Dekrety offset {off:+d}"
    elif "kb_hooks_offset" in rule_params:
        off = rule_params["kb_hooks_offset"]
        vic_cfg["korona_borgiowie"]["hooks"] = _apply_offset_to_item(vic_cfg["korona_borgiowie"]["hooks"], off, min_val=0)
        desc = f"Korona Borgiowie: Haki offset {off:+d}"
    elif "kt_frags_offset" in rule_params:
        off = rule_params["kt_frags_offset"]
        vic_cfg["kabala_toledo"]["fragments"] = _apply_offset_to_item(vic_cfg["kabala_toledo"]["fragments"], off, min_val=1)
        desc = f"Kabała Toledo: Fragmenty Kodeksu offset {off:+d}"
    elif "kt_era_offset" in rule_params:
        off = rule_params["kt_era_offset"]
        vic_cfg["kabala_toledo"]["era"] = _apply_offset_to_item(vic_cfg["kabala_toledo"]["era"], off, min_val=1)
        desc = f"Kabała Toledo: Era zwycięstwa offset {off:+d}"
    elif "kt_heresy_band" in rule_params:
        band = list(rule_params["kt_heresy_band"])
        vic_cfg["kabala_toledo"]["heresy_band"] = band
        desc = f"Kabała Toledo: Pasmo Herezji {band[0]}–{band[1]}"
    elif "gc_falls_offset" in rule_params:
        off = rule_params["gc_falls_offset"]
        vic_cfg["gildia_cieni"]["falls"]["default"] = max(1, vic_cfg["gildia_cieni"]["falls"]["default"] + off)
        vic_cfg["gildia_cieni"]["falls"]["no_oficjum"] = max(1, vic_cfg["gildia_cieni"]["falls"]["no_oficjum"] + off)
        desc = f"Gildia Cieni: Upadki offset {off:+d}"
    elif "gc_falls_default_offset" in rule_params:
        off = rule_params["gc_falls_default_offset"]
        vic_cfg["gildia_cieni"]["falls"]["default"] = max(1, vic_cfg["gildia_cieni"]["falls"]["default"] + off)
        desc = f"Gildia Cieni: Upadki (z Oficjum) offset {off:+d}"
    elif "gc_falls_no_oficjum_offset" in rule_params:
        off = rule_params["gc_falls_no_oficjum_offset"]
        vic_cfg["gildia_cieni"]["falls"]["no_oficjum"] = max(1, vic_cfg["gildia_cieni"]["falls"]["no_oficjum"] + off)
        desc = f"Gildia Cieni: Upadki (bez Oficjum) offset {off:+d}"

    # --- Level 3: Card Parameters ---
    elif "card_overrides" in rule_params:
        cid, p_dict = list(rule_params["card_overrides"].items())[0]
        p_name, new_val = list(p_dict.items())[0]
        if cid in cards_cfg:
            c_name = cards_cfg[cid].get("name", cid)
            cards_cfg[cid][p_name] = new_val
            desc = f"Karta `{cid}` ({c_name}): `{p_name}` → `{new_val}`"
        else:
            cards_cfg[cid] = {p_name: new_val}
            desc = f"Karta `{cid}`: `{p_name}` → `{new_val}`"

    # --- Level 4: Variants ---
    elif "time_deck_freq" in rule_params:
        var_cfg["time_deck_freq"] = rule_params["time_deck_freq"]
        desc = f"Wariant: Częstotliwość Talii Czasu = co {var_cfg['time_deck_freq']} Erę"
    elif "sea_route_era" in rule_params:
        var_cfg["sea_route_era"] = rule_params["sea_route_era"]
        desc = f"Wariant: Otwarcie Szlaku Morskiego = Era {var_cfg['sea_route_era']}"
    elif "inquisitor_speed" in rule_params:
        var_cfg["inquisitor_speed"] = rule_params["inquisitor_speed"]
        desc = f"Wariant: Prędkość Ruchu Inkwizytora = {var_cfg['inquisitor_speed']}"
    elif "verdict_secret" in rule_params:
        var_cfg["verdict_secret"] = bool(rule_params["verdict_secret"])
        desc = f"Wariant: Werdykt Tajny = {var_cfg['verdict_secret']}"

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
