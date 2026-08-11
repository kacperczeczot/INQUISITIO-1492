# Playtesting — notatki balansu

## Hipotezy do sprawdzenia

1. Próg oskarżenia **7** vs **8** — który generuje lepszy dramat bez snowballa Inkwizycji?
2. Czy Kabała musi „żyć” w strefie 4–6, czy próg jest za wąski?
3. Czy Gildia Cieni ma wystarczająco narzędzi wrabiania przy 2–3 graczach?
4. Tempo Relikwii: czy 2 ewakuacje są osiągalne w 60–90 min?

## Szablon sesji

Użyj pełnego szablonu: [`sessions/_TEMPLATE.md`](sessions/_TEMPLATE.md)  
Kopiuj do `sessions/YYYY-MM-DD-skrot.md` (opis: [`sessions/README.md`](sessions/README.md)).

Setupy: [`setups.md`](setups.md) · Macierz Herezji kart: [`heresy-calibration.md`](heresy-calibration.md)

### Symulacja (zalecane przed / obok stołu)

```bash
cd sim && source .venv/bin/activate
python -m inquisitio compare --games 200 --setup 3p-oficjum-alandalus-korona --seed 42
```

Wklej metryki z `playtesting/sim-reports/compare-*.md` do tabeli A/B poniżej (kolumny Sesja A/B mogą być runami sim).  
Szczegóły silnika: [`../sim/README.md`](../sim/README.md).

---

## Protokół A/B — próg oskarżenia 7 vs 8

Cel: rozstrzygnąć hipotezę #1 (dramat przy stole vs snowball Oficjum).

### Procedura

1. Wybierz skład frakcji z [`setups.md`](setups.md) (najlepiej ten sam skład w obu sesjach).
2. **Sesja A** — próg **7** (domyślny z zasad). Zapisz metryki poniżej.
3. **Sesja B** — próg **8**, ten sam skład / zbliżona liczba graczy. Zapisz metryki.
4. Porównaj wiersze A vs B; wpisz decyzję w „Werdykt”.

Nie zmieniaj kosztów `heresy` kart między A i B — kalibracja kart to osobna pętla (`heresy-calibration.md`).

### Metryki (wypełnij na sesję)

| Metryka | Sesja A (próg 7) | Sesja B (próg 8) |
| :--- | :--- | :--- |
| Data / skrót pliku sesji | sim balance-v10 / compare 2026-08-11 (150–200 gier, 3p O/A/K) | j.w. |
| Gracze / frakcje | Oficjum + Al-Andalus + Korona | to samo |
| Liczba Er | avg ~4.4 | avg ~4.4 |
| Wejścia w strefę Krytyczną (łącznie, wszyscy) | ~1.5 / grę | niżej |
| Liczba **Rzutów Oskarżenia** | **~1.5 / grę** | **~1.0 / grę** |
| Liczba Procesów zakończonych wyrokiem | umiarkowane | niżej |
| Stosy Oficjum na koniec | ~0.5 / grę | niżej |
| Czy ktoś wygrał „z procesu” / Stosu? (tak/nie + kto) | Oficjum ~14% winrate | Oficjum ~6% |
| Ewakuowane Relikwie / Wskazówki / Kontrole (skrót) | Korona ~52% / Al-Andalus ~35% / Oficjum ~14% | Korona ~65% / Al-Andalus ~29% / Oficjum ~6% |
| Subiektywny dramat (1–5) | 3–4 (sim) | 3 (sim) |
| Subiektywny snowball Oficjum (1–5, 5 = za mocno) | 2 | 1 |

### Kryterium decyzji

- Preferuj próg, przy którym **Oskarżenie pada ≥1×** w typowej sesji, ale Oficjum nie zbiera 3 Stosów „za darmo” przed Erą 4.
- Jeśli przy 7: za dużo oskarżeń / Oficjum wygrywa zbyt często → zostań przy **8** (lub obniż `target_heresy` Gildii).
- Jeśli przy 8: Krytyczna jest martwa, nikt nie oskarża → zostań przy **7** (lub podnieś tempo Herezji na kartach +2/+3).

### Werdykt (po min. 1× A i 1× B)

| Pole | Wartość |
| :--- | :--- |
| Wybrany próg na lock | **7** (sim v10) |
| Powód (1–2 zdania) | Przy 7 oskarżenia ~1.5/grę i Oficjum ~14% winrate; przy 8 Oficjum spada do ~6% a Korona ~65%. Potwierdzić przy stole. |
| Data decyzji | 2026-08-11 (sim v10) |

---

## Log zmian balansu

| Data | Zmiana | Powód |
| :--- | :--- | :--- |
| — | — | Start repo |
| 2026-08-11 | Korona win = **2+2** Kontrola; nerf `kb-01/05/07/09/10`; Pieczęć nie instant-win | Sim: Korona ~96% w 3p, gry w ~2.6 Eru |
| 2026-08-11 | Kabała: max 1 Wskazówka/Era, clue wymaga strefy Obserwowanej; nerf `kt-03/08` | Sim: Kabała ~93% w 3p z Gildią |
| 2026-08-11 | Proces: obrona **4 zł / 3 karty**; scrutiny +1 Herezji dla lidera Intrygi w Fazie IV | Za mało oskarżeń / wyroków; Oficjum 0% |
| 2026-08-11 | Agenci: słabsze unikanie Herezji, silniejsze wrabianie vs lider | Mid-heresy martwa w matchupach Korony |
| 2026-08-11 | **Pass 2 (v10):** bugfix `caa-06` (ewakuacja bez Floty za darmo); nerf grabienia Relikwii z puli; Oficjum win **2 Stosy** + **4 Wpływ→Stos** (tylko gdy oskarża / Agent w Trybunale·Lochach); Flota w talii czasu wcześniej; bez konfiskaty clues przy oczyszczeniu; Gildia bez auto-Upadku z procesu | Al-Andalus 100%/62%; Oficjum 0–3%; potem Oficjum 95% przy farmie Wpływu |
| 2026-08-11 | Sim v10 (200 gier): 3p O/A/K ≈ **52/35/14**; oskarżenia ~1.5/grę; próg **7** lepszy niż 8 | Meta grywalna; Kabala/Oficjum w 5p nadal do dogrania przy stole |
| 2026-08-11 | **Skill > luck:** Talia Czasu = odkryj 2 / wybór dogrywającego; Szlak za **3 zł**; mulligan do 2; 1. gracz bez RNG; exploration agentów 5%; usunięto force-insert Floty | Los Talii Czasu / Floty nie może dyktować wyniku |
