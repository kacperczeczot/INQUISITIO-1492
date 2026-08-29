import re
from pathlib import Path

for filename in ['scripts/sim/audytor_3p.py', 'scripts/sim/audytor_5p.py']:
    text = Path(filename).read_text()
    
    # Remove mode="legacy" from rank_key
    text = re.sub(r'rank_key\((.*?), mode="legacy"\)', r'rank_key(\1)', text)
    
    # Remove mode="legacy" from accept_candidate
    text = re.sub(r'mode="legacy",\n\s*', '', text)
    
    Path(filename).write_text(text)

print("Fixed modes.")
