# INQUISITIO-1492 — Księga Zasad

> *„Toledo, Rok Pański 1492. Grenada upadła, a na starym moście Alcántara spotykają się ci, którzy wierzą w ogień, ci, którzy uciekają z relikwiami, mędrcy składający zakazany kodeks i królewscy poborcy. W tym mieście nikt nie jest bez winy — chodzi jedynie o to, kto spłonie pierwszy.”*

---

## Złote prawa stołu

1. **Prawo Trybunału** — `ksiega` + `slownik` > teach > GDD / notatki.
2. **Edykt karty** — tekst karty (`Łamie regułę …`) > księga / teach.
3. **Zasada delty** — karta pisze tylko deltę; procedury bazowe są tutaj i w `game/mechanics/`.
4. **Wyrok surowy** — brak zapisu / konflikt kolejności → na niekorzyść gracza, który najbardziej zyskuje; remis korzyści → wyższa Herezja przegrywa spór; graj dalej.

---

## 1. Komponenty

| Element | Ilość (orient.) | Uwagi |
| :--- | :--- | :--- |
| Plansza 5 lokacji | 1 | Graf sąsiedztwa + slot Inkwizytora + Areszt w Lochach |
| Planszetka gracza | 1 / gracza | Tor Herezji 0–10, cel frakcji, złoto |
| Talia frakcji | 10 kart / frakcja | Pełna talia C na stole |
| Agenci | 3 / gracza | Kolor frakcji; nakładka **Marionetka** |
| Wielki Inkwizytor | 1 figurka | Stany: Patrol / Autodafé |
| Żetony Hak | ~10 | **Jeden typ** |
| Relikwie / Fragmenty / Stosy | wg setupu | Cele narracyjne |
| Złoto | pula | Koszty kart, łapówki |
| Kronika Dziejów | ≥8 | Edykty |

→ [`../../game/components/inventory.md`](../../game/components/inventory.md)

---

## Suplement III — Setup (3–5p)

1. Rozłóż planszę (kolejność lokacji 1→5). Inkwizytor na **Trybunale**, stan **Patrol**.
2. Każdy wybiera frakcję: talia, 3 Agenci, planszetka (Herezja = 0), cel zwycięstwa.
3. Złoto startowe: **3 zł** na gracza (w 5p: **2 zł**).
4. Relikwie / Fragmenty według [`../../playtesting/setups.md`](../../playtesting/setups.md).
5. Dobierz **5** kart z talii 10 (C).
6. **Pierwszy gracz:** ustala stół (nie losujcie domyślnie).
7. Kronika Dziejów: od Ery 1.

**Brak.** Gra jest na 3–5 graczy.

---

## Suplement II — Przebieg Ery (E.0–E.VI)

Wydarzenia ramowe są **obowiązkowe**. **Okno reakcji** — opcjonalne karty typu Reakcja przy spełnionym warunku (poza kolejką).

| Krok | Nazwa (faza) | Co się dzieje |
| :---: | :--- | :--- |
| **E.0** | Start Ery | Reset limitów anti-AP (Hak / Przesłuchanie / Nasłanie) |
| **E.I** | Inkwizytor | Patrol 0–1 lokacji **lub** Autodafé (jeśli wolno) |
| **E.II** | Plan / Intryga | Naprzemiennie: zakryta karta pod lokacją + opcjonalny ruch Agenta; Haki (B+) |
| **E.III** | Odkrycie | Lokacje 1→5: odkryj karty, efekty, Herezja |
| **E.IV** | Lochy | Przesłuchania aresztowanych (B+) |
| **E.V** | Dwór | Oskarżenia przy Krytycznej → Werdykt |
| **E.VI** | Czystka | Dobór do 5; edykt Talii Czasu (C); przesuń 1. gracza |

### E.I — Inkwizytor (faza)

1. **Nasłanie (opcjonalne):** raz na gracza na Erę możesz wskazać kierunek / lokację docelową według reguł frakcji i kart. **Oficjum** ma stałą przewagę: przy konflikcie nasłań wygrywa Oficjum (chyba że karta specjalna mówi inaczej).
2. **Patrol:** Inkwizytor przesuwa się o **0 lub 1** lokację wzdłuż **krawędzi grafu** (domyślnie jeden krok po najkrótszej ścieżce w stronę nasłania; **bez nasłania** — gracz z **najniższą Herezją** wybiera; remis → **1. gracz**).
   * **Połączenia miejskie (graf):**  
     * `1 Trybunał` ↔ `2 Pałac`, `3 Lochy`  
     * `2 Pałac` ↔ `1 Trybunał`, `3 Lochy`, `4 Rynek`  
     * `3 Lochy` ↔ `1 Trybunał`, `2 Pałac`, `5 Gildia`  
     * `4 Rynek` ↔ `2 Pałac`, `5 Gildia`  
     * `5 Gildia` ↔ `3 Lochy`, `4 Rynek`
