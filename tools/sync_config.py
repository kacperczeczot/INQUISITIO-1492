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
    if isinstance(t, dict):
        return f"**{t['3p']}** dla 3p, **{t['4p']}** dla 4p, **{t['5p']}** dla 5p"
    return f"**{t}**"


def _stacks_text(cfg: dict) -> str:
    s = cfg["victory"]["swiete_oficjum"]["stacks"]
    if isinstance(s, dict):
        return f"**{s['3p']} Stosy**@3p / **{s['4p']} Stosy**@4–5p"
    return f"**{s} Stosy**"


def _condemns_text(cfg: dict) -> str:
    c = cfg["victory"]["swiete_oficjum"]["condemns"]
    if isinstance(c, dict):
        if c["3p"] == c["4p"] == c["5p"]:
            return f"**{c['3p']}** Skazania"
        return f"**{c['3p']}** przy 3p, **{c['4p']}** przy 4–5p"
    return f"**{c} Skazania**"


def _relics_text(cfg: dict) -> str:
    r = cfg["victory"]["cienie_al_andalus"]["relics"]
    p = cfg["victory"]["cienie_al_andalus"]["path_era"]
    if isinstance(p, dict):
        p_era = f"Era {p['3p']}+ przy 3p / Era {p['4p']}+ przy 4–5p" if p["3p"] != p["4p"] else f"Era {p['3p']}+"
    else:
        p_era = f"Era {p}+"
    return f"**{r} Relikwie** + ścieżka (Podwójny / cichy exit / szlak morski / {p_era})"


def _korona_text(cfg: dict) -> str:
    kb = cfg["victory"]["korona_borgiowie"]
    d = kb["decrees"]
    d_val = d["3p"] if isinstance(d, dict) else d
    e = kb["era"]
    e_val = e["3p"] if isinstance(e, dict) else e
    return f"**{d_val}** Dekrety (od Ery **{e_val}**)"


def _kabala_text(cfg: dict) -> str:
    kt = cfg["victory"]["kabala_toledo"]
    f = kt["fragments"]
    f_val = f["3p"] if isinstance(f, dict) else f
    e = kt["era"]
    if isinstance(e, dict):
        e_text = f"od Ery **{e['3p']}**@3p / **{e['4p']}**@4–5p" if e["3p"] != e["4p"] else f"od Ery **{e['3p']}**"
    else:
        e_text = f"od Ery **{e}**"
    hb = kt["heresy_band"]
    return f"**{f_val} Fragmenty** + Herezja **{hb[0]}–{hb[1]}** ({e_text})"


def _gildia_text(cfg: dict) -> str:
    gc = cfg["victory"]["gildia_cieni"]["falls"]
    return (
        f"**{gc['default']} upadki** (Hak / Podwójny / Autodafé lokacji kluczowej / Werdykt na celu z Hakiem); "
        f"**{gc['no_oficjum']}** gdy brak Oficjum"
    )


def _victory_table(cfg: dict) -> str:
    """Generate the victory conditions table for Kanon 4p."""
    v = cfg["victory"]
    so_s = v["swiete_oficjum"]["stacks"]
    so_stacks = so_s["4p"] if isinstance(so_s, dict) else so_s
    so_c = v["swiete_oficjum"]["condemns"]
    so_condemns = so_c["4p"] if isinstance(so_c, dict) else so_c

    caa_r = v["cienie_al_andalus"]["relics"]
    caa_p = v["cienie_al_andalus"]["path_era"]
    caa_era = caa_p["4p"] if isinstance(caa_p, dict) else caa_p

    kb_d = v["korona_borgiowie"]["decrees"]
    kb_dec = kb_d["4p"] if isinstance(kb_d, dict) else kb_d
    kb_e = v["korona_borgiowie"]["era"]
    kb_era = kb_e["4p"] if isinstance(kb_e, dict) else kb_e

    kt_f = v["kabala_toledo"]["fragments"]
    kt_frag = kt_f["4p"] if isinstance(kt_f, dict) else kt_f
    kt_hb = v["kabala_toledo"]["heresy_band"]
    kt_e = v["kabala_toledo"]["era"]
    kt_era = kt_e["4p"] if isinstance(kt_e, dict) else kt_e

    gc_f = v["gildia_cieni"]["falls"]

    return f"""| Frakcja | Warunek Zwycięstwa (Kanon 4p) |
| :--- | :--- |
| **Święte Oficjum** | **{so_stacks} Stosy** (spaleni agenci) **lub {so_condemns} Skazania** Werdyktem |
| **Cienie Al-Andalus** | **{caa_r} Relikwie** + ścieżka (Podwójny / cichy exit / szlak morski / Era {caa_era}+) |
| **Korona & Borgiowie** | **{kb_dec} Dekrety** (od Ery **{kb_era}**) |
| **Kabała z Toledo** | **{kt_frag} Fragmenty** + Herezja **{kt_hb[0]}–{kt_hb[1]}** (od Ery **{kt_era}**) |
| **Gildia Cieni** | **{gc_f['default']} Upadki** (Hak / Podwójny / Autodafé / Werdykt na celu z Hakiem); **{gc_f['no_oficjum']}** gdy brak Oficjum |"""


