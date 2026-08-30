#!/usr/bin/env python3
"""INQUISITIO-1492 — GRAND COMBO AUDITOR (Global Greedy Optimizer)."""

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
from inquisitio.cards.loader import load_all_cards
from inquisitio.config import CONFIG, _CONFIG_PATH
from inquisitio.engine.setup import SETUP_PRESETS
from inquisitio.runner.adaptive_racer import AdaptiveSequentialRacer
from inquisitio.runner.canon_accept import accept_global_candidate

import audit_level1
import audit_level2
import audit_level3
import audit_level4

def apply_global_combo_mutation(raw_cfg: dict[str, Any], rule_params: dict[str, Any], raw_cards: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    """Applies isolated 3p/4p/5p parameters + global L3 card parameters."""
    cfg = copy.deepcopy(raw_cfg)
    cards = copy.deepcopy(raw_cards)

    def _set_mode(section_dict: dict, key: str, default_val: Any, mode: str, offset: Any):
        if offset is None: return
        off = int(offset)
        cur = section_dict.get(key, default_val)
        if isinstance(cur, dict):
            val_cand = cur.get(mode, cur.get("4p", default_val))
            base_v = int(val_cand) if val_cand is not None else int(default_val)
            new_v = max(1, base_v + off)
            cur[mode] = new_v
        else:
            base_v = int(cur) if cur is not None else int(default_val)
            new_v = max(1, base_v + off)
            section_dict[key] = {"3p": cur, "4p": cur, "5p": cur}
            section_dict[key][mode] = new_v

    for k, v in rule_params.items():
        if k == "card_overrides":
            for cid, param_dict in v.items():
                if cid not in cards: cards[cid] = {}
                for pk, pv in param_dict.items():
                    cards[cid][pk] = pv
            continue

        mode = None
        if k.startswith("3P_"): mode, base_k = "3p", k[3:]
        elif k.startswith("4P_"): mode, base_k = "4p", k[3:]
        elif k.startswith("5P_"): mode, base_k = "5p", k[3:]
        else: continue

        if base_k == "start_gold_offset": _set_mode(cfg.setdefault("system", {}), "start_gold", 4, mode, v)
        elif base_k == "threshold_offset": _set_mode(cfg.setdefault("system", {}), "accusation_threshold", 6, mode, v)
        elif base_k == "agents_offset": _set_mode(cfg.setdefault("system", {}), "agents_per_player", 3, mode, v)
        elif base_k == "hand_limit_offset": _set_mode(cfg.setdefault("system", {}), "hand_limit", 5, mode, v)
        
        elif base_k == "gc_falls_offset": _set_mode(cfg.setdefault("victory", {}).setdefault("gildia_cieni", {}), "falls", 9, mode, v)
        elif base_k == "so_stacks_offset": _set_mode(cfg.setdefault("victory", {}).setdefault("swiete_oficjum", {}), "stacks", 7, mode, v)
        elif base_k == "so_condemns_offset": _set_mode(cfg.setdefault("victory", {}).setdefault("swiete_oficjum", {}), "condemns", 3, mode, v)
        elif base_k == "caa_relics_offset": _set_mode(cfg.setdefault("victory", {}).setdefault("cienie_al_andalus", {}), "relics", 2, mode, v)
        elif base_k == "kb_decrees_offset": _set_mode(cfg.setdefault("victory", {}).setdefault("korona_borgiowie", {}), "decrees", 2, mode, v)
        elif base_k == "kt_frags_offset": _set_mode(cfg.setdefault("victory", {}).setdefault("kabala_toledo", {}), "fragments", 3, mode, v)

    return cfg, cards

def generate_global_pool():
    pool = []
    def _add_split(tests):
        for tid, tname, tdict in tests:
            if tid.endswith("BAZA") or not tdict: continue
            pool.append((f"3P_{tid}", f"[3P] {tname}", {f"3P_{k}": v for k, v in tdict.items()}))
            pool.append((f"4P_{tid}", f"[4P] {tname}", {f"4P_{k}": v for k, v in tdict.items()}))
            pool.append((f"5P_{tid}", f"[5P] {tname}", {f"5P_{k}": v for k, v in tdict.items()}))
            
    _add_split(audit_level1.build_level1_tests())
    _add_split(audit_level2.build_level2_tests())
    for tid, tname, tdict in audit_level3.build_level3_tests(param_filter="cost,heresy"):
        if tid.endswith("BAZA") or not tdict: continue
        pool.append((tid, f"[L3] {tname}", tdict))
    return pool

def save_new_config(cfg, cards, version):
    with open(_CONFIG_PATH, 'w') as f:
        yaml.dump(cfg, f, default_flow_style=False, sort_keys=False)

def main():
    print("═══════════════════════════════════════════════════════════════════════")
    print("   INQUISITIO-1492 — GRAND COMBO AUDITOR (Global Greedy Optimizer)    ")
    print("═══════════════════════════════════════════════════════════════════════")
    
    with open(_CONFIG_PATH, "r", encoding="utf-8") as f:
        curr_cfg = yaml.safe_load(f)
    curr_cards = load_all_cards(as_dict=True)
    atomic_pool = generate_global_pool()
    setups_to_run = list(SETUP_PRESETS.keys())
    
    iteration = 1
    while True:
        print(f"\n🌀 --- ITERACJA #{iteration} ---")
        base_racer = AdaptiveSequentialRacer(
            "BASE", "Baza", {},
            target_setups=setups_to_run,
            game_config=curr_cfg, card_overrides={}
        )
        base_racer.run_micro_steps(max_games=6400)
        print(f"   Baza Global Score: {base_racer.score_global:.2f} | 4P: {base_racer.score_4p:.2f}")
        
        base_dict = {
            "score_global": base_racer.score_global,
            "score_4p": base_racer.score_4p,
            "min_balance": base_racer.min_balance,
            "vitality_penalty": base_racer.vitality_penalty,
            "vitality_warnings": base_racer.vitality_warnings
        }
        
        print(f"\n🏁 [START] Pula: {len(atomic_pool)} atomów")
        racers = []
        for tid, tname, rule_params in atomic_pool:
            n_cfg, n_cards = apply_global_combo_mutation(curr_cfg, rule_params, curr_cards)
            racers.append(AdaptiveSequentialRacer(
                tid, tname, rule_params,
                target_setups=setups_to_run,
                game_config=n_cfg, card_overrides=rule_params.get("card_overrides", {})
            ))
            
        for stage in [400, 1600, 6400]:
            print(f"⏳ [N={stage}] Startuje {len(racers)} kandydatów...")
            active = []
            for r in racers:
                r.run_micro_steps(max_games=stage)
                if r.vitality_penalty > 0.10: r.is_pruned = True
                elif r.score_global < base_dict["score_global"] - 1.0: r.is_pruned = True
                if not r.is_pruned: active.append(r)
            racers = active
            if not racers: break
                
        if not racers:
            print("\n🛑 LOKALNE OPTIMUM OSIĄGNIĘTE. Brak zyskownych atomów.")
            break
            
        racers.sort(key=lambda x: x.score_global, reverse=True)
        best = racers[0]
        cand_dict = {
            "score_global": best.score_global,
            "score_4p": best.score_4p,
            "min_balance": best.min_balance,
            "vitality_penalty": best.vitality_penalty,
            "vitality_warnings": best.vitality_warnings
        }
        
        decision = accept_global_candidate(base_dict, cand_dict)
        print(f"\n🏆 Najlepszy z puli: {best.desc}")
        print(f"   Decyzja: {decision.accepted} - {decision.reason}")
        
        if decision.accepted:
            print(f"✅ ZNALEZIONO POPRAWKĘ! Aktualizuję bazę i idę dalej (Kombos stacking)!")
            curr_cfg, curr_cards = apply_global_combo_mutation(curr_cfg, best.rule_params, curr_cards)
            iteration += 1
        else:
            print("\n🛑 Brak akceptowalnego kandydata. Koniec optymalizacji.")
            break

if __name__ == "__main__":
    main()
