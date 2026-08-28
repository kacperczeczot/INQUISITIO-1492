"""Replay & Game Inspector Tool — Trace turn-by-turn logs for problematic games."""
from __future__ import annotations
import random
from pathlib import Path
from inquisitio.agents.politics import PoliticsAgent
from inquisitio.engine.setup import new_game
from inquisitio.engine.turn import play_game

def inspect_game(setup: str = "4p-core", seed: int = 42, layer: str = "C", threshold: int = 7) -> str:
    rng = random.Random(seed)
    state = new_game(setup=setup, seed=seed, threshold=threshold, layer=layer)
    agent = PoliticsAgent(rng)

    def choose(st, fid, legal):
        return agent.choose_card(st, fid, legal)

    winner = play_game(state, rng, choose)

    lines = [
        f"========================================================",
        f"INSPEKCJA GRY (REPLAY LOG): Setup `{setup}` | Seed: {seed}",
        f"Zwycięzca: {winner.value.upper()} | Przebieg: {state.metrics.eras} Er",
        f"========================================================\n",
        "## Przebieg Tura po Turze (Narracja Logów):",
        "",
    ]

    for entry in state.log:
        lines.append(f"- {entry}")

    lines.extend([
        "",
        "## Statystyki Końcowe Graczy:",
        "",
    ])

    for fid, pl in state.players.items():
        lines.append(
            f"- **{fid.value.upper()}**: Złoto={pl.gold}zł | Herezja={pl.heresy} | "
            f"Stosy={pl.stacks} | Relikwie={pl.relics_evacuated} | Dekrety={pl.decrees_played} | "
            f"Fragmenty={pl.fragments} | Upadki={pl.falls}"
        )

    return "\n".join(lines)

def save_replay_report(setup: str = "4p-core", seed: int = 42, out_dir: str = "data/playtesting/sim-reports/game_replays"):
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    content = inspect_game(setup=setup, seed=seed)
    file_path = out_path / f"replay_{setup}_seed_{seed}.md"
    file_path.write_text(content, encoding="utf-8")
    print(f"Replay saved to {file_path}")
    return file_path

if __name__ == "__main__":
    save_replay_report("4p-core", seed=42)
    save_replay_report("5p-full", seed=42)
