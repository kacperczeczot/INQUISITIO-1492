[Strona główna](../../../../../README.md) > [legacy_iterations_01_28](README.md) > [01_iteracja_01_diagnoza](01_iteracja_01_diagnoza.md)

---

# Raport Diagnostyczny Balansu — Iteracja 01

**Weryfikacja próby:** 500 gier na setup | **Warstwa:** C | **Próg Oskarżenia:** 7 | **Czas wykonania:** 3.39s

## 1. Tabela Wyników Wszystkich 16 Setupów

| Kod Setupu | Gr. | Wygrane Frakcji (%) | Śr. Er | Deadlocki | Stan Błędu (Red Line) |
| :--- | :---: | :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | **cienie-al-andalus**: 19.8%, **kabala-toledo**: 45.4%, **gildia-cieni**: 34.8% | 6.66 | 0.00 | 🔴 FAILED (CRITICAL OVERPOWER: max_share=0.45>0.45 wins={'cienie-al-andalus': 99, 'kabala-toledo': 227, 'gildia-cieni': 174}; CRITICAL UNDERPOWER: min_share=0.20<0.2 wins={'cienie-al-andalus': 99, 'kabala-toledo': 227, 'gildia-cieni': 174}) |
| `3p-cienie-korona-gildia` | 3 | **cienie-al-andalus**: 23.4%, **korona-borgiowie**: 34.4%, **gildia-cieni**: 42.2% | 6.41 | 0.00 | 🟢 PASS (W normie) |
| `3p-cienie-korona-kabala` | 3 | **cienie-al-andalus**: 25.0%, **korona-borgiowie**: 42.0%, **kabala-toledo**: 33.0% | 6.91 | 0.00 | 🟢 PASS (W normie) |
| `3p-korona-kabala-gildia` | 3 | **korona-borgiowie**: 25.2%, **kabala-toledo**: 32.4%, **gildia-cieni**: 42.4% | 6.78 | 0.00 | 🟢 PASS (W normie) |
| `3p-oficjum-alandalus-gildia` | 3 | **swiete-oficjum**: 41.8%, **cienie-al-andalus**: 24.0%, **gildia-cieni**: 34.2% | 6.19 | 0.00 | 🟢 PASS (W normie) |
| `3p-oficjum-alandalus-kabala` | 3 | **swiete-oficjum**: 23.4%, **cienie-al-andalus**: 25.6%, **kabala-toledo**: 51.0% | 6.71 | 0.00 | 🔴 FAILED (CRITICAL OVERPOWER: max_share=0.51>0.45 wins={'kabala-toledo': 255, 'swiete-oficjum': 117, 'cienie-al-andalus': 128}) |
| `3p-oficjum-alandalus-korona` | 3 | **swiete-oficjum**: 35.4%, **cienie-al-andalus**: 27.4%, **korona-borgiowie**: 37.2% | 6.51 | 0.00 | 🟢 PASS (W normie) |
| `3p-oficjum-kabala-gildia` | 3 | **swiete-oficjum**: 35.4%, **kabala-toledo**: 35.4%, **gildia-cieni**: 29.2% | 6.31 | 0.00 | 🟢 PASS (W normie) |
| `3p-oficjum-korona-gildia` | 3 | **swiete-oficjum**: 43.2%, **korona-borgiowie**: 25.6%, **gildia-cieni**: 31.2% | 5.97 | 0.00 | 🟢 PASS (W normie) |
| `3p-oficjum-korona-kabala` | 3 | **swiete-oficjum**: 41.4%, **korona-borgiowie**: 33.2%, **kabala-toledo**: 25.4% | 6.74 | 0.00 | 🟢 PASS (W normie) |
| `4p-core` | 4 | **swiete-oficjum**: 46.8%, **cienie-al-andalus**: 16.6%, **korona-borgiowie**: 16.8%, **kabala-toledo**: 19.8% | 5.68 | 0.00 | 🔴 FAILED (CRITICAL OVERPOWER: max_share=0.47>0.35 wins={'kabala-toledo': 99, 'swiete-oficjum': 234, 'korona-borgiowie': 84, 'cienie-al-andalus': 83}) |
| `4p-no-cienie` | 4 | **swiete-oficjum**: 48.0%, **korona-borgiowie**: 10.2%, **kabala-toledo**: 16.0%, **gildia-cieni**: 25.8% | 5.21 | 0.00 | 🔴 FAILED (CRITICAL OVERPOWER: max_share=0.48>0.35 wins={'kabala-toledo': 80, 'gildia-cieni': 129, 'swiete-oficjum': 240, 'korona-borgiowie': 51}; CRITICAL UNDERPOWER: min_share=0.10<0.15 wins={'kabala-toledo': 80, 'gildia-cieni': 129, 'swiete-oficjum': 240, 'korona-borgiowie': 51}) |
| `4p-no-kabala` | 4 | **swiete-oficjum**: 44.6%, **cienie-al-andalus**: 14.6%, **korona-borgiowie**: 15.0%, **gildia-cieni**: 25.8% | 5.18 | 0.00 | 🔴 FAILED (CRITICAL OVERPOWER: max_share=0.45>0.35 wins={'cienie-al-andalus': 73, 'swiete-oficjum': 223, 'gildia-cieni': 129, 'korona-borgiowie': 75}; CRITICAL UNDERPOWER: min_share=0.15<0.15 wins={'cienie-al-andalus': 73, 'swiete-oficjum': 223, 'gildia-cieni': 129, 'korona-borgiowie': 75}) |
| `4p-no-korona` | 4 | **swiete-oficjum**: 38.8%, **cienie-al-andalus**: 13.8%, **kabala-toledo**: 23.2%, **gildia-cieni**: 24.2% | 5.21 | 0.00 | 🔴 FAILED (CRITICAL OVERPOWER: max_share=0.39>0.35 wins={'gildia-cieni': 121, 'swiete-oficjum': 194, 'kabala-toledo': 116, 'cienie-al-andalus': 69}; CRITICAL UNDERPOWER: min_share=0.14<0.15 wins={'gildia-cieni': 121, 'swiete-oficjum': 194, 'kabala-toledo': 116, 'cienie-al-andalus': 69}) |
| `4p-no-oficjum` | 4 | **cienie-al-andalus**: 14.0%, **korona-borgiowie**: 21.2%, **kabala-toledo**: 17.6%, **gildia-cieni**: 47.2% | 5.74 | 0.00 | 🔴 FAILED (CRITICAL OVERPOWER: max_share=0.47>0.35 wins={'gildia-cieni': 236, 'korona-borgiowie': 106, 'cienie-al-andalus': 70, 'kabala-toledo': 88}; CRITICAL UNDERPOWER: min_share=0.14<0.15 wins={'gildia-cieni': 236, 'korona-borgiowie': 106, 'cienie-al-andalus': 70, 'kabala-toledo': 88}) |
| `5p-full` | 5 | **swiete-oficjum**: 43.6%, **cienie-al-andalus**: 7.6%, **korona-borgiowie**: 10.8%, **kabala-toledo**: 12.2%, **gildia-cieni**: 25.8% | 4.47 | 0.00 | 🔴 FAILED (CRITICAL OVERPOWER: max_share=0.44>0.3 wins={'cienie-al-andalus': 38, 'swiete-oficjum': 218, 'gildia-cieni': 129, 'korona-borgiowie': 54, 'kabala-toledo': 61}; CRITICAL UNDERPOWER: min_share=0.08<0.1 wins={'cienie-al-andalus': 38, 'swiete-oficjum': 218, 'gildia-cieni': 129, 'korona-borgiowie': 54, 'kabala-toledo': 61}) |

