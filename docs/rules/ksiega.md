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
3. Złoto startowe: **4 zł** na gracza.
4. Relikwie / Fragmenty według [`../../playtesting/setups.md`](../../playtesting/setups.md).
5. Dobierz **5** kart z talii 10 (C).
6. **Pierwszy gracz:** ustala stół (nie losujcie domyślnie).
7. Kronika Dziejów: od Ery 1.

**Brak.** Gra jest na 3–5 graczy.

---

## Suplement II — Przebieg Ery (3 Fazy)

Każda Era w Toledo składa się z 3 następujących po sobie Faz:

| Faza | Nazwa | Co się dzieje przy stole |
| :---: | :--- | :--- |
| **I** | **Intryga** | 2 rundy naprzemiennie: Zagraj zakrytą kartę pod lokację (płać koszt) **LUB** Akcja Gospodarcza (+1 zł); ruch Agenta o 1 / Hak |
| **II** | **Sąd** | 1. Wkroczenie Inkwizytora (Patrol/Autodafé) → 2. Odkrycie kart (1→5) → 3. Lochy → 4. Dwór (Werdykt) |
| **III** | **Kronika & Czystka** | Sprawdzenie zwycięstwa → **Uzupełnienie:** Dobierz karty do limitu **5** + Dochód **+1 złoto** → **Edykt Dziejów** na kolejną Erę → przesuń 1. gracza |

---

### Faza I: Intryga (Działania Graczy)

Zaczynając od 1. gracza, każdy wykonuje naprzemiennie **2 tury akcji** (Runda 1 i Runda 2). W swojej turze wybierasz jedną z dwóch opcji:

* **Opcja A (Zagraj Kartę):** Zagraj **zakrytą** kartę Akcji pod wybraną lokacją (**płać koszt złota przy zagraniu**). Opcjonalnie: wystaw lub przesuń **1 Agenta** o max 1 lokację.
* **Opcja B (Akcja Gospodarcza / Zarobek):** Dobierz **+1 złoto** z banku. Opcjonalnie: wystaw lub przesuń **1 Agenta** o max 1 lokację.

*(B+) Przed lub po swojej akcji możesz wykonać **Wymuszenie Haka (procedura)** (1 / Erę) — ofiara spełnia żądanie albo +2 Herezja.*  
*Karty **Reakcja** trzymaj w ręce — zagrywasz w **oknie reakcji** przy spełnionym warunku.*

