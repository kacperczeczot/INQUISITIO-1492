[Strona główna](../../../../../README.md) > [v0.71](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.71 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v0.70` (4P: `69.9 pkt`) → **Nowa Wersja:** `v0.71` (4P: `88.4 pkt`)
**Data:** 2026-08-16 22:57 | **Czas Trwania Iteracji:** 627.4s | **Zysk 4P:** `+18.5 pkt` | **Zysk Global:** `+8.2 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L2_SO_CONDEMNS_PLUS1` — **Oficjum Skazania: 2 → 3**
- **Opis Modyfikacji:** Święte Oficjum: Skazania offset +1
- **Wynik Kanonu 4P Score:** 69.9 → 🟡 ** 88.4** (`⬆️ +18.5`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 58.7 → 89.1 (`⬆️ +30.4`) pkt
  - `4p-no-cienie`: 63.4 → 87.6 (`⬆️ +24.2`) pkt
  - `4p-no-kabala`: 68.9 → 87.6 (`⬆️ +18.7`) pkt
  - `4p-no-korona`: 64.6 → 83.8 (`⬆️ +19.2`) pkt
  - `4p-no-oficjum`: 93.8 pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 72.8 → 68.0 (`-4.8`) pkt
- **Tryb 4-osobowy (4p Avg):** 67.1 → 85.7 (`⬆️ +18.6`) pkt
- **Tryb 5-osobowy (5p Avg):** 43.2 → 53.9 (`⬆️ +10.7`) pkt
- **Global Game Balance Score:** 61.0 → 🟠 ** 69.2** (`⬆️ +8.2`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.40 Er`
  - **Deadlocki (Limit Er):** `0.1%` (norma: <5%)
  - **Pas Biedy (Złoto):** `23.9%` (norma: <30%)
  - **Autodafé / partię:** `1.49`
  - **Oskarżenia / partię:** `3.28`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2 → 3 | 69.9 → 🟡 ** 88.4** (`⬆️ +18.5`) | 0.1% | 23.9% | 🌟 ZWYCIĘZCA |
| #2 | `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 5 → 6 | 69.9 → 🟡 ** 86.9** (`⬆️ +17.0`) | 0.1% | 23.6% | 🟢 ZYSK |
| #3 | `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 6/7/8 → 7/8/9 | 69.9 → 🟡 ** 86.0** (`⬆️ +16.1`) | 0.0% | 23.6% | 🟢 ZYSK |
| #4 | `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 69.9 → 🟡 ** 84.3** (`⬆️ +14.4`) | 0.0% | 23.5% | 🟢 ZYSK |
| #5 | `L4_INQUISITOR_SPEED0` | Inkwizytor Patrol: ruch 1 → 0 | 69.9 → 🟡 ** 81.6** (`⬆️ +11.7`) | 0.1% | 23.1% | 🟢 ZYSK |
| #6 | `L3_SO-05_TARGET_HERESY_MINUS1` | SO-05 (Wezwanie do Trybunału): target_heresy 2 → 1 | 69.9 → 🟡 ** 81.4** (`⬆️ +11.5`) | 0.1% | 23.5% | 🟢 ZYSK |
| #7 | `L3_KT-09_HERESY_MINUS1` | KT-09 (Fragment Kodeksu): heresy 1 → 0 | 69.9 → 🟡 ** 80.0** (`⬆️ +10.1`) | 0.0% | 23.3% | 🟢 ZYSK |
| #8 | `L3_KT-03_HERESY_MINUS1` | KT-03 (Zakazana Wiedza): heresy 1 → 0 | 69.9 → 🟡 ** 79.2** (`⬆️ +9.3`) | 0.0% | 23.3% | 🟢 ZYSK |
| #9 | `L3_SO-08_TARGET_HERESY_MINUS1` | SO-08 (Nasłanie Inkwizytora): target_heresy 1 → 0 | 69.9 → 🟡 ** 79.0** (`⬆️ +9.1`) | 0.1% | 23.6% | 🟢 ZYSK |
| #10 | `L3_CAA-04_TARGET_HERESY_MINUS1` | CAA-04 (Fałszywy Trop): target_heresy 1 → 0 | 69.9 → 🟡 ** 78.6** (`⬆️ +8.7`) | 0.1% | 23.4% | 🟢 ZYSK |
| #11 | `L3_CAA-10_HERESY_MINUS1` | CAA-10 (Echo Alhambry): heresy 1 → 0 | 69.9 → 🟡 ** 77.9** (`⬆️ +8.0`) | 0.1% | 23.6% | 🟢 ZYSK |
| #12 | `L3_KB-03_TARGET_HERESY_MINUS1` | KB-03 (Plotka Dworska): target_heresy 1 → 0 | 69.9 → 🟡 ** 77.9** (`⬆️ +8.0`) | 0.0% | 23.3% | 🟢 ZYSK |
| #13 | `L3_KT-04_TARGET_HERESY_MINUS1` | KT-04 (Zwierciadło Herezji): target_heresy 1 → 0 | 69.9 → 🟡 ** 77.7** (`⬆️ +7.8`) | 0.0% | 23.5% | 🟢 ZYSK |
| #14 | `L3_CAA-08_HERESY_MINUS1` | CAA-08 (Kaptur Nocy): heresy 1 → 0 | 69.9 → 🟡 ** 76.2** (`⬆️ +6.3`) | 0.1% | 23.5% | 🟢 ZYSK |
| #15 | `L3_CAA-03_HERESY_MINUS1` | CAA-03 (Cień na Rynku): heresy 1 → 0 | 69.9 → 🟡 ** 76.1** (`⬆️ +6.2`) | 0.1% | 23.5% | 🟢 ZYSK |
| #16 | `L3_SO-03_TARGET_HERESY_MINUS1` | SO-03 (Podejrzenie): target_heresy 1 → 0 | 69.9 → 🟡 ** 76.1** (`⬆️ +6.2`) | 0.1% | 23.4% | 🟢 ZYSK |
| #17 | `L3_CAA-06_HERESY_MINUS1` | CAA-06 (Ucieczka z Lochów): heresy 1 → 0 | 69.9 → 🟡 ** 76.0** (`⬆️ +6.1`) | 0.1% | 23.4% | 🟢 ZYSK |
| #18 | `L3_GC-08_TARGET_HERESY_MINUS1` | GC-08 (Zatrute Złoto): target_heresy 1 → 0 | 69.9 → 🟠 ** 74.9** (`⬆️ +5.0`) | 0.1% | 23.5% | 🟢 ZYSK |
| #19 | `L3_SO-05_COST_PLUS1` | SO-05 (Wezwanie do Trybunału): cost 0 → 1 | 69.9 → 🟠 ** 73.6** (`⬆️ +3.7`) | 0.0% | 23.9% | 🟢 ZYSK |
| #20 | `L3_KT-06_COST_PLUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 3 | 69.9 → 🟠 ** 72.8** (`⬆️ +2.9`) | 0.0% | 22.8% | 🟢 ZYSK |
| #21 | `L3_SO-06_GOLD_PLUS1` | SO-06 (Areszt Trybunalski): gold 0 → 1 | 69.9 → 🟠 ** 72.6** (`⬆️ +2.7`) | 0.1% | 22.9% | 🟢 ZYSK |
| #22 | `L3_SO-02_COST_PLUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 2 | 69.9 → 🟠 ** 72.4** (`⬆️ +2.5`) | 0.0% | 24.4% | 🟢 ZYSK |
| #23 | `L3_SO-08_COST_PLUS1` | SO-08 (Nasłanie Inkwizytora): cost 1 → 2 | 69.9 → 🟠 ** 72.0** (`⬆️ +2.1`) | 0.0% | 24.1% | 🟢 ZYSK |
| #24 | `L3_SO-02_COST_MINUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 0 | 69.9 → 🟠 ** 71.2** (`⬆️ +1.3`) | 0.1% | 22.8% | 🟢 ZYSK |