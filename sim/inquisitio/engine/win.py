from __future__ import annotations

from inquisitio.engine.state import GameState
from inquisitio.model import FactionId


def _convert_oficjum_influence(state: GameState) -> None:
    """3 Wpływ w Trybunale → 1 Stos (ścieżka bez Autodafé)."""
    if FactionId.SWIETE_OFICJUM not in state.players:
        return
    ofi = state.player(FactionId.SWIETE_OFICJUM)
    while ofi.influence_tribunal >= 4:
        ofi.influence_tribunal -= 4
        ofi.stakes += 1
        state.metrics.stakes_total += 1
        state.metrics.log(event="influence_to_stake", stakes=ofi.stakes)


def check_winner(state: GameState) -> FactionId | None:
    _convert_oficjum_influence(state)
    for faction, p in state.players.items():
        # Kalibracja: 2 Stosy (było 3) — Oficjum musi być w meta
        if faction == FactionId.SWIETE_OFICJUM and p.stakes >= 2:
            state.winner = faction
            state.win_reason = "2 stosy"
            return faction
        if faction == FactionId.CIENIE_AL_ANDALUS and p.evacuated_relics >= 2:
            state.winner = faction
            state.win_reason = "2 relikwie ewakuowane"
            return faction
        if faction == FactionId.KORONA_BORGIOWIE and p.control_palace >= 2 and p.control_market >= 2:
            state.winner = faction
            state.win_reason = "kontrola Palac+Rynek (2+2)"
            return faction
        # Kalibracja: 4 Wskazówki + cap 1/era + sweet spot
        if faction == FactionId.KABALA_TOLEDO and p.clues >= 4:
            state.winner = faction
            state.win_reason = "4 wskazowki"
            return faction
        if faction == FactionId.GILDIA_CIENI and len(set(p.collapses)) >= 2:
            state.winner = faction
            state.win_reason = "upadek 2 frakcji"
            return faction
    return None


def end_game_by_eras(state: GameState) -> FactionId:
    """Highest intrigue progress; tie -> lowest heresy."""
    _convert_oficjum_influence(state)

    def score(f: FactionId) -> tuple[int, int]:
        p = state.player(f)
        # Równy postęp 0–4 względem celu frakcji (bez farmienia Wpływu)
        progress = {
            FactionId.SWIETE_OFICJUM: p.stakes * 2,  # cel 2 → max 4
            FactionId.CIENIE_AL_ANDALUS: p.evacuated_relics * 2 + min(1, p.relics),
            FactionId.KORONA_BORGIOWIE: 2 * min(p.control_palace, p.control_market)
            + (1 if p.control_palace != p.control_market else 0),
            FactionId.KABALA_TOLEDO: p.clues,
            FactionId.GILDIA_CIENI: len(set(p.collapses)) * 2,
        }.get(f, 0)
        return (progress, -p.heresy)

    winner = max(state.order, key=score)
    state.winner = winner
    state.win_reason = "limit er"
    return winner
