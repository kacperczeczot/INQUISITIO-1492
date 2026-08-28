#!/usr/bin/env python3
"""Synchronize game_config.yaml → documentation & engine.

Usage:
    sim/.venv/bin/python tools/sync_config.py

Reads game_config.yaml (Single Source of Truth) and propagates
values into:
  • docs/rules/ksiega.md  (CONFIG-marked sections)
  • data/playtesting/simulation_guide.md  (norm references)
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = PROJECT_ROOT / "data/game_config.yaml"

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def load_config() -> dict:
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


def _threshold_text(cfg: dict) -> str:
    t = cfg["system"]["accusation_threshold"]
    if isinstance(t, dict):
        return f"**{t.get('4p', 7)}**"
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
    return f"**{r} Relikwie** + ścieżka (Marionetka / cichy exit / szlak morski)"


def _korona_text(cfg: dict) -> str:
    kb = cfg["victory"]["korona_borgiowie"]
    d = kb["decrees"]
    d_val = d["3p"] if isinstance(d, dict) else d
    return f"**{d_val}** Dekrety"


def _kabala_text(cfg: dict) -> str:
    kt = cfg["victory"]["kabala_toledo"]
    f = kt["fragments"]
    f_val = f["3p"] if isinstance(f, dict) else f
    e = kt["era"]
    if isinstance(e, dict):
        e_text = f"od Ery **{e['3p']}**@3p / **{e['4p']}**@4–5p" if e["3p"] != e["4p"] else f"od Ery **{e['3p']}**"
    else:
        e_text = f"od Ery **{e}**"
    hb = kt.get("heresy_band")
    if hb:
        if int(hb[0]) <= 0:
            band = f"Herezja **≤ {hb[1]}**"
        else:
            band = f"Herezja **{hb[0]}–{hb[1]}**"
        return f"**{f_val} Fragmenty** + {band} ({e_text})"
    return f"**{f_val} Fragmenty** ({e_text})"


def _gildia_text(cfg: dict) -> str:
    n, extra = _gc_falls_pair(cfg)
    core = f"**{n} upadki** (Hak / Marionetka / Autodafé lokacji kluczowej / Werdykt na celu z Hakiem)"
    if extra is None:
        return core
    return f"{core}; **{extra}** gdy brak Oficjum"


def _gc_falls_pair(cfg: dict) -> tuple[int, int | None]:
    gc = cfg["victory"]["gildia_cieni"]["falls"]
    if isinstance(gc, dict):
        d = int(gc["default"])
        n = int(gc.get("no_oficjum", d))
        return d, None if d == n else n
    return int(gc), None


def _victory_table(cfg: dict) -> str:
    """Generate the victory conditions table for Kanon 4p."""
    v = cfg["victory"]
    so_s = v["swiete_oficjum"]["stacks"]
    so_stacks = so_s["4p"] if isinstance(so_s, dict) else so_s
    so_c = v["swiete_oficjum"]["condemns"]
    so_condemns = so_c["4p"] if isinstance(so_c, dict) else so_c

    caa_r = v["cienie_al_andalus"]["relics"]

    kb_d = v["korona_borgiowie"]["decrees"]
    kb_dec = kb_d["4p"] if isinstance(kb_d, dict) else kb_d

    kt_f = v["kabala_toledo"]["fragments"]
    kt_frag = kt_f["4p"] if isinstance(kt_f, dict) else kt_f
    kt_e = v["kabala_toledo"].get("era")
    kt_era = (kt_e["4p"] if isinstance(kt_e, dict) else kt_e) if kt_e else None
    kt_hb = v["kabala_toledo"].get("heresy_band")
    if kt_era:
        kt_cell = (
            f"**{kt_frag} Fragmenty** + Herezja **{kt_hb[0]}–{kt_hb[1]}** (od Ery **{kt_era}**)"
            if kt_hb
            else f"**{kt_frag} Fragmenty** (od Ery **{kt_era}**)"
        )
    else:
        kt_cell = f"**{kt_frag} Fragmenty** (Pieczęć Salomona: Herezja 4–6)"

    gc_n, gc_extra = _gc_falls_pair(cfg)
    gc_cell = (
        f"**{gc_n} Upadki** (Hak / Marionetka / Autodafé / Werdykt na celu z Hakiem)"
        if gc_extra is None
        else (
            f"**{gc_n} Upadki** (Hak / Marionetka / Autodafé / Werdykt na celu z Hakiem); "
            f"**{gc_extra}** gdy brak Oficjum"
        )
    )

    return f"""| Frakcja | Warunek Zwycięstwa (Kanon 4p) |
| :--- | :--- |
| **Święte Oficjum** | **{so_stacks} Stosy** (spaleni agenci) **lub {so_condemns} Skazania** Werdyktem |
| **Cienie Al-Andalus** | **{caa_r} Relikwie** + ścieżka (Marionetka / cichy exit / szlak morski) |
| **Korona & Borgiowie** | **{kb_dec} Dekrety** |
| **Kabała z Toledo** | {kt_cell} |
| **Gildia Cieni** | {gc_cell} |"""


def _heresy_table(cfg: dict) -> str:
    """Generate heresy zones table for Kanon 4p."""
    s = cfg["system"]
    ot = int(s.get("observed_threshold", 4))
    t = s["accusation_threshold"]
    t4 = t["4p"] if isinstance(t, dict) else t
    clean_max = ot - 1
    return f"""| Zakres | Strefa | Skutek |
