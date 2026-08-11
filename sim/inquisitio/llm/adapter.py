"""Optional LLM hook for intrigue forks. Off unless INQ_LLM=1."""

from __future__ import annotations

import json
import os
import urllib.request
from typing import TYPE_CHECKING

from inquisitio.model import FactionId, LocationId

if TYPE_CHECKING:
    from inquisitio.engine.state import GameState


class LLMAdapter:
    def enabled(self) -> bool:
        return False

    def maybe_choose_location(
        self,
        state: GameState,
        faction: FactionId,
        true_loc: LocationId,
        intent: str,
    ) -> LocationId | None:
        return None

    def maybe_accuse(
        self,
        state: GameState,
        faction: FactionId,
        target: FactionId,
        base_ev: float,
    ) -> bool | None:
        return None


class OpenAICompatibleAdapter(LLMAdapter):
    def enabled(self) -> bool:
        return os.environ.get("INQ_LLM", "").strip() in {"1", "true", "yes"}

    def _chat(self, prompt: str) -> str | None:
        if not self.enabled():
            return None
        api_key = os.environ.get("OPENAI_API_KEY") or os.environ.get("INQ_LLM_KEY")
        base = os.environ.get("INQ_LLM_BASE", "https://api.openai.com/v1")
        model = os.environ.get("INQ_LLM_MODEL", "gpt-4o-mini")
        if not api_key:
            return None
        body = json.dumps(
            {
                "model": model,
                "messages": [
                    {"role": "system", "content": "You are an intrigue player in INQUISITIO 1492. Reply with a single token only."},
                    {"role": "user", "content": prompt},
                ],
                "temperature": 0.4,
                "max_tokens": 20,
            }
        ).encode()
        req = urllib.request.Request(
            f"{base.rstrip('/')}/chat/completions",
            data=body,
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                data = json.loads(resp.read().decode())
            return data["choices"][0]["message"]["content"].strip()
        except Exception:
            return None

    def maybe_choose_location(self, state, faction, true_loc, intent):
        if not self.enabled():
            return None
        prompt = (
            f"Faction={faction.value} intent={intent} true_loc={true_loc.value}. "
            f"Reply with one of: trybunal,palac,lochy,rynek,gildia (feint allowed)."
        )
        text = self._chat(prompt)
        if not text:
            return None
        token = text.split()[0].strip().lower().strip("`.,")
        try:
            return LocationId(token)
        except ValueError:
            return None

    def maybe_accuse(self, state, faction, target, base_ev):
        if not self.enabled():
            return None
        prompt = (
            f"Faction={faction.value} may accuse {target.value} "
            f"(heresy={state.player(target).heresy}, threshold={state.threshold}, ev={base_ev:.2f}). "
            f"Reply YES or NO."
        )
        text = self._chat(prompt)
        if not text:
            return None
        return text.upper().startswith("Y")


def get_adapter() -> LLMAdapter:
    adapter = OpenAICompatibleAdapter()
    if adapter.enabled():
        return adapter
    return LLMAdapter()
