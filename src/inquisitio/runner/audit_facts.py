from __future__ import annotations
import shutil
from pathlib import Path
from inquisitio.config import CONFIG
from inquisitio.runner.scoring import color_score


def fmt_signed(val: float) -> str:
    if val > 0.05:
        return f"⬆️ +{val:.1f}"
    if val < -0.05:
        return f"🔻 {val:.1f}"
    return "= 0.0"


def score_pair(old: float, new: float, *, colored: bool = False) -> str:
    """Show baza → test (Δ) with explicit +/- indicators for full transparency."""
    d = new - old
    new_s = color_score(new, bold=True) if colored else f"{new:.1f}"
    if abs(d) < 0.05:
        return f"{old:.1f} → {new_s} (`= 0.0`)"
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
    min_games_per_setup: int | None = None,
) -> tuple[Path, Path]:
    """Write report directly to data/playtesting/sim-reports/archive/{version}/ with game_config.yaml snapshot.
    Enforces ADR-0014: Hard prohibition on saving reports with < 5000 games per setup.
    """
    if min_games_per_setup is not None and min_games_per_setup < 5000:
        raise ValueError(
            f"⛔ ADR-0014 VIOLATION: ZAKAZ zapisu raportu do pliku przy próbie {min_games_per_setup} < 5000 gier per setup!"
        )

    # Secondary text scan check to prevent bypasses
    report_text = "\n".join(report_lines)
    import re
    m = re.search(r"Wielkość Próby:\s*(\d+)\s*gier/setup", report_text)
    if m:
        sample_detected = int(m.group(1))
        if sample_detected < 5000:
            raise ValueError(
                f"⛔ ADR-0014 VIOLATION: Wykryto próbę {sample_detected} gier/setup < 5000. Raport nie może być zapisany jako plik!"
            )

    if custom_out:
        out_path = Path(custom_out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(report_text, encoding="utf-8")
        return out_path, out_path

    repo_root = Path(__file__).resolve().parent.parent.parent.parent
    base_dir = repo_root / "data" / "playtesting" / "sim-reports"
    archive_dir = base_dir / "archive" / CONFIG.version

    archive_path = archive_dir / filename

    archive_dir.mkdir(parents=True, exist_ok=True)
    archive_path.write_text(report_text, encoding="utf-8")

    # Automatically snapshot game_config.yaml in the archive folder
    config_src = repo_root / "data/game_config.yaml"
    if config_src.exists():
        shutil.copy2(config_src, archive_dir / "game_config.yaml")

    return archive_path, archive_path
