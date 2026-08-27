"""Audytor 4P: same funnel as kanon, no L3 cards, vitality veto on dead dual-path crutches."""
from __future__ import annotations

import sys
from pathlib import Path

TOOLS_SIM = Path(__file__).resolve().parents[2] / "tools" / "sim"
if str(TOOLS_SIM) not in sys.path:
    sys.path.insert(0, str(TOOLS_SIM))

from inquisitio.config_updater import apply_mutation_to_config  # noqa: E402
from audytor_4p import (  # noqa: E402
    accept_macro_candidate,
    cheap_funnel_flags,
    drop_dead_path_crutches,
    generate_all_atomic_candidates_macro,
    is_ablation_off,
    is_dead_path_crutch,
    is_frozen_identity_knob,
    lookahead_next_action,
    macro_vector_beats,
    merge_mutations,
)


def _dead_skazania_base() -> dict:
    return {
        "score_4p": 35.0,
        "score_4p_balance": 86.6,
        "min_balance": 83.0,
        "setup_scores_balance": {
            "4p-core": 90.0,
            "4p-no-cienie": 85.0,
            "4p-no-kabala": 86.0,
            "4p-no-korona": 87.0,
            "4p-no-oficjum": 85.0,
        },
        "setup_shares": {
            "4p-core": {"SO": 25.0, "CAA": 25.0, "KB": 25.0, "KT": 25.0},
            "4p-no-cienie": {"SO": 25.0, "KB": 25.0, "KT": 25.0, "GC": 25.0},
            "4p-no-kabala": {"SO": 25.0, "CAA": 25.0, "KB": 25.0, "GC": 25.0},
            "4p-no-korona": {"SO": 25.0, "CAA": 25.0, "KT": 25.0, "GC": 25.0},
            "4p-no-oficjum": {"CAA": 25.0, "KB": 25.0, "KT": 25.0, "GC": 25.0},
        },
        "vitality_penalty": 1.2,
        "vitality_warnings": [
            "4p-core: Martwa ścieżka skazania (swiete-oficjum): 19/1264 wygranych (<8%) — gra tylko stosy",
        ],
        "deadlock_pct": 1.1,
        "poverty_pct": 5.5,
        "eras_avg": 5.96,
        "acc_avg": 3.0,
    }


def test_cheap_funnel_skips_when_pool_fits_top():
    assert cheap_funnel_flags(20, 48, 24) == (False, False)
    assert cheap_funnel_flags(24, 48, 24) == (False, False)
    assert cheap_funnel_flags(30, 48, 24) == (False, True)
    assert cheap_funnel_flags(48, 48, 24) == (False, True)
    assert cheap_funnel_flags(60, 48, 24) == (True, True)


def test_macro_pool_has_no_cards_or_l3():
    pool = generate_all_atomic_candidates_macro()
    ids = [c[0] for c in pool]
    assert ids
    assert all(not tid.startswith("L3_") for tid in ids)
    for _tid, _name, params in pool:
        assert "card_overrides" not in params
        assert "disabled_cards" not in params
    assert all("AGENTS" not in tid for tid in ids)
    assert all("VERDICT_SECRET" not in tid for tid in ids)
    assert all("KB_HOOKS" not in tid for tid in ids)
    assert all("KB_ERA" not in tid for tid in ids)
    assert all("KT_HERESY" not in tid for tid in ids)
    assert all("NO_TIME_DECK" not in tid for tid in ids)
    assert all("SEA_ROUTE_OFF" not in tid for tid in ids)
    assert all("INQUISITOR_SPEED0" not in tid for tid in ids)
    for _tid, _name, params in pool:
        assert "agents_offset" not in params
        assert "verdict_secret" not in params
        assert "kb_hooks_offset" not in params
        assert "kb_era_offset" not in params
        assert "kt_heresy_band" not in params
        assert "no_time_deck" not in params
        assert "time_deck_freq" not in params
        assert int(params.get("sea_route_era") or 0) < 90
        assert params.get("inquisitor_speed") != 0
        cd = params.get("autodafe_cooldown")
        if cd is not None:
            assert int(cd) not in (0, 99)
    assert all("TIME_DECK" not in tid for tid in ids)
    assert "L1_HAND_LIMIT_PLUS1" in ids
    assert "L1_MAX_ERAS_PLUS1" not in ids
    assert "L1_AUTODAFE_COOLDOWN_PLUS1" in ids


