"""Format baza → wariant for audit score tables."""
from __future__ import annotations

from inquisitio.runner.scoring import color_score


def fmt_signed(val: float) -> str:
    if val > 0:
        return f"⬆️ +{val:.1f}"
    return f"{val:.1f}"


def score_pair(old: float, new: float, *, colored: bool = False) -> str:
    """Show baza → test (Δ) only when the score moved."""
    d = new - old
    new_s = color_score(new, bold=True) if colored else f"{new:.1f}"
    if abs(d) < 0.05:
        return new_s
    return f"{old:.1f} → {new_s} (`{fmt_signed(d)}`)"


def delta_status(g_diff: float) -> str:
    if g_diff > 0.5:
        return "🟢 POPRAWIA GLOBALNIE"
    if g_diff < -0.5:
        return "🔴 POGARSZA GLOBALNIE"
    return "⚪ OPTYMALNY"
