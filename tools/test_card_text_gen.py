#!/usr/bin/env python3
"""Script to test generating card effect texts from game_config.yaml and comparing with actual card markdown files."""
import sys
from pathlib import Path

# Add repo root to path
REPO_ROOT = Path(__file__).resolve().parent.parent
SIM_DIR = REPO_ROOT / "sim"
sys.path.insert(0, str(SIM_DIR))

from inquisitio.cards.loader import load_all_cards
from inquisitio.config import CONFIG


def declension_pl(n: int, nom_sg: str, gen_sg: str, gen_pl: str) -> str:
    """Zwraca poprawną formę gramatyczną w języku polskim dla liczby n."""
    if n == 1:
        return nom_sg
    if 2 <= n % 10 <= 4 and not (12 <= n % 100 <= 14):
        return gen_sg
    return gen_pl


def format_card_text(cid: str, data: dict) -> str:
    """Generate canonical Leksykon effect text based purely on game_config.yaml data."""
    parts = []

    # 1. Signature / Rule Breaker Lead
    breaks = data.get("breaks_rule")
    decree = data.get("decree")
    if breaks:
        if decree:
            parts.append(f"DEKRET {decree} — Łamie regułę „{breaks}”:")
        else:
            parts.append(f"Łamie regułę „{breaks}”:")

    # 2. Trigger / Condition Lead
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

    # 3. Main Action Clauses
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
    elif act == "mark_fall":
        parts.append("Oznacz Upadek wobec tego rywala.")

    # 4. Limit Suffixes
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
        parts.append("Limit: bez ruchu Agenta w tej Erze.")
    elif lim_era == 1:
        parts.append("Limit: 1 / Erę.")

    return " ".join(parts).strip()


def main():
    cards_from_md = load_all_cards(force=True)
    cards_config = CONFIG.cards.raw()

    diffs = []
    matches = 0

    print("========================================================")
    print("ANALIZA ZGODNOŚCI TEKSTU WYGENEROWANEGO Z CONFIGU Z MARROW")
    print("========================================================\n")

    for cid in sorted(cards_config.keys()):
        cfg_card = cards_config[cid]
        md_card = cards_from_md.get(cid)

        if not md_card:
            print(f"⚠️ Karta {cid} brakująca w md!")
            continue

        generated = format_card_text(cid, cfg_card)
        actual = md_card.effect.replace("\n", " ").strip()
        # Normalization for spacing
        gen_norm = " ".join(generated.split())
        act_norm = " ".join(actual.split())

        if gen_norm == act_norm:
            matches += 1
        else:
            diffs.append((cid, cfg_card.get("name", cid), gen_norm, act_norm))

    print(f"Zgadzające się karty: {matches} / {len(cards_config)}")
    print(f"Różnice do przeanalizowania: {len(diffs)} / {len(cards_config)}\n")

    if diffs:
        print("────────────────────────────────────────────────────────")
        print("SZCZEGÓŁOWE RÓŻNICE (WYGENEROWANY TEKST vs OTRZYMANY Z KARTY)")
        print("────────────────────────────────────────────────────────\n")
        for cid, cname, gen, act in diffs:
            print(f"🃏 KARTA: `{cid.upper()}` ({cname})")
            print(f"   Wygenerowany z configu : {gen}")
            print(f"   Faktyczny tekst w pliku : {act}")
            print()

if __name__ == "__main__":
    main()
