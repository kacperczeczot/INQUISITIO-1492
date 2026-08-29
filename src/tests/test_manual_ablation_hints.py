from __future__ import annotations

import sys
from pathlib import Path

SCRIPTS_SIM = Path(__file__).resolve().parents[2] / "scripts" / "sim"
if str(SCRIPTS_SIM) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_SIM))

from manual_ablation_hints import (
    collect_manual_ablation_candidates,
    format_manual_ablation_report,
)


def test_collects_dead_path_telemetry_and_faction_warnings():
    base = {
        "score_4p": 63.2,
        "vitality_penalty": 2.4,
        "eras_avg": 5.8,
        "deadlock_pct": 6.8,
        "poverty_pct": 18.0,
        "vitality_warnings": [
            "4p-core: Paraliż Gry / Deadlocks 6.8% (>5%)",
            "4p-core: Zanikanie Haków Korony (0.12/partię)",
            "4p-core: Martwa ścieżka skazania (swiete-oficjum): 19/1264 wygranych (<8%) — gra tylko stosy",
        ],
    }
    rows = collect_manual_ablation_candidates(base)
    categories = {r.category for r in rows}
    assert "MARTWA_ŚCIEŻKA" in categories
    assert "TOKSYCZNA_TELEMETRIA" in categories
    assert "Kastracja MECHANIKI" in categories
    assert all("Ręcznie:" in r.action for r in rows)


def test_report_empty_when_healthy():
    lines = format_manual_ablation_report([], version="v0.99.10", patches_applied=0)
    assert any("Brak ostrzeżeń" in line for line in lines)


def test_report_lists_candidates():
    base = {
        "score_4p": 63.2,
        "vitality_penalty": 1.2,
        "eras_avg": 5.8,
        "deadlock_pct": 6.8,
        "poverty_pct": 5.0,
        "vitality_warnings": [
            "4p-core: Paraliż Gry / Deadlocks 6.8% (>5%)",
        ],
    }
    rows = collect_manual_ablation_candidates(base)
    text = "\n".join(format_manual_ablation_report(rows, version="v0.99.10", patches_applied=2))
    assert "Deadlocki powyżej progu" in text
    assert "feature_impact_4p.py" not in text or "Ręcznie:" in text
