# Specyfikacja Konfiguracji `game_config.yaml` — Inquisitio 1492

Dokument zawiera pełną dokumentację techniczną, schemat pól oraz dopuszczalne wartości dla pliku **`game_config.yaml`**, który stanowi **Jedno Źródło Prawdy (Single Source of Truth)** dla zasad gry, ekonomii, słownika kart i celów balansowych symulatora.

---

## 📂 Struktura Pliku Konfiguracyjnego

Plik podzielony jest na 4 poziomy modyfikacji balansowych oraz sekcje pomocnicze:

1. **Poziom 1 (`system`):** Zasady i stałe ogólnosystemowe (złoto startowe, agenci, limit ręki, max Er, progi oskarżeń).
2. **Poziom 2 (`victory`):** Warunki zwycięstwa dla 5 frakcji w zależności od liczby graczy (3p, 4p, 5p).
3. **Poziom 3 (`economy` & `cards`):** Globalna ekonomia oraz indywidualna deklaratywna specyfikacja 50 kart.
4. **Poziom 4 (`variants`, `heresy_zones`, `telemetry_norms`):** Warianty rozgrywki, tor planszetek i normy audytowe.

---

## ⚙️ POZIOM 1: Zasady Systemowe (`system`)

| Klucz w YAML | Typ | Dopuszczalne wartości | Domyślnie | Opis |
| :--- | :--- | :--- | :--- | :--- |
| `start_gold` | `int` | `1 .. 10` | `3` | Złoto na starcie gry dla każdego gracza |
| `agents_per_player` | `int` | `1 .. 5` | `3` | Liczba figurków agentów w puli gracza |
| `hand_limit` | `int` | `3 .. 10` | `5` | Maksymalna liczba kart na ręce na koniec tury |
| `max_eras` | `int` | `3 .. 12` | `8` | Limit Er (po osiągnięciu gra kończy się remisem / deadlockiem) |
| `autodafe_cooldown` | `int` | `1 .. 4` | `3` | Co ile Er Inkwizytor ogłasza rutynowe Autodafé |
| `accusation_threshold` | `dict` | `3p: 5..10`, `4p: 5..10`, `5p: 5..10` | `3p:6, 4p:7, 5p:7` | Próg Herezji wyzwalający Werdykt i Oskarżenie |

---

## 🏆 POZIOM 2: Warunki Zwycięstwa Frakcji (`victory`)

### 1. Święte Oficjum (`swiete_oficjum`)
| Klucz w YAML | Typ | Dopuszczalne wartości | Opis |
| :--- | :--- | :--- | :--- |
| `stacks` | `dict` | `3p: 1..5`, `4p: 1..5`, `5p: 1..5` | Wymagana liczba Stosów (ze spalonych agentów w Autodafé) |
| `condemns` | `dict` | `3p: 1..5`, `4p: 1..5`, `5p: 1..5` | Wymagana liczba skazanych rywali w Werdyktach (ścieżka alternatywna) |

### 2. Cienie Al-Andalus (`cienie_al_andalus`)
| Klucz w YAML | Typ | Dopuszczalne wartości | Opis |
| :--- | :--- | :--- | :--- |
| `relics` | `int` | `1 .. 3` | Liczba Relikwii wymagana do ewakuacji |
| `path_era` | `dict` | `3p: 3..8`, `4p: 3..8`, `5p: 3..8` | Minimalna Era na ukończenie ewakuacji bez ścieżki (szlak / Podwójny / cichy exit) |

### 3. Korona Borgiowie (`korona_borgiowie`)
| Klucz w YAML | Typ | Dopuszczalne wartości | Opis |
| :--- | :--- | :--- | :--- |
| `decrees` | `dict` | `3p: 1..4`, `4p: 1..4`, `5p: 1..4` | Liczba zagranych kart Dekretów Signature (`KB-09`, `KB-10`) |
| `hooks` | `dict` | `3p: 0..3`, `4p: 0..3`, `5p: 0..3` | Liczba unikalnych rywali, na których Korona założyła Hak |
| `path_era` | `dict` | `3p: 3..8`, `4p: 3..8`, `5p: 3..8` | Maksymalna Era na zrealizowanie domeny politycznej |

### 4. Kabała Toledo (`kabala_toledo`)
| Klucz w YAML | Typ | Dopuszczalne wartości | Opis |
| :--- | :--- | :--- | :--- |
| `fragments` | `dict` | `3p: 1..4`, `4p: 1..4`, `5p: 1..4` | Wymagana liczba zgromadzonych Fragmentów Kodeksu |
| `heresy_band` | `list[int]` | `[min, max]` (np. `[3, 7]`) | Dopuszczalny przedział Herezji w momencie ukończenia Cyklu |
| `path_era` | `dict` | `3p: 3..8`, `4p: 3..8`, `5p: 3..8` | Maksymalna Era na dokończenie Rytuału Cyklu |

