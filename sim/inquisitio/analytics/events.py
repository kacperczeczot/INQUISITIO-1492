"""Macro Tactical Event Dictionary for Simulation Analytics & Strategy Insight Mining."""
from __future__ import annotations
from enum import Enum

class TacticalEvent(str, Enum):
    TACTICAL_PASS_EARLY = "tactical_pass_early"  # Era 1-3 pass to save gold for signature/finisher
    TACTICAL_PASS_LATE = "tactical_pass_late"
    EARLY_INQUISITOR_MOVE = "early_inquisitor_move"  # Send Inquisitor in Era 1-2
    AUTODAFE_ON_RELIC_SITE = "autodafe_on_relic_site"  # Trigger/support Autodafe where Relic is located
    HOOK_FORCED_ON_LEADER = "hook_forced_on_leader"  # Force hook on current score leader
    EARLY_DECREE_PLAY = "early_decree_play"  # Play decree in Era 1-3
    FRAGMENT_HOLD_OBSERWOWANA = "fragment_hold_obserwowana"  # Kabala holding fragments while in 4-6 heresy
    SIGNATURE_FINISHER_PLAY = "signature_finisher_play"  # Playing faction signature card
