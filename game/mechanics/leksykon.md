[Strona główna](../../README.md) > [Gra](../README.md) > [Mechaniki](README.md)

---

# Leksykon efektów kart

> **Patrz także:** słownik stołu [`../../docs/rules/slownik.md`](../../docs/rules/slownik.md) (osobno — nie dubluje komend) · księga [`../../docs/rules/ksiega.md`](../../docs/rules/ksiega.md) · SCHEMA [`../cards/SCHEMA.md`](../cards/SCHEMA.md)

**Zamknięty słownik** pola `effect`. Każda karta mówi tym samym językiem.

**Zasada twarda:** w `effect` wolno używać **wyłącznie** tokenów z tego pliku (komendy §1, etykiety §2, rzeczowniki §3, klej §4, szablony §5).  
Słowo spoza leksykonu = błąd redakcji. Nie „dopisujemy po polsku” — dodajemy hasło do leksykonu albo zmieniamy efekt.

**Effect = delta:** pisz tylko to, co zmienia rozstrzygnięcie względem reguł bazowych. Nie powtarzaj reguł z mechanik (`haki.md`, Autodafé, limity Ery). Zakaz nawiasów typu „(bez X)” gdy X i tak nie obowiązuje.

### Styl `effect` (twardy)

Cel: krótki tekst jak instrukcja, nie proza.

1. **Lead:** każde zdanie-akcja zaczyna się od **komendy §1** albo **etykiety §2** (ew. po bloku `Jeśli …:`).
2. **Casing:** komendy i `Łamie regułę` = **Title Case** zawsze (także po `—` / `:`). Bannery talii = **CAPS:** `EDYKT.` / `EDYKT Ery.` / `DEKRET N`. Anti-AP i kara = Title + `:` → `Limit:` / `Odmowa:`.
3. **Bez zbędnego `1`:** przy liczbie pojedynczej nie pisz cyfry (`Załóż Hak`, `Aresztuj Agenta`, `Zyskaj Fragment`). Cyfra tylko gdy N ≠ 1 albo to dystans/limit (`o 1 lokację`, `Limit: 1 / Erę`, `+1 Herezja`, `≥1 Fragment`).
4. **Akcent typograficzny (PnP):** **pogrubienie** = komendy §1 + lead etykiet; *kursywa* = pojęcia mechaniczne ze słownika (zamknięta lista w generatorze: Autodafé, Przesłuchanie, Werdykt, Hak, Podwójny, Relikwia, Fragment, Stos, Inkwizytor, Szlak Morski, Nasłanie, Upadek, Herezja…). Nie kursywuj Agent / Lokacja / złoto.
5. **Zero prozy:** zakaz zdań wyjaśniających, teach A/B/C, „musisz mieć…”, „ten pożar nie…”. Smak → `lore` / `heresy_text`.
6. **Łańcuch / bloki:** warunek = `Jeśli …:` + linia komendy. Osobne informacje (akcja vs warunek vs `Limit:`) = **pusta linia** między blokami — PnP rysuje separator.

Źródło prawdy także dla `_KEYWORD_LEAD_RE` w [`tools/pnp/generate.py`](../../tools/pnp/generate.py).  
Schemat kart: [`../cards/SCHEMA.md`](../cards/SCHEMA.md).

**PnP:** **pogrubiaj** komendy (§1) i lead etykiet; *kursywuj* pojęcia mechaniczne (pkt 4). Linia `Jeśli …:` bez pogrubiania całego warunku. Lead `Łamie regułę` / `EDYKT` / `DEKRET` → banery w strefie EFFECT (nie zwykły akapit).  
**Typ karty** (`Akcja` / `Reakcja` / `Specjalna` / …) = **tylko badge** — nie powtarzaj w `effect`.  
**Strefy karty:** HDR → art → EFFECT → lore — patrz [`../cards/SCHEMA.md`](../cards/SCHEMA.md).

---

## 1. Komendy

Jedyny dozwolony lead instrukcji (po ewentualnym szablonie z §5). Forma: **Title Case**.

