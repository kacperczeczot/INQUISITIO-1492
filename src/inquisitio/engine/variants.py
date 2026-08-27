"""Read L4 variant knobs: sys_overrides first, then CONFIG.variants."""
from __future__ import annotations

from inquisitio.config import CONFIG
from inquisitio.engine.state import GameState


def variant_get(state: GameState, key: str, default=None):
    sys = state.sys_overrides or {}
    if key in sys:
        return sys[key]
    return CONFIG.variants.get(key, default)


def variant_int(state: GameState, key: str, default: int = 0) -> int:
    return int(variant_get(state, key, default))


def variant_bool(state: GameState, key: str, default: bool = False) -> bool:
    val = variant_get(state, key, default)
    return bool(val)
