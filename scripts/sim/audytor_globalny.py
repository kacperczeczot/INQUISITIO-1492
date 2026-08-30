#!/usr/bin/env python3
"""INQUISITIO-1492 — GRAND COMBO AUDITOR (Global Beam Search Optimizer)."""

import argparse
import copy
import sys
import time
from pathlib import Path
from typing import Any

# Ścieżki
TOOLS_SRC_DIR = Path(__file__).resolve().parent
SRC_DIR = TOOLS_SRC_DIR.parent.parent / "src"
for p in (TOOLS_SRC_DIR, SRC_DIR):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

import yaml
from datetime import datetime
from inquisitio.config import _CONFIG_PATH
from inquisitio.engine.setup import SETUP_PRESETS
from inquisitio.runner.adaptive_racer import AdaptiveSequentialRacer, merge_mutations
from inquisitio.runner.canon_accept import accept_global_candidate
from inquisitio.runner.batch import run_batch
from inquisitio.runner.scoring import calculate_setup_score, calculate_category_scores, calculate_global_score
from audytor_kanonu import select_diverse_beam_seeds

import audit_level1
import audit_level2
import audit_level3
import audit_level4

BALANCE_NOTES_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "playtesting" / "balance-notes.md"
REPORTS_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "playtesting" / "sim-reports"

def _run_full_diagnostic(rule_params: dict, games_per_setup: int = 1000, seed: int = 42) -> dict:
    all_setups = sorted(SETUP_PRESETS.keys())
    summaries = []
    setup_scores = {}
    for sname in all_setups:
        s = run_batch(games=games_per_setup, setup=sname, seed=seed, layer="C", win_overrides=rule_params)
        summaries.append(s)
        setup_scores[sname] = calculate_setup_score(s)
    cat_scores = calculate_category_scores(summaries)
    global_score = calculate_global_score(cat_scores)
    return {
        "score_global": global_score,
        "score_3p": cat_scores.get("3p", 0.0),
        "score_4p": cat_scores.get("4p", 0.0),
        "score_5p": cat_scores.get("5p", 0.0),
    }

def get_cat_score(res_dict: dict, prefix: str) -> float:
    scores = [s for k, s in res_dict.get("setup_scores", {}).items() if k.startswith(prefix)]
    return sum(scores) / len(scores) if scores else 0.0

def update_balance_notes(
    old_version: str,
    new_version: str,
    change_desc: str,
    rule_id: str,
    base_dict: dict,
    best_dict: dict,
):
    if not BALANCE_NOTES_PATH.exists(): return
    content = BALANCE_NOTES_PATH.read_text(encoding="utf-8")
    today = datetime.now().strftime("%Y-%m-%d")
    d_g = best_dict["score_global"] - base_dict["score_global"]
    delta_str = f"+{d_g:.1f}" if d_g > 0 else f"{d_g:.1f}"
    
    patch_note_block = (
        f"### 🌐 Patch {new_version} ({today}) — Global Auditor: {change_desc} (Zysk Global Δ {delta_str} pkt)\n"
        f"- **Modyfikacja:** `{rule_id}` -> {change_desc}\n"
        f"- **Wynik Globalny:** {base_dict['score_global']:.1f} → **{best_dict['score_global']:.1f}**\n"
        f"- **Balans 4P:** {base_dict['score_4p']:.1f} → {best_dict['score_4p']:.1f}\n"
        f"- **Balans 3P:** {base_dict['score_3p']:.1f} → {best_dict['score_3p']:.1f}\n"
        f"- **Balans 5P:** {base_dict['score_5p']:.1f} → {best_dict['score_5p']:.1f}\n"
        f"\n"
    )
    
    history_heading = "## 📜 Chronologiczna Historia Zmian Balansu (Faza Prototypowa — Patch Notes)"
    if history_heading in content:
        idx = content.find(history_heading) + len(history_heading)
        content = content[:idx] + "\n\n" + patch_note_block.strip() + "\n\n" + content[idx:].lstrip("\n")
        BALANCE_NOTES_PATH.write_text(content, encoding="utf-8")

def log_global_iteration(
    log_path: Path, iteration: int, depth: int,
    old_version: str, new_version: str, desc: str,
    base_dict: dict, best_dict: dict
):
    log_path.parent.mkdir(parents=True, exist_ok=True)
    if not log_path.exists():
        headers = [
            "# Dziennik Optymalizacji Globalnej (Beam Search)",
            "",
            "| Iteracja | Depth | Data | Wersja | Modyfikacja | Global Score | 3P Score | 4P Score | 5P Score |",
            "| :---: | :---: | :---: | :---: | :--- | :---: | :---: | :---: | :---: |"
        ]
        log_path.write_text("\n".join(headers) + "\n", encoding="utf-8")
        
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    row = (
        f"| #{iteration} | {depth}D | {now} | `{old_version}` → `{new_version}` | "
        f"**{desc}** | "
        f"{base_dict['score_global']:.1f} → **{best_dict['score_global']:.1f}** | "
        f"{base_dict['score_3p']:.1f} → {best_dict['score_3p']:.1f} | "
        f"{base_dict['score_4p']:.1f} → {best_dict['score_4p']:.1f} | "
        f"{base_dict['score_5p']:.1f} → {best_dict['score_5p']:.1f} |"
    )
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(row + "\n")

