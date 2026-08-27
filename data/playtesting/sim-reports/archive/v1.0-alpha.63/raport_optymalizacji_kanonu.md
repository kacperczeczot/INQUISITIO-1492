[Strona główna](../../../../../README.md) > [v1.0-alpha.63](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.63 (Iteracja #2, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.62` (4P: `67.9 pkt`) → **Nowa Wersja:** `v1.0-alpha.63` (4P: `71.4 pkt`)
**Data:** 2026-08-24 07:01 | **Czas Trwania Iteracji:** 444.3s | **Zysk 4P:** `+3.5 pkt` | **Zysk Global:** `+0.7 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_CAA-05_TARGET_HERESY_SET2` — **CAA-05 (Ukryty Kurier): dodaj target_heresy = 2**
- **Opis Modyfikacji:** Karta `caa-05` (Ukryty Kurier): `target_heresy` → `2`
- **Wynik Kanonu 4P Balance:** 67.9 → 🟠 ** 71.4** (`⬆️ +3.5`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 65.1 → 77.1 (`⬆️ +12.0`) pkt
  - `4p-no-cienie`: 55.1 pkt
  - `4p-no-kabala`: 73.2 → 77.3 (`⬆️ +4.1`) pkt
  - `4p-no-korona`: 84.7 → 86.4 (`⬆️ +1.7`) pkt
  - `4p-no-oficjum`: 61.6 → 60.9 (`-0.7`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 27.9 → 30.0 (`⬆️ +2.1`) pkt
- **Tryb 4-osobowy (4p Avg):** 61.3 → 61.6 (`⬆️ +0.3`) pkt
- **Tryb 5-osobowy (5p Avg):** 2.6 → 2.4 (`-0.2`) pkt
- **Global Game Balance Score:** 30.6 → 🔴 ** 31.3** (`⬆️ +0.7`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.81 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `5.3%` (norma: <30%)
  - **Autodafé / partię:** `1.41`
  - **Oskarżenia / partię:** `6.95`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_CAA-05_TARGET_HERESY_SET2` | CAA-05 (Ukryty Kurier): dodaj target_heresy = 2 | 67.9 → 🟠 ** 71.4** (`⬆️ +3.5`) | 0.0% | 5.3% | 🌟 ZWYCIĘZCA |
| #2 | `L3_CAA-11_TARGET_HERESY_PLUS1` | CAA-11 (Nocna Zmiana Warty): target_heresy 0 → 1 | 67.9 → 🟠 ** 70.7** (`⬆️ +2.8`) | 0.0% | 5.2% | 🟢 ZYSK |
| #3 | `L3_CAA-12_TARGET_HERESY_SET2` | CAA-12 (Skrytka w Murach): dodaj target_heresy = 2 | 67.9 → 🟠 ** 69.2** (`⬆️ +1.3`) | 0.0% | 5.3% | 🟢 ZYSK |
| #4 | `L3_KB-11_HERESY_PLUS1` | KB-11 (Tajny Emisariusz): heresy 0 → 1 | 67.9 → 🟠 ** 68.0** (`⬆️ +0.1`) | 0.0% | 5.2% | 🟢 ZYSK |
| #5 | `L3_KB-11_HERESY_SET1` | KB-11 (Tajny Emisariusz): dodaj heresy = 1 | 67.9 → 🟠 ** 68.0** (`⬆️ +0.1`) | 0.0% | 5.2% | 🟢 ZYSK |
| #6 | `L4_INQUISITOR_SPEED2` | Inkwizytor Patrol: ruch 1 → 2 (podwojenie) | 67.9 → 🟠 ** 67.3** (`-0.6`) | 0.0% | 5.3% | ⚪ STRATA/NEUTRALNY |
| #7 | `L3_KT-01_COST_MINUS1` | KT-01 (Rytuał Przejścia): cost 1 → 0 | 67.9 → 🟠 ** 67.0** (`-0.9`) | 0.0% | 5.2% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_CAA-01_TARGET_HERESY_PLUS1` | CAA-01 (Przejście Podziemiami): target_heresy 1 → 2 | 67.9 → 🟠 ** 70.5** (`⬆️ +2.6`) | 0.0% | 5.3% | 🟢 ZYSK |
| #9 | `L3_CAA-10_GOLD_SET2` | CAA-10 (Echo Alhambry): dodaj gold = 2 | 67.9 → 🟠 ** 69.8** (`⬆️ +1.9`) | 0.0% | 5.2% | 🟢 ZYSK |
| #10 | `L3_CAA-01_TARGET_HERESY_MINUS1` | CAA-01 (Przejście Podziemiami): target_heresy 1 → 0 | 67.9 → 🟠 ** 68.9** (`⬆️ +1.0`) | 0.0% | 5.3% | 🟢 ZYSK |
| #11 | `L3_CAA-01_GOLD_SET3` | CAA-01 (Przejście Podziemiami): dodaj gold = 3 | 67.9 → 🟠 ** 67.8** (`-0.1`) | 0.0% | 5.3% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_CAA-01_GOLD_SET2` | CAA-01 (Przejście Podziemiami): dodaj gold = 2 | 67.9 → 🟠 ** 68.4** (`⬆️ +0.5`) | 0.0% | 5.3% | 🟢 ZYSK |
| #13 | `L3_CAA-11_COST_MINUS1` | CAA-11 (Nocna Zmiana Warty): cost 1 → 0 | 67.9 → 🟠 ** 70.0** (`⬆️ +2.1`) | 0.0% | 5.3% | 🟢 ZYSK |
| #14 | `L3_CAA-11_GOLD_PLUS1` | CAA-11 (Nocna Zmiana Warty): gold 3 → 4 | 67.9 → 🟠 ** 69.7** (`⬆️ +1.8`) | 0.0% | 5.3% | 🟢 ZYSK |
| #15 | `L3_CAA-01_GOLD_PLUS1` | CAA-01 (Przejście Podziemiami): gold 0 → 1 | 67.9 → 🟠 ** 68.5** (`⬆️ +0.6`) | 0.0% | 5.3% | 🟢 ZYSK |
| #16 | `L3_CAA-01_GOLD_SET1` | CAA-01 (Przejście Podziemiami): dodaj gold = 1 | 67.9 → 🟠 ** 68.5** (`⬆️ +0.6`) | 0.0% | 5.3% | 🟢 ZYSK |
| #17 | `L3_CAA-01_TARGET_HERESY_PLUS2` | CAA-01 (Przejście Podziemiami): target_heresy 1 → 3 (+2) | 67.9 → 🟠 ** 70.5** (`⬆️ +2.6`) | 0.0% | 5.3% | 🟢 ZYSK |
| #18 | `L3_SO-03_TARGET_HERESY_MINUS1` | SO-03 (Podejrzenie): target_heresy 3 → 2 | 67.9 → 🟠 ** 72.1** (`⬆️ +4.2`) | 0.0% | 5.3% | 🟢 ZYSK |
| #19 | `L3_CAA-11_TARGET_HERESY_SET2` | CAA-11 (Nocna Zmiana Warty): dodaj target_heresy = 2 | 67.9 → 🟠 ** 72.3** (`⬆️ +4.4`) | 0.0% | 5.3% | 🟢 ZYSK |
| #20 | `L3_CAA-10_TARGET_HERESY_PLUS1` | CAA-10 (Echo Alhambry): target_heresy 0 → 1 | 67.9 → 🟠 ** 67.2** (`-0.7`) | 0.0% | 5.2% | ⚪ STRATA/NEUTRALNY |