| :---: | :--- | :--- |
| 0–{clean_max} | Czysta | Bezpieczniej, słabsze akcje |
| {ot}–{t4-1} | Obserwowana | Ryzyko — jeden krok od oskarżenia |
| ≥{t4} | **Krytyczna** | Inni mogą **Rzucić Oskarżenie** |"""


def _scaling_box(cfg: dict) -> str:
    """Generate 3p and 5p player count scaling modifications box."""
    s = cfg["system"]
    v = cfg["victory"]

    t = s["accusation_threshold"]
    t3 = t["3p"] if isinstance(t, dict) else t
    t5 = t["5p"] if isinstance(t, dict) else t
    ot = int(s.get("observed_threshold", 4))

    g = s["start_gold"]
    g4 = g["4p"] if isinstance(g, dict) else g
    g5 = g["5p"] if isinstance(g, dict) else g

    so_s = v.get("swiete_oficjum", {}).get("stacks", 4)
    so_s4 = so_s.get("4p", 4) if isinstance(so_s, dict) else so_s
    so_s3 = so_s.get("3p", so_s4) if isinstance(so_s, dict) else so_s4
    so_s5 = so_s.get("5p", so_s4) if isinstance(so_s, dict) else so_s4

    lines_3p = [
        f"> - **Próg Oskarżenia (Krytyczna Herezja):** **`{t3}`** (Strefy: Czysta `0–{ot-1}` / Obserwowana `{ot}–{t3-1}` / Krytyczna `≥{t3}`).",
    ]
    if so_s3 != so_s4:
        lines_3p.append(f"> - **Święte Oficjum:** Wymaga **`{so_s3} Stosów`** (zamiast {so_s4}).")

    kb_e = v.get("korona_borgiowie", {}).get("era")
    if kb_e is not None:
        kb_e3 = kb_e.get("3p") if isinstance(kb_e, dict) else kb_e
        kb_e4 = kb_e.get("4p") if isinstance(kb_e, dict) else kb_e
        if kb_e3 is not None and kb_e4 is not None and kb_e3 != kb_e4:
            lines_3p.append(
                f"> - **Korona & Borgiowie:** Może wygrać od **`Ery {kb_e3}`** (zamiast {kb_e4})."
            )

    kt_e = v.get("kabala_toledo", {}).get("era", 6)
    kt_e3 = kt_e.get("3p", 6) if isinstance(kt_e, dict) else kt_e
    kt_e4 = kt_e.get("4p", 6) if isinstance(kt_e, dict) else kt_e
    if kt_e3 != kt_e4:
        lines_3p.append(
            f"> - **Kabała z Toledo:** Może wygrać od **`Ery {kt_e3}`** (zamiast {kt_e4})."
        )

    lines_5p = []
    if g5 != g4:
        lines_5p.append(f"> - **Złoto Startowe:** Każdy gracz otrzymuje na start **`{g5} zł`** (zamiast {g4} zł).")
    lines_5p.append(f"> - **Próg Oskarżenia (Krytyczna Herezja):** **`{t5}`** (Strefy: Czysta `0–{ot-1}` / Obserwowana `{ot}–{t5-1}` / Krytyczna `≥{t5}`).")
    if so_s5 != so_s4:
        lines_5p.append(
            f"> - **Święte Oficjum:** Wymaga **`{so_s5} Stosów`** (zamiast {so_s4}) ze względu na większą pulę wrogich agentów."
        )

    mod_3p_str = "\n".join(lines_3p)
    mod_5p_str = "\n".join(lines_5p)

    return f"""> ### 👥 Modyfikacje dla 3 Graczy (3p):
{mod_3p_str}
>
> ### 👥 Modyfikacje dla 5 Graczy (5p):
{mod_5p_str}"""


def _balance_rule(cfg: dict) -> str:
    """Generate the balance rule text."""
    t = cfg["system"]["accusation_threshold"]
    t4 = t["4p"] if isinstance(t, dict) else t
    return f"**Zasada Balansu:** bazowy próg oskarżenia wynosi **{t4}**."


def _system_summary(cfg: dict) -> str:
    s = cfg["system"]
    g = s["start_gold"]
    g_val = g["4p"] if isinstance(g, dict) else g
    return f"""**Parametry systemowe (Kanon 4p):** Złoto startowe: **{g_val} zł** | Agenci: **{s['agents_per_player']}** | Limit ręki: **{s['hand_limit']}** | Max Er: **{s['max_eras']}** | Autodafé cooldown: co **{s['autodafe_cooldown']}** Ery | Karty/Erę: **{s['cards_per_era']}**"""


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

    # 3p/5p boxes only — keep 2p Dual Control above them.
    three_five_pattern = re.compile(
        r"> ### 👥 Modyfikacje dla 3 Graczy \(3p\):.*?"
        r"(?=\n---\n)",
        re.DOTALL,
    )
    if three_five_pattern.search(text):
        text = three_five_pattern.sub(_scaling_box(cfg) + "\n", text)
        changes.append("Modyfikacje 3p/5p zaktualizowane")

    # Inline system replacements
    cd = cfg["system"]["autodafe_cooldown"]
    text = re.sub(r"Autodafé \(max co \d+ Ery\)", f"Autodafé (max co {cd} Ery)", text)
    text = re.sub(r"Autodafé max \*\*co \d+ Ery\*\*", f"Autodafé max **co {cd} Ery**", text)
    me = cfg["system"]["max_eras"]
    ver = cfg.get("version", "")
    if ver:
        text = re.sub(r"### Wariant kanoniczny: 4 graczy · wersja .*", f"### Wariant kanoniczny: 4 graczy · wersja {ver}", text)
    text = re.sub(r"\| Maksymalna liczba Er \| \d+ \|", f"| Maksymalna liczba Er | {me} |", text)
    text = re.sub(r"Rozgrywka trwa maksymalnie \d+ Er\.", f"Rozgrywka trwa maksymalnie {me} Er.", text)
    text = re.sub(r"Jeśli po zakończeniu Ery \d+ nikt nie osiągnął", f"Jeśli po zakończeniu Ery {me} nikt nie osiągnął", text)
    text = re.sub(r"\*\*Limit Er: \d+\.\*\*", f"**Limit Er: {me}.**", text)
    text = re.sub(
        r"\| Limit Er / remis \| \*\*\d+\*\* Er;",
        f"| Limit Er / remis | **{me}** Er;",
        text,
    )
    text = re.sub(r"Remis postępu po \*\*\d+\*\* Er", f"Remis postępu po **{me}** Er", text)

    # Balance rule in Tribunal section
    old_bal = re.compile(r"\*\*Zasada Balansu:\*\* bazowy próg.*?\.")
    text = old_bal.sub(_balance_rule(cfg), text)

    ksiega_path.write_text(text, encoding="utf-8")
    changes.append("Zsynchronizowano docs/rules/ksiega.md")
    return changes


def sync_wariant_2p(cfg: dict) -> list[str]:
    """Sync wariant-2p.md with game_config.yaml."""
    path = PROJECT_ROOT / "docs" / "rules" / "wariant-2p.md"
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    ver = cfg.get("version", "")
    me = cfg["system"]["max_eras"]
    if ver:
        text = re.sub(r"### Suplement do Księgi Zasad · Wersja .*", f"### Suplement do Księgi Zasad · Wersja {ver}", text)
    text = re.sub(r"Gra trwa maksymalnie \*\*\d+ Er\*\*", f"Gra trwa maksymalnie **{me} Er**", text)
    text = re.sub(r"Rozstrzyganie remisów po \d+\. Erze", f"Rozstrzyganie remisów po {me}. Erze", text)
    path.write_text(text, encoding="utf-8")
    return ["Zsynchronizowano docs/rules/wariant-2p.md"]


def sync_teach_sheet(cfg: dict) -> list[str]:
    """Sync teach-sheet.md with game_config.yaml."""
    path = PROJECT_ROOT / "docs" / "rules" / "teach-sheet.md"
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")

    # Replace setup line
    g = cfg["system"]["start_gold"]
    g4 = g["4p"] if isinstance(g, dict) else g
    g5 = g["5p"] if isinstance(g, dict) else g
    if g4 == g5:
        gold_teach = f"planszetka (Herezja **0**), **{g4} złoto**."
    else:
        gold_teach = f"planszetka (Herezja **0**), **{g4} złoto** (w 5p: **{g5} zł**)."
    text = re.sub(r"planszetka \(Herezja \*\*0\*\*\), .*", gold_teach, text)

    t = cfg["system"]["accusation_threshold"]
    t3 = t["3p"] if isinstance(t, dict) else t
    t4 = t["4p"] if isinstance(t, dict) else t
    t5 = t["5p"] if isinstance(t, dict) else t
    ot = int(cfg["system"].get("observed_threshold", 4))

    text = re.sub(
        r"\| 0–\d+ \| Czysta \|.*?\n"
        r"\| \d+–\d+.*\| Obserwowana \|.*?\n"
        r"\| \d+–10 \(w 3p: ≥\d+, w 5p: ≥\d+\) \| \*\*Krytyczna\*\* \|.*",
        f"| 0–{ot - 1} | Czysta | Bezpiecznie, zwykle słabiej |\n"
        f"| {ot}–{t4 - 1} (w 3p: {ot}–{t3 - 1}, w 5p: {ot}–{t5 - 1}) | Obserwowana | Ryzyko — jeden krok od oskarżenia |\n"
        f"| {t4}–10 (w 3p: ≥{t3}, w 5p: ≥{t5}) | **Krytyczna** | Inni mogą Cię oskarżyć |",
        text,
    )

    text = re.sub(
        r"1\. Cel w Krytycznej \(≥.*?\)\.",
        f"1. Cel w Krytycznej (≥{t4}, w 3p: ≥{t3}, w 5p: ≥{t5}).",
        text
    )

    me = cfg["system"]["max_eras"]
    text = re.sub(r"\*\*Limit:\*\* \d+ Er", f"**Limit:** {me} Er", text)

    cd = cfg["system"]["autodafe_cooldown"]
    text = re.sub(r"Autodafé \(max co \d+ Ery\)", f"Autodafé (max co {cd} Ery)", text)
    text = re.sub(r"Autodafé max \*\*co \d+ Ery\*\*", f"Autodafé max **co {cd} Ery**", text)

    # Victory table
    v = cfg.get("victory", {})
    so_s = v.get("swiete_oficjum", {}).get("stacks", 4)
    so_4p = so_s.get("4p", 4) if isinstance(so_s, dict) else so_s
    so_3p = so_s.get("3p", 4) if isinstance(so_s, dict) else so_s
    so_5p = so_s.get("5p", 4) if isinstance(so_s, dict) else so_s
    so_c = v.get("swiete_oficjum", {}).get("condemns", 3)
    so_c = so_c.get("4p", 3) if isinstance(so_c, dict) else so_c
    
    so_mods = []
    if so_3p != so_4p:
        so_mods.append(f"w 3p: {so_3p} Stosy")
    if so_5p != so_4p:
        so_mods.append(f"w 5p: {so_5p} Stosów")
    
    so_teach_text = f"**{so_4p} Stosy** lub **{so_c} Skazania Werdyktem** ({', '.join(so_mods)})" if so_mods else f"**{so_4p} Stosy** lub **{so_c} Skazania Werdyktem**"

    kb_d = v.get("korona_borgiowie", {}).get("decrees", 2)
    kb_d4 = kb_d.get("4p", 2) if isinstance(kb_d, dict) else kb_d
    kb_e = v.get("korona_borgiowie", {}).get("era")
    if kb_e is None:
        kb_teach_text = f"**{kb_d4} Dekrety**"
    else:
        kb_4p = kb_e.get("4p") if isinstance(kb_e, dict) else kb_e
        kb_3p = kb_e.get("3p") if isinstance(kb_e, dict) else kb_e
        kb_teach_text = (
            f"**{kb_d4} Dekrety** (od Ery {kb_4p}; w 3p: od Ery {kb_3p})"
            if kb_4p != kb_3p
            else f"**{kb_d4} Dekrety** (od Ery {kb_4p})"
        )

    kt_e = v.get("kabala_toledo", {}).get("era", 6)
    kt_4p = kt_e.get("4p", 6) if isinstance(kt_e, dict) else kt_e
    kt_3p = kt_e.get("3p", 6) if isinstance(kt_e, dict) else kt_e
    kt_hb = v.get("kabala_toledo", {}).get("heresy_band")
    kt_f = v.get("kabala_toledo", {}).get("fragments", 3)
    kt_frag = kt_f.get("4p", 3) if isinstance(kt_f, dict) else kt_f
    if kt_hb:
        kt_core = f"**{kt_frag} Fragmenty** + Herezja **{kt_hb[0]}–{kt_hb[1]}**"
    else:
        kt_core = f"**{kt_frag} Fragmenty**"
    kt_teach_text = f"{kt_core} (od Ery {kt_4p}; w 3p: od Ery {kt_3p})" if kt_4p != kt_3p else f"{kt_core} (od Ery {kt_4p})"

    gc_f = v.get("gildia_cieni", {}).get("falls", {"default": 4, "no_oficjum": 4})
    gc_def = gc_f.get("default", 4) if isinstance(gc_f, dict) else gc_f
    gc_noso = gc_f.get("no_oficjum", gc_def) if isinstance(gc_f, dict) else gc_f
    gc_teach_text = (
        f"**{gc_def} Upadki**"
        if gc_def == gc_noso
        else f"**{gc_def} Upadki** ({gc_noso} bez Oficjum)"
    )

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
| Święte Oficjum | {so_teach_text} |
| Cienie Al-Andalus | {_relics_text(cfg)} |
| Korona & Borgiowie | {kb_teach_text} |
| Kabała z Toledo | {kt_teach_text} |
| Gildia Cieni | {gc_teach_text} |
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
    ot = int(s.get("observed_threshold", 4))

    g = s["start_gold"]
    g4 = g["4p"] if isinstance(g, dict) else g
    g5 = g["5p"] if isinstance(g, dict) else g
    income = int(s.get("era_income", 1))
    ig = int(s.get("intrigue_gold", 1))
    if g4 == g5:
        gold_hier = f"- **Ekonomia:** `{g4} złote` na start · Dochód `+{income} złoty` w Fazie III (Kronika) + opcja Akcji Gospodarczej (+{ig} zł) w Fazie I (Intryga)"
    else:
        gold_hier = f"- **Ekonomia:** `{g4} złote` na start (w 5p: `{g5} złote`) · Dochód `+{income} złoty` w Fazie III (Kronika) + opcja Akcji Gospodarczej (+{ig} zł) w Fazie I (Intryga)"
    text = re.sub(r"- \*\*Ekonomia:\*\* .*", gold_hier, text)

    if isinstance(t, dict):
        t4 = t.get("4p", 7)
    else:
        t4 = int(t)
    text = re.sub(r"- \*\*Maksymalny limit Er:\*\* `\d+ Er`", f"- **Maksymalny limit Er:** `{s['max_eras']} Er`", text)
    prog_hier = f"- **Próg Oskarżenia na Dworze:** `Herezja ≥ {t4}`"
    strefy_prog = (
        f"- **Strefy Herezji:** Czysta `0–{ot - 1}`; Obserwowana od `{ot}` do `T−1`; Krytyczna `≥T`\n"
        + f"- **Próg Obserwowanej:** `≥{ot}` (Autodafé: Stos zamiast aresztu)\n"
        + prog_hier
    )
    text = re.sub(
        r"- \*\*Strefy(?: i pasma)? Herezji:\*\* .*\n"
        r"(?:  - \*\*.*\n)*"
        r"(?:- \*\*Próg Obserwowanej:\*\* .*\n)?"
        r"- \*\*Próg Oskarżenia na Dworze:\*\* .*",
        strefy_prog,
        text,
        count=1,
    )
    h = s["hand_limit"]
    h4 = h["4p"] if isinstance(h, dict) else h
    text = re.sub(
        r"- \*\*Limit kart na ręce:\*\* `\d+ kart`",
        f"- **Limit kart na ręce:** `{h4} kart`",
        text,
    )
    v = cfg["victory"]
    so_s = v["swiete_oficjum"]["stacks"]
    so_st = so_s["4p"] if isinstance(so_s, dict) else so_s
    so_c = v["swiete_oficjum"]["condemns"]
    so_co = so_c["4p"] if isinstance(so_c, dict) else so_c
    caa_r = v["cienie_al_andalus"]["relics"]
    kb_d = v["korona_borgiowie"]["decrees"]
    kb_dec = kb_d["4p"] if isinstance(kb_d, dict) else kb_d
    gc_n, _gc_extra = _gc_falls_pair(cfg)
    so_cell = f"**{so_st} Stosy** lub {so_co} Skazania"
    caa_cell = f"**{caa_r} Relikwie** + Ścieżka"
    kb_cell = f"**{kb_dec} Dekrety**"
    gc_cell = f"**{gc_n} Upadki**"
    text = re.sub(
        r"\| \*\*Święte Oficjum\*\* \|.*",
        f"| **Święte Oficjum** | {so_cell} | {so_cell} | {so_cell} |",
        text,
    )
    text = re.sub(
        r"\| \*\*Cienie Al-Andalus\*\* \|.*",
        f"| **Cienie Al-Andalus** | {caa_cell} | {caa_cell} | {caa_cell} |",
        text,
    )
    text = re.sub(
        r"\| \*\*Korona & Borgiowie\*\* \|.*",
        f"| **Korona & Borgiowie** | {kb_cell} | {kb_cell} | {kb_cell} |",
        text,
    )
    text = re.sub(
        r"\| \*\*Gildia Cieni\*\* \|.*",
        f"| **Gildia Cieni** | {gc_cell} | {gc_cell} | {gc_cell} |",
        text,
    )
    kt = v["kabala_toledo"]
    kt_e = kt.get("era")
    kt_era = (kt_e["4p"] if isinstance(kt_e, dict) else kt_e) if kt_e else None
    kt_f = kt["fragments"]
    kt_frag = kt_f["4p"] if isinstance(kt_f, dict) else kt_f
    kt_sub = f"**{kt_frag} Fragmenty** (Era {kt_era}+)" if kt_era else f"**{kt_frag} Fragmenty** (Pieczęć Salomona)"
    text = re.sub(
        r"\| \*\*Kabała z Toledo\*\* \|.*",
        f"| **Kabała z Toledo** | {kt_sub} | {kt_sub} | {kt_sub} |",
        text,
    )
    text = re.sub(
        r"- \*\*Cooldown Autodafé Inkwizytora:\*\* Max `co \d+ Ery`",
        f"- **Cooldown Autodafé Inkwizytora:** Max `co {s['autodafe_cooldown']} Ery`",
        text
    )

    path.write_text(text, encoding="utf-8")
    return ["Zsynchronizowano docs/rules/hierarchia_balansowania.md"]


def sync_balance_notes(cfg: dict) -> list[str]:
    """Sync the live SSOT snapshot at the top of balance-notes.md (not patch history)."""
    path = PROJECT_ROOT / "playtesting" / "balance-notes.md"
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    s = cfg["system"]
    t = s["accusation_threshold"]
    if isinstance(t, dict):
        t3, t4, t5 = t.get("3p", 6), t.get("4p", 7), t.get("5p", 8)
        prog_why = f"Kanon 4p = **{t4}**. Obserwowana kończy się na T−1."
    else:
        t3 = t4 = t5 = int(t)
        prog_why = f"Kanon 4p = **{t4}**. Obserwowana kończy się na T−1."
    ot = int(s.get("observed_threshold", 4))
    g = s["start_gold"]
    g4 = g["4p"] if isinstance(g, dict) else g
    h = s["hand_limit"]
    h4 = h["4p"] if isinstance(h, dict) else h
    cd = s["autodafe_cooldown"]
    me = s["max_eras"]
    kt = cfg["victory"]["kabala_toledo"]
    kt_e = kt.get("era")
    kt_era = (kt_e["4p"] if isinstance(kt_e, dict) else kt_e) if kt_e else None
    text = re.sub(
        r"\| \*\*Próg Obserwowanej\*\* \| \*\*\d+\*\* \| \*\*\d+\*\* \| \*\*\d+\*\* \|.*",
        f"| **Próg Obserwowanej** | **{ot}** | **{ot}** | **{ot}** | Czysta to 0–{ot-1}. Od **{ot}** Autodafé pali na Stos (nie areszt). |",
        text,
        count=1,
    )
    text = re.sub(
        r"\| \*\*Próg Oskarżenia \(Krytyczna(?: Herezja)?\)\*\* \| \*\*\d+\*\* \| \*\*\d+\*\* \| \*\*\d+\*\* \|.*",
        f"| **Próg Oskarżenia (Krytyczna)** | **{t3}** | **{t4}** | **{t5}** | {prog_why} |",
        text,
        count=1,
    )
    text = re.sub(
        r"\| \*\*Strefy Herezji \(Czysta / Obserw\. / Kryt\.\)\*\* \|.*\n",
        "",
        text,
        count=1,
    )
    text = re.sub(
        r"\| \*\*Maksymalna Liczba Er\*\* \| \*\*\d+\*\* \| \*\*\d+\*\* \| \*\*\d+\*\* \|",
        f"| **Maksymalna Liczba Er** | **{me}** | **{me}** | **{me}** |",
        text,
        count=1,
    )
    text = re.sub(
        r"\| \*\*Cooldown Autodafé\*\* \| \*\*\d+ Ery\*\* \| \*\*\d+ Ery\*\* \| \*\*\d+ Ery\*\* \|.*",
        f"| **Cooldown Autodafé** | **{cd} Ery** | **{cd} Ery** | **{cd} Ery** | Zunifikowany cooldown co {cd} Ery (pierwsze możliwe od Ery {cd}). |",
        text,
        count=1,
    )
    text = re.sub(
        r"\| \*\*Złoto Startowe\*\* \| \*\*\d+ zł\*\* \| \*\*\d+ zł\*\* \| \*\*\d+ zł\*\* \|.*",
        f"| **Złoto Startowe** | **{g4} zł** | **{g4} zł** | **{g4} zł** | Zunifikowane {g4} zł dla wszystkich składów graczy. |",
        text,
        count=1,
    )
    text = re.sub(
        r"\| \*\*Limit Kart na Ręce\*\* \| \*\*\d+ Kart\*\* \| \*\*\d+ Kart\*\* \| \*\*\d+ Kart\*\* \|.*",
        f"| **Limit Kart na Ręce** | **{h4} Kart** | **{h4} Kart** | **{h4} Kart** | Zunifikowany limit {h4} kart dla wszystkich składów graczy. |",
        text,
        count=1,
    )
    if kt_era:
        text = re.sub(
            r"(- \*\*Minimalna Era:\*\* \*\*)\d+",
            rf"\g<1>{kt_era}",
            text,
            count=1,
        )

    path.write_text(text, encoding="utf-8")
    return ["Zsynchronizowano data/playtesting/balance-notes.md (snapshot SSOT)"]


def sync_slownik(cfg: dict) -> list[str]:
    """Sync slownik.md with game_config.yaml."""
    path = PROJECT_ROOT / "docs" / "rules" / "slownik.md"
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    s = cfg["system"]
    g = s["start_gold"]
    g4 = g["4p"] if isinstance(g, dict) else g
    g5 = g["5p"] if isinstance(g, dict) else g
    income = int(s.get("era_income", 1))
    ig = int(s.get("intrigue_gold", 1))
    if g4 == g5:
        gold_str = f"Start **{g4}**; dochód **+{income} złoto** w Fazie III (Kronika) + opcja Akcji Gospodarczej (+{ig} zł) w Fazie I (Intryga)."
    else:
        gold_str = f"Start **{g4}** (w 5p: **{g5}**); dochód **+{income} złoto** w Fazie III (Kronika) + opcja Akcji Gospodarczej (+{ig} zł) w Fazie I (Intryga)."
    text = re.sub(r"Start \*\*.*?\*\*; dochód \*\*.*?\*\* w Fazie III.*?\.", gold_str, text)
    text = re.sub(r"Maksymalny czas gry wynosi \*\*\d+ Er\*\*\.", f"Maksymalny czas gry wynosi **{s['max_eras']} Er**.", text)
    text = re.sub(r"Po \d+ Erach:", f"Po {s['max_eras']} Erach:", text)
    text = re.sub(r"Po \d+ Erach wygrywa", f"Po {s['max_eras']} Erach wygrywa", text)
    text = re.sub(r"Limit gry: \*\*\d+\*\* Er", f"Limit gry: **{s['max_eras']}** Er", text)
    text = re.sub(r"Limit \d+ Er → najbliższy celowi", f"Limit {s['max_eras']} Er → najbliższy celowi", text)
    text = re.sub(r"Remis postępu po \*\*\d+\*\* Er", f"Remis postępu po **{s['max_eras']}** Er", text)
    text = re.sub(r"Remis postępu po \d+ Er", f"Remis postępu po **{s['max_eras']}** Er", text)
    v = cfg["victory"]
    kb_d = v["korona_borgiowie"]["decrees"]
    kb_dec = kb_d["4p"] if isinstance(kb_d, dict) else kb_d
    kt_f = v["kabala_toledo"]["fragments"]
    kt_frag = kt_f["4p"] if isinstance(kt_f, dict) else kt_f
    kt_e = v["kabala_toledo"].get("era")
    kt_era = (kt_e["4p"] if isinstance(kt_e, dict) else kt_e) if kt_e else None
    text = re.sub(r"Warunek zwycięstwa: \*\*\d+ Dekrety\*\*", f"Warunek zwycięstwa: **{kb_dec} Dekrety**", text)
    if kt_era:
        text = re.sub(
            r"Warunek: \*\*\d+ Fragmenty\*\* od Ery \*\*\d+\*\*",
            f"Warunek: **{kt_frag} Fragmenty** od Ery **{kt_era}**",
            text,
        )
    else:
        text = re.sub(
            r"Warunek: \*\*\d+ Fragmenty\*\* od Ery \*\*\d+\*\*",
            f"Warunek: **{kt_frag} Fragmenty** (Pieczęć Salomona)",
            text,
        )

    path.write_text(text, encoding="utf-8")
    return ["Zsynchronizowano docs/rules/slownik.md"]


def sync_setups(cfg: dict) -> list[str]:
    """Sync setups.md with game_config.yaml."""
    path = PROJECT_ROOT / "playtesting" / "setups.md"
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    t = cfg["system"]["accusation_threshold"]
    g = cfg["system"]["start_gold"]
    g4 = g["4p"] if isinstance(g, dict) else g
    g5 = g["5p"] if isinstance(g, dict) else g
    if g4 == g5:
        gold_str = f"Złoto startowe: **{g4} zł** na gracza."
    else:
        gold_str = f"Złoto startowe: **{g4} zł** na gracza (w 5p: **{g5} zł**)."
    gold_pattern = re.compile(r"3\. Złoto startowe: .*")
    text = gold_pattern.sub(f"3. {gold_str}", text)

    hand_pattern = re.compile(r"Dobierz .*? kart z talii")
    text = hand_pattern.sub(f"Dobierz **{cfg['system']['hand_limit']}** kart z talii", text)

    me = cfg["system"]["max_eras"]
    text = re.sub(r"\| Limit Er \| \*\*\d+\*\* \| \*\*\d+\*\* \|", f"| Limit Er | **{me}** | **{me}** |", text)

    path.write_text(text, encoding="utf-8")
    return ["Zsynchronizowano data/playtesting/setups.md"]


def sync_readme(cfg: dict) -> list[str]:
    """Sync README.md victory conditions table with game_config.yaml."""
    path = PROJECT_ROOT / "README.md"
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    v = cfg.get("victory", {})
    so_s = v.get("swiete_oficjum", {}).get("stacks", 4)
    so_4p = so_s.get("4p", 4) if isinstance(so_s, dict) else so_s
    so_3p = so_s.get("3p", 4) if isinstance(so_s, dict) else so_s
    so_5p = so_s.get("5p", 4) if isinstance(so_s, dict) else so_s
    
    so_mods = []
    if so_3p != so_4p:
        so_mods.append(f"w 3p: {so_3p} Stosy")
    if so_5p != so_4p:
        so_mods.append(f"w 5p: {so_5p} Stosów")
    
    so_c = v.get("swiete_oficjum", {}).get("condemns", 3)
    so_c4 = so_c.get("4p", 3) if isinstance(so_c, dict) else so_c
    so_readme_text = (
        f"**{so_4p} Stosy** (spaleni agenci) **lub {so_c4} Skazania** Werdyktem *({', '.join(so_mods)})*"
        if so_mods
        else f"**{so_4p} Stosy** (spaleni agenci) **lub {so_c4} Skazania** Werdyktem"
    )

    kb_d = v.get("korona_borgiowie", {}).get("decrees", 2)
    kb_d4 = kb_d.get("4p", 2) if isinstance(kb_d, dict) else kb_d
    kb_e = v.get("korona_borgiowie", {}).get("era")
    if kb_e is None:
        kb_readme_text = f"**{kb_d4} Dekrety**"
    else:
        kb_4p = kb_e.get("4p") if isinstance(kb_e, dict) else kb_e
        kb_3p = kb_e.get("3p") if isinstance(kb_e, dict) else kb_e
        kb_readme_text = (
            f"**{kb_d4} Dekrety** (od Ery {kb_4p}; *w 3p: od Ery {kb_3p}*)"
            if kb_4p != kb_3p
            else f"**{kb_d4} Dekrety** (od Ery {kb_4p})"
        )

    caa_r = v.get("cienie_al_andalus", {}).get("relics", 2)
    caa_readme_text = f"**{caa_r} Relikwie** + ścieżka"

    kt_hb = v.get("kabala_toledo", {}).get("heresy_band")
    kt_e = v.get("kabala_toledo", {}).get("era", 6)
    kt_4p = kt_e.get("4p", 6) if isinstance(kt_e, dict) else kt_e
    kt_3p = kt_e.get("3p", 6) if isinstance(kt_e, dict) else kt_e
    kt_f = v.get("kabala_toledo", {}).get("fragments", 3)
    kt_frag = kt_f.get("4p", 3) if isinstance(kt_f, dict) else kt_f
    if kt_hb:
        kt_core = f"**{kt_frag} Fragmenty** + Herezja **{kt_hb[0]}–{kt_hb[1]}**"
    else:
        kt_core = f"**{kt_frag} Fragmenty**"
    kt_readme_text = f"{kt_core} (od Ery {kt_4p}; *w 3p: od Ery {kt_3p}*)" if kt_4p != kt_3p else f"{kt_core} (od Ery {kt_4p})"
    gc_n, gc_extra = _gc_falls_pair(cfg)
    gc_readme_text = f"**{gc_n} Upadki**" if gc_extra is None else f"**{gc_n} Upadki** *({gc_extra} gdy brak Oficjum)*"

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
| **Święte Oficjum** | {so_readme_text} |
| **Cienie Al-Andalus** | {caa_readme_text} |
| **Korona & Borgiowie** | {kb_readme_text} |
| **Kabała z Toledo** | {kt_readme_text} |
| **Gildia Cieni** | {gc_readme_text} |
"""
    if old_readme_vic.search(text):
        text = old_readme_vic.sub(new_readme_vic, text)
        path.write_text(text, encoding="utf-8")
        return ["Zsynchronizowano README.md"]
    return []


