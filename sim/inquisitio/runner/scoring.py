"""Balance Scoring Engine — Strict Relative Deviation Hierarchy."""
from __future__ import annotations

from inquisitio.engine.setup import SETUP_PRESETS
from inquisitio.runner.balance import BalanceGate, gate_for, faction_shares
from inquisitio.runner.batch import BatchSummary

def calculate_setup_score(summary: BatchSummary) -> float:
    """Calculates Balance Score (0–100) for a single setup summary using strict relative deviations."""
    gate = gate_for(summary.setup, summary.layer)
    shares = faction_shares(summary)
    n_players = len(SETUP_PRESETS[summary.setup])
    p_ideal = 1.0 / n_players

    total_penalty = 0.0
    for fid, win_share in shares.items():
        # Relative deviation from fair share
        rel_dev = abs(win_share - p_ideal) / p_ideal

        in_target = (gate.target_min <= win_share <= gate.target_max)
        in_critical = (gate.critical_min <= win_share <= gate.critical_max)

        if in_target:
            # Subtle penalty for slight target variations
            penalty = 40.0 * (rel_dev ** 2)
        elif in_critical:
            # Significant penalty for warning band (e.g. 11.8% vs 20.0% is 41% rel_dev)
            penalty = 120.0 * (rel_dev ** 1.5)
        else:
            # Harsh Red Line violation penalty
            penalty = 500.0 * rel_dev + 25.0

        total_penalty += penalty

    # Deadlock penalty
    if summary.eras_limit_pct > 0.05:
        total_penalty += (summary.eras_limit_pct - 0.05) * 200.0

    score = max(0.0, 100.0 - total_penalty)
    return round(score, 1)


def calculate_category_scores(summaries: list[BatchSummary]) -> dict[str, float]:
    """Calculates category scores for 3p, 4p, and 5p (averaging setup scores per category)."""
    scores_by_cat: dict[str, list[float]] = {"3p": [], "4p": [], "5p": []}

    for summary in summaries:
        n_players = len(SETUP_PRESETS[summary.setup])
        cat = f"{n_players}p"
        score = calculate_setup_score(summary)
        scores_by_cat[cat].append(score)

    return {
        cat: round(sum(vals) / len(vals), 1) if vals else 0.0
        for cat, vals in scores_by_cat.items()
    }


def calculate_global_score(category_scores: dict[str, float]) -> float:
    """Calculates unweighted global game balance score (3p, 4p, 5p equal 33.3% weight)."""
    valid_scores = [v for v in category_scores.values() if v > 0.0]
    if not valid_scores:
        return 0.0
    return round(sum(valid_scores) / len(valid_scores), 1)
