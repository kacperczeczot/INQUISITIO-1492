import re
from pathlib import Path

path = Path('scripts/sim/audytor_4p.py')
text = path.read_text()

# We need to replace lines 870 to 900 roughly. Let's find the exact block using regex.
block_to_replace_regex = r'                cand_dict = \{c\[0\]: c for c in candidate_pool\}[\s\S]*?if accepted_candidate is not None and best_ver_res is not None:'

replacement = """                cand_dict = {c[0]: c for c in candidate_pool}
                
                # 2A. Wyścig Adaptive Monte Carlo Racer (od 400 do max_games)
                racer = AdaptiveSequentialRacer(
                    setups=setups,
                    batch_step=self.args.batch_step,
                    min_games=self.args.min_games,
                    max_games=self.args.max_games,
                    epsilon_indiff=self.args.epsilon_indiff,
                    workers=self.args.workers,
                    min_delta=self.args.min_delta,
                )
                
                target_floor = pending_res["score_4p_balance"] if pending_res else None
                base_stats, candidate_results = racer.run_race(
                    base_cand=("BASE", "Baza", {}),
                    candidate_pool=candidate_pool,
                    seed=self.args.seed,
                    delta_pool=None,
                    label_prefix=f"WYŚCIG MAKRO 4P — FAZA {current_phase}D",
                    target_floor_score=target_floor,
                    base_stats_cache=None,
                )
                
                surviving_stats = [c for c in candidate_results if not c.is_pruned]
                surviving_stats.sort(key=lambda x: rank_key(x.to_result_dict()))
                
                accepted_candidate = None
                best_ver_res = None
                
                if surviving_stats:
                    # Bierzemy top lidera po wyścigu i weryfikujemy go na twardej próbie 10k
                    leader_stats = surviving_stats[0]
                    leader_cand = cand_dict[leader_stats.id]
                    print(f"\\n--- [OSTATECZNA WERYFIKACJA 10K] Lider z wyścigu: {leader_cand[1]} ---")
                    
                    stage3_task = ((leader_cand[0], leader_cand[1], leader_cand[2]), self.args.confirm_games, self.args.seed, setups)
                    stage3_results = self._execute_pool(_run_single_test_task_4p, [stage3_task], label=f"Weryfikacja SSOT 10k")
                    ver_res = stage3_results[0]
                    
                    decision = accept_macro_candidate(
                        base_res, ver_res, min_delta=self.args.min_delta
                    )
                    
                    print(
                        f"   [WERYFIKACJA 10k] win share {ver_res.get('score_4p_balance', ver_res['score_4p']):.1f} | "
                        f"witalność {ver_res.get('vitality_penalty', 0):.3f} | {decision.reason}"
                    )
                    
                    if decision.accepted:
                        accepted_candidate = leader_cand
                        best_ver_res = ver_res

                if accepted_candidate is not None and best_ver_res is not None:"""

if re.search(block_to_replace_regex, text):
    text = re.sub(block_to_replace_regex, replacement, text)
    path.write_text(text)
    print("Successfully replaced.")
else:
    print("Regex failed to match!")
