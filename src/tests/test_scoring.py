"""Win-share balance score vs legacy setup score (vitality blended in)."""
from inquisitio.engine.setup import SETUP_PRESETS
from inquisitio.runner.batch import BatchSummary
from inquisitio.runner.scoring import calculate_balance_score, calculate_setup_score, evaluate_vitality


def _equal_wins(setup: str, games: int = 1000) -> dict[str, int]:
    factions = SETUP_PRESETS[setup]
    n = len(factions)
    base, rem = divmod(games, n)
    wins = {f.value: base for f in factions}
    for f in list(factions)[:rem]:
        wins[f.value] += 1
    return wins


def _summary(setup: str = "4p-core", games: int = 1000, **kwargs) -> BatchSummary:
    wins = kwargs.pop("wins", None) or _equal_wins(setup, games)
    defaults = dict(
        accusations_avg=2.0,
        convictions_avg=0.5,
        autodafe_avg=1.8,
        hooks_avg=1.0,
        doubles_avg=0.2,
        passes_forced_pct=0.05,
        eras_limit_pct=0.0,
        eras_avg=5.5,
    )
    defaults.update(kwargs)
    return BatchSummary(
        games=games,
        setup=setup,
        threshold=7,
        wins=wins,
        **defaults,
    )


def test_equal_shares_balance_and_setup_match_when_vitality_is_zero():
    s = _summary()
    assert evaluate_vitality(s).vitality_penalty == 0.0
    assert calculate_balance_score(s) == calculate_setup_score(s)
    assert calculate_balance_score(s) >= 98.0


def test_so_condemns_never_winning_is_dead_path_not_healthy():
    s = _summary(
        win_paths={
            "so_stacks": 200,
            "so_condemns": 0,
            "caa_sea_route": 100,
            "caa_era": 100,
            "kb_main": 200,
            "kt_codex": 200,
        },
    )
    vit = evaluate_vitality(s)
    assert vit.vitality_penalty > 0.0
    assert any("skazania" in w for w in vit.warnings)


def test_empty_win_paths_does_not_invent_dead_path():
    s = _summary()
    vit = evaluate_vitality(s)
    assert vit.vitality_penalty == 0.0
    assert vit.is_healthy


def test_deadlock_lowers_setup_score_but_not_balance_score():
    s = _summary(eras_limit_pct=0.10)
    vit = evaluate_vitality(s)
    assert vit.vitality_penalty > 0.0
    balance = calculate_balance_score(s)
    setup = calculate_setup_score(s)
    assert balance >= 98.0
    assert setup < balance


def test_early_era_sprint_triggers_vitality_penalty():
    # Era 1-2 sprint: 5% of games in Era 1 and 2
    s_sprint = _summary(
        games=1000,
        eras_avg=5.1,
        era_hist={1: 20, 2: 30, 3: 50, 4: 300, 5: 400, 6: 200},
    )
    vit_sprint = evaluate_vitality(s_sprint)
    assert vit_sprint.vitality_penalty > 0.0
    assert any("Era 1-2" in w for w in vit_sprint.warnings)

    # Clean distribution: 0% in Era 1-2, 3% in Era 3, 15% in Era 4, 82% in Era 5+
    s_clean = _summary(
        games=1000,
        eras_avg=5.5,
        era_hist={3: 30, 4: 150, 5: 500, 6: 320},
    )
    vit_clean = evaluate_vitality(s_clean)
    assert vit_clean.vitality_penalty == 0.0
    assert vit_clean.is_healthy


def test_calculate_balance_score_se_delta_method():
    from inquisitio.runner.scoring import calculate_balance_score_se, calculate_balance_stats
    
    # 1. Equal shares: SE should be very small
    s_equal = _summary(games=1000)
    se_equal = calculate_balance_score_se(s_equal)
    assert 0.0 <= se_equal < 0.2
    
    # 2. Imbalanced shares: SE should be non-zero and decrease with sqrt(N)
    imbalanced_wins_100 = {
        "swiete-oficjum": 45,
        "cienie-al-andalus": 25,
        "korona-borgiowie": 15,
        "kabala-toledo": 15,
    }
    s_imb_100 = _summary(games=100, wins=imbalanced_wins_100)
    score_100, se_100 = calculate_balance_stats(s_imb_100)
    
    imbalanced_wins_1000 = {
        "swiete-oficjum": 450,
        "cienie-al-andalus": 250,
        "korona-borgiowie": 150,
        "kabala-toledo": 150,
    }
    s_imb_1000 = _summary(games=1000, wins=imbalanced_wins_1000)
    score_1000, se_1000 = calculate_balance_stats(s_imb_1000)
    
    assert score_100 == score_1000
    # Standard error with 10x games should be ~sqrt(10) ≈ 3.16 times smaller
    ratio = se_100 / se_1000
    assert 2.5 <= ratio <= 3.8


def test_merge_batch_summaries():
    from inquisitio.runner.batch import merge_batch_summaries
    
    s1 = _summary(games=200, autodafe_avg=1.0, eras_avg=5.0, eras_min=3, eras_max=7)
    s2 = _summary(games=300, autodafe_avg=2.0, eras_avg=6.0, eras_min=4, eras_max=9)
    
    merged = merge_batch_summaries([s1, s2])
    assert merged.games == 500
    assert merged.eras_min == 3
    assert merged.eras_max == 9
    # Weighted averages: (1.0*200 + 2.0*300)/500 = 1.6
    assert abs(merged.autodafe_avg - 1.6) < 1e-6
    # (5.0*200 + 6.0*300)/500 = 5.6
    assert abs(merged.eras_avg - 5.6) < 1e-6

