"""Unit tests for AdaptiveSequentialRacer and CandidateStats."""
from __future__ import annotations

import sys
from pathlib import Path

TOOLS_SIM = Path(__file__).resolve().parents[2] / "tools" / "sim"
if str(TOOLS_SIM) not in sys.path:
    sys.path.insert(0, str(TOOLS_SIM))

from audytor_kanonu import AdaptiveSequentialRacer, CandidateStats
from inquisitio.engine.setup import SETUP_PRESETS


def test_candidate_stats_update_metrics():
    from inquisitio.runner.batch import BatchSummary
    
    cand = CandidateStats(("TEST_MUT", "Test Mutation", {"test_param": 1}))
    
    # Simulate summaries for 5 setups with equal faction wins per setup
    for sname in ["4p-core", "4p-no-cienie", "4p-no-kabala", "4p-no-korona", "4p-no-oficjum"]:
        factions = SETUP_PRESETS[sname]
        wins = {f.value: 50 for f in factions}
        summary = BatchSummary(
            games=200,
            setup=sname,
            threshold=8,
            wins=wins,
            autodafe_avg=1.5,
            accusations_avg=4.0,
            eras_avg=5.5,
        )
        cand.combined_summary_per_setup[sname] = summary
        cand.summaries_per_setup[sname] = [summary]
        
    cand.total_games_per_setup = 200
    cand.update_metrics()
    
    assert cand.score_4p_balance >= 98.0
    assert cand.score_se >= 0.0
    lb, ub = cand.ci_95
    assert lb <= cand.score_4p_balance <= ub
    
    res_dict = cand.to_result_dict()
    assert res_dict["id"] == "TEST_MUT"
    assert "score_4p_balance" in res_dict
    assert "ci_95" in res_dict
    assert "setup_scores_balance" in res_dict


def test_adaptive_racer_pruning_and_racing():
    setups = ["4p-core", "4p-no-cienie", "4p-no-kabala", "4p-no-korona", "4p-no-oficjum"]
    
    racer = AdaptiveSequentialRacer(
        setups=setups,
        batch_step=100,
        min_games=200,
        max_games=400,
        epsilon_indiff=0.20,
        workers=2,
        min_delta=0.50,
    )
    
    base_cand = ("BASE", "Baza", {})
    # Candidate 1: neutral/good
    cand_1 = ("CAND_1", "Kandydat 1", {"observed_threshold_offset": 1})
    # Candidate 2: bad mutation (should be pruned or finish below)
    cand_2 = ("CAND_2", "Kandydat 2", {"start_gold_offset": -5})
    
    base_stats, candidates = racer.run_race(
        base_cand=base_cand,
        candidate_pool=[cand_1, cand_2],
        seed=42,
    )
    
    assert base_stats.total_games_per_setup >= 200
    assert len(candidates) == 2
    for c in candidates:
        assert c.score_4p_balance > 0.0
        assert c.ci_95[0] <= c.score_4p_balance <= c.ci_95[1]
