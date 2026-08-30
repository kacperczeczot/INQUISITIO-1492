# Katalog kart — INQUISITIO 1492

> **Auto-generowane.** Nie edytuj ręcznie.
> Źródło: pojedyncze pliki w `docs/game/cards/factions/` i `docs/game/cards/time-deck/`.
> Odśwież: `python3 tools/cards/build_catalog.py`

Łącznie kart: **70**

Schemat pól: [`SCHEMA.md`](SCHEMA.md). Słownictwo `effect`: [`../mechanics/leksykon.md`](../mechanics/leksykon.md).

## Spis

- [Święte Oficjum](#swiete-oficjum) (12)
- [Cienie Al-Andalus](#cienie-al-andalus) (12)
- [Korona & Borgiowie](#korona-borgiowie) (12)
- [Kabała z Toledo](#kabala-toledo) (12)
- [Gildia Cieni](#gildia-cieni) (12)
- [Kronika Dziejów](#time) (10)

<a id="swiete-oficjum"></a>

## Święte Oficjum

Kart: **12**

### `so-01` — Patrol Familiariuszy

| Pole | Wartość |
| :--- | :--- |
| `id` | so-01 |
| `name` | Patrol Familiariuszy |
| `faction` | swiete-oficjum |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 1 |
| `heresy` | 2 |
| `heresy_text` | Familiariusze obchodzą miasto pod szyldem porządku i prawa. |
| `effect` | Przesuń swojego Agenta o 1 lokację. |
| `lore` | Cisi bracia zakonni krążą po bruku Toledo, nasłuchując każdego szeptu niezgodnego z dogmatem. |
| `tags` | move |
| `status` | prototyp |

### `so-02` — Skarbiec Trybunału

| Pole | Wartość |
| :--- | :--- |
| `id` | so-02 |
| `name` | Skarbiec Trybunału |
| `faction` | swiete-oficjum |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 1 |
| `heresy` | 2 |
| `heresy_text` | Konfiskata majątku skazańców to prawny obowiązek trybunału. |
| `effect` | Zyskaj 2 złota. Wskaż rywala: +2 Herezja. |
| `lore` | Złoto skonfiskowane heretykom zasila machinerię trybunału i opłaca setki donosicieli. |
| `tags` | gold |
| `status` | prototyp |

### `so-03` — Podejrzenie

| Pole | Wartość |
| :--- | :--- |
| `id` | so-03 |
| `name` | Podejrzenie |
| `faction` | swiete-oficjum |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 1 |
| `heresy` | 2 |
| `heresy_text` | Oskarżenie z urzędu niesie pieczęć Trybunału, nie plotkę rynku. |
| `effect` | Wskaż rywala: +1 Herezja. |
| `lore` | Jeden donos wrzucony do puszki w katedrze wystarczy, by cień podejrzeń padł na całą rodzinę. |
| `tags` | heresy |
| `status` | prototyp |

### `so-04` — Publiczne Ostrzeżenie

| Pole | Wartość |
| :--- | :--- |
| `id` | so-04 |
| `name` | Publiczne Ostrzeżenie |
| `faction` | swiete-oficjum |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 0 |
| `heresy` | 0 |
| `heresy_text` | Familiariusze wskazują kierunek patrolu Wielkiego Inkwizytora. |
| `effect` | Przesuń Inkwizytora o 1 lokację w stronę lokacji swojego Agenta. Limit: 1 nasłanie / gracza / Erę. |
| `lore` | Dzwon zwiastujący procesję pokutną zmusza grzeszników do natychmiastowego opuszczenia miasta. |
| `tags` | inquisitor |
| `status` | prototyp |

### `so-05` — Wezwanie do Trybunału

| Pole | Wartość |
| :--- | :--- |
| `id` | so-05 |
| `name` | Wezwanie do Trybunału |
| `faction` | swiete-oficjum |
| `type` | reakcja |
| `layer` | A |
| `cost_gold` | 0 |
| `heresy` | 1 |
| `heresy_text` | — |
| `effect` | Jeśli rywal zagrywa kartę z Herezją ≥ 1: Wskaż tego rywala: +1 Herezja. |
| `lore` | Gdy zbrojni strażnicy pukają nocą do wrót, w Toledo nie ma człowieka, który czułby się bezpieczny. |
| `tags` | reaction |
| `status` | prototyp |

### `so-06` — Areszt Trybunalski

| Pole | Wartość |
| :--- | :--- |
| `id` | so-06 |
| `name` | Areszt Trybunalski |
| `faction` | swiete-oficjum |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 2 |
| `heresy` | 0 |
| `heresy_text` | Areszt trybunalski ma moc, której dwór nie kwestionuje publicznie. |
| `effect` | Aresztuj Agenta rywala w lokacji swojego Agenta. |
| `lore` | Kute żelazem bramy trybunalskich kazamatów zamykają się za każdym, kogo dosięgnie oskarżenie. |
| `tags` | arrest |
| `status` | prototyp |

### `so-07` — Przesłuchanie Oficjum

| Pole | Wartość |
| :--- | :--- |
| `id` | so-07 |
| `name` | Przesłuchanie Oficjum |
| `faction` | swiete-oficjum |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 1 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Wykonaj Przesłuchanie na aresztowanego Agenta rywala. Limit: 1 / gracza / Erę. |
| `lore` | W kamiennych podziemiach trybunału milczenie jest tylko chwilową iluzją przed nieuchronnym wyznaniem. |
| `tags` | interrogation |
| `status` | prototyp |

### `so-08` — Nasłanie Inkwizytora

| Pole | Wartość |
| :--- | :--- |
| `id` | so-08 |
| `name` | Nasłanie Inkwizytora |
| `faction` | swiete-oficjum |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 0 |
| `heresy` | 0 |
| `heresy_text` | Powtórne wezwanie Inkwizytora w jednym tygodniu budzi szepty na dworze. |
| `effect` | Przesuń Inkwizytora do lokacji ze swoim Agentem. Limit: 1 nasłanie / gracza / Erę. |
| `lore` | Widok czarnego habitu i płonącej pochodni Inkwizytora paraliżuje całe dzielnice Toledo. |
| `tags` | inquisitor, heresy |
| `status` | prototyp |

### `so-09` — Świadek Koronny

| Pole | Wartość |
| :--- | :--- |
| `id` | so-09 |
| `name` | Świadek Koronny |
| `faction` | swiete-oficjum |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 1 |
| `heresy` | 2 |
| `heresy_text` | — |
| `effect` | Załóż Hak na rywala z Agentem w Lochach lub w lokacji Inkwizytora. |
| `lore` | Świadek, który otrzymał rozgrzeszenie w zamian za zeznania, jest najgroźniejszą bronią oskarżyciela. |
| `tags` | hook |
| `status` | prototyp |

### `so-10` — Oczyść Miasto

| Pole | Wartość |
| :--- | :--- |
| `id` | so-10 |
| `name` | Oczyść Miasto |
| `faction` | swiete-oficjum |
| `type` | signature |
| `layer` | A |
| `cost_gold` | 5 |
| `heresy` | 1 |
| `heresy_text` | Autodafé z rozkazu trybunału pali strach, nie tylko drewno. |
| `effect` | Łamie regułę „Autodafé / 3 Ery”: Ogłoś Autodafé w lokacji Inkwizytora. Jeśli Agent rywala jest w lokacji Inkwizytora: Zyskaj Stos. |
| `lore` | Dym z placu Zocodover unosi się ku niebiosom, oczyszczając miasto z grzechu i buntu. |
| `tags` | signature, autodafe, heresy |
| `status` | prototyp |

### `so-11` — Dekret Czystości Wiary

| Pole | Wartość |
| :--- | :--- |
| `id` | so-11 |
| `name` | Dekret Czystości Wiary |
| `faction` | swiete-oficjum |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 0 |
| `heresy` | 1 |
| `heresy_text` | — |
| `effect` | Wskaż rywala: +1 Herezja. Zyskaj 1 złoto. |
| `lore` | Kto odmawia posłuszeństwa dekretom wiary, sam wydaje na siebie wyrok wiecznego potępienia. |
| `tags` | heresy, gold |
| `status` | prototyp |

### `so-12` — Straż Trybunalska

| Pole | Wartość |
| :--- | :--- |
| `id` | so-12 |
| `name` | Straż Trybunalska |
| `faction` | swiete-oficjum |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 1 |
| `heresy` | 2 |
| `heresy_text` | — |
| `effect` | Przesuń swojego Agenta o 1 lokację. |
| `lore` | Zbrojna straż w żelaznych pancerzach pilnuje, by żaden heretyk nie zbiegł przed oblicze sprawiedliwości. |
| `tags` | move, gold |
| `status` | prototyp |

<a id="cienie-al-andalus"></a>

## Cienie Al-Andalus

Kart: **12**

### `caa-01` — Przejście Podziemiami

| Pole | Wartość |
| :--- | :--- |
| `id` | caa-01 |
| `name` | Przejście Podziemiami |
| `faction` | cienie-al-andalus |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 0 |
| `heresy` | 0 |
| `heresy_text` | Tunele starej Toledo znane tylko wtajemniczonym w bractwie. |
| `effect` | Przesuń swojego Agenta o 1 lokację. |
| `lore` | Podziemne akwedukty Maurów wciąż łączą pałace z ruinami dawnych meczetów. |
| `tags` | move, relic |
| `status` | prototyp |

### `caa-02` — Złoto z Kryjówki

| Pole | Wartość |
| :--- | :--- |
| `id` | caa-02 |
| `name` | Złoto z Kryjówki |
| `faction` | cienie-al-andalus |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 1 |
| `heresy` | 1 |
| `heresy_text` | — |
| `effect` | Zyskaj 3 złota. |
| `lore` | Skarby ukryte w murach przed upadkiem Grenady finansują walkę o ocalenie dziedzictwa. |
| `tags` | gold |
| `status` | prototyp |

### `caa-03` — Cień na Rynku

| Pole | Wartość |
| :--- | :--- |
| `id` | caa-03 |
| `name` | Cień na Rynku |
| `faction` | cienie-al-andalus |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 1 |
| `heresy` | 1 |
| `heresy_text` | Kupcy rozpoznają obce oblicze w tłumie na placu. |
| `effect` | Przesuń swojego Agenta o 1 lokację. |
| `lore` | W gwarze targowiska najłatwiej przekazać zakazany zwój lub ostrzec braci przed obławą. |
| `tags` | move, relic, heresy |
| `status` | prototyp |

### `caa-04` — Fałszywy Trop

| Pole | Wartość |
| :--- | :--- |
| `id` | caa-04 |
| `name` | Fałszywy Trop |
| `faction` | cienie-al-andalus |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 0 |
| `heresy` | 0 |
| `heresy_text` | Familiariusze łapią fałszywy trop, podrzucany przez cudze ręce. |
| `effect` | Wskaż rywala: +1 Herezja. |
| `lore` | Porzucony burnus i ślad w zaułku kierują inkwizytorów w ślepą uliczkę, z dala od prawdziwych uciekinierów. |
| `tags` | heresy |
| `status` | prototyp |

### `caa-05` — Ukryty Kurier

| Pole | Wartość |
| :--- | :--- |
| `id` | caa-05 |
| `name` | Ukryty Kurier |
| `faction` | cienie-al-andalus |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 0 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Jeśli masz Agenta w lokacji z Relikwią: Ewakuuj Relikwię z tej lokacji. Limit: 1 / Erę. |
| `lore` | Zaufany posłaniec przemyka nocą przez bramy miejskie, niosąc relikwię ku bezpiecznym górom. |
| `tags` | relic |
| `status` | prototyp |

### `caa-06` — Ucieczka z Lochów

| Pole | Wartość |
| :--- | :--- |
| `id` | caa-06 |
| `name` | Ucieczka z Lochów |
| `faction` | cienie-al-andalus |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 0 |
| `heresy` | 0 |
| `heresy_text` | Klucz od strażnika, który nigdy nie służył Koronie. |
| `effect` | Uwolnij swojego aresztowanego Agenta z Lochów. Przesuń tego Agenta o 1 lokację. |
| `lore` | Podrobiony klucz i przekupiony strażnik otwierają kraty lochów nim nadejdzie świt. |
| `tags` | move, arrest |
| `status` | prototyp |

### `caa-07` — Szantaż Bractwa

| Pole | Wartość |
| :--- | :--- |
| `id` | caa-07 |
| `name` | Szantaż Bractwa |
| `faction` | cienie-al-andalus |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 0 |
| `heresy` | 0 |
| `heresy_text` | Bractwo zna imiona sąsiadów lepiej niż proboszczowie. |
| `effect` | Załóż Hak na rywala z Agentem w sąsiedniej lokacji swojego Agenta. |
| `lore` | Wiemy, jakie tajemnice skrywasz w alkowie — jeden nasz krok i trybunał pozna całą prawdę. |
| `tags` | hook |
| `status` | prototyp |

### `caa-08` — Kaptur Nocy

| Pole | Wartość |
| :--- | :--- |
| `id` | caa-08 |
| `name` | Kaptur Nocy |
| `faction` | cienie-al-andalus |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 1 |
| `heresy` | 0 |
| `heresy_text` | Marionetka w obcych szeregach zostawia ślad w rejestrze gości. |
| `effect` | Jeśli masz Marionetkę: Przesuń Marionetkę o 1 lokację. |
| `lore` | Złamany szantażem urzędnik wykonuje nasze polecenia, nie mając pojęcia, komu naprawdę służy. |
| `tags` | double, heresy |
| `status` | prototyp |

### `caa-09` — Kurier Relikwii

| Pole | Wartość |
| :--- | :--- |
| `id` | caa-09 |
| `name` | Kurier Relikwii |
| `faction` | cienie-al-andalus |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 0 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Przenieś Relikwię z lokacji swojego Agenta do sąsiedniej lokacji. |
| `lore` | Ocalone manuskrypty i relikwie przodków są warte więcej niż całe złoto kastylijskiej korony. |
| `tags` | relic, move |
| `status` | prototyp |

### `caa-10` — Echo Alhambry

| Pole | Wartość |
| :--- | :--- |
| `id` | caa-10 |
| `name` | Echo Alhambry |
| `faction` | cienie-al-andalus |
| `type` | signature |
| `layer` | A |
| `cost_gold` | 2 |
| `heresy` | 0 |
| `heresy_text` | Dwie Relikwie znikają w jednej nocy — nie czyni tak pielgrzym. |
| `effect` | Łamie regułę „Relikwia tylko ze Szlaku Morskiego”: Jeśli nie ma Inkwizytora w lokacji lub masz Marionetkę lub Szlak jest otwarty: Ewakuuj do 2 Relikwii z lokacji Twoich Agentów. |
| `lore` | Echo dawnej chwały Andaluzji rozbrzmiewa w sercach tych, którzy nigdy nie złożyli broni. |
| `tags` | signature, relic, heresy |
| `status` | prototyp |

### `caa-11` — Nocna Zmiana Warty

| Pole | Wartość |
| :--- | :--- |
| `id` | caa-11 |
| `name` | Nocna Zmiana Warty |
| `faction` | cienie-al-andalus |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 2 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Przesuń swojego Agenta o 1 lokację. Jeśli Inkwizytor jest w Twojej lokacji docelowej: przesuń go o 1 lokację. |
| `lore` | Zmienić latarnika, zgasić pochodnię w zaułku — i oto inkwizytor błądzi w labiryncie nocy. |
| `tags` | move, inquisitor |
| `status` | prototyp |

### `caa-12` — Skrytka w Murach

| Pole | Wartość |
| :--- | :--- |
| `id` | caa-12 |
| `name` | Skrytka w Murach |
| `faction` | cienie-al-andalus |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 1 |
| `heresy` | 1 |
| `heresy_text` | — |
| `effect` | Zyskaj 3 złota. |
| `lore` | Stare mauretańskie złoto ukryte w murach pałacowych czekało na ten decydujący dzień. |
| `tags` | gold, heresy |
| `status` | prototyp |

<a id="korona-borgiowie"></a>

## Korona & Borgiowie

Kart: **12**

### `kb-01` — Rozkaz Dworu

| Pole | Wartość |
| :--- | :--- |
| `id` | kb-01 |
| `name` | Rozkaz Dworu |
| `faction` | korona-borgiowie |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 1 |
| `heresy` | 1 |
| `heresy_text` | Królewski nakaz wiąże bez pytania biskupów o zgodę. |
| `effect` | Przesuń swojego Agenta o 1 lokację. |
| `lore` | Królewski rozkaz z pieczęcią z laku łamie każdy opór i otwiera najpilniej strzeżone wrota. |
| `tags` | move |
| `status` | prototyp |

### `kb-02` — Pobór Podatków

| Pole | Wartość |
| :--- | :--- |
| `id` | kb-02 |
| `name` | Pobór Podatków |
| `faction` | korona-borgiowie |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 1 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Zyskaj 2 złota. Wskaż rywala: +1 Herezja. |
| `lore` | Skarbiec korony musi być pełny, by opłacić lojalność wielmożów i milczenie kardynałów. |
| `tags` | gold |
| `status` | prototyp |

### `kb-03` — Plotka Dworska

| Pole | Wartość |
| :--- | :--- |
| `id` | kb-03 |
| `name` | Plotka Dworska |
| `faction` | korona-borgiowie |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 1 |
| `heresy` | 1 |
| `heresy_text` | Szept z sali tronowej dociera do familiariusza szybciej niż msza. |
| `effect` | Wskaż rywala: +1 Herezja. |
| `lore` | Zatruty szept w królewskiej alkowie potrafi zniszczyć ród potężniejszy niż armia zbrojnych. |
| `tags` | heresy |
| `status` | prototyp |

### `kb-04` — Faworyt Dworu

| Pole | Wartość |
| :--- | :--- |
| `id` | kb-04 |
| `name` | Faworyt Dworu |
| `faction` | korona-borgiowie |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 4 |
| `heresy` | 3 |
| `heresy_text` | Faworyzm dworu budzi zazdrość kortegan i biskupów. |
| `effect` | Przesuń swojego Agenta o 1 lokację. Załóż Hak na rywala. |
| `lore` | Faworyt dworu cieszy się łaską królowej, dopóki jego użyteczność przewyższa jego ambicję. |
| `tags` | hook, move, heresy |
| `status` | prototyp |

### `kb-05` — List Żelazny

| Pole | Wartość |
| :--- | :--- |
| `id` | kb-05 |
| `name` | List Żelazny |
| `faction` | korona-borgiowie |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 2 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Załóż Hak na rywala. |
| `lore` | Królewski list żelazny chroni przed szubienicą, lecz czyni jego posiadacza wiecznym dłużnikiem tronu. |
| `tags` | decree, hook |
| `status` | prototyp |

### `kb-06` — Areszt Królewski

| Pole | Wartość |
| :--- | :--- |
| `id` | kb-06 |
| `name` | Areszt Królewski |
| `faction` | korona-borgiowie |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 2 |
| `heresy` | 0 |
| `heresy_text` | Królewski areszt ma precedens starszy niż bulla papieska. |
| `effect` | Aresztuj Agenta rywala w Pałacu lub w lokacji ze swoim Agentem. |
| `lore` | Królewscy halabardnicy nie pytają o winę — wykonują wolę suwerena z bezwzględną precyzją. |
| `tags` | arrest |
| `status` | prototyp |

### `kb-07` — Szantaż Pieczęcią

| Pole | Wartość |
| :--- | :--- |
| `id` | kb-07 |
| `name` | Szantaż Pieczęcią |
| `faction` | korona-borgiowie |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 2 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Załóż Hak na rywala z Herezją ≥ 3. |
| `lore` | Papieska bulla i królewska pieczęć dają władzę, przed którą uginają się najtwardsze karki. |
| `tags` | hook |
| `status` | prototyp |

### `kb-08` — Przekupstwo Sędziego

| Pole | Wartość |
| :--- | :--- |
| `id` | kb-08 |
| `name` | Przekupstwo Sędziego |
| `faction` | korona-borgiowie |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 2 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | W następnym Werdykcie Twój głos ma wagę 2. Załóż Hak na rywala. |
| `lore` | Każdy wyrok ma swoją cenę, a waga sprawiedliwości przechyla się tam, gdzie padnie cięższe złoto. |
| `tags` | verdict, hook, gold |
| `status` | prototyp |

### `kb-09` — Dekret Królewski

| Pole | Wartość |
| :--- | :--- |
| `id` | kb-09 |
| `name` | Dekret Królewski |
| `faction` | korona-borgiowie |
| `type` | signature |
| `layer` | A |
| `cost_gold` | 2 |
| `heresy` | 0 |
| `heresy_text` | Absolutyzm wymusza posłuszeństwo, którego Kościół nie śmie nazwać. |
| `effect` | DEKRET 1 — Łamie regułę „1 wymuszenie Haka / gracza / Erę”: Wymuś spełnienie Haka. Odmowa: +3 Herezja. |
| `lore` | Królewski edykt nie podlega dyskusji — opór wobec korony jest tożsamy ze zdradą stanu. |
| `tags` | signature, decree, heresy |
| `status` | prototyp |

### `kb-10` — Pieczęć Korony

| Pole | Wartość |
| :--- | :--- |
| `id` | kb-10 |
| `name` | Pieczęć Korony |
| `faction` | korona-borgiowie |
| `type` | signature |
| `layer` | A |
| `cost_gold` | 4 |
| `heresy` | 1 |
| `heresy_text` | Dwie pieczęcie na dwóch gardłach — tak brzmi koniec oporu. |
| `effect` | DEKRET 2 — Łamie regułę „zwycięstwo tylko po Erze”: Jeśli masz aktywne Haki na ≥ 2 graczach: zwycięstwo. |
| `lore` | Gdy obie pieczęcie spoczną na pergaminie, żaden wielmoża w Kastylii nie zdoła podnieść głowy. |
| `tags` | signature, decree, heresy |
| `status` | prototyp |

### `kb-11` — Tajny Emisariusz

| Pole | Wartość |
| :--- | :--- |
| `id` | kb-11 |
| `name` | Tajny Emisariusz |
| `faction` | korona-borgiowie |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 1 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Przesuń swojego Agenta o 1 lokację. |
| `lore` | Złote pierścienie i listy polecające otwierają przed naszymi ludźmi każde drzwi w Toledo. |
| `tags` | move, gold |
| `status` | prototyp |

### `kb-12` — Szantaż Salonowy

| Pole | Wartość |
| :--- | :--- |
| `id` | kb-12 |
| `name` | Szantaż Salonowy |
| `faction` | korona-borgiowie |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 1 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Załóż Hak na rywala. |
| `lore` | Jedno niedyskretne słowo przy królewskim stole staje się wieczystą smyczą w naszych rękach. |
| `tags` | hook |
| `status` | prototyp |

<a id="kabala-toledo"></a>

## Kabała z Toledo

Kart: **12**

### `kt-01` — Ścieżka Wtajemniczenia

| Pole | Wartość |
| :--- | :--- |
| `id` | kt-01 |
| `name` | Ścieżka Wtajemniczenia |
| `faction` | kabala-toledo |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 1 |
| `heresy` | 0 |
| `heresy_text` | Wędrówka ścieżkami mądrości pozostaje niewidoczna dla niewtajemniczonych. |
| `effect` | Przesuń swojego Agenta o 1 lokację. |
| `lore` | Dyskretne kroki adepta po bruku Toledo nie przyciągają wzroku czujnych inkwizytorów. |
| `tags` | move, fragment |
| `status` | prototyp |

### `kt-02` — Transmutacja Złota

| Pole | Wartość |
| :--- | :--- |
| `id` | kt-02 |
| `name` | Transmutacja Złota |
| `faction` | kabala-toledo |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 0 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Zyskaj 3 złota. |
| `lore` | Alchemia i wiedza przodków pozwalają pomnażać kruszec z dala od chciwych oczu poborców. |
| `tags` | gold |
| `status` | prototyp |

### `kt-03` — Zakazana Wiedza

| Pole | Wartość |
| :--- | :--- |
| `id` | kt-03 |
| `name` | Zakazana Wiedza |
| `faction` | kabala-toledo |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 0 |
| `heresy` | 2 |
| `heresy_text` | Zakazane strony Kodeksu świecą tylko dla wtajemniczonych oczu. |
| `effect` | Zyskaj Fragment. |
| `lore` | Karty tajemnego Kodeksu świecą blaskiem widocznym tylko dla oczu wtajemniczonych. |
| `tags` | fragment, heresy |
| `status` | prototyp |

### `kt-04` — Zwierciadło Herezji

| Pole | Wartość |
| :--- | :--- |
| `id` | kt-04 |
| `name` | Zwierciadło Herezji |
| `faction` | kabala-toledo |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 1 |
| `heresy` | 0 |
| `heresy_text` | Zwierciadło odbija winę na obce imię w rejestrze familiariuszy. |
| `effect` | Wskaż rywala: +1 Herezja. |
| `lore` | Mistyczne zwierciadło odbija złą wolę prześladowców, kierując ich gniew na inne imię. |
| `tags` | heresy |
| `status` | prototyp |

### `kt-05` — Wskazówka Cyklu

| Pole | Wartość |
| :--- | :--- |
| `id` | kt-05 |
| `name` | Wskazówka Cyklu |
| `faction` | kabala-toledo |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 2 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Jeśli masz Agenta w Lochach lub Trybunale: Zyskaj Fragment. Jeśli nie masz Agenta w Lochach lub Trybunale: Zyskaj 1 złoto. |
| `lore` | Układ gwiazd nad Toledo wskazuje godzinę, w której pieczęć wiedzy może zostać otwarta. |
| `tags` | fragment |
| `status` | prototyp |

### `kt-06` — Przesłuchanie Imienia

| Pole | Wartość |
| :--- | :--- |
| `id` | kt-06 |
| `name` | Przesłuchanie Imienia |
| `faction` | kabala-toledo |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 2 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Wykonaj Przesłuchanie. Jeśli +2 Herezja lub Hak: Zyskaj Fragment. Limit: 1 / Erę. |
| `lore` | Imię wyryte na pergaminie zawiera w sobie moc wiązania woli i odsłaniania tajemnic. |
| `tags` | interrogation, fragment |
| `status` | prototyp |

### `kt-07` — Archiwum Ukryte

| Pole | Wartość |
| :--- | :--- |
| `id` | kt-07 |
| `name` | Archiwum Ukryte |
| `faction` | kabala-toledo |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 1 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Załóż Hak na rywala z Herezją ≥ 3. |
| `lore` | W podziemiach synagogi spoczywają archiwa, o których istnieniu biskupi nie śmią nawet marzyć. |
| `tags` | hook |
| `status` | prototyp |

### `kt-08` — Areszt Wiedzy

| Pole | Wartość |
| :--- | :--- |
| `id` | kt-08 |
| `name` | Areszt Wiedzy |
| `faction` | kabala-toledo |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 3 |
| `heresy` | 0 |
| `heresy_text` | Uczeń w lochach to zasób Korony — tak twierdzi sam Trybunał. |
| `effect` | Aresztuj Agenta rywala w Lochach lub w Trybunale. |
| `lore` | Strażnicy wiedzy wiedzą, jak zamknąć w lochu każdego, kto zbezcześci święte manuskrypty. |
| `tags` | arrest |
| `status` | prototyp |

### `kt-09` — Fragment Kodeksu

| Pole | Wartość |
| :--- | :--- |
| `id` | kt-09 |
| `name` | Fragment Kodeksu |
| `faction` | kabala-toledo |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 2 |
| `heresy` | 1 |
| `heresy_text` | Pergamin Salomona brudzi palce i sumienie. |
| `effect` | Jeśli masz ≥1 Fragment i Agenta w Lochach lub Trybunale: Zyskaj Fragment. |
| `lore` | Odnaleziony fragment starożytnego Kodeksu przybliża nas do poznania ostatecznej tajemnicy stworzenia. |
| `tags` | fragment, heresy |
| `status` | prototyp |

### `kt-10` — Pieczęć Salomona

| Pole | Wartość |
| :--- | :--- |
| `id` | kt-10 |
| `name` | Pieczęć Salomona |
| `faction` | kabala-toledo |
| `type` | signature |
| `layer` | A |
| `cost_gold` | 4 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Łamie regułę „Herezja tylko z karty”: Jeśli masz 3 Fragmenty zwycięstwo. |
| `lore` | Gdy Pieczęć Salomona zostanie domknięta, pradawna mądrość zatriumfuje nad mrokiem prześladowań. |
| `tags` | signature, fragment |
| `status` | prototyp |

### `kt-11` — Medytacja Sefirot

| Pole | Wartość |
| :--- | :--- |
| `id` | kt-11 |
| `name` | Medytacja Sefirot |
| `faction` | kabala-toledo |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 1 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Zmniejsz swoją Herezję o 1. Zyskaj 1 złoto. |
| `lore` | Waga losu wymaga idealnej równowagi — ani zbyt czysty, ani zbyt splamiony w oczach świata. |
| `tags` | gold, heresy |
| `status` | prototyp |

### `kt-12` — Strażnik Archiwum

| Pole | Wartość |
| :--- | :--- |
| `id` | kt-12 |
| `name` | Strażnik Archiwum |
| `faction` | kabala-toledo |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 1 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Przesuń swojego Agenta o 1 lokację. |
| `lore` | Kto zagląda w pergaminy Salomona, ten nieświadomie zostawia swój ślad na kartach przeznaczenia. |
| `tags` | move, heresy |
| `status` | prototyp |

<a id="gildia-cieni"></a>

## Gildia Cieni

Kart: **12**

### `gc-01` — Przekupiony Strażnik

| Pole | Wartość |
| :--- | :--- |
| `id` | gc-01 |
| `name` | Przekupiony Strażnik |
| `faction` | gildia-cieni |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 1 |
| `heresy` | 1 |
| `heresy_text` | Strażnik zna cenę milczenia lepiej niż modlitwy. |
| `effect` | Przesuń swojego Agenta o 1 lokację. |
| `lore` | Dźwięk złotych dukatów w sakiewce strażnika potrafi uczynić go ślepym i głuchym na całą noc. |
| `tags` | move |
| `status` | prototyp |

### `gc-02` — Czarny Rynek

| Pole | Wartość |
| :--- | :--- |
| `id` | gc-02 |
| `name` | Czarny Rynek |
| `faction` | gildia-cieni |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 0 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Zyskaj 3 złota. |
| `lore` | Handel spod lady i przemyt w zaułkach portowych — w piwnicach Toledo kupisz wszystko: od noża po fałszywe rozgrzeszenie. |
| `tags` | gold, heresy |
| `status` | prototyp |

### `gc-03` — Podrzucenie Księgi

| Pole | Wartość |
| :--- | :--- |
| `id` | gc-03 |
| `name` | Podrzucenie Księgi |
| `faction` | gildia-cieni |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 1 |
| `heresy` | 2 |
| `heresy_text` | Zakazana księga ląduje w cudzej komnacie o świcie. |
| `effect` | Wskaż rywala: +1 Herezja. |
| `lore` | Zakazana księga podłożona do komnaty rywala sprowadzi na niego inkwizycję jeszcze przed południem. |
| `tags` | heresy |
| `status` | prototyp |

### `gc-04` — Informator

| Pole | Wartość |
| :--- | :--- |
| `id` | gc-04 |
| `name` | Informator |
| `faction` | gildia-cieni |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 1 |
| `heresy` | 1 |
| `heresy_text` | Donosiciel pamięta twarz i zapach srebra. |
| `effect` | Załóż Hak na rywala. |
| `lore` | Donosiciel z zaułka nie żąda wiele, lecz pamięta każdą twarz i każdy brudny sekret miasta. |
| `tags` | hook, heresy |
| `status` | prototyp |

### `gc-05` — Fałszywy Świadek

| Pole | Wartość |
| :--- | :--- |
| `id` | gc-05 |
| `name` | Fałszywy Świadek |
| `faction` | gildia-cieni |
| `type` | reakcja |
| `layer` | A |
| `cost_gold` | 2 |
| `heresy` | 1 |
| `heresy_text` | — |
| `effect` | Podczas Werdyktu, po ujawnieniu większości: Zmień swój głos. Limit: 1 / Erę. |
| `lore` | Za odpowiednią sumę fałszywy świadek przysięgnie przed trybunałem na wszystkie świętości. |
| `tags` | reaction |
| `status` | prototyp |

### `gc-06` — Szantaż

| Pole | Wartość |
| :--- | :--- |
| `id` | gc-06 |
| `name` | Szantaż |
| `faction` | gildia-cieni |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 3 |
| `heresy` | 1 |
| `heresy_text` | — |
| `effect` | Załóż Hak na rywala. |
| `lore` | List z dowodem zdrady leży na stole — albo zapłacisz naszą cenę, albo jutro zawiśniesz. |
| `tags` | hook |
| `status` | prototyp |

### `gc-07` — Skrytobójstwo

| Pole | Wartość |
| :--- | :--- |
| `id` | gc-07 |
| `name` | Skrytobójstwo |
| `faction` | gildia-cieni |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 1 |
| `heresy` | 1 |
| `heresy_text` | Ciało w kanałach Gildii mówi więcej niż świadek na rynku. |
| `effect` | Aresztuj Agenta rywala w Gildii lub na Rynku. |
| `lore` | Ciało w mrocznym kanale Toledo mówi więcej niż sto kazań o kruchości ludzkiego żywota. |
| `tags` | arrest, heresy |
| `status` | prototyp |

### `gc-08` — Zatrute Złoto

| Pole | Wartość |
| :--- | :--- |
| `id` | gc-08 |
| `name` | Zatrute Złoto |
| `faction` | gildia-cieni |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 1 |
| `heresy` | 1 |
| `heresy_text` | — |
| `effect` | Zyskaj 1 złoto. Wskaż rywala: +1 Herezja. |
| `lore` | Pieniądze pachnące trucizną parzą dłonie tego, kto przyjmie je w godzinie chciwości. |
| `tags` | gold, heresy |
| `status` | prototyp |

### `gc-09` — Lista Dłużników

| Pole | Wartość |
| :--- | :--- |
| `id` | gc-09 |
| `name` | Lista Dłużników |
| `faction` | gildia-cieni |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 1 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Załóż Hak na rywala. Jeśli Odmowa tego Haka w tej Erze: Oznacz Upadek wobec tego rywala. |
| `lore` | Dług zaciągnięty w podziemiach Gildii spłaca się majątkiem, wolnością albo krwią. |
| `tags` | hook, fall |
| `status` | prototyp |

### `gc-10` — Upadek Domu

| Pole | Wartość |
| :--- | :--- |
| `id` | gc-10 |
| `name` | Upadek Domu |
| `faction` | gildia-cieni |
| `type` | signature |
| `layer` | A |
| `cost_gold` | 4 |
| `heresy` | 0 |
| `heresy_text` | Dom płonie w oczach miasta, zanim zdąży zaprzeczyć. |
| `effect` | Łamie regułę „Upadek tylko z odmowy Haka”: Jeśli rywal ma ujawniony Hak, Marionetkę lub Autodafé w lokacji kluczowej: Oznacz Upadek wobec tego rywala. |
| `lore` | Gdy upada potężny ród, w ruinach jego pałacu ucztują ci, którzy pociągali za sznurki z cienia. |
| `tags` | signature, fall, heresy |
| `status` | prototyp |

### `gc-11` — Fałszywe Świadectwo Cechu

| Pole | Wartość |
| :--- | :--- |
| `id` | gc-11 |
| `name` | Fałszywe Świadectwo Cechu |
| `faction` | gildia-cieni |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 0 |
| `heresy` | 2 |
| `heresy_text` | — |
| `effect` | Wskaż rywala: +1 Herezja. Zyskaj 1 złoto. |
| `lore` | Podrobiony podpis na wekslu to najtańszy i najszybszy sposób na zrujnowanie wielkiego rodu. |
| `tags` | heresy, hook |
| `status` | prototyp |

### `gc-12` — Złodziejski Zwiad

| Pole | Wartość |
| :--- | :--- |
| `id` | gc-12 |
| `name` | Złodziejski Zwiad |
| `faction` | gildia-cieni |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 1 |
| `heresy` | 2 |
| `heresy_text` | — |
| `effect` | Przesuń swojego Agenta o 1 lokację. |
| `lore` | Dla zwinnego kieszonkowca nocny spacer wąskimi uliczkami Toledo zawsze przynosi pełną sakiewkę. |
| `tags` | move, gold, heresy |
| `status` | prototyp |

<a id="time"></a>

## Kronika Dziejów

Kart: **10**

### `time-01` — Kapitulacja Grenady

| Pole | Wartość |
| :--- | :--- |
| `id` | time-01 |
| `name` | Kapitulacja Grenady |
| `faction` | time |
| `type` | wydarzenie |
| `layer` | C |
| `cost_gold` | 0 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Każdy gracz z Agentem w Pałacu zyskuje +1 złoto. Przesuń Inkwizytora o 1 krok w stronę Trybunału. |
| `lore` | Świętowanie na Dworze. Korona nagradza dyplomatów, a Inkwizytor powraca do centrum władzy kościelnej. |
| `tags` | edict, gold, inquisitor |
| `status` | prototyp |

### `time-02` — Godzina Policyjna

| Pole | Wartość |
| :--- | :--- |
| `id` | time-02 |
| `name` | Godzina Policyjna |
| `faction` | time |
| `type` | wydarzenie |
| `layer` | C |
| `cost_gold` | 0 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | EDYKT Ery. W tej Erze: Każde zagranie karty pod Rynek lub Gildię kosztuje +1 złoto dodatkowo. |
| `lore` | Straż miejska blokuje plebejskie zaułki. Ukryte operacje i handel stają się znacznie kosztowniejsze. |
| `tags` | edict, gold, tax |
| `status` | prototyp |

### `time-03` — Flota Odkrywców

| Pole | Wartość |
| :--- | :--- |
| `id` | time-03 |
| `name` | Flota Odkrywców |
| `faction` | time |
| `type` | wydarzenie |
| `layer` | C |
| `cost_gold` | 0 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Otwórz Szlak Morski. Każdy gracz z Agentem na Rynku lub w Gildii zyskuje +1 złoto. |
| `lore` | Wyprawa za ocean otwiera szlak ucieczki, a portowe rynki i warsztaty zalewa fala nowych zleceń. |
| `tags` | edict, sea_route, gold |
| `status` | prototyp |

### `time-04` — Rewizja w Dzielnicach

| Pole | Wartość |
| :--- | :--- |
| `id` | time-04 |
| `name` | Rewizja w Dzielnicach |
| `faction` | time |
| `type` | wydarzenie |
| `layer` | C |
| `cost_gold` | 0 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Gracz o najwyższej Herezji: +1 Herezja. Gracz o najniższej Herezji: Zyskuje +1 złoto. |
| `lore` | Inkwizycja zaostrza śledztwa wobec najbardziej podejrzanych, sowicie nagradzając lojalnych mieszczan. |
| `tags` | edict, heresy, gold |
| `status` | prototyp |

### `time-05` — Gorączka Donosów

| Pole | Wartość |
| :--- | :--- |
| `id` | time-05 |
| `name` | Gorączka Donosów |
| `faction` | time |
| `type` | wydarzenie |
| `layer` | C |
| `cost_gold` | 0 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | EDYKT Ery. W tej Erze: Próg Krytycznej Herezji (oskarżenia na Dworze) jest obniżony o 1. |
| `lore` | Paranoja w Toledo sięga zenitu. Wystarczy cień podejrzenia, by stanąć przed trybunałem sądu. |
| `tags` | edict, heresy, verdict |
| `status` | prototyp |

### `time-06` — Nocna Obława

| Pole | Wartość |
| :--- | :--- |
| `id` | time-06 |
| `name` | Nocna Obława |
| `faction` | time |
| `type` | wydarzenie |
| `layer` | C |
| `cost_gold` | 0 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Przesuń Inkwizytora do lokacji z największą liczbą Agentów. Przy remisie wybiera Pierwszy Gracz. |
| `lore` | Straż i inkwizytorzy uderzają w najludniejsze zgromadzenie w mieście, siejąc postrach. |
| `tags` | edict, inquisitor |
| `status` | prototyp |

### `time-07` — Bunt w Lochach

| Pole | Wartość |
| :--- | :--- |
| `id` | time-07 |
| `name` | Bunt w Lochach |
| `faction` | time |
| `type` | wydarzenie |
| `layer` | C |
| `cost_gold` | 0 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Uwolnij 1 uwięzionego Agenta do Gildii. Jeśli w Lochach nie ma uwięzionych Agentów: Umieść Relikwię w Lochach. |
| `lore` | Zamieszki w kazamatach otwierają drogę ucieczki dla więźnia lub ujawniają ukrytą w murach relikwię. |
| `tags` | edict, dungeon, relic |
| `status` | prototyp |

### `time-08` — Święte Przymierze

| Pole | Wartość |
| :--- | :--- |
| `id` | time-08 |
| `name` | Święte Przymierze |
| `faction` | time |
| `type` | wydarzenie |
| `layer` | C |
| `cost_gold` | 0 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | EDYKT Ery. W tej Erze: Faza Dworu zostaje zawieszona (brak możliwości rzucenia Oskarżenia). |
| `lore` | Tymczasowy rozejm polityczny na szczytach władzy zamraża publiczne procesy i egzekucje. |
| `tags` | edict, verdict |
| `status` | prototyp |

### `time-09` — Jarmark Królewski

| Pole | Wartość |
| :--- | :--- |
| `id` | time-09 |
| `name` | Jarmark Królewski |
| `faction` | time |
| `type` | wydarzenie |
| `layer` | C |
| `cost_gold` | 0 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | EDYKT Ery. W tej Erze: Akcja Gospodarcza na Rynku przynosi +2 złote zamiast +1 zł. |
| `lore` | Królewski przywilej targowy ściąga kupców z całej Kastylii, napędzając miejski handel. |
| `tags` | edict, gold, market |
| `status` | prototyp |

### `time-10` — Amnestia Biskupia

| Pole | Wartość |
| :--- | :--- |
| `id` | time-10 |
| `name` | Amnestia Biskupia |
| `faction` | time |
| `type` | wydarzenie |
| `layer` | C |
| `cost_gold` | 0 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Każdy gracz w Strefie Obserwowanej zmniejsza swoją Herezję o 1. |
| `lore` | Biskup ogłasza wielki jubileusz i powszechne rozgrzeszenie, dając wytchnienie podejrzanym. |
| `tags` | edict, heresy |
| `status` | prototyp |
