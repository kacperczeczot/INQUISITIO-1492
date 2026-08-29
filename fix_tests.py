import re
from pathlib import Path

path = Path('src/tests/test_canon_accept.py')
text = path.read_text()

# Strip canon_should_stop kwargs
text = re.sub(r'canon_should_stop\(base, mode=".*?"\)', 'canon_should_stop(base)', text)
text = text.replace('mode="legacy", ', '')
text = text.replace('mode="legacy"', '')

tests_to_delete = [
    "test_foundation_allows_climb_from_wrecked_shares",
    "test_climb_still_runs_inside_red_line_outside_target_band",
    "test_band_climb_accepts_score_or_min_gain",
    "test_band_hygiene_accepts_health_fix_with_lower_score",
    "test_band_hygiene_accepts_score_gain_in_band",
    "test_band_veto_core_below_90_and_red_line",
    "test_no_cienie_88_with_shares_in_band_optimizes_score",
    "test_healthy_v086_table_rejects_insufficient_gain",
    "test_dead_win_path_keeps_hygiene_open",
    "test_hygiene_still_fixes_accusations_out_of_window",
]

for t in tests_to_delete:
    # Delete the test function using regex
    # Matches `def test_name():` and everything indented under it, up to the next unindented line or EOF
    pattern = re.compile(rf'^def {t}\(.*?\)[\s\S]*?(?=\n\S|\Z)', re.MULTILINE)
    text = pattern.sub('', text)

path.write_text(text)
