# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.80 (SSOT Baseline)

**Wersja Bazowa SSOT:** `v1.0-alpha.80` (Kanon 4P: `75.7 pkt`)
**Data:** 2026-08-29 01:20 | **Silnik:** Natywny C++20 (`inquisitio_native`) | **Próba:** 10 000 partii / setup (50 000 partii łącznie)

## 1. Wynik Balansu Kanonu 4P (Czysty Baseline SSOT)
- **Wynik Kanonu 4P Balance:** 🟠 **75.7 pkt** (średnia z 5 setupów)
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 🟠 **71.6 pkt** (SO 31.1%, CAA 19.7%, KB 25.3%, KT 23.8%)
  - `4p-no-cienie`: 🔴 **63.6 pkt** (SO 30.1%, KB 17.2%, KT 29.4%, GC 23.3%)
  - `4p-no-kabala`: 🟢 **93.5 pkt** (SO 26.3%, CAA 24.5%, KB 23.4%, GC 25.9%)
  - `4p-no-korona`: 🟠 **68.3 pkt** (SO 32.8%, CAA 22.8%, KT 23.3%, GC 21.1%)
  - `4p-no-oficjum`: 🟡 **81.6 pkt** (CAA 27.1%, KB 22.5%, KT 22.0%, GC 28.3%)

## 2. Kluczowa Telemetria Silnika (Kanon 4P)
- **Średnia Długość Gry:** `5.79 Er` (norma: 5.0–6.5)
- **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
- **Pas Biedy (Złoto):** `4.6%` (norma: <28%)
- **Autodafé / partię:** `1.50` (norma: 0.7–1.8)
- **Oskarżenia / partię:** `7.80` (norma: 3.5–8.5)
- **Witalność mechanik:** 🟢 **Pełna Witalność** (0 kar we wszystkich setupach 4P)
