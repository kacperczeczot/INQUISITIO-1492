[Strona główna](../../README.md) > [Playtesting](../README.md) > [Raporty Symulacji](README.md)

---

# 📊 Raporty Symulacji i Audytów Balansu

Katalog zawiera automatycznie generowane raporty symulacyjne silnika `INQUISITIO-1492`.

## 📁 Struktura Katalogu

Wszystkie raporty, dzienniki iteracji (`audytor_*_log.md` / `canon_4p_log.md`) oraz snapshoty `game_config.yaml` są zapisywane bezpośrednio w dedykowanych folderach per wersja balansu:

- **📁 `archive/v0.XX/` — Kompletne Raporty Wersji Balansu:**
  - `archive/v0.69/`, `archive/v0.68/`, `archive/v0.67/`, ...
  - [`game_config.yaml`](archive/v0.69/game_config.yaml) — zamrożona migawka konfiguracji gry danej wersji
  - [`raport_telemetrii.md`](archive/v0.69/raport_telemetrii.md) — pełny rozkład szans wygranych (Win Shares) dla 16 setupów i 5 filarów telemetrii
  - [`raport_optymalizacji_kanonu.md`](archive/v0.69/raport_optymalizacji_kanonu.md) — raport z audytu optymalizatora
  - Dzienniki audytorów (`canon_4p_log.md`, `audytor_4p_log.md`, `audytor_3p_log.md`, `audytor_5p_log.md`)
  - Szczegółowe raporty audytów poziomów (`audyt_level1_raport.md` do `audyt_level4_raport.md`, `audyt_stress_raport.md`) jeśli wygenerowano w danej wersji
- **📁 `game_replays/` — Zapisy Partii Krok-po-Kroku**

## 🛠️ Generowanie i Archiwizacja

Uruchomienie generatorów raportów automatycznie stempluje numer wersji balansu z `game_config.yaml` oraz zapisuje kopię w `archive/{wersja}/`:

```bash
# 1. Pełny Grand Audit (Wszystkie poziomy L1–L4 + stres ekonomiczny + telemetria 16 setupów)
python tools/sim/run_grand_audit.py

# 2. Autonomiczne optymalizatory (Lookahead +1D)
python tools/sim/audytor_kanonu.py --workers 10
python tools/sim/audytor_4p.py --workers 10
python tools/sim/audytor_3p.py --workers 10
python tools/sim/audytor_5p.py --workers 10
```
