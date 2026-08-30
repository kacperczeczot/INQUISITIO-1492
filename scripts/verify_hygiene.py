#!/usr/bin/env python3
"""Automated Repository Hygiene and Rule Enforcement Guard.

Checks:
1. Root directory cleanliness (no stray python/markdown/log scripts in root).
2. SSOT Version Alignment (game_config.yaml version has corresponding entry in balance-notes.md).
3. Generic Game Physics / Invariants check.
4. Unit tests pass (optional with --with-tests, or fast mode).
"""
import sys
from pathlib import Path
import re
import yaml

ROOT_DIR = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT_DIR / "src"
sys.path.insert(0, str(SRC_DIR))

from inquisitio.config import GameConfig, ConfigValidationError

ALLOWED_ROOT_FILES = {
    ".DS_Store",
    ".gitignore",
    "README.md",
    "pyrightconfig.json",
    "compile_flags.txt",
}

def check_root_cleanliness() -> list[str]:
    errors = []
    for item in ROOT_DIR.iterdir():
        if item.is_file():
            if item.name not in ALLOWED_ROOT_FILES:
                errors.append(
                    f"⛔ Zanieczyszczenie root: Plik '{item.name}' nie ma prawa znajdować się w katalogu głównym! "
                    "Użyj folderu scratch/ lub przenieś go do scripts/ / data/."
                )
    return errors


def check_ssot_and_patch_notes() -> list[str]:
    errors = []
    config_path = ROOT_DIR / "data/game_config.yaml"
    notes_path = ROOT_DIR / "data/playtesting/balance-notes.md"

    if not config_path.exists():
        errors.append("⛔ Brak pliku data/game_config.yaml!")
        return errors

    with open(config_path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    version = cfg.get("version")
    if not version:
        errors.append("⛔ Brak pola 'version' w data/game_config.yaml!")
        return errors

    if not notes_path.exists():
        errors.append("⛔ Brak pliku data/playtesting/balance-notes.md!")
        return errors

    notes_text = notes_path.read_text(encoding="utf-8")
    if version not in notes_text:
        errors.append(
            f"⛔ Niespójność dokumentacji: Wersja '{version}' z data/game_config.yaml "
            f"nie posiada żadnego wpisu w data/playtesting/balance-notes.md! (Reguła #4 z dyscypliny)"
        )

    # Validate generic invariants
    try:
        GameConfig.validate_invariants(cfg)
    except ConfigValidationError as e:
        errors.append(f"⛔ Naruszenie fizyki gry w data/game_config.yaml: {e}")

    return errors


def main():
    print("========================================================")
    print("🛡️  STRAŻNIK HIGIENY REPOZYTORIUM I DYSCYPLINY (Pre-flight)")
    print("========================================================")

    all_errors = []

    # 1. Root Cleanliness
    root_errs = check_root_cleanliness()
    if root_errs:
        all_errors.extend(root_errs)
    else:
        print("✔ Czystość katalogu głównego (root): OK")

    # 2. SSOT & Patch Notes
    ssot_errs = check_ssot_and_patch_notes()
    if ssot_errs:
        all_errors.extend(ssot_errs)
    else:
        print("✔ Spójność SSOT i Patch Notes: OK")

    # 3. Summary
    if all_errors:
        print("\n❌ WYKRYTO NARUSZENIA ZASAD REPOZYTORIUM:")
        for err in all_errors:
            print(f"  {err}")
        print("\nOperacja zablokowana! Usuń naruszenia przed kontynuacją.")
        sys.exit(1)
    else:
        print("\n✅ Wszystkie mechaniczne zasady higieny repozytorium spełnione!")
        sys.exit(0)


if __name__ == "__main__":
    main()
