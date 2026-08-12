[Strona główna](../../README.md) > [Dokumentacja](../README.md) > [Zasady](README.md)

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
| Agenci | 3 / gracza | Kolor frakcji; nakładka **Podwójny** |
| Wielki Inkwizytor | 1 figurka | Stany: Patrol / Autodafé |
| Żetony Hak | ~10 | **Jeden typ** |
| Relikwie / Fragmenty / Stosy | wg setupu | Cele narracyjne |
| Złoto | pula | Koszty kart, łapówki |
| Talia Czasu | ≥8 | Edykty |

→ [`../../game/components/inventory.md`](../../game/components/inventory.md)

---

## Suplement III — Setup (3–5p)

1. Rozłóż planszę (kolejność lokacji 1→5). Inkwizytor na **Trybunale**, stan **Patrol**.
2. Każdy wybiera frakcję: talia, 3 Agenci, planszetka (Herezja = 0), cel zwycięstwa.
3. Złoto startowe: **3** na gracza.
4. Relikwie / Fragmenty według [`../../playtesting/setups.md`](../../playtesting/setups.md).
5. Dobierz **5** kart z talii 10 (C).
6. **Pierwszy gracz:** ustala stół (nie losujcie domyślnie).
7. Talia Czasu: od Ery 1.

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
2. **Patrol:** Inkwizytor przesuwa się o **0 lub 1** lokację wzdłuż **krawędzi grafu** (domyślnie jeden krok po najkrótszej ścieżce w stronę nasłania; **bez nasłania** — gracz z **najniższą Herezją** wybiera; remis → **1. gracz**). Sąsiedztwo: [`../../game/board/locations.md`](../../game/board/locations.md).
3. **Autodafé (procedura)** (max **co 2 Ery**): jeśli **Ogłoś** — w lokacji Inkwizytora każdy obecny Agent → właściciel **+1 Herezja**; połóż **1 Stos**; Relikwia → pula. **Wymuś Autodafé** (edykt) = to samo **bez** Stosu.

→ [`../../game/mechanics/wielki-inkwizytor.md`](../../game/mechanics/wielki-inkwizytor.md) · hasło: [Inkwizytor](slownik.md#inkwizytor), [Autodafé](slownik.md#autodafé)

### E.II — Plan / Intryga (faza)

Zaczynając od 1. gracza, naprzemiennie aż każdy zagra **2 karty** w tej Erze (także przy 3p i 5p):

1. **E.II.1** Na początek swojej tury: otrzymaj **+1 złoto** (trickle).
2. **E.II.2** Zagraj **zakrytą** kartę Akcji pod wybraną lokacją (**płać złoto przy zagraniu**). → [Inicjacja karty](#suplement-i--inicjacja-karty--zdolności)
3. Zastosuj wymagania `location` / `agents` jeśli karta wymaga Agenta w lokacji (sprawdzane przy odkryciu; jeśli brak — karta **fizzle bez Herezji**, chyba że tekst karty mówi inaczej).
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

1. **Podwójny** — znacznik na figurce; raz na Erę możesz ruszyć tym Agentem o 1 jak swoim (należy kolorem do właściciela; **bez** dodatkowego głosu przy Werdykcie). Wykrycie (karta / Inkwizytor w lokacji z Podwójnym): właściciel **+2 Herezja**, znacznik znika.
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
| 7–10 | **Krytyczna** | Inni mogą **Rzucić Oskarżenie** |

**Źródła:** `heresy` karty, `target_heresy`, ujawniony Hak, Autodafé, wykryty Podwójny, edykty.

→ [`../../game/mechanics/poziom-herezji.md`](../../game/mechanics/poziom-herezji.md) · [Herezja](slownik.md#herezja)

---

## 3. Karty specjalne i Talia Czasu

- Pełna talia **10** kart / frakcję, w tym karta specjalna (`breaks_rule: true`) — czytaj kartę; łamie wskazaną regułę raz.
- Na końcu Ery (E.VI): odkryj **1** edykt z Talii Czasu.

---

## 4. Zwycięstwo

Natychmiast, gdy spełnisz warunek frakcji:

| Frakcja | Warunek (C — stół) |
| :--- | :--- |
| Święte Oficjum | **3 Stosy** **lub** skazania Werdyktem (**2** przy ≤3p, **3** przy 4–5p) |
| Cienie Al-Andalus | **2 Relikwie** + ścieżka (Podwójny / cichy exit / szlak morski) |
| Korona | **2** Dekrety + ≥1 Hak (od Ery **7**@3p / **6**@4–5p); na **5p** też 1 Dekret + 2 Haki od Ery 6 |
| Kabała | **3 Fragmenty** + Herezja **4–6** (od Ery **7**@3p / **6**@4p / **5**@5p) |
| Gildia | **2 upadki** (Hak / Podwójny / Autodafé lokacji kluczowej / Werdykt na celu z Hakiem); **3** gdy brak Oficjum |

Sim teach (A/B): inne progi / tie-break — nie drukuj osobno; szczegóły w silniku.

**Limit Er: 8.** Jeśli nikt nie wygrał — wygrywa gracz najbliższy celowi; remis postępu → **najniższa Herezja**.

→ [Zwycięstwo](slownik.md#zwycięstwo)

---

## 5. Limity anti-AP (zapamiętaj)

Na gracza na Erę: **1** wymuszenie Haka · **1** Przesłuchanie · **1** nasłanie Inkwizytora.  
Autodafé: max **co 2 Ery** (karta specjalna Oficjum może łamać — czytaj kartę).  
Karty / Erę: **2**.

---

## Suplement I — Inicjacja karty / zdolności

Przy zagraniu karty Akcji (E.II) lub gdy tekst każe „inicjuj”:

1. **Deklaracja** — wskaż kartę i lokację (lub cel wg tekstu).
2. **Koszty** — zapłać złoto / inne koszty **przy zagraniu** (freeze).
3. **Efekt** — przy odkryciu (E.III) lub natychmiast, jeśli karta mówi inaczej; język efektu: [`../../game/mechanics/leksykon.md`](../../game/mechanics/leksykon.md).

Jeśli wymagania `location` / `agents` nie są spełnione przy rozpatrzeniu → **fizzle** bez Herezji (chyba że karta mówi inaczej).

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

## 6. Freeze prototypu (offline)

Zamrożone reguły (bez „ustal przy stole”):

| Reguła | Freeze |
| :--- | :--- |
| Płatność złota | przy zagraniu |
| Trickle złota | **+1** na początek swojej tury (E.II) |
| Fizzle (brak lokacji/agentów) | bez Herezji |
| Relikwia przy Autodafé | wraca do puli |
| Werdykt | głosowanie **jawne** |
| Podwójny | tylko ruch (bez głosu) |
| Karty / Erę | **2** (3–5p) |
| Talia Czasu | odkryj **1** edykt |
| Patrol bez nasłania | najniższa Herezja; remis → 1. gracz |
| Limit Er / remis | 8 Er; najbliższy cel, potem najniższa Herezja |
| Lokacje kluczowe Gildii | Oficjum→Trybunał, Korona→Pałac, Cienie→Gildia, Kabała→Lochy, ofiara-Gildia→Rynek |

**Otwarte do playtestu:** próg oskarżenia **7 vs 8** ([`../../playtesting/balance-notes.md`](../../playtesting/balance-notes.md)).