| Komenda | Znaczenie | Forma kanoniczna |
| :--- | :--- | :--- |
| **Przesuń** | Ruch figurki | `Przesuń swojego Agenta o 1 lokację.` · `Przesuń Inkwizytora do lokacji X.` |
| **Zyskaj** | +Złoto / +Fragment / +Stos | `Zyskaj N złota.` · `Zyskaj Fragment.` · `Zyskaj Stos.` |
| **Załóż** | Żeton Hak z banku gry | `Załóż Hak na rywala.` = wolny cel (wybór dowolnego rywala). Z filtrem: `Załóż Hak na rywala z Herezją ≥ 4.` · `Załóż Hak na rywala z Agentem w…`. **Nie** kradzież Haka rywala. **Zakaz** synonimów: `dowolnego` / `wybranego` / `wskazanego` / `na gracza` (przy Hakach). |
| **Wskaż** | Cel + Herezja na rywala | `Wskaż rywala: +N Herezja.` |
| **Aresztuj** | Agent → Areszt w Lochach | `Aresztuj Agenta rywala [warunek lokacji].` |
| **Uwolnij** | Wyjmij z Aresztu | `Uwolnij swojego aresztowanego Agenta z Lochów.` |
| **Przenieś** | Obiekt (Relikwia) | `Przenieś Relikwię z lokacji A do sąsiedniej lokacji.` |
| **Wykonaj** | Procedura | `Wykonaj Przesłuchanie.` |
| **Ogłoś** | Autodafé z Stosem / oskarżenie | `Ogłoś Autodafé w lokacji Inkwizytora.` → pełna procedura Autodafé **ze Stosem**. |
| **Wymuś** | Wymuszenie Haka lub Autodafé | `Wymuś spełnienie Haka.` (wymaga już posiadanego Haka). `Wymuś Autodafé w lokacji Inkwizytora.` → procedura Autodafé **bez Stosu** (Herezja obecnych + Relikwia do puli). |
| **Otwórz** | Trwały stan stołu | `Otwórz Szlak Morski do końca gry.` |
| **Umieść** | Żeton na planszy | `Umieść Relikwię w Lochach.` |
| **Ewakuuj** | Relikwia poza grę | `Ewakuuj Relikwię z tej lokacji.` |
| **Oznacz** | Upadek | `Oznacz Upadek wobec tego rywala.` |
| **Zmień** | Głos Werdyktu | `Zmień swój głos.` |
| **Ustaw** | Ustal wartość Herezji | `Ustaw swoją Herezję na N.` |

Nowa komenda = osobna decyzja designerska + wpis w tej tabeli (nie synonim w tekście karty).

---

## 2. Etykiety strukturalne

| Etykieta | Forma kanoniczna |
| :--- | :--- |
| **Limit:** | `Limit: 1 / gracza / Erę.` · `Limit: 1 / Erę.` · `Limit: 1 nasłanie / gracza / Erę.` · `Limit: bez ruchu Agenta w tej Erze.` |
| **Łamie regułę** | Zawsze Title Case: `Łamie regułę „…”:` (+ komendy §1). Po dekrecie: `DEKRET N — Łamie regułę „…”:` (nie małe `łamie`). Badge **Specjalna** — nie powtarzaj w `effect`. |
| **DEKRET N** | CAPS; N ∈ {1, 2}: `DEKRET N — Łamie regułę „…”:` |
| **EDYKT** · **EDYKT Ery.** | CAPS; lead Talii Czasu. **`EDYKT.`** = skutek trwały lub jednorazowy bez limitu Ery (`do końca gry`, natychmiastowe `Wymuś`/`Umieść`). **`EDYKT Ery.`** = skutek **tej Ery** (Herezja / ruch / Hak w oknie Ery). |
| **Odmowa:** | Po **Wymuś** spełnienie Haka: `Odmowa: +N Herezja.` |
| **zwycięstwo** | Token końcowy (mała litera): `…: zwycięstwo.` |

---

## 3. Rzeczowniki i nazwy własne

Wyłącznie te terminy (odmiana dozwolona: Agenta, Lokacji, Herezję, złota, Haka, …).

