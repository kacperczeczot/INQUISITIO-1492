"""Solo Dev-Play — narracyjny log jednej partii."""
from __future__ import annotations

import random
import re
from dataclasses import dataclass

from inquisitio.agents.politics import PoliticsAgent
from inquisitio.engine.setup import SETUP_PRESETS, new_game
from inquisitio.engine.state import FactionId, GameState, heresy_zone
from inquisitio.engine.turn import play_game

_ERA_RE = re.compile(r"^E(\d+):\s*(.*)$")


@dataclass
class FeelResult:
    state: GameState
    narrative: str
    summary: str


def _progress_line(state: GameState, fid: FactionId) -> str:
    pl = state.players[fid]
    parts = [
        f"heresy={pl.heresy}({heresy_zone(pl.heresy)})",
        f"gold={pl.gold}",
    ]
    if fid == FactionId.SWIETE_OFICJUM:
        parts.append(f"stacks={pl.stacks}")
        if pl.condemned_rivals:
            parts.append(f"condemned={len(pl.condemned_rivals)}")
    elif fid == FactionId.CIENIE_AL_ANDALUS:
        parts.append(f"relics={pl.relics_evacuated}")
    elif fid == FactionId.KORONA_BORGIOWIE:
        hooks = sum(1 for n in pl.hooks_on.values() if n > 0)
        parts.append(f"decrees={pl.decrees_played} hooks_on={hooks}")
    elif fid == FactionId.KABALA_TOLEDO:
        parts.append(f"fragments={pl.fragments}")
    elif fid == FactionId.GILDIA_CIENI:
        parts.append(f"falls={pl.falls}")
    return f"  {fid.value}: " + ", ".join(parts)


def format_narrative(state: GameState) -> str:
    eras: dict[int, list[str]] = {}
    for line in state.log:
        m = _ERA_RE.match(line)
        if not m:
            eras.setdefault(0, []).append(line)
            continue
        era_n = int(m.group(1))
        eras.setdefault(era_n, []).append(m.group(2))

    blocks: list[str] = []
    for era_n in sorted(k for k in eras if k > 0):
        blocks.append(f"=== Era {era_n} ===")
        for msg in eras[era_n]:
            blocks.append(f"  {msg}")
        blocks.append("")
    if 0 in eras:
        blocks.append("=== Other ===")
        for msg in eras[0]:
            blocks.append(f"  {msg}")
        blocks.append("")
    return "\n".join(blocks).rstrip() + "\n"


def format_summary(state: GameState) -> str:
    m = state.metrics
    winner = state.winner.value if state.winner else "?"
    lines = [
        "=== Metryki ===",
        f"Winner: {winner}",
        f"Layer: {state.layer}  threshold: {state.accusation_threshold}  seed: {state.rng_seed}",
        f"Eras: {m.eras}  cards_played: {m.cards_played}",
        f"Autodafé: {m.autodafe_count}  accusations: {m.accusations}  convictions: {m.convictions}",
        f"Hooks created: {m.hooks_created}  forced: {m.hooks_forced}  doubles: {m.doubles_created}",
        f"Deadlocks: {m.deadlocks}  legal_moves_sampled: {m.legal_moves_sampled}",
        "Progress:",
    ]
    for fid in state.turn_order:
        lines.append(_progress_line(state, fid))
    return "\n".join(lines) + "\n"


def run_feel(
    *,
    setup: str = "3p-oficjum-alandalus-korona",
    seed: int = 42,
    layer: str = "A",
    threshold: int = 7,
    max_eras: int | None = None,
) -> FeelResult:
    if setup not in SETUP_PRESETS:
        raise ValueError(f"Unknown setup {setup!r}; known: {sorted(SETUP_PRESETS)}")
    rng = random.Random(seed)
    state = new_game(setup=setup, seed=seed, threshold=threshold, layer=layer)
    if max_eras is not None:
        state.max_eras = max_eras
    agent = PoliticsAgent(rng)

    def choose(st: GameState, fid: FactionId, legal: list[str]):
        return agent.choose_card(st, fid, legal)

    play_game(state, rng, choose)
    return FeelResult(
        state=state,
        narrative=format_narrative(state),
        summary=format_summary(state),
    )


def render_feel(result: FeelResult) -> str:
    st = result.state
    header = (
        f"INQUISITIO 1492 — Solo Dev-Play\n"
        f"setup={'+'.join(f.value for f in st.turn_order)}  "
        f"layer={st.layer}  seed={st.rng_seed}  threshold={st.accusation_threshold}\n"
        f"Inquisitor start: {st.inquisitor_location}\n\n"
    )
    return header + result.narrative + "\n" + result.summary