## 2. Analiza Problemów Balansowych (Czerwona Linia i Cel Ścisły)

### A. Frakcje Przeważone (Overpowered)
- **`3p-cienie-kabala-gildia`** — **kabala-toledo** wygrywa **45.4%** (Przekroczona Czerwona Linia max: 45.0%)
- *`3p-cienie-korona-gildia`* — *gildia-cieni* wygrywa *42.2%* (Powyżej Celu Ścisłego max: 38.0%)
- *`3p-cienie-korona-kabala`* — *korona-borgiowie* wygrywa *42.0%* (Powyżej Celu Ścisłego max: 38.0%)
- *`3p-korona-kabala-gildia`* — *gildia-cieni* wygrywa *42.4%* (Powyżej Celu Ścisłego max: 38.0%)
- *`3p-oficjum-alandalus-gildia`* — *swiete-oficjum* wygrywa *41.8%* (Powyżej Celu Ścisłego max: 38.0%)
- **`3p-oficjum-alandalus-kabala`** — **kabala-toledo** wygrywa **51.0%** (Przekroczona Czerwona Linia max: 45.0%)
- *`3p-oficjum-korona-gildia`* — *swiete-oficjum* wygrywa *43.2%* (Powyżej Celu Ścisłego max: 38.0%)
- *`3p-oficjum-korona-kabala`* — *swiete-oficjum* wygrywa *41.4%* (Powyżej Celu Ścisłego max: 38.0%)
- **`4p-core`** — **swiete-oficjum** wygrywa **46.8%** (Przekroczona Czerwona Linia max: 35.0%)
- **`4p-no-cienie`** — **swiete-oficjum** wygrywa **48.0%** (Przekroczona Czerwona Linia max: 35.0%)
- **`4p-no-kabala`** — **swiete-oficjum** wygrywa **44.6%** (Przekroczona Czerwona Linia max: 35.0%)
- **`4p-no-korona`** — **swiete-oficjum** wygrywa **38.8%** (Przekroczona Czerwona Linia max: 35.0%)
- **`4p-no-oficjum`** — **gildia-cieni** wygrywa **47.2%** (Przekroczona Czerwona Linia max: 35.0%)
- **`5p-full`** — **swiete-oficjum** wygrywa **43.6%** (Przekroczona Czerwona Linia max: 30.0%)
- *`5p-full`* — *gildia-cieni* wygrywa *25.8%* (Powyżej Celu Ścisłego max: 24.0%)

