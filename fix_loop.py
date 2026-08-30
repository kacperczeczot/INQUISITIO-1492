import re

def fix_script(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    pattern = re.compile(
        r"racers\.sort\(key=lambda x: x\.score_4p, reverse=True\)\n"
        r"\s*best_rejection = None\n"
        r"\s*for cand_stat in ranked:\n.*?"
        r"if not best_rejection:\n\s*best_rejection = f\"Odpadł najlepszy kandydat: \{decision\.reason\}\"",
        re.DOTALL
    )
    
    # Wait, the code in audytor_3p.py actually uses 'ranked' which is NOT 'racers'!
    # Let me check the exact code first.
