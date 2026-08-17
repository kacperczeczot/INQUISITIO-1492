"""Hooks — single token type (Layer B)."""
from __future__ import annotations

from inquisitio.engine.heresy import add_heresy
from inquisitio.engine.state import FactionId, GameState


def grant_hook(state: GameState, holder: FactionId, target: FactionId) -> None:
    if holder == target:
        return
    pl = state.players[holder]
    if sum(pl.hooks_on.values()) >= 2:
        state.add_log(f"Hook {holder.value} discarded (max 2 active)")
        return
    pl.hooks_on[target] = pl.hooks_on.get(target, 0) + 1
    pl.hook_victims_ever.add(target)
    state.metrics.hooks_created += 1
    state.add_log(f"Hook {holder.value} on {target.value}")


def active_hook_targets(state: GameState, holder: FactionId) -> list[FactionId]:
    pl = state.players[holder]
    return [t for t, n in pl.hooks_on.items() if n > 0]


def force_hook(
    state: GameState,
    holder: FactionId,
    target: FactionId,
    comply: bool,
) -> bool:
    """1 force per player per era. comply=True: consume hook silently; False: burn +heresy."""
    holder_pl = state.players[holder]
    if holder_pl.used_hook:
        return False
    if holder_pl.hooks_on.get(target, 0) <= 0:
        return False
    holder_pl.used_hook = True
    holder_pl.hooks_on[target] -= 1
    if holder_pl.hooks_on[target] <= 0:
        del holder_pl.hooks_on[target]
    state.metrics.hooks_forced += 1
    if comply:
        victim_pl = state.players[target]
        if victim_pl.gold > 0:
            victim_pl.gold -= 1
            holder_pl.gold += 1
            state.add_log(
                f"Hook complied {target.value} under {holder.value} (1 gold)"
            )
        else:
            state.add_log(f"Hook complied {target.value} under {holder.value}")
        return True
    add_heresy(state, target, 2, reason="hook_reveal")
    # Gildia fall on refuse — A teach + C (B awards falls mainly via verdict)
    if holder == FactionId.GILDIA_CIENI and state.layer in ("A", "C"):
        holder_pl.falls += 1
        state.add_log(f"Gildia fall -> {holder_pl.falls}")
    state.add_log(f"Hook revealed on {target.value}")
    return True


def count_hooks_held(state: GameState, holder: FactionId) -> int:
    return sum(state.players[holder].hooks_on.values())


def distinct_hook_victims(state: GameState, holder: FactionId) -> int:
    """Active hooks (current)."""
    return len(active_hook_targets(state, holder))


def distinct_hook_victims_ever(state: GameState, holder: FactionId) -> int:
    """Lifetime distinct victims — used for Korona victory (force doesn't erase progress)."""
    return len(state.players[holder].hook_victims_ever)
