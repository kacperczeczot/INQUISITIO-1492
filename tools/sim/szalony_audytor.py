#!/usr/bin/env python3
"""Szalony Audytor — przyjazny alias dla auto_balancer.py."""
import sys
from pathlib import Path

# Fix path to include sim and tools/sim directories
TOOLS_SIM_DIR = Path(__file__).resolve().parent
SIM_DIR = TOOLS_SIM_DIR.parent.parent / "sim"

for p in (TOOLS_SIM_DIR, SIM_DIR):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

from auto_balancer import main

if __name__ == "__main__":
    main()
