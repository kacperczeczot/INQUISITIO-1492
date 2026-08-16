[Strona główna](../../README.md) > [Playtesting](../README.md) > [Raporty Symulacji](README.md)

---

# 📊 Raporty Symulacji i Audytów Balansu

Katalog zawiera automatycznie generowane raporty symulacyjne silnika `INQUISITIO-1492`.

## 📁 Struktura Katalogu

- **📁 `current/` — Bieżące Raporty (Wersja Aktywna):**
  - [`current/raport_telemetrii.md`](current/raport_telemetrii.md) — pełny rozkład szans wygranych (Win Shares) dla 16 setupów i 5 filarów telemetrii
  - [`current/raport_uzytecznosci_i_wplywu_4p.md`](current/raport_uzytecznosci_i_wplywu_4p.md) — matryca ablacyjna 50 kart i mechanik w Kanonie 4P
  - [`current/raport_optymalizacji_kanonu.md`](current/raport_optymalizacji_kanonu.md) — raport z audytu optymalizatora 4P (Audytor Kanonu)
  - [`current/audyt_level1_raport.md`](current/audyt_level1_raport.md) — audyt ±1 parametrów systemowych (złoto, agenci, progi, cooldowny)
  - [`current/audyt_level2_raport.md`](current/audyt_level2_raport.md) — audyt ±1 warunków zwycięstwa frakcji i reguł skalowania
  - [`current/audyt_level3_raport.md`](current/audyt_level3_raport.md) — precyzyjny audyt ±1 parametrów pojedynczych kart
  - [`current/audyt_level4_raport.md`](current/audyt_level4_raport.md) — audyt wariantów niszowych i modyfikatorów
  - [`current/audyt_stress_raport.md`](current/audyt_stress_raport.md) — testy stresu ekonomicznego (Poverty Stress Test)
- **📁 `logs/` — Dzienniki Ciągłe Procesów i Optymalizacji:**
  - [`logs/canon_4p_log.md`](logs/canon_4p_log.md) — rejestr iteracji Audytora Kanonu 4P
  - [`logs/audytor_4p_log.md`](logs/audytor_4p_log.md) — rejestr optymalizacji 4P Makro
  - [`logs/audytor_3p_log.md`](logs/audytor_3p_log.md) — rejestr optymalizacji formatu 3P
  - [`logs/audytor_5p_log.md`](logs/audytor_5p_log.md) — rejestr optymalizacji formatu 5P
- **📁 `archive/` — Archiwum Historyczne Wersji:**
  - `archive/v0.58/`, `archive/v0.57/`, ... — kompletne migawki raportów per wersja balansu ze snapshotem `game_config.yaml`
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
