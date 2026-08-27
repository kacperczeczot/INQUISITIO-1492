[Strona główna](../../README.md) > [adr](README.md) > [0010-witalnosc-alternatywnych-sciezek-zwyciestwa](0010-witalnosc-alternatywnych-sciezek-zwyciestwa.md)

---

# ADR-0010: Witalność Alternatywnych Ścieżek Zwycięstwa (Dual-Path Invariant)

* **Status:** ACCEPTED
* **Data:** 2026-08-23
* **Autorzy:** Antigravity & Designer
* **Dotyczy:** `sim/inquisitio/engine/win.py`, `tools/sim/audit_level2.py`, `docs/adr/0003-anatomia-i-asymetria-warunkow-zwyciestwa-frakcji.md`

---

## 1. Kontekst Problemu
Niektóre frakcje (w szczególności Święte Oficjum) posiadają w swoim portfolio dwie niezależne ścieżki do wygranej:
1. **Ścieżka Egzekucyjna (Stosy / Autodafé)** — eliminacja agentów rywali na stosach.
2. **Ścieżka Sądowa (Procesy i Skazania Rywali)** — polityczne skazanie określonej liczby unikalnych frakcji.

W trakcie automatycznego strojenia dochodziło do zjawiska degeneracji: algorytm maksymalizował jedną ścieżkę (np. tylko skazania), całkowicie uśmiercając drugą (0% wygranych przez stosy).

### Dlaczego to był błąd?
* Jeśli ścieżka staje się martwa w telemetrii ($<8\%$), gracz traci poczucie wyboru strategicznego, a karty wspierające tę mechanikę stają się „martwym drewnem” w talii.

---

## 2. Decyzja Projektowa
1. **Zasada Witalności Podwójnej Ścieżki:**
   - Wszelkie frakcje posiadające alternatywne warunki zwycięstwa muszą utrzymywać zdrową witalność obu ścieżek w symulacjach wielkoskalowych.
   - Niedopuszczalne jest obniżenie progu jednej ścieżki do poziomu, który czyni drugą ścieżkę statystycznie martwą.
2. **Zrównoważenie tempa obu dróg:**
   - Ścieżka Stosów wymaga aktywnego napędzania Herezji na planszy i polowań Inkwizytora.
   - Ścieżka Skazań wymaga celowego wrabiania różnych rywali i przepychania procesów w Trybunale.
   - Obie ścieżki muszą osiągać dojrzałość w Złotym Oknie (Ery 5–7).

---

## 3. Szczegółowe Uzasadnienie (Game Design)
* **Elastyczność taktyczna:** Gracz kierujący Oficjum powinien móc dostosować strategię do zachowania stołu: jeśli rywale unikają Inkwizytora, uderza w procesy w Trybunale; jeśli rywale zbierają Herezję, pali ich w Autodafé.
* **Głębia rozgrywki:** Rywale muszą stale monitorować oba wektory zagrożenia ze strony Inkwizycji.

---

## 4. Niezmienniki Architektoniczne (Invariants)
* 🛑 **ZAKAZ:** Tłumienia jednej ze ścieżek Oficjum poniżej minimalnego progu witalności w telemetrii.
* 🛡️ **GWARANCJA:** Narzędzia audytorskie traktują uśmiercenie którejkolwiek ścieżki jako błąd krytyczny balansu (Degeneration Penalty).

---

## 5. Konsekwencje
* Wartości progowe dla obu ścieżek podlegają zrównoważonemu strojeniu w `game_config.yaml`.
* Żadna karta w talii Oficjum nie traci swojej racji bytu.
