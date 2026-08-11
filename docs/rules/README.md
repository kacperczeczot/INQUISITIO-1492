# Zasady prototypu — INQUISITIO 1492

Playable szkic pod stół **3–5 graczy**.  
GDD: [`../gdd/Inquisitio_1492_GDD.md`](../gdd/Inquisitio_1492_GDD.md) · Roadmap: [`../roadmap.md`](../roadmap.md) · Setupy: [`../../playtesting/setups.md`](../../playtesting/setups.md)

> Prototyp (warstwy A/B/C). Pełny rulebook dla graczy — po sesjach PnP (patrz roadmap).

---

## 1. Komponenty

| Element | Ilość (orient.) | Uwagi |
| :--- | :--- | :--- |
| Plansza 5 lokacji | 1 | Łańcuch + slot Inkwizytora + Areszt w Lochach |
| Planszetka gracza | 1 / gracza | Tor Herezji 0–10, cel frakcji, złoto |
| Talia frakcji | 10 kart / frakcja | Warstwa A używa kart `layer: A` (5 szt.) |
| Agenci | 3 / gracza | Kolor frakcji; nakładka **Podwójny** (B+) |
| Wielki Inkwizytor | 1 figurka | Stany: Patrol / Autodafé |
| Żetony Hak | ~10 | **Jeden typ** |
| Relikwie / Fragmenty / Stosy | wg setupu | Cele narracyjne |
| Złoto | pula | Drugorzędne (koszty kart, łapówki opcjonalne) |
| Talia Czasu | ≥8 | Warstwa C — edykty |

---

## 2. Setup (3–5p)

1. Rozłóż planszę (kolejność lokacji 1→5). Inkwizytor na **Trybunale**, stan **Patrol**.
2. Każdy wybiera frakcję: talia, 3 Agenci, planszetka (Herezja = 0), cel zwycięstwa.
3. Złoto startowe: **3** na gracza.
4. Relikwie / Fragmenty według [`setups.md`](../../playtesting/setups.md).
5. Dobierz **5** kart (Warstwa A: tylko z `layer: A` w talii testowej PnP; pełna gra C: cała talia 10).
6. **Pierwszy gracz:** ustala stół (nie losujcie domyślnie).
7. Talia Czasu: od Ery 1 (C) lub od Ery 2 w skróconym teście.

**Brak.** Gra jest na 3–5 graczy.

---

## 3. Przebieg Ery

| Faza | Nazwa | Co się dzieje |
| :---: | :--- | :--- |
| 0 | Start Ery | Reset limitów anti-AP (Hak / Przesłuchanie / Nasłanie) |
| I | Inkwizytor | Patrol 0–1 lokacji **lub** Autodafé (jeśli wolno) |
| II | Plan / Intryga | Naprzemiennie: zakryta karta pod lokacją + opcjonalny ruch Agenta; Haki (B+) |
| III | Odkrycie | Lokacje 1→5: odkryj karty, efekty, Herezja |
| IV | Lochy | Przesłuchania aresztowanych (B+) |
| V | Dwór | Oskarżenia przy Krytycznej → Werdykt |
| VI | Czystka | Dobór do 5; edykt Talii Czasu (C); przesuń 1. gracza |

---

## 4. Poziom Herezji (ikona)

Tor **0–10** na planszetce.

| Zakres | Strefa | Skutek |
| :---: | :--- | :--- |
| 0–3 | Czysta | Bezpieczniej, słabsze akcje |
| 4–6 | Obserwowana | Ryzyko; Kabała lubi ten pas |
| 7–10 | **Krytyczna** | Inni mogą **Rzucić Oskarżenie** |

**Źródła:** `heresy` karty, `target_heresy` (wrabianie), ujawniony Hak, Autodafé (Agenci w lokacji), wykryty Podwójny, edykty.

→ [`../../game/mechanics/poziom-herezji.md`](../../game/mechanics/poziom-herezji.md)

---

## 5. Wielki Inkwizytor