### 5. Gildia Cieni (`gildia_cieni`)
| Klucz w YAML | Typ | Dopuszczalne wartości | Opis |
| :--- | :--- | :--- | :--- |
| `falls.default` | `int` | `1 .. 4` | Liczba doprowadzonych Upadków rywali w standardowej grze |
| `falls.no_oficjum` | `int` | `1 .. 5` | Liczba Upadków rywali, gdy w partii nie bierze udziału Święte Oficjum |

---

## 🃏 POZIOM 3: Słownik Kart (`cards:`)

Każdy wpis karty w `cards:` zawiera słownik deklaratywnych właściwości:

### 1. Właściwości Ogólne i Identyfikacja

| Pole | Typ | Dopuszczalne wartości | Opis |
| :--- | :--- | :--- | :--- |
| `name` | `str` | Dowolny tekst | Nazwa karty (np. `"Publiczne Ostrzeżenie"`) |
| `type` | `enum` | `akcja`, `reakcja`, `signature` | Kategoria funkcjonalna karty |
| `layer` | `enum` | `A`, `B`, `C` | Warstwa zaawansowania karty |
| `cost` | `int` | `0 .. 10` | Koszt zagrania karty w złocie z banku |
| `heresy` | `int` | `0 .. 5` | Własny przyrost Herezji po zagraniu `[🔥 N]` |
| `target_heresy` | `int` | `0 .. 5` | Liczba Herezji przydzielana wskazanemu rywalowi |
| `gold` | `int` | `0 .. 10` | Złoto pozyskiwane z banku |
| `agents` | `int` | `0 .. 3` | Liczba ruchów przemieszczenia agenta |

### 2. Deklaratywne Komendy Mechaniczne (`action`) oraz Powiązane Parametry Dedykowane

Każda akcja (`action`) wykorzystuje ściśle dopasowany zestaw właściwości pomocniczych. Poniższa tabela grupuje parametry wg komend mechanicznych:

| Wartość `action` | Powiązane parametry dedykowane | Opis komendy i generowana fraza leksykonu |
| :--- | :--- | :--- |
| `move_agent` | `agents`, `free_agent`, `move_relic`, `target_loc`, `condition` | Przemieszcza agenta (własnego, Podwójnego, uwolnienie z Lochów lub ruch Relikwii) |
| `gain_gold` | `gold`, `target_heresy` | Pozyskuje N złota z banku (`Zyskaj N złota.`) oraz opcjonalnie wskaż rywala (+N Herezja) |
| `frame_rival` | `target_heresy`, `target_scope`, `change_vote` | Przydziela rywalowi +N Herezji (`Wskaż rywala: +N Herezja.`) lub zmienia głos w Werdykcie |
| `send_inquisitor` | `target_loc`, `inquisitor_send_limit` | Przesuwa Inkwizytora (`Przesuń Inkwizytora do lokacji ze swoim Agentem.`) |
| `arrest` | `target_loc`, `arrest` | Aresztuje agenta rywala (`Aresztuj Agenta rywala w lokacji swojego Agenta.`) |
| `interrogate` | `target_loc`, `bonus_on_heresy`, `interrogate_limit` | Przeprowadza Przesłuchanie (`Wykonaj Przesłuchanie na aresztowanym Agentem rywala.`) |
| `creates_hook` | `condition`, `target_loc`, `verdict_weight`, `on_refusal`, `creates_hook`, `penalty_heresy`, `mark_fall` | Zakłada Hak na rywala, wymusza realizację Haka lub oznacza Upadek Domu |
| `autodafe` | `breaks_rule` | Wywołuje spalenie Autodafé (`Ogłoś Autodafé w lokacji Inkwizytora.`) |
| `evacuate_relic` | `max_relics`, `condition`, `kurier_limit` | Ewakuuje Relikwie (`Ewakuuj Relikwię z tej lokacji.`) |
| `check_victory` | `decree`, `condition`, `target_heresy_band`, `fallback_heresy` | Sprawdza natychmiastowe zwycięstwo (Korony / Kabały z korektą Herezji) |
| `grant_fragment` | `condition` | Pozyskuje Fragment Kodeksu (`Zyskaj Fragment.`) oraz opcjonalnie złoto alternatywne |

### 3. Filtry Lokacji (`target_loc`)

