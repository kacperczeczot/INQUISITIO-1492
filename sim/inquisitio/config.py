"""Central game configuration loader — Single Source of Truth.

Usage:
    from inquisitio.config import CONFIG

CONFIG is a module-level singleton that loads game_config.yaml once.
All engine modules read defaults from CONFIG; audit scripts override
via sys_overrides / win_overrides dicts.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

# ── locate game_config.yaml ────────────────────────────────────────
_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent  # sim/ → project root
_CONFIG_PATH = _PROJECT_ROOT / "game_config.yaml"


class _Section:
    """Dot-access wrapper over a nested dict."""

    def __init__(self, data: dict[str, Any]) -> None:
        self._data = data

    def __getattr__(self, key: str) -> Any:
        try:
            val = self._data[key]
        except KeyError:
            raise AttributeError(f"Config has no key '{key}'") from None
        if isinstance(val, dict):
            return _Section(val)
        return val

    def __getitem__(self, key: str) -> Any:
        if key not in self._data:
            # Fallback for 5p -> 4p if 5p not explicitly specified
            if key == "5p" and "4p" in self._data:
                return self.__getitem__("4p")
            raise KeyError(f"Config has no key '{key}'")
        val = self._data[key]
        if isinstance(val, dict):
            return _Section(val)
        return val

    def get(self, key: str, default: Any = None) -> Any:
        if key not in self._data:
            if key == "5p" and "4p" in self._data:
                return self.get("4p", default)
            return default
        val = self._data[key]
        if isinstance(val, dict):
            return _Section(val)
        return val

    def raw(self) -> dict[str, Any]:
        """Return the underlying raw dict."""
        return self._data

    def __repr__(self) -> str:
        return f"_Section({self._data!r})"


class GameConfig:
    """Typed accessor for game_config.yaml."""

    def __init__(self, path: Path | None = None) -> None:
        p = path or _CONFIG_PATH
        with open(p, encoding="utf-8") as f:
            self._raw: dict[str, Any] = yaml.safe_load(f)
        self.system = _Section(self._raw["system"])
        self.victory = _Section(self._raw["victory"])
        self.economy = _Section(self._raw["economy"])
        self.cards = _Section(self._raw.get("cards", {}))
        self.variants = _Section(self._raw["variants"])
        self.heresy_zones = _Section(self._raw["heresy_zones"])
        self.telemetry_norms = _Section(self._raw["telemetry_norms"])

    # ── Convenience helpers ──────────────────────────────────────

    def threshold_for(self, n_players: int) -> int:
        """Accusation threshold for a given player count."""
        key = f"{n_players}p"
        return self.system.accusation_threshold[key]

    def victory_raw(self) -> dict[str, Any]:
        """Raw victory dict for sync_config templating."""
        return self._raw["victory"]

    def raw(self) -> dict[str, Any]:
        """Full raw dict."""
        return self._raw

    def reload(self, path: Path | None = None) -> None:
        """Re-read the YAML file (useful after editing)."""
        self.__init__(path)  # type: ignore[misc]


# ── Module-level singleton ──────────────────────────────────────────
CONFIG = GameConfig()
