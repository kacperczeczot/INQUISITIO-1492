import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
SRC = ROOT / "src"
SCRIPTS_SIM = ROOT / "scripts" / "sim"

for p in (ROOT, SRC, SCRIPTS_SIM):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))