| Wartość `target_loc` | Tłumaczenie gramatyczne w Leksykonie |
| :--- | :--- |
| `agent_location` | `…w stronę lokacji swojego Agenta.` |
| `same_location` | `…w lokacji swojego Agenta.` |
| `neighbor_location` | `…w sąsiedniej lokacji swojego Agenta.` |
| `dungeon` | `…z Lochów.` / `…w Lochach.` |
| `palace_or_same_location` | `…w Pałacu lub w lokacji ze swoim Agentem.` |
| `dungeon_or_tribunal` | `…w Lochach lub w Trybunale.` |
| `guild_or_market` | `…w Gildii lub na Rynku.` |

### 4. Warunki i Triggery (`condition` / `trigger`)

| Wartość klucza | Typ | Tłumaczenie gramatyczne w Leksykonie |
| :--- | :--- | :--- |
| `relic_present` | `condition` | `Jeśli masz Agenta w lokacji z Relikwią:` |
| `has_double_agent` | `condition` | `Jeśli masz Podwójnego:` |
| `agent_in_dungeon_or_tribunal` | `condition` | `Jeśli masz Agenta w Lochach lub Trybunale:` |
| `fragments_eq_3` | `condition` | `Jeśli masz 3 Fragmenty` |
| `active_hooks_gte_2` | `condition` | `Jeśli masz aktywne Haki na ≥ 2 graczach:` |
| `no_inquisitor_or_double_or_sea_route` | `condition` | `Jeśli nie ma Inkwizytora w lokacji lub masz Podwójnego lub Szlak jest otwarty:` |
| `has_fragment_and_agent_in_dungeon_or_tribunal` | `condition` | `Jeśli masz ≥1 Fragment i Agenta w Lochach lub Trybunale:` |
| `rival_has_hook_or_double_or_autodafe` | `condition` | `Jeśli rywal ma ujawniony Hak, Podwójnego lub Autodafé w lokacji kluczowej:` |
| `rival_in_dungeon_or_inquisitor` | `condition` | `…z Agentem w Lochach lub w lokacji Inkwizytora.` |
| `heresy_gte_4` | `condition` | `…z Herezją ≥ 4.` |
| `rival_plays_heresy_gte_1` | `trigger` | `Jeśli rywal zagrywa kartę z Herezją ≥ 1:` |
| `after_verdict_majority_revealed` | `trigger` | `Podczas Werdyktu, po ujawnieniu większości:` |

### 5. Zakresy Celu (`target_scope`)

| Wartość `target_scope` | Tłumaczenie w Leksykonie |
| :--- | :--- |
| `free_rival` | `Wskaż rywala:` (wybór wolnego celu) |
| `triggering_rival` | `Wskaż tego rywala:` (cel ściśle wyzwalający reakcję) |

### 6. Limity Anti-AP

| Klucz limitu | Typ | Domyślnie | Fraza w Leksykonie | Zastosowanie |
| :--- | :--- | :--- | :--- | :--- |
| `inquisitor_send_limit` | `int` | `1` | `Limit: N nasłanie / gracza / Erę.` | Nasłanie Inkwizytora (`SO-04`, `SO-08`) |
| `interrogate_limit` | `int` | `1` | `Limit: N / gracza / Erę.` | Przesłuchanie Oficjum (`SO-07`) |
| `interrogate_limit` | `int` | `1` | `Limit: N / Erę.` | Przesłuchanie Kabały (`KT-06`) |
| `kurier_limit` | `int` | `1` | `Limit: N / Erę.` | Ewakuacja Ukrytego Kuriera (`CAA-05`) |
| `vote_change_limit` | `int` | `1` | `Limit: N / Erę.` | Zmiana głosu Fałszywego Świadka (`GC-05`) |
| `limit_per_era` | `int` | `1` | `Limit: N / Erę.` | Standardowy limit użyć akcji na Erę |
| `no_move_limit` | `bool` | `true` | `Limit: bez ruchu Agenta w tej Erze.` | Reakcja bez ruchu agenta (`SO-05`) |

---

## 🛠️ Narzędzia i Użycie

1. **Synchronizacja Dokumentów z Configiem:**
   ```bash
   sim/.venv/bin/python tools/sync_config.py
   ```
2. **Sprawdzanie i Weryfikacja Generatora Kart z Configu:**
   ```bash
   sim/.venv/bin/python tools/test_card_text_gen.py
   ```
3. **Uruchamianie Audytów Balansowych Monte Carlo po Edycji Configu:**
   ```bash
   sim/.venv/bin/python tools/sim/audit_level3.py --faction so --games 100
   ```