def _heresy_table(cfg: dict) -> str:
    """Generate heresy zones table for Kanon 4p."""
    s = cfg["system"]
    t = s["accusation_threshold"]
    t4 = t["4p"] if isinstance(t, dict) else t
    return f"""| Zakres | Strefa | Skutek |
| :---: | :--- | :--- |
| 0–3 | Czysta | Bezpieczniej, słabsze akcje |
| 4–{t4-1} | Obserwowana | Ryzyko; Kabała lubi ten pas |
| ≥{t4} | **Krytyczna** | Inni mogą **Rzucić Oskarżenie** |"""


def _scaling_box(cfg: dict) -> str:
    """Generate 3p and 5p player count scaling modifications box."""
    s = cfg["system"]
    v = cfg["victory"]

    t = s["accusation_threshold"]
    t3 = t["3p"] if isinstance(t, dict) else t
    t5 = t["5p"] if isinstance(t, dict) else t

    g = s["start_gold"]
    g5 = g["5p"] if isinstance(g, dict) else g

    so_s = v["swiete_oficjum"]["stacks"]
    so_s3 = so_s["3p"] if isinstance(so_s, dict) else so_s

    kt_e = v["kabala_toledo"]["era"]
    kt_e3 = kt_e["3p"] if isinstance(kt_e, dict) else kt_e

    return f"""> ### 👥 Modyfikacje dla 3 Graczy (3p):
> - **Próg Oskarżenia (Krytyczna Herezja):** **`{t3}`** (Strefy: Czysta `0–3` / Obserwowana `4–{t3-1}` / Krytyczna `≥{t3}`).
> - **Święte Oficjum:** Wymaga **`{so_s3} Stosów`** (zamiast 4).
> - **Kabała z Toledo:** Może wygrać od **`Ery {kt_e3}`** (zamiast 6).
>
> ### 👥 Modyfikacje dla 5 Graczy (5p):
> - **Złoto Startowe:** Każdy gracz otrzymuje na start **`{g5} zł`** (zamiast 3 zł).
> - **Próg Oskarżenia (Krytyczna Herezja):** **`{t5}`** (Strefy: Czysta `0–3` / Obserwowana `4–{t5-1}` / Krytyczna `≥{t5}`)."""


def _balance_rule(cfg: dict) -> str:
    """Generate the balance rule text."""
    t = cfg["system"]["accusation_threshold"]
    t4 = t["4p"] if isinstance(t, dict) else t
    return f"**Zasada Balansu:** bazowy próg oskarżenia wynosi **{t4}** (w 3p: **{t['3p']}**, w 5p: **{t['5p']}**)."


def _system_summary(cfg: dict) -> str:
    s = cfg["system"]
    return f"""**Parametry systemowe (Kanon 4p):** Złoto startowe: **3 zł** (w 5p: 2 zł) | Agenci: **{s['agents_per_player']}** | Limit ręki: **{s['hand_limit']}** | Max Er: **{s['max_eras']}** | Autodafé cooldown: co **{s['autodafe_cooldown']}** Ery | Karty/Erę: **{s['cards_per_era']}**"""