3. **Autodafé (procedura)** (max **co 3 Ery**): jeśli **Ogłoś** — w lokacji Inkwizytora: każdy obecny Agent rywala w strefie **Czystej (0–3 Herezji)** → trafia do **Aresztu w Lochach** (+1 Herezja dla właściciela, bez Stosu); w strefie **Obserwowanej lub Krytycznej (≥4 Herezji)** → **spalony na Stosie** (+1 Herezja dla właściciela, **+1 Stos** dla Oficjum); Relikwia → pula. **Wymuś Autodafé** (edykt) = to samo **bez** Stosu.

→ [`../../game/mechanics/wielki-inkwizytor.md`](../../game/mechanics/wielki-inkwizytor.md) · hasło: [Inkwizytor](slownik.md#inkwizytor), [Autodafé](slownik.md#autodafé)

### E.II — Plan / Intryga (faza)

Zaczynając od 1. gracza, każdy wykonuje naprzemiennie **2 tury**. W swojej turze zagrywasz **zakrytą** kartę Akcji (płacąc jej koszt) **albo pasujesz**:

1. **E.II.1** Na początek swojej tury: otrzymaj **+1 złoto** (dopływ złota).
2. **E.II.2** Zagraj **zakrytą** kartę Akcji pod wybraną lokacją (**płać złoto przy zagraniu**). → [Inicjacja karty](#suplement-i--inicjacja-karty--zdolności)
3. Zastosuj wymagania `location` / `agents` jeśli karta wymaga Agenta w lokacji (sprawdzane przy odkryciu; jeśli brak — karta **ponosi fiasko bez Herezji**, chyba że tekst karty mówi inaczej).
4. Opcjonalnie: wystaw lub przesuń **1 Agenta** o max 1 lokację (chyba że karta mówi inaczej).
5. **(B+)** Przed lub po swoim zagraniu możesz wykonać **Wymuszenie Haka (procedura)** (1 / Erę) — ofiara spełnia żądanie albo +2 Herezja.

Karty **Reakcja** trzymaj w ręce — zagrywasz w **oknie reakcji** przy spełnionym warunku.  
**Karta specjalna / permanent:** według tekstu karty (C).

→ [Hak](slownik.md#hak) · [`../../game/mechanics/haki.md`](../../game/mechanics/haki.md)

### E.III — Odkrycie (faza)

Od lokacji **1 → 5**:

1. Odkryj karty w kolejności od 1. gracza wokół stołu.
2. Rozpatrz efekty; dodaj `heresy` zagrywającemu i `target_heresy` wskazanym.
3. Areszty (`arrest`) → Agent do Lochów.
4. Konflikty przestrzeni: więcej Agentów frakcji wygrywa „kontrolę” lokacji przy remisie efektów eliminacji; dalej niższa Herezja.

### E.IV — Lochy (faza)

**Przesłuchanie (procedura)** — 1 / gracza / Erę. Dostęp: Agent w Lochach **lub** karta dająca dostęp. Wybierz aresztowanego Agenta rywala:

1. **Marionetka** — znacznik na figurce; raz na Erę możesz ruszyć tym Agentem o 1 jak swoim (należy kolorem do właściciela; **bez** dodatkowego głosu przy Werdykcie). Wykrycie (karta / Inkwizytor w lokacji z Marionetką): właściciel **+2 Herezja**, znacznik znika.
2. **Hak** — bierzesz żeton Haka na właściciela.
3. **+2 Herezja** właścicielowi zamiast (1) lub (2).

→ [`../../game/mechanics/lochy-przesluchania.md`](../../game/mechanics/lochy-przesluchania.md)

### E.V — Dwór (faza)

Gdy ktoś jest w **Krytycznej**, inny gracz może **Rzucić Oskarżenie** (1× przeciw temu samemu graczowi / Erę) → **Werdykt (procedura)**:

1. Oskarżyciel ogłasza cel.
2. Każdy **poza oskarżonym** głosuje **jawnie**: Skazać / Uniewinnić.
3. Remis → Uniewinnienie.
4. **Skazanie:** 1 Agent oskarżonego → **Stos** (eliminacja) **lub** do Lochów +1 Herezja (wybór oskarżyciela; Oficjum zwykle wybiera Stos). Oficjum zapisuje Stos jeśli Agent spłonął.
5. **Uniewinnienie:** oskarżyciel **+1 Herezja**.

→ [`../../game/mechanics/werdykt-stolu.md`](../../game/mechanics/werdykt-stolu.md)

### E.VI — Czystka (faza)

1. Dobierz karty do limitu ręki **5**.
2. Odkryj **1** edykt z Talii Czasu (C) — obowiązuje następną Erę / natychmiast według tekstu.
3. Przesuń znacznik 1. gracza.

---

## 2. Herezja (skrót)

Tor **0–10** na planszetce.

| Zakres | Strefa | Skutek |
| :---: | :--- | :--- |
| 0–3 | Czysta | Bezpieczniej, słabsze akcje |
| 4–6 | Obserwowana | Ryzyko; Kabała lubi ten pas |
| ≥7 | **Krytyczna** | Inni mogą **Rzucić Oskarżenie** |

**Źródła:** `heresy` karty, `target_heresy`, ujawniony Hak, Autodafé, wykryta Marionetka, edykty.

→ [`../../game/mechanics/poziom-herezji.md`](../../game/mechanics/poziom-herezji.md) · [Herezja](slownik.md#herezja)

---

## 3. Karty specjalne i Kronika Dziejów

- Pełna talia **10** kart / frakcję, w tym karta specjalna (`breaks_rule: true`) — czytaj kartę; łamie wskazaną regułę raz.
- Na końcu Ery (E.VI): odkryj **1** edykt z Kroniki Dziejów.

---

## 4. Zwycięstwo (Kanon 4p)

Natychmiast, gdy spełnisz warunek frakcji:

| Frakcja | Warunek Zwycięstwa (Kanon 4p) |
| :--- | :--- |
| **Święte Oficjum** | **4 Stosy** (spaleni agenci) **lub 2 Skazania** Werdyktem |
| **Cienie Al-Andalus** | **2 Relikwie** + ścieżka (Marionetka / cichy exit / szlak morski / Era 5+) |
| **Korona & Borgiowie** | **2 Dekrety** (od Ery **5**) |
| **Kabała z Toledo** | **3 Fragmenty** + Herezja **3–8** (od Ery **6**) |
| **Gildia Cieni** | **2 Upadki** (Hak / Marionetka / Autodafé / Werdykt na celu z Hakiem); **3** gdy brak Oficjum |

**Limit Er: 10.** Jeśli nikt nie wygrał — wygrywa gracz najbliższy celowi; remis postępu → **najniższa Herezja**.

→ [Zwycięstwo](slownik.md#zwycięstwo)

---

## 5. Skalowanie Składu (Warianty 2p, 3p i 5p)

Kanonem rozgrywki jest **skład 4-osobowy**. Przy grze w innym gronie wprowadź wyłącznie poniższe modyfikacje:

> ### 👥 Wariant 2-osobowy: „Wojna Cieni” (2x2p — Dual Control)
> Dwóch graczy kontroluje łącznie **4 frakcje** (po 2 frakcje na gracza) z zachowaniem 100% kanonicznych talii i celów:
> 1. **Snake Draft frakcji:** Gracz 1 wybiera 1. frakcję $\rightarrow$ Gracz 2 wybiera 2. i 3. frakcję $\rightarrow$ Gracz 1 dobiera 4. frakcję.
> 2. **Separacja zasobów:** Złoto, karty na ręce, tor Herezji (0–10) i Haki są całkowicie niezależne dla każdej z 4 frakcji (nie wolno ich łączyć ani przekazywać między swoimi frakcjami).
> 3. **Przebieg Fazy Planu (E.II):** Karty zagrywane są naprzemiennie frakcjami: A1 $\rightarrow$ B1 $\rightarrow$ A2 $\rightarrow$ B2 (po 2 rundy = 8 zakrytych kart na stole).
> 4. **Brak auto-agresji:** Twoja frakcja nie może przesłuchiwać (E.IV) ani zakładać Haków na Twoją drugą frakcję.
> 5. **Werdykt (E.V):** Oskarżona frakcja nie głosuje; głosują pozostałe 2 neutralne frakcje (jedna Gracza A, jedna Gracza B) + oskarżyciel. Do Skazania potrzebna jest przewaga (np. wymuszona Hakiem).
> 6. **Długość gry:** Limit Er wynosi **12 Er** (Kronika Dziejów: 12 kart lub przetasowanie w Erze 10).
> 7. **Podwójne Zwycięstwo:** Wygrywa gracz, którego **OBIE frakcje** jednocześnie spełnią swoje pełne cele kanoniczne.
>    * *Tie-breaker po 12. Erze:* 1 zrealizowany cel + postęp 2. frakcji $\rightarrow$ niższa suma Herezji obu frakcji $\rightarrow$ wyższa łączna suma złota.
>
> ### 👥 Modyfikacje dla 3 Graczy (3p):
> - **Próg Oskarżenia (Krytyczna Herezja):** **`6`** (Strefy: Czysta `0–3` / Obserwowana `4–5` / Krytyczna `≥6`).
> - **Święte Oficjum:** Wymaga **`3 Stosów`** (zamiast 4).
> - **Kabała z Toledo:** Może wygrać od **`Ery 7`** (zamiast 6).
>
> ### 👥 Modyfikacje dla 5 Graczy (5p):
> - **Złoto Startowe:** Każdy gracz otrzymuje na start **`2 zł`** (zamiast 3 zł).
> - **Próg Oskarżenia (Krytyczna Herezja):** **`8`** (Strefy: Czysta `0–3` / Obserwowana `4–7` / Krytyczna `≥8`).

---

## 6. Limity anti-AP (zapamiętaj)

Na gracza na Erę: **1** wymuszenie Haka · **1** Przesłuchanie · **1** nasłanie Inkwizytora.  
Autodafé: max **co 3 Ery** (karta specjalna Oficjum może łamać — czytaj kartę).  
Karty / Erę: **2**.

---

## Suplement I — Inicjacja karty / zdolności

Przy zagraniu karty Akcji (E.II) lub gdy tekst każe „inicjuj”:

1. **Deklaracja** — wskaż kartę i lokację (lub cel wg tekstu).
2. **Koszty** — zapłać złoto / inne koszty **przy zagraniu** (kanon reguł).
3. **Efekt** — przy odkryciu (E.III) lub natychmiast, jeśli karta mówi inaczej; język efektu: [`../../game/mechanics/leksykon.md`](../../game/mechanics/leksykon.md).

Jeśli wymagania `location` / `agents` nie są spełnione przy rozpatrzeniu → **fiasko** bez Herezji (chyba że karta mówi inaczej).

---

## Suplement IV — Anatomia karty

Kolejność czytania przy stole:

1. **Typ** (Akcja / Reakcja / Specjalna / …) — badge.
2. **Koszt** (złoto, warunki).
3. **`effect`** — komendy z leksykonu; etykiety `Limit:`, `Łamie regułę`, `EDYKT`.
4. **Pigułka Herezji** (`heresy` / `target_heresy`).
5. **`lore` / `heresy_text`** — **zero mechaniki**; nie wchodzą w interakcję z grą.

Kanon pól: [`../../game/cards/SCHEMA.md`](../../game/cards/SCHEMA.md).

---

## 6. Prawomocność reguł (Kanon stołu)

Prawomocne reguły kanoniczne:

| Reguła | Kanon |
| :--- | :--- |
| Płatność złota | przy zagraniu |
| Dopływ złota | **+1** na początek swojej tury (E.II) |
| Fiasko (brak lokacji/agentów) | bez Herezji |
| Relikwia przy Autodafé | wraca do puli |
| Werdykt | głosowanie **jawne** (na 4–5p Stos dla Oficjum tylko gdy Oficjum oskarżało) |
| Marionetka | tylko ruch (bez głosu) |
| Karty / Erę | **do 2** (zagranie lub pas) |
| Kronika Dziejów | odkryj **1** edykt |
| Patrol bez nasłania | najniższa Herezja; remis → 1. gracz |
| Limit Er / remis | 9 Er; najbliższy cel, potem najniższa Herezja |
| Lokacje kluczowe Gildii | Oficjum→Trybunał, Korona→Pałac, Cienie→Gildia, Kabała→Lochy, ofiara-Gildia→Rynek |

**Zasada Balansu:** próg oskarżenia wynosi **6** dla 3p, **7** dla 4p, **8** dla 5p (zatwierdzone w raportach sim-reports).
