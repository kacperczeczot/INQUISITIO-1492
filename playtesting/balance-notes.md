# Playtesting — notatki balansu (dramat)

Sim filtruje: deadlocki, legal moves, częstotliwość Autodafé / oskarżeń / Haków / Podwójnych.  
Wins w raporcie są informacyjne.  
**Werdykt fun = sesja ludzka** ([`sessions/_TEMPLATE.md`](sessions/_TEMPLATE.md)).

Setupy: [`setups.md`](setups.md) · Silnik: [`../sim/README.md`](../sim/README.md).

## Hipotezy dramatu

1. Próg oskarżenia **7** vs **8** — który daje lepszy dramat Werdyktu bez snowballa Oficjum?
2. **Herezja** — czy gracze boją się 6→7 i jednocześnie chcą mocy kart z `heresy`?
3. **Autodafé** — czy pali lokacje we właściwym tempie (max co 2 Ery)?
4. **Hak** — czy 1 wymuszenie/Erę wystarcza przeciw AP, a odmowa (+2 Herezja) boli?
5. **Podwójny** — czy wykrycie psuje zaufanie przy stole?
6. **Kabała 4–6** — czy stół wypycha ją poza sweet spot?
7. **Signature** — czy psują czytelność Inkwizytora/Werdyktu z Warstwy A?
8. Tempo Relikwii: czy 2 ewakuacje są osiągalne w 60–90 min?

## Symulacja (przed / obok stołu)

```bash
cd sim && source .venv/bin/activate
python -m inquisitio compare --games 50 --setup 3p-oficjum-alandalus-korona --seed 42
```

Wklej metryki z `playtesting/sim-reports/` do protokołu A/B poniżej (kolumny mogą być runami sim **lub** sesjami ludzkimi).

---

## Protokół A/B — próg oskarżenia 7 vs 8

Cel: hipoteza #1 (dramat Werdyktu vs snowball Oficjum).

### Procedura

1. Ten sam skład z [`setups.md`](setups.md) w obu sesjach / batchach.
2. **A** — próg **7**. **B** — próg **8**.
3. Nie zmieniaj kosztów `heresy` kart między A i B.
4. Zapisz metryki; wpisz werdykt.

### Metryki

| Metryka | Sesja A (próg 7) | Sesja B (próg 8) |
| :--- | :--- | :--- |
| Data / plik sesji lub raport sim | | |
| Gracze / frakcje / warstwa PnP | | |
| Liczba Er (avg) | | |
| Wejścia w Krytyczną | | |
| Oskarżenia / skazania | | |
| Autodafé | | |
| Haki utworzone / wymuszone | | |
| Podwójni | | |
| Stosy Oficjum | | |
| Emocja Werdyktu 1–5 (stół) / dramat sim | | |
| Snowball Oficjum 1–5 | | |
| Downtime bloku III/Werdykt (min) | | |

### Kryterium decyzji

- Preferuj próg, przy którym **Oskarżenie pada ≥1×** w typowej sesji, a Oficjum nie zbiera Stosów „za darmo” przed połową gry.
- Przy 7 za dużo oskarżeń / snowball → rozważ **8** lub obniż tempo `target_heresy`.
- Przy 8 martwa Krytyczna → zostań przy **7** lub podnieś Herezję na kartach.

### Werdykt

| Pole | Wartość |
| :--- | :--- |
| Wybrany próg | *(do wypełnienia po sesjach)* |
| Powód | |
| Data | |

---

## Co logować po każdej sesji (UX)

- Emocja Werdyktu, strach przed Inkwizytorem (1–5)
- Downtime / AP
- Czy Signature zepsuły teach Warstwy A

Szablon: [`sessions/_TEMPLATE.md`](sessions/_TEMPLATE.md).

---

## Log zmian balansu (prototyp polityczny)

| Data | Zmiana | Powód |
| :--- | :--- | :--- |
| 2026-08-12 | Przebudowa prototypu: Herezja + Inkwizytor + Werdykt + Lochy/Haki + Signature | Nowy rdzeń polityczny |
