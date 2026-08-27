"""Strategy Insight Mining Engine — Synthesizes Polish Natural Language Strategy Insights from Simulation Events."""
from __future__ import annotations
from dataclasses import dataclass
from inquisitio.analytics.events import TacticalEvent

SIGNIFICANCE_THRESHOLD: float = 0.10  # Regulowany próg istotności (np. 10% różnicy win rate)

@dataclass
class StrategyInsight:
    faction: str
    event: str
    impact_pct: float
    description: str

TEMPLATES = {
    (TacticalEvent.TACTICAL_PASS_EARLY, "cienie-al-andalus"): (
        "Taktyczne spasowanie w Erze 1–3 w celu zaoszczędzenia 2zł na kartę Signature "
        "zwiększa szansę na wygraną Cieni o +{impact:.1f}%."
    ),
    (TacticalEvent.TACTICAL_PASS_EARLY, "kabala-toledo"): (
        "Oszczędzanie złota na Pieczęć Salomona we wczesnej fazie gry (Erze 2) "
        "podnosi skuteczność Kabały o +{impact:.1f}%."
    ),
    (TacticalEvent.EARLY_DECREE_PLAY, "korona-borgiowie"): (
        "Wczesne zagranie Dekretu Miejskiego (przed Erą 4) zwiększa tempo zwycięstwa Korony "
        "o +{impact:.1f}%."
    ),
    (TacticalEvent.SIGNATURE_FINISHER_PLAY, "swiete-oficjum"): (
        "Użycie karty Signature Oficjum przy progu 4 Stosów podnosi wygraną o +{impact:.1f}%."
    ),
}

def mine_strategy_insights(
    event_win_rates: dict[tuple[str, str], float],
    baseline_win_rates: dict[str, float],
    threshold: float = SIGNIFICANCE_THRESHOLD,
) -> list[StrategyInsight]:
    insights: list[StrategyInsight] = []

    for (evt_name, fid), win_rate in event_win_rates.items():
        base_rate = baseline_win_rates.get(fid, 0.25)
        diff = win_rate - base_rate

        if diff >= threshold:
            # Match template
            key = (evt_name, fid)
            if key in TEMPLATES:
                template = TEMPLATES[key]
                desc = template.format(impact=diff * 100.0)
            else:
                desc = f"Zdarzenie '{evt_name}' zwiększa skuteczność frakcji {fid} o +{diff*100.0:.1f}%."

            insights.append(
                StrategyInsight(
                    faction=fid,
                    event=evt_name,
                    impact_pct=round(diff * 100.0, 1),
                    description=desc,
                )
            )

    return insights
