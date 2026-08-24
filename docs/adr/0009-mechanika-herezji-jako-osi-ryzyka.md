# ADR-0009: Mechanika Herezji jako Dynamicznej Osi Ryzyka i Push-Your-Luck

* **Status:** ACCEPTED
* **Data:** 2026-08-23
* **Autorzy:** Antigravity & Designer
* **Dotyczy:** `sim/inquisitio/engine/heresy.py`, `sim/inquisitio/engine/effects/`, `game_config.yaml`, `docs/rules/`

---

## 1. Kontekst Problemu
Herezja jest unikalną walutą w INQUISITIO-1492 – służy zarówno jako paliwo dla potężnych akcji, jak i wskaźnik podatności na represje Inkwizycji. We wcześniejszych fazach pojawiały się próby tworzenia kart dających darmowe, całkowite resety Herezji do zera lub pomijania pasm ostrzegawczych.

### Dlaczego to było wadliwe?
1. **Niszczenie napięcia:** Możliwość natychmiastowego zresetowania Herezji do zera usuwa element ryzyka i negatywnej interakcji przy stole.
2. **Kastracja celów Inkwizycji:** Święte Oficjum i procesy inkwizycyjne stają się bezużyteczne, jeśli rywale mogą w jednej chwili uciec z progu oskarżenia.

---

## 2. Decyzja Projektowa
1. **Trzystrefowa Architektura Herezji:**
   - **Strefa Czysta (0 do T_obs - 1):** Pełne bezpieczeństwo przed stosem podczas Autodafé; aresztowanie skutkuje jedynie uwięzieniem w Lochach.
   - **Strefa Obserwowana (T_obs do T_acc - 1):** Gracz znajduje się pod lupą Trybunału; agent schwytany przez Inkwizytora podczas Autodafé trafia na Stos.
   - **Strefa Krytyczna / Próg Oskarżenia (T_acc+):** Pełna podatność na procesy i Werdykt Inkwizycji w Fazie II.
2. **Zasada kontrolowanej redukcji:**
   - Oczyszczenie z Herezji wymaga poświęcenia akcji, złota lub realizacji konkretnych warunków na planszy.
   - Brak kart resetujących Herezję do 0 bez ekwiwalentnego kosztu.
3. **Sygnatura Kabały (Złote Pasmo Herezji):**
   - Kabała z Toledo operuje na krawędzi wiedzy tajemnej – jej finiszer wymaga utrzymania Herezji w precyzyjnym paśmie (wartość bazowa w SSOT: `[4, 6]`), balansując między brakiem mocy a stosem.

---

## 3. Szczegółowe Uzasadnienie (Game Design)
* **Klimat inkwizycyjny:** Każdy punkt Herezji to realna groźba. Im bardziej gracz korzysta z zakazanych mocy, tym bliżej znajduje się Trybunału.
* **Interakcja negatywna:** Rywale mogą celowo wrabiać gracza w Herezję (`frame_rival`), zmuszając go do marnowania akcji na oczyszczenie lub wypychając go pod topór Inkwizycji.

---

## 4. Niezmienniki Architektoniczne (Invariants)
* 🛑 **ZAKAZ:** Wprowadzania efektów bezwarunkowo kasujących całą Herezję do 0.
* 🛡️ **GWARANCJA:** Przejście przez próg krytyczny zawsze otwiera możliwość rozpatrzenia procesu w Fazie II.

---

## 5. Konsekwencje
* Wartości progów `observed` oraz `accusation` są konfigurowane centralnie w SSOT (`game_config.yaml`).
* Zapewniono stałą dynamikę zagrożenia i wzajemnego szantażu przy stole.
