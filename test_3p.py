import sys
sys.path.insert(0, 'src')
import inquisitio_native
res = inquisitio_native.run_batch(games=1000, setup="3p-oficjum-korona-kabala")
wins = res["wins"]
total = sum(wins.values())
for k, v in wins.items():
    print(f"{k}: {v/total*100:.1f}%")
