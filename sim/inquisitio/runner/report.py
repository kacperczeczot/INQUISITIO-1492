from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from inquisitio.runner.batch import BatchSummary


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def default_report_dir() -> Path:
    return _repo_root() / "playtesting" / "sim-reports"


def write_report(
    summary: BatchSummary,
    *,
    out_dir: Path | None = None,
    label: str | None = None,
) -> tuple[Path, Path]:
    out_dir = out_dir or default_report_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    base = label or f"batch-t{summary.threshold}-{summary.setup}-{ts}"
    json_path = out_dir / f"{base}.json"
    md_path = out_dir / f"{base}.md"
    data = summary.to_dict()
    json_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    md_path.write_text(render_markdown(summary), encoding="utf-8")
    return json_path, md_path


def write_compare_report(
    results: dict[str, BatchSummary],
    *,
    out_dir: Path | None = None,
) -> tuple[Path, Path]:
    out_dir = out_dir or default_report_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    base = f"compare-7vs8-{ts}"
    json_path = out_dir / f"{base}.json"
    md_path = out_dir / f"{base}.md"
    payload = {k: v.to_dict() for k, v in results.items()}
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = ["# Compare thresholds\n"]
    for k, s in results.items():
        lines.append(f"## Próg {k}\n")
        lines.append(render_markdown(s))
        lines.append("")
    # quick delta
    if "7" in results and "8" in results:
        a, b = results["7"], results["8"]
        lines.append("## Delta (7 − 8)\n")
        lines.append(f"- accusations/game: {a.accusations - b.accusations:+.2f}")
        lines.append(f"- critical_entries/game: {a.critical_entries - b.critical_entries:+.2f}")
        lines.append(f"- verdicts/game: {a.verdicts - b.verdicts:+.2f}")
        lines.append(f"- stakes/game: {a.stakes - b.stakes:+.2f}")
        lines.append("")
        lines.append("Skopiuj metryki do `playtesting/balance-notes.md` (tabela A/B).")
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return json_path, md_path


def render_markdown(summary: BatchSummary) -> str:
    wins = "\n".join(f"| {k} | {v} | {100*v/summary.games:.1f}% |" for k, v in sorted(summary.wins.items()))
    heresy = "\n".join(
        f"| {k} | {v:.2f} |" for k, v in sorted(summary.max_heresy_avg.items())
    )
    return f"""# Batch {summary.setup} (próg {summary.threshold})

- Games: **{summary.games}**
- Avg eras: **{summary.avg_eras:.2f}**
- Critical entries / game: **{summary.critical_entries:.2f}**
- Accusations / game: **{summary.accusations:.2f}**
- Verdicts / game: **{summary.verdicts:.2f}**
- Stakes / game: **{summary.stakes:.2f}**
- Feint rate: **{summary.feint_rate:.1%}**
- Strategic accusation rate: **{summary.strategic_accusation_rate:.1%}**

## Wins

| Faction | Wins | Winrate |
| :--- | ---: | ---: |
{wins}

## Win reasons

{chr(10).join(f"- {k}: {v}" for k, v in sorted(summary.win_reasons.items()))}

## Avg max heresy seen

| Faction | Max heresy (avg) |
| :--- | ---: |
{heresy}
"""