def generate_global_pool():
    """Generates complete universal atomic pool across all 4 levels:
    - Level 1: System Macro Rules (thresholds, observed, cards/era, era_income, intrigue_gold, max_eras, autodafe_cooldown, start_gold, agents)
    - Level 2: Faction Victory Goals (stacks, condemns, relics, decrees, hooks, fragments, falls across 3p/4p/5p)
    - Level 3: All Card Parameters (cost, heresy, target_heresy, gold, agents across all 60 cards)
    - Level 4: Niche Variants & Economy Rules (sea route, time deck, card/sig cost offsets)
    """
    pool = []
    def _add_split(tests):
        for tid, tname, tdict in tests:
            if tid.endswith("BAZA") or not tdict: continue
            pool.append((tid, tname, tdict))
            
    # L1 & L2 rules for 3P, 4P, 5P
    _add_split(audit_level1.build_level1_tests())
    _add_split(audit_level2.build_level2_tests())
    
    # L3 cards (global - ALL parameters: cost, heresy, target_heresy, gold, agents)
    for tid, tname, tdict in audit_level3.build_level3_tests(param_filter="all"):
        if tid.endswith("BAZA") or not tdict: continue
        pool.append((tid, f"[L3] {tname}", tdict))
        
    # L4 variants & economy
    _add_split(audit_level4.build_level4_tests())
    
    return pool

def parse_args():
    parser = argparse.ArgumentParser(description="Grand Combo Auditor (Global Beam Search Optimizer)")
    parser.add_argument("--beam-width", type=int, default=20, help="Szerokość wiązki (ile najlepszych mutacji przechodzi do kolejnej fazy)")
    parser.add_argument("--max-depth", type=int, default=6, help="Maksymalna głębokość przeszukiwania (kombosy N-wymiarowe)")
    parser.add_argument("--min-delta", type=float, default=0.05, help="Minimalny zysk globalny do wdrożenia patcha")
    parser.add_argument("--continuous", action="store_true", default=True, help="Tryb pracy ciągłej bez przedwczesnego wyłączania")
    return parser.parse_args()

