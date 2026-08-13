"""Telemetry Bounds Engine — Critical 2-tier (Target/RedLine) and Secondary 1-tier (Warning)."""
from __future__ import annotations
from dataclasses import dataclass
from inquisitio.runner.batch import BatchSummary

@dataclass(frozen=True)
class MetricCheckResult:
    metric_id: str
    name: str
    value: float
    status: str  # "OK", "WARNING", "CRITICAL"
    message: str

def evaluate_telemetry(summary: BatchSummary) -> list[MetricCheckResult]:
    results: list[MetricCheckResult] = []

    # --- KATEGORIA A: Mechaniki Krytyczne (2 Poziomy: Target vs Red Line) ---

    # 1. Średnia liczba Er (eras_avg)
    eras = summary.eras_avg
    if 5.0 <= eras <= 7.0:
        st, msg = "OK", "W normie (5.0–7.0 Er)"
    elif 4.0 <= eras <= 7.5:
        st, msg = "WARNING", f"Porażenie tempa: {eras:.2f} Er (zalecane 5.0–7.0)"
    else:
        st, msg = "CRITICAL", f"CRITICAL PACING: {eras:.2f} Er (Czerwona Linia: 4.0–7.5)"
    results.append(MetricCheckResult("eras_avg", "Średnia Liczba Er", eras, st, msg))

    # 2. Procent gier z limitem 8 Er (eras_limit_pct / Deadlocks)
    lim_pct = summary.eras_limit_pct * 100.0
    if lim_pct <= 5.0:
        st, msg = "OK", "W normie (<=5%)"
    elif lim_pct <= 15.0:
        st, msg = "WARNING", f"Podwyższony limit Er: {lim_pct:.1f}%"
    else:
        st, msg = "CRITICAL", f"CRITICAL DEADLOCK: {lim_pct:.1f}% gier kończy remis (limit >15%)"
    results.append(MetricCheckResult("eras_limit_pct", "Remisy na Limite Er (%)", lim_pct, st, msg))

    # 3. Autodafé na partię (autodafe_avg)
    auto = summary.autodafe_avg
    if 1.0 <= auto <= 2.5:
        st, msg = "OK", "W normie (1.0–2.5)"
    elif 0.5 <= auto <= 4.0:
        st, msg = "WARNING", f"Nietypowa aktywność Autodafé: {auto:.2f}"
    else:
        st, msg = "CRITICAL", f"CRITICAL AUTODAFE: {auto:.2f} na partię (Czerwona Linia: 0.5–4.0)"
    results.append(MetricCheckResult("autodafe_avg", "Średnia Autodafé / partię", auto, st, msg))

    # 4. Oskarżenia i Werdykty (accusations_avg)
    acc = summary.accusations_avg
    if 1.5 <= acc <= 4.0:
        st, msg = "OK", "W normie (1.5–4.0)"
    elif 0.8 <= acc <= 6.0:
        st, msg = "WARNING", f"Odbiegi aktywności Oskarżeń: {acc:.2f}"
    else:
        st, msg = "CRITICAL", f"CRITICAL ACCUSATIONS: {acc:.2f} na partię (Czerwona Linia: 0.8–6.0)"
    results.append(MetricCheckResult("accusations_avg", "Średnia Oskarżeń / partię", acc, st, msg))

    # --- KATEGORIA B: Mechaniki Pomocnicze (1 Poziom: Zakres Ostrzegawczy) ---

    # 5. Średni stan Złota (avg_gold_end)
    gold = summary.avg_gold_end
    if 0.20 <= gold <= 1.50:
        st, msg = "OK", "W normie (0.20–1.50 zł)"
    else:
        st, msg = "WARNING", f"Ostrzeżenie Skarbcowe: {gold:.2f} zł na koniec Ery"
    results.append(MetricCheckResult("avg_gold_end", "Średni Stan Złota End", gold, st, msg))

    # 6. Średnia Herezja końcowa (avg_heresy_end)
    her = summary.avg_heresy_end
    if 4.5 <= her <= 7.5:
        st, msg = "OK", "W normie (4.5–7.5)"
    else:
        st, msg = "WARNING", f"Ostrzeżenie Poziomu Herezji: {her:.2f}"
    results.append(MetricCheckResult("avg_heresy_end", "Średnia Herezja End", her, st, msg))

    # 7. Pas Przymusowy z Biedy (passes_forced_pct)
    fpass = summary.passes_forced_pct * 100.0
    if fpass <= 3.0:
        st, msg = "OK", "W normie (<=3%)"
    else:
        st, msg = "WARNING", f"Ostrzeżenie Ubóstwa: {fpass:.1f}% tur w pasie z braku złota"
    results.append(MetricCheckResult("passes_forced_pct", "Pas Przymusowy (%)", fpass, st, msg))

    # 8. Min Era (eras_min)
    min_e = summary.eras_min
    if min_e >= 3:
        st, msg = "OK", "W normie (>=3 Er)"
    else:
        st, msg = "WARNING", f"Ostrzeżenie Anomali Wygranej: partia wygrana w Erze {min_e}"
    results.append(MetricCheckResult("eras_min", "Min Liczba Er", float(min_e), st, msg))

    return results
