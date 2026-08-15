[Strona główna](../../README.md) > [Dokumentacja](../README.md) > [Zasady](README.md)

---

## Agent

Figurka frakcji na planszy (3 / gracza). Porusza się o max 1 krawędź grafu na turę Planu (chyba że karta mówi inaczej). Kontroluje lokacje, wchodzi w Autodafé, areszt i Werdykt.

**Patrz także:** [Lokacja](#lokacja), [Marionetka](#marionetka), [Areszt](#areszt)

---

## Areszt

Stan Agenta w strefie Areszt lokacji **Lochy**. Agent nie porusza się i nie kontroluje lokacji, dopóki nie wróci. Źródła: `arrest` na karcie, Werdykt, edykt / Autodafé wg tekstu.

**Patrz także:** [Lochy](#lochy), [Przesłuchanie](#przesłuchanie) · [`../../game/mechanics/lochy-przesluchania.md`](../../game/mechanics/lochy-przesluchania.md)

---

## Autodafé (procedura)

Czystka lokacji Inkwizytora: Agent rywala w strefie **Czystej (0–3 Herezji)** → do **Aresztu w Lochach** (+1 Herezja, bez Stosu); w strefie **Obserwowanej / Krytycznej (≥4 Herezji)** → **spalenie na Stosie** (+1 Herezja, +1 Stos dla Oficjum). Relikwia w lokacji wraca do puli. Max **co 3 Ery** (bazowo).  
**Ogłoś Autodafé** → Stos przy rywalu ≥4 Herezji. **Wymuś Autodafé** (edykt) → **bez** Stosu.

**Patrz także:** [Inkwizytor](#inkwizytor), [Stos](#stos) · [`../../game/mechanics/wielki-inkwizytor.md`](../../game/mechanics/wielki-inkwizytor.md) · leksykon **Ogłoś** / **Wymuś**

---

## Czystka (faza)

**Faza III (Kronika & Czystka):** Sprawdzenie natychmiastowych celów zwycięstwa; **Uzupełnienie:** dobór kart do limitu 5 + pobranie dochodu **+1 złoto** z banku; odkrycie karty Kroniki Dziejów; przesuń znacznik 1. gracza.

**Patrz także:** [Zwycięstwo](#zwycięstwo), [Era](#era), [Złoto](#złoto) · [`ksiega.md`](ksiega.md)

---

## Dekret

Cel / znacznik Korony (i karty Korony). Warunek zwycięstwa: zwykle 2 Dekrety + Haki (od Ery 5; 3p ≥0 / 4–5p ≥1).

**Patrz także:** [Zwycięstwo](#zwycięstwo), [Hak](#hak)

---

## Edykt

Karta Kroniki Dziejów lub efekt zmieniający prawo Ery. Odkrywany w **Fazie III (Kronika)** (1 / Erę jako prawo na kolejną rundę). Tekst edyktu obowiązuje w danej Erze według karty.

**Patrz także:** [Kronika Dziejów](#kronika-dziejów), [Edykt karty](#edykt-karty)

---

## Edykt karty

**Złote prawo:** tekst karty (`Łamie regułę …` / `breaks_rule`) wygrywa z księgą i teach.

**Patrz także:** [Złote prawa](#złote-prawa), [Karty (typy)](#karty-typy)

---

## Era

Jedna pełna runda składająca się z **3 Faz** (I Intryga, II Sąd, III Kronika & Czystka). Limit gry: **10** Er (potem remis postępu → najbliższy celowi, potem najniższa Herezja).

**Patrz także:** [Wydarzenie ramowe](#wydarzenie-ramowe), [Zwycięstwo](#zwycięstwo) · [`ksiega.md`](ksiega.md)

---

## Fiasko

Karta nie rozpatruje efektu (np. brak Agenta / lokacji przy odkryciu). Zgodnie z **kanonem reguł**: fiasko karty następuje **bez** przydzielania Herezji, chyba że tekst karty mówi inaczej.

**Patrz także:** [Inicjacja karty](#inicjacja-karty), [Odkrycie](#odkrycie)

---

## Fragment

Znacznik / cel Kabały. Warunek: 3 Fragmenty + Herezja **3–8**, od wskazanej Ery.

**Patrz także:** [Herezja](#herezja), [Zwycięstwo](#zwycięstwo)

---

## Hak

Żeton **jednego typu** — prywatna władza nad ofiarą. Źródła: Przesłuchanie, karty (`creates_hook`), edykty. Max **2** aktywne Haki / gracza (prototyp).

**Patrz także:** [Wymuszenie](#wymuszenie), [Przesłuchanie](#przesłuchanie) · [`../../game/mechanics/haki.md`](../../game/mechanics/haki.md)

---

## Herezja

Tor **0–10** na planszetce. Strefy: Czysta 0–3, Obserwowana 4–5 (3p) / 4–6 (4–5p), **Krytyczna** 6–10 (3p) / 7–10 (4–5p). **Oskarżenie** od Herezji ≥ **6** (3p) / ≥ **7** (4–5p). Źródła: karty, Hak ujawniony, Autodafé, Marionetka wykryta, Werdykt (uniewinnienie) itd.

**Patrz także:** [Krytyczna](#krytyczna), [Oskarżenie](#oskarżenie) · [`../../game/mechanics/poziom-herezji.md`](../../game/mechanics/poziom-herezji.md)

---

## Inicjacja karty

**Suplement I:** deklaracja → koszty (płać przy zagraniu) → efekt (przy odkryciu w Fazie II lub wg tekstu). Język efektu → leksykon.

**Patrz także:** [Fiasko](#fiasko), [Limit / Erę](#limit--erę) · [`ksiega.md`](ksiega.md) · [`../../game/mechanics/leksykon.md`](../../game/mechanics/leksykon.md)

---

## Inkwizytor

Figurka NPC (Wielki Inkwizytor). Stany: Patrol / Autodafé. W **Fazie II (Sąd):** nasłania → ruch 0–1 → ewentualne Autodafé. Bez nasłania ruch wybiera gracz z najniższą Herezją (remis → 1. gracz).

**Patrz także:** [Nasłanie](#nasłanie), [Autodafé](#autodafé) · [`../../game/mechanics/wielki-inkwizytor.md`](../../game/mechanics/wielki-inkwizytor.md)

---

## Karty (typy)

**Akcja** — zagrywana zakryta pod lokacją w Fazie I (Intryga). **Reakcja** — okno reakcji przy warunku. **Specjalna** — często `Łamie regułę`. Anatomia: SCHEMA; komendy: leksykon (Title Case; `EDYKT`/`DEKRET` = CAPS; zero prozy w `effect`).

**Patrz także:** [Okno reakcji](#okno-reakcji), [Edykt karty](#edykt-karty) · [`../../game/cards/SCHEMA.md`](../../game/cards/SCHEMA.md) · [`../../game/mechanics/leksykon.md`](../../game/mechanics/leksykon.md)

---

## Krytyczna

Strefa Herezji **6–10 (3p)** lub **7–10 (4–5p)** — tożsamy z progiem oskarżenia. Inni gracze mogą **Rzucić Oskarżenie** w Fazie II (limit 1× przeciw temu graczowi / Erę).

**Patrz także:** [Herezja](#herezja), [Werdykt](#werdykt) · [`../../game/mechanics/poziom-herezji.md`](../../game/mechanics/poziom-herezji.md)

---

## Limit / Erę

Etykieta na karcie (`Limit:`) i limity anti-AP stołu: **1** wymuszenie Haka · **1** Przesłuchanie · **1** nasłanie · **max 2** akcje na gracza na Erę (zagranie karty lub Akcja Gospodarcza). Autodafé: max co 3 Ery.  
**Maksymalnie** (np. max 2 Haki) = twardy cap posiadania, nie to samo co Limit / Erę.

**Patrz także:** [Wydarzenie ramowe](#wydarzenie-ramowe), [Może / musi](#może--musi) · leksykon §2

---

## Lokacja

Jedno z 5 miejsc na grafie (Trybunał → … → Gildia). Kolejność odkrywania kart 1→5 ≠ graf ruchu. Inkwizytor i Agenci poruszają się po **krawędziach**.

**Patrz także:** [Odkrycie](#odkrycie), [Agent](#agent) · [`../../game/board/locations.md`](../../game/board/locations.md)

---

## Lochy

Lokacja #3. Tu znajduje się strefa Aresztu oraz przeprowadzana jest procedura **Przesłuchania** w Fazie II (Sąd).

**Patrz także:** [Areszt](#areszt), [Przesłuchanie](#przesłuchanie) · [`../../game/mechanics/lochy-przesluchania.md`](../../game/mechanics/lochy-przesluchania.md)

---

## Może / musi

**Może** = opcjonalne (np. nasłanie, ruch Agenta, Autodafé jeśli wolno). Kroki **wydarzeń ramowych** 3 Faz są obowiązkowe, o ile tekst nie mówi „opcjonalne”. Konflikt „czy muszę?” bez zapisu → [Wyrok surowy](#wyrok-surowy).

**Patrz także:** [Okno reakcji](#okno-reakcji), [Limit / Erę](#limit--erę)

---

## Nasłanie (opcjonalne)

Raz na gracza na Erę: wskaż kierunek / lokację dla Inkwizytora. Konflikt nasłań: wygrywa **Oficjum** (chyba że karta specjalna inaczej).

**Patrz także:** [Inkwizytor](#inkwizytor) · [`../../game/mechanics/wielki-inkwizytor.md`](../../game/mechanics/wielki-inkwizytor.md)

---

## Odkrycie (krok Fazy II)

**Faza II (Krok 2):** lokacje 1→5 — odkryj karty od 1. gracza, rozpatrz efekty, Herezję, areszty i konflikty kontroli.

**Patrz także:** [Fiasko](#fiasko), [Inicjacja karty](#inicjacja-karty) · [`ksiega.md`](ksiega.md)

---

## Okno reakcji

Moment poza kolejką Fazy Intrygi, gdy warunek karty **Reakcja** jest spełniony. Opcjonalne; nie zastępuje wydarzeń ramowych.

**Patrz także:** [Karty (typy)](#karty-typy), [Wydarzenie ramowe](#wydarzenie-ramowe)

---

## Oskarżenie

Akcja gracza w **Fazie II (Dwór)** przeciw celowi w Krytycznej (1× przeciw temu graczowi / Erę). Uruchamia **Werdykt (procedura)**.

**Patrz także:** [Krytyczna](#krytyczna), [Werdykt](#werdykt) · [`../../game/mechanics/werdykt-stolu.md`](../../game/mechanics/werdykt-stolu.md)

---

## Marionetka

Znacznik na Agencie po Przesłuchaniu. Raz / Erę kontroler rusza nim o 1 jak swoim; **bez** dodatkowego głosu Werdyktu. Wykrycie → właściciel +2 Herezja, znacznik znika.

**Patrz także:** [Przesłuchanie](#przesłuchanie), [Agent](#agent) · [`../../game/mechanics/lochy-przesluchania.md`](../../game/mechanics/lochy-przesluchania.md)

---

## Przesłuchanie (procedura)

1 / gracza / Erę w **Fazie II (Lochy)**. Dostęp: Agent w Lochach lub karta. Wybór na aresztowanym rywalu: Marionetka **lub** Hak **lub** +2 Herezja właścicielowi.

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

## Kronika Dziejów

Talia 10 edyktów i wydarzeń miejskich (Toledo 1492). W **Fazie III (Kronika)** odkryj **1** kartę jako zwiastun prawa na nadchodzącą Erę.

**Patrz także:** [Edykt](#edykt), [Faza III](#faza-iii)

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

Obowiązkowy krok Ery w strukturze **3 Faz** (I Intryga, II Sąd, III Kronika & Czystka). Osobno od opcjonalnego [okna reakcji](#okno-reakcji).

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

Waluta kosztów kart i łapówek. Start **3** (w 5p: **2**); dochód **+1 złoto** w Fazie III (Kronika) + opcja Akcji Gospodarczej (+1 zł) w Fazie I (Intryga). Płatność **przy zagraniu** (kanon reguł).

**Patrz także:** [Inicjacja karty](#inicjacja-karty), [Czystka](#czystka) · [`ksiega.md`](ksiega.md)

---

## Zwycięstwo

Natychmiast po spełnieniu warunku frakcji (C). Limit 8 Er → najbliższy celowi; remis → najniższa Herezja. Tabela warunków: [`ksiega.md`](ksiega.md).

**Patrz także:** [Era](#era), [Herezja](#herezja)
