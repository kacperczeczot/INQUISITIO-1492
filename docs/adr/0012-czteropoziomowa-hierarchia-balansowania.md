# ADR-0012: Czteropoziomowa Hierarchia Balansowania (L1-L4 Invariant)

* **Status:** ACCEPTED
* **Data:** 2026-08-23
* **Autorzy:** Antigravity & Designer
* **Dotyczy:** `tools/sim/`, `game_config.yaml`, `docs/rules/hierarchia_balansowania.md`

---

## 1. Kontekst Problemu
Podczas wczesnych iteracji balansu asystent próbował naprawiać globalne anomalie rozgrywki poprzez chaotyczne mikro-korekty dziesiątek pojedynczych kart jednocześnie. Prowadziło to do przeuczenia (overfittingu), zniszczenia tożsamości talii i niestabilności telemetrii.

---

## 2. Decyzja Projektowa
1. **Bezwzględna Hierarchia Poziomów Balansowania:**
   - **Poziom 1 (L1 — Parametry Systemowe Stołu):** Złoto startowe, liczba agentów, limit ręki, progi Herezji (obserwowana/krytyczna), cooldown Autodafé.
   - **Poziom 2 (L2 — Warunki Zwycięstwa Frakcji):** Progi questowe (Dekrety, Relikwie, Fragmenty, Stosy/Skazania, Upadki).
   - **Poziom 3 (L3 — Parametry Kart):** Koszty złota, przyrost/spadek Herezji, zyski zasobów, zasięgi i warunki aktywacji.
   - **Poziom 4 (L4 — Zegar i Wydarzenia):** Częstotliwość i siła Edyktów Kroniki Dziejów (Time Deck).
2. **Zasada Priorytetu Wyższego Poziomu:**
   - Kategorycznie zabrania się wprowadzania masowych zmian na poziomie niższym (L3 — pojedyncze karty), jeśli problem balansu można rozwiązać elegancką, pojedynczą korektą na poziomie wyższym (L1/L2).

---

## 3. Szczegółowe Uzasadnienie (Game Design)
* **Stabilność modelu:** Zmiany makro (L1/L2) wpływają równomiernie na cały ekosystem stołu, zachowując spójność matematyczną.
* **Ochrona tożsamości kart:** Karty zachowują swój unikalny charakter zamiast być nieustannie modyfikowane w oderwaniu od reguł ogólnych.

---

## 4. Niezmienniki Architektoniczne (Invariants)
* 🛑 **ZAKAZ:** Modyfikacji parametrów kart (L3) przed upewnieniem się, że poziomy L1 i L2 są poprawnie skalibrowane.
* 🛡️ **GWARANCJA:** Audytor kanonu optymalizuje parametry w ścisłym porządku hierarchicznym L1 $\to$ L2 $\to$ L3 $\to$ L4.

---

## 5. Konsekwencje
* Wszelkie procedury audytu przestrzegają hierarchii poziomów.
* Zmniejszono liczbę chaotycznych mikro-edycji w pliku `game_config.yaml`.
