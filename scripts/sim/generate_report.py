#!/usr/bin/env python3
"""Script to generate a comprehensive Telemetry and Win Share Report across all 16 setups."""
import argparse
import sys
import time
from pathlib import Path

# Fix path to include sim directory
SIM_DIR = Path(__file__).resolve().parent.parent.parent / "sim"
sys.path.insert(0, str(SIM_DIR))

from datetime import datetime
from inquisitio.config import CONFIG
from inquisitio.engine.setup import SETUP_PRESETS, FactionId
from inquisitio.runner.batch import run_batch
from inquisitio.runner.scoring import calculate_setup_score, calculate_balance_score, evaluate_vitality, color_score
from inquisitio.runner.audit_facts import save_and_archive_report
from inquisitio.runner.era_analytics import generate_era_distribution_markdown

FACTION_NAMES = {
    FactionId.SWIETE_OFICJUM: "SO",
    FactionId.CIENIE_AL_ANDALUS: "CAA",
    FactionId.KORONA_BORGIOWIE: "KB",
    FactionId.KABALA_TOLEDO: "KT",
    FactionId.GILDIA_CIENI: "GC",
}

def main():
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 - Generate Telemetry Report")
    parser.add_argument("--games", type=int, default=10000, help="Number of games per setup (ADR-0014: >= 5000)")
    parser.add_argument("--seed", type=int, default=42, help="RNG seed")
    parser.add_argument("--players", type=int, default=None, choices=[3, 4, 5], help="Filter setups by player count")
    parser.add_argument("--output", type=str, default=None, help="Output markdown path")
    args = parser.parse_args()

    games_per_setup = args.games
    if args.players:
        setups = [s for s in sorted(SETUP_PRESETS.keys()) if len(SETUP_PRESETS[s]) == args.players]
        title_tag = f"DLA {len(setups)} SETUPÓW ({args.players}P)"
    else:
        setups = sorted(SETUP_PRESETS.keys())
        title_tag = "DLA 16 SETUPÓW"

    print("========================================================")
    print(f"GENEROWANIE PEŁNEJ TELEMETRII I WIN-SHARE {title_tag}")
    print(f"Próba: {games_per_setup} gier per setup | Ziarno: {args.seed}")
    print("========================================================\n")

    t0 = time.time()
    setup_data = []
    all_summaries = []
    thresh = int(CONFIG.system.accusation_threshold)

    for sname in setups:
        summary = run_batch(games=games_per_setup, setup=sname, seed=args.seed, layer="C", threshold=thresh)
        all_summaries.append(summary)
        score = calculate_setup_score(summary)
        balance = calculate_balance_score(summary)
        vit = evaluate_vitality(summary)
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

        # 3-color telemetry zones: 🟢 strict norm, 🟡 warning band, 🔴 out of norm
        if 5.0 <= avg_eras <= 6.5:
            eras_opt = "🟢"
        elif 4.5 <= avg_eras <= 7.0:
            eras_opt = "🟡"
        else:
            eras_opt = "🔴"

        if deadlock_pct <= 5.0:
            deadlock_opt = "🟢"
        elif deadlock_pct <= 10.0:
            deadlock_opt = "🟡"
        else:
            deadlock_opt = "🔴"

        if poverty_pct <= 28.0:
            poverty_opt = "🟢"
        elif poverty_pct <= 32.0:
            poverty_opt = "🟡"
        else:
            poverty_opt = "🔴"

        if 0.7 <= autodafe_avg <= 1.8:
            autodafe_opt = "🟢"
        elif 0.5 <= autodafe_avg <= 2.0:
            autodafe_opt = "🟡"
        else:
            autodafe_opt = "🔴"

        if 3.5 <= accusations_avg <= 8.5:
            acc_opt = "🟢"
        elif 2.0 <= accusations_avg <= 10.0:
            acc_opt = "🟡"
        else:
            acc_opt = "🔴"

        setup_data.append({
            "setup": sname,
            "n_players": n_players,
            "score": score,
            "balance": balance,
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
            "vitality_status": vit.status,
            "vitality_warnings": vit.warnings,
            "vitality_penalty": round(vit.vitality_penalty, 3),
        })

    elapsed = round(time.time() - t0, 2)

    report_lines = [
        f"# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: {CONFIG.version}",
        "",
        f"**Wersja Balansu:** `{CONFIG.version}` | **Data:** {datetime.now().strftime('%Y-%m-%d %H:%M')} | **Wielkość Próby:** {games_per_setup} gier/setup ({games_per_setup * 16} gier łącznie) | **Czas Symulacji:** {elapsed}s",
        "",
        "*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).",
        "*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).",
        "",
        "## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny",
        "",
        "| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |",
    ]

    for d in setup_data:
        so_s = f"{d['shares'].get('SO', 0.0):.1f}%" if "SO" in d['shares'] else "-"
        caa_s = f"{d['shares'].get('CAA', 0.0):.1f}%" if "CAA" in d['shares'] else "-"
        kb_s = f"{d['shares'].get('KB', 0.0):.1f}%" if "KB" in d['shares'] else "-"
        kt_s = f"{d['shares'].get('KT', 0.0):.1f}%" if "KT" in d['shares'] else "-"
        gc_s = f"{d['shares'].get('GC', 0.0):.1f}%" if "GC" in d['shares'] else "-"

        if d['score'] >= 90.0:
            eval_str = "🟢 ZBALANSOWANY"
        elif d['score'] >= 80.0:
            eval_str = "🟡 AKCEPTOWALNY"
        elif d['score'] >= 65.0:
            eval_str = "🟠 WYMAGA UWAGI"
        else:
            eval_str = "🔴 ODCHYLONY"
        report_lines.append(
            f"| `{d['setup']}` | {d['n_players']} | {color_score(d['score'], bold=True)} | {color_score(d['balance'])} | {d['ideal_share']:.1f}% | {so_s} | {caa_s} | {kb_s} | {kt_s} | {gc_s} | {eval_str} |"
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
        "## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)",
        "",
        "| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |",
        "| :--- | :---: | :---: | :--- |",
    ])

    for d in setup_data:
        warn_str = ", ".join(d['vitality_warnings']) if d['vitality_warnings'] else "Brak — wszystkie mechaniki aktywne i płynne"
        report_lines.append(
            f"| `{d['setup']}` | {d['vitality_status']} | {d['vitality_penalty']:.3f} | {warn_str} |"
        )

    # --- Section 3.1: Faction Attention Report ---
    faction_stats: dict[str, list[tuple[str, float, float]]] = {}
    for d in setup_data:
        ideal = d['ideal_share'] / 100.0
        for fname, share_pct in d['shares'].items():
            share = share_pct / 100.0
            faction_stats.setdefault(fname, []).append((d['setup'], share, ideal))

    report_lines.extend([
        "",
        "## 3.1. Frakcje Wymagające Uwagi",
        "",
    ])

    faction_summary = []
    for fname, entries in sorted(faction_stats.items()):
        avg_share = sum(s for _, s, _ in entries) / len(entries)
        worst_setup = max(entries, key=lambda e: abs(e[1] - e[2]))
        worst_dev = worst_setup[1] - worst_setup[2]
        worst_dev_pct = worst_dev * 100.0
        if abs(worst_dev_pct) > 5.0:
            status = "🟡 DOMINUJE" if worst_dev > 0 else "🟡 SŁABA"
        elif abs(worst_dev_pct) > 8.0:
            status = "🔴 SILNIE ZABURZONA"
        else:
            status = "🟢 OK"
        faction_summary.append((fname, avg_share * 100, worst_setup[0], worst_dev_pct, status))

    report_lines.append("| Frakcja | Śr. Win Share (wszystkie setupy) | Najgorszy Setup | Max Odchylenie od Ideału | Status |")
    report_lines.append("| :--- | :---: | :--- | :---: | :--- |")
    for fname, avg_s, ws_name, ws_dev, ws_status in sorted(faction_summary, key=lambda x: abs(x[3]), reverse=True):
        dev_sign = f"+{ws_dev:.1f}%" if ws_dev > 0 else f"{ws_dev:.1f}%"
        report_lines.append(f"| **{fname}** | {avg_s:.1f}% | `{ws_name}` | {dev_sign} | {ws_status} |")

    weak_setups = [(d['setup'], d['score'], d['shares'], d['ideal_share']) for d in setup_data if d['score'] < 90.0]
    if weak_setups:
        report_lines.extend([
            "",
            "### Setupy poniżej Score 90 (wymagające poprawy):",
            "",
            "| Setup | Score | Główny problem |",
            "| :--- | :---: | :--- |",
        ])
        for sname, score, shares, ideal in sorted(weak_setups, key=lambda x: x[1]):
            max_dev_fname = max(shares, key=lambda f: abs(shares[f] - ideal))
            dev = shares[max_dev_fname] - ideal
            problem = f"{max_dev_fname} {'dominuje' if dev > 0 else 'za słaba'} ({shares[max_dev_fname]:.1f}% vs ideal {ideal:.1f}%)"
            report_lines.append(f"| `{sname}` | {color_score(score, bold=True)} | {problem} |")
    else:
        report_lines.extend(["", "### ✅ Wszystkie setupy mają Score ≥ 90 — brak setupów wymagających poprawy."])

    # --- Section 4: Era & Timing Distribution ---
    report_lines.extend([""])
    report_lines.extend(generate_era_distribution_markdown(all_summaries))

    # --- Section 5: Legend ---
    report_lines.extend([
        "",
        "## 5. Legenda Wskaźników Telemetrii i Norm Balansowych",
        "",
        "- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p",
        "- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem",
        "- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%",
        "- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%",
        "- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem",
        "- **⚖️ Oskarżenia / Partię:** 🟢 **3.5 – 8.5** | 🟡 2.0–3.5 / 8.5–10.0 | 🔴 poza zakresem",
        "- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 80 | 🟠 ≥ 65 | 🔴 < 65",
    ])

    default_report_name = f"raport_telemetrii_{args.players}p.md" if args.players else "raport_telemetrii.md"
    out_path, archive_path = save_and_archive_report(report_lines, default_report_name, args.output)

    print("========================================================")
    print(f"RAPORT TELEMETRII WYGENEROWANY W {elapsed}s!")
    print(f"Raport zapisano w: {out_path}")
    if archive_path:
        print(f"Zarchiwizowano w: {archive_path}")
        print(f"Snapshot configu w: {archive_path.parent / 'game_config.yaml'}")
    print("========================================================")

if __name__ == "__main__":
    main()
