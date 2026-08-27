[Strona główna](../../../../../README.md) > [legacy_iterations_01_28](README.md) > [14_audyt_kombinacji_3_poprawek](14_audyt_kombinacji_3_poprawek.md)

---

# Raport 14: Audyt Kombinatoryczny TOP 3 Poprawek Warunków Zwycięstwa

**Przeanalizowano Wariantów:** 8 | **Próba:** 300 gier/setup | **Czas:** 34.73s
**Wynik Bazy:** `41.6 / 100.0 pkt`

## 1. Tabela Porównawcza: Pojedynczo vs Parami vs Komplet 3

| ID | Typ Testu | Nazwa Kombinacji Poprawek | Global Score | Różnica vs Baza | 3p Avg | 4p Avg | 5p Avg | Czy Poprawia Wynik? |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BAZA` | BAZA | Baza (Obecny Zaktualizowany Pakiet Zasad) | ** 41.6** | `0.0` | 15.8 | 59.8 | 49.3 | ⚪ NEUTRALNY |
| `SING_1` | POJEDYNCZO | 1. Kabała: Wymagane Fragmenty = 2 na 5p (WIN_KT_02) | ** 46.7** | `+5.1` | 15.8 | 59.8 | 64.5 | 🟢 TAK (Poprawia) |
| `SING_2` | POJEDYNCZO | 2. Kabała: Pasmo Herezji = 3–7 (WIN_KT_04) | ** 44.7** | `+3.1` | 17.6 | 54.3 | 62.1 | 🟢 TAK (Poprawia) |
| `SING_3` | POJEDYNCZO | 3. Cienie: Relikwie = 3 dla wszystkich składów (WIN_CAA_01) | ** 42.6** | `+1.0` | 18.9 | 59.7 | 49.3 | 🟢 TAK (Poprawia) |
| `PAIR_1_2` | PAIRWISE | Para (1+2): Kabała 5p Fragmenty=2 + Pasmo 3–7 | ** 46.2** | `+4.6` | 17.6 | 54.3 | 66.6 | 🟢 TAK (Poprawia) |
| `PAIR_1_3` | PAIRWISE | Para (1+3): Kabała 5p Fragmenty=2 + Cienie Relikwie=3 | ** 47.7** | `+6.1` | 18.9 | 59.7 | 64.5 | 🟢 TAK (Poprawia) |
| `PAIR_2_3` | PAIRWISE | Para (2+3): Kabała Pasmo 3–7 + Cienie Relikwie=3 | ** 45.7** | `+4.1` | 20.7 | 54.3 | 62.1 | 🟢 TAK (Poprawia) |
| `TRIPLET` | TRIPLET | Komplet (1+2+3): Wszystkie 3 poprawki jednocześnie | ** 47.2** | `+5.6` | 20.7 | 54.3 | 66.6 | 🟢 TAK (Poprawia) |

## 2. Szczegółowa Analiza Porównawcza Synergii

### A. Wdrożenie Pojedyncze (Single Tweaks)
- `SING_1` (Kabała 5p Fragmenty=2): Score = `46.7 pkt` (5p score: `64.5 pkt`)
- `SING_2` (Kabała Pasmo 3–7): Score = `44.7 pkt` (5p score: `62.1 pkt`)
- `SING_3` (Cienie Relikwie=3): Score = `42.6 pkt` (3p score: `18.9 pkt`)

### B. Wdrożenie Parami (Pairwise Synergies)
- `PAIR_1_2` (Kabała 5p Fragmenty=2 + Pasmo 3–7): Score = `46.2 pkt`
- `PAIR_1_3` (Kabała 5p Fragmenty=2 + Cienie Relikwie=3): Score = `47.7 pkt`
- `PAIR_2_3` (Kabała Pasmo 3–7 + Cienie Relikwie=3): Score = `45.7 pkt`

### C. Wdrożenie Pełne (Triplet Ensemble)
- `TRIPLET` (Komplet 1+2+3): Score = `47.2 pkt` (3p:20.7, 4p:54.3, 5p:66.6)

## 3. Ostateczna Rekomendacja Produkcyjna GDD

🏆 **Absolutnie Zwycięskie Zestawienie:** **TRIPLET (Komplet (1+2+3): Wszystkie 3 poprawki jednocześnie)** z wynikami w poszczególnych kategoriach!