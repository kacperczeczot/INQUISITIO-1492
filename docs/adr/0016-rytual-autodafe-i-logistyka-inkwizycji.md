[Strona główna](../../README.md) > [adr](README.md) > [0016-rytual-autodafe-i-logistyka-inkwizycji](0016-rytual-autodafe-i-logistyka-inkwizycji.md)

---

# ADR-0016: Rytuał Autodafé, Cykliczność i Logistyka Przesłuchań Inkwizycji

* **Status:** ACCEPTED
* **Data:** 2026-08-23
* **Autorzy:** Antigravity & Designer
* **Dotyczy:** `sim/inquisitio/engine/inquisitor.py`, `sim/inquisitio/engine/turn.py`, `game_config.yaml`, `docs/rules/ksiega.md`

---

## 1. Kontekst Problemu
Autodafé to centralne, publiczne wydarzenie inkwizycyjne w grze. W historii prac pojawiały się dwie krytyczne rozbieżności:
1. **Zasięg stosu:** Błędne interpretacje zakładały palenie heretyków na całej planszy jednocześnie, co niszczyło logistykę unikania Inkwizytora.
2. **Częstotliwość:** Zbyt częste Autodafé (np. co 1–2 ery) zamieniało grę w rzeźnię agentów, z kolei zbyt rzadkie czyniło ścieżkę Stosów Oficjum martwą.

---

## 2. Decyzja Projektowa
1. **Lokalność i Logistyka Autodafé (Lokalny Zasięg Stosu):**
   - Rytuał Autodafé nie uderza globalnie w całą planszę.
   - **Pod topór Inkwizycji trafiają wyłącznie agenci znajdujący się w TEJ SAMEJ LOKACJI co pion Inkwizytora** w momencie rozpatrzenia fazy.
2. **Warunkowość Kary (Areszt vs Stos):**
   - **Gracz w Strefie Czystej (Herezja < T_obs):** Agent schwytany przez Inkwizytora zostaje **aresztowany i przeniesiony do Lochów** (brak punktu Stosu dla Oficjum).
   - **Gracz w Strefie Obserwowanej lub Krytycznej (Herezja $\ge$ T_obs):** Agent zostaje **skazany i spalony na Stosie** (Święte Oficjum inkasuje +1 Stos).
3. **Częstotliwość i Cel Średniej Liczby Autodafé (~2 razy na partię):**
   - W standardowej partii trwającej średnio 5.5–6.5 Er (ADR-0004), rytuał Autodafé **musi pojawić się dokładnie ~2 razy** (pierwsze wczesne Autodafé w okolicy Ery 3 oraz drugie kulminacyjne Autodafé w szczycie Złotego Okna w Erze 6).
   - Ustawienie cooldownu $\ge 4$ Er jest błędem projektowym, ponieważ w grze trwającej 5–7 Er drugie Autodafé wypadłoby w Erze 8–9 (po zakończeniu partii), redukując liczbę Autodafé do zaledwie 1 na grę i kradnąc Oficjum drugą szansę na Stosy.

---

## 3. Szczegółowe Uzasadnienie (Game Design & Klimat)
* **Klimat grozy i dwa punkty zwrotne:** Dwa Autodafé w partii tworzą doskonałą dynamikę: pierwsze zmusza do wczesnej ostrożności i ucieczki przed stosem, drugie stanowi wielki finał polowań Inkwizycji w późnej fazie gry.
* **Metoda Balansowania Oficjum:** Dominację Oficjum kontrolujemy poprzez **koszty i siłę oskarżeń na kartach (L3)** oraz **wymóg Progu Obserwowanej ($\ge 5\text{☣}$)**, a NIE poprzez niszczenie rytmu gry i sztuczne blokowanie Autodafé do 1 razu na mecz.

---

## 4. Niezmienniki Architektoniczne (Invariants)
* 🛑 **ZAKAZ:** Podnoszenia cooldownu Autodafé do wartości $\ge 4$ Er, która redukowałaby średnią liczbę Autodafé w Złotym Oknie poniżej 1.5 na partię.
* 🛑 **ZAKAZ:** Palenia agentów poza lokacją, w której fizycznie znajduje się pion Inkwizytora.
* 🛑 **ZAKAZ:** Naliczania punktu Stosu dla Oficjum, jeśli ukarany gracz posiada Herezję poniżej Progu Obserwowanej (`observed_threshold`).
* 🛡️ **GWARANCJA:** Gracz zawsze ma możliwość uniknięcia stosu poprzez przemieszczenie agenta poza lokację Inkwizytora przed nadejściem fazy sądu.

---

## 5. Konsekwencje
* Pełna zgodność silnika `sim/inquisitio/engine/inquisitor.py` z księgą zasad `docs/rules/ksiega.md`.
* Eliminacja nagłych, nieuczciwych wipe-outów agentów na całej planszy przy zachowaniu 2 emocjonujących rytuałów w każdej pełnej partii.
