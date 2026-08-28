[Strona główna](../../README.md) > [Gra](../README.md) > [Karty](README.md)

---

# SCHEMA kart — prototyp intrygi

Frontmatter YAML jest **jedynym źródłem** treści karty (body po `---` puste).
**Nie ma `table_note`.** Cały opis z dawnego Efektu + Przy stole jest w polach poniżej.

**Zbiorczy przegląd wszystkich kart:** [`KATALOG.md`](KATALOG.md) (auto-generowany z plików poniżej; `python3 tools/cards/build_catalog.py`).

**Słownictwo `effect`:** [`../mechanics/leksykon.md`](../mechanics/leksykon.md) — **zamknięty** słownik (komendy, klej, szablony). Słowo spoza leksykonu = błąd.

## Pola na karcie PnP

**Strefy layoutu (generator):** pasek frakcji (lewa krawędź) → **HDR** (nazwa, type-badge, pigułki; `heresy_text` tylko gdy `heresy ≠ 0`) → **slot art** (~12 mm placeholder) → **EFFECT** (`effect`, banery Łamie/EDYKT/DEKRET) → **FOOT** (`lore`, niski kontrast).

| Pole | Rola | Przykład |
| :--- | :--- | :--- |
| `cost` | Koszt w złocie (pigułka gdy > 0) | `1`, `2` |
| `effect` | Instrukcja akcji | `Przesuń swojego Agenta o 1 lokację.` |
| `heresy` | Liczba (pigułka gdy ≠ 0) | `0`, `1`, `2` |
| `heresy_text` | Klimat / powód fabularny akcji | `Konfiskata majątku skazańców to prawny obowiązek trybunału.` |
| `lore` | Klimat przy stole (drukowane) | `Rywale widzą paliwo Oficjum — kasę pod areszt i przesłuchanie.` |

### Podział

- **`effect`** — reguły wg [`../mechanics/leksykon.md`](../mechanics/leksykon.md): lead komendy/etykiety, Title Case / CAPS wg leksykonu, **zero prozy**. Bez „Zapłać N” (→ `cost`), bez „Ty: +N Herezja” (→ `heresy`).
- **`heresy`** — jedyny wskaźnik mechaniczny Herezji na zagrywającym (pigułka `[🔥 N]`).
- **`heresy_text`** — **wyłącznie** klimat, historia i powód fabularny. Nie powtarza ani nie tłumaczy mechaniki. Pole opcjonalne — pomiń, gdy akcja nie wymaga dodatkowego smaku.
- **`lore`** — szept przy stole / konsekwencja społeczna. **Nie** notatki Teach, sim, ID kart, warstw A/B/C ani żargon EN.
- Herezja na rywala (`Wskaż rywala: +1 Herezja`) zostaje w **`effect`**.

### `heresy_text` — zasady pisania

**Gdy `heresy == 0`:** krótkie zdanie budujące klimat — dlaczego akcja jest bezpieczna politycznie lub religijnie w Toledo 1492 (np. *„Królewski nakaz wiąże bez pytania biskupów o zgodę”*). Jeśli karta nie wymaga opisu — **pomiń pole**.

**Gdy `heresy > 0`:** zwięzły opis skandalu, plotki lub otwartego naruszenia prawa (np. *„Częste wzywanie Inkwizytora budzi niepokój samych kardynałów”*).

**Styl:** kronika lub szept w sali tronowej. Zero żargonu planszówkowego.

**Zakaz w `heresy_text`:** powtarzanie pigułki i zasad — m.in. „bez Herezji”, „zero Herezji”, „czysta ekonomia”, „Ty nie…”, „na Ciebie”, „nie dodaje Herezji”, „sweet spot”, „efekt karty”.

### `lore` — zasady pisania

**Tak:** klimat, napięcie przy stole, co widzą rywale.  
**Nie:** `Teach A/B/C`, `Cel A:`, ID kart (`so-04`, `kt-06+`), `sim`, `warstwa`, `reposition`, `double-dip`, `sweet spot`, `Finisher`, `czysta ekonomia`, angielski żargon balansu.

Notatki playtestowe → [`data/playtesting/`](../../data/playtesting/), nie na kartę.

## Meta (zsynchronizowane z `game_config.yaml`)

`id`, `name`, `faction`, `type`, `layer`, `cost`, `heresy`, `tags`.  
*(Flagi opcjonalne pod sim: `agents`, `target_heresy`, `creates_hook`, `breaks_rule`, `gold`, `arrest` — obecne w `game_config.yaml`, w plikach `.md` pomijane gdy fałszywe/zerowe).*

## Przykład

```yaml
---
id: so-01
name: Patrol Familiariuszy
faction: swiete-oficjum
type: akcja
layer: A
cost: 1
heresy: 0
tags:
- move
effect: Przesuń swojego Agenta o 1 lokację.
heresy_text: Familiariusze obchodzą miasto pod szyldem porządku i prawa.
lore: Cichy obrót przed patrolem Inkwizytora albo zbliżenie do rywala pod areszt.
---
```

```yaml
---
id: so-04
name: Publiczne Ostrzeżenie
faction: swiete-oficjum
type: akcja
layer: A
cost: 1
heresy: 1
tags:
- inquisitor
- heresy
effect: |
  Przesuń Inkwizytora do lokacji ze swoim Agentem.
  Limit: 1 nasłanie / gracza / Erę.
heresy_text: Częste wzywanie Inkwizytora budzi niepokój samych kardynałów.
lore: Oficjum nasyła Inkwizytora przed Autodafé. Stół przestawia plany.
---
```
