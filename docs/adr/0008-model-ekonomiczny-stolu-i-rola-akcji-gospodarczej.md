[Strona główna](../../README.md) > [adr](README.md) > [0008-model-ekonomiczny-stolu-i-rola-akcji-gospodarczej](0008-model-ekonomiczny-stolu-i-rola-akcji-gospodarczej.md)

---

# ADR-0008: Model Ekonomiczny Stołu i Rola Akcji Gospodarczej

* **Status:** ACCEPTED
* **Data:** 2026-08-23
* **Autorzy:** Antigravity & Designer
* **Dotyczy:** `sim/inquisitio/engine/`, `game_config.yaml`, `docs/rules/`

---

## 1. Kontekst Problemu
W trakcie iteracji balansu występowało zjawisko „pasa biedy” (blokada gracza przy 0 zł uniemożliwiająca zagranie jakiejkolwiek karty) lub przeciwnie – nadpłynność finansowa (karty dające zbyt duże sumy złota bez żadnego ryzyka taktycznego).

### Dlaczego to wymagało decyzji architektonicznej?
1. **Pasywność vs dynamika kart:** Jeśli zwykła Akcja Gospodarcza daje tyle samo lub więcej niż karta z ręki, karty ekonomiczne stają się bezużyteczne.
2. **Ryzyko paraliżu decyzyjnego:** Gracz bez złota nie może wypaść z gry (deadlock decyzyjny) – musi mieć zawsze dostępną akcję podstawową, która przywraca go do płynności.

---

## 2. Decyzja Projektowa
1. **Dwuakcyjny model tury w Erze:**
   - W każdej erze gracz wykonuje dokładnie 2 Rundy Akcji.
   - W każdej rundzie gracz ma wybór: **Zagranie Karty z Ręki** (płacąc jej koszt w złocie) LUB **Wykonanie Akcji Gospodarczej** (pobranie dochodu bazowego ze stołu, z bonusem na Rynku).
2. **Hierarchia opłacalności kart finansowych:**
   - Karty ekonomiczne muszą oferować wyraźną przewagę taktyczną nad Akcją Gospodarczą (np. większy zysk netto, darmowy ruch agenta, generowanie zagrożenia na rywalu lub manipulację Herezją).
3. **Zasada witalności płynności (Anti-Poverty Target):**
   - Telemetria gry musi utrzymywać globalny wskaźnik Pasu Biedy poniżej akceptowalnego progu tolerancji (docelowo $<8\%$).

---

## 3. Szczegółowe Uzasadnienie (Game Design)
* **Płynność i tempo:** Gracz nigdy nie jest „zablokowany”. Zawsze ma możliwość odbudowania budżetu w ramach Akcji Gospodarczej.
* **Cena czasu:** Wybranie Akcji Gospodarczej kosztuje cenne tempo (gracz nie zagrywa w tej rundzie karty questowej ani ataku), co tworzy naturalny dylemat strategiczny.

---

## 4. Niezmienniki Architektoniczne (Invariants)
* 🛑 **ZAKAZ:** Wprowadzania kart finansowych, które są gorsze lub równe w zysku netto pasywnej Akcji Gospodarczej bez dodatkowego efektu planszowego.
* 🛡️ **GWARANCJA:** Gracz ma zawsze gwarantowaną opcję pozyskania złota w Fazie I bez konieczności posiadania karty na ręce.

---

## 5. Konsekwencje
* Płynność finansowa stołu jest regulowana relacją między kosztami kart a bazowym dochodem w `game_config.yaml`.
* Brak możliwości wystąpienia twardego deadlocku ekonomicznego.
