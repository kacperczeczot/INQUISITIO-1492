[Strona główna](../../../../../README.md) > [legacy_iterations_01_28](README.md) > [02_podsumowanie_20_iteracji](02_podsumowanie_20_iteracji.md)

---

# Podsumowanie 17 Iteracji Optymalizacji Balansu

## 1. Trajektoria Naruszeń Czerwonej Linii

| Iteracja | Opis Zmiany Mechanicznej / Kart | Naruszenia (Blockery Red Line) | Czas (s) |
| :---: | :--- | :---: | :---: |
| Iteracja 01 | Baseline (Obecny stan z Opcją B Autodafé) | **14** | 3.38s |
| Iteracja 02 | Oficjum Stosy = 4 na 4p/5p (zamiast 3) | **14** | 3.34s |
| Iteracja 03 | Oficjum Stosy 4 na 4p/5p + Gildia Upadki 3 w 4p-no-oficjum | **14** | 3.36s |
| Iteracja 04 | Cienie: Dostęp do alternatywnej ścieżki ewakuacji od Ery 6 na 4-5p | **14** | 3.36s |
| Iteracja 05 | Korona: Dekret miejski od Ery 5 na 4-5p (zamiast Ery 6) | **14** | 3.39s |
| Iteracja 06 | Kabała: Wygrana od Ery 6 dla wszystkich składów 3p (zamiast Ery 7) | **14** | 3.49s |
| Iteracja 07 | Karta Cieni caa-05 (Ukryty Kurier): obniżenie kosztu z 2zł do 1zł | **11** | 3.4s |
| Iteracja 08 | Karta Cieni caa-10 (Echo Alhambry): obniżenie kosztu z 2zł do 1zł | **11** | 3.38s |
| Iteracja 09 | Karta Korony kb-09 (Dekret Królewski): obniżenie kosztu z 3zł do 2zł | **16** | 3.33s |
| Iteracja 10 | Karta Oficjum so-10 (Oczyść Miasto): podniesienie kosztu z 4zł do 5zł i Herezji z 2 do 3 | **17** | 3.34s |
| Iteracja 11 | Karta Korony kb-05 (List Żelazny): obniżenie kosztu z 3zł do 2zł | **11** | 3.43s |
| Iteracja 12 | Karta Kabały kt-10 (Pieczęć Salomona): obniżenie kosztu z 3zł do 2zł | **9** | 3.41s |
| Iteracja 13 | Karta Gildii gc-10 (Upadek Domu): obniżenie kosztu z 3zł do 2zł | **10** | 3.46s |
| Iteracja 14 | Werdykt: Stos z wyroku Werdyktu przyznawany Oficjum na 4-5p tylko gdy Oficjum oskarżało | **10** | 3.41s |
| Iteracja 15 | Cienie: Na 5p ewakuacja 2 Relikwii gwarantuje natychmiastowe zwycięstwo | **10** | 3.39s |
| Iteracja 16 | Kabała: Dociągnięcie progu Ery w 3p z Cieniami do Ery 7 (zapobiega op 3p) | **10** | 3.43s |
| Iteracja 17 | Ostateczny Skan Balansu — Wyniki Skorygowane | **10** | 3.45s |

## 2. Ostateczny Rozkład Wygranych we Wszystkich 16 Setupach (Iteracja 17)

