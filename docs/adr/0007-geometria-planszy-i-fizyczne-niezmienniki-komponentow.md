[Strona główna](../../README.md) > [adr](README.md) > [0007-geometria-planszy-i-fizyczne-niezmienniki-komponentow](0007-geometria-planszy-i-fizyczne-niezmienniki-komponentow.md)

---

# ADR-0007: Geometria Planszy i Fizyczne Niezmienniki Komponentów

* **Status:** ACCEPTED
* **Data:** 2026-08-23
* **Autorzy:** Antigravity & Designer
* **Dotyczy:** `sim/inquisitio/engine/`, `game_config.yaml`, `docs/rules/`, `docs/gdd/`

---

## 1. Kontekst Problemu
W procesie optymalizacji i kalibracji balansu botów pojawiały się pokusy manipulowania liczbą pionów gracza, limitami ręki czy dodawaniem dynamicznych pól w zależności od liczby graczy (np. 4 agenci w 5p, 2 agenci w 3p).

### Dlaczego to było wadliwe?
1. **Naruszenie fizycznej geometrii pudełka:** Zmiana liczby fizycznych komponentów na gracza destabilizuje balans przestrzenny planszy (zagęszczenie w lokacjach).
2. **Utrata tożsamości mechanicznej:** 3 agenci na gracza stanowią optymalny trójkąt decyzyjny (np. 1 agent w Portach, 1 w Lochach/Trybunale, 1 mobilny).
3. **Zaburzenie skalowania:** Gra powinna skalować się naturalnie poprzez zagęszczenie agentów na tych samych 5 lokacjach, a nie zmianę puli pionków.

---

## 2. Decyzja Projektowa
1. **Fizyczna niezmienność komponentów:**
   - Każda frakcja dysponuje dokładnie **stałą liczbą Agentów** na planszy (wartość bazowa w SSOT: 3).
   - Plansza posiada dokładnie **5 stałych Lokacji**: Trybunał Inkwizycji, Lochy, Katedra, Rynek oraz Gildia Kupiecka.
   - Pula kart frakcyjnych w talii wynosi dokładnie **12 unikalnych kart**.
2. **Zunifikowane zasady wejścia:**
   - Złoto startowe oraz limit kart na ręce są zunifikowane dla stołu i podlegają globalnej kalibracji w SSOT.
3. **Skalowanie:**
   - Trudność manewrowania i ryzyko aresztowania rosną naturalnie wraz z liczbą graczy (więcej agentów na 5 polach planszy), co odzwierciedla ciasnotę polityczną Toledo w 1492 roku.

---

## 3. Szczegółowe Uzasadnienie (Game Design)
* **Logistyka przestrzenna:** Posiadanie stałej liczby 3 agentów wymusza na graczach trudne wybory: obrona własnej pozycji vs infiltracja rywala vs ucieczka przed Inkwizytorem.
* **Przejrzystość stołu:** Gracze widzą i kontrolują dokładnie tę samą pulę zasobów fizycznych niezależnie od setupu.

---

## 4. Niezmienniki Architektoniczne (Invariants)
* 🛑 **ZAKAZ:** Modyfikowania liczby agentów na gracza w zależności od setupu lub liczby graczy (zakaz wyjątków `agents_3p`, `agents_5p`).
* 🛑 **ZAKAZ:** Tworzenia dynamicznych lokacji na planszy w silniku symulacji bez formalnego rozszerzenia GDD.
* 🛡️ **GWARANCJA:** Plansza zawsze składa się z 5 kanonicznych lokacji, a Inkwizytor porusza się w ramach tej samej topologii grafu.

---

## 5. Konsekwencje
* Silnik symulacji używa stałej struktury grafu lokacji i stałej liczby agentów.
* Wszelkie dostrajanie balansu odbywa się poprzez koszty akcji, ruchy i efekty kart, a nie modyfikację liczby pionków.
