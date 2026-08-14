#!/usr/bin/env python3
"""Master script to run a Grand Monte Carlo Audit across all 6 simulation reports.

- Raport Główny (Telemetria i Win Shares 16 setupów): 10 000 gier / setup (160 000 partii)
- Poziomy 1–4 oraz Testy Stresu: 3 000 gier / setup (48 000 partii per test)
- Łączna próba: ~10.5 miliona partii
- Szacowany czas wykonania: ~30-35 minut na 10 rdzeniach
"""
import argparse
import subprocess
import sys
import time
from pathlib import Path

TOOLS_SIM_DIR = Path(__file__).resolve().parent
PYTHON_BIN = sys.executable

AUDIT_PIPELINE = [
    ("1. Raport Główny (Telemetria i Win Shares 16 setupów)", TOOLS_SIM_DIR / "generate_report.py", ["--games", "10000", "--seed", "42"]),
    ("2. Poziom 1 (Mechaniki Systemowe i Offsety)", TOOLS_SIM_DIR / "audit_level1.py", ["--games", "3000", "--seed", "42"]),
    ("3. Poziom 2 (Warunki Zwycięstwa i Skalowanie)", TOOLS_SIM_DIR / "audit_level2.py", ["--games", "3000", "--seed", "42"]),
    ("4. Poziom 3 (Parametry Wszystkich 50 Kart - Koszt/Herezja)", TOOLS_SIM_DIR / "audit_level3.py", ["--games", "3000", "--param", "cost,heresy", "--seed", "42"]),
    ("5. Poziom 4 (Warianty Niszowe i Edykty)", TOOLS_SIM_DIR / "audit_level4.py", ["--games", "3000", "--seed", "42"]),
    ("6. Testy Stresu Ekonomicznego (Poverty Stress)", TOOLS_SIM_DIR / "audit_stress_tests.py", ["--games", "3000", "--seed", "42"]),
]


def main():
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 — Grand Monte Carlo Audit (10k Główny, 3k Poziomy 1-4)")
    parser.add_argument("--seed", type=int, default=42, help="Globalne ziarno losowości (default: 42)")
    args = parser.parse_args()

    print("═══════════════════════════════════════════════════════════════")
    print("      INQUISITIO-1492 — GRAND MONTE CARLO AUDIT (30 MIN)       ")
    print("      Raport Główny: 10 000 gier | Poziomy L1–L4: 3 000 gier    ")
    print(f"      Ziarno losowości: {args.seed} | Łącznie: ~10.5M partii   ")
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
        print(f"✔ [{idx}/{len(AUDIT_PIPELINE)}] Zakończono {name} w {step_elapsed}s ({round(step_elapsed/60, 1)} min)")

    elapsed = round(time.time() - t_start, 1)
    print("\n═══════════════════════════════════════════════════════════════")
    print(f"✅ GRAND MONTE CARLO AUDIT ZAKOŃCZONY W {elapsed}s ({round(elapsed/60, 1)} min)!")
    print("Wszystkie raporty zarchiwizowane w: playtesting/sim-reports/archive/{wersja}/")
    print("═══════════════════════════════════════════════════════════════")


if __name__ == "__main__":
    main()
