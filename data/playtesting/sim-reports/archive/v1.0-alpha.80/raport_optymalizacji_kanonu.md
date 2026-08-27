[Strona główna](../../../../../README.md) > [v1.0-alpha.80](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.80 (Iteracja #1, Faza 2D)

**Wersja Poprzednia:** `v1.0-alpha.79` (4P: `84.5 pkt`) → **Nowa Wersja:** `v1.0-alpha.80` (4P: `85.1 pkt`)
**Data:** 2026-08-24 21:28 | **Czas Trwania Iteracji:** 712.5s | **Zysk 4P:** `⬆️ +0.6 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (2D Synergia):** `L3_SO-02_HERESY_SET2__L3_CAA-08_COST_PLUS1`
- **Opis Modyfikacji:** Karta `so-02` (Skarbiec Trybunału): `heresy` → `2` + Karta `caa-08` (Kaptur Nocy): `cost` → `3`
- **Wynik Kanonu 4P Balance:** 84.5 → 🟡 ** 85.1** (`⬆️ +0.6`) pkt
- **Rozbicie Setupów Kanonu 4P (Próba 10 000 partii / setup — SSOT):**
  - `4p-core`: 90.9 → 93.2 (`⬆️ +2.3`) pkt
  - `4p-no-oficjum`: 73.6 → 76.9 (`⬆️ +3.3`) pkt
  - `4p-no-korona`: 83.2 → 84.9 (`⬆️ +1.7`) pkt
  - `4p-no-kabala`: 87.2 → 87.0 (`🔻 -0.2`) pkt
  - `4p-no-cienie`: 74.6 → 73.6 (`🔻 -1.0`) pkt

## 2. Kluczowa Telemetria Silnika (Kanon 4P — 50 000 Partii)
- **Średnia Długość Gry:** `5.77 Er` (norma: 5.0–6.5)
- **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
- **Pas Biedy (Złoto):** `4.4%` (norma: <28%)
- **Autodafé / partię:** `1.54` (norma: 0.7–1.8)
- **Oskarżenia / partię:** `7.80` (norma: 3.5–8.5)
- **Witalność mechanik:** 🟢 **Pełna Witalność** (0 kar we wszystkich setupach 4P)