| Kod Setupu | Gr. | Wygrane Frakcji (%) | Śr. Er | Deadlocki | Status Błędu |
| :--- | :---: | :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | **cienie-al-andalus**: 35.8%, **kabala-toledo**: 32.8%, **gildia-cieni**: 31.4% | 6.23 | 0.00 | 🟢 PASS (W normie) |
| `3p-cienie-korona-gildia` | 3 | **cienie-al-andalus**: 32.6%, **korona-borgiowie**: 23.2%, **gildia-cieni**: 44.2% | 5.76 | 0.00 | 🟢 PASS (W normie) |
| `3p-cienie-korona-kabala` | 3 | **cienie-al-andalus**: 43.2%, **korona-borgiowie**: 39.4%, **kabala-toledo**: 17.4% | 6.50 | 0.00 | 🔴 FAILED (CRITICAL UNDERPOWER: min_share=0.17<0.2 wins={'kabala-toledo': 87, 'cienie-al-andalus': 216, 'korona-borgiowie': 197}) |
| `3p-korona-kabala-gildia` | 3 | **korona-borgiowie**: 29.8%, **kabala-toledo**: 25.2%, **gildia-cieni**: 45.0% | 6.39 | 0.00 | 🟢 PASS (W normie) |
| `3p-oficjum-alandalus-gildia` | 3 | **swiete-oficjum**: 39.6%, **cienie-al-andalus**: 33.6%, **gildia-cieni**: 26.8% | 5.70 | 0.00 | 🟢 PASS (W normie) |
| `3p-oficjum-alandalus-kabala` | 3 | **swiete-oficjum**: 13.8%, **cienie-al-andalus**: 45.6%, **kabala-toledo**: 40.6% | 6.44 | 0.00 | 🔴 FAILED (CRITICAL OVERPOWER: max_share=0.46>0.45 wins={'cienie-al-andalus': 228, 'kabala-toledo': 203, 'swiete-oficjum': 69}; CRITICAL UNDERPOWER: min_share=0.14<0.2 wins={'cienie-al-andalus': 228, 'kabala-toledo': 203, 'swiete-oficjum': 69}) |
| `3p-oficjum-alandalus-korona` | 3 | **swiete-oficjum**: 30.8%, **cienie-al-andalus**: 42.0%, **korona-borgiowie**: 27.2% | 6.02 | 0.00 | 🟢 PASS (W normie) |
| `3p-oficjum-kabala-gildia` | 3 | **swiete-oficjum**: 26.4%, **kabala-toledo**: 48.8%, **gildia-cieni**: 24.8% | 6.67 | 0.00 | 🔴 FAILED (CRITICAL OVERPOWER: max_share=0.49>0.45 wins={'kabala-toledo': 244, 'gildia-cieni': 124, 'swiete-oficjum': 132}) |
| `3p-oficjum-korona-gildia` | 3 | **swiete-oficjum**: 38.8%, **korona-borgiowie**: 27.2%, **gildia-cieni**: 34.0% | 5.89 | 0.00 | 🟢 PASS (W normie) |
| `3p-oficjum-korona-kabala` | 3 | **swiete-oficjum**: 33.2%, **korona-borgiowie**: 43.0%, **kabala-toledo**: 23.8% | 6.74 | 0.00 | 🟢 PASS (W normie) |
| `4p-core` | 4 | **swiete-oficjum**: 31.0%, **cienie-al-andalus**: 22.0%, **korona-borgiowie**: 32.2%, **kabala-toledo**: 14.8% | 5.42 | 0.00 | 🔴 FAILED (CRITICAL UNDERPOWER: min_share=0.15<0.15 wins={'cienie-al-andalus': 110, 'swiete-oficjum': 155, 'korona-borgiowie': 161, 'kabala-toledo': 74}) |
| `4p-no-cienie` | 4 | **swiete-oficjum**: 38.4%, **korona-borgiowie**: 20.6%, **kabala-toledo**: 12.4%, **gildia-cieni**: 28.6% | 5.19 | 0.00 | 🔴 FAILED (CRITICAL OVERPOWER: max_share=0.38>0.35 wins={'swiete-oficjum': 192, 'korona-borgiowie': 103, 'gildia-cieni': 143, 'kabala-toledo': 62}; CRITICAL UNDERPOWER: min_share=0.12<0.15 wins={'swiete-oficjum': 192, 'korona-borgiowie': 103, 'gildia-cieni': 143, 'kabala-toledo': 62}) |
| `4p-no-kabala` | 4 | **swiete-oficjum**: 37.4%, **cienie-al-andalus**: 22.2%, **korona-borgiowie**: 17.0%, **gildia-cieni**: 23.4% | 4.88 | 0.00 | 🔴 FAILED (CRITICAL OVERPOWER: max_share=0.37>0.35 wins={'cienie-al-andalus': 111, 'korona-borgiowie': 85, 'swiete-oficjum': 187, 'gildia-cieni': 117}) |
| `4p-no-korona` | 4 | **swiete-oficjum**: 25.0%, **cienie-al-andalus**: 23.4%, **kabala-toledo**: 24.2%, **gildia-cieni**: 27.4% | 5.25 | 0.00 | 🟢 PASS (W normie) |
| `4p-no-oficjum` | 4 | **cienie-al-andalus**: 21.2%, **korona-borgiowie**: 23.8%, **kabala-toledo**: 15.6%, **gildia-cieni**: 39.4% | 5.28 | 0.00 | 🔴 FAILED (CRITICAL OVERPOWER: max_share=0.39>0.35 wins={'gildia-cieni': 197, 'korona-borgiowie': 119, 'cienie-al-andalus': 106, 'kabala-toledo': 78}) |
| `5p-full` | 5 | **swiete-oficjum**: 39.2%, **cienie-al-andalus**: 16.2%, **korona-borgiowie**: 12.0%, **kabala-toledo**: 13.2%, **gildia-cieni**: 19.4% | 4.36 | 0.00 | 🔴 FAILED (CRITICAL OVERPOWER: max_share=0.39>0.3 wins={'swiete-oficjum': 196, 'cienie-al-andalus': 81, 'gildia-cieni': 97, 'korona-borgiowie': 60, 'kabala-toledo': 66}) |