def sync_cards(cfg: dict) -> list[str]:
    """Sync card markdown files (parameters + effect text), KATALOG.md, and card-editor.html from game_config.yaml."""
    from scripts.pnp.generate_card_text import sync_card_markdowns
    from scripts.cards.build_catalog import main as build_catalog_main
    from scripts.pnp.sync_card_editor import main as sync_card_editor_main

    # 1. Sync card parameters (cost, layer, type) & effect text
    updated_files = sync_card_markdowns(dry_run=False)

    # 2. Rebuild KATALOG.md
    build_catalog_main()

    # 3. Sync card-editor.html CARDS_DATABASE
    sync_card_editor_main()

    res = [f"Zsynchronizowano {len(cfg.get('cards', {}))} kart w docs/game/cards/"]
    if updated_files:
        res.append(f"Zaktualizowano opisy efektów dla {len(updated_files)} kart")
    res.append("Przegenerowano docs/game/cards/KATALOG.md")
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
    print(f"   ⚔️ Cienie: {v['cienie_al_andalus']['relics']} Relikwii")
    kb = v["korona_borgiowie"]
    kb_era = kb.get("era")
    kb_era_txt = f" | Ery {kb_era}" if kb_era is not None else ""
    print(f"   ⚔️ Korona: Dekrety {kb['decrees']}{kb_era_txt}")
    kt_e_txt = f" | Ery {v['kabala_toledo']['era']}" if "era" in v['kabala_toledo'] else " (Pieczęć Salomona)"
    print(f"   ⚔️ Kabała: Fragmenty {v['kabala_toledo']['fragments']}{kt_e_txt}")
    print(f"   ⚔️ Gildia: Upadki {v['gildia_cieni']['falls']}")
    print()

    # Sync docs & cards
    print("📝 Synchronizuję dokumentację i pliki kart z game_config.yaml...")
    for ch in sync_readme(cfg):
        print(f"   ✅ {ch}")
    for ch in sync_ksiega(cfg):
        print(f"   ✅ {ch}")
    for ch in sync_wariant_2p(cfg):
        print(f"   ✅ {ch}")
    for ch in sync_teach_sheet(cfg):
        print(f"   ✅ {ch}")
    for ch in sync_hierarchia(cfg):
        print(f"   ✅ {ch}")
    for ch in sync_balance_notes(cfg):
        print(f"   ✅ {ch}")
    for ch in sync_slownik(cfg):
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
    print("  1. Sprawdź zmiany: git diff docs/ docs/game/cards/ data/playtesting/")
    print("  2. Uruchom testy: sim/.venv/bin/pytest sim/tests/ -q")


if __name__ == "__main__":
    main()


