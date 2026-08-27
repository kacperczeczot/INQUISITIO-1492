#!/usr/bin/env python3
"""Verify PnP player-boards: nothing clipped inside 210×148 mm mats.

Usage (macOS, Chrome installed):
  python3 tools/pnp/verify_player_boards.py
  python3 tools/pnp/verify_player_boards.py assets/prototypes/player-boards.html
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
DEFAULT = REPO / "assets/prototypes/player-boards.html"

EXPR = r"""(() => {
  function contained(inner, outer, slack=1) {
    const a = inner.getBoundingClientRect();
    const b = outer.getBoundingClientRect();
    return a.left >= b.left - slack && a.top >= b.top - slack
      && a.right <= b.right + slack && a.bottom <= b.bottom + slack
      && a.width > 0 && a.height > 0;
  }
  const boards = [...document.querySelectorAll('.player-stack')];
  const problems = [];
  const mm = 96/25.4;
  for (const board of boards) {
    const faction = board.dataset.faction || '?';
    const br = board.getBoundingClientRect();
    if (Math.abs(br.width/mm-210)>4 || Math.abs(br.height/mm-148)>4)
      problems.push(`${faction}: size ${(br.width/mm).toFixed(1)}x${(br.height/mm).toFixed(1)}mm`);
    const limits = board.querySelector('.pb-box.limits');
    const wells = [...board.querySelectorAll('.pb-limit')];
    if (board.querySelector('.pb-body.layer-c') && wells.length !== 3)
      problems.push(`${faction}: wells=${wells.length}`);
    if (limits) {
      if (!contained(limits, board)) problems.push(`${faction}: limits outside board`);
      for (const w of wells) {
        const lbl = ((w.querySelector('.pb-limit-lbl')||{}).textContent||'').trim();
        if (!contained(w, limits)) problems.push(`${faction}: ${lbl} outside limits`);
        if (!contained(w, board)) problems.push(`${faction}: ${lbl} outside board`);
        const lab = w.querySelector('.pb-limit-lbl');
        if (lab && lab.scrollWidth > lab.clientWidth + 1)
          problems.push(`${faction}: truncated ${lbl}`);
      }
    }
    for (const el of board.querySelectorAll('.agent-slot,.pb-box.hooks .pb-token,.pb-box.progress .pb-token')) {
      if (!contained(el, board)) problems.push(`${faction}: clipped ${el.className}`);
    }
  }
  return {boards: boards.length, ok: problems.length===0, problems};
})()"""


def main() -> int:
    target = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else DEFAULT
    if not target.is_file():
        print(f"missing: {target}", file=sys.stderr)
        return 2
    if not Path(CHROME).exists():
        print(f"Chrome not found: {CHROME}", file=sys.stderr)
        return 2

    try:
        import websocket  # noqa: F401
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "websocket-client", "-q"])
        import websocket  # noqa: F401

    import websocket

    port = 9339
    profile = Path("/tmp/chrome-pb-verify-profile")
    profile.mkdir(exist_ok=True)
    proc = subprocess.Popen(
        [
            CHROME,
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            f"--remote-debugging-port={port}",
            "--remote-allow-origins=*",
            f"--user-data-dir={profile}",
            f"file://{target}",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
    )
    try:
        tabs = None
        for _ in range(100):
            try:
                with urllib.request.urlopen(f"http://127.0.0.1:{port}/json/list", timeout=0.2) as r:
                    tabs = json.load(r)
                if any(target.name in (t.get("url") or "") for t in tabs):
                    break
            except Exception:
                time.sleep(0.1)
        else:
            err = (proc.stderr.read() or b"").decode("utf-8", "replace")[-1500:]
            print("CDP not ready\n" + err, file=sys.stderr)
            return 2

        tab = next(t for t in tabs if target.name in (t.get("url") or ""))
        ws = websocket.create_connection(tab["webSocketDebuggerUrl"], timeout=8)
        msg_id = 0

        def cdp(method: str, params: dict | None = None) -> dict:
            nonlocal msg_id
            msg_id += 1
            i = msg_id
            ws.send(json.dumps({"id": i, "method": method, "params": params or {}}))
            while True:
                msg = json.loads(ws.recv())
                if msg.get("id") == i:
                    return msg

        cdp("Runtime.enable")
        time.sleep(0.6)
        res = cdp("Runtime.evaluate", {"expression": EXPR, "returnByValue": True})
        payload = res["result"]["result"]["value"]
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return 0 if payload.get("ok") and payload.get("boards", 0) > 0 else 1
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except Exception:
            proc.kill()


if __name__ == "__main__":
    raise SystemExit(main())
