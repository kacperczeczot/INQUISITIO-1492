"""Balance Scoring Engine — win-share decay, plus a separate Mechanic Vitality Gate.

`calculate_balance_score` is win-share equality only.
`calculate_setup_score` is the legacy blend (win share + vitality in one exponent).
"""
from __future__ import annotations

from dataclasses import dataclass, field
import math

from inquisitio.engine.setup import SETUP_PRESETS
from inquisitio.runner.balance import faction_shares
from inquisitio.runner.batch import BatchSummary

# Dual win-paths that players can see. If a faction wins often but one path
# never fires, the unused clause is dead — not "healthy because accusations exist".
_DUAL_WIN_PATHS: tuple[tuple[str, str, str, str, str], ...] = (
    ("swiete-oficjum", "so_stacks", "so_condemns", "stosy", "skazania"),
)
_DEAD_PATH_MIN_WINS = 20
_DEAD_PATH_MIN_SHARE = 0.08
_DEAD_PATH_PENALTY = 1.2


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

    # Dual victory clauses: usage floors are not enough (hooks can be a tax).
    paths = summary.win_paths or {}
    for fid, path_a, path_b, label_a, label_b in _DUAL_WIN_PATHS:
        if fid not in factions:
            continue
        n_a = int(paths.get(path_a, 0))
        n_b = int(paths.get(path_b, 0))
        total = n_a + n_b
        if total < _DEAD_PATH_MIN_WINS:
            continue
        share_a = n_a / total
        share_b = n_b / total
        if share_b < _DEAD_PATH_MIN_SHARE:
            penalty += _DEAD_PATH_PENALTY
            warnings.append(
                f"Martwa ścieżka {label_b} ({fid}): {n_b}/{total} wygranych "
                f"(<{_DEAD_PATH_MIN_SHARE:.0%}) — gra tylko {label_a}"
            )
        if share_a < _DEAD_PATH_MIN_SHARE:
            penalty += _DEAD_PATH_PENALTY
            warnings.append(
                f"Martwa ścieżka {label_a} ({fid}): {n_a}/{total} wygranych "
                f"(<{_DEAD_PATH_MIN_SHARE:.0%}) — gra tylko {label_b}"
            )

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


def _win_share_decay(summary: BatchSummary) -> float:
    """RMS relative deviation of win shares, scaled for exponential score decay."""
    shares = faction_shares(summary)
    n_players = len(SETUP_PRESETS[summary.setup])
    p_ideal = 1.0 / n_players

    sum_sq_rd = 0.0
    for _fid, win_share in shares.items():
        rel_dev = abs(win_share - p_ideal) / p_ideal
        sum_sq_rd += rel_dev ** 2
    rms_rd = math.sqrt(sum_sq_rd / n_players)
    return 3.2 * (rms_rd ** 1.25)


def calculate_balance_score(summary: BatchSummary) -> float:
    """Win-share equality only (0.1–100.0). Does not apply vitality penalty.

    Use this for 4P canon ranking. Vitality is a separate gate, not part of this number.
    """
    val = 100.0 * math.exp(-_win_share_decay(summary))
    return round(max(0.1, min(100.0, val)), 1)


def calculate_setup_score(summary: BatchSummary) -> float:
    """Legacy setup score: win-share decay plus vitality penalty in the same exponent.

    Kept unchanged for 3p/5p auditors, L1–L4 reports, and historical comparability.
    """
    vitality = evaluate_vitality(summary)
    val = 100.0 * math.exp(-(_win_share_decay(summary) + vitality.vitality_penalty))
    return round(max(0.1, min(100.0, val)), 1)



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

