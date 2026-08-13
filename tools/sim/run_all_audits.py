#!/usr/bin/env python3
"""Master script to run all 4 Level Audits (Level 1 to Level 4) sequentially."""
import argparse
import subprocess
import sys
import time
from pathlib import Path

TOOLS_SIM_DIR = Path(__file__).resolve().parent
PYTHON_BIN = sys.executable

AUDIT_SCRIPTS = [
    ("Poziom 1 (Mechaniki Systemowe)", TOOLS_SIM_DIR / "audit_level1.py"),
    ("Poziom 2 (Warunki Zwycięstwa)", TOOLS_SIM_DIR / "audit_level2.py"),
    ("Poziom 3 (Parametry Kart)", TOOLS_SIM_DIR / "audit_level3.py"),
    ("Poziom 4 (Warianty Niszowe)", TOOLS_SIM_DIR / "audit_level4.py"),
]


def main():
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 - Run All 4 Level Audits Sequentially")
    parser.add_argument("--games", type=int, default=300, help="Number of games per setup (default: 300)")
    args = parser.parse_args()

    print("═══════════════════════════════════════════════════════")
    print("      INQUISITIO-1492 — KOMPLETNY AUDYT 4 POZIOMÓW    ")
    print(f"      Próba: {args.games} gier / setup")
    print("═══════════════════════════════════════════════════════\n")

    t_start = time.time()

    for idx, (name, script_path) in enumerate(AUDIT_SCRIPTS, 1):
        print(f"\n▶ [{idx}/4] Uruchamiam Audyt {name}...")
        cmd = [PYTHON_BIN, str(script_path), "--games", str(args.games)]
        res = subprocess.run(cmd)
        if res.returncode != 0:
            print(f"❌ Błąd podczas wykonywania: {script_path.name}")
            sys.exit(res.returncode)

    elapsed = time.time() - t_start
    print("\n═══════════════════════════════════════════════════════")
    print(f"✅ WSZYSTKIE 4 AUDYTY ZAKOŃCZONE W {elapsed:.1f}s!")
    print("Raporty zapisano w: playtesting/sim-reports/")
    print("═══════════════════════════════════════════════════════")


if __name__ == "__main__":
    main()
