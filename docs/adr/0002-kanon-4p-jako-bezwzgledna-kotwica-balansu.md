# ADR-0002: Kanon 4P jako Bezwzględna Kotwica Balansu i SSOT

* **Status:** ACCEPTED
* **Data:** 2026-08-23
* **Autorzy:** Antigravity & Designer
* **Dotyczy:** `tools/sim/audytor_kanonu.py`, `sim/inquisitio/runner/scoring.py`, `game_config.yaml`

---

## 1. Kontekst Problemu
W historii prac nad balansem wielokrotnie dochodziło do sytuacji, w których próby jednoczesnego zbalansowania gry dla 3, 4 i 5 graczy prowadziły do rozmycia parametrów, paraliżu audytora oraz psucia głównego formatu turniejowego.
Wprowadzanie poprawek "pod 3P" niszczyło synergie w 4P, a audytor błądził w kompromisach wieloformatowych.

---

## 2. Decyzja Projektowa
1. **Bezwzględny Prymat Kanonu 4P:**
   - Podstawą i jedyną kotwicą balansu gry INQUISITIO-1492 jest **Kanon 4-osobowy (5 setupów 4P)**:
     1. `4p-core` (Święte Oficjum, Cienie Al-Andalus, Korona Borgiowie, Kabała Toledo)
     2. `4p-no-cienie` (Święte Oficjum, Gildia Cieni, Korona Borgiowie, Kabała Toledo)
     3. `4p-no-kabala` (Święte Oficjum, Cienie Al-Andalus, Korona Borgiowie, Gildia Cieni)
     4. `4p-no-korona` (Święte Oficjum, Cienie Al-Andalus, Gildia Cieni, Kabała Toledo)
     5. `4p-no-oficjum` (Gildia Cieni, Cienie Al-Andalus, Korona Borgiowie, Kabała Toledo)
2. **Kolejność Prac i Optymalizacji:**
   - **KROK 1 (Priorytet Bezwzględny):** Wszystkie 5 setupów Kanonu 4P muszą osiągnąć wynik **80+ pkt** (idealnie 85–90+ pkt).
   - **KROK 2:** Dopiero po doprowadzeniu do perfekcji Kanonu 4P dopuszcza się kalibrację dedykowanych offsetów dla trybów 3P i 5P w sekcji `overrides` konfiguracji.
3. **ZAKAZ ODWOŁYWANIA SIĘ DO 3P W TRAKCIE KALIBRACJI 4P:**
   - Podczas pracy nad Kanonem 4P zabrania się argumentowania zmian w oparciu o gry 3-osobowe.

---

## 3. Szczegółowe Uzasadnienie
* **Struktura Stołu w 4P:** 4 graczy tworzy pełną dynamikę koalicji 2 vs 2, 3 vs 1 oraz trójkątów intryg. Jest to docelowy, turniejowy i pudełkowy format gry.
* **Jednoznaczność Celu Optymalizatora:** Algorytmy mutacji (audytor kanonu) muszą mieć jednoznaczną funkcję celu bez sprzecznych wektorów gradientu.

---

## 4. Niezmienniki (Invariants)
* 🛑 Żaden patch nie może zostać przyjęty do `game_config.yaml`, jeśli obniża minimalny wynik któregokolwiek z 5 setupów 4P poniżej progu akceptacji.
* 🛡️ Każdy raport ewaluacyjny (`raport_telemetrii.md`) musi w pierwszej kolejności przedstawiać macierz 5 setupów Kanonu 4P.
