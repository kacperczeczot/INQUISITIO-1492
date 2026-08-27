[Strona główna](../../../../../README.md) > [v1.0-alpha.71](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.71 (Iteracja #5, Faza 2D)

**Wersja Poprzednia:** `v1.0-alpha.70` (4P: `74.5 pkt`) → **Nowa Wersja:** `v1.0-alpha.71` (4P: `77.1 pkt`)
**Data:** 2026-08-24 08:25 | **Czas Trwania Iteracji:** 592.6s | **Zysk 4P:** `+2.6 pkt` | **Zysk Global:** `+0.2 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (2D):** `L3_SO-07_COST_MINUS1__L3_CAA-08_TARGET_HERESY_PLUS1` — **SO-07 (Przesłuchanie Oficjum): cost 2 → 1 + CAA-08 (Kaptur Nocy): target_heresy 1 → 2**
- **Opis Modyfikacji:** Karta `so-07` (Przesłuchanie Oficjum): `cost` → `1` + Karta `caa-08` (Kaptur Nocy): `target_heresy` → `2`
- **Wynik Kanonu 4P Balance:** 74.5 → 🟡 ** 77.1** (`⬆️ +2.6`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 86.3 → 84.4 (`-1.9`) pkt
  - `4p-no-cienie`: 64.4 → 69.9 (`⬆️ +5.5`) pkt
  - `4p-no-kabala`: 86.5 → 84.7 (`-1.8`) pkt
  - `4p-no-korona`: 76.1 → 85.2 (`⬆️ +9.1`) pkt
  - `4p-no-oficjum`: 59.3 → 61.4 (`⬆️ +2.1`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 32.1 → 32.0 (`-0.1`) pkt
- **Tryb 4-osobowy (4p Avg):** 70.9 → 70.2 (`-0.7`) pkt
- **Tryb 5-osobowy (5p Avg):** 20.6 → 22.1 (`⬆️ +1.5`) pkt
- **Global Game Balance Score:** 41.2 → 🔴 ** 41.4** (`⬆️ +0.2`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.82 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `4.3%` (norma: <30%)
  - **Autodafé / partię:** `1.52`
  - **Oskarżenia / partię:** `6.77`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_SO-07_COST_MINUS1__L3_CAA-08_TARGET_HERESY_PLUS1` | SO-07 (Przesłuchanie Oficjum): cost 2 → 1 + CAA-08 (Kaptur Nocy): target_heresy 1 → 2 | 74.5 → 🟡 ** 77.1** (`⬆️ +2.6`) | 0.0% | 4.3% | 🌟 ZWYCIĘZCA |
| #2 | `L3_SO-07_COST_MINUS1__L3_CAA-08_COST_MINUS1` | SO-07 (Przesłuchanie Oficjum): cost 2 → 1 + CAA-08 (Kaptur Nocy): cost 1 → 0 | 74.5 → 🟡 ** 76.9** (`⬆️ +2.4`) | 0.0% | 4.3% | 🟢 ZYSK |
| #3 | `L3_SO-07_COST_MINUS1__L3_CAA-08_GOLD_PLUS1` | SO-07 (Przesłuchanie Oficjum): cost 2 → 1 + CAA-08 (Kaptur Nocy): gold 3 → 4 | 74.5 → 🟡 ** 76.8** (`⬆️ +2.3`) | 0.0% | 4.3% | 🟢 ZYSK |
| #4 | `L3_SO-06_TARGET_HERESY_PLUS1__L3_CAA-03_TARGET_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): target_heresy 1 → 2 + CAA-03 (Cień na Rynku): target_heresy 0 → 1 | 74.5 → 🟡 ** 76.5** (`⬆️ +2.0`) | 0.0% | 4.2% | 🟢 ZYSK |
| #5 | `L3_SO-06_TARGET_HERESY_PLUS1__L3_CAA-03_TARGET_HERESY_SET1` | SO-06 (Areszt Trybunalski): target_heresy 1 → 2 + CAA-03 (Cień na Rynku): dodaj target_heresy = 1 | 74.5 → 🟡 ** 76.5** (`⬆️ +2.0`) | 0.0% | 4.2% | 🟢 ZYSK |
| #6 | `L3_SO-06_TARGET_HERESY_PLUS1__L3_CAA-03_TARGET_HERESY_SET2` | SO-06 (Areszt Trybunalski): target_heresy 1 → 2 + CAA-03 (Cień na Rynku): dodaj target_heresy = 2 | 74.5 → 🟡 ** 76.0** (`⬆️ +1.5`) | 0.0% | 4.2% | 🟢 ZYSK |
| #7 | `L3_SO-06_TARGET_HERESY_PLUS1__L3_CAA-03_GOLD_MINUS1` | SO-06 (Areszt Trybunalski): target_heresy 1 → 2 + CAA-03 (Cień na Rynku): gold 2 → 1 | 74.5 → 🟡 ** 75.3** (`⬆️ +0.8`) | 0.0% | 4.2% | 🟢 ZYSK |
| #8 | `L3_SO-06_TARGET_HERESY_PLUS1__L3_CAA-05_TARGET_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): target_heresy 1 → 2 + CAA-05 (Ukryty Kurier): target_heresy 2 → 3 | 74.5 → 🟡 ** 76.7** (`⬆️ +2.2`) | 0.0% | 4.2% | 🟢 ZYSK |
| #9 | `L1_AUTODAFE_COOLDOWN_PLUS1__L3_CAA-09_TARGET_HERESY_PLUS1` | Cooldown Autodafé: 4 → 5 Ery + CAA-09 (Kurier Relikwii): target_heresy 0 → 1 | 74.5 → 🟡 ** 77.4** (`⬆️ +2.9`) | 0.0% | 4.1% | 🟢 ZYSK |
| #10 | `L1_AUTODAFE_COOLDOWN_PLUS1__L3_CAA-09_TARGET_HERESY_SET1` | Cooldown Autodafé: 4 → 5 Ery + CAA-09 (Kurier Relikwii): dodaj target_heresy = 1 | 74.5 → 🟡 ** 77.4** (`⬆️ +2.9`) | 0.0% | 4.1% | 🟢 ZYSK |
| #11 | `L1_AUTODAFE_COOLDOWN_PLUS1__L3_CAA-11_COST_PLUS1` | Cooldown Autodafé: 4 → 5 Ery + CAA-11 (Nocna Zmiana Warty): cost 1 → 2 | 74.5 → 🟠 ** 73.4** (`-1.1`) | 0.0% | 4.2% | ⚪ STRATA/NEUTRALNY |
| #12 | `L1_AUTODAFE_COOLDOWN_PLUS1__L3_CAA-08_GOLD_PLUS1` | Cooldown Autodafé: 4 → 5 Ery + CAA-08 (Kaptur Nocy): gold 3 → 4 | 74.5 → 🟡 ** 78.0** (`⬆️ +3.5`) | 0.0% | 4.2% | 🟢 ZYSK |
| #13 | `L1_AUTODAFE_COOLDOWN_PLUS1__L3_CAA-08_COST_MINUS1` | Cooldown Autodafé: 4 → 5 Ery + CAA-08 (Kaptur Nocy): cost 1 → 0 | 74.5 → 🟡 ** 77.9** (`⬆️ +3.4`) | 0.0% | 4.2% | 🟢 ZYSK |
| #14 | `L1_AUTODAFE_COOLDOWN_PLUS1__L3_CAA-03_TARGET_HERESY_PLUS1` | Cooldown Autodafé: 4 → 5 Ery + CAA-03 (Cień na Rynku): target_heresy 0 → 1 | 74.5 → 🟡 ** 76.9** (`⬆️ +2.4`) | 0.0% | 4.1% | 🟢 ZYSK |
| #15 | `L1_AUTODAFE_COOLDOWN_PLUS1__L3_CAA-03_TARGET_HERESY_SET1` | Cooldown Autodafé: 4 → 5 Ery + CAA-03 (Cień na Rynku): dodaj target_heresy = 1 | 74.5 → 🟡 ** 76.9** (`⬆️ +2.4`) | 0.0% | 4.1% | 🟢 ZYSK |
| #16 | `L1_AUTODAFE_COOLDOWN_PLUS1__L3_CAA-01_GOLD_SET3` | Cooldown Autodafé: 4 → 5 Ery + CAA-01 (Przejście Podziemiami): dodaj gold = 3 | 74.5 → 🟡 ** 76.2** (`⬆️ +1.7`) | 0.0% | 4.1% | 🟢 ZYSK |
| #17 | `L1_AUTODAFE_COOLDOWN_PLUS1__L3_CAA-01_GOLD_SET2` | Cooldown Autodafé: 4 → 5 Ery + CAA-01 (Przejście Podziemiami): dodaj gold = 2 | 74.5 → 🟡 ** 75.0** (`⬆️ +0.5`) | 0.0% | 4.1% | 🟢 ZYSK |
| #18 | `L1_AUTODAFE_COOLDOWN_PLUS1__L3_CAA-07_TARGET_HERESY_PLUS1` | Cooldown Autodafé: 4 → 5 Ery + CAA-07 (Szantaż Bractwa): target_heresy 0 → 1 | 74.5 → 🟡 ** 77.4** (`⬆️ +2.9`) | 0.0% | 4.2% | 🟢 ZYSK |
| #19 | `L1_AUTODAFE_COOLDOWN_PLUS1__L3_CAA-07_TARGET_HERESY_SET1` | Cooldown Autodafé: 4 → 5 Ery + CAA-07 (Szantaż Bractwa): dodaj target_heresy = 1 | 74.5 → 🟡 ** 77.4** (`⬆️ +2.9`) | 0.0% | 4.2% | 🟢 ZYSK |
| #20 | `L1_AUTODAFE_COOLDOWN_PLUS1__L3_CAA-03_HERESY_PLUS1` | Cooldown Autodafé: 4 → 5 Ery + CAA-03 (Cień na Rynku): heresy 1 → 2 | 74.5 → 🟠 ** 74.3** (`-0.2`) | 0.0% | 4.1% | ⚪ STRATA/NEUTRALNY |