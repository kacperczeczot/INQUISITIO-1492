"""Era and Timing Analytics — detailed game length and per-era faction win share distributions."""
from __future__ import annotations

from collections import Counter, defaultdict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from inquisitio.runner.batch import BatchSummary

FACTION_DISPLAY = {
    "swiete-oficjum": "SO",
    "cienie-al-andalus": "CAA",
    "korona-borgiowie": "KB",
    "kabala-toledo": "KT",
    "gildia-cieni": "GC",
}

FACTION_ORDER = ["SO", "CAA", "KB", "KT", "GC"]
FID_ORDER = [
    "swiete-oficjum",
    "cienie-al-andalus",
    "korona-borgiowie",
    "kabala-toledo",
    "gildia-cieni",
]


def generate_era_distribution_markdown(summaries: list[BatchSummary]) -> list[str]:
    """Generates markdown sections for game duration and per-era faction win distribution."""
    global_era_hist: Counter[int] = Counter()
    global_era_faction_wins: dict[int, Counter[str]] = defaultdict(Counter)
    total_all_games = 0

    for s in summaries:
        for era, cnt in s.era_hist.items():
            global_era_hist[era] += cnt
            total_all_games += cnt
        for era, f_wins in s.era_faction_wins.items():
            for fid, cnt in f_wins.items():
                global_era_faction_wins[era][fid] += cnt

    lines = [
        "## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er",
        "",
        "### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)",
        "",
        "| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |",
        "| :---: | :---: | :---: | :--- | :--- |",
    ]

    for era in sorted(global_era_hist.keys()):
        cnt = global_era_hist[era]
        pct = (cnt / total_all_games) * 100.0 if total_all_games else 0.0
        bar_len = int(round(pct / 2.0))
        bar = "█" * bar_len

        if era <= 2:
            tempo_eval = "🔴 Ekstremalnie wczesna (sprint / anomalia)"
        elif era <= 4:
            tempo_eval = "🟡 Wczesna / Szybka gra"
        elif era <= 7:
            tempo_eval = "🟢 Złote Okno Rozgrywki (Ery 5–7)"
        elif era <= 10:
            tempo_eval = "🟡 Przedłużona / Późna gra"
        else:
            tempo_eval = "🔴 Ekstremalnie przedłużona (deadlock / anomalia)"

        lines.append(f"| **Era {era}** | {cnt:,} | {pct:5.1f}% | `{bar:<20s}` | {tempo_eval} |")

    lines.extend([
        "",
        "### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)",
        "",
        "| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |",
        "| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |",
    ])

    tot_so = sum(global_era_faction_wins[e].get("swiete-oficjum", 0) for e in global_era_hist)
    tot_caa = sum(global_era_faction_wins[e].get("cienie-al-andalus", 0) for e in global_era_hist)
    tot_kb = sum(global_era_faction_wins[e].get("korona-borgiowie", 0) for e in global_era_hist)
    tot_kt = sum(global_era_faction_wins[e].get("kabala-toledo", 0) for e in global_era_hist)
    tot_gc = sum(global_era_faction_wins[e].get("gildia-cieni", 0) for e in global_era_hist)

    for era in sorted(global_era_hist.keys()):
        cnt = global_era_hist[era]
        f_wins = global_era_faction_wins[era]

        so_cnt = f_wins.get("swiete-oficjum", 0)
        caa_cnt = f_wins.get("cienie-al-andalus", 0)
        kb_cnt = f_wins.get("korona-borgiowie", 0)
        kt_cnt = f_wins.get("kabala-toledo", 0)
        gc_cnt = f_wins.get("gildia-cieni", 0)

        so_pct = (so_cnt / cnt) * 100.0 if cnt else 0.0
        caa_pct = (caa_cnt / cnt) * 100.0 if cnt else 0.0
        kb_pct = (kb_cnt / cnt) * 100.0 if cnt else 0.0
        kt_pct = (kt_cnt / cnt) * 100.0 if cnt else 0.0
        gc_pct = (gc_cnt / cnt) * 100.0 if cnt else 0.0

        pct_list = [("SO", so_cnt, so_pct), ("CAA", caa_cnt, caa_pct), ("KB", kb_cnt, kb_pct), ("KT", kt_cnt, kt_pct), ("GC", gc_cnt, gc_pct)]
        dominant_tag, dominant_cnt, dominant_pct = max(pct_list, key=lambda x: x[1])
        dominant_str = f"**{dominant_tag} ({dominant_cnt:,})**" if dominant_cnt > 0 else "-"

        lines.append(
            f"| **Era {era}** | {cnt:,} | {so_cnt:,} | {caa_cnt:,} | {kb_cnt:,} | {kt_cnt:,} | {gc_cnt:,} | {dominant_str} |"
        )

    lines.append(
        f"| **SUMA** | **{total_all_games:,}** | **{tot_so:,}** | **{tot_caa:,}** | **{tot_kb:,}** | **{tot_kt:,}** | **{tot_gc:,}** | **Łącznie: 100.0%** |"
    )

    # 4.3 Setup Era breakdown for 4P Canon setups
    canon_4p_setups = ["4p-core", "4p-no-cienie", "4p-no-kabala", "4p-no-korona", "4p-no-oficjum"]
    canon_summaries = [s for s in summaries if s.setup in canon_4p_setups]

    if canon_summaries:
        lines.extend([
            "",
            "### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)",
            "",
            "| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |",
            "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |",
        ])

        for s in canon_summaries:
            total_g = s.games
            sprint_g = sum(cnt for era, cnt in s.era_hist.items() if era <= 2)
            early_g = sum(cnt for era, cnt in s.era_hist.items() if 3 <= era <= 4)
            opt_g = sum(cnt for era, cnt in s.era_hist.items() if 5 <= era <= 7)
            late_g = sum(cnt for era, cnt in s.era_hist.items() if 8 <= era <= 10)
            dead_g = sum(cnt for era, cnt in s.era_hist.items() if era >= 11)

            sprint_pct = (sprint_g / total_g) * 100.0 if total_g else 0.0
            early_pct = (early_g / total_g) * 100.0 if total_g else 0.0
            opt_pct = (opt_g / total_g) * 100.0 if total_g else 0.0
            late_pct = (late_g / total_g) * 100.0 if total_g else 0.0
            dead_pct = (dead_g / total_g) * 100.0 if total_g else 0.0

            era6_wins = s.era_faction_wins.get(6, {})
            if era6_wins:
                best_fid, best_cnt = max(era6_wins.items(), key=lambda x: x[1])
                best_pct = (best_cnt / sum(era6_wins.values())) * 100.0
                era6_str = f"**{FACTION_DISPLAY.get(best_fid, best_fid)} ({best_pct:.1f}%)**"
            else:
                era6_str = "Brak gier w Erze 6"

            lines.append(
                f"| `{s.setup}` | **{s.eras_avg:.2f}** | {sprint_pct:4.1f}% | {early_pct:4.1f}% | {opt_pct:4.1f}% | {late_pct:4.1f}% | {dead_pct:4.1f}% | {era6_str} |"
            )

    return lines