def test_macro_pool_is_pm1_only():
    ids = {c[0] for c in generate_all_atomic_candidates_macro()}
    assert "L2_SO_CONDEMNS_MINUS1" in ids
    assert "L2_SO_CONDEMNS_LO" not in ids
    assert "L2_SO_CONDEMNS_HI" not in ids
    assert "L1_START_GOLD_0" not in ids
    assert "L1_START_GOLD_DOUBLE" not in ids
    assert "L1_MAX_ERAS_HALF" not in ids
    assert "L1_MAX_ERAS_PLUS1" not in ids
    assert "L1_MAX_ERAS_MINUS1" not in ids
    assert "L1_OBSERVED_PLUS1" in ids
    assert "L1_OBSERVED_MINUS1" in ids
    assert "L1_CARDS_PER_ERA_PLUS1" in ids
    assert "L2_CAA_ERA_PLUS1" not in ids
    assert "L2_CAA_RELICS_PLUS1" in ids
    assert "L2_SO_CONDEMNS_PLUS1" in ids
    assert "L4_SEA_ROUTE_ERA_PLUS1" in ids
    assert "L4_SEA_ROUTE_ERA_MINUS1" in ids
    assert "L1_AUTODAFE_DISABLED" not in ids
    assert "L1_AUTODAFE_COOLDOWN_PLUS1" in ids
    assert "L4_TIME_DECK_EVERY_2ERAS" not in ids
    assert "L2_GC_FALLS_PLUS1" in ids
    assert "L2_GC_FALLS_DEFAULT_PLUS1" not in ids
    assert "L2_GC_FALLS_NO_SO_MINUS1" not in ids
    for _tid, _name, params in generate_all_atomic_candidates_macro():
        assert "gc_falls_default_offset" not in params
        assert "gc_falls_no_oficjum_offset" not in params


def test_identity_knobs_rejected_at_accept():
    base = _dead_skazania_base()
    base["vitality_penalty"] = 0.0
    base["vitality_warnings"] = []
    cand = {
        **base,
        "id": "L1_AGENTS_MINUS1",
        "params": {"agents_offset": -1},
        "score_4p": 90.0,
        "min_balance": 90.0,
    }
    d = accept_macro_candidate(base, cand, mode="band", min_delta=0.05)
    assert not d.accepted
    assert "tożsamość" in d.reason


def test_ablation_off_rejected_at_accept():
    base = _dead_skazania_base()
    base["vitality_penalty"] = 0.0
    base["vitality_warnings"] = []
    cand = {
        **base,
        "id": "L4_SEA_ROUTE_OFF",
        "params": {"sea_route_era": 99},
        "score_4p": 90.0,
        "min_balance": 90.0,
    }
    d = accept_macro_candidate(base, cand, mode="band", min_delta=0.05)
    assert not d.accepted
    assert "ablacja" in d.reason


def test_max_eras_pm1_is_frozen_identity():
    assert is_frozen_identity_knob("L1_MAX_ERAS_PLUS1", {"max_eras_offset": 1})
    assert is_frozen_identity_knob("L1_MAX_ERAS_MINUS1", {"max_eras_offset": -1})
    assert not is_frozen_identity_knob("L1_HAND_LIMIT_PLUS1", {"hand_limit_offset": 1})
    assert not is_frozen_identity_knob("L1_AUTODAFE_COOLDOWN_PLUS1", {"cooldown_offset": 1})
    ids = {c[0] for c in generate_all_atomic_candidates_macro()}
    assert "L1_HAND_LIMIT_PLUS1" in ids
    assert "L1_MAX_ERAS_PLUS1" not in ids
    assert "L1_MAX_ERAS_MINUS1" not in ids
    assert "L1_AUTODAFE_COOLDOWN_PLUS1" in ids
    assert "L1_OBSERVED_PLUS1" in ids
    assert "L1_CARDS_PER_ERA_PLUS1" in ids
    assert "L1_INTRIGUE_GOLD_PLUS1" not in ids
    assert "L1_INTRIGUE_GOLD_MINUS1" not in ids


