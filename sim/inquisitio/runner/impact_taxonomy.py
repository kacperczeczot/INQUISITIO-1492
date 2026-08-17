"""Ablation taxonomy for 4P cards and L1/L2/L4 mechanics.

Δ4P is 'what happens to the table when we remove or nudge this'.
A near-zero delta is a dead clause, not a 'balanced regulator'.
A card that raises its own faction's win share when removed is a self-harm tax,
even if removing it wrecks 4P equality (the table was balanced *by* the tax).
"""
from __future__ import annotations


def classify_card_impact_4p(d_share: float, d_4p: float) -> tuple[str, str, str]:
    """Classifies card impact into the 4P ablation matrix.

    d_share: base faction win% minus ablated win% (positive = card helps the faction).
    d_4p: ablated 4P score minus base (positive = removing the card improves 4P).
    """
    if d_share <= -2.0:
        return "SELF_HARM", "🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax)", "SELF_HARM"

    if d_4p >= 1.2:
        if d_share > 0.8:
            return "TOXIC_CARRIER", "⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver)", "DISRUPTOR"
        elif d_share < -0.8:
            return "TOXIC_BRAKE", "⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm)", "DISRUPTOR"
        else:
            return "TOXIC_NOISE", "⚠️ SZUM DESTABILIZUJĄCY (Meta Disruptor)", "DISRUPTOR"

    if d_4p <= -2.0 or d_share >= 2.5:
        if d_share >= 2.5:
            return "PILLAR", "👑 FILAR KANONU (Core Keystone)", "STABILIZER"
        elif d_share <= -2.5:
            return "SHIELD", "🛡️ TARCZA DEFENSYWNA (Faction Shield)", "STABILIZER"
        else:
            return "ANCHOR", "⚓ KOTWICA KANONU (Balance Anchor)", "STABILIZER"

    if abs(d_share) <= 0.4 and abs(d_4p) <= 0.4:
        return "DEAD_WEIGHT", "💤 KARTA NISKIEGO WPŁYWU (Dead / Passive)", "DEAD_WEIGHT"

    if d_share >= 1.0:
        return "ENGINE", "⚡ MOTOR FRAKCJI (Offensive Engine)", "BALANCED"
    elif d_share <= -1.0:
        return "BRAKE", "🛑 HAMULEC FRAKCJI (Control Tool)", "BALANCED"
    else:
        return "UTILITY", "⚖️ ZBALANSOWANE NARZĘDZIE (Utility)", "BALANCED"


def classify_mechanic_impact_4p(d_4p: float, max_d_share: float) -> tuple[str, str, str]:
    """Classifies system/victory mechanic impact.

    Key L1/L2/L4 knobs should land in STABILIZER. A mid Δ that only
    shuffles share is a weak lever (needs work), not a gold-star 'balanced' slot.
    Near-zero ablation is DEAD, not optimal.
    """
    if abs(d_4p) <= 0.8 and max_d_share <= 1.5:
        return "M_DEAD", "💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra)", "DEAD"

    if abs(d_4p) >= 15.0 or max_d_share >= 10.0:
        severity = "CRITICAL"
    elif abs(d_4p) >= 4.0 or max_d_share >= 4.0:
        severity = "MODERATE"
    else:
        severity = "LOW"

    if d_4p <= -4.0:
        direction = "STABILIZER"
    elif d_4p >= 1.5:
        direction = "DISRUPTOR"
    else:
        direction = "NEUTRAL"

    mapping = {
        ("CRITICAL", "STABILIZER"): ("M_CRIT_STAB", "👑 KRYTYCZNY FILAR (Core Engine Pillar)", "STABILIZER"),
        ("CRITICAL", "NEUTRAL"): ("M_CRIT_NEUT", "⚓ KLUCZOWY STABILIZATOR (Key Anchor)", "STABILIZER"),
        ("CRITICAL", "DISRUPTOR"): ("M_CRIT_DISR", "⚠️ KRYTYCZNA WADA (Critical Flaw)", "DISRUPTOR"),
        ("MODERATE", "STABILIZER"): ("M_MOD_STAB", "🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard)", "STABILIZER"),
        ("MODERATE", "NEUTRAL"): (
            "M_MOD_NEUT",
            "⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu)",
            "WEAK",
        ),
        ("MODERATE", "DISRUPTOR"): ("M_MOD_DISR", "⚠️ UMIARKOWANE OBCIĄŻENIE (Moderate Drag)", "DISRUPTOR"),
        ("LOW", "STABILIZER"): ("M_LOW_STAB", "🛡️ DROBNY BEZPIECZNIK (Minor Buffer)", "STABILIZER"),
        ("LOW", "NEUTRAL"): ("M_LOW_NEUT", "💤 MARTWA MECHANIKA (Low Impact)", "DEAD"),
        ("LOW", "DISRUPTOR"): ("M_LOW_DISR", "💡 KANDYDAT DO UPROSZCZENIA (Simplification)", "DISRUPTOR"),
    }
    return mapping.get((severity, direction), ("M_GENERIC", "⚠️ ZA SŁABA DŹWIGNIA", "WEAK"))
