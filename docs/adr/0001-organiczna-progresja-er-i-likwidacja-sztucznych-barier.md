[Strona główna](../../README.md) > [adr](README.md) > [0001-organiczna-progresja-er-i-likwidacja-sztucznych-barier](0001-organiczna-progresja-er-i-likwidacja-sztucznych-barier.md)

---

# ADR-0001: Organiczna Progresja Er i Likwidacja Sztucznych Barier Czasowych

* **Status:** ACCEPTED
* **Data:** 2026-08-23
* **Autorzy:** Antigravity & Designer
* **Dotyczy:** `sim/inquisitio/engine/win.py`, `game_config.yaml`, `sim/inquisitio/engine/effects/`

---

## 1. Kontekst Problemu
W wersjach v1.0-alpha.30 – v1.0-alpha.43 w silniku wprowadzono twarde, binarne blokady er w sprawdzaniu warunków zwycięstwa (`win.py`), takie jak:
- `if pl.relics_evacuated >= relic_need and state.era >= 3:`
- `or (pl.shadow_exit and state.era >= 4)`
- `if pl.fragments >= frag_need and heresy_ok and state.era >= max(1, base_era):` (gdzie `base_era = 6`)

### Dlaczego to było wadliwe?
1. **Sztuczny podział rozgrywki na monolityczne fazy:**
   - Przed Erą 3 lub 4 szansa na zwycięstwo frakcji wynosiła sztucznie **0.0%**.
   - W Erze 3 Cienie Al-Andalus wygrywały **59.5%** partii, a w Erze 6 ich szanse spadały do **6.1%**.
   - W Erze 6 Kabała Toledo wygrywała **58.2%** partii, działając jak bezwzględny, pasywny stoper wyłączający inne frakcje.
2. **Kastracja dynamiki stołu:**
   - Zamiast modulować szanse i stawiać przed graczami wyzwania logistyczne i strategiczne, gra traktowała ery jak sztywne progi uniemożliwiające wygraną mimo wykonania questu.

---

## 2. Decyzja Projektowa
1. **Całkowite usunięcie twardych warunków `state.era >= X` z silnika sprawdzania zwycięstwa ([`win.py`](file:///Users/kacper/Documents/GitHub/INQUISITIO-1492/sim/inquisitio/engine/win.py)).**
2. **Zastąpienie sztucznych barier organicznymi kosztami i wymaganiami questowymi:**
   - **Kabała Toledo:** Wymaga zgromadzenia 3 fragmentów oraz utrzymania poziomu herezji w **Złotym Paśmie Herezji `[4, 6]`** w momencie rzucania `kt-10 Pieczęć Salomona` (koszt 3 zł).
   - **Cienie Al-Andalus:** Wymaga ewakuacji 2 relikwii z planszy za pomocą kuriera (`caa-05`, koszt 2 zł), podwójnego agenta (`path_via_double`), uniknięcia stosu (`avoided_autodafe`) lub przez otwarty Szlak Morski.
   - **Korona Borgiowie:** Wymaga zagrania 2 dekretów i utrzymania haków na rywalach.
   - **Święte Oficjum:** Wymaga skazania 3 rywali w procesach lub postawienia 6 stosów, wspartego dochodem ze skarbca (`so-02`, 3 zł).
3. **Funkcja Er:** Ery nie blokują wygranej, lecz **naturalnie modulują dostęp do zasobów, tempo dociągu kart, ryzyko aresztowań i eskalację herezji**.

---

## 3. Szczegółowe Uzasadnienie (Game Design & Matematyka)

### 3.1. Płynna Krzywa Rozkładu Czasu Gry (Krzywa Gaussa)
* **Era 1–2 (Wczesny start):** Szansa na wygraną wynosi $0.1–2.0\%$. Może wystąpić tylko przy skrajnie ryzykownym, niekontrowanym zagraniu "all-in" lub krytycznych błędach przeciwników.
* **Era 3 (Wczesna faza średnia):** ~$10–18\%$ partii — szybkie strategie ucieczki lub agresywne procesy inkwizycji.
* **Era 4–6 (Serce gry — Złote Okno Rozgrywki):** **$70–80\%$ wszystkich partii**. W tej fazie każda z 4 frakcji przy stole ma zbliżone ($20–30\%$) szanse na wygraną w danej erze.
* **Era 7+ (Dogrywka/Wyczerpanie):** ~$5–10\%$ partii — dramatyczne końcówki, gdzie o zwycięstwie decyduje pojedynczy ruch na wyczerpanych zasobach.

### 3.2. Likwidacja Monopolu Kabały w Erze 6
* Kabała w Erze 6 nie wygrywa automatycznie, ponieważ jej poziom herezji jest dynamicznie atakowany przez oskarżenia Inkwizycji (wypychające Kabałę na 7+) lub szantaże Gildii (zbijające herezję na 2–3).
* Kabała musi poświęcić akcje i złoto na stabilizację sefirot, co daje rywalom pełne okno na domknięcie własnego zwycięstwa.

---

## 4. Niezmienniki Architektoniczne (Invariants)
* 🛑 **ZAKAZ:** Wprowadzania jakichkolwiek warunków `if state.era < X: return None` do funkcji `check_winner_details`.
* 🛑 **ZAKAZ:** Tworzenia kart dających natychmiastowe zwycięstwo bez interaktywnego warunku zasobowego/pozycyjnego.
* 🛡️ **GWARANCJA:** Każda frakcja obecna w grze 4P musi mieć niezerowe szanse na wygraną w Erach 3, 4, 5 i 6.

---

## 5. Konsekwencje
* Silnik symulacji mierzy naturalną witalność rozgrywki opartą na interakcji kart i agentów.
* Zlikwidowano syndrom "martwej frakcji" w późnej fazie gry.
