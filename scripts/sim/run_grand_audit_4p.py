#!/usr/bin/env python3
"""Master script to run a Grand Monte Carlo Audit across all 7 simulation reports for 4P setups only.

- Raport Główny (Telemetria i Win Shares 5 setupów 4P): 10 000 gier / setup (50 000 partii)
- Poziomy 1–4 oraz Testy Stresu: 3 000 gier / setup (15 000 partii per test)
- Badanie Użyteczności i Wpływu (Feature Impact 4P): 5 000 gier / setup (25 000 partii per wariant)
- Łączna próba: ~5.3 miliona partii
- Szacowany czas wykonania: ~15-18 minut na 10 rdzeniach
"""
import argparse
import os
import subprocess
import sys
import time
from pathlib import Path

TOOLS_SIM_DIR = Path(__file__).resolve().parent
SIM_DIR = TOOLS_SIM_DIR.parent.parent / "sim"
PYTHON_BIN = sys.executable

AUDIT_PIPELINE = [
    ("1. Raport Główny (Telemetria i Win Shares 5 setupów 4P)", TOOLS_SIM_DIR / "generate_report.py", ["--games", "10000", "--players", "4", "--seed", "42"]),
    ("2. Poziom 1 (Mechaniki Systemowe i Offsety 4P)", TOOLS_SIM_DIR / "audit_level1.py", ["--games", "5000", "--players", "4", "--seed", "42"]),
    ("3. Poziom 2 (Warunki Zwycięstwa i Skalowanie 4P)", TOOLS_SIM_DIR / "audit_level2.py", ["--games", "5000", "--players", "4", "--seed", "42"]),
    ("4. Poziom 3 (Parametry Wszystkich 50 Kart - Koszt/Herezja 4P)", TOOLS_SIM_DIR / "audit_level3.py", ["--games", "5000", "--players", "4", "--param", "cost,heresy", "--seed", "42"]),
    ("5. Poziom 4 (Warianty Niszowe i Edykty 4P)", TOOLS_SIM_DIR / "audit_level4.py", ["--games", "5000", "--players", "4", "--seed", "42"]),
    ("6. Testy Stresu Ekonomicznego (Poverty Stress 4P)", TOOLS_SIM_DIR / "audit_stress_tests.py", ["--games", "5000", "--players", "4", "--seed", "42"]),
    ("7. Badanie Użyteczności i Wpływu Elementów (Feature & Card Impact 4P)", TOOLS_SIM_DIR / "feature_impact_4p.py", ["--games", "5000", "--seed", "42"]),
]


def main():
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 — Grand Monte Carlo Audit 4P (10k Główny, 3k L1-L4, 5k Feature Impact)")
    parser.add_argument("--seed", type=int, default=42, help="Globalne ziarno losowości (default: 42)")
    args = parser.parse_args()

    print("═══════════════════════════════════════════════════════════════")
    print("    INQUISITIO-1492 — GRAND MONTE CARLO AUDIT 4P (15 MIN)     ")
    print("      Raport Główny: 10 000 gier | Poziomy L1–L4: 3 000 gier    ")
    print("      Feature & Card Impact: 5 000 gier | Łącznie: ~5.3M partii ")
    print(f"      Ziarno losowości: {args.seed}                            ")
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
        env = os.environ.copy()
        env["PYTHONPATH"] = f"{SIM_DIR}{os.pathsep}{env.get('PYTHONPATH', '')}"
        cmd = [PYTHON_BIN, str(script_path)] + cmd_args
        res = subprocess.run(cmd, env=env)
        if res.returncode != 0:
            print(f"\n❌ Błąd podczas wykonywania: {script_path.name}")
            sys.exit(res.returncode)
        step_elapsed = round(time.time() - t_step, 1)
        print(f"✔ [{idx}/{len(AUDIT_PIPELINE)}] Zakończono {name} w {step_elapsed}s ({round(step_elapsed/60, 1)} min)")

    elapsed = round(time.time() - t_start, 1)
    print("\n═══════════════════════════════════════════════════════════════")
    print(f"✅ GRAND MONTE CARLO AUDIT 4P ZAKOŃCZONY W {elapsed}s ({round(elapsed/60, 1)} min)!")
    print("Wszystkie raporty 4P zarchiwizowane w: data/playtesting/sim-reports/archive/{wersja}/")
    print("═══════════════════════════════════════════════════════════════")


if __name__ == "__main__":
    main()
