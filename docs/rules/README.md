# Zasady gry — szkic prototypu (Faza 1)

> Playable paper prototype. Pełny rulebook PL → Faza 4.  
> Komponenty: [`../../game/components/inventory.md`](../../game/components/inventory.md)  
> Plansza: [`../../game/board/locations.md`](../../game/board/locations.md)  
> Planszetka: [`../../game/board/player-board.md`](../../game/board/player-board.md)  
> Setupy playtestowe (2–3p / 4–5p): [`../../playtesting/setups.md`](../../playtesting/setups.md)

## Wartości prototypu

| Parametr | Wartość |
| :--- | :--- |
| Gracze | 2–5 |
| Ręka startowa | **5** (+ **mulligan** do 2 kart) |
| Limit ręki | **5** (dobierz do 5 na koniec Fazy IV) |
| Agenci na frakcję | **3** |
| Złoto startowe | **2** na gracza |
| Próg oskarżenia | **7** (wariant playtest: 8) |
| Relikwie setup | **1** w Lochach + **2** w puli odkrytej obok planszy (reszta zakryta w puli) |
| Wskazówki Kodeksu | pula **6+** żetonów (Kabała zbiera 4) |
| Er / limit czasu | opcjonalnie **6 Er**; wcześniej wygrywa spełnienie Intrygi |
| **Skill > luck** | Talia Czasu = wybór z 2; Szlak Morski otwieralny za złoto; 1. gracz bez kostki |

---

## Setup

Dla wariantów liczby graczy i skróconego 2–3p → [`../../playtesting/setups.md`](../../playtesting/setups.md).

1. Rozłóż planszę 5 lokacji (kolejność 1→5).
2. Każdy gracz wybiera frakcję: talia 10 kart, 3 Agenci, planszetka (Herezja = 0), cel zwycięstwa.
3. Wymieszaj Talię Czasu (8 kart); połóż zakryty stos.
4. Umieść 1 Relikwię w Lochach; 2 Relikwie odkryte w puli; pozostałe zakryte.
5. Każdy dobiera **5** kart; **mulligan:** raz możesz odłożyć do **2** kart na spód talii i dobrać tyle samo.
6. **Pierwszy gracz:** ustalacie przy stole (nie losujcie domyślnie). Propozycja: ten, kto **nie** wybierał frakcji jako pierwszy / kto uczy reguł. Kostka tylko przy remisie decyzji.

---

## Runda = 4 fazy (Era)

### I. Wydarzenie Historyczne (Talia Czasu) — wybór, nie czysty los

1. Odkryj **2** wierzchnie karty Talii Czasu.
2. Wybiera gracz z **najniższym postępem Intrygi** (dogrywka). Remis → aktualny pierwszy gracz.
   - **Postęp przy stole (bez kalkulatora):** % celu frakcji — Oficjum: Stosy÷2 (+ Wpływ÷4); Al-Andalus: (ewakuacje×2 + Relikwie na ręku)÷4; Korona: (Kontrola Pałac+Rynek)÷4; Kabała: Wskazówki÷4; Gildia: unikalne Upadki÷2. Kto ma najmniej — wybiera.
3. Wybrane wydarzenie obowiązuje w tej Erze; **odrzucone** idzie na **spód** talii (wróci później).
4. To jest decyzja polityczna (kogo wspomagasz / blokujesz), nie rzut.

### II. Planowanie Intryg

Zaczynając od pierwszego gracza, **naprzemiennie** (1 karta na turę gracza), aż każdy zagra **2 karty** w tej Erze (w 2-graczu: po 3):

1. Zagraj **zakrytą** kartę Akcji pod wybraną lokacją (slot kart).
2. Opcjonalnie: umieść lub przesuń **1 Agenta** o max 1 lokację (chyba że karta mówi inaczej).
3. **Szlak Morski (skill):** jeśli Szlak zamknięty, gracz z Agentem na Rynku lub w Gildii może **raz na swoją turę** zapłacić **3 złota**, by otworzyć Szlak (nie trzeba czekać na Flotę Kolumba). Flota nadal otwiera Szlak za darmo.

