[Strona główna](../../../../../README.md) > [v1.0-alpha.48](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.48 (Iteracja #2, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.47` (4P: `61.1 pkt`) → **Nowa Wersja:** `v1.0-alpha.48` (4P: `72.0 pkt`)
**Data:** 2026-08-23 12:32 | **Czas Trwania Iteracji:** 567.6s | **Zysk 4P:** `+10.9 pkt` | **Zysk Global:** `+1.6 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_CAA-06_TARGET_HERESY_SET2` — **CAA-06 (Ucieczka z Lochów): dodaj target_heresy = 2**
- **Opis Modyfikacji:** Karta `caa-06` (Ucieczka z Lochów): `target_heresy` → `2`
- **Wynik Kanonu 4P Balance:** 61.1 → 🟠 ** 72.0** (`⬆️ +10.9`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 48.0 → 59.5 (`⬆️ +11.5`) pkt
  - `4p-no-cienie`: 89.9 pkt
  - `4p-no-kabala`: 51.9 → 68.7 (`⬆️ +16.8`) pkt
  - `4p-no-korona`: 61.3 → 77.6 (`⬆️ +16.3`) pkt
  - `4p-no-oficjum`: 54.3 → 64.1 (`⬆️ +9.8`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 14.9 → 16.2 (`⬆️ +1.3`) pkt
- **Tryb 4-osobowy (4p Avg):** 43.3 → 46.5 (`⬆️ +3.2`) pkt
- **Tryb 5-osobowy (5p Avg):** 4.4 → 4.9 (`⬆️ +0.5`) pkt
- **Global Game Balance Score:** 20.9 → 🔴 ** 22.5** (`⬆️ +1.6`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.40 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `3.9%` (norma: <30%)
  - **Autodafé / partię:** `1.84`
  - **Oskarżenia / partię:** `5.62`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_CAA-06_TARGET_HERESY_SET2` | CAA-06 (Ucieczka z Lochów): dodaj target_heresy = 2 | 61.1 → 🟠 ** 72.0** (`⬆️ +10.9`) | 0.0% | 3.9% | 🌟 ZWYCIĘZCA |
| #2 | `L3_GC-08_GOLD_PLUS1` | GC-08 (Zatrute Złoto): gold 1 → 2 | 61.1 → 🟠 ** 61.8** (`⬆️ +0.7`) | 0.0% | 4.0% | 🟢 ZYSK |
| #3 | `L3_SO-03_TARGET_HERESY_MINUS1` | SO-03 (Podejrzenie): target_heresy 3 → 2 | 61.1 → 🟠 ** 65.5** (`⬆️ +4.4`) | 0.0% | 4.0% | 🟢 ZYSK |
| #4 | `L3_SO-02_GOLD_MINUS1` | SO-02 (Skarbiec Trybunału): gold 3 → 2 | 61.1 → 🟠 ** 63.4** (`⬆️ +2.3`) | 0.0% | 4.3% | 🟢 ZYSK |
| #5 | `L3_SO-06_TARGET_HERESY_MINUS1` | SO-06 (Areszt Trybunalski): target_heresy 1 → 0 | 61.1 → 🟠 ** 62.7** (`⬆️ +1.6`) | 0.0% | 3.8% | 🟢 ZYSK |
| #6 | `L3_CAA-06_TARGET_HERESY_SET1` | CAA-06 (Ucieczka z Lochów): dodaj target_heresy = 1 | 61.1 → 🟠 ** 69.9** (`⬆️ +8.8`) | 0.0% | 4.0% | 🟢 ZYSK |
| #7 | `L3_CAA-06_TARGET_HERESY_PLUS1` | CAA-06 (Ucieczka z Lochów): target_heresy 0 → 1 | 61.1 → 🟠 ** 69.9** (`⬆️ +8.8`) | 0.0% | 4.0% | 🟢 ZYSK |
| #8 | `L3_KB-10_TARGET_HERESY_SET2` | KB-10 (Pieczęć Korony): dodaj target_heresy = 2 | 61.1 → 🟠 ** 62.7** (`⬆️ +1.6`) | 0.0% | 3.9% | 🟢 ZYSK |
| #9 | `L3_CAA-06_GOLD_PLUS1` | CAA-06 (Ucieczka z Lochów): gold 0 → 1 | 61.1 → 🟠 ** 67.7** (`⬆️ +6.6`) | 0.0% | 4.0% | 🟢 ZYSK |
| #10 | `L3_CAA-06_GOLD_SET1` | CAA-06 (Ucieczka z Lochów): dodaj gold = 1 | 61.1 → 🟠 ** 67.7** (`⬆️ +6.6`) | 0.0% | 4.0% | 🟢 ZYSK |
| #11 | `L3_KB-07_HERESY_PLUS1` | KB-07 (Szantaż Pieczęcią): heresy 0 → 1 | 61.1 → 🟠 ** 62.8** (`⬆️ +1.7`) | 0.0% | 3.9% | 🟢 ZYSK |
| #12 | `L3_KB-07_HERESY_SET1` | KB-07 (Szantaż Pieczęcią): dodaj heresy = 1 | 61.1 → 🟠 ** 62.8** (`⬆️ +1.7`) | 0.0% | 3.9% | 🟢 ZYSK |
| #13 | `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 61.1 → 🟠 ** 62.4** (`⬆️ +1.3`) | 0.0% | 4.0% | 🟢 ZYSK |
| #14 | `L3_CAA-05_TARGET_HERESY_SET2` | CAA-05 (Ukryty Kurier): dodaj target_heresy = 2 | 61.1 → 🟠 ** 71.7** (`⬆️ +10.6`) | 0.0% | 3.9% | 🟢 ZYSK |
| #15 | `L3_CAA-06_GOLD_SET2` | CAA-06 (Ucieczka z Lochów): dodaj gold = 2 | 61.1 → 🟠 ** 70.2** (`⬆️ +9.1`) | 0.0% | 4.0% | 🟢 ZYSK |
| #16 | `L3_CAA-10_TARGET_HERESY_SET2` | CAA-10 (Echo Alhambry): dodaj target_heresy = 2 | 61.1 → 🟠 ** 65.7** (`⬆️ +4.6`) | 0.0% | 4.0% | 🟢 ZYSK |
| #17 | `L3_KB-07_HERESY_SET2` | KB-07 (Szantaż Pieczęcią): dodaj heresy = 2 | 61.1 → 🟠 ** 63.4** (`⬆️ +2.3`) | 0.0% | 3.9% | 🟢 ZYSK |
| #18 | `L3_KB-08_HERESY_SET2` | KB-08 (Przekupstwo Sędziego): dodaj heresy = 2 | 61.1 → 🟠 ** 63.6** (`⬆️ +2.5`) | 0.0% | 3.9% | 🟢 ZYSK |
| #19 | `L3_KB-04_HERESY_SET2` | KB-04 (Faworyt Dworu): dodaj heresy = 2 | 61.1 → 🟠 ** 63.1** (`⬆️ +2.0`) | 0.0% | 4.1% | 🟢 ZYSK |
| #20 | `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5 → 6 | 61.1 → 🟠 ** 60.6** (`-0.5`) | 0.0% | 3.6% | ⚪ STRATA/NEUTRALNY |