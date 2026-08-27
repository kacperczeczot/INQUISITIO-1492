---
name: Reguły Projektu INQUISITIO-1492
description: Zasady domenowe i operacyjne symulatora gry planszowej INQUISITIO 1492.
---

# Reguły Projektu — INQUISITIO 1492: Cienie Toledo

Niniejszy plik jest punktem wejścia dla wszystkich asystentów AI pracujących w tym repozytorium.
Szczegółowe reguły operacyjne są podzielone na wyspecjalizowane pliki w tym katalogu:

---

## Pliki Reguł

| Plik | Zakres |
| :--- | :--- |
| [`dyscyplina_agenta_i_zero_samowolki.md`](dyscyplina_agenta_i_zero_samowolki.md) | Zakaz samowolki, wymóg zgody użytkownika, weryfikacja matematyczna, zgodność z ADR |
| [`edycja_konfiguracji.md`](edycja_konfiguracji.md) | Procedura edycji `data/game_config.yaml` (podbicie wersji, patch notes, synchronizacja) |
| [`balansowanie.md`](balansowanie.md) | Zasady balansowania mechaniki, zgodność z Konstytucją ADR, zakaz engine hacks |
| [`balance-flattening.md`](balance-flattening.md) | Procedura wyrównywania win-rate między frakcjami |

---

## Mapa Repozytorium

| Katalog | Rola |
| :--- | :--- |
| [`src/`](../../src/) | Kod symulatora Python (silnik, agenci, runner) i C++ (moduł natywny) |
| [`src/native/`](../../src/native/) | Natywny moduł C++ (`inquisitio_native.cpp`) kompilowany przez `build.sh` |
| [`scripts/`](../../scripts/) | Narzędzia: audytory Monte Carlo, generator PnP, sync_config |
| [`data/game_config.yaml`](../../data/game_config.yaml) | **SSOT** — jedyne źródło prawdy dla parametrów gry |
| [`data/playtesting/`](../../data/playtesting/) | Raporty i archiwa z sesji playtestingowych |
| [`docs/adr/`](../../docs/adr/) | Rejestr Decyzji Architektonicznych (ADR-0001 do ADR-0016+) |
| [`docs/game/`](../../docs/game/) | Dokumentacja projektowa gry: karty, mechaniki, frakcje, lore |
| [`assets/`](../../assets/) | Prototypy kart (card-editor.html), grafiki |

---

## Kluczowe Zasady Operacyjne

> **Zero Samowolki:** Modyfikacje `data/game_config.yaml` i kodu silnika wyłącznie na wyraźne polecenie użytkownika.

> **SSOT:** Wszystkie parametry gry żyją wyłącznie w `data/game_config.yaml`. Silnik i dokumentacja są synchronizowane przez `scripts/sync_config.py`.

> **Zgodność z ADR:** Każda propozycja musi być spójna z aktywnymi rekordami w `docs/adr/`.
