"""Manual ablation hints from vitality diagnostics (no auto-removal)."""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

_SETUP_PREFIX_RE = re.compile(r"^(?P<setup>4p-[^:]+):\s*(?P<msg>.+)$")
_DEAD_PATH_RE = re.compile(
    r"Martwa ścieżka (?P<path>\S+) \((?P<fid>[^)]+)\): "
    r"(?P<n>\d+)/(?P<total>\d+) wygranych.*?gra tylko (?P<alive>\S+)"
)


@dataclass(frozen=True)
class ManualAblationCandidate:
    category: str
    severity: str
    setup: str | None
    title: str
    detail: str
    action: str


def _parse_setup_warning(raw: str) -> tuple[str | None, str]:
    m = _SETUP_PREFIX_RE.match(raw.strip())
    if m:
        return m.group("setup"), m.group("msg")
    return None, raw.strip()


def _dead_path_candidates(base_res: dict) -> list[ManualAblationCandidate]:
    out: list[ManualAblationCandidate] = []
    worst: dict[tuple[str, str], dict[str, Any]] = {}

    for raw in base_res.get("vitality_warnings") or []:
        setup, msg = _parse_setup_warning(raw)
        m = _DEAD_PATH_RE.search(msg)
        if not m:
            continue
        n = int(m.group("n"))
        total = int(m.group("total"))
        share = n / total if total else 0.0
        key = (m.group("fid"), m.group("path"))
        prev = worst.get(key)
        if prev is None or share < prev["share"]:
            worst[key] = {
                "setup": setup,
                "path": m.group("path"),
                "fid": m.group("fid"),
                "alive": m.group("alive"),
                "n": n,
                "total": total,
                "share": share,
            }

    for item in worst.values():
        out.append(
            ManualAblationCandidate(
                category="MARTWA_ŚCIEŻKA",
                severity="WYSOKA" if item["share"] < 0.05 else "ŚREDNIA",
                setup=item["setup"],
                title=f"{item['fid']}: klauzula „{item['path']}” praktycznie nie wygrywa",
                detail=(
                    f"{item['n']}/{item['total']} wygranych (<8%) — gra tylko przez „{item['alive']}”."
                ),
                action=(
                    "Ręcznie: potwierdź ablacją w feature_impact_4p.py; "
                    "rozważ usunięcie lub redesign martwej klauzuli zwycięstwa (audytor tego nie robi)."
                ),
            )
        )
    return out


def _telemetry_candidates(base_res: dict) -> list[ManualAblationCandidate]:
    out: list[ManualAblationCandidate] = []
    seen: set[str] = set()

    for raw in base_res.get("vitality_warnings") or []:
        setup, msg = _parse_setup_warning(raw)
        if "Paraliż Gry / Deadlocks" in msg:
            key = "deadlock"
            if key in seen:
                continue
            seen.add(key)
            out.append(
                ManualAblationCandidate(
                    category="TOKSYCZNA_TELEMETRIA",
                    severity="WYSOKA" if float(base_res.get("deadlock_pct") or 0) > 8 else "ŚREDNIA",
                    setup=setup,
                    title="Deadlocki powyżej progu zdrowia stołu",
                    detail=msg,
                    action=(
                        "Ręcznie: sprawdź limity Er, stosy i tempo gry. "
                        "Nie obniżaj progów zwycięstwa jako protezy — to decyzja projektowa."
                    ),
                )
            )
        elif "Zator Monetarny / Pas Biedy" in msg:
            key = "poverty"
            if key in seen:
                continue
            seen.add(key)
            out.append(
                ManualAblationCandidate(
                    category="TOKSYCZNA_TELEMETRIA",
                    severity="WYSOKA" if float(base_res.get("poverty_pct") or 0) > 25 else "ŚREDNIA",
                    setup=setup,
                    title="Pas biedy / zator monetarny",
                    detail=msg,
                    action=(
                        "Ręcznie: sprawdź przepływ złota, koszty kart i dochód ery. "
                        "Wyłączenie Gospodarczej to osobna decyzja po ablacji, nie patch ±1."
                    ),
                )
            )
    return out


