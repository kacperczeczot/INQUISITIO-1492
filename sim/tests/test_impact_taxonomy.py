"""Ablation labels: Δ≈0 is dead, self-harm is not a pillar."""
from inquisitio.runner.impact_taxonomy import (
    classify_card_impact_4p,
    classify_mechanic_impact_4p,
)


def test_near_zero_mechanic_is_dead_not_optimal():
    sub, _role, group = classify_mechanic_impact_4p(0.0, 0.2)
    assert group == "DEAD"
    assert sub == "M_DEAD"


def test_hook_requirement_style_zero_delta_is_dead():
    _, _, group = classify_mechanic_impact_4p(0.0, 0.0)
    assert group == "DEAD"


def test_real_pillar_stays_stabilizer():
    _, _, group = classify_mechanic_impact_4p(-44.0, 16.0)
    assert group == "STABILIZER"


def test_share_nudge_without_table_crash_is_weak_not_optimal():
    _, role, group = classify_mechanic_impact_4p(-2.0, 5.0)
    assert group == "WEAK"
    assert "SŁABA" in role


def test_kb_hook_tax_card_is_self_harm_not_shield():
    # 24.8% → 40.9% when removed: d_share negative, d_4p catastrophic
    _, _, group = classify_card_impact_4p(24.8 - 40.9, 50.0 - 94.6)
    assert group == "SELF_HARM"


def test_true_dead_weight_card():
    _, _, group = classify_card_impact_4p(0.1, 0.0)
    assert group == "DEAD_WEIGHT"