Karty typu **reakcja** zatrzymaj w ręce — zagrywasz je poza kolejką, gdy spełniony warunek.

**Permanent:** zagraj odkryty na swoją planszetkę; zajmuje slot zagrania w tej turze.

### III. Odkrycie i Konfrontacja

Od lokacji **1 → 5**:

1. Odkryj wszystkie karty pod lokacją (kolejność: od pierwszego gracza wokół stołu).
2. Rozpatrz efekty; dodaj Herezję z frontmatter kart (`heresy` / `target_heresy`).
3. **Starcie Agentów** (prototyp): jeśli w lokacji są Agenci ≥ 2 frakcji i ktoś zagrał efekt eliminacji/aresztu — rozpatrz karty najpierw, potem w razie remisu „kontroli przestrzeni” wygrywa gracz z większą liczbą Agentów; przy remisie — gracz z niższą Herezją.
4. Transport Relikwii według kart.

### IV. Sąd Inkwizycyjny & Czyszczenie

1. Sprawdź Tory Herezji. Każdy gracz w strefie Krytycznej (≥ 7) może zostać celem **Rzucenia Oskarżenia** (darmowa reakcja raz na gracza na Erę, chyba że karta mówi inaczej).
2. Rozpatrz Procesy (patrz niżej).
3. Uwolnij Agentów z Lochów według efektów / zapłaty 2 złota (opcjonalnie).
4. Zbierz zasoby jawne lokacji, jeśli masz w nich Agenta i nie zagrałeś Cienia w tej lokacji w Erze (prototyp: +1 złoto z Pałacu/Rynku).
5. Dobierz do limitu ręki **5**. Przesuń znacznik pierwszego gracza w lewo.

---

## Procedura Procesu

Gdy ktoś **Rzuci Oskarżenie** na gracza z Herezją ≥ 7:

1. **Aresztowanie** — 1 Agent oskarżonego z planszy → Lochy (jeśli brak na planszy: +1 Herezji zamiast tego).
2. **Przekupstwo & licytacja** — oskarżony: odrzuć **3** karty **lub** zapłać **5** złota. Nawet przy oczyszczeniu: **konfiskata** 1 żetonu postępu Intrygi. Inni mogą przebijać złotem (Korona).
3. **Wyrok / Autodafé** — jeśli nie oczyszczony: Agent w Lochach idzie na stos (eliminacja). Oficjum zapisuje 1 Stos. Oskarżony: −1 Wpływ / utrata 1 żetonu postępu Intrygi (jeśli ma).

---

## Zwycięstwo

Natychmiast, gdy gracz spełni **warunek Intrygi** swojej frakcji (patrz `game/factions/`).

- **Święte Oficjum:** **2** Stosy — **4 Wpływ Trybunału → 1 Stos** (Wpływ z procesu gdy oskarżasz lub Agent w Trybunale/Lochach).
- **Korona:** ≥**2** żetony Kontroli w **Pałacu** i ≥**2** na **Rynku**.
- **Kabała:** **4** Wskazówek (max 1/Era, strefa Obserwowana).
- **Upadek frakcji (Gildia):** 2 żetony Upadku na różnych rywalach.

**Remis / limit Er:** najwyższy sumaryczny postęp Intrygi (Stosy / Relikwie ewakuowane / Kontrole / Wskazówki / Upadki); remis → najniższa Herezja.

**Presja publiczna (prototyp sim / stół):** na początku Fazy IV gracz z najwyższym postępem Intrygi (≥ ~35% celu) otrzymuje **+1 Herezji** (scrutiny).

---

## Quick reference — 4 fazy

| Faza | Co robisz |
| :---: | :--- |
| **I** | Odkryj Talię Czasu |
| **II** | Zakryte karty pod lokacje + Agenci |
| **III** | Odkryj 1→5, efekty, Herezja, Relikwie |
| **IV** | Oskarżenia, Procesy, dobór do 5 |

**Herezja:** 0–3 czysta · 4–6 obserwowana · **7–10** można oskarżyć
