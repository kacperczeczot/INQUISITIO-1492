# Katalog kart — INQUISITIO 1492

> **Auto-generowane.** Nie edytuj ręcznie.
> Źródło: pojedyncze pliki w `game/cards/factions/` i `game/cards/time-deck/`.
> Odśwież: `python3 tools/cards/build_catalog.py`

Łącznie kart: **58**

Schemat pól: [`SCHEMA.md`](SCHEMA.md). Słownictwo `effect`: [`../mechanics/leksykon.md`](../mechanics/leksykon.md).

## Spis

- [Święte Oficjum](#swiete-oficjum) (10)
- [Cienie Al-Andalus](#cienie-al-andalus) (10)
- [Korona & Borgiowie](#korona-borgiowie) (10)
- [Kabała z Toledo](#kabala-toledo) (10)
- [Gildia Cieni](#gildia-cieni) (10)
- [Talia Czasu](#time) (8)

<a id="swiete-oficjum"></a>

## Święte Oficjum

Kart: **10**

### `so-01` — Patrol Familiariuszy

| Pole | Wartość |
| :--- | :--- |
| `id` | so-01 |
| `name` | Patrol Familiariuszy |
| `faction` | swiete-oficjum |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 1 |
| `heresy` | 0 |
| `heresy_text` | Familiariusze obchodzą miasto pod szyldem porządku i prawa. |
| `effect` | Przesuń swojego Agenta o 1 lokację. |
| `lore` | Cichy obrót przed patrolem Inkwizytora albo zbliżenie do rywala pod areszt. |
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
| `heresy` | 0 |
| `heresy_text` | Konfiskata majątku skazańców to prawny obowiązek trybunału. |
| `effect` | Zyskaj 2 złota. |
| `lore` | Rywale widzą paliwo Oficjum — kasę pod areszt i przesłuchanie. |
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
| `heresy` | 0 |
| `heresy_text` | Oskarżenie z urzędu niesie pieczęć Trybunału, nie plotkę rynku. |
| `effect` | Wskaż rywala: +1 Herezja. |
| `lore` | Publiczne napiętnowanie wrabia pod Krytyczną, zanim padnie nasłanie. |
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
| `cost_gold` | 1 |
| `heresy` | 0 |
| `heresy_text` | Familiariusze wskazują kierunek patrolu Wielkiego Inkwizytora. |
| `effect` | Przesuń Inkwizytora o 1 lokację w stronę lokacji swojego Agenta. Limit: 1 nasłanie / gracza / Erę. |
| `lore` | Oficjum daje sygnał patrolu, powoli naprowadzając Inkwizytora na cel. |
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
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Jeśli rywal zagrywa kartę z Herezją ≥ 1: Wskaż tego rywala: +1 Herezja. Limit: bez ruchu Agenta w tej Erze. |
| `lore` | Rywale wahają się przed brudnymi kartami, gdy Oficjum trzyma tę reakcję. |
| `tags` | reaction |
| `status` | prototyp |

### `so-06` — Areszt Trybunalski

| Pole | Wartość |
| :--- | :--- |
| `id` | so-06 |
| `name` | Areszt Trybunalski |
| `faction` | swiete-oficjum |
| `type` | akcja |
| `layer` | B |
| `cost_gold` | 2 |
| `heresy` | 0 |
| `heresy_text` | Areszt trybunalski ma moc, której dwór nie kwestionuje publicznie. |
| `effect` | Aresztuj Agenta rywala w lokacji swojego Agenta. |
| `lore` | Otwarty terror pozycji. Rywal unika Twojego pola albo płaci Przesłuchaniem. |
| `tags` | arrest |
| `status` | prototyp |

### `so-07` — Przesłuchanie Oficjum

| Pole | Wartość |
| :--- | :--- |
| `id` | so-07 |
| `name` | Przesłuchanie Oficjum |
| `faction` | swiete-oficjum |
| `type` | akcja |
| `layer` | B |
| `cost_gold` | 2 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Wykonaj Przesłuchanie na aresztowanego Agenta rywala. Limit: 1 / gracza / Erę. |
| `lore` | Prywatna władza. Ofiara negocjuje przy stole, zanim wybierzesz opcję. |
| `tags` | interrogation |
| `status` | prototyp |

### `so-08` — Nasłanie Inkwizytora

| Pole | Wartość |
| :--- | :--- |
| `id` | so-08 |
| `name` | Nasłanie Inkwizytora |
| `faction` | swiete-oficjum |
| `type` | akcja |
| `layer` | B |
| `cost_gold` | 2 |
| `heresy` | 1 |
| `heresy_text` | Powtórne wezwanie Inkwizytora w jednym tygodniu budzi szepty na dworze. |
| `effect` | Przesuń Inkwizytora do lokacji ze swoim Agentem. Limit: 1 nasłanie / gracza / Erę. |
| `lore` | Cały stół przestawia plany Autodafé i uników — zagrożenie terytorialne. |
| `tags` | inquisitor, heresy |
| `status` | prototyp |

### `so-09` — Świadek Koronny

| Pole | Wartość |
| :--- | :--- |
| `id` | so-09 |
| `name` | Świadek Koronny |
| `faction` | swiete-oficjum |
| `type` | akcja |
| `layer` | B |
| `cost_gold` | 2 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Załóż Hak na rywala z Agentem w Lochach lub w lokacji Inkwizytora. |
| `lore` | Szantaż „w imię wiary”. Odmowa = Herezja — ofiara często spełnia żądanie. |
| `tags` | hook |
| `status` | prototyp |

### `so-10` — Oczyść Miasto

| Pole | Wartość |
| :--- | :--- |
| `id` | so-10 |
| `name` | Oczyść Miasto |
| `faction` | swiete-oficjum |
| `type` | signature |
| `layer` | C |
| `cost_gold` | 4 |
| `heresy` | 2 |
| `heresy_text` | Autodafé z rozkazu trybunału pali strach, nie tylko drewno. |
| `effect` | Łamie regułę „Autodafé / 3 Ery”: Ogłoś Autodafé w lokacji Inkwizytora. Jeśli Agent rywala jest w lokacji Inkwizytora: Zyskaj Stos. |
| `lore` | Kulminacja terroru — ucieczka z lokacji Inkwizytora albo panika. |
| `tags` | signature, autodafe, heresy |
| `status` | prototyp |

<a id="cienie-al-andalus"></a>

## Cienie Al-Andalus

Kart: **10**

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
| `lore` | Cichy krok pod Relikwię albo z dala od Inkwizytora, zanim ktoś zauważy wzorzec. |
| `tags` | move |
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
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Zyskaj 2 złota. |
| `lore` | Ukryty skarb bractwa — stół widzi, że Cienie mają kasę na ewakuację. |
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
| `cost_gold` | 0 |
| `heresy` | 1 |
| `heresy_text` | Kupcy rozpoznają obce oblicze w tłumie na placu. |
| `effect` | Przesuń swojego Agenta o 1 lokację. |
| `lore` | Agent przeciąga Relikwię ku Rynkowi i Gildii, zanim ktoś dostrzeże cień. |
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
| `cost_gold` | 1 |
| `heresy` | 0 |
| `heresy_text` | Familiariusze łapią fałszywy trop, podrzucany przez cudze ręce. |
| `effect` | Wskaż rywala: +1 Herezja. |
| `lore` | Bluff „to nie my”, gdy Inkwizytor zmierza w Twoją stronę. |
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
| `cost_gold` | 1 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Jeśli masz Agenta w lokacji z Relikwią: Ewakuuj Relikwię z tej lokacji. Limit: 1 / Erę. |
| `lore` | Cichy port po pierwszej ewakuacji — druga Relikwia znika bez fanfar. |
| `tags` | relic |
| `status` | prototyp |

### `caa-06` — Ucieczka z Lochów

| Pole | Wartość |
| :--- | :--- |
| `id` | caa-06 |
| `name` | Ucieczka z Lochów |
| `faction` | cienie-al-andalus |
| `type` | akcja |
| `layer` | B |
| `cost_gold` | 2 |
| `heresy` | 0 |
| `heresy_text` | Klucz od strażnika, który nigdy nie służył Koronie. |
| `effect` | Uwolnij swojego aresztowanego Agenta z Lochów. Przesuń tego Agenta o 1 lokację. |
| `lore` | Psuje plan Przesłuchania. Trzymanie Cieni w Lochach to wyścig z ich kasą. |
| `tags` | move, arrest |
| `status` | prototyp |

### `caa-07` — Szantaż Bractwa

| Pole | Wartość |
| :--- | :--- |
| `id` | caa-07 |
| `name` | Szantaż Bractwa |
| `faction` | cienie-al-andalus |
| `type` | akcja |
| `layer` | B |
| `cost_gold` | 2 |
| `heresy` | 0 |
| `heresy_text` | Bractwo zna imiona sąsiadów lepiej niż proboszczowie. |
| `effect` | Załóż Hak na rywala z Agentem w sąsiedniej lokacji swojego Agenta. |
| `lore` | Szantaż z bliska — „wiemy, gdzie stoisz”. Wymusza dystans od Cieni. |
| `tags` | hook |
| `status` | prototyp |

### `caa-08` — Kaptur Nocy

| Pole | Wartość |
| :--- | :--- |
| `id` | caa-08 |
| `name` | Kaptur Nocy |
| `faction` | cienie-al-andalus |
| `type` | akcja |
| `layer` | B |
| `cost_gold` | 1 |
| `heresy` | 1 |
| `heresy_text` | Podwójny agent zostawia ślad w rejestrze gości. |
| `effect` | Jeśli masz Podwójnego: Przesuń tego Podwójnego o 1 lokację. |
| `lore` | Złamany Agent jako kurier Relikwii. Skandal, gdy ktoś wykryje Podwójnego. |
| `tags` | double, heresy |
| `status` | prototyp |

### `caa-09` — Kurier Relikwii

| Pole | Wartość |
| :--- | :--- |
| `id` | caa-09 |
| `name` | Kurier Relikwii |
| `faction` | cienie-al-andalus |
| `type` | akcja |
| `layer` | C |
| `cost_gold` | 2 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Przenieś Relikwię z lokacji swojego Agenta do sąsiedniej lokacji. |
| `lore` | Bluff kierunku Relikwii jest połową gry Cieni. |
| `tags` | relic, move |
| `status` | prototyp |

### `caa-10` — Echo Alhambry

| Pole | Wartość |
| :--- | :--- |
| `id` | caa-10 |
| `name` | Echo Alhambry |
| `faction` | cienie-al-andalus |
| `type` | signature |
| `layer` | C |
| `cost_gold` | 0 |
| `heresy` | 1 |
| `heresy_text` | Dwie Relikwie znikają w jednej nocy — nie czyni tak pielgrzym. |
| `effect` | Łamie regułę „Relikwia tylko ze Szlaku Morskiego”: Jeśli nie ma Inkwizytora w lokacji lub masz Podwójnego lub Szlak jest otwarty: Ewakuuj do 2 Relikwii z lokacji Twoich Agentów. |
| `lore` | As przed Flotą Kolumba. Oficjum musi palić Cieni wcześniej. |
| `tags` | signature, relic, heresy |
| `status` | prototyp |

<a id="korona-borgiowie"></a>

## Korona & Borgiowie

Kart: **10**

### `kb-01` — Rozkaz Dworu

| Pole | Wartość |
| :--- | :--- |
| `id` | kb-01 |
| `name` | Rozkaz Dworu |
| `faction` | korona-borgiowie |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 1 |
| `heresy` | 0 |
| `heresy_text` | Królewski nakaz wiąże bez pytania biskupów o zgodę. |
| `effect` | Przesuń swojego Agenta o 1 lokację. |
| `lore` | Ustawiasz figurę pod Pałac lub pod przyszły Hak; wygląda na rutynę dworu. |
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
| `effect` | Zyskaj 2 złota. |
| `lore` | Korona zbiera daninę pod Dekrety i przekupstwa. Sygnał bogactwa — stać Cię na Areszt i kartę specjalną. |
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
| `heresy` | 0 |
| `heresy_text` | Szept z sali tronowej dociera do familiariusza szybciej niż msza. |
| `effect` | Wskaż rywala: +1 Herezja. |
| `lore` | Polityczne ukłucie; często celujesz w kogoś pod przyszły Hak (≥4). |
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
| `cost_gold` | 1 |
| `heresy` | 1 |
| `heresy_text` | Faworyzm dworu budzi zazdrość kortegan i biskupów. |
| `effect` | Przesuń swojego Agenta o 1 lokację. Załóż Hak na rywala. |
| `lore` | Stół widzi faworyta z żetonem szantażu, zanim padnie Dekret. |
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
| `lore` | List żelazny kupuje dźwignię dworu — i milczenie o Twojej reputacji. |
| `tags` | decree, hook |
| `status` | prototyp |

### `kb-06` — Areszt Królewski

| Pole | Wartość |
| :--- | :--- |
| `id` | kb-06 |
| `name` | Areszt Królewski |
| `faction` | korona-borgiowie |
| `type` | akcja |
| `layer` | B |
| `cost_gold` | 2 |
| `heresy` | 0 |
| `heresy_text` | Królewski areszt ma precedens starszy niż bulla papieska. |
| `effect` | Aresztuj Agenta rywala w Pałacu lub w lokacji ze swoim Agentem. |
| `lore` | Pałac staje się pułapką; Twoja obecność gdziekolwiek to groźba aresztu. |
| `tags` | arrest |
| `status` | prototyp |

### `kb-07` — Szantaż Pieczęcią

| Pole | Wartość |
| :--- | :--- |
| `id` | kb-07 |
| `name` | Szantaż Pieczęcią |
| `faction` | korona-borgiowie |
| `type` | akcja |
| `layer` | B |
| `cost_gold` | 2 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Załóż Hak na rywala z Herezją ≥ 4. |
| `lore` | Korona poluje na już brudnych. Dwa Haki zaczynają się tu. |
| `tags` | hook |
| `status` | prototyp |

### `kb-08` — Przekupstwo Sędziego

| Pole | Wartość |
| :--- | :--- |
| `id` | kb-08 |
| `name` | Przekupstwo Sędziego |
| `faction` | korona-borgiowie |
| `type` | akcja |
| `layer` | B |
| `cost_gold` | 3 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | W następnym Werdykcie Twój głos ma wagę 2. Załóż Hak na rywala. |
| `lore` | Otwarty handel wyrokiem. Następne Oskarżenie będzie przechylone. |
| `tags` | verdict |
| `status` | prototyp |

### `kb-09` — Dekret Królewski

| Pole | Wartość |
| :--- | :--- |
| `id` | kb-09 |
| `name` | Dekret Królewski |
| `faction` | korona-borgiowie |
| `type` | signature |
| `layer` | C |
| `cost_gold` | 3 |
| `heresy` | 1 |
| `heresy_text` | Absolutyzm wymusza posłuszeństwo, którego Kościół nie śmie nazwać. |
| `effect` | DEKRET 1 — Łamie regułę „1 wymuszenie Haka / gracza / Erę”: Wymuś spełnienie Haka. Odmowa: +3 Herezja. |
| `lore` | Absolutyzm wymaga przygotowania. Bez Haka Dekret tylko liczy się do toru. |
| `tags` | signature, decree, heresy |
| `status` | prototyp |

### `kb-10` — Pieczęć Korony

| Pole | Wartość |
| :--- | :--- |
| `id` | kb-10 |
| `name` | Pieczęć Korony |
| `faction` | korona-borgiowie |
| `type` | signature |
| `layer` | C |
| `cost_gold` | 2 |
| `heresy` | 2 |
| `heresy_text` | Dwie pieczęcie na dwóch gardłach — tak brzmi koniec oporu. |
| `effect` | DEKRET 2 — Łamie regułę „zwycięstwo tylko po Erze”: Jeśli masz aktywne Haki na ≥ 2 graczach: zwycięstwo. |
| `lore` | Stół musi zerwać Twoje Haki, zanim zbierzesz obie pieczęcie. |
| `tags` | signature, decree, heresy |
| `status` | prototyp |

<a id="kabala-toledo"></a>

## Kabała z Toledo

Kart: **10**

### `kt-01` — Rytuał Przejścia

| Pole | Wartość |
| :--- | :--- |
| `id` | kt-01 |
| `name` | Rytuał Przejścia |
| `faction` | kabala-toledo |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 1 |
| `heresy` | 0 |
| `heresy_text` | Symboliczne przejście przez próg nie budzi alarmu familiariuszy. |
| `effect` | Przesuń swojego Agenta o 1 lokację. |
| `lore` | Ustawiasz się pod Lochy i Trybunał, gdzie Fragmenty czekają na właściwą winę. |
| `tags` | move |
| `status` | prototyp |

### `kt-02` — Transmutacja Złota

| Pole | Wartość |
| :--- | :--- |
| `id` | kt-02 |
| `name` | Transmutacja Złota |
| `faction` | kabala-toledo |
| `type` | akcja |
| `layer` | A |
| `cost_gold` | 1 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Zyskaj 2 złota. |
| `lore` | Alchemia sakiewki — budżet pod Imię i Kodeks bez hałasu rynku. |
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
| `heresy` | 1 |
| `heresy_text` | Zakazane strony Kodeksu świecą tylko dla wtajemniczonych oczu. |
| `effect` | Zyskaj Fragment. |
| `lore` | Pierwszy Fragment bez lochów — świadome wejście w Obserwowaną. |
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
| `cost_gold` | 0 |
| `heresy` | 0 |
| `heresy_text` | Zwierciadło odbija winę na obce imię w rejestrze familiariuszy. |
| `effect` | Wskaż rywala: +1 Herezja. |
| `lore` | Ktoś ma być brudniejszy od Ciebie, zanim familiariusze domkną rejestr. |
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
| `cost_gold` | 1 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Jeśli masz Agenta w Lochach lub Trybunale: Zyskaj Fragment. Jeśli nie masz Agenta w Lochach lub Trybunale: Zyskaj złoto. |
| `lore` | Drugi Fragment wymaga miejsca wiedzy — Agent przy Kodeksie w Lochach lub Trybunale. |
| `tags` | fragment |
| `status` | prototyp |

### `kt-06` — Przesłuchanie Imienia

| Pole | Wartość |
| :--- | :--- |
| `id` | kt-06 |
| `name` | Przesłuchanie Imienia |
| `faction` | kabala-toledo |
| `type` | akcja |
| `layer` | B |
| `cost_gold` | 2 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Wykonaj Przesłuchanie. Jeśli +2 Herezja lub Hak: Zyskaj Fragment. Limit: 1 / Erę. |
| `lore` | Wiedza z bólu imienia. Stół widzi, że wybierasz Fragment kosztem „łagodniejszej” opcji Podwójnego. |
| `tags` | interrogation, fragment |
| `status` | prototyp |

### `kt-07` — Archiwum Ukryte

| Pole | Wartość |
| :--- | :--- |
| `id` | kt-07 |
| `name` | Archiwum Ukryte |
| `faction` | kabala-toledo |
| `type` | akcja |
| `layer` | B |
| `cost_gold` | 1 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Załóż Hak na rywala z Herezją ≥ 4. |
| `lore` | Szantaż z archiwum win. Celujesz w tych, którzy już są na radarze. |
| `tags` | hook |
| `status` | prototyp |

### `kt-08` — Areszt Wiedzy

| Pole | Wartość |
| :--- | :--- |
| `id` | kt-08 |
| `name` | Areszt Wiedzy |
| `faction` | kabala-toledo |
| `type` | akcja |
| `layer` | B |
| `cost_gold` | 2 |
| `heresy` | 0 |
| `heresy_text` | Uczeń w lochach to zasób Korony — tak twierdzi sam Trybunał. |
| `effect` | Aresztuj Agenta rywala w Lochach lub w Trybunale. |
| `lore` | Kara za wchodzenie w święte i podziemne miejsca wiedzy. Synergia z Twoim Przesłuchaniem. |
| `tags` | arrest |
| `status` | prototyp |

### `kt-09` — Fragment Kodeksu

| Pole | Wartość |
| :--- | :--- |
| `id` | kt-09 |
| `name` | Fragment Kodeksu |
| `faction` | kabala-toledo |
| `type` | akcja |
| `layer` | C |
| `cost_gold` | 1 |
| `heresy` | 1 |
| `heresy_text` | Pergamin Salomona brudzi palce i sumienie. |
| `effect` | Jeśli masz ≥1 Fragment i Agenta w Lochach lub Trybunale: Zyskaj Fragment. |
| `lore` | Jawny postęp do trzech Fragmentów. Oficjum wie, kiedy jesteś blisko. |
| `tags` | fragment, heresy |
| `status` | prototyp |

### `kt-10` — Pieczęć Salomona

| Pole | Wartość |
| :--- | :--- |
| `id` | kt-10 |
| `name` | Pieczęć Salomona |
| `faction` | kabala-toledo |
| `type` | signature |
| `layer` | C |
| `cost_gold` | 1 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Łamie regułę „Herezja tylko z karty”: Jeśli masz 3 Fragmenty i Herezję 4–6: zwycięstwo. Jeśli masz 3 Fragmenty bez Herezji 4–6: Ustaw swoją Herezję na 5. |
| `lore` | Stół musi zbić Ci Fragmenty albo wypchnąć Cię z 4–6. |
| `tags` | signature, fragment |
| `status` | prototyp |

<a id="gildia-cieni"></a>

## Gildia Cieni

Kart: **10**

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
| `lore` | Cichy ruch pod Rynek/Gildię, skąd później bierzesz areszt i szantaż. |
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
| `cost_gold` | 1 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Zyskaj 2 złota. |
| `lore` | Handel spod lady — stół czuje, że Gildia ma gotówkę na brud. |
| `tags` | gold |
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
| `heresy` | 0 |
| `heresy_text` | Zakazana księga ląduje w cudzej komnacie o świcie. |
| `effect` | Wskaż rywala: +1 Herezja. |
| `lore` | Klasyczny frame: zakazana księga ląduje w cudzej komnacie. |
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
| `cost_gold` | 0 |
| `heresy` | 1 |
| `heresy_text` | Donosiciel pamięta twarz i zapach srebra. |
| `effect` | Załóż Hak na rywala. |
| `lore` | Donos bez oficjalnego pieczęci — fundament pod Upadek i odmowę. |
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
| `cost_gold` | 0 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Podczas Werdyktu, po ujawnieniu większości: Zmień swój głos. Limit: 1 / Erę. |
| `lore` | Zdrada w ostatniej chwili. Nikt nie ufa Twojemu „tak” przy stole. |
| `tags` | reaction |
| `status` | prototyp |

### `gc-06` — Szantaż

| Pole | Wartość |
| :--- | :--- |
| `id` | gc-06 |
| `name` | Szantaż |
| `faction` | gildia-cieni |
| `type` | akcja |
| `layer` | B |
| `cost_gold` | 2 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Załóż Hak na rywala. |
| `lore` | Uniwersalny szantaż podziemia. Fundament pod Listę Dłużników i Upadek. |
| `tags` | hook |
| `status` | prototyp |

### `gc-07` — Skrytobójstwo

| Pole | Wartość |
| :--- | :--- |
| `id` | gc-07 |
| `name` | Skrytobójstwo |
| `faction` | gildia-cieni |
| `type` | akcja |
| `layer` | B |
| `cost_gold` | 2 |
| `heresy` | 1 |
| `heresy_text` | Ciało w kanałach Gildii mówi więcej niż świadek na rynku. |
| `effect` | Aresztuj Agenta rywala w Gildii lub na Rynku. |
| `lore` | Terroryzujesz dwie lokacje handlu. Rywal unika Rynku albo płaci Lochami. |
| `tags` | arrest, heresy |
| `status` | prototyp |

### `gc-08` — Zatrute Złoto

| Pole | Wartość |
| :--- | :--- |
| `id` | gc-08 |
| `name` | Zatrute Złoto |
| `faction` | gildia-cieni |
| `type` | akcja |
| `layer` | B |
| `cost_gold` | 1 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Zyskaj złoto. Wskaż rywala: +1 Herezja. |
| `lore` | Prezent, który brudzi — kasa w jednej dłoni, piętno w drugiej. |
| `tags` | gold, heresy |
| `status` | prototyp |

### `gc-09` — Lista Dłużników

| Pole | Wartość |
| :--- | :--- |
| `id` | gc-09 |
| `name` | Lista Dłużników |
| `faction` | gildia-cieni |
| `type` | akcja |
| `layer` | C |
| `cost_gold` | 2 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | Załóż Hak na rywala. Jeśli Odmowa tego Haka w tej Erze: Oznacz Upadek wobec tego rywala. |
| `lore` | Odmowa przestaje być tania — płacisz Upadkiem frakcji. Dramat długu przy stole. |
| `tags` | hook, fall |
| `status` | prototyp |

### `gc-10` — Upadek Domu

| Pole | Wartość |
| :--- | :--- |
| `id` | gc-10 |
| `name` | Upadek Domu |
| `faction` | gildia-cieni |
| `type` | signature |
| `layer` | C |
| `cost_gold` | 4 |
| `heresy` | 2 |
| `heresy_text` | Dom płonie w oczach miasta, zanim zdąży zaprzeczyć. |
| `effect` | Łamie regułę „Upadek tylko z odmowy Haka”: Jeśli rywal ma ujawniony Hak, Podwójnego lub Autodafé w lokacji kluczowej: Oznacz Upadek wobec tego rywala. |
| `lore` | Egzekucja domu. Stół boi się trzymać ujawnione brudy. |
| `tags` | signature, fall, heresy |
| `status` | prototyp |

<a id="time"></a>

## Talia Czasu

Kart: **8**

### `time-01` — Upadek Grenady

| Pole | Wartość |
| :--- | :--- |
| `id` | time-01 |
| `name` | Upadek Grenady |
| `faction` | time |
| `type` | wydarzenie |
| `layer` | C |
| `cost_gold` | 0 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | EDYKT Ery. Każdy gracz z Agentem na Rynku: +1 Herezja. |
| `lore` | Obecność kosztuje reputację. Wszyscy uciekają z Rynku albo świadomie biorą Herezję za handel. Panika ekonomiczna. |
| `tags` | edict |
| `status` | prototyp |

### `time-02` — Edykt z Alhambry

| Pole | Wartość |
| :--- | :--- |
| `id` | time-02 |
| `name` | Edykt z Alhambry |
| `faction` | time |
| `type` | wydarzenie |
| `layer` | C |
| `cost_gold` | 0 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | EDYKT Ery. Gracz Cieni: Przesuń swojego Agenta o 1 lokację. Każdy inny gracz z Agentem w Gildii: +1 Herezja. |
| `lore` | Cienie dostają darmowy krok ewakuacji; reszta unika Gildii albo płaci. |
| `tags` | edict |
| `status` | prototyp |

### `time-03` — Flota Kolumba

| Pole | Wartość |
| :--- | :--- |
| `id` | time-03 |
| `name` | Flota Kolumba |
| `faction` | time |
| `type` | wydarzenie |
| `layer` | C |
| `cost_gold` | 0 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | EDYKT. Otwórz Szlak Morski do końca gry. |
| `lore` | Przełom gry o Relikwie. Cienie przyspieszają; Oficjum musi zamykać Rynek i Gildię. |
| `tags` | edict, relic |
| `status` | prototyp |

### `time-04` — Archiwa Alhambry

| Pole | Wartość |
| :--- | :--- |
| `id` | time-04 |
| `name` | Archiwa Alhambry |
| `faction` | time |
| `type` | wydarzenie |
| `layer` | C |
| `cost_gold` | 0 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | EDYKT Ery.  Jeśli Kabała ma Agenta w Trybunale lub Lochach: Zyskaj Fragment. |
| `lore` | Kabała ustawia Agenta z wyprzedzeniem; stół widzi darmowy Fragment albo nic. |
| `tags` | edict, fragment |
| `status` | prototyp |

### `time-05` — Auto-da-fé Toledo

| Pole | Wartość |
| :--- | :--- |
| `id` | time-05 |
| `name` | Auto-da-fé Toledo |
| `faction` | time |
| `type` | wydarzenie |
| `layer` | C |
| `cost_gold` | 0 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | EDYKT. Wymuś Autodafé w lokacji Inkwizytora. |
| `lore` | Nagły pożar. Figury przy Inkwizytorze dostają paniki; strach bez darmowego Stosu dla Oficjum. |
| `tags` | edict, autodafe |
| `status` | prototyp |

### `time-06` — Spisek na Dworze

| Pole | Wartość |
| :--- | :--- |
| `id` | time-06 |
| `name` | Spisek na Dworze |
| `faction` | time |
| `type` | wydarzenie |
| `layer` | C |
| `cost_gold` | 0 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | EDYKT Ery. Gracz Korony lub Gildii z najniższą Herezją: Załóż Hak na rywala. Remis: decyzja stołu. |
| `lore` | Nagły szantaż dla „najczystszej” Korony/Gildii. Reszta negocjuje, kto dostanie Hak. |
| `tags` | edict, hook |
| `status` | prototyp |

### `time-07` — Niepokój na Rynku

| Pole | Wartość |
| :--- | :--- |
| `id` | time-07 |
| `name` | Niepokój na Rynku |
| `faction` | time |
| `type` | wydarzenie |
| `layer` | C |
| `cost_gold` | 0 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | EDYKT Ery. Przesuń Inkwizytora o 1 lokację do Rynku. |
| `lore` | Rynek staje się strefą śmierci Autodafé. Kupcy i Cienie uciekają. |
| `tags` | edict, inquisitor |
| `status` | prototyp |

### `time-08` — Krypta pod Toledo

| Pole | Wartość |
| :--- | :--- |
| `id` | time-08 |
| `name` | Krypta pod Toledo |
| `faction` | time |
| `type` | wydarzenie |
| `layer` | C |
| `cost_gold` | 0 |
| `heresy` | 0 |
| `heresy_text` | — |
| `effect` | EDYKT. Umieść Relikwię w Lochach.  Jeśli pierwszy Agent jest w Lochach w następnej Erze: Przenieś Relikwię do tego Agenta. |
| `lore` | Wyścig do Lochów. Cienie vs Oficjum — kto pierwszy, ten bierze. |
| `tags` | edict, relic |
| `status` | prototyp |
