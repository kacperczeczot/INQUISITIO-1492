[Strona główna](../../README.md) > [Playtesting](../README.md) > [Raporty Symulacji](README.md)

---

# 📊 Raporty Symulacji i Audytów Balansu

Katalog zawiera automatycznie generowane raporty symulacyjne silnika `INQUISITIO-1492`.

## 📁 Struktura Katalogu

- **Bieżące Raporty (Wersja Aktywna):**
  - [`raport_telemetrii.md`](raport_telemetrii.md) — pełny rozkład szans wygranych (Win Shares) dla 16 setupów i 5 filarów telemetrii
  - [`audyt_level1_raport.md`](audyt_level1_raport.md) — audyt ±1 parametrów systemowych (złoto, agenci, progi, cooldowny)
  - [`audyt_level2_raport.md`](audyt_level2_raport.md) — audyt ±1 warunków zwycięstwa frakcji i reguł skalowania
  - [`audyt_level3_raport.md`](audyt_level3_raport.md) — precyzyjny audyt ±1 parametrów pojedynczych kart
  - [`audyt_level4_raport.md`](audyt_level4_raport.md) — audyt wariantów niszowych i modyfikatorów
  - [`audyt_stress_raport.md`](audyt_stress_raport.md) — testy stresu ekonomicznego (Poverty Stress Test)
- **Katalog `archive/` (Archiwum Historyczne):**
  - `archive/v1.12/`, `archive/v1.13/`, ... — migawki raportów per wersja balansu (zapisywane automatycznie przy każdym generowaniu)
  - `archive/legacy_iterations_01_28/` — historyczne raporty z wczesnych faz rozwoju (iteracje 1–28)
- **Katalog `game_replays/`:**
  - Przykładowe zapisy partii krok-po-kroku (seed 42).

## 🛠️ Generowanie i Archiwizacja

Uruchomienie generatorów raportów automatycznie stempluje numer wersji balansu z `game_config.yaml` oraz zapisuje kopię w `archive/{wersja}/`:

```bash
# 1. Standardowy pełny audyt balansu (Wszystkie 6 raportów, optymalna próba, ~1.5 min)
python tools/sim/run_standard_audit.py

# 2. Głęboki pełny audyt walidacyjny / Release Gate (Maksymalna próba, zero szumu, ~4 min)
python tools/sim/run_deep_audit.py
```
