[Strona główna](../../README.md) > [adr](README.md) > [0015-model-heurystycznego-racjonalnego-gracza](0015-model-heurystycznego-racjonalnego-gracza.md)

---

# ADR-0015: Model Heurystycznego Racjonalnego Gracza w Symulacji

* **Status:** ACCEPTED
* **Data:** 2026-08-23
* **Autorzy:** Antigravity & Designer
* **Dotyczy:** `sim/inquisitio/agents/`, `sim/inquisitio/engine/`

---

## 1. Kontekst Problemu
Symulacja gry planszowej wymaga botów, które zachowują się jak myślący ludzie przy stole. Losowy wybór kart wypaczał telemetrię, z kolei stosowanie zewnętrznych modeli LLM przez API było niemożliwe ze względu na czas i koszty (miliony partii).

---

## 2. Decyzja Projektowa
1. **Model Heurystycznego Racjonalnego Gracza (Fast Rational Agent):**
   - Boty operują na szybkich, deterministycznych heurystykach oceny stanu planszy (priorytetyzacja celów frakcyjnych, obrona przed stosem, szacowanie ryzyka Herezji, taktyczne pasowanie).
2. **Bezwzględna Uczciwość Informacyjna (No Cheating Policy):**
   - Bot ma dostęp wyłącznie do informacji jawnych na stole oraz własnej ręki.
   - Bot NIE WIDZI zakrytych kart w talii rywali ani nadchodzących kart w talii Kroniki Dziejów.
3. **Ewolucja inteligencji bota przed badaniem balansu:**
   - Heurystyki botów muszą być w pełni nauczone i stabilne przed przystąpieniem do optymalizacji parametrów kart, aby telemetria mierzyła balans gry, a nie błędy sztucznej inteligencji.

---

## 3. Szczegółowe Uzasadnienie (Game Design)
* **Realizm rozgrywki:** Boty symulują graczy średniozaawansowanych, dążących do optymalizacji swoich celów i blokowania lidera stołu.
* **Szybkość:** Silnik symuluje 10 000 partii w kilkanaście sekund, co umożliwia głębokie analizy wielowymiarowe.

---

## 4. Niezmienniki Architektoniczne (Invariants)
* 🛑 **ZAKAZ:** Dostępów botów do ukrytych stanów gry (brak omniscient botów).
* 🛡️ **GWARANCJA:** Decyzje bota wynikają wyłącznie z jawnych reguł i kart na ręce.

---

## 5. Konsekwencje
* Stabilne, wiarygodne zachowanie botów we wszystkich 16 setupach.
