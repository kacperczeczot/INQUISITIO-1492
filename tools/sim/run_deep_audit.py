#!/usr/bin/env python3
"""Master script to run a Deep Release Validation Audit across all 6 simulation reports.

High sample sizes (2000-3000 games/setup) ensuring zero statistical noise for patch stamping and GDD validation.
"""
import argparse
import subprocess
import sys
import time
from pathlib import Path

TOOLS_SIM_DIR = Path(__file__).resolve().parent
PYTHON_BIN = sys.executable

AUDIT_PIPELINE = [
    ("Telemetria i Win Shares (16 setupów)", TOOLS_SIM_DIR / "generate_report.py", ["--games", "3000", "--seed", "42"]),
    ("Poziom 1 (Mechaniki Systemowe)", TOOLS_SIM_DIR / "audit_level1.py", ["--games", "2000", "--seed", "42"]),
    ("Poziom 2 (Warunki Zwycięstwa)", TOOLS_SIM_DIR / "audit_level2.py", ["--games", "2000", "--seed", "42"]),
    ("Poziom 3 (Parametry Kart - Koszt/Herezja)", TOOLS_SIM_DIR / "audit_level3.py", ["--games", "500", "--param", "cost,heresy", "--seed", "42"]),
    ("Poziom 4 (Warianty Niszowe i Edykty)", TOOLS_SIM_DIR / "audit_level4.py", ["--games", "2000", "--seed", "42"]),
    ("Testy Stresu Ekonomicznego (Poverty Stress)", TOOLS_SIM_DIR / "audit_stress_tests.py", ["--games", "2000", "--seed", "42"]),
]


def main():
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 — Głęboki Pełny Audyt Walidacyjny (Wszystkie 6 Raportów)")
    parser.add_argument("--seed", type=int, default=42, help="Globalne ziarno losowości (default: 42)")
    args = parser.parse_args()

    print("═══════════════════════════════════════════════════════════════")
    print("      INQUISITIO-1492 — GŁĘBOKI AUDYT WALIDACYJNY (RELEASE)    ")
    print("      Wszystkie 6 Raportów Symulacyjnych (Maksymalna próba)     ")
    print(f"      Ziarno losowości: {args.seed}")
    print("═══════════════════════════════════════════════════════════════\n")

    t_start = time.time()

    for idx, (name, script_path, default_args) in enumerate(AUDIT_PIPELINE, 1):
        cmd_args = list(default_args)
        # Override seed if passed via CLI
        if "--seed" in cmd_args and args.seed != 42:
            seed_idx = cmd_args.index("--seed")
            cmd_args[seed_idx + 1] = str(args.seed)

        print(f"\n▶ [{idx}/{len(AUDIT_PIPELINE)}] Uruchamiam: {name}...")
        t_step = time.time()
        cmd = [PYTHON_BIN, str(script_path)] + cmd_args
        res = subprocess.run(cmd)
        if res.returncode != 0:
            print(f"\n❌ Błąd podczas wykonywania: {script_path.name}")
            sys.exit(res.returncode)
        step_elapsed = round(time.time() - t_step, 1)
        print(f"✔ [{idx}/{len(AUDIT_PIPELINE)}] Zakończono {name} w {step_elapsed}s")

    elapsed = round(time.time() - t_start, 1)
    print("\n═══════════════════════════════════════════════════════════════")
    print(f"✅ GŁĘBOKI AUDYT WALIDACYJNY ZAKOŃCZONY W {elapsed}s ({round(elapsed/60, 1)} min)!")
    print("Raporty zarchiwizowane w: playtesting/sim-reports/archive/{wersja}/")
    print("═══════════════════════════════════════════════════════════════")


if __name__ == "__main__":
    main()
