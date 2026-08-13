#!/usr/bin/env python3
"""Synchronize game_config.yaml → documentation & engine.

Usage:
    sim/.venv/bin/python tools/sync_config.py

Reads game_config.yaml (Single Source of Truth) and propagates
values into:
  • docs/rules/ksiega.md  (CONFIG-marked sections)
  • playtesting/simulation_guide.md  (norm references)
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = PROJECT_ROOT / "game_config.yaml"

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def load_config() -> dict:
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


def _threshold_text(cfg: dict) -> str:
    t = cfg["system"]["accusation_threshold"]
    return f"**{t['3p']}** dla 3p oraz **{t['4p']}** dla 4–5p"


def _stacks_text(cfg: dict) -> str:
    s = cfg["victory"]["swiete_oficjum"]["stacks"]
    return f"**{s['3p']} Stosy**@3p / **{s['4p']} Stosy**@4p / **{s['5p']} Stosów**@5p"


def _condemns_text(cfg: dict) -> str:
    c = cfg["victory"]["swiete_oficjum"]["condemns"]
    return f"**{c['3p']}** przy 3p, **{c['4p']}** przy 4p, **{c['5p']}** przy 5p"


def _relics_text(cfg: dict) -> str:
    r = cfg["victory"]["cienie_al_andalus"]["relics"]
    p = cfg["victory"]["cienie_al_andalus"]["path_era"]
    return (
        f"**{r} Relikwie** + ścieżka "
        f"(Podwójny / cichy exit / szlak morski / Era {p['3p']}+ przy 3p / Era {p['4p']}+ przy 4–5p)"
    )


def _korona_text(cfg: dict) -> str:
    kb = cfg["victory"]["korona_borgiowie"]
    d3 = kb["decrees"]["3p"]
    e3, e4, e5 = kb["era"]["3p"], kb["era"]["4p"], kb["era"]["5p"]
    h3, h4 = kb["hooks"]["3p"], kb["hooks"]["4p"]
    alt = kb["alt_path"]
    if e3 == e4 == e5:
        era = f"od Ery **{e3}**"
    else:
        era = f"od Ery **{e3}**@3p / **{e4}**@4–5p"
    return (
        f"**{d3}** Dekrety ({era}; 3p ≥{h3} Haków / 4–5p ≥{h4} Hak); "
        f"na **4–5p** też {alt['decrees']} Dekret + {alt['hooks']} Haki od Ery {alt['era']}"
    )


def _kabala_text(cfg: dict) -> str:
    kt = cfg["victory"]["kabala_toledo"]
    f3, f4, f5 = kt["fragments"]["3p"], kt["fragments"]["4p"], kt["fragments"]["5p"]
    e3, e4 = kt["era"]["3p"], kt["era"]["4p"]
    hb = kt["heresy_band"]
    if f3 == f4 == f5:
        frags = f"**{f3} Fragmenty**"
    else:
        frags = f"**{f3}**@3p / **{f4}**@4p / **{f5}**@5p Fragmenty"
    return (
        f"{frags} + Herezja **{hb[0]}–{hb[1]}** "
        f"(od Ery **{e3}**@3p / **{e4}**@4–5p)"
    )


def _gildia_text(cfg: dict) -> str:
    gc = cfg["victory"]["gildia_cieni"]["falls"]
    return (
        f"**{gc['default']} upadki** (Hak / Podwójny / Autodafé lokacji kluczowej / Werdykt na celu z Hakiem); "
        f"**{gc['no_oficjum']}** gdy brak Oficjum"
    )


def _victory_table(cfg: dict) -> str:
    """Generate the victory conditions table for ksiega.md."""
    return f"""| Frakcja | Warunek (C — stół) |
| :--- | :--- |
| Święte Oficjum | {_stacks_text(cfg)} **lub** skazania Werdyktem ({_condemns_text(cfg)}) |
| Cienie Al-Andalus | {_relics_text(cfg)} |
| Korona | {_korona_text(cfg)} |
| Kabała | {_kabala_text(cfg)} |
| Gildia | {_gildia_text(cfg)} |"""


def _heresy_table(cfg: dict) -> str:
    """Generate heresy zones table."""
    hz = cfg["heresy_zones"]
    c = hz["clean"]
    o3 = hz["observed"]["3p"]
    o4 = hz["observed"]["4p_plus"]
    cr3 = hz["critical"]["3p"]
    cr4 = hz["critical"]["4p_plus"]
    return f"""| Zakres | Strefa | Skutek |