| Termin | Uwagi |
| :--- | :--- |
| Agent | Figurka gracza |
| Lokacja | Węzeł planszy; nazwy: Trybunał, Pałac, Lochy, Rynek, Gildia |
| Herezja | Tor 0–10 |
| Złoto | |
| Hak | [`haki.md`](haki.md) |
| Relikwia | |
| Fragment | |
| Stos | |
| Inkwizytor | |
| Era | |
| Werdykt | [`werdykt-stolu.md`](werdykt-stolu.md) |
| Autodafé | |
| Podwójny | |
| Areszt | Strefa w Lochach |
| Lochy | |
| Dekret | |
| Upadek | |
| Szlak Morski | |
| Przesłuchanie | Procedura: [`lochy-przesluchania.md`](lochy-przesluchania.md) |
| rywal | Inny gracz (cel) |
| gracz | |
| głos | Werdykt; domyślna **waga 1** — [`werdykt-stolu.md`](werdykt-stolu.md) |
| waga | Mnożnik głosu przy Werdykcie (`waga 2` = głos liczy się podwójnie) |
| większość | Werdykt |
| karta | |
| reguła | Karta specjalna |
| spełnienie | Hak |
| ogłoszenie | Autodafé |
| nasłanie | Limit Inkwizytora |
| Czysta · Obserwowana · Krytyczna | Strefy Herezji — [`poziom-herezji.md`](poziom-herezji.md) |
| Cienie · Kabała · Korona · Oficjum · Gildia | Frakcje (Gildia = też lokacja) |
| Remis | Edykt — równa Herezja |
| decyzja stołu | Remis przy edykcie |

---

## 4. Klej (słowa funkcyjne)

Jedyna dozwolona „gramatyka” poza §1–3. Nic poza tą listą. Każdy token poniżej jest hasłem leksykonu.

**Przyimki / spójniki:** `o` · `do` · `z` · `ze` · `na` · `w` · `lub` · `oraz` · `i` · `vs` · `wobec` · `po` · `bez` · `od` · `Podczas`

**Zaimek / określnik:** `swój` · `swojego` · `swoją` · `swoje` · `swoim` · `Twój` · `Twojego` · `Twoją` · `Twoje` · `ten` · `ta` · `to` · `tym` · `tej` · `tych` · `tego` · `tę` · `1` · `N`

**Osoba / stan:** `masz` · `ma` · `nie` · `jest` · `są` · `był` · `była` · `zagrywa` · `odmówi` · `otrzymuje` · `otrzymaną` · `liczy` · `się`

**Znaki:** `.` · `:` · `—` · `/` · `+` · `≥` · `–` · `„”` · `()`

**Frazy porównania (zamknięte):** `dokładnie` · `sąsiedniej` · `aresztowanego` · `obecny` · `obecnych` · `aktywne` · `ujawniony` · `właśnie` · `końca gry` · `tej Ery` · `tej lokacji` · `następnej Ery` · `następnym Werdykcie` · `podwójnie` · `Herezja ≥ N` · `Herezję N–N` · `z dala od` · `każdy` · `inny` · `najniższą` · `pierwszy` · `kluczowej` · `łamie` · `tylko` · `Twój głos ma wagę N` · `bez ruchu Agenta w tej Erze`
Nowe słowo funkcyjne = wpis tutaj, nie improwizacja na karcie.

---

## 5. Szablony (jedyna dozwolona składnia zdań)

`effect` = zero lub więcej linii z poniższych form. Slot `[Komenda…]` = wyłącznie §1 (+ argumenty z §3–4).

| Id | Forma | Użycie |
| :--- | :--- | :--- |
| S1 | `[Komenda…].` | Zwykła akcja |
| S2 | `Limit: ….` | Anti-AP (§2) |
| S3 | `Po ogłoszeniu Autodafé [Komenda…].` | Timing Autodafé |
| S4 | `Jeśli [stan z §3–4]:` + nowa linia `[Komenda…].` (lub `zwycięstwo.`) | Warunek stanu **lub** trigger reakcji — **nigdy** `Jeśli …, Komenda` w jednej linii |
| S5 | *(zarezerwowane — używaj S4; słowo warunku tylko **Jeśli**)* | — |
| S6 | `Podczas Werdyktu, po ujawnieniu większości:` + nowa linia `[Komenda…].` | Okno Werdyktu |
| S7 | `Łamie regułę „…”:` + nowe linie (S1 / S4) · `DEKRET N — Łamie regułę „…”:` + nowe linie | Karta specjalna (badge **Specjalna**; bez powtórzenia typu w tekście) |
| S8 | `EDYKT.` / `EDYKT Ery.` + linie S1–S4 / S9–S12 | Talia Czasu |
| S9 | `[Cel]: +N Herezja.` | Edykt / zbiorowa Herezja (bez **Wskaż**); np. `Każdy gracz z Agentem na Rynku: +1 Herezja.` |
| S10 | `Odmowa: +N Herezja.` | Kara Haka (§2) |
| S11 | `[Adresat]: [Komenda…].` | Edykt — adresat frakcji / warunkowy wykonuje komendę z §1; np. `Gracz Cieni: Przesuń…`. PnP: wiersz adresata + wiersz komendy (pogrubionej). Hak: `…: Załóż Hak na rywala.` |
| S12 | `Remis: decyzja stołu.` | Edykt — remis Herezji / wyboru |
| S13 | `W następnym Werdykcie Twój głos ma wagę N.` | Siła głosu (Korona) |
| S14 | `Limit: bez ruchu Agenta w tej Erze.` | Anti-AP ruchu (np. po reakcji) |