def sync_ksiega(cfg: dict) -> list[str]:
    """Replace CONFIG-marked sections in ksiega.md."""
    ksiega_path = PROJECT_ROOT / "docs" / "rules" / "ksiega.md"
    text = ksiega_path.read_text(encoding="utf-8")
    changes: list[str] = []

    # Replace victory table
    old_victory_pattern = re.compile(
        r"(\| Frakcja \| Warunek.*?\n(?:\| :---.*?\n)?)"
        r"(\| (?:Święte Oficjum|\*\*Święte Oficjum\*\*) \|.*?\n)"
        r"(\| (?:Cienie Al-Andalus|\*\*Cienie Al-Andalus\*\*) \|.*?\n)"
        r"(\| (?:Korona|\*\*Korona & Borgiowie\*\*) \|.*?\n)"
        r"(\| (?:Kabała|\*\*Kabała z Toledo\*\*) \|.*?\n)"
        r"(\| (?:Gildia|\*\*Gildia Cieni\*\*) \|.*?\n)",
        re.MULTILINE
    )
    new_victory = _victory_table(cfg) + "\n"
    if old_victory_pattern.search(text):
        text = old_victory_pattern.sub(new_victory, text)
        changes.append("Tabela Zwycięstwa (Kanon 4p) zaktualizowana")

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
        changes.append("Tabela Herezji (Kanon 4p) zaktualizowana")

    # Replace scaling section box
    scaling_pattern = re.compile(
        r"(## 5\. Skalowanie Składu.*?\n\n)(?:>.*?\n)+",
        re.MULTILINE
    )
    if scaling_pattern.search(text):
        text = scaling_pattern.sub(f"## 5. Skalowanie Składu (Warianty 3p i 5p)\n\nKanonem rozgrywki jest **skład 4-osobowy**. Przy grze w innym gronie wprowadź wyłącznie poniższe modyfikacje:\n\n{_scaling_box(cfg)}\n\n", text)
        changes.append("Ramka Skalowania Składu zaktualizowana")

    # Replace setup section values
    gold_pattern = re.compile(r"Złoto startowe: .*? na gracza\.")
    text = gold_pattern.sub("Złoto startowe: **3 zł** na gracza (w 5p: **2 zł**).", text)

    hand_pattern = re.compile(r"Dobierz .*? kart z talii")
    text = hand_pattern.sub(f"Dobierz **{cfg['system']['hand_limit']}** kart z talii", text)

    limit_pattern = re.compile(r"Dobierz karty do limitu ręki .*?\.")
    text = limit_pattern.sub(f"Dobierz karty do limitu ręki **{cfg['system']['hand_limit']}**.", text)

    # Replace "Limit Er" in freeze table
    limit_er_pattern = re.compile(r"\*\*Limit Er: \d+\.\*\*")
    text = limit_er_pattern.sub(f"**Limit Er: {cfg['system']['max_eras']}.**", text)

    # Replace autodafe cooldown
    autodafe_pattern = re.compile(r"max \*\*co \d+ Ery\*\*")
    text = autodafe_pattern.sub(f"max **co {cfg['system']['autodafe_cooldown']} Ery**", text)

    # Replace cards per era
    cards_pattern = re.compile(r"\*\*do \d+\*\* \(zagranie lub pas\)")
    text = cards_pattern.sub(f"**do {cfg['system']['cards_per_era']}** (zagranie lub pas)", text)

    ksiega_path.write_text(text, encoding="utf-8")
    changes.append("Inline parametry zsynchronizowane")
    return changes


