from __future__ import annotations

from inquisitio.engine.state import GameState
from inquisitio.model import FactionId


def run_process(
    state: GameState,
    accused: FactionId,
    accuser: FactionId,
    *,
    strategic: bool = False,
) -> bool:
    """Run accusation process. Returns True if verdict (burn)."""
    state.metrics.accusations += 1
    if strategic:
        state.metrics.strategic_accusations += 1
    state.metrics.log(
        event="accusation",
        era=state.era,
        accuser=accuser.value,
        accused=accused.value,
        strategic=strategic,
    )

    accused_p = state.player(accused)
    accused_p.accused_this_era = True

    # Oficjum zyskuje Wpływ gdy oskarża LUB ma Agenta w Trybunale/Lochach
    if FactionId.SWIETE_OFICJUM in state.players:
        from inquisitio.model import LocationId

        ofi = state.player(FactionId.SWIETE_OFICJUM)
        present = bool(ofi.agents_in(LocationId.TRYBUNAL) or ofi.agents_in(LocationId.LOCHY))
        if accuser == FactionId.SWIETE_OFICJUM or present:
            ofi.influence_tribunal += 1

    # Arrest
    board = accused_p.agents_on_board()
    if board:
        agent = board[0]
        agent.in_dungeon = True
        agent.location = None
    else:
        accused_p.add_heresy(1)

    # Defense cost: 5 złota lub 3 karty
    cleansed = False
    if accused_p.gold >= 5:
        accused_p.gold -= 5
        if FactionId.SWIETE_OFICJUM in state.players:
            state.player(FactionId.SWIETE_OFICJUM).gold += 5
        accused_p.add_heresy(-2)
        cleansed = True
    elif len(accused_p.hand) >= 3:
        for _ in range(3):
            if accused_p.hand:
                accused_p.discard.append(accused_p.hand.pop())
        accused_p.add_heresy(-2)
        cleansed = True

    # Konfiskata przy oczyszczeniu: złoto / kontrola — NIE clues/relikwie zwycięstwa
    if cleansed:
        if accused_p.gold > 0:
            take = min(2, accused_p.gold)
            accused_p.gold -= take
            if FactionId.SWIETE_OFICJUM in state.players:
                state.player(FactionId.SWIETE_OFICJUM).gold += take
        elif accused_p.control_palace > 0:
            accused_p.control_palace -= 1
        elif accused_p.control_market > 0:
            accused_p.control_market -= 1

    # Korona may force verdict by paying +1 over defense
    force = False
    if FactionId.KORONA_BORGIOWIE in state.players and FactionId.KORONA_BORGIOWIE != accused:
        korona = state.player(FactionId.KORONA_BORGIOWIE)
        # Prefer force if Oficjum ally or accused threatens control
        if korona.gold >= 1 and (
            accused_p.control_palace + accused_p.control_market >= 1 or accused_p.heresy >= state.threshold
        ):
            if cleansed and korona.gold >= 4:
                korona.gold -= 4
                force = True
                cleansed = False
            elif not cleansed and korona.gold >= 1:
                korona.gold -= 1
                force = True

    if cleansed and not force:
        state.metrics.log(event="process_cleansed", accused=accused.value)
        return False

    # Verdict / Autodafé
    state.metrics.verdicts += 1
    dungeon = accused_p.dungeon_agents()
    if dungeon:
        dungeon[0].burned = True
        dungeon[0].in_dungeon = False
    if FactionId.SWIETE_OFICJUM in state.players:
        oficjum = state.player(FactionId.SWIETE_OFICJUM)
        oficjum.stakes += 1
        state.metrics.stakes_total += 1
    # Lose intrigue token
    if accused_p.clues > 0:
        accused_p.clues -= 1
        state.clue_pool += 1
    elif accused_p.relics > 0:
        accused_p.relics -= 1
        state.relic_pool += 1
    elif accused_p.control_palace > 0:
        accused_p.control_palace -= 1
    elif accused_p.control_market > 0:
        accused_p.control_market -= 1
    accused_p.influence_tribunal = max(0, accused_p.influence_tribunal - 1)

    # Gildia: Upadek tylko przy stosie / gc-10 — nie auto z procesu
    # (usunięto auto-collapse przy heresy >= 8)

    state.metrics.log(event="verdict", accused=accused.value, forced=force)
    return True
