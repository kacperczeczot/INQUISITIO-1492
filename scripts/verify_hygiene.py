#!/usr/bin/env python3
"""Kompleksowy Strażnik Dyscypliny, Higieny Repozytorium i Niezmienników Gry.

Weryfikuje wszystkie żelazne zasady repozytorium przed commitem / audytem:
1. Czystość katalogu głównego (Zero tolerancji dla śmieci w root).
2. Spójność SSOT i format wpisu w balance-notes.md.
3. Fizyczna wykonalność warunków zwycięstwa vs talia kart (Reguła #18).
4. Integralność i zapieczętowanie archiwów wersji (Reguła #15).
5. Brak ukrytych sztucznych bramek czasowych w silniku (ADR-0001 / Anti-Cheat).
6. 100% testów jednostkowych pytest (Reguła #4 / #5).
"""
import subprocess
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
    """1. Weryfikacja czystości katalogu głównego."""
    errors = []
    for item in ROOT_DIR.iterdir():
        if item.is_file():
            if item.name not in ALLOWED_ROOT_FILES:
                errors.append(
                    f"⛔ [ROOT CLEANLINESS] Plik '{item.name}' znajduje się w katalogu głównym! "
                    "Katalog główny musi być czysty. Przenieś plik do data/, scripts/ lub scratch/."
                )
    return errors


def check_ssot_and_patch_notes() -> tuple[list[str], dict]:
    """2. Weryfikacja SSOT i rzetelności patch notes w balance-notes.md."""
    errors = []
    config_path = ROOT_DIR / "data/game_config.yaml"
    notes_path = ROOT_DIR / "data/playtesting/balance-notes.md"

    if not config_path.exists():
        errors.append("⛔ [SSOT] Brak pliku data/game_config.yaml!")
        return errors, {}

    try:
        with open(config_path, "r", encoding="utf-8") as f:
            cfg = yaml.safe_load(f)
    except Exception as e:
        errors.append(f"⛔ [SSOT] Błąd parsowania YAML w data/game_config.yaml: {e}")
        return errors, {}

    version = cfg.get("version")
    if not version or not re.match(r"^v1\.0-alpha\.\d+$", version):
        errors.append(f"⛔ [SSOT] Nieprawidłowy format wersji: '{version}' (wymagane: v1.0-alpha.X)!")

    if not notes_path.exists():
        errors.append("⛔ [PATCH NOTES] Brak pliku data/playtesting/balance-notes.md!")
        return errors, cfg

    notes_text = notes_path.read_text(encoding="utf-8")
    
    # Check if latest version has formal header
    pattern = rf"###\s+[🟢🌐🔵]\s+Patch\s+{re.escape(version)}\s+\(\d{{4}}-\d{{2}}-\d{{2}}\)"
    if not re.search(pattern, notes_text):
        errors.append(
            f"⛔ [PATCH NOTES] Brak wymaganego nagłówka patcha dla '{version}' w balance-notes.md! "
            f"Oczekiwano formatu: '### 🟢 Patch {version} (YYYY-MM-DD) — ...'"
        )

    return errors, cfg


def check_physics_and_deck_invariants(cfg: dict) -> list[str]:
    """3. Matematyczna i fizyczna weryfikacja warunków gry vs zawartość talii kart (Reguła #18)."""
    errors = []
    if not cfg:
        return errors

    # Generic invariants from config.py
    try:
        GameConfig.validate_invariants(cfg)
    except ConfigValidationError as e:
        errors.append(f"⛔ [GAME PHYSICS] Naruszenie niezmienników fizyki gry: {e}")

    cards = cfg.get("cards", {})
    vic = cfg.get("victory", {})

    def _get_val(val, p_key="4p", default=1):
        if isinstance(val, dict):
            return int(val.get(p_key, val.get("4p", default)))
        return int(val) if val is not None else default

    # A. Korona Borgiowie: decrees vs cards in deck
    kb_req = _get_val(vic.get("korona_borgiowie", {}).get("decrees", 2))
    kb_cards_decrees = sum(
        int(c.get("decree", 0)) for cid, c in cards.items() 
        if cid.startswith("kb-") and isinstance(c, dict) and "decree" in c
    )
    if kb_cards_decrees < kb_req:
        errors.append(
            f"⛔ [DECK INVARIANT] Korona Borgiowie wymaga {kb_req} dekretów, "
            f"ale w talii znajduje się tylko {kb_cards_decrees} kart z efektem 'decree'!"
        )

    # B. Kabała Toledo: fragments vs cards in deck
    kt_req = _get_val(vic.get("kabala_toledo", {}).get("fragments", 3))
    kt_cards_frags = sum(
        int(c.get("grant_fragment", 0)) for cid, c in cards.items() 
        if cid.startswith("kt-") and isinstance(c, dict) and "grant_fragment" in c
    )
    if kt_cards_frags < kt_req:
        errors.append(
            f"⛔ [DECK INVARIANT] Kabała Toledo wymaga {kt_req} fragmentów, "
            f"ale w talii znajduje się tylko {kt_cards_frags} kart z efektem 'grant_fragment'!"
        )

    # C. Cienie Al-Andalus: relics vs cards in deck
    caa_req = _get_val(vic.get("cienie_al_andalus", {}).get("relics", 2))
    caa_cards_relics = sum(
        int(c.get("evacuate_relic", 0)) for cid, c in cards.items() 
        if cid.startswith("caa-") and isinstance(c, dict) and "evacuate_relic" in c
    )
    if caa_cards_relics < caa_req:
        errors.append(
            f"⛔ [DECK INVARIANT] Cienie Al-Andalus wymagają {caa_req} relikwii, "
            f"ale w talii znajduje się tylko {caa_cards_relics} kart z efektem 'evacuate_relic'!"
        )

    return errors