Figurka NPC. Na Fazie I:

1. **Nasłanie (opcjonalne):** raz na gracza na Erę możesz wskazać kierunek / lokację docelową według reguł frakcji i kart. **Oficjum** ma stałą przewagę: przy konflikcie nasłań wygrywa Oficjum (chyba że karta Signature mówi inaczej).
2. **Patrol:** Inkwizytor przesuwa się o **0 lub 1** lokację wzdłuż łańcucha (domyślnie w stronę wskazaną nasłaniem; bez nasłania — decyzja gracza z najniższą Herezją / 1. gracz przy remisie).
3. **Autodafé** (max **co 2 Ery**): jeśli ogłoszone — w lokacji Inkwizytora każdy obecny Agent daje właścicielowi **+1 Herezja**; połóż **1 Stos** (Oficjum liczy Stosy). Relikwia w lokacji wraca do puli lub spala się (ustalenie setupu: prototyp = wraca do puli).

→ [`../../game/mechanics/wielki-inkwizytor.md`](../../game/mechanics/wielki-inkwizytor.md)

---

## 6. Faza II — Plan / Intryga

Zaczynając od 1. gracza, naprzemiennie aż każdy zagra **2 karty** w tej Erze (przy 5p: 2; przy 3p playtest możesz grać 3 — zanotuj):

1. Zagraj **zakrytą** kartę Akcji pod wybraną lokacją (koszt złota z ręki natychmiast lub przy odkryciu — prototyp: **płać przy zagraniu**).
2. Zastosuj wymagania `location` / `agents` jeśli karta wymaga Agenta w lokacji (sprawdzane przy odkryciu; jeśli brak — karta fizzle, Herezja i tak jeśli zapisana jako koszt gry — prototyp: fizzle bez Herezji).
3. Opcjonalnie: wystaw lub przesuń **1 Agenta** o max 1 lokację (chyba że karta mówi inaczej).
4. **(B+)** Przed lub po swoim zagraniu możesz **wymusić Hak** (1 / Erę) — ofiara spełnia żądanie albo +2 Herezja.

Karty **reakcja** trzymaj w ręce — zagrywasz poza kolejką przy spełnionym warunku.  
**Signature / permanent:** według tekstu karty (C).

---

## 7. Faza III — Odkrycie

Od lokacji **1 → 5**:

1. Odkryj karty w kolejności od 1. gracza wokół stołu.
2. Rozpatrz efekty; dodaj `heresy` zagrywającemu i `target_heresy` wskazanym.
3. Areszty (`arrest`) → Agent do Lochów.
4. Konflikty przestrzeni: więcej Agentów frakcji wygrywa „kontrolę” lokacji przy remisie efektów eliminacji; dalej niższa Herezja.

---

## 8. Warstwa B — Lochy i Haki

### Lochy / Przesłuchanie (1 / gracza / Erę)

Masz dostęp, jeśli masz Agenta w Lochach **lub** kartę dającą dostęp. Wybierz aresztowanego Agenta rywala:

1. **Podwójny** — znacznik na figurce; przy swoim ruchu możesz raz na Erę ruszyć tym Agentem jak swoim **lub** przy Werdykcie dodać +1 głos „w imieniu” właściciela (prototyp: ruch). Wykrycie (karta / Inkwizytor w lokacji z Podwójnym): właściciel **+2 Herezja**, znacznik znika.
2. **Hak** — bierzesz żeton Haka na właściciela.
3. **+2 Herezja** właścicielowi zamiast (1) lub (2).

→ [`../../game/mechanics/lochy-przesluchania.md`](../../game/mechanics/lochy-przesluchania.md)

### Haki (1 typ żetonu)

**Wymuszenie (1 / gracza / Erę):** ogłoś żądanie z listy przykładowej: *nie oskarżaj X / zagłosuj skazać|uniewinnić / przesuń Agenta / nie graj Cienia w lokacji Y / oddaj 1 złoto*. Ofiara spełnia **albo** odmawia → Hak znika, ofiara **+2 Herezja** (cap 10).

