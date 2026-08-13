[Strona główna](../../README.md) > [Dokumentacja](../README.md) > [Zasady](README.md)

---

## Agent

Figurka frakcji na planszy (3 / gracza). Porusza się o max 1 krawędź grafu na turę Planu (chyba że karta mówi inaczej). Kontroluje lokacje, wchodzi w Autodafé, areszt i Werdykt.

**Patrz także:** [Lokacja](#lokacja), [Podwójny](#podwójny), [Areszt](#areszt)

---

## Areszt

Stan Agenta w strefie Areszt lokacji **Lochy**. Agent nie porusza się i nie kontroluje lokacji, dopóki nie wróci. Źródła: `arrest` na karcie, Werdykt, edykt / Autodafé wg tekstu.

**Patrz także:** [Lochy](#lochy), [Przesłuchanie](#przesłuchanie) · [`../../game/mechanics/lochy-przesluchania.md`](../../game/mechanics/lochy-przesluchania.md)

---

## Autodafé (procedura)

Czystka lokacji Inkwizytora: Agent rywala w strefie **Czystej (0–3 Herezji)** → do **Aresztu w Lochach** (+1 Herezja, bez Stosu); w strefie **Obserwowanej / Krytycznej (≥4 Herezji)** → **spalenie na Stosie** (+1 Herezja, +1 Stos dla Oficjum). Relikwia w lokacji wraca do puli. Max **co 2 Ery** (bazowo).  
**Ogłoś Autodafé** → Stos przy rywalu ≥4 Herezji. **Wymuś Autodafé** (edykt) → **bez** Stosu.

**Patrz także:** [Inkwizytor](#inkwizytor), [Stos](#stos) · [`../../game/mechanics/wielki-inkwizytor.md`](../../game/mechanics/wielki-inkwizytor.md) · leksykon **Ogłoś** / **Wymuś**

---

## Czystka (faza)

**E.VI:** dobór do ręki 5; odkryj 1 edykt Talii Czasu; przesuń 1. gracza.

**Patrz także:** [Talia Czasu](#talia-czasu), [Era](#era) · [`ksiega.md`](ksiega.md)

---

## Dekret

Cel / znacznik Korony (i karty Korony). Warunek zwycięstwa: zwykle 2 Dekrety + ≥1 Hak (progi Er wg liczby graczy).

**Patrz także:** [Zwycięstwo](#zwycięstwo), [Hak](#hak)

---

## Edykt

Karta Talii Czasu lub efekt zmieniający prawo Ery. Odkrywany w **E.VI** (1 / Erę). Tekst edyktu obowiązuje według karty.

**Patrz także:** [Talia Czasu](#talia-czasu), [Edykt karty](#edykt-karty)

---

## Edykt karty

**Złote prawo:** tekst karty (`Łamie regułę …` / `breaks_rule`) wygrywa z księgą i teach.

**Patrz także:** [Złote prawa](#złote-prawa), [Karty (typy)](#karty-typy)

---

## Era

Jedna pełna pętla wydarzeń ramowych **E.0–E.VI**. Limit gry: **8** Er (potem remis postępu → najbliższy celowi, potem najniższa Herezja).

**Patrz także:** [Wydarzenie ramowe](#wydarzenie-ramowe), [Zwycięstwo](#zwycięstwo) · [`ksiega.md`](ksiega.md)

---

## Fizzle

Karta nie rozpatruje efektu (np. brak Agenta / lokacji przy odkryciu). **Freeze:** fizzle **bez** Herezji, chyba że tekst karty mówi inaczej.

**Patrz także:** [Inicjacja karty](#inicjacja-karty), [Odkrycie](#odkrycie)

---

## Fragment

Znacznik / cel Kabały. Warunek: 3 Fragmenty + Herezja w strefie Obserwowanej (4–6), od wskazanej Ery.

**Patrz także:** [Herezja](#herezja), [Zwycięstwo](#zwycięstwo)

---

## Hak

Żeton **jednego typu** — prywatna władza nad ofiarą. Źródła: Przesłuchanie, karty (`creates_hook`), edykty. Max **2** aktywne Haki / gracza (prototyp).

**Patrz także:** [Wymuszenie](#wymuszenie), [Przesłuchanie](#przesłuchanie) · [`../../game/mechanics/haki.md`](../../game/mechanics/haki.md)

---

## Herezja

Tor **0–10** na planszetce. Strefy: Czysta 0–3, Obserwowana 4–6, **Krytyczna** 7–10 (można oskarżyć). Źródła: karty, Hak ujawniony, Autodafé, Podwójny wykryty, Werdykt (uniewinnienie) itd.

**Patrz także:** [Krytyczna](#krytyczna), [Oskarżenie](#oskarżenie) · [`../../game/mechanics/poziom-herezji.md`](../../game/mechanics/poziom-herezji.md)

---

## Inicjacja karty

**Suplement I:** deklaracja → koszty (płać przy zagraniu) → efekt (przy odkryciu lub wg tekstu). Język efektu → leksykon.

**Patrz także:** [Fizzle](#fizzle), [Limit / Erę](#limit--erę) · [`ksiega.md`](ksiega.md) · [`../../game/mechanics/leksykon.md`](../../game/mechanics/leksykon.md)

---

## Inkwizytor

Figurka NPC (Wielki Inkwizytor). Stany: Patrol / Autodafé. W **E.I:** nasłania → ruch 0–1 → ewentualne Autodafé. Bez nasłania ruch wybiera gracz z najniższą Herezją (remis → 1. gracz).

**Patrz także:** [Nasłanie](#nasłanie), [Autodafé](#autodafé) · [`../../game/mechanics/wielki-inkwizytor.md`](../../game/mechanics/wielki-inkwizytor.md)

---

## Karty (typy)

**Akcja** — zakryta pod lokacją w E.II. **Reakcja** — okno reakcji przy warunku. **Specjalna** — często `Łamie regułę`. Anatomia: SCHEMA; komendy: leksykon (Title Case; `EDYKT`/`DEKRET` = CAPS; zero prozy w `effect`).

**Patrz także:** [Okno reakcji](#okno-reakcji), [Edykt karty](#edykt-karty) · [`../../game/cards/SCHEMA.md`](../../game/cards/SCHEMA.md) · [`../../game/mechanics/leksykon.md`](../../game/mechanics/leksykon.md)

---

## Krytyczna

Strefa Herezji **7–10**. Inni gracze mogą **Rzucić Oskarżenie** przeciw Tobie (limit 1× przeciw temu graczowi / Erę).

**Patrz także:** [Herezja](#herezja), [Werdykt](#werdykt) · [`../../game/mechanics/poziom-herezji.md`](../../game/mechanics/poziom-herezji.md)

---

## Limit / Erę

Etykieta na karcie (`Limit:`) i limity anti-AP stołu: **1** wymuszenie Haka · **1** Przesłuchanie · **1** nasłanie · **max 2** karty Akcji na gracza na Erę (z opcją pasa). Autodafé: max co 2 Ery.  
**Maksymalnie** (np. max 2 Haki) = twardy cap posiadania, nie to samo co Limit / Erę.

**Patrz także:** [Wydarzenie ramowe](#wydarzenie-ramowe), [Może / musi](#może--musi) · leksykon §2

---

## Lokacja

Jedno z 5 miejsc na grafie (Trybunał → … → Gildia). Kolejność odkrywania kart 1→5 ≠ graf ruchu. Inkwizytor i Agenci poruszają się po **krawędziach**.

**Patrz także:** [Odkrycie](#odkrycie), [Agent](#agent) · [`../../game/board/locations.md`](../../game/board/locations.md)

---

## Lochy

Lokacja #3 + faza **E.IV**. Tu Areszt i **Przesłuchanie (procedura)**.

**Patrz także:** [Areszt](#areszt), [Przesłuchanie](#przesłuchanie) · [`../../game/mechanics/lochy-przesluchania.md`](../../game/mechanics/lochy-przesluchania.md)

---

## Może / musi

**Może** = opcjonalne (np. nasłanie, ruch Agenta, Autodafé jeśli wolno). Kroki **wydarzeń ramowych** E.* są obowiązkowe, o ile tekst nie mówi „opcjonalne”. Konflikt „czy muszę?” bez zapisu → [Wyrok surowy](#wyrok-surowy).

**Patrz także:** [Okno reakcji](#okno-reakcji), [Limit / Erę](#limit--erę)

---

## Nasłanie (opcjonalne)

Raz na gracza na Erę: wskaż kierunek / lokację dla Inkwizytora. Konflikt nasłań: wygrywa **Oficjum** (chyba że karta specjalna inaczej).

**Patrz także:** [Inkwizytor](#inkwizytor) · [`../../game/mechanics/wielki-inkwizytor.md`](../../game/mechanics/wielki-inkwizytor.md)

---

## Odkrycie (faza)

**E.III:** lokacje 1→5 — odkryj karty od 1. gracza, efekty, Herezja, areszty, konflikty kontroli.

**Patrz także:** [Fizzle](#fizzle), [Inicjacja karty](#inicjacja-karty) · [`ksiega.md`](ksiega.md)

---

## Okno reakcji

Moment poza kolejką Planu, gdy warunek karty **Reakcja** jest spełniony. Opcjonalne; nie zastępuje wydarzeń ramowych.

**Patrz także:** [Karty (typy)](#karty-typy), [Wydarzenie ramowe](#wydarzenie-ramowe)

---

## Oskarżenie

Akcja gracza w **E.V** przeciw celowi w Krytycznej (1× przeciw temu graczowi / Erę). Uruchamia **Werdykt (procedura)**.

**Patrz także:** [Krytyczna](#krytyczna), [Werdykt](#werdykt) · [`../../game/mechanics/werdykt-stolu.md`](../../game/mechanics/werdykt-stolu.md)

---

## Podwójny

Znacznik na Agentcie po Przesłuchaniu. Raz / Erę kontroler rusza nim o 1 jak swoim; **bez** dodatkowego głosu Werdyktu. Wykrycie → właściciel +2 Herezja, znacznik znika.

**Patrz także:** [Przesłuchanie](#przesłuchanie), [Agent](#agent) · [`../../game/mechanics/lochy-przesluchania.md`](../../game/mechanics/lochy-przesluchania.md)

---

## Przesłuchanie (procedura)

1 / gracza / Erę w **E.IV**. Dostęp: Agent w Lochach lub karta. Wybór na aresztowanym rywalu: Podwójny **lub** Hak **lub** +2 Herezja właścicielowi.

**Patrz także:** [Lochy](#lochy), [Hak](#hak) · [`../../game/mechanics/lochy-przesluchania.md`](../../game/mechanics/lochy-przesluchania.md)

---

## Relikwia

Znacznik celu Cieni (i interakcji Autodafé). Przy Autodafé w lokacji z Relikwią: Relikwia **wraca do puli** (freeze).

**Patrz także:** [Autodafé](#autodafé), [Zwycięstwo](#zwycięstwo)

---

## Remis

Przy Werdykcie (równe wagi głosów) → Uniewinnienie. Przy remisie korzyści bez zapisu → [Wyrok surowy](#wyrok-surowy). Remis postępu po 8 Er → najniższa Herezja.

**Patrz także:** [Werdykt](#werdykt), [Zwycięstwo](#zwycięstwo)

---

## Reakcja

Typ karty trzymanej w ręce; zagranie w [oknie reakcji](#okno-reakcji) przy warunku z tekstu.

**Patrz także:** [Karty (typy)](#karty-typy), [Okno reakcji](#okno-reakcji)

---

## Stos

Żeton eliminacji / zwycięstwa Oficjum. Źródła: Autodafé, skazanie Werdyktem (wybór Stosu). Oficjum liczy Stosy do celu.

**Patrz także:** [Autodafé](#autodafé), [Werdykt](#werdykt), [Zwycięstwo](#zwycięstwo)

---

## Talia Czasu

Talia edyktów (≥8). W **E.VI** odkryj **1** edykt. Zmienia prawo Ery / natychmiast wg tekstu.

**Patrz także:** [Edykt](#edykt), [Czystka](#czystka)

---

## Werdykt (procedura)

Głosowanie jawne Skazać / Uniewinnić (bez oskarżonego) po Oskarżeniu. Remis → Uniewinnienie. Skazanie: Agent → Stos lub Lochy +1 Herezja. Uniewinnienie: oskarżyciel +1 Herezja.

**Patrz także:** [Oskarżenie](#oskarżenie), [Krytyczna](#krytyczna) · [`../../game/mechanics/werdykt-stolu.md`](../../game/mechanics/werdykt-stolu.md)

---

## Wymuszenie (procedura)

Zużyj Hak (1 / gracza / Erę): ogłoś żądanie z listy; ofiara spełnia **albo** odmawia → Hak znika, ofiara +2 Herezja (cap 10).

**Patrz także:** [Hak](#hak), [Limit / Erę](#limit--erę) · [`../../game/mechanics/haki.md`](../../game/mechanics/haki.md)

---

## Wydarzenie ramowe

Obowiązkowy krok Ery **E.0–E.VI** (Start, Inkwizytor, Plan, Odkrycie, Lochy, Dwór, Czystka). Osobno od opcjonalnego [okna reakcji](#okno-reakcji).

**Patrz także:** [Era](#era) · [`ksiega.md`](ksiega.md)

---

## Wyrok surowy

**Złote prawo:** brak zapisu / konflikt kolejności → na niekorzyść gracza, który najbardziej zyskuje; remis korzyści → wyższa Herezja przegrywa spór; graj dalej.

**Patrz także:** [Złote prawa](#złote-prawa), [Remis](#remis)

---

## Złote prawa

Prawo Trybunału (hierarchia dokumentów) · Edykt karty · Zasada delty · Wyrok surowy. Pełny tekst: [`README.md`](README.md).

**Patrz także:** [Edykt karty](#edykt-karty), [Wyrok surowy](#wyrok-surowy)

---

## Złoto

Waluta kosztów kart i łapówek. Start **3**; trickle **+1** na początek swojej tury w E.II. Płatność **przy zagraniu** (freeze).

**Patrz także:** [Inicjacja karty](#inicjacja-karty) · [`ksiega.md`](ksiega.md)

---

## Zwycięstwo

Natychmiast po spełnieniu warunku frakcji (C). Limit 8 Er → najbliższy celowi; remis → najniższa Herezja. Tabela warunków: [`ksiega.md`](ksiega.md).

**Patrz także:** [Era](#era), [Herezja](#herezja)
