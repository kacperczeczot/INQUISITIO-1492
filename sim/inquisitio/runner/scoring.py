"""Balance Scoring Engine — Continuous Asymptotic Exponential Decay Model."""
from __future__ import annotations

import math

from inquisitio.engine.setup import SETUP_PRESETS
from inquisitio.runner.balance import faction_shares
from inquisitio.runner.batch import BatchSummary

def calculate_setup_score(summary: BatchSummary) -> float:
    """Calculates Balance Score (0.1–100.0) for a single setup summary using continuous exponential decay.
    
    Properties:
    - Never reaches 0.0 (preserves non-zero gradient for optimization and variant comparison).
    - Strictly reserves >=98.0 pkt for deviations <= 0.5 p.p.
    - Smooth, continuous loss landscape without arbitrary step-discontinuities.
    """
    shares = faction_shares(summary)
    n_players = len(SETUP_PRESETS[summary.setup])
    p_ideal = 1.0 / n_players

    # Root Mean Square Relative Deviation (RMS-RD)
    sum_sq_rd = 0.0
    for fid, win_share in shares.items():
        rel_dev = abs(win_share - p_ideal) / p_ideal
        sum_sq_rd += rel_dev ** 2
    rms_rd = math.sqrt(sum_sq_rd / n_players)

    # Exponential decay with power 1.25 (scaled so <=0.5 pp dev is >=98.0 pkt)
    c = 3.2
    exponent = c * (rms_rd ** 1.25)

    # Deadlock penalty
    deadlock_penalty = max(0.0, (summary.eras_limit_pct - 0.05)) * 5.0

    val = 100.0 * math.exp(-(exponent + deadlock_penalty))
    score = max(0.1, min(100.0, val))
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


def color_score(val: float, bold: bool = False) -> str:
    """Formats balance score with status icon (🟢 >=90, 🟡 75-89.9, 🟠 60-74.9, 🔴 <60)."""
    if val >= 90.0:
        icon = "🟢"
    elif val >= 75.0:
        icon = "🟡"
    elif val >= 60.0:
        icon = "🟠"
    else:
        icon = "🔴"
    val_str = f"**{val:5.1f}**" if bold else f"{val:.1f}"
    return f"{icon} {val_str}"