def main():
    args = parse_args()
    print("═══════════════════════════════════════════════════════════════════════")
    print("   INQUISITIO-1492 — GRAND COMBO AUDITOR (Global Beam Search Optimizer)")
    print(f"   Parametry: Wiązka (Beam) = {args.beam_width}, Głębokość (Depth) = {args.max_depth}")
    print("═══════════════════════════════════════════════════════════════════════")
    
    atomic_pool = generate_global_pool()
    setups_to_run = list(SETUP_PRESETS.keys())
    
    racer = AdaptiveSequentialRacer(
        setups=setups_to_run,
        batch_step=400,
        min_games=400,
        max_games=6400,
        epsilon_indiff=0.15,
        workers=10,
        min_delta=0.05,
        target_metric="global",
    )
    
    current_base_cand = ("BAZA", "Konfiguracja Startowa", {})
    iteration = 1
    
    print("\n🔍 [BENCHMARK 10K] Obliczam stan referencyjny 10 000 gier/setup dla BAZY początkowej...")
    base_dict_10k = _run_full_diagnostic({}, games_per_setup=10000, seed=42)
    
    while True:
        print(f"\n=======================================================================")
        print(f"🔄 ITERACJA #{iteration} (Baza: {current_base_cand[1]})")
        print(f"=======================================================================")
        
        patch_found = False
        beam_seeds = [current_base_cand]
        cached_base_stats = None
        base_dict = None
        
        for depth in range(1, args.max_depth + 1):
            print(f"\n🌀 --- GŁĘBOKOŚĆ (DEPTH) #{depth} ---")
            
            candidate_pool = []
            seen = set()
            
            # Cross current beam seeds with all atomic mutations
            for seed in beam_seeds:
                for atom in atomic_pool:
                    merged = merge_mutations(seed, atom)
                    if merged and merged[0] not in seen:
                        candidate_pool.append(merged)
                        seen.add(merged[0])
                        
            print(f"🏁 Wygenerowano {len(candidate_pool)} kandydatów do przetestowania.")
            if not candidate_pool:
                print("🛑 Brak możliwych kombinacji.")
                break
                
            base_stats, ranked_stats = racer.run_race(
                base_cand=current_base_cand,
                candidate_pool=candidate_pool,
                seed=42 + depth + iteration * 100,
                label_prefix=f"GŁĘBOKOŚĆ {depth}",
                base_stats_cache=cached_base_stats,
            )
            cached_base_stats = base_stats
            if base_dict is None:
                base_dict = base_stats.to_result_dict()
                print(f"\n   Baza Global Score: {base_dict['score_global']:.2f} | 4P: {base_dict['score_4p']:.2f}")
            
            surviving = [c for c in ranked_stats if not c.is_pruned]
            if not surviving:
                print("\n🛑 Wiązka wygasła na tej głębokości (brak ocalałych).")
                break
                
            surviving.sort(key=lambda c: c.to_result_dict()['score_global'], reverse=True)
            
            best_accepted_cand = None
            best_decision = None
            
            # Szukamy pierwszej lepszej akceptowalnej poprawki (GREEDY + 10k CERT)
            from inquisitio.config import CONFIG, _CONFIG_PATH
            from inquisitio.config_updater import apply_mutation_to_config, save_config_and_bump_version
            import shutil

            for cand_stat in surviving:
                cand_dict = cand_stat.to_result_dict()
                decision = accept_global_candidate(base_dict, cand_dict)
                
                if decision.accepted:
                    print(f"\n   🟢 [GREEDY 6.4k OK] Kandydat: {cand_stat.name}")
                    print(f"      Decyzja: {decision.reason}")
                    
                    cand_tup = cand_stat.delta_tuple if cand_stat.delta_tuple else cand_stat.cand_tuple
                    rule_id = cand_tup[0]
                    delta_params = cand_tup[2]
                    
                    print(f"   🔍 [CERTYFIKACJA 10K] Potwierdzam kandydata (10 000 gier/setup, potrwa to ~15-20s)...")
                    cand_dict_10k = _run_full_diagnostic(delta_params, games_per_setup=10000, seed=42)
                    
                    delta_10k = cand_dict_10k['score_global'] - base_dict_10k['score_global']
                    if delta_10k >= args.min_delta:
                        print(f"   ✅ [CERTYFIKACJA 10K ZDANA] Zysk: +{delta_10k:.2f} pkt!")
                        best_accepted_cand = cand_stat
                        best_decision = decision
                        best_dict_10k = cand_dict_10k
                        break
                    else:
                        print(f"   🛑 [CERTYFIKACJA 10K ODRZUCONA] Kandydat dał zysk {delta_10k:.2f} pkt w 10k. Odrzucam fałszywy alarm z 6.4k!")
            
            if best_accepted_cand:
                print(f"\n🚀 Wdrażam zweryfikowaną poprawkę w {depth}D: {best_accepted_cand.name}")
                print("   Restartuję poszukiwania od 1D!")
                
                with open(_CONFIG_PATH, "r", encoding="utf-8") as f:
                    current_raw_cfg = yaml.safe_load(f)
                    
                old_version = current_raw_cfg.get("system", {}).get("version", current_raw_cfg.get("version", "unknown"))
                cand_tup = best_accepted_cand.delta_tuple if best_accepted_cand.delta_tuple else best_accepted_cand.cand_tuple
                rule_id = cand_tup[0]
                delta_params = cand_tup[2]
                
                mod_cfg, change_desc = apply_mutation_to_config(current_raw_cfg, rule_id, delta_params)
                new_version, saved_path = save_config_and_bump_version(mod_cfg, _CONFIG_PATH, bump_version=True)
                CONFIG.reload()
                
                # Logging to files
                version_archive_dir = REPORTS_DIR / "archive" / new_version
                version_archive_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy2(_CONFIG_PATH, version_archive_dir / "game_config.yaml")
                
                log_global_iteration(
                    version_archive_dir / "global_log.md",
                    iteration, depth, old_version, new_version, change_desc, base_dict_10k, best_dict_10k
                )
                
                update_balance_notes(
                    old_version, new_version, change_desc, rule_id, base_dict_10k, best_dict_10k
                )
                
                print(f"   Wersja zaktualizowana do: **{new_version}**")
                print("   📑 Zaktualizowano balance-notes.md oraz wygenerowano raport w archiwum!")
                
                current_base_cand = ("BAZA", f"Baza ({new_version})", {})
                base_dict_10k = best_dict_10k
                patch_found = True
                break # Przerwij pętlę głębokości (Beam Search), wracamy do nowej iteracji
            
            if depth < args.max_depth:
                # Advance the beam
                beam_seeds = select_diverse_beam_seeds(surviving, beam_width=args.beam_width)
                print(f"➡️ Brak akceptowalnej poprawki. Przekazuję {len(beam_seeds)} różnorodnych nasion do Głębokości #{depth + 1}")

        if not patch_found:
            print("\n═══════════════════════════════════════════════════════════════════════")
            print(f"🔍 [STATUS EKSPLORACJI] Wyczerpano badaną wiązkę kombinacji do głębokości #{args.max_depth}.")
            if args.continuous:
                print("🔄 [TRYB CIĄGŁY] Odświeżam pełną pulę parametrów i rozpoczynam nowy cykl poszukiwań...")
                atomic_pool = generate_global_pool()
                base_dict_10k = _run_full_diagnostic({}, games_per_setup=10000, seed=42 + iteration)
                time.sleep(1)
            else:
                print(f"🏆 Końcowy wynik: {current_base_cand[1]}")
                if base_dict:
                    print(f"   Wynik Globalny: {base_dict['score_global']:.2f}")
                    print(f"   Minimalny Balans: {base_dict['min_balance']:.2f}%")
                break
            
        iteration += 1
        
if __name__ == "__main__":
    main()
