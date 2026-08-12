[Strona główna](../README.md) > [Playtesting](README.md)

---


# Playtesting — balans (stan aktualny)

Sim filtruje: deadlocki, oskarżenia, Autodafé, Haki, Podwójni.  
**Werdykt fun = sesja ludzka** ([`sessions/_TEMPLATE.md`](sessions/_TEMPLATE.md)).

Setupy: [`setups.md`](setups.md) · Silnik: [`../sim/README.md`](../sim/README.md).

## Hipotezy (otwarte na stole)

1. Próg oskarżenia **7** vs **8** — dramat Werdyktu vs snowball Oficjum?
2. Sweet spot Kabały **4–6** — czy stół wypycha?
3. Tempo Relikwii — 2 ewakuacje w 60–90 min?

## Gate przed stołem

```bash
cd sim && source .venv/bin/activate
python -m inquisitio matrix --games 100 --layers A,B,C --seed 42
python -m inquisitio feel --setup 3p-oficjum-alandalus-korona --seed 42 --layer C
pytest tests/test_balance.py tests/test_smoke.py -q
```

Wysokie deadlocki C = blocker (napraw, nie drukuj).

## Stan teraz (seed 42, 100 gier / skład) — 2026-08-12

Matryca **30/30**, pytest **79**. Deadlocki ~0–0.4. Warstwa **C** = live-ready pod playtest.

### Wins C

| Setup | Oficjum | Cienie | Korona | Kabała | Gildia |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 3p Oficjum–Cienie–Korona | 24% | 34% | 42% | — | — |
| 3p Oficjum–Kabała–Gildia | 30% | — | — | 38% | 32% |
| 3p Cienie–Korona–Gildia | — | 34% | 29% | — | 37% |
| 3p Oficjum–Cienie–Gildia | 24% | 39% | — | — | 37% |
| 5p-full | 26% | 10% | 20% | 22% | 22% |

### Soft-spoty do stołu

- 3p z Koroną — Korona ~42% (w gate, lider)
- 5p Cienie — ~10% (dolna półka)
- A teach — Gildia/Korona często wygrywają tie-break (OK dla teach)

### Reguły win (C) — skrót

| Frakcja | Cel |
| :--- | :--- |
| Oficjum | 3 Stosy **lub** skazania (2@≤3p / 3@4–5p) |
| Cienie | 2 Relikwie + ścieżka |
| Korona | 2 Dekrety + ≥1 Hak (Era 7@3p / 6@4–5p); 5p też 1 Dekret+2 Haki od Ery 6 |
| Kabała | 3 Fragmenty + Herezja 4–6 (Era 7@3p / 6@4p / 5@5p) |
| Gildia | 2 upadki (3 bez Oficjum) |

Szczegóły: [`../docs/rules/ksiega.md`](../docs/rules/ksiega.md) · słownik: [`../docs/rules/slownik.md`](../docs/rules/slownik.md) · frakcje: [`../game/factions/`](../game/factions/).

## Po sesji

Loguj UX w `sessions/` — nie dokładaj tu changelogu iteracji sim.
