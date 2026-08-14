#!/usr/bin/env python3
"""
Generator Tekstów Kart na podstawie game_config.yaml.
Przekształca deklaratywną specyfikację mechaniki z game_config.yaml na kanoniczne zdania Leksykonu z gramatyczną odmianą PL.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

# Add repo root to path
REPO_ROOT = Path(__file__).resolve().parents[2]
SIM_DIR = REPO_ROOT / "sim"
sys.path.insert(0, str(SIM_DIR))

import yaml
from inquisitio.config import CONFIG


def declension_pl(n: int, nom_sg: str, gen_sg: str, gen_pl: str) -> str:
    """Zwraca poprawną formę gramatyczną w języku polskim dla liczby n."""
    if n == 1:
        return nom_sg
    if 2 <= n % 10 <= 4 and not (12 <= n % 100 <= 14):
        return gen_sg
    return gen_pl


def generate_card_effect_text(cid: str, data: dict[str, Any]) -> str:
    """
    Generuje kanoniczny tekst efektu na kartę w języku polskim na podstawie wpisu w game_config.yaml.
    """
    parts: list[str] = []

    # 1. Nagłówek dla kart Specjalnych (Signature) oraz Łamiących Reguły
    breaks = data.get("breaks_rule")
    decree = data.get("decree")
    if breaks:
        if decree:
            parts.append(f"DEKRET {decree} — Łamie regułę „{breaks}”:")
        else:
            parts.append(f"Łamie regułę „{breaks}”:")

    # 2. Wstęp z Warunkiem (Condition) lub Triggerem Reakcji
    trigger = data.get("trigger")
    condition = data.get("condition")

    if trigger == "rival_plays_heresy_gte_1":
        parts.append("Jeśli rywal zagrywa kartę z Herezją ≥ 1:")
    elif trigger == "after_verdict_majority_revealed":
        parts.append("Podczas Werdyktu, po ujawnieniu większości:")

    if condition == "relic_present":
        parts.append("Jeśli masz Agenta w lokacji z Relikwią:")
    elif condition == "has_double_agent":
        parts.append("Jeśli masz Podwójnego:")
    elif condition == "agent_in_dungeon_or_tribunal":
        parts.append("Jeśli masz Agenta w Lochach lub Trybunale:")
    elif condition == "fragments_eq_3":
        parts.append("Jeśli masz 3 Fragmenty")
    elif condition == "active_hooks_gte_2":
        parts.append("Jeśli masz aktywne Haki na ≥ 2 graczach:")
    elif condition == "no_inquisitor_or_double_or_sea_route":
        parts.append("Jeśli nie ma Inkwizytora w lokacji lub masz Podwójnego lub Szlak jest otwarty:")
    elif condition == "has_fragment_and_agent_in_dungeon_or_tribunal":
        parts.append("Jeśli masz ≥1 Fragment i Agenta w Lochach lub Trybunale:")
    elif condition == "rival_has_hook_or_double_or_autodafe":
        parts.append("Jeśli rywal ma ujawniony Hak, Podwójnego lub Autodafé w lokacji kluczowej:")

    # 3. Główne Zestawienie Komend Akcji
    act = data.get("action")
    tloc = data.get("target_loc")
    gold = data.get("gold")
    agents = data.get("agents")
    theresy = data.get("target_heresy")

    if act == "move_agent":
        if data.get("free_agent"):
            if agents == 1:
                parts.append("Uwolnij swojego aresztowanego Agenta z Lochów. Przesuń tego Agenta o 1 lokację.")
            else:
                parts.append("Uwolnij swojego aresztowanego Agenta z Lochów.")
        elif condition == "has_double_agent":
            parts.append("Przesuń tego Podwójnego o 1 lokację.")
        elif data.get("move_relic"):
            parts.append("Przenieś Relikwię z lokacji swojego Agenta do sąsiedniej lokacji.")
        elif agents == 1:
            parts.append("Przesuń swojego Agenta o 1 lokację.")
        elif agents and agents > 1:
            noun = declension_pl(agents, "lokację", "lokacje", "lokacji")
            parts.append(f"Przesuń swojego Agenta o {agents} {noun}.")
        else:
            parts.append("Przesuń swojego Agenta o 1 lokację.")
    elif act == "gain_gold":
        if gold == 1:
            parts.append("Zyskaj złoto.")
        elif gold and gold >= 2:
            noun = declension_pl(gold, "złoto", "złota", "złota")
            parts.append(f"Zyskaj {gold} {noun}.")
        if theresy:
            parts.append(f"Wskaż rywala: +{theresy} Herezja.")
    elif act == "frame_rival":
        if data.get("change_vote"):
            parts.append("Zmień swój głos.")
        else:
            tscope = data.get("target_scope")
            prefix = "Wskaż tego rywala:" if tscope == "triggering_rival" else "Wskaż rywala:"
            if theresy == 1:
                parts.append(f"{prefix} +1 Herezja.")
            elif theresy and theresy > 1:
                parts.append(f"{prefix} +{theresy} Herezja.")
    elif act == "send_inquisitor":
        if tloc == "agent_location":
            parts.append("Przesuń Inkwizytora o 1 lokację w stronę lokacji swojego Agenta.")
        elif tloc == "same_location":
            parts.append("Przesuń Inkwizytora do lokacji ze swoim Agentem.")
        else:
            parts.append("Przesuń Inkwizytora.")
    elif act == "arrest":
        if tloc == "same_location":
            parts.append("Aresztuj Agenta rywala w lokacji swojego Agenta.")
        elif tloc == "palace_or_same_location":
            parts.append("Aresztuj Agenta rywala w Pałacu lub w lokacji ze swoim Agentem.")
        elif tloc == "dungeon_or_tribunal":
            parts.append("Aresztuj Agenta rywala w Lochach lub w Trybunale.")
        elif tloc == "guild_or_market":
            parts.append("Aresztuj Agenta rywala w Gildii lub na Rynku.")
        else:
            parts.append("Aresztuj Agenta rywala.")
    elif act == "interrogate":
        if tloc == "dungeon":
            parts.append("Wykonaj Przesłuchanie na aresztowanego Agenta rywala.")
        elif data.get("bonus_on_heresy") == "grant_fragment":
            parts.append("Wykonaj Przesłuchanie. Jeśli +2 Herezja lub Hak: Zyskaj Fragment.")
        else:
            parts.append("Wykonaj Przesłuchanie.")
    elif act == "creates_hook":
        if data.get("mark_fall") and condition == "rival_has_hook_or_double_or_autodafe":
            parts.append("Oznacz Upadek wobec tego rywala.")
        elif data.get("penalty_heresy"):
            pen = data.get("penalty_heresy", 3)
            parts.append(f"Wymuś spełnienie Haka. Odmowa: +{pen} Herezja.")
        elif condition == "rival_in_dungeon_or_inquisitor":
            parts.append("Załóż Hak na rywala z Agentem w Lochach lub w lokacji Inkwizytora.")
        elif condition == "heresy_gte_4":
            parts.append("Załóż Hak na rywala z Herezją ≥ 4.")
        elif tloc == "neighbor_location":
            parts.append("Załóż Hak na rywala z Agentem w sąsiedniej lokacji swojego Agenta.")
        elif data.get("verdict_weight") == 2:
            parts.append("W następnym Werdykcie Twój głos ma wagę 2. Załóż Hak na rywala.")
        elif agents == 1:
            parts.append("Przesuń swojego Agenta o 1 lokację. Załóż Hak na rywala.")
        else:
            parts.append("Załóż Hak na rywala.")

        if data.get("on_refusal") == "mark_fall":
            parts.append("Jeśli Odmowa tego Haka w tej Erze: Oznacz Upadek wobec tego rywala.")
    elif act == "autodafe":
        parts.append("Ogłoś Autodafé w lokacji Inkwizytora. Jeśli Agent rywala jest w lokacji Inkwizytora: Zyskaj Stos.")
    elif act == "evacuate_relic":
        if data.get("max_relics") == 2:
            parts.append("Ewakuuj do 2 Relikwii z lokacji Twoich Agentów.")
        else:
            parts.append("Ewakuuj Relikwię z tej lokacji.")
    elif act == "check_victory":
        band = data.get("target_heresy_band")
        fb = data.get("fallback_heresy")
        if band and fb:
            parts.append(f"i Herezję {band[0]}–{band[1]}: zwycięstwo. Jeśli masz 3 Fragmenty bez Herezji {band[0]}–{band[1]}: Ustaw swoją Herezję na {fb}.")
        else:
            parts.append("zwycięstwo.")
    elif act == "grant_fragment":
        parts.append("Zyskaj Fragment.")
        if condition == "agent_in_dungeon_or_tribunal":
            parts.append("Jeśli nie masz Agenta w Lochach lub Trybunale: Zyskaj złoto.")

    # 4. Zwroty Limitów Anti-AP
    inq_lim = data.get("inquisitor_send_limit")
    int_lim = data.get("interrogate_limit")
    kur_lim = data.get("kurier_limit")
    vote_lim = data.get("vote_change_limit")
    lim_era = data.get("limit_per_era")
    no_move_lim = data.get("no_move_limit")

    if inq_lim == 1:
        parts.append("Limit: 1 nasłanie / gracza / Erę.")
    elif int_lim == 1:
        if cid == "so-07":
            parts.append("Limit: 1 / gracza / Erę.")
        else:
            parts.append("Limit: 1 / Erę.")
    elif kur_lim == 1 or vote_lim == 1:
        parts.append("Limit: 1 / Erę.")
    elif no_move_lim:
        parts.append("Limit: bez Przesuń z karty / tę Erę.")
    elif lim_era == 1:
        parts.append("Limit: 1 / Erę.")

    return " ".join(parts).strip()


def sync_card_markdowns(dry_run: bool = True) -> list[str]:
    """
    Aktualizuje pole `effect:` w plikach markdown kart (game/cards/) wygenerowanym tekstem z game_config.yaml.
    """
    cards_config = CONFIG.cards.raw()
    cards_dir = REPO_ROOT / "game" / "cards"
    updated_files = []

    for path in cards_dir.rglob("*.md"):
        if path.name.upper() in ("SCHEMA.MD", "KATALOG.MD", "README.MD"):
            continue
        content = path.read_text(encoding="utf-8")
        parts = content.split("---")
        if len(parts) < 3:
            continue
        try:
            meta = yaml.safe_load(parts[1])
            if not isinstance(meta, dict) or "id" not in meta:
                continue
            cid = str(meta["id"])
            if cid not in cards_config:
                continue

            cfg_card = cards_config[cid]
            gen_text = generate_card_effect_text(cid, cfg_card)
            curr_text = str(meta.get("effect") or "").strip()

            cfg_cost = cfg_card.get("cost", meta.get("cost", 0))
            cfg_heresy = cfg_card.get("heresy", meta.get("heresy", 0))
            cfg_type = cfg_card.get("type", meta.get("type", "akcja"))
            cfg_layer = cfg_card.get("layer", meta.get("layer", "A"))

            param_changed = (
                meta.get("cost") != cfg_cost
                or meta.get("heresy") != cfg_heresy
                or meta.get("type") != cfg_type
                or meta.get("layer") != cfg_layer
                or gen_text != curr_text
            )

            if param_changed:
                meta["cost"] = cfg_cost
                meta["heresy"] = cfg_heresy
                meta["type"] = cfg_type
                meta["layer"] = cfg_layer
                meta["effect"] = gen_text
                if not dry_run:
                    clean_meta = {}
                    for k in ["id", "name", "faction", "type", "layer", "cost", "heresy"]:
                        if k in meta:
                            clean_meta[k] = meta[k]
                    if "tags" in cfg_card:
                        clean_meta["tags"] = cfg_card["tags"]
                    elif meta.get("tags"):
                        clean_meta["tags"] = meta["tags"]
                    if meta.get("effect"):
                        clean_meta["effect"] = meta["effect"]
                    if meta.get("heresy_text"):
                        clean_meta["heresy_text"] = meta["heresy_text"]
                    if meta.get("lore"):
                        clean_meta["lore"] = meta["lore"]
                    for flag in ["target_heresy", "agents", "gold"]:
                        if meta.get(flag):
                            clean_meta[flag] = meta[flag]
                    for flag in ["creates_hook", "breaks_rule", "arrest"]:
                        val = meta.get(flag)
                        if val:
                            clean_meta[flag] = val

                    new_yaml = yaml.dump(clean_meta, allow_unicode=True, sort_keys=False)
                    new_content = f"---\n{new_yaml}---\n" + "---".join(parts[2:])
                    path.write_text(new_content, encoding="utf-8")
                updated_files.append(f"{cid} (cost:{meta.get('cost')}, heresy:{meta.get('heresy')}): {curr_text} -> {gen_text}")
        except Exception as e:
            print(f"Error processing {path}: {e}")

    return updated_files


def main():
    dry_run = "--apply" not in sys.argv
    print("========================================================")
    print(f"GENERATOR TEKSTÓW KART (Dry Run = {dry_run})")
    print("========================================================\n")

    changes = sync_card_markdowns(dry_run=dry_run)
    if dry_run:
        print(f"Liczba kart wymagających aktualizacji tekstu: {len(changes)}")
        for ch in changes:
            print(f"  • {ch}")
        print("\nAby zapisać zmiany w plikach .md, uruchom:")
        print("  sim/.venv/bin/python tools/pnp/generate_card_text.py --apply")
    else:
        print(f"✅ Zaktualizowano {len(changes)} plików kart .md z game_config.yaml!")


if __name__ == "__main__":
    main()