### B. Frakcje Pod-zbalansowane (Underpowered)
- **`3p-cienie-kabala-gildia`** — **cienie-al-andalus** wygrywa **19.8%** (Poniżej Czerwonej Linii min: 20.0%)
- *`3p-cienie-korona-gildia`* — *cienie-al-andalus* wygrywa *23.4%* (Poniżej Celu Ścisłego min: 28.0%)
- *`3p-cienie-korona-kabala`* — *cienie-al-andalus* wygrywa *25.0%* (Poniżej Celu Ścisłego min: 28.0%)
- *`3p-korona-kabala-gildia`* — *korona-borgiowie* wygrywa *25.2%* (Poniżej Celu Ścisłego min: 28.0%)
- *`3p-oficjum-alandalus-gildia`* — *cienie-al-andalus* wygrywa *24.0%* (Poniżej Celu Ścisłego min: 28.0%)
- *`3p-oficjum-alandalus-kabala`* — *swiete-oficjum* wygrywa *23.4%* (Poniżej Celu Ścisłego min: 28.0%)
- *`3p-oficjum-alandalus-kabala`* — *cienie-al-andalus* wygrywa *25.6%* (Poniżej Celu Ścisłego min: 28.0%)
- *`3p-oficjum-alandalus-korona`* — *cienie-al-andalus* wygrywa *27.4%* (Poniżej Celu Ścisłego min: 28.0%)
- *`3p-oficjum-korona-gildia`* — *korona-borgiowie* wygrywa *25.6%* (Poniżej Celu Ścisłego min: 28.0%)
- *`3p-oficjum-korona-kabala`* — *kabala-toledo* wygrywa *25.4%* (Poniżej Celu Ścisłego min: 28.0%)
- *`4p-core`* — *cienie-al-andalus* wygrywa *16.6%* (Poniżej Celu Ścisłego min: 20.0%)
- *`4p-core`* — *korona-borgiowie* wygrywa *16.8%* (Poniżej Celu Ścisłego min: 20.0%)
- *`4p-core`* — *kabala-toledo* wygrywa *19.8%* (Poniżej Celu Ścisłego min: 20.0%)
- **`4p-no-cienie`** — **korona-borgiowie** wygrywa **10.2%** (Poniżej Czerwonej Linii min: 15.0%)
- *`4p-no-cienie`* — *kabala-toledo* wygrywa *16.0%* (Poniżej Celu Ścisłego min: 20.0%)
- **`4p-no-kabala`** — **cienie-al-andalus** wygrywa **14.6%** (Poniżej Czerwonej Linii min: 15.0%)
- *`4p-no-kabala`* — *korona-borgiowie* wygrywa *15.0%* (Poniżej Celu Ścisłego min: 20.0%)
- **`4p-no-korona`** — **cienie-al-andalus** wygrywa **13.8%** (Poniżej Czerwonej Linii min: 15.0%)
- **`4p-no-oficjum`** — **cienie-al-andalus** wygrywa **14.0%** (Poniżej Czerwonej Linii min: 15.0%)
- *`4p-no-oficjum`* — *kabala-toledo* wygrywa *17.6%* (Poniżej Celu Ścisłego min: 20.0%)
- **`5p-full`** — **cienie-al-andalus** wygrywa **7.6%** (Poniżej Czerwonej Linii min: 10.0%)
- *`5p-full`* — *korona-borgiowie* wygrywa *10.8%* (Poniżej Celu Ścisłego min: 16.0%)
- *`5p-full`* — *kabala-toledo* wygrywa *12.2%* (Poniżej Celu Ścisłego min: 16.0%)