def sync_teach_sheet(cfg: dict) -> list[str]:
    """Sync teach-sheet.md with game_config.yaml."""
    path = PROJECT_ROOT / "docs" / "rules" / "teach-sheet.md"
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")

    # Replace setup line
    text = re.sub(r"planszetka \(Herezja \*\*0\*\*\), .*", "planszetka (Herezja **0**), **3 złoto** (w 5p: **2 zł**).", text)

    # Replace heresy zones
    text = re.sub(
        r"\| 4–5 \(3p\) / 4–6 \(4–5p\) \| Obserwowana \|.*?\n\| 6–10 \(3p\) / 7–10 \(4–5p\) \| \*\*Krytyczna\*\* \|.*?\n",
        f"| 4–6 (w 3p: 4–5) | Obserwowana | Ryzyko; Kabała lubi ten pas |\n| 7–10 (w 3p: ≥6, w 5p: ≥8) | **Krytyczna** | Inni mogą Cię oskarżyć |\n",
        text
    )

    # Accusation rule
    text = re.sub(
        r"1\. Cel w Krytycznej \(≥.*?\)\.",
        "1. Cel w Krytycznej (≥7, w 3p: ≥6, w 5p: ≥8).",
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

    # Victory table
    old_teach_vic = re.compile(
        r"(\| Frakcja \| Cel.*?\n(?:\| :---.*?\n)?)"
        r"(\| Święte Oficjum \|.*?\n)"
        r"(\| Cienie Al-Andalus \|.*?\n)"
        r"(\| Korona & Borgiowie \|.*?\n)"
        r"(\| Kabała z Toledo \|.*?\n)"
        r"(\| Gildia Cieni \|.*?\n)",
        re.MULTILINE
    )
    new_teach_vic = f"""| Frakcja | Cel (Kanon 4p) |
| :--- | :--- |
| Święte Oficjum | **4 Stosy** lub **2 Skazania Werdyktem** (w 3p: 3 Stosy) |
| Cienie Al-Andalus | **2 Relikwie** + ścieżka (od Ery 5) |
| Korona & Borgiowie | **2 Dekrety** (od Ery 6) |
| Kabała z Toledo | **3 Fragmenty** + Herezja **3–8** od Ery 6 (w 3p: od Ery 7) |
| Gildia Cieni | **2 Upadki** (3 bez Oficjum) |
"""
    if old_teach_vic.search(text):
        text = old_teach_vic.sub(new_teach_vic, text)

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


def sync_readme(cfg: dict) -> list[str]:
    """Sync README.md victory conditions table with game_config.yaml."""
    path = PROJECT_ROOT / "README.md"
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    v = cfg.get("victory", {})
    kb_era = v.get("korona_borgiowie", {}).get("era", 5)
    caa_era = v.get("cienie_al_andalus", {}).get("path_era", 5)

    old_readme_vic = re.compile(
        r"(## Frakcje.*?\n\n)"
        r"(\| Frakcja \|.*?\n(?:\| :---.*?\n)?)"
        r"(\| \*\*Święte Oficjum\*\* \|.*?\n)"
        r"(\| \*\*Cienie Al-Andalus\*\* \|.*?\n)"
        r"(\| \*\*Korona & Borgiowie\*\* \|.*?\n)"
        r"(\| \*\*Kabała z Toledo\*\* \|.*?\n)"
        r"(\| \*\*Gildia Cieni\*\* \|.*?\n)",
        re.MULTILINE
    )
    new_readme_vic = f"""## Frakcje i Cele Zwycięstwa (Kanon 4p)

| Frakcja | Cel (Kanon 4p) |
| :--- | :--- |
| **Święte Oficjum** | **4 Stosy** (spaleni agenci) **lub 2 Skazania** Werdyktem *(w 3p: 3 Stosy)* |
| **Cienie Al-Andalus** | **2 Relikwie** + ścieżka (od Ery {caa_era}) |
| **Korona & Borgiowie** | **2 Dekrety** (od Ery {kb_era}) |
| **Kabała z Toledo** | **3 Fragmenty** + Herezja **3–8** (od Ery 6; *w 3p: od Ery 7*) |
| **Gildia Cieni** | **2 Upadki** *(3 gdy brak Oficjum)* |
"""
    if old_readme_vic.search(text):
        text = old_readme_vic.sub(new_readme_vic, text)
        path.write_text(text, encoding="utf-8")
        return ["Zsynchronizowano README.md"]
    return []


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
    for ch in sync_readme(cfg):
        print(f"   ✅ {ch}")
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


