# Roadmap — INQUISITIO 1492

## Faza 0 — Koncepcja ✅

- [x] Dokument koncepcyjny (GDD)
- [x] Struktura repozytorium
- [x] Opisy frakcji i lokacji (szkice)

## Faza 1 — Prototyp papierowy ✅

- [x] 10 kart startowych × 5 frakcji (`game/cards/factions/`)
- [x] Talia Czasu — min. 8 wydarzeń historycznych (`game/cards/time-deck/`)
- [x] Szkic planszy 5 lokacji (`game/board/`)
- [x] Planszetki graczy z Torem Herezji 0–10
- [x] Szkic zasad (`docs/rules/`)

## Faza 2 — Playtesting & balans

Infrastruktura w `playtesting/` gotowa (setupy, protokół 7 vs 8, macierz Herezji, szablony sesji).  
**Silnik symulacji intryg:** [`../sim/`](../sim/) — batch A/B, agenci polityczni, raporty w `playtesting/sim-reports/`.  
Poniższe punkty sesyjne ludzkie odhaczasz **po realnych rozgrywkach** — nie wcześniej.

- [ ] Sesje 2–3 graczy (uproszczony setup) — setup: [`../playtesting/setups.md`](../playtesting/setups.md)
- [ ] Sesje 4–5 graczy (pełny asymetryczny setup)
- [ ] Test progu oskarżenia: **7** vs **8** — protokół + `python -m inquisitio compare` ([`../sim/README.md`](../sim/README.md))
- [ ] Kalibracja kosztów Herezji kart (+1 / +2 / +3) — macierz: [`../playtesting/heresy-calibration.md`](../playtesting/heresy-calibration.md)
- [x] Szablony notatek w `playtesting/sessions/` (README + `_TEMPLATE.md`)
- [x] Silnik symulacji (`sim/`) z agentami intrygi + batch raportami

## Faza 3 — Produkcja wizualna

- [ ] Paleta: czerwień, złoto, czerń, pergaminowa biel
- [ ] Ikony: intryga, skrytobójstwo, relikwia, herezja, proces
- [ ] Pixel art lokacji i frakcji (`assets/art/`, `assets/icons/`)
- [ ] Prototypy komponentów (`assets/prototypes/`)

## Faza 4 — Rulebook & gotowość do wydania prototypu

- [ ] Pełny rulebook PL
- [ ] Lista komponentów finalna
- [ ] Quick-start / teach sheet
- [ ] FAQ z testów