def test_gospodarcza_is_frozen_identity_knob():
    assert is_ablation_off("L1_INTRIGUE_GOLD_MINUS1", {"intrigue_gold_offset": -1})
    assert is_ablation_off("L1_INTRIGUE_GOLD_PLUS1", {"intrigue_gold_offset": 1})
    base = _dead_skazania_base()
    base["vitality_penalty"] = 0.0
    base["vitality_warnings"] = []
    cand = {
        **base,
        "id": "L1_INTRIGUE_GOLD_PLUS1",
        "params": {"intrigue_gold_offset": 1},
        "score_4p": 90.0,
        "min_balance": 90.0,
    }
    d = accept_macro_candidate(base, cand, mode="band", min_delta=0.05)
    assert not d.accepted
    assert "zamrożona" in d.reason or "tożsamość" in d.reason or "ablacja" in d.reason


def test_macro_vector_beats_requires_score_or_vitality():
    held = {"score_4p": 73.7, "score_4p_balance": 73.7, "vitality_penalty": 0.0, "deadlock_pct": 1.0}
    rider = {"score_4p": 73.7, "score_4p_balance": 73.7, "vitality_penalty": 0.0, "deadlock_pct": 0.4}
    better = {"score_4p": 74.0, "score_4p_balance": 74.0, "vitality_penalty": 0.0, "deadlock_pct": 1.0}
    vit = {"score_4p": 73.7, "score_4p_balance": 73.7, "vitality_penalty": 0.0, "deadlock_pct": 1.0}
    assert not macro_vector_beats(rider, held, 0.05)
    assert macro_vector_beats(better, held, 0.05)
    held_vit = {**held, "vitality_penalty": 1.2}
    assert macro_vector_beats(vit, held_vit, 0.05)


def test_chronicle_tempo_rejected_at_accept():
    base = _dead_skazania_base()
    base["vitality_penalty"] = 0.0
    base["vitality_warnings"] = []
    cand = {
        **base,
        "id": "L4_TIME_DECK_EVERY_2ERAS",
        "params": {"time_deck_freq": 2},
        "score_4p": 90.0,
        "min_balance": 90.0,
    }
    d = accept_macro_candidate(base, cand, mode="band", min_delta=0.05)
    assert not d.accepted
    assert "tożsamość" in d.reason


def test_crutch_veto_rejects_lowering_dead_condemns():
    base = _dead_skazania_base()
    cand = {
        **base,
        "id": "L2_SO_CONDEMNS_MINUS1",
        "params": {"so_condemns_offset": -1},
        "score_4p": 90.0,
        "vitality_penalty": 0.0,
        "acc_avg": 3.0,
    }
    d = accept_macro_candidate(base, cand, mode="band", min_delta=0.05)
    assert not d.accepted
    assert "proteza" in d.reason
    assert is_dead_path_crutch(base, cand["params"])


def test_crutch_not_applied_when_path_is_alive():
    base = _dead_skazania_base()
    base["vitality_warnings"] = []
    base["vitality_penalty"] = 0.0
    assert not is_dead_path_crutch(base, {"so_condemns_offset": -1})


def test_drop_crutches_from_pool_and_beam():
    base = _dead_skazania_base()
    pool = [
        ("L2_SO_CONDEMNS_MINUS1", "skazania −1", {"so_condemns_offset": -1}),
        ("L2_SO_CONDEMNS_LO", "skazania skraj", {"so_condemns_offset": -2}),
        ("L1_AUTODAFE_DISABLED", "autodafé off", {"autodafe_cooldown": 99}),
        ("L2_SO_CONDEMNS_HI", "skazania +", {"so_condemns_offset": 3}),
    ]
    kept = drop_dead_path_crutches(base, pool)
    ids = {c[0] for c in kept}
    assert "L2_SO_CONDEMNS_MINUS1" not in ids
    assert "L2_SO_CONDEMNS_LO" not in ids
    assert "L1_AUTODAFE_DISABLED" in ids
    assert "L2_SO_CONDEMNS_HI" in ids


