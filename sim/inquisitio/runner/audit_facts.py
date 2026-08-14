from __future__ import annotations
import shutil
from pathlib import Path
from inquisitio.config import CONFIG
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


def split_and_sort_audit_results(results: list[dict], base: dict) -> tuple[list[dict], list[dict]]:
    """Splits results into (positives, negatives).
    Positive: has ANY category or global delta > 0.
    Strictly negative: all categories and global deltas <= 0.
    Both lists are sorted descending by global delta (primary) and max category delta (secondary).
    The base result is always the first item in positives.
    """
    positives = [base]
    negatives = []

    for r in results[1:]:
        g_diff = r["global_score"] - base["global_score"]
        d_3p = r["cat_scores"].get("3p", 0.0) - base["cat_scores"].get("3p", 0.0)
        d_4p = r["cat_scores"].get("4p", 0.0) - base["cat_scores"].get("4p", 0.0)
        d_5p = r["cat_scores"].get("5p", 0.0) - base["cat_scores"].get("5p", 0.0)

        if g_diff > 0.001 or d_3p > 0.001 or d_4p > 0.001 or d_5p > 0.001:
            positives.append(r)
        else:
            negatives.append(r)

    # Sort positives (excluding base which stays at index 0)
    non_base_pos = sorted(
        positives[1:],
        key=lambda x: (
            x["global_score"] - base["global_score"],
            max(
                x["cat_scores"].get("3p", 0.0) - base["cat_scores"].get("3p", 0.0),
                x["cat_scores"].get("4p", 0.0) - base["cat_scores"].get("4p", 0.0),
                x["cat_scores"].get("5p", 0.0) - base["cat_scores"].get("5p", 0.0),
            ),
        ),
        reverse=True,
    )
    positives = [base] + non_base_pos

    # Sort negatives descending by global delta (least negative first)
    negatives = sorted(
        negatives,
        key=lambda x: x["global_score"] - base["global_score"],
        reverse=True,
    )

    return positives, negatives


def save_and_archive_report(
    report_lines: list[str],
    filename: str,
    custom_out: str | None = None,
) -> tuple[Path, Path | None]:
    """Write report to playtesting/sim-reports/ and archive with game_config.yaml snapshot."""
    if custom_out:
        out_path = Path(custom_out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text("\n".join(report_lines), encoding="utf-8")
        return out_path, None

    repo_root = Path(__file__).resolve().parent.parent.parent.parent
    base_dir = repo_root / "playtesting" / "sim-reports"
    archive_dir = base_dir / "archive" / CONFIG.version

    out_path = base_dir / filename
    archive_path = archive_dir / filename

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(report_lines), encoding="utf-8")

    archive_dir.mkdir(parents=True, exist_ok=True)
    archive_path.write_text("\n".join(report_lines), encoding="utf-8")

    # Automatically snapshot game_config.yaml in the archive folder
    config_src = repo_root / "game_config.yaml"
    if config_src.exists():
        shutil.copy2(config_src, archive_dir / "game_config.yaml")

    return out_path, archive_path