def _faction_castration_candidates(base_res: dict) -> list[ManualAblationCandidate]:
    out: list[ManualAblationCandidate] = []
    seen: set[str] = set()

    for raw in base_res.get("vitality_warnings") or []:
        setup, msg = _parse_setup_warning(raw)
        if "Zanikanie Oskarżeń Oficjum" in msg:
            key = "so_acc"
        elif "Kastracja Wyroków Oficjum" in msg:
            key = "so_verdict"
        elif "Zanikanie Haków Korony" in msg:
            key = "kb_hooks"
        elif "Zanikanie Infiltracji Gildii Cieni" in msg:
            key = "gc_infil"
        else:
            continue
        if key in seen:
            continue
        seen.add(key)
        out.append(
            ManualAblationCandidate(
                category="Kastracja MECHANIKI",
                severity="WYSOKA",
                setup=setup,
                title="Mechanika frakcji praktycznie nie żyje przy stole",
                detail=msg,
                action=(
                    "Ręcznie: sprawdź koszty, warunki kart i AI — czy mechanika jest zablokowana regułą. "
                    "Usunięcie systemu tylko po potwierdzeniu ablacją."
                ),
            )
        )
    return out


def collect_manual_ablation_candidates(base_res: dict) -> list[ManualAblationCandidate]:
    """Build deduplicated manual-review list from the latest 4P baseline."""
    merged = (
        _dead_path_candidates(base_res)
        + _telemetry_candidates(base_res)
        + _faction_castration_candidates(base_res)
    )
    seen: set[tuple[str, str, str | None]] = set()
    out: list[ManualAblationCandidate] = []
    for item in merged:
        key = (item.category, item.title, item.setup)
        if key in seen:
            continue
        seen.add(key)
        out.append(item)
    severity_order = {"WYSOKA": 0, "ŚREDNIA": 1, "NISKA": 2}
    out.sort(key=lambda c: (severity_order.get(c.severity, 9), c.category, c.title))
    return out


def format_manual_ablation_report(
    candidates: list[ManualAblationCandidate],
    *,
    version: str,
    patches_applied: int,
) -> list[str]:
    lines = [
        f"# Kandydaci do ręcznej ablacji — Kanon 4P ({version})",
        "",
        f"**Wersja:** `{version}` | **Patchy w sesji:** {patches_applied}",
        "",
        "Lista diagnostyczna — **audytor nie usuwa mechanik automatycznie**. "
        "Każdy punkt wymaga ręcznej decyzji po `feature_impact_4p.py` lub redesignie reguł.",
        "",
    ]
    if not candidates:
        lines.append("Brak ostrzeżeń witalności wymagających ręcznej rewizji.")
        return lines

    lines.extend([
        "| Priorytet | Kategoria | Setup | Problem | Rekomendacja ręczna |",
        "| :---: | :--- | :--- | :--- | :--- |",
    ])
    for c in candidates:
        setup = f"`{c.setup}`" if c.setup else "—"
        lines.append(
            f"| {c.severity} | {c.category} | {setup} | **{c.title}** — {c.detail} | {c.action} |"
        )
    return lines


def print_manual_ablation_summary(
    candidates: list[ManualAblationCandidate],
    *,
    version: str,
    patches_applied: int,
) -> None:
    print("\n═══════════════════════════════════════════════════════════════════════")
    print("   KANDYDACI DO RĘCZNEJ ABLACJI (informacyjnie — audytor nie zatrzymuje)")
    print("═══════════════════════════════════════════════════════════════════════")
    print(f"Wersja końcowa: {version} | Patchy w sesji: {patches_applied}")
    if not candidates:
        print("   Brak ostrzeżeń witalności wymagających ręcznej rewizji.")
        return
    for idx, c in enumerate(candidates, 1):
        setup = f" [{c.setup}]" if c.setup else ""
        print(f"\n   {idx}. [{c.severity}] {c.category}{setup}")
        print(f"      {c.title}")
        print(f"      {c.detail}")
        print(f"      → {c.action}")