→ [Hak](slownik.md#hak) · [`../../game/mechanics/haki.md`](../../game/mechanics/haki.md)

### Faza II: Sąd (Rozstrzygnięcie i Konsekwencje)

W Fazie Sądu rozliczamy skutki intryg w 4 krokach:

#### 1. Wkroczenie Inkwizytora
* **Nasłanie (opcjonalne):** raz na gracza na Erę możesz wskazać kierunek / lokację docelową według reguł frakcji i kart (przy konflikcie wygrywa Oficjum).
* **Patrol:** Inkwizytor przesuwa się o **0 lub 1** lokację wzdłuż krawędzi grafu (domyślnie w stronę nasłania; bez nasłania — gracz z **najniższą Herezją** wybiera; remis → **1. gracz**).
  * **Graf połączeń:** `1 Trybunał` ↔ `2 Pałac`, `3 Lochy` | `2 Pałac` ↔ `1 Trybunał`, `3 Lochy`, `4 Rynek` | `3 Lochy` ↔ `1 Trybunał`, `2 Pałac`, `5 Gildia` | `4 Rynek` ↔ `2 Pałac`, `5 Gildia` | `5 Gildia` ↔ `3 Lochy`, `4 Rynek`.
* **Autodafé (procedura)** (max **co 3 Ery**, pierwsze możliwe od Ery **3**): w lokacji Inkwizytora Agenci rywali w strefie Czystej (0–3) → Areszt w Lochach (+1 Herezja, bez Stosu); w strefie Obserwowanej/Krytycznej (≥4) → Stos (+1 Herezja, +1 Stos dla Oficjum); Relikwia → pula.

→ [`../../game/mechanics/wielki-inkwizytor.md`](../../game/mechanics/wielki-inkwizytor.md)

#### 2. Odkrycie kart (1 → 5)
* Odkryj karty w kolejności od 1. gracza wokół stołu w lokacjach 1→5.
* Rozpatrz efekty; dodaj `heresy` zagrywającemu i `target_heresy` wskazanym.
* Areszty (`arrest`) → Agent do Lochów.

#### 3. Lochy (Przesłuchania)
* **Przesłuchanie (procedura)** — 1 / gracza / Erę dla gracza z Agentem w Lochach. Wybierz uwięzionego Agenta rywala:
  * **Marionetka:** znacznik na figurce (ruch o 1 jak swoim / bez głosu).
  * **Hak:** żeton Haka na właściciela.
  * **+2 Herezja** właścicielowi.

→ [`../../game/mechanics/lochy-przesluchania.md`](../../game/mechanics/lochy-przesluchania.md)

#### 4. Dwór (Oskarżenia i Werdykt)
* Gracz może **Rzucić Oskarżenie** przeciwko rywalowi w **Strefie Krytycznej** (≥7 w 4p, ≥6 w 3p, ≥8 w 5p) → **Werdykt**:
  * Jawne głosowanie stołu: Skazać / Uniewinnić (bez oskarżonego; remis = uniewinnienie).
  * **Skazanie:** 1 Agent oskarżonego → Lochy (+1 Herezja). Unikalne nazwisko na tor **3 Skazania** (każdy oskarżyciel). **Stos** tylko gdy **Oficjum oskarżało** (powtórka na tym samym celu też +1 Stos).
  * **Uniewinnienie:** oskarżyciel +1 Herezja.

→ [`../../game/mechanics/werdykt-stolu.md`](../../game/mechanics/werdykt-stolu.md)

### Faza III: Kronika & Czystka (Koniec Ery)

1. **Zwycięstwo:** Sprawdź natychmiastowe warunki zwycięstwa frakcji.
2. **Uzupełnienie:** Dobierz karty do limitu ręki **5**.
3. **Edykt Dziejów:** Odkryj wierzchnią kartę Kroniki Dziejów (nowe prawo / wydarzenie na nadchodzącą Erę).
4. **Koniec rundy:** Przesuń znacznik 1. gracza & Odnów limity (1 nasłanie, 1 Hak, 1 Przesłuchanie).

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
- Na początku Ery (Faza I: Kronika): odkryj **1** kartę z Kroniki Dziejów.

---

## 4. Zwycięstwo (Kanon 4p)

Natychmiast, gdy spełnisz warunek frakcji:

| Frakcja | Warunek Zwycięstwa (Kanon 4p) |
| :--- | :--- |
| **Święte Oficjum** | **4 Stosy** (spaleni agenci) **lub 3 Skazania** Werdyktem |
| **Cienie Al-Andalus** | **2 Relikwie** + ścieżka (Marionetka / cichy exit / szlak morski) |
| **Korona & Borgiowie** | **2 Dekrety** |
| **Kabała z Toledo** | **3 Fragmenty** + Herezja **≤ 9** (od Ery **6**) |
| **Gildia Cieni** | **4 Upadki** (Hak / Marionetka / Autodafé / Werdykt na celu z Hakiem) |

**Limit Er: 12.** Jeśli nikt nie wygrał — wygrywa gracz najbliższy celowi; remis postępu → **najniższa Herezja**.

→ [Zwycięstwo](slownik.md#zwycięstwo)

---

## 5. Skalowanie Składu (Warianty 2p, 3p i 5p)

Kanonem rozgrywki jest **skład 4-osobowy**. Przy grze w innym gronie wprowadź wyłącznie poniższe modyfikacje:

> ### 👥 Wariant 2-osobowy: „Wojna Cieni” (2x2p — Dual Control)
> Dwóch graczy kontroluje łącznie **4 frakcje** (po 2 frakcje na gracza) z zachowaniem 100% kanonicznych talii i celów:
> 1. **Snake Draft frakcji:** Gracz 1 wybiera 1. frakcję $\rightarrow$ Gracz 2 wybiera 2. i 3. frakcję $\rightarrow$ Gracz 1 dobiera 4. frakcję.
> 2. **Separacja zasobów:** Złoto, karty na ręce, tor Herezji (0–10) i Haki są całkowicie niezależne dla każdej z 4 frakcji (nie wolno ich łączyć ani przekazywać między swoimi frakcjami).
> 3. **Przebieg Fazy Intrygi (Faza I):** Karty zagrywane są naprzemiennie frakcjami: A1 $\rightarrow$ B1 $\rightarrow$ A2 $\rightarrow$ B2 (po 2 rundy = 8 zakrytych kart na stole).
> 4. **Brak auto-agresji:** Twoja frakcja nie może przesłuchiwać (Faza II) ani zakładać Haków na Twoją drugą frakcję.
> 5. **Werdykt (Faza II):** Oskarżona frakcja nie głosuje; głosują pozostałe 2 neutralne frakcje (jedna Gracza A, jedna Gracza B) + oskarżyciel. Do Skazania potrzebna jest przewaga (np. wymuszona Hakiem).
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

Przy zagraniu karty Akcji (Faza I) lub gdy tekst każe „inicjuj”:

1. **Deklaracja** — wskaż kartę i lokację (lub cel wg tekstu).
2. **Koszty** — zapłać złoto / inne koszty **przy zagraniu** (kanon reguł).
3. **Efekt** — przy odkryciu (Faza II) lub natychmiast, jeśli karta mówi inaczej; język efektu: [`../../game/mechanics/leksykon.md`](../../game/mechanics/leksykon.md).

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
| Dochód złota | **+1 zł** w Fazie III (Kronika) + opcja Akcji Gospodarczej (+1 zł w Fazie I) |
| Fiasko (brak lokacji/agentów) | bez Herezji |
| Relikwia przy Autodafé | wraca do puli |
| Werdykt | głosowanie **jawne**; Skazanie (nazwisko) z każdego wyroku; Stos tylko gdy Oficjum oskarżało (także powtórka) |
| Marionetka | tylko ruch (bez głosu) |
| Karty / Erę | **do 2** (zagranie lub Akcja Gospodarcza) |
| Kronika Dziejów | odkryj **1** kartę w Fazie III (nowe prawo na kolejną Erę) |
| Patrol bez nasłania | najniższa Herezja; remis → 1. gracz |
| Limit Er / remis | 9 Er; najbliższy cel, potem najniższa Herezja |
| Lokacje kluczowe Gildii | Oficjum→Trybunał, Korona→Pałac, Cienie→Gildia, Kabała→Lochy, ofiara-Gildia→Rynek |

**Zasada Balansu:** próg oskarżenia wynosi **6** dla 3p, **7** dla 4p, **8** dla 5p (zatwierdzone w raportach sim-reports).