**Zakaz:** inne otwarcia zdań, synonimy komend, proza spoza szablonów. **Zakaz:** `Gdy` (zawsze `Jeśli`).

### Poza `effect`

| Treść | Gdzie |
| :--- | :--- |
| Herezja na zagrywającego (liczba) | `heresy` — pigułka `[🔥 N]` |
| Klimat / powód fabularny Herezji | opcjonalnie `heresy_text` — bez powtarzania mechaniki |
| Koszt złota | `cost_gold` |
| Herezja na rywala | komenda **Wskaż** w `effect` |
| Typ Reakcja / Akcja / … | badge `type` + `layer` |
| Smak przy stole (drukowane) | `lore` — bez Teach/sim/ID kart/żargonu balansu |

---

## 6. Legacy → kanon (do wyparcia z kart)

| Legacy (zakazane) | Kanon |
| :--- | :--- |
| `Zapłać N złota` | `cost_gold` |
| `Ty: +N Herezja` | `heresy` (pigułka); opcjonalnie smak w `heresy_text` |
| „bez Herezji” / „Ty nie…” w `heresy_text` | usuń — pigułka wystarczy; `heresy_text` = wyłącznie klimat |
| `Teach A` / `sim` / `reposition` / ID kart w `lore` | usuń — `lore` = klimat przy stole; notatki → `playtesting/` |
| `Reakcja.` w `effect` | usuń (badge `type`) |
| `SIGNATURE` / `Signature` w `effect` | usuń (badge **Specjalna**); zostaw `Łamie regułę „…”:` · Korona: `DEKRET N — Łamie regułę …` |
| `— łamie regułę` (małe ł) | `— Łamie regułę` |
| `Anuluj` / `Prawo stołu:` | usunięte z leksykonu — nie używaj |
| `A:` / `B:` / `C:` / warstwy w `effect` | usuń; jedna delta warstwy C (teach → playtesting) |
| `heresy ≥ 1` | `Herezja ≥ 1` |
| `Gdy …` / `Jeśli …, [Komenda]` w jednej linii | `Jeśli …:` + nowa linia z komendą (S4) |
| `możesz` / `może` | usuń; obowiązkowa komenda albo warunek S4 |
| `figurka idzie do` / `figurka do Lochów` | **Aresztuj** |
| `Załóż Hak na dowolnego/wybranego gracza` · `…na wskazanego rywala` · `…na gracza` (wolny cel) | `Załóż Hak na rywala.` |
| `Załóż Hak na dowolnego gracza z Herezją ≥ N` · `…na gracza z…` | `Załóż Hak na rywala z Herezją ≥ N.` / `…z Agentem…` |
| `albo` (w `effect`) | `lub` |
| `Załóż Hak na …` z cyfrą `1` | `Załóż Hak na …` (bez zbędnego `1`) |
| `Wymuszenie według reguł Haków` | usuń (reguła w [`haki.md`](haki.md) po **Załóż**) |
| `(Herezja obecnych)` / „ten pożar nie…” / „musisz mieć już Hak” | usuń — wynika z **Wymuś** / mechanik |
| `(bez progu Herezji)` i inne „bez X” bez delty | usuń |
| `natychmiast sprawdź wygraną` | `zwycięstwo` / reguła frakcji po **Oznacz** |
| dowolna proza spoza §1–5 | przeredaguj do szablonu lub rozszerz leksykon |
