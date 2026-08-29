import re
from pathlib import Path

for filename in ['scripts/sim/audytor_3p.py', 'scripts/sim/audytor_5p.py']:
    text = Path(filename).read_text()
    
    # 1. Update argparse
    argparse_block = """    parser.add_argument("--hours", type=float, default=None, help="Maksymalny czas sesji w godzinach")
    parser.add_argument("--max-iters", type=int, default=None, help="Maksymalna liczba udanych patchów")
    
    # Adaptive Monte Carlo Racing parameters
    parser.add_argument("--batch-step", type=int, default=400, help="Rozmiar mikro-kroku partii na setup (domyślnie: 400)")
    parser.add_argument("--min-games", type=int, default=400, help="Minimalna liczba gier/setup przed sprawdzeniem kryterium stopu (domyślnie: 400)")
    parser.add_argument("--max-games", type=int, default=6400, help="Maksymalna liczba gier/setup w wyścigu (domyślnie: 6400)")
    parser.add_argument("--epsilon-indiff", type=float, default=0.15, help="Próg strefy nierozróżnialności / szumu balansu w pkt (domyślnie: 0.15)")
    parser.add_argument("--confirm-games", type=int, default=10000, help="Liczba gier weryfikujących SSOT (domyślnie: 10000)")
    
    parser.add_argument("--min-delta", type=float, default=0.05, help="Minimalny zysk punktowy dla 3P (domyślnie: 0.05)")"""
    
    if "audytor_5p" in filename:
        argparse_block = argparse_block.replace("dla 3P", "dla 5P")
        
    text = re.sub(r'    parser\.add_argument\("--hours".*?\n.*?min-delta.*?\n', argparse_block + '\n', text, flags=re.DOTALL)
    
    # 2. Update racer instantiation
    racer_init = """        racer = AdaptiveSequentialRacer(
            setups=setups,
            batch_step=self.args.batch_step,
            min_games=self.args.min_games,
            max_games=self.args.max_games,
            epsilon_indiff=self.args.epsilon_indiff,
            workers=self.args.workers,
            min_delta=self.args.min_delta,
        )"""
    
    text = re.sub(r'        racer = AdaptiveSequentialRacer\([\s\S]*?min_delta=self\.args\.min_delta,\n        \)', racer_init, text)
    
    # 3. Update SSOT game counts
    # find `_run_full_diagnostic(..., games_per_setup=10000, seed=42)` and replace with `self.args.confirm_games`
    text = text.replace('games_per_setup=10000', 'games_per_setup=self.args.confirm_games')
    
    Path(filename).write_text(text)

print("Fixed 3p and 5p.")
