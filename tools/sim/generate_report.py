#!/usr/bin/env python3
"""Script to generate a comprehensive Telemetry and Win Share Report across all 16 setups."""
import argparse
import sys
import time
from pathlib import Path

# Fix path to include sim directory
SIM_DIR = Path(__file__).resolve().parent.parent.parent / "sim"
from datetime import datetime
from inquisitio.config import CONFIG
from inquisitio.engine.setup import SETUP_PRESETS, FactionId
from inquisitio.runner.batch import run_batch
from inquisitio.runner.scoring import calculate_setup_score, color_score
from inquisitio.runner.audit_facts import save_and_archive_report

FACTION_NAMES = {
    FactionId.SWIETE_OFICJUM: "SO",
    FactionId.CIENIE_AL_ANDALUS: "CAA",
    FactionId.KORONA_BORGIOWIE: "KB",
    FactionId.KABALA_TOLEDO: "KT",
    FactionId.GILDIA_CIENI: "GC",
}

def main():
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 - Generate Telemetry Report")
    parser.add_argument("--games", type=int, default=500, help="Number of games per setup")
    parser.add_argument("--seed", type=int, default=42, help="RNG seed")
    parser.add_argument("--output", type=str, default=None, help="Output markdown path")
    args = parser.parse_args()

    games_per_setup = args.games
    setups = sorted(SETUP_PRESETS.keys())

    print("========================================================")
    print("GENEROWANIE PEŁNEJ TELEMETRII I WIN-SHARE DLA 16 SETUPÓW")
    print(f"Próba: {games_per_setup} gier per setup | Ziarno: {args.seed}")
    print("========================================================\n")

    t0 = time.time()
    setup_data = []

    for sname in setups:
        summary = run_batch(games=games_per_setup, setup=sname, seed=args.seed, layer="C", threshold=8)
        score = calculate_setup_score(summary)
        factions = SETUP_PRESETS[sname]
        n_players = len(factions)
        ideal_share = round(100.0 / n_players, 1)

        faction_shares = {}
        for fid in factions:
            fname = FACTION_NAMES[fid]
            w_count = summary.wins.get(fid, 0)
            share = round((w_count / summary.games) * 100.0, 1)
            faction_shares[fname] = share

        avg_eras = round(summary.eras_avg, 2)
        deadlock_pct = round(summary.eras_limit_pct * 100.0, 1)
        poverty_pct = round(summary.passes_forced_pct * 100.0, 1)
        autodafe_avg = round(summary.autodafe_avg, 2)
        accusations_avg = round(summary.accusations_avg, 2)

        eras_opt = "🟢" if (5.0 <= avg_eras <= 7.0) else "🔴"
        deadlock_opt = "🟢" if (deadlock_pct <= 15.0) else "🔴"
        poverty_opt = "🟢" if (poverty_pct <= 30.0) else "🔴"
        autodafe_opt = "🟢" if (0.5 <= autodafe_avg <= 2.0) else "⚪"
        acc_opt = "🟢" if (1.5 <= accusations_avg <= 4.5) else "⚪"

        setup_data.append({
            "setup": sname,
            "n_players": n_players,
            "score": score,
            "ideal_share": ideal_share,
            "shares": faction_shares,
            "avg_eras": avg_eras,
            "eras_opt": eras_opt,
            "deadlock_pct": deadlock_pct,
            "deadlock_opt": deadlock_opt,
            "poverty_pct": poverty_pct,
            "poverty_opt": poverty_opt,
            "autodafe_avg": autodafe_avg,
            "autodafe_opt": autodafe_opt,
            "accusations_avg": accusations_avg,
            "acc_opt": acc_opt,
            "end_gold": round(summary.avg_gold_end, 2),
            "end_heresy": round(summary.avg_heresy_end, 2),
        })

    elapsed = round(time.time() - t0, 2)

    report_lines = [
        f"# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: {CONFIG.version}",
        "",
        f"**Wersja Balansu:** `{CONFIG.version}` | **Data:** {datetime.now().strftime('%Y-%m-%d %H:%M')} | **Wielkość Próby:** {games_per_setup} gier/setup ({games_per_setup * 16} gier łącznie) | **Czas Symulacji:** {elapsed}s",
        "",
        "## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny",
        "",
        "| Setup | Gr. | Score | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |",
    ]

    for d in setup_data:
        so_s = f"{d['shares'].get('SO', 0.0):.1f}%" if "SO" in d['shares'] else "-"
        caa_s = f"{d['shares'].get('CAA', 0.0):.1f}%" if "CAA" in d['shares'] else "-"
        kb_s = f"{d['shares'].get('KB', 0.0):.1f}%" if "KB" in d['shares'] else "-"
        kt_s = f"{d['shares'].get('KT', 0.0):.1f}%" if "KT" in d['shares'] else "-"
        gc_s = f"{d['shares'].get('GC', 0.0):.1f}%" if "GC" in d['shares'] else "-"

        eval_str = "🟢 ZBALANSOWANY" if d['score'] >= 50.0 else ("🟡 AKCEPTOWALNY" if d['score'] >= 25.0 else "🔴 ODCHYLONY")
        report_lines.append(
            f"| `{d['setup']}` | {d['n_players']} | {color_score(d['score'], bold=True)} | {d['ideal_share']:.1f}% | {so_s} | {caa_s} | {kb_s} | {kt_s} | {gc_s} | {eval_str} |"
        )

    report_lines.extend([
        "",
        "## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności",
        "",
        "| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |",
    ])

    for d in setup_data:
        all_ok = (d['eras_opt'] == "🟢" and d['deadlock_opt'] == "🟢" and d['poverty_opt'] == "🟢")
        status_icon = "🟢 OPTYMALNA" if all_ok else "⚠️ WARTOŚCI BRZEGOWE"

        report_lines.append(
            f"| `{d['setup']}` | {d['avg_eras']} {d['eras_opt']} | {d['deadlock_pct']}% {d['deadlock_opt']} | {d['poverty_pct']}% {d['poverty_opt']} | {d['autodafe_avg']} {d['autodafe_opt']} | {d['accusations_avg']} {d['acc_opt']} | {d['end_gold']}zł | {d['end_heresy']} | {status_icon} |"
        )

    report_lines.extend([
        "",
        "## 3. Legenda Wskaźników Telemetrii i Norm Balansowych",
        "",
        "- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p",
        "- **⏱️ Średnia Er (Tempo Gry):** Normatyw: **5.0 – 7.0 Er** (oznaczono 🟢 / 🔴)",
        "- **🔒 Remisy po 8 Erach (Deadlock %):** Dopuszczalne: **< 15.0%** (oznaczono 🟢 / 🔴)",
        "- **💰 Pas Biedy (Poverty Rate %):** Dopuszczalne: **< 30.0%** tur spasionych z braku monety (oznaczono 🟢 / 🔴)",
        "- **🔥 Autodafé / Partię (Aktywność Inkwizycji):** Optymalne: **0.5 – 2.0** na grę (oznaczono 🟢 / ⚪)",
        "- **⚖️ Oskarżenia na Dworze / Partię:** Optymalne: **1.5 – 4.5** na grę (oznaczono 🟢 / ⚪)",
    ])

    out_path, archive_path = save_and_archive_report(report_lines, "raport_telemetrii.md", args.output)

    print("========================================================")
    print(f"RAPORT TELEMETRII WYGENEROWANY W {elapsed}s!")
    print(f"Raport zapisano w: {out_path}")
    if archive_path:
        print(f"Zarchiwizowano w: {archive_path}")
        print(f"Snapshot configu w: {archive_path.parent / 'game_config.yaml'}")
    print("========================================================")

if __name__ == "__main__":
    main()