| :---: | :--- | :--- |
| {c[0]}–{c[1]} | Czysta | Bezpieczniej, słabsze akcje |
| {o3[0]}–{o3[1]}@3p / {o4[0]}–{o4[1]}@4–5p | Obserwowana | Ryzyko; Kabała lubi ten pas |
| ≥{cr3}@3p / ≥{cr4}@4–5p | **Krytyczna** | Inni mogą **Rzucić Oskarżenie** |"""


def _balance_rule(cfg: dict) -> str:
    """Generate the balance rule text."""
    t = cfg["system"]["accusation_threshold"]
    return f"**Zasada Balansu:** próg oskarżenia wynosi {_threshold_text(cfg)} (zatwierdzone w raportach sim-reports)."


def _system_summary(cfg: dict) -> str:
    s = cfg["system"]
    return f"""**Parametry systemowe:** Złoto startowe: **{s['start_gold']}** | Agenci: **{s['agents_per_player']}** | Limit ręki: **{s['hand_limit']}** | Max Er: **{s['max_eras']}** | Autodafé cooldown: co **{s['autodafe_cooldown']}** Ery | Karty/Erę: **{s['cards_per_era']}**"""


def sync_ksiega(cfg: dict) -> list[str]:
    """Replace CONFIG-marked sections in ksiega.md."""
    ksiega_path = PROJECT_ROOT / "docs" / "rules" / "ksiega.md"
    text = ksiega_path.read_text(encoding="utf-8")
    changes: list[str] = []

    # Replace victory table
    old_victory_pattern = re.compile(
        r"(\| Frakcja \| Warunek.*?\n(?:\| :---.*?\n)?)"
        r"(\| Święte Oficjum \|.*?\n)"
        r"(\| Cienie Al-Andalus \|.*?\n)"
        r"(\| Korona \|.*?\n)"
        r"(\| Kabała \|.*?\n)"
        r"(\| Gildia \|.*?\n)",
        re.MULTILINE
    )
    new_victory = _victory_table(cfg) + "\n"
    if old_victory_pattern.search(text):
        text = old_victory_pattern.sub(new_victory, text)
        changes.append("Tabela Zwycięstwa zaktualizowana")

    # Replace heresy zones table
    old_heresy_pattern = re.compile(
        r"(\| Zakres \| Strefa \| Skutek \|\n"
        r"\| :---:.*?\n)"
        r"(\| 0–3 \|.*?\n)"
        r"(\| 4–.*?\n)"
        r"(\| ≥.*?\n)",
        re.MULTILINE
    )
    new_heresy = _heresy_table(cfg) + "\n"
    if old_heresy_pattern.search(text):
        text = old_heresy_pattern.sub(new_heresy, text)
        changes.append("Tabela Herezji zaktualizowana")

    # Replace balance rule
    old_balance_pattern = re.compile(r"\*\*Zasada Balansu:\*\*.*$", re.MULTILINE)
    new_balance = _balance_rule(cfg)
    if old_balance_pattern.search(text):
        text = old_balance_pattern.sub(new_balance, text)
        changes.append("Reguła Balansu zaktualizowana")

    # Replace setup section values
    gold_pattern = re.compile(r"Złoto startowe: \*\*\d+\*\*")
    text = gold_pattern.sub(f"Złoto startowe: **{cfg['system']['start_gold']}**", text)

    hand_pattern = re.compile(r"Dobierz \*\*\d+\*\* kart")
    text = hand_pattern.sub(f"Dobierz **{cfg['system']['hand_limit']}** kart", text)

    limit_pattern = re.compile(r"Dobierz karty do limitu ręki \*\*\d+\*\*")
    text = limit_pattern.sub(f"Dobierz karty do limitu ręki **{cfg['system']['hand_limit']}**", text)

    # Replace "Limit Er" in freeze table
    limit_er_pattern = re.compile(r"(\d+) Er; najbliższy cel")
    text = limit_er_pattern.sub(f"{cfg['system']['max_eras']} Er; najbliższy cel", text)

    # Replace autodafe cooldown
    autodafe_pattern = re.compile(r"max \*\*co \d+ Ery\*\*")
    text = autodafe_pattern.sub(f"max **co {cfg['system']['autodafe_cooldown']} Ery**", text)

    # Replace cards per era
    cards_pattern = re.compile(r"\*\*do \d+\*\* \(zagranie lub pas\)")
    text = cards_pattern.sub(f"**do {cfg['system']['cards_per_era']}** (zagranie lub pas)", text)

    ksiega_path.write_text(text, encoding="utf-8")
    if changes:
        changes.append(f"+ inline parametry (złoto, limit ręki, Er, autodafé, karty/erę)")
    else:
        changes.append("Inline parametry zsynchronizowane")
    return changes


def sync_teach_sheet(cfg: dict) -> list[str]:
    """Sync teach-sheet.md with game_config.yaml."""
    path = PROJECT_ROOT / "docs" / "rules" / "teach-sheet.md"
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    t = cfg["system"]["accusation_threshold"]
    hz = cfg["heresy_zones"]
    c, o3, o4 = hz["clean"], hz["observed"]["3p"], hz["observed"]["4p_plus"]
    cr3, cr4 = hz["critical"]["3p"], hz["critical"]["4p_plus"]

    # Accusation rule
    text = re.sub(
        r"1\. Cel w Krytycznej \(≥.*?\)\.",
        f"1. Cel w Krytycznej (≥{t['3p']} w 3p, ≥{t['4p']} w 4–5p).",
        text
    )

    # Max eras
    text = re.sub(
        r"Limit: \d+ Er",
        f"Limit: {cfg['system']['max_eras']} Er",
        text
    )

    cd = cfg["system"]["autodafe_cooldown"]
    text = re.sub(r"Autodafé \(max co \d+ Ery\)", f"Autodafé (max co {cd} Ery)", text)
    text = re.sub(r"Autodafé max \*\*co \d+ Ery\*\*", f"Autodafé max **co {cd} Ery**", text)

    path.write_text(text, encoding="utf-8")
    return ["Zsynchronizowano docs/rules/teach-sheet.md"]


def sync_hierarchia(cfg: dict) -> list[str]:
    """Sync hierarchia_balansowania.md with game_config.yaml."""
    path = PROJECT_ROOT / "docs" / "rules" / "hierarchia_balansowania.md"
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    s = cfg["system"]
    t = s["accusation_threshold"]
    hz = cfg["heresy_zones"]
    o3, o4 = hz["observed"]["3p"], hz["observed"]["4p_plus"]
    cr3, cr4 = hz["critical"]["3p"], hz["critical"]["4p_plus"]

    text = re.sub(r"- \*\*Maksymalny limit Er:\*\* `\d+ Er`", f"- **Maksymalny limit Er:** `{s['max_eras']} Er`", text)
    text = re.sub(
        r"- \*\*Obserwowana:\*\* `.*?`",
        f"- **Obserwowana:** `{o3[0]}–{o3[1]} Herezji (3p) / {o4[0]}–{o4[1]} (4–5p)`",
        text
    )
    text = re.sub(
        r"- \*\*Krytyczna / Heretyk:\*\* `.*?`",
        f"- **Krytyczna / Heretyk:** `{cr3}–10 Herezji (3p) / {cr4}–10 (4–5p)`",
        text
    )
    text = re.sub(
        r"- \*\*Próg Oskarżenia na Dworze:\*\* `.*?`",
        f"- **Próg Oskarżenia na Dworze:** `Herezja ≥ {t['3p']} (3p) / ≥ {t['4p']} (4–5p)`",
        text
    )
    text = re.sub(
        r"- \*\*Cooldown Autodafé Inkwizytora:\*\* Max `co \d+ Ery`",
        f"- **Cooldown Autodafé Inkwizytora:** Max `co {s['autodafe_cooldown']} Ery`",
        text
    )

    path.write_text(text, encoding="utf-8")
    return ["Zsynchronizowano docs/rules/hierarchia_balansowania.md"]


def sync_setups(cfg: dict) -> list[str]:
    """Sync setups.md with game_config.yaml."""
    path = PROJECT_ROOT / "playtesting" / "setups.md"
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    s = cfg["system"]
    t = s["accusation_threshold"]

    text = re.sub(
        r"\| Próg Krytycznej \(Oskarżenie\) \| \*\*\d+\*\* \| \*\*\d+\*\* \|",
        f"| Próg Krytycznej (Oskarżenie) | **{t['3p']}** | **{t['4p']}** |",
        text
    )
    text = re.sub(
        r"\| Limit Er \| \*\*\d+\*\* \| \*\*\d+\*\* \|",
        f"| Limit Er | **{s['max_eras']}** | **{s['max_eras']}** |",
        text
    )

    path.write_text(text, encoding="utf-8")
    return ["Zsynchronizowano playtesting/setups.md"]


def sync_cards(cfg: dict) -> list[str]:
    """Sync card markdown files (parameters + effect text), KATALOG.md, and card-editor.html from game_config.yaml."""
    from tools.pnp.generate_card_text import sync_card_markdowns
    from tools.cards.build_catalog import main as build_catalog_main
    from tools.pnp.sync_card_editor import main as sync_card_editor_main

    # 1. Sync card parameters (cost, layer, type) & effect text
    updated_files = sync_card_markdowns(dry_run=False)

    # 2. Rebuild KATALOG.md
    build_catalog_main()

    # 3. Sync card-editor.html CARDS_DATABASE
    sync_card_editor_main()

    res = [f"Zsynchronizowano {len(cfg.get('cards', {}))} kart w game/cards/"]
    if updated_files:
        res.append(f"Zaktualizowano opisy efektów dla {len(updated_files)} kart")
    res.append("Przegenerowano game/cards/KATALOG.md")
    res.append("Zsynchronizowano baza kart w card-editor.html")
    return res


def main():
    print("═══════════════════════════════════════════════════════")
    print("INQUISITIO-1492 — SYNCHRONIZACJA KONFIGURACJI")
    print("═══════════════════════════════════════════════════════\n")

    cfg = load_config()

    # Summary of current values
    s = cfg["system"]
    print(f"📋 Odczytano game_config.yaml:")
    print(f"   • Złoto startowe: {s['start_gold']}")
    print(f"   • Agenci: {s['agents_per_player']}")
    print(f"   • Limit ręki: {s['hand_limit']}")
    print(f"   • Max Er: {s['max_eras']}")
    print(f"   • Autodafé cooldown: co {s['autodafe_cooldown']} Ery")
    print(f"   • Próg Oskarżenia: {s['accusation_threshold']}")
    print()

    v = cfg["victory"]
    print(f"   ⚔️ Oficjum: Stosy {v['swiete_oficjum']['stacks']} | Skazania {v['swiete_oficjum']['condemns']}")
    print(f"   ⚔️ Cienie: {v['cienie_al_andalus']['relics']} Relikwii | Ery {v['cienie_al_andalus']['path_era']}")
    print(f"   ⚔️ Korona: Dekrety {v['korona_borgiowie']['decrees']} | Haki {v['korona_borgiowie']['hooks']} | Ery {v['korona_borgiowie']['era']}")
    print(f"   ⚔️ Kabała: Fragmenty {v['kabala_toledo']['fragments']} | Herezja {v['kabala_toledo']['heresy_band']} | Ery {v['kabala_toledo']['era']}")
    print(f"   ⚔️ Gildia: Upadki {v['gildia_cieni']['falls']}")
    print()

    # Sync docs & cards
    print("📝 Synchronizuję dokumentację i pliki kart z game_config.yaml...")
    for ch in sync_ksiega(cfg):
        print(f"   ✅ {ch}")
    for ch in sync_teach_sheet(cfg):
        print(f"   ✅ {ch}")
    for ch in sync_hierarchia(cfg):
        print(f"   ✅ {ch}")
    for ch in sync_setups(cfg):
        print(f"   ✅ {ch}")
    for ch in sync_cards(cfg):
        print(f"   ✅ {ch}")

    print()
    print("═══════════════════════════════════════════════════════")
    print("✅ KONFIGURACJA ZSYNCHRONIZOWANA DLA WSZYSTKICH PLIKÓW I KART!")
    print("═══════════════════════════════════════════════════════")
    print()
    print("Następne kroki:")
    print("  1. Sprawdź zmiany: git diff docs/ game/cards/ playtesting/")
    print("  2. Uruchom testy: sim/.venv/bin/pytest sim/tests/ -q")


if __name__ == "__main__":
    main()


