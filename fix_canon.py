import re
from pathlib import Path

path = Path('src/inquisitio/runner/canon_accept.py')
text = path.read_text()

# Fix rank_key signature
text = re.sub(r'def rank_key\(res: dict, \*, mode: str = "band", base_in_band: bool = False\) -> tuple:', 'def rank_key(res: dict) -> tuple:', text)

# Fix canon_should_stop signature
text = re.sub(r'def canon_should_stop\(res: dict, \*, mode: str = "legacy"\) -> bool:', 'def canon_should_stop(res: dict) -> bool:', text)

# Fix accept_candidate signature
# def accept_candidate(\n    base: dict,\n    cand: dict,\n    *,\n    mode: str = "legacy",\n    min_delta: float = 0.05,\n) -> AcceptDecision:
sig = """def accept_candidate(
    base: dict,
    cand: dict,
    *,
    min_delta: float = 0.05,
) -> AcceptDecision:"""
text = re.sub(r'def accept_candidate\([\s\S]*?min_delta: float = 0.05,\n\) -> AcceptDecision:', sig, text)

# Remove `if mode == "legacy":` block and unindent
match = re.search(r'    if mode == "legacy":\n([\s\S]*?)    if mode != "band":', text)
if match:
    legacy_block = match.group(1)
    unindented_legacy_block = legacy_block.replace('        ', '    ')
    
    # Replace from `if mode == "legacy":` to end of file with unindented legacy block
    text = re.sub(r'    if mode == "legacy":\n[\s\S]*', unindented_legacy_block.rstrip() + '\n', text)

path.write_text(text)
