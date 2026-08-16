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
  - [`logs/auto_balancer_log.md`](logs/auto_balancer_log.md) — dziennik działania Szalonego Audytora
  - [`logs/outlier_hunter_log.md`](logs/outlier_hunter_log.md) — rejestr optymalizacji niszowych setupów
- **📁 `archive/` — Archiwum Historyczne Wersji:**
  - `archive/v0.56/`, `archive/v0.55/`, ... — kompletne migawki raportów per wersja balansu ze snapshotem `game_config.yaml`
- **📁 `game_replays/` — Zapisy Partii Krok-po-Kroku**

## 🛠️ Generowanie i Archiwizacja

Uruchomienie generatorów raportów automatycznie stempluje numer wersji balansu z `game_config.yaml` oraz zapisuje kopię w `archive/{wersja}/`:

```bash
# 1. Standardowy pełny audyt balansu (Wszystkie 6 raportów, optymalna próba, ~1.5 min)
python tools/sim/run_standard_audit.py

# 2. Głęboki pełny audyt walidacyjny / Release Gate (Maksymalna próba, zero szumu, ~4 min)
python tools/sim/run_deep_audit.py
```
