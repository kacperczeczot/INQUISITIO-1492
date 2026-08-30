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
_CONFIG_PATH = _PROJECT_ROOT / "data/game_config.yaml"


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


class ConfigValidationError(ValueError):
    """Raised when game configuration violates physical or mathematical invariants."""
    pass


class GameConfig:
    """Typed accessor for game_config.yaml."""

    def __init__(self, path: Path | None = None) -> None:
        p = path or _CONFIG_PATH
        with open(p, encoding="utf-8") as f:
            self._raw: dict[str, Any] = yaml.safe_load(f)
        self.validate_invariants(self._raw)
        self.version = str(self._raw.get("version", "v1.12"))
        self.system = _Section(self._raw["system"])
        self.victory = _Section(self._raw["victory"])
        self.economy = _Section(self._raw["economy"])
        self.cards = _Section(self._raw.get("cards", {}))
        self.variants = _Section(self._raw["variants"])
        self.telemetry_norms = _Section(self._raw["telemetry_norms"])

    @staticmethod
    def validate_invariants(raw: dict[str, Any]) -> None:
        """Validate generic mathematical and physical invariants of the configuration."""
        vic = raw.get("victory", {})
        sys = raw.get("system", {})

        def _get_p_val(val: Any, p_key: str, default: int = 0) -> int:
            if isinstance(val, dict):
                return int(val.get(p_key, val.get("4p", default)))
            if val is None:
                return default
            return int(val)

        # 1. Check unique rival interaction limits (e.g. condemns)
        so = vic.get("swiete_oficjum", {})
        condemns = so.get("condemns")
        if condemns is not None:
            for p_count, p_key in [(3, "3p"), (4, "4p"), (5, "5p")]:
                c_val = _get_p_val(condemns, p_key, 3)
                max_rivals = p_count - 1
                if c_val > max_rivals:
                    raise ConfigValidationError(
                        f"Fizyczna niemożliwość: 'condemns' ({c_val}) dla formatu {p_key} "
                        f"przekracza maksymalną liczbę rywali przy stole ({max_rivals})!"
                    )

        # 2. Check victory requirements positivity
        for faction, reqs in vic.items():
            if not isinstance(reqs, dict):
                continue
            for req_name, req_val in reqs.items():
                for p_key in ["3p", "4p", "5p"]:
                    v = _get_p_val(req_val, p_key, 1)
                    if v <= 0:
                        raise ConfigValidationError(
                            f"Nieprawidłowy warunek zwycięstwa: {faction}.{req_name} w {p_key} wynosi {v} <= 0."
                        )

        # 3. Check system positivity
        start_gold = sys.get("start_gold", 4)
        for p_key in ["3p", "4p", "5p"]:
            sg = _get_p_val(start_gold, p_key, 4)
            if sg < 0:
                raise ConfigValidationError(f"Złoto startowe w {p_key} nie może być ujemne: {sg}")

    # ── Convenience helpers ──────────────────────────────────────

    def threshold_for(self, n_players: int) -> int:
        """Accusation threshold for a given player count."""
        t = self.system.accusation_threshold
        if hasattr(t, "raw"):
            t = t.raw()
        elif type(t).__name__ == "_Section":
            t = t._data
        if isinstance(t, (int, float)):
            return int(t)
        if isinstance(t, dict):
            key = f"{n_players}p"
            return int(t.get(key, t.get("4p", 7)))
        return int(t)

    def observed_threshold(self) -> int:
        """Start of Observed (Autodafé burn). One number for the table."""
        return int(self.system.observed_threshold)

    def era_income(self) -> int:
        return int(getattr(self.system, "era_income", 1))

    def intrigue_gold(self) -> int:
        """Faza I Akcja Gospodarcza (one table number)."""
        return int(getattr(self.system, "intrigue_gold", 1))

    def start_gold_for(self, n_players: int) -> int:
        """Starting gold for a given player count."""
        sg = self.system.start_gold
        if isinstance(sg, (_Section, dict)):
            key = f"{n_players}p"
            return sg[key]
        return int(sg)

    def hand_limit_for(self, n_players: int) -> int:
        """Hand limit for a given player count."""
        hl = self.system.hand_limit
        if isinstance(hl, (_Section, dict)):
            key = f"{n_players}p"
            return hl[key]
        return int(hl)

    def victory_raw(self) -> dict[str, Any]:
        """Raw victory dict for sync_config templating."""
        return self._raw["victory"]

    def raw(self) -> dict[str, Any]:
        """Full raw dict."""
        return self._raw

    def get_active_overrides(self, setup_type: str = "4p") -> dict:
        """Returns overrides relative to the C++ hardcoded baseline snapshot."""
        ov = {}
        cards = self._raw.get("cards", {})
        card_ov = {}
        for cid, cdata in cards.items():
            if not isinstance(cdata, dict):
                continue
            diff = {}
            for k in ["cost", "heresy", "target_heresy", "gold"]:
                if k in cdata:
                    diff[k] = cdata[k]
            if diff:
                card_ov[cid] = diff
        if card_ov:
            ov["card_overrides"] = card_ov

        def _get_val(val, stype):
            if isinstance(val, dict):
                return val.get(stype, val.get("4p", 0))
            return val

        vic = self._raw.get("victory", {})
        if "swiete_oficjum" in vic and "stacks" in vic["swiete_oficjum"]:
            ov["so_stacks_offset"] = _get_val(vic["swiete_oficjum"]["stacks"], setup_type) - 7
        if "korona_borgiowie" in vic and "decrees" in vic["korona_borgiowie"]:
            ov["kb_decrees_offset"] = _get_val(vic["korona_borgiowie"]["decrees"], setup_type) - 2
        if "cienie_al_andalus" in vic and "relics" in vic["cienie_al_andalus"]:
            ov["caa_relics_offset"] = _get_val(vic["cienie_al_andalus"]["relics"], setup_type) - 2
        if "kabala_toledo" in vic and "fragments" in vic["kabala_toledo"]:
            ov["kt_frags_offset"] = _get_val(vic["kabala_toledo"]["fragments"], setup_type) - 3
        if "gildia_cieni" in vic and "falls" in vic["gildia_cieni"]:
            ov["gc_falls_offset"] = _get_val(vic["gildia_cieni"]["falls"], setup_type) - 9
        return ov

    def reload(self, path: Path | None = None) -> None:
        """Re-read the YAML file (useful after editing)."""
        self.__init__(path)  # type: ignore[misc]
        try:
            from inquisitio.cards.loader import load_all_cards
            load_all_cards(force=True)
        except Exception:
            pass


# ── Module-level singleton ──────────────────────────────────────────
CONFIG = GameConfig()