def check_archive_integrity(cfg: dict) -> list[str]:
    """4. Weryfikacja integralności zapieczętowanych archiwów (Reguła #15)."""
    errors = []
    archive_root = ROOT_DIR / "data/playtesting/sim-reports/archive"
    if not archive_root.exists():
        return errors

    for ver_dir in archive_root.iterdir():
        if ver_dir.is_dir() and ver_dir.name.startswith("v1.0-alpha."):
            cfg_snapshot = ver_dir / "game_config.yaml"
            if not cfg_snapshot.exists():
                errors.append(
                    f"⛔ [ARCHIVE INTEGRITY] Uszkodzone archiwum: '{ver_dir.name}' nie zawiera snapshotu 'game_config.yaml'!"
                )
            md_files = list(ver_dir.glob("*.md"))
            if not md_files:
                errors.append(
                    f"⛔ [ARCHIVE INTEGRITY] Uszkodzone archiwum: '{ver_dir.name}' nie zawiera żadnego pliku raportu .md!"
                )

    return errors


def check_anti_cheat_adr() -> list[str]:
    """5. Skanowanie silnika pod kątem zabronionych sztucznych bramek erowych (ADR-0001)."""
    errors = []
    engine_dir = ROOT_DIR / "src/inquisitio/engine"
    if not engine_dir.exists():
        return errors

    banned_patterns = [
        re.compile(r"if\s+state\.era\s*[<>]=?\s*\d+"),
        re.compile(r"if\s+st\.era\s*[<>]=?\s*\d+"),
    ]

    for py_file in engine_dir.glob("*.py"):
        if py_file.name in ("turn.py", "setup.py", "scoring.py"):
            continue  # Natural era increment logic is in turn.py
        text = py_file.read_text(encoding="utf-8")
        for line_no, line in enumerate(text.splitlines(), start=1):
            for pat in banned_patterns:
                if pat.search(line) and not line.strip().startswith("#"):
                    errors.append(
                        f"⛔ [ADR-0001 VIOLATION] Wykryto sztuczną bramkę erową w {py_file.name}:{line_no}: '{line.strip()}'!"
                    )
    return errors


def check_unit_tests() -> list[str]:
    """6. Uruchomienie pełnego pakietu testów jednostkowych pytest."""
    errors = []
    res = subprocess.run(
        [sys.executable, "-m", "pytest", "-q"],
        cwd=str(ROOT_DIR),
        capture_output=True,
        text=True,
    )
    if res.returncode != 0:
        errors.append(
            f"⛔ [PYTEST FAILURE] Testy jednostkowe zakończyły się błędem (exit code {res.returncode}):\n{res.stdout}\n{res.stderr}"
        )
    return errors


def main():
    print("========================================================")
    print("🛡️  PEŁNY STRAŻNIK DYSCYPLINY I INTEGRALNOŚCI REPOZYTORIUM")
    print("========================================================\n")

    all_errors = []

    # 1. Root Cleanliness
    errs = check_root_cleanliness()
    if errs:
        all_errors.extend(errs)
    else:
        print("✔ [1/6] Czystość katalogu głównego (root): OK")

    # 2. SSOT & Patch Notes
    errs, cfg = check_ssot_and_patch_notes()
    if errs:
        all_errors.extend(errs)
    else:
        print("✔ [2/6] Spójność SSOT i format Patch Notes: OK")

    # 3. Physics & Deck Invariants
    errs = check_physics_and_deck_invariants(cfg)
    if errs:
        all_errors.extend(errs)
    else:
        print("✔ [3/6] Matematyczna fizyka gry i zasoby talii (Reguła #18): OK")

    # 4. Archive Integrity
    errs = check_archive_integrity(cfg)
    if errs:
        all_errors.extend(errs)
    else:
        print("✔ [4/6] Integralność i zapieczętowanie archiwów (Reguła #15): OK")

    # 5. Anti-Cheat & ADR-0001
    errs = check_anti_cheat_adr()
    if errs:
        all_errors.extend(errs)
    else:
        print("✔ [5/6] Zgodność z Konstytucją ADR (brak sztucznych bramek): OK")

    # 6. Unit Tests
    errs = check_unit_tests()
    if errs:
        all_errors.extend(errs)
    else:
        print("✔ [6/6] Pełny pakiet testów jednostkowych (pytest 100% PASS): OK")

    print("\n========================================================")
    if all_errors:
        print("❌ ZNALEZIONO KRYTYCZNE NARUSZENIA ZASAD REPOZYTORIUM:")
        for err in all_errors:
            print(f"  {err}")
        print("\n⛔ COMMIT / PROCES ZABLOKOWANY!")
        sys.exit(1)
    else:
        print("✅ WSZYSTKIE TESTY DYSCYPLINY I INTEGRALNOŚCI SPEŁNIONE!")
        print("========================================================")
        sys.exit(0)


if __name__ == "__main__":
    main()
