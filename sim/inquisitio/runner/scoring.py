"""Balance Scoring Engine — Continuous Asymptotic Exponential Decay Model with Mechanic Vitality Gate."""
from __future__ import annotations

from dataclasses import dataclass, field
import math

from inquisitio.engine.setup import SETUP_PRESETS
from inquisitio.runner.balance import faction_shares
from inquisitio.runner.batch import BatchSummary


@dataclass
class VitalityReport:
    is_healthy: bool
    status: str
    warnings: list[str] = field(default_factory=list)
    vitality_penalty: float = 0.0


def evaluate_vitality(summary: BatchSummary) -> VitalityReport:
    """Evaluates whether core faction mechanics and economic flow remain vibrant and alive.
    
    Prevents degenerate balance mutations where a faction 'balances' win rate
    by completely abandoning or losing access to its signature mechanics (e.g. 0 condemnations, 0 hooks).
    """
    factions = SETUP_PRESETS.get(summary.setup, [])
    warnings = []
    penalty = 0.0

    # 1. Economic Flow & Poverty Stress (Threshold > 15.0%)
    if summary.passes_forced_pct > 0.15:
        excess = (summary.passes_forced_pct - 0.15) * 8.0
        penalty += excess
        warnings.append(f"Zator Monetarny / Pas Biedy {summary.passes_forced_pct*100:.1f}% (>15%)")

    # 2. Deadlock Stress (Threshold > 5.0%)
    if summary.eras_limit_pct > 0.05:
        excess = (summary.eras_limit_pct - 0.05) * 10.0
        penalty += excess
        warnings.append(f"Paraliż Gry / Deadlocks {summary.eras_limit_pct*100:.1f}% (>5%)")

    # 3. Faction Mechanic Vitality Gates
    # Święte Oficjum: requires active court accusations and executions/stacks
    if "swiete-oficjum" in factions:
        if summary.accusations_avg < 0.5:
            penalty += 1.5
            warnings.append(f"Zanikanie Oskarżeń Oficjum ({summary.accusations_avg:.2f}/partię)")
        if summary.convictions_avg < 0.1 and summary.autodafe_avg < 0.1:
            penalty += 2.5
            warnings.append("Kastracja Wyroków Oficjum (brak Skazań i Stosów)")

    # Korona Borgiowie: requires active extortion network (hooks)
    if "korona-borgiowie" in factions:
        if summary.hooks_avg < 0.3:
            penalty += 1.5
            warnings.append(f"Zanikanie Haków Korony ({summary.hooks_avg:.2f}/partię)")

    # Gildia Cieni: requires active double-agents or blackmail
    if "gildia-cieni" in factions:
        if summary.doubles_avg < 0.05 and summary.hooks_avg < 0.2:
            penalty += 1.0
            warnings.append("Zanikanie Infiltracji Gildii Cieni")

    is_healthy = len(warnings) == 0
    if is_healthy:
        status = "🟢 Pełna Witalność"
    elif penalty < 2.0:
        status = "⚠️ Ostrzeżenie Witalności"
    else:
        status = "🔴 Zagrożenie Witalności (Kastracja Mechanik)"

    return VitalityReport(
        is_healthy=is_healthy,
        status=status,
        warnings=warnings,
        vitality_penalty=penalty,
    )


def calculate_setup_score(summary: BatchSummary) -> float:
    """Calculates Balance Score (0.1–100.0) for a single setup summary using continuous exponential decay.
    
    Properties:
    - Never reaches 0.0 (preserves non-zero gradient for optimization and variant comparison).
    - Strictly reserves >=98.0 pkt for deviations <= 0.5 p.p.
    - Integrates Mechanic Vitality Gate (penalizes mechanic castrations and flow deadlocks).
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

    # Vitality penalty (includes deadlock & mechanic vitality checks)
    vitality = evaluate_vitality(summary)
    total_penalty = vitality.vitality_penalty

    val = 100.0 * math.exp(-(exponent + total_penalty))
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

