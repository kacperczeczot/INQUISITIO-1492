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

    def keys(self):
        return self._data.keys()

    def values(self):
        return self._data.values()

    def items(self):
        return self._data.items()

    def __iter__(self):
        return iter(self._data)

    def __len__(self) -> int:
        return len(self._data)

    def __contains__(self, key: str) -> bool:
        return key in self._data

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
                v_format = val.get(p_key, val.get("4p", default))
                if isinstance(v_format, dict):
                    return int(v_format.get("default", list(v_format.values())[0] if v_format else default))
                return int(v_format)
            if val is None:
                return default
            return int(val)

        # 1. Check unique rival interaction limits (e.g. condemns)
        so = vic.get("swiete_oficjum", {})
        condemns = so.get("condemns")
        if condemns is not None:
            for p_count, p_key in [(3, "3p"), (4, "4p"), (5, "5p")]:
                max_rivals = p_count - 1
                if isinstance(condemns, dict):
                    v_p = condemns.get(p_key, condemns.get("4p", 3))
                    if isinstance(v_p, dict):
                        for sub_k, sub_v in v_p.items():
                            if int(sub_v) > max_rivals:
                                raise ConfigValidationError(
                                    f"Fizyczna niemożliwość: 'condemns.{p_key}.{sub_k}' ({sub_v}) "
                                    f"przekracza maksymalną liczbę rywali przy stole ({max_rivals})!"
                                )
                    elif int(v_p) > max_rivals:
                        raise ConfigValidationError(
                            f"Fizyczna niemożliwość: 'condemns' ({v_p}) dla formatu {p_key} "
                            f"przekracza maksymalną liczbę rywali przy stole ({max_rivals})!"
                        )
                elif int(condemns) > max_rivals:
                    raise ConfigValidationError(
                        f"Fizyczna niemożliwość: 'condemns' ({condemns}) dla formatu {p_key} "
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

        # 4. Check card property bounds (Hard bounds for economic sanity & game balance)
        cards = raw.get("cards", {})
        for cid, c in cards.items():
            if not isinstance(c, dict):
                continue
            cost = int(c.get("cost", 0))
            if cost < 0 or cost > 5:
                raise ConfigValidationError(f"Karta '{cid}' ma koszt {cost} poza dozwolonym zakresem [0, 5]!")
            gold = int(c.get("gold", 0))
            if gold < 0 or gold > 3:
                raise ConfigValidationError(f"Karta '{cid}' daje złoto {gold} poza dozwolonym zakresem [0, 3]!")
            heresy = int(c.get("heresy", 0))
            if heresy < 0 or heresy > 3:
                raise ConfigValidationError(f"Karta '{cid}' ma herezję {heresy} poza dozwolonym zakresem [0, 3]!")
            th = int(c.get("target_heresy", 0))
            if th < 0 or th > 2:
                raise ConfigValidationError(f"Karta '{cid}' ma target_heresy {th} poza dozwolonym zakresem [0, 2]!")
            agents = int(c.get("agents", 0))
            if agents < 0 or agents > 2:
                raise ConfigValidationError(f"Karta '{cid}' ma agents {agents} poza dozwolonym zakresem [0, 2]!")

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
            v = t.get(key, t.get("4p", 7))
            if isinstance(v, dict):
                return int(v.get("default", list(v.values())[0] if v else 7))
            return int(v)
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
            v = sg.get(key, sg.get("4p", 4)) if isinstance(sg, dict) else sg[key]
            if isinstance(v, dict):
                return int(v.get("default", list(v.values())[0] if v else 4))
            return int(v)
        return int(sg)

    def hand_limit_for(self, n_players: int) -> int:
        """Hand limit for a given player count."""
        hl = self.system.hand_limit
        if isinstance(hl, (_Section, dict)):
            key = f"{n_players}p"
            v = hl.get(key, hl.get("4p", 5)) if isinstance(hl, dict) else hl[key]
            if isinstance(v, dict):
                return int(v.get("default", list(v.values())[0] if v else 5))
            return int(v)
        return int(hl)

    def victory_raw(self) -> dict[str, Any]:
        """Raw victory dict for sync_config templating."""
        return self._raw["victory"]

    def raw(self) -> dict[str, Any]:
        """Full raw dict."""
        return self._raw

    def get_active_overrides(self, setup_type: str = "4p", setup_name: str | None = None) -> dict:
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

        from inquisitio.engine.setup import SETUP_PRESETS
        present_factions = set(SETUP_PRESETS.get(setup_name, [])) if setup_name else set()

        def _get_val(val, stype):
            if isinstance(val, dict):
                v_format = val.get(stype, val.get("4p", 0))
                if isinstance(v_format, dict):
                    MISSING_TAGS = {
                        "no_so": "swiete-oficjum", "no_oficjum": "swiete-oficjum",
                        "no_caa": "cienie-al-andalus", "no_cienie": "cienie-al-andalus",
                        "no_kb": "korona-borgiowie", "no_korona": "korona-borgiowie",
                        "no_kt": "kabala-toledo", "no_kabala": "kabala-toledo",
                        "no_gc": "gildia-cieni", "no_gildia": "gildia-cieni",
                    }
                    WITH_TAGS = {
                        "with_so": "swiete-oficjum", "has_so": "swiete-oficjum",
                        "with_caa": "cienie-al-andalus", "has_caa": "cienie-al-andalus",
                        "with_kb": "korona-borgiowie", "has_kb": "korona-borgiowie",
                        "with_kt": "kabala-toledo", "has_kt": "kabala-toledo",
                        "with_gc": "gildia-cieni", "has_gc": "gildia-cieni",
                    }
                    for tag, fid in MISSING_TAGS.items():
                        if tag in v_format and fid not in present_factions:
                            return v_format[tag]
                    for tag, fid in WITH_TAGS.items():
                        if tag in v_format and fid in present_factions:
                            return v_format[tag]
                    return v_format.get("default", list(v_format.values())[0] if v_format else 0)
                return v_format
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
