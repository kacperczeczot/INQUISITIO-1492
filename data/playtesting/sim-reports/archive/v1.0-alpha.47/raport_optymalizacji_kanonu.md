# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.47 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.46` (4P: `51.6 pkt`) → **Nowa Wersja:** `v1.0-alpha.47` (4P: `59.7 pkt`)
**Data:** 2026-08-23 11:52 | **Czas Trwania Iteracji:** 518.2s | **Zysk 4P:** `+8.1 pkt` | **Zysk Global:** `+5.4 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L1_AGENTS_MINUS1` — **Agenci: 3 → 2**
- **Opis Modyfikacji:** Liczba agentów: offset -1 (nowa: 2)
- **Wynik Kanonu 4P Balance:** 51.6 → 🔴 ** 59.7** (`⬆️ +8.1`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 56.5 → 50.4 (`-6.1`) pkt
  - `4p-no-cienie`: 46.6 → 89.3 (`⬆️ +42.7`) pkt
  - `4p-no-kabala`: 64.0 → 48.1 (`-15.9`) pkt
  - `4p-no-korona`: 45.1 → 56.6 (`⬆️ +11.5`) pkt
  - `4p-no-oficjum`: 45.8 → 54.3 (`⬆️ +8.5`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 14.1 → 13.5 (`-0.6`) pkt
- **Tryb 4-osobowy (4p Avg):** 21.8 → 37.0 (`⬆️ +15.2`) pkt
- **Tryb 5-osobowy (5p Avg):** 3.9 → 5.7 (`⬆️ +1.8`) pkt
- **Global Game Balance Score:** 13.3 → 🔴 ** 18.7** (`⬆️ +5.4`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.43 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `4.0%` (norma: <30%)
  - **Autodafé / partię:** `1.84`
  - **Oskarżenia / partię:** `5.63`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 51.6 → 🔴 ** 59.7** (`⬆️ +8.1`) | 0.0% | 4.0% | 🌟 ZWYCIĘZCA |
| #2 | `L3_KT-01_TARGET_HERESY_SET2` | KT-01 (Rytuał Przejścia): dodaj target_heresy = 2 | 51.6 → 🔴 ** 52.7** (`⬆️ +1.1`) | 0.0% | 3.4% | 🟢 ZYSK |
| #3 | `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 51.6 → 🟠 ** 73.7** (`⬆️ +22.1`) | 0.0% | 3.6% | 🟢 ZYSK |
| #4 | `L3_SO-02_TARGET_HERESY_MINUS1` | SO-02 (Skarbiec Trybunału): target_heresy 1 → 0 | 51.6 → 🟠 ** 62.2** (`⬆️ +10.6`) | 0.0% | 3.6% | 🟢 ZYSK |
| #5 | `L3_SO-07_GOLD_SET3` | SO-07 (Przesłuchanie Oficjum): dodaj gold = 3 | 51.6 → 🟠 ** 61.0** (`⬆️ +9.4`) | 0.0% | 3.8% | 🟢 ZYSK |
| #6 | `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 6 → 7 | 51.6 → 🟠 ** 60.8** (`⬆️ +9.2`) | 0.0% | 3.5% | 🟢 ZYSK |
| #7 | `L3_SO-07_TARGET_HERESY_SET2` | SO-07 (Przesłuchanie Oficjum): dodaj target_heresy = 2 | 51.6 → 🟠 ** 60.2** (`⬆️ +8.6`) | 0.0% | 4.0% | 🟢 ZYSK |
| #8 | `L3_SO-07_GOLD_SET2` | SO-07 (Przesłuchanie Oficjum): dodaj gold = 2 | 51.6 → 🔴 ** 59.0** (`⬆️ +7.4`) | 0.0% | 3.7% | 🟢 ZYSK |
| #9 | `L3_SO-07_TARGET_HERESY_SET1` | SO-07 (Przesłuchanie Oficjum): dodaj target_heresy = 1 | 51.6 → 🟠 ** 60.0** (`⬆️ +8.4`) | 0.0% | 3.9% | 🟢 ZYSK |
| #10 | `L3_SO-07_TARGET_HERESY_PLUS1` | SO-07 (Przesłuchanie Oficjum): target_heresy 0 → 1 | 51.6 → 🟠 ** 60.0** (`⬆️ +8.4`) | 0.0% | 3.9% | 🟢 ZYSK |
| #11 | `L3_SO-03_TARGET_HERESY_MINUS1` | SO-03 (Podejrzenie): target_heresy 3 → 2 | 51.6 → 🟠 ** 61.1** (`⬆️ +9.5`) | 0.0% | 3.5% | 🟢 ZYSK |
| #12 | `L3_SO-02_HERESY_SET2` | SO-02 (Skarbiec Trybunału): dodaj heresy = 2 | 51.6 → 🟠 ** 67.1** (`⬆️ +15.5`) | 0.0% | 3.8% | 🟢 ZYSK |
| #13 | `L3_SO-05_TARGET_HERESY_MINUS1` | SO-05 (Wezwanie do Trybunału): target_heresy 1 → 0 | 51.6 → 🔴 ** 57.2** (`⬆️ +5.6`) | 0.0% | 3.4% | 🟢 ZYSK |
| #14 | `L3_SO-02_HERESY_SET1` | SO-02 (Skarbiec Trybunału): dodaj heresy = 1 | 51.6 → 🟠 ** 63.3** (`⬆️ +11.7`) | 0.0% | 3.7% | 🟢 ZYSK |
| #15 | `L3_SO-02_HERESY_PLUS1` | SO-02 (Skarbiec Trybunału): heresy 0 → 1 | 51.6 → 🟠 ** 63.3** (`⬆️ +11.7`) | 0.0% | 3.7% | 🟢 ZYSK |
| #16 | `L3_SO-03_HERESY_PLUS1` | SO-03 (Podejrzenie): heresy 2 → 3 | 51.6 → 🔴 ** 58.8** (`⬆️ +7.2`) | 0.0% | 3.5% | 🟢 ZYSK |
| #17 | `L3_KT-05_HERESY_MINUS1` | KT-05 (Wskazówka Cyklu): heresy 1 → 0 | 51.6 → 🟠 ** 60.1** (`⬆️ +8.5`) | 0.0% | 3.4% | 🟢 ZYSK |
| #18 | `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5 → 6 | 51.6 → 🟠 ** 67.9** (`⬆️ +16.3`) | 0.0% | 3.2% | 🟢 ZYSK |
| #19 | `L2_SO_STACKS_PLUS2` | Oficjum Stosy: 6 → 8 | 51.6 → 🟠 ** 62.0** (`⬆️ +10.4`) | 0.0% | 3.5% | 🟢 ZYSK |
| #20 | `L1_OBSERVED_PLUS2` | Próg Obserwowanej: offset +2 | 51.6 → 🔴 ** 57.4** (`⬆️ +5.8`) | 0.0% | 3.3% | 🟢 ZYSK |