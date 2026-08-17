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
        autodafe_avg=1.0,
        hooks_avg=1.0,
        doubles_avg=0.2,
        passes_forced_pct=0.05,
        eras_limit_pct=0.0,
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
