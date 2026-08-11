"""Write drama-focused batch reports."""
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from inquisitio.runner.batch import BatchSummary

REPO_ROOT = Path(__file__).resolve().parents[3]
REPORT_DIR = REPO_ROOT / "playtesting" / "sim-reports"


def _ts() -> str:
    return datetime.now().strftime("%Y%m%d-%H%M%S")


def write_report(summary: BatchSummary) -> tuple[Path, Path]:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = _ts()
    base = f"drama-{summary.setup}-t{summary.threshold}-{stamp}"
    jp = REPORT_DIR / f"{base}.json"
    mp = REPORT_DIR / f"{base}.md"
    data = {
        "games": summary.games,
        "setup": summary.setup,
        "threshold": summary.threshold,
        "wins": summary.wins,
        "metrics": {
            "autodafe_avg": summary.autodafe_avg,
            "accusations_avg": summary.accusations_avg,
            "convictions_avg": summary.convictions_avg,
            "hooks_avg": summary.hooks_avg,
            "hooks_forced_avg": summary.hooks_forced_avg,
            "doubles_avg": summary.doubles_avg,
            "deadlocks_avg": summary.deadlocks_avg,
            "legal_moves_avg": summary.legal_moves_avg,
            "eras_avg": summary.eras_avg,
            "cards_played_avg": summary.cards_played_avg,
        },
        "note": "Wins are informational. Primary metrics: deadlock, legal moves, drama events.",
    }
    jp.write_text(json.dumps(data, indent=2), encoding="utf-8")
    md = [
        f"# Drama report — {summary.setup}",
        "",
        f"Games: {summary.games} · threshold: {summary.threshold}",
        "",
        "## Wins (informational)",
        "",
    ]
    for k, v in sorted(summary.wins.items(), key=lambda x: -x[1]):
        md.append(f"- {k}: {v}")
    md += [
        "",
        "## Drama / health metrics",
        "",
        f"- Autodafé / game: **{summary.autodafe_avg:.2f}**",
        f"- Accusations / game: **{summary.accusations_avg:.2f}**",
        f"- Convictions / game: **{summary.convictions_avg:.2f}**",
        f"- Hooks created / game: **{summary.hooks_avg:.2f}**",
        f"- Hooks forced / game: **{summary.hooks_forced_avg:.2f}**",
        f"- Doubles / game: **{summary.doubles_avg:.2f}**",
        f"- Deadlocks (no legal play) / game: **{summary.deadlocks_avg:.2f}**",
        f"- Legal moves sampled / game: **{summary.legal_moves_avg:.1f}**",
        f"- Eras / game: **{summary.eras_avg:.2f}**",
        f"- Cards played / game: **{summary.cards_played_avg:.1f}**",
        "",
        "> Sim filters deadlocks and drama frequency. Political balance = table.",
        "",
    ]
    mp.write_text("\n".join(md), encoding="utf-8")
    return jp, mp


def write_compare_report(results: dict[int, BatchSummary]) -> tuple[Path, Path]:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = _ts()
    jp = REPORT_DIR / f"compare-thresholds-{stamp}.json"
    mp = REPORT_DIR / f"compare-thresholds-{stamp}.md"
    payload = {
        str(k): {
            "wins": v.wins,
            "accusations_avg": v.accusations_avg,
            "deadlocks_avg": v.deadlocks_avg,
            "autodafe_avg": v.autodafe_avg,
        }
        for k, v in results.items()
    }
    jp.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    lines = ["# Threshold compare (drama experiment)", ""]
    for t, s in sorted(results.items()):
        lines.append(
            f"- t={t}: accusations={s.accusations_avg:.2f}, "
            f"autodafe={s.autodafe_avg:.2f}, deadlocks={s.deadlocks_avg:.2f}, wins={s.wins}"
        )
    lines.append("")
    mp.write_text("\n".join(lines), encoding="utf-8")
    return jp, mp