def test_merge_2d_rejects_overlapping_keys_and_keeps_no_cards():
    a = ("L1_A", "a", {"autodafe_cooldown": 99})
    b = ("L2_B", "b", {"so_condemns_offset": 3})
    merged = merge_mutations(a, b)
    assert merged is not None
    assert merged[0] == "L1_A__L2_B"
    assert "card_overrides" not in merged[2]
    clash = merge_mutations(a, ("L1_A2", "a2", {"autodafe_cooldown": 0}))
    assert clash is None


def test_absolute_extremes_persist_to_yaml_keys():
    raw = {
        "system": {"start_gold": 4, "max_eras": 12, "autodafe_cooldown": 3, "accusation_threshold": 7},
        "victory": {"swiete_oficjum": {"stacks": 5, "condemns": 3}, "gildia_cieni": {"falls": {"default": 3, "no_oficjum": 5}}},
        "variants": {"time_deck_freq": 1, "sea_route_era": 4, "inquisitor_speed": 1},
        "cards": {},
    }
    cfg, desc = apply_mutation_to_config(raw, "L1_AUTODAFE_DISABLED", {"autodafe_cooldown": 99})
    assert cfg["system"]["autodafe_cooldown"] == 99
    assert "99" in desc
    cfg, _ = apply_mutation_to_config(raw, "L1_START_GOLD_0", {"start_gold": 0})
    assert cfg["system"]["start_gold"] == 0
    cfg, _ = apply_mutation_to_config(
        {"system": {}, "victory": {"gildia_cieni": {"falls": 4}}, "variants": {}, "cards": {}},
        "L2_GC_FALLS_PLUS1",
        {"gc_falls_offset": 1},
    )
    assert cfg["victory"]["gildia_cieni"]["falls"] == 5
    cfg, _ = apply_mutation_to_config(
        {"system": {}, "victory": {"korona_borgiowie": {"decrees": 2}}, "variants": {}, "cards": {}},
        "L2_KB_ERA_PLUS1",
        {"kb_era_offset": 1},
    )
    assert "era" not in cfg["victory"]["korona_borgiowie"]


def test_lookahead_1d_always_peeks_2d():
    assert lookahead_next_action(depth=1, max_depth=4, has_pending=False, found_better=False) == "deeper_empty"
    assert lookahead_next_action(depth=1, max_depth=4, has_pending=False, found_better=True) == "hold_and_deeper"


def test_lookahead_holds_then_applies_shallower_if_deeper_misses():
    assert lookahead_next_action(depth=2, max_depth=4, has_pending=True, found_better=False) == "apply_pending"
    assert lookahead_next_action(depth=2, max_depth=4, has_pending=True, found_better=True) == "hold_and_deeper"


def test_lookahead_stop_when_2d_empty_and_nothing_held():
    assert lookahead_next_action(depth=2, max_depth=4, has_pending=False, found_better=False) == "stop"


def test_lookahead_applies_at_max_depth():
    assert lookahead_next_action(depth=4, max_depth=4, has_pending=True, found_better=True) == "apply_current"
    assert lookahead_next_action(depth=4, max_depth=4, has_pending=True, found_better=False) == "apply_pending"


def test_generate_antagonistic_and_hybrid_candidates_with_slug_shares():
    from audytor_kanonu import generate_all_atomic_candidates, generate_antagonistic_and_hybrid_candidates
    base_res = {
        "setup_scores": {"4p-no-oficjum": 71.0, "4p-core": 90.0},
        "setup_shares": {
            "4p-no-oficjum": {"cienie-al-andalus": 19.0, "gildia-cieni": 31.0, "korona-borgiowie": 25.0, "kabala-toledo": 25.0},
            "4p-core": {"swiete-oficjum": 25.0, "cienie-al-andalus": 25.0, "korona-borgiowie": 25.0, "kabala-toledo": 25.0},
        },
    }
    atomic_pool = generate_all_atomic_candidates()
    antag = generate_antagonistic_and_hybrid_candidates(base_res, atomic_pool)
    assert len(antag) > 0
    # Sprawdź czy wygenerowano pary uderzające w dominantę GC i wspomagające deficyt CAA
    has_gc_nerf_caa_buff = any("L3_GC-" in c[0] and "L3_CAA-" in c[0] for c in antag)
    assert has_gc_nerf_caa_buff

