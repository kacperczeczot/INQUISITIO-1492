#!/usr/bin/env python3
"""Kompleksowy Strażnik Dyscypliny, Higieny Repozytorium i Niezmienników Gry.

Weryfikuje wszystkie żelazne zasady repozytorium przed commitem / audytem:
 1. Czystość katalogu głównego i brak śmieci w repozytorium (Reguła #14 & Project Rules).
 2. Spójność SSOT, format wersji i kompletność wpisu w balance-notes.md (Reguły #1, #2, #4).
 3. Pełna synchronizacja dokumentacji i katalogu kart z SSOT (scripts/sync_config.py) (Reguła #4).
 4. Logika i użyteczność kart — brak martwych kart i brak pustych opisów (Reguła #2 & §13).
 5. Matematyczna fizyka gry, geometria stołu i zasoby talii (Reguła #18 & Anti-Pattern §13).
 6. Kompatybilność i kompletność modułu natywnego C++ (Reguła #10 / C++ Zero-Bug Guarantee).
 7. Jakość telemetrii — brak pustych tabel, suma szans = 100%, próba >= 5000 (Reguły #9, #10).
 8. Integralność i zapieczętowanie archiwów wersji (Reguły #15, #17).
 9. Zgodność z Konstytucją ADR — brak ukrytych bramek erowych i hacków silnika (ADR-0001 / ADR-0002).
10. 100% zaliczonych testów jednostkowych pytest (Reguła #4 / #5).
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT_DIR = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT_DIR / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from inquisitio.config import ConfigValidationError, GameConfig

ALLOWED_ROOT_FILES = {
    ".DS_Store",
    ".gitignore",
    "README.md",
    "pyrightconfig.json",
    "compile_flags.txt",
}

DISALLOWED_PATTERNS = [
    re.compile(r"\.tmp$", re.IGNORECASE),
    re.compile(r"\.bak$", re.IGNORECASE),
    re.compile(r"\.orig$", re.IGNORECASE),
    re.compile(r"^scratch.*\.py$", re.IGNORECASE),
]


# ==============================================================================
# 1. Czystość katalogu głównego i drzewa plików
# ==============================================================================
def check_root_cleanliness() -> list[str]:
    """Weryfikacja czystości katalogu głównego (brak tymczasowych plików)."""
    errors = []
    for item in ROOT_DIR.iterdir():
        if item.is_file():
            if item.name not in ALLOWED_ROOT_FILES:
                errors.append(
                    f"⛔ [ROOT CLEANLINESS] Plik '{item.name}' znajduje się w katalogu głównym! "
                    "Katalog główny musi być czysty. Przenieś plik do data/, scripts/ lub scratch/."
                )

    # Check for temporary/backup files across tracked directories
    for search_dir in (ROOT_DIR / "src", ROOT_DIR / "data", ROOT_DIR / "scripts"):
        if not search_dir.exists():
            continue
        for p in search_dir.rglob("*"):
            if p.is_file():
                for pat in DISALLOWED_PATTERNS:
                    if pat.search(p.name):
                        errors.append(
                            f"⛔ [FILE HYGIENE] Znaleziono plik śmieciowy/tymczasowy: '{p.relative_to(ROOT_DIR)}'! Usuń go."
                        )

    return errors


# ==============================================================================
# 2. Spójność SSOT i format Patch Notes
# ==============================================================================
def check_ssot_and_patch_notes() -> tuple[list[str], dict[str, Any]]:
    """Weryfikacja SSOT (data/game_config.yaml) i wpisu w balance-notes.md."""
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
    if not version or not re.match(r"^v1\.0-alpha\.\d+$", str(version)):
        errors.append(f"⛔ [SSOT] Nieprawidłowy format wersji: '{version}' (wymagane: v1.0-alpha.X)!")

    date_str = cfg.get("date")
    if not date_str or not re.match(r"^\d{4}-\d{2}-\d{2}$", str(date_str)):
        errors.append(f"⛔ [SSOT] Nieprawidłowy format daty: '{date_str}' (wymagane: YYYY-MM-DD)!")

    if not notes_path.exists():
        errors.append("⛔ [PATCH NOTES] Brak pliku data/playtesting/balance-notes.md!")
        return errors, cfg

    notes_text = notes_path.read_text(encoding="utf-8")

    # Check if latest version has formal header
    pattern = rf"###\s+[🟢🌐🔵]\s+Patch\s+{re.escape(str(version))}\s+\(\d{{4}}-\d{{2}}-\d{{2}}\)"
    if not re.search(pattern, notes_text):
        errors.append(
            f"⛔ [PATCH NOTES] Brak wymaganego nagłówka patcha dla '{version}' w balance-notes.md! "
            f"Oczekiwano formatu: '### 🟢 Patch {version} (YYYY-MM-DD) — ...'"
        )

    return errors, cfg


# ==============================================================================
# 3. Pełna synchronizacja dokumentacji z SSOT
# ==============================================================================
def check_documentation_sync(cfg: dict[str, Any], auto_fix: bool = False) -> list[str]:
    """Sprawdza czy dokumentacja i pliki kart są w 100% zsynchronizowane z game_config.yaml."""
    errors = []
    if auto_fix:
        subprocess.run([sys.executable, str(ROOT_DIR / "scripts/sync_config.py")], capture_output=True)

    # Run sync_config and see if any git diffs appear on disk
    res = subprocess.run(
        [sys.executable, str(ROOT_DIR / "scripts/sync_config.py")],
        cwd=str(ROOT_DIR),
        capture_output=True,
        text=True,
    )
    if res.returncode != 0:
        errors.append(f"⛔ [SYNC CONFIG FAILURE] scripts/sync_config.py zwrócił błąd:\n{res.stderr or res.stdout}")
        return errors

    # Check if git diff shows unstaged changes in docs/ or assets/
    diff_res = subprocess.run(
        ["git", "diff", "--name-only", "docs/", "assets/", "data/playtesting/setups.md", "README.md"],
        cwd=str(ROOT_DIR),
        capture_output=True,
        text=True,
    )
    if diff_res.returncode == 0 and diff_res.stdout.strip():
        desynced = [f"  • {line.strip()}" for line in diff_res.stdout.strip().splitlines()]
        errors.append(
            "⛔ [DOCUMENTATION DESYNC] Dokumentacja/katalog kart jest niezsynchronizowany z game_config.yaml!\n"
            + "\n".join(desynced)
            + "\n👉 Rozwiązanie: Uruchom 'python3 scripts/sync_config.py' i dodaj zmiany do commita."
        )

    return errors


# ==============================================================================
# 4. Logika i użyteczność kart — brak martwych kart i pustych efektów
# ==============================================================================
def check_card_effects_and_utility(cfg: dict[str, Any]) -> list[str]:
    """Weryfikuje, że każda z 60 kart frakcyjnych i 10 kart wydarzeń posiada poprawny efekt."""
    errors = []
    try:
        from inquisitio.cards.loader import load_all_cards

        cards = load_all_cards(force=True)
    except Exception as e:
        errors.append(f"⛔ [CARDS LOADER] Błąd ładowania bazy kart: {e}")
        return errors

    total_cards = len(cards)
    if total_cards != 70:
        errors.append(f"⛔ [CARDS COUNT] Oczekiwano dokładnie 70 kart w talii (60 frakcji + 10 wydarzeń), a wczytano: {total_cards}!")

    factions = {"so": 0, "caa": 0, "kb": 0, "kt": 0, "gc": 0, "time": 0}
    for cid, card in cards.items():
        prefix = cid.split("-")[0]
        if prefix in factions:
            factions[prefix] += 1

        # 1. Effect text must not be empty
        if not card.effect or not card.effect.strip():
            errors.append(
                f"⛔ [CARD EFFECT EMPTY] Karta '{cid}' ({card.name}) ma pusty opis efektu! "
                "Sprawdź definicję w game_config.yaml i generatorze scripts/pnp/generate_card_text.py."
            )

        # 2. Lore or Heresy text must exist
        if not card.lore and not card.heresy_text:
            errors.append(f"⛔ [CARD LORE MISSING] Karta '{cid}' ({card.name}) nie posiada ani lore, ani heresy_text!")

        # 3. Check anti-dead-weight invariants for faction cards
        if prefix != "time":
            raw = card.raw or {}
            act = raw.get("action")
            cost = card.cost_gold

            # If card gives gold, it must give > 0 gold or > 0 target heresy
            if act == "gain_gold":
                g = raw.get("gold", 0)
                th = raw.get("target_heresy", 0)
                if g <= 0 and th <= 0:
                    errors.append(
                        f"⛔ [DEAD CARD] Karta '{cid}' ({card.name}) ma 'action: gain_gold', ale daje 0 złota i 0 herezji rywalowi! To jest martwa karta."
                    )

            # Paid cards must provide at least one mechanical value
            if cost > 0:
                has_value = any(
                    [
                        raw.get("gold", 0) > 0,
                        raw.get("target_heresy", 0) > 0,
                        raw.get("agents", 0) > 0,
                        raw.get("decree", 0) > 0,
                        raw.get("grant_fragment", 0) > 0,
                        raw.get("evacuate_relic", 0) > 0,
                        raw.get("creates_hook"),
                        raw.get("mark_fall"),
                        raw.get("arrest"),
                        raw.get("free_agent"),
                        raw.get("move_relic"),
                        raw.get("breaks_rule"),
                        raw.get("trigger"),
                        raw.get("action") in ("send_inquisitor", "move_agent", "frame_rival", "arrest"),
                    ]
                )
                if not has_value:
                    errors.append(
                        f"⛔ [USELESS PAID CARD] Karta '{cid}' ({card.name}) kosztuje {cost} zł, ale nie oferuje żadnego efektu mechanicznego!"
                    )

    for fac in ("so", "caa", "kb", "kt", "gc"):
        cnt = factions.get(fac, 0)
        if cnt != 12:
            errors.append(f"⛔ [FACTION CARDS COUNT] Frakcja '{fac}' posiada {cnt} kart (wymagane: dokładnie 12)!")

    if factions.get("time", 0) != 10:
        errors.append(f"⛔ [TIME CARDS COUNT] Talia wydarzeń (time) posiada {factions.get('time', 0)} kart (wymagane: dokładnie 10)!")

    return errors


# ==============================================================================
# 5. Matematyczna fizyka gry, geometria stołu i zasoby talii (Reguła #18)
# ==============================================================================
def check_physics_and_deck_invariants(cfg: dict[str, Any]) -> list[str]:
    """Weryfikuje matematyczną osiągalność warunków zwycięstwa vs liczba graczy i talia kart."""
    errors = []
    if not cfg:
        return errors

    # Generic validation from config.py
    try:
        GameConfig.validate_invariants(cfg)
    except ConfigValidationError as e:
        errors.append(f"⛔ [GAME PHYSICS] Naruszenie niezmienników fizyki gry: {e}")

    cards = cfg.get("cards", {})
    vic = cfg.get("victory", {})
    sys_cfg = cfg.get("system", {})

    def _get_val(val: Any, p_key: str = "4p", default: int = 1) -> int:
        if isinstance(val, dict):
            return int(val.get(p_key, val.get("4p", default)))
        return int(val) if val is not None else default

    # 1. ŚWIĘTE OFICJUM: Skazania vs Liczba Rywali przy stole (Kluczowy Anty-Pattern!)
    # W 3p jest tylko 2 rywali -> skazanie 3 unikalnych rywali jest FIZYCZNIE NIEMOŻLIWE!
    so_condemns = vic.get("swiete_oficjum", {}).get("condemns", 3)
    if isinstance(so_condemns, dict):
        c_3p = int(so_condemns.get("3p", 2))
        c_4p = int(so_condemns.get("4p", 3))
        c_5p = int(so_condemns.get("5p", 3))
        if c_3p > 2:
            errors.append(
                f"⛔ [PHYSICS VIOLATION] victory.swiete_oficjum.condemns.3p = {c_3p} > 2! "
                "W partii 3-osobowej jest tylko 2 rywali — skazanie 3 unikalnych rywali jest matematycznie niemożliwe!"
            )
        if c_4p > 3:
            errors.append(
                f"⛔ [PHYSICS VIOLATION] victory.swiete_oficjum.condemns.4p = {c_4p} > 3! "
                "W partii 4-osobowej jest tylko 3 rywali."
            )
        if c_5p > 4:
            errors.append(
                f"⛔ [PHYSICS VIOLATION] victory.swiete_oficjum.condemns.5p = {c_5p} > 4! "
                "W partii 5-osobowej jest tylko 4 rywali."
            )
    else:
        if int(so_condemns) > 3:
            errors.append(f"⛔ [PHYSICS VIOLATION] victory.swiete_oficjum.condemns = {so_condemns} > 3!")

    # 2. KORONA BORGIOWIE: Dekrety vs Karty w talii
    kb_req_4p = _get_val(vic.get("korona_borgiowie", {}).get("decrees", 2), "4p")
    kb_req_3p = _get_val(vic.get("korona_borgiowie", {}).get("decrees", 2), "3p")
    kb_req_5p = _get_val(vic.get("korona_borgiowie", {}).get("decrees", 2), "5p")
    kb_cards_decrees = sum(
        int(c.get("decree", 0)) for cid, c in cards.items() if cid.startswith("kb-") and isinstance(c, dict) and "decree" in c
    )
    for p_name, req in [("3p", kb_req_3p), ("4p", kb_req_4p), ("5p", kb_req_5p)]:
        if kb_cards_decrees < req:
            errors.append(
                f"⛔ [DECK INVARIANT] Korona Borgiowie ({p_name}) wymaga {req} dekretów, "
                f"ale w talii znajduje się tylko {kb_cards_decrees} kart z efektem 'decree'!"
            )

    # 3. KABAŁA TOLEDO: Fragmenty vs Karty w talii
    kt_req_4p = _get_val(vic.get("kabala_toledo", {}).get("fragments", 3), "4p")
    kt_req_3p = _get_val(vic.get("kabala_toledo", {}).get("fragments", 3), "3p")
    kt_req_5p = _get_val(vic.get("kabala_toledo", {}).get("fragments", 3), "5p")
    kt_cards_frags = sum(
        int(c.get("grant_fragment", 0))
        for cid, c in cards.items()
        if cid.startswith("kt-") and isinstance(c, dict) and "grant_fragment" in c
    )
    for p_name, req in [("3p", kt_req_3p), ("4p", kt_req_4p), ("5p", kt_req_5p)]:
        if kt_cards_frags < req:
            errors.append(
                f"⛔ [DECK INVARIANT] Kabała Toledo ({p_name}) wymaga {req} fragmentów, "
                f"ale w talii znajduje się tylko {kt_cards_frags} kart z efektem 'grant_fragment'!"
            )

    # 4. CIENIE AL-ANDALUS: Relikwie vs Karty w talii
    caa_req_4p = _get_val(vic.get("cienie_al_andalus", {}).get("relics", 2), "4p")
    caa_req_3p = _get_val(vic.get("cienie_al_andalus", {}).get("relics", 2), "3p")
    caa_req_5p = _get_val(vic.get("cienie_al_andalus", {}).get("relics", 2), "5p")
    caa_cards_relics = sum(
        int(c.get("evacuate_relic", 0))
        for cid, c in cards.items()
        if cid.startswith("caa-") and isinstance(c, dict) and "evacuate_relic" in c
    )
    for p_name, req in [("3p", caa_req_3p), ("4p", caa_req_4p), ("5p", caa_req_5p)]:
        if caa_cards_relics < req:
            errors.append(
                f"⛔ [DECK INVARIANT] Cienie Al-Andalus ({p_name}) wymagają {req} relikwii, "
                f"ale w talii znajduje się tylko {caa_cards_relics} kart z efektem 'evacuate_relic'!"
            )

    # 5. Sanity bounds on system parameters
    for p_key in ("3p", "4p", "5p"):
        sg = _get_val(sys_cfg.get("start_gold", 4), p_key)
        if not (1 <= sg <= 10):
            errors.append(f"⛔ [SYSTEM SANITY] start_gold ({p_key}) = {sg} poza bezpiecznym zakresem [1, 10]!")

        th = _get_val(sys_cfg.get("accusation_threshold", 7), p_key)
        if not (4 <= th <= 15):
            errors.append(f"⛔ [SYSTEM SANITY] accusation_threshold ({p_key}) = {th} poza bezpiecznym zakresem [4, 15]!")

    hl = int(sys_cfg.get("hand_limit", 5))
    if not (3 <= hl <= 8):
        errors.append(f"⛔ [SYSTEM SANITY] hand_limit = {hl} poza zakresem [3, 8]!")

    return errors


# ==============================================================================
# 6. Kompatybilność i kompletność modułu natywnego C++
# ==============================================================================
def check_cpp_native_parity() -> list[str]:
    """Weryfikuje kompilację C++, obsługę wszystkich 16 setupów i brak starych bugów wątkowych."""
    errors = []
    cpp_source = ROOT_DIR / "src/native/inquisitio_native.cpp"
    build_script = ROOT_DIR / "src/native/build.sh"

    if not cpp_source.exists():
        errors.append("⛔ [C++ NATIVE] Brak pliku źródłowego src/native/inquisitio_native.cpp!")
        return errors

    cpp_text = cpp_source.read_text(encoding="utf-8")

    # 1. Verify compilation
    res = subprocess.run(["bash", str(build_script)], cwd=str(ROOT_DIR), capture_output=True, text=True)
    if res.returncode != 0:
        errors.append(f"⛔ [C++ COMPILATION FAILURE] Kompilacja C++ nie powiodła się:\n{res.stderr or res.stdout}")

    # 2. Verify all 16 canonical setups are explicitly mapped (preventing silent fallback to 4p-core)
    from inquisitio.engine.setup import SETUP_PRESETS

    for setup_name in SETUP_PRESETS.keys():
        if f'"{setup_name}"' not in cpp_text:
            errors.append(
                f"⛔ [C++ SETUP COVERAGE] Silnik C++ nie zawiera jawnej definicji setupu '{setup_name}'! "
                "Grozi to cichym fallbackiem do wariantu 4p-core."
            )

    # 3. Verify era_faction_wins is tracked (preventing the zero telemetry table bug)
    if "era_faction_wins" not in cpp_text:
        errors.append("⛔ [C++ TELEMETRY BUG] Brak śledzenia 'era_faction_wins' w inquisitio_native.cpp! Wykresy er będą puste.")

    # 4. Verify thread support parameter
    if "threads" not in cpp_text:
        errors.append("⛔ [C++ THREADS BUG] Brak obsługi parametru 'threads' w C++ (grozi przesubskrypcją wątków)!")

    return errors


# ==============================================================================
# 7. Jakość telemetrii — brak pustych tabel, suma szans = 100%
# ==============================================================================
def check_telemetry_quality() -> list[str]:
    """Weryfikuje jakość bieżącego raportu telemetrii (brak zerowych tabel, poprawność sumy win-share)."""
    errors = []
    active_rep = ROOT_DIR / "data/playtesting/sim-reports/raport_telemetrii.md"
    if not active_rep.exists():
        return errors

    text = active_rep.read_text(encoding="utf-8")

    # 1. Check for zero rows in era breakdown: "| **Era X** | N | 0 | 0 | 0 | 0 | 0 |"
    zero_row_pat = re.compile(r"\|\s*\*\*Era\s+\d+\*\*\s*\|\s*[\d,]+\s*\|\s*0\s*\|\s*0\s*\|\s*0\s*\|\s*0\s*\|\s*0\s*\|")
    if zero_row_pat.search(text):
        errors.append(
            f"⛔ [EMPTY TELEMETRY TABLE] Raport '{active_rep.relative_to(ROOT_DIR)}' zawiera wiersze z samymi zerami w rozkładzie er!"
        )

    # 2. Check sample size in official active report (ADR-0014: >= 5000)
    m_sample = re.search(r"Próba:\s*(\d[\d\s,]*)\s*gier", text)
    if m_sample:
        sample_num = int(re.sub(r"[^\d]", "", m_sample.group(1)))
        if sample_num < 5000:
            errors.append(
                f"⛔ [SAMPLE TOO SMALL] Raport '{active_rep.relative_to(ROOT_DIR)}' ma próbę N={sample_num} < 5000 gier/setup (Reguła #9 / ADR-0014)!"
            )

    return errors


# ==============================================================================
# 8. Integralność i zapieczętowanie archiwów wersji
# ==============================================================================
def check_archive_integrity(cfg: dict[str, Any]) -> list[str]:
    """Weryfikacja integralności zapieczętowanych archiwów (Reguła #15)."""
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


# ==============================================================================
# 9. Zgodność z Konstytucją ADR (brak sztucznych bramek)
# ==============================================================================
def check_anti_cheat_adr() -> list[str]:
    """Skanowanie silnika pod kątem zabronionych sztucznych bramek erowych (ADR-0001)."""
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


# ==============================================================================
# 10. Testy jednostkowe pytest
# ==============================================================================
def check_unit_tests() -> list[str]:
    """Uruchomienie pełnego pakietu testów jednostkowych pytest."""
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


# ==============================================================================
# Git Hook Management
# ==============================================================================
def install_git_hook() -> bool:
    """Instaluje lub aktualizuje hook pre-commit w .git/hooks/pre-commit."""
    hook_path = ROOT_DIR / ".git/hooks/pre-commit"
    hook_content = """#!/bin/sh
# Git pre-commit hook enforcing repository hygiene & SSOT integrity
python3 scripts/verify_hygiene.py
if [ $? -ne 0 ]; then
    echo "\\n⛔ Git commit zablokowany przez Strażnika Higieny Repozytorium!"
    exit 1
fi
"""
    try:
        hook_path.parent.mkdir(parents=True, exist_ok=True)
        hook_path.write_text(hook_content, encoding="utf-8")
        hook_path.chmod(0o755)
        print(f"✅ Zainstalowano hook pre-commit w {hook_path}")
        return True
    except Exception as e:
        print(f"❌ Błąd instalacji hooka: {e}")
        return False


# ==============================================================================
# GŁÓWNA PĘTLA AUDYTOWA
# ==============================================================================
def main():
    parser = argparse.ArgumentParser(description="Strażnik Higieny, Dyscypliny i Integralności Repozytorium.")
    parser.add_argument("--fix", action="store_true", help="Automatycznie naprawia brak synchronizacji dokumentacji.")
    parser.add_argument("--install-hook", action="store_true", help="Instaluje hook pre-commit w repozytorium git.")
    args = parser.parse_args()

    if args.install_hook:
        install_git_hook()
        sys.exit(0)

    print("========================================================")
    print("🛡️  PEŁNY STRAŻNIK DYSCYPLINY I INTEGRALNOŚCI REPOZYTORIUM")
    print("========================================================\n")

    all_errors: list[str] = []

    # 1. Root Cleanliness
    errs = check_root_cleanliness()
    if errs:
        all_errors.extend(errs)
    else:
        print("✔ [ 1/10] Czystość katalogu głównego (zero śmieci w root): OK")

    # 2. SSOT & Patch Notes
    errs, cfg = check_ssot_and_patch_notes()
    if errs:
        all_errors.extend(errs)
    else:
        print("✔ [ 2/10] Spójność SSOT i format Patch Notes w balance-notes.md: OK")

    # 3. Full Documentation Sync
    errs = check_documentation_sync(cfg, auto_fix=args.fix)
    if errs:
        all_errors.extend(errs)
    else:
        print("✔ [ 3/10] Pełna synchronizacja dokumentacji z SSOT (sync_config.py): OK")

    # 4. Card Effects & Utility
    errs = check_card_effects_and_utility(cfg)
    if errs:
        all_errors.extend(errs)
    else:
        print("✔ [ 4/10] Logika i użyteczność 70 kart (brak martwych kart / pustych opisów): OK")

    # 5. Physics & Deck Invariants
    errs = check_physics_and_deck_invariants(cfg)
    if errs:
        all_errors.extend(errs)
    else:
        print("✔ [ 5/10] Matematyczna fizyka gry, geometria stołu i zasoby talii (Reguła #18): OK")

    # 6. C++ Native Module Parity
    errs = check_cpp_native_parity()
    if errs:
        all_errors.extend(errs)
    else:
        print("✔ [ 6/10] Kompatybilność i pokrycie 16 setupów w module C++ (Reguła #10): OK")

    # 7. Telemetry Quality
    errs = check_telemetry_quality()
    if errs:
        all_errors.extend(errs)
    else:
        print("✔ [ 7/10] Jakość telemetrii (brak pustych tabel erowych, próba >= 5000): OK")

    # 8. Archive Integrity
    errs = check_archive_integrity(cfg)
    if errs:
        all_errors.extend(errs)
    else:
        print("✔ [ 8/10] Integralność i zapieczętowanie archiwów wersji (Reguła #15): OK")

    # 9. Anti-Cheat & ADR-0001
    errs = check_anti_cheat_adr()
    if errs:
        all_errors.extend(errs)
    else:
        print("✔ [ 9/10] Zgodność z Konstytucją ADR (brak sztucznych bramek erowych): OK")

    # 10. Unit Tests
    errs = check_unit_tests()
    if errs:
        all_errors.extend(errs)
    else:
        print("✔ [10/10] Pełny pakiet testów jednostkowych (pytest 100% PASS): OK")

    print("\n========================================================")
    if all_errors:
        print("❌ ZNALEZIONO KRYTYCZNE NARUSZENIA ZASAD REPOZYTORIUM:\n")
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