→ [`../../game/mechanics/haki.md`](../../game/mechanics/haki.md)

---

## 9. Warstwa A/B/C — Werdykt stołu

Gdy ktoś jest w **Krytycznej**, inny gracz może **Rzucić Oskarżenie** (1× przeciw temu samemu graczowi / Erę):

1. Oskarżyciel ogłasza cel.
2. Każdy **poza oskarżonym** głosuje tajnie lub jawnie (prototyp: **jawnie**): Skazać / Uniewinnić.
3. Remis → Uniewinnienie.
4. **Skazanie:** 1 Agent oskarżonego → **Stos** (eliminacja) **lub** do Lochów +1 Herezja (wybór oskarżyciela; Oficjum zwykle wybiera Stos). Oficjum zapisuje Stos jeśli Agent spłonął.
5. **Uniewinnienie:** oskarżyciel **+1 Herezja**.

To głosowanie stołu: Skazać albo Uniewinnić.

→ [`../../game/mechanics/werdykt-stolu.md`](../../game/mechanics/werdykt-stolu.md)

---

## 10. Warstwa C — Signature i Talia Czasu

- Pełna talia **10** kart / frakcję, w tym Signature (`breaks_rule: true`) — czytaj kartę; łamie wskazaną regułę raz.
- Na końcu Ery (po czystce): odkryj **1** edykt z Talii Czasu (lub wybór z 2 — playtest) obowiązujący następną Erę / natychmiast według tekstu.

---

## 11. Zwycięstwo

Natychmiast, gdy spełnisz warunek frakcji:

| Frakcja | Warunek |
| :--- | :--- |
| Święte Oficjum | **2 Stosy** **lub** **2** skazania Werdyktem rywali, którzy byli w Krytycznej |
| Cienie Al-Andalus | **2 Relikwie** ewakuowane poza planszę; ≥1 z udziałem Podwójnego **lub** ewakuacja bez Autodafé na lokacji wyjścia w tej Erze |
| Korona | **2** zagrane Dekrety signature w grze **oraz** aktywne Haki na **2** różnych graczach |
| Kabała | **3 Fragmenty**; w chwili wygranej Herezja **4–6** |
| Gildia | **2 upadki**: na rywalu publiczny Hak w chwili Upadku **lub** Podwójny pod Twoją kontrolą **lub** jego kluczowa lokacja spalona Autodafé (Pałac/Rynek/Gildia — ustal przy stole: 1 lokacja „klucz” na frakcję) |

**Limit Er (domyślnie 8):** jeśli nikt nie wygrał — wygrywa gracz najbliższy celowi; remis → najniższa Herezja.

---

## 12. Limity anti-AP (zapamiętaj)

Na gracza na Erę: **1** wymuszenie Haka · **1** Przesłuchanie · **1** nasłanie Inkwizytora.  
Autodafé: max **co 2 Ery** (Signature Oficjum może łamać — czytaj kartę).

---

## 13. Teach sheet (1 strona — do PnP)

1. **Herezja** pali Cię publicznie; Krytyczna = można Cię oskarżyć.  
2. **Inkwizytor** chodzi i może spalić lokację (Autodafé).  
3. Zagrywasz **zakryte** karty pod lokacje; potem odkrycie 1→5.  
4. **Werdykt:** stół głosuje Skazać / Uniewinnić.  
5. **(B)** Lochy → Podwójny lub Hak. Hak = spełnij żądanie albo +Herezja.  
6. **(C)** Signature łamią reguły; Talia Czasu zmienia prawo Ery.

---

## 14. Warstwy testowe

| Warstwa | Co jest w grze | Czego nie ma |
| :--- | :--- | :--- |
| **A** | Herezja, Inkwizytor, Werdykt, 5 prostych kart | Haki, Podwójni, Signature |
| **B** | + Lochy, Haki, karty narzędzi | Signature |
| **C** | Pełne 10 + Signature + Talia Czasu | — |
