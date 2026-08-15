[Strona główna](../../README.md) > [Gra](../README.md) > [Plansza](README.md)

---

# Planszetka gracza — mat pod komponenty

Wydrukuj **1 na gracza** (½ A4 = **210×148 mm**). Mata na żetony/figurki, nie karta do ołówka.

Szczegóły Herezji: [`../mechanics/poziom-herezji.md`](../mechanics/poziom-herezji.md).  
Cele: [`../factions/`](../factions/). Żetony: [`../components/print-3d.md`](../components/print-3d.md).

---

## Budżet mm (nie łamać)

```
210 × 148  (zewnętrzne)
└─ padding 3 mm → obszar roboczy 204 × 142
   ├─ NAGŁÓWEK     auto    frakcja 18 pt + cel 15 pt (wysokość = treść, zero dziury)
   ├─ gap           1.5 mm
   ├─ HEREZJA      28 mm   tytuł 13 pt + tor 18 mm + strefy 11 pt (tuż pod torem)
   ├─ gap           1.5 mm
   └─ KORPUS       1fr     reszta mm
        Warstwa C:
        ├─ rząd 1  ~1.07fr Agenci 70 | Złoto flex | Haki 48
        ├─ gap      2 mm
        └─ rząd 2  ~1fr    Limity flex (3 kolumny ✕+etykieta) | Postęp 72
        Warstwa A: jeden rząd 1fr
                   Agenci 70 | Złoto flex | Limit 36 | Postęp 72
```

**Limity Ery (C) — budżet szerokości:**  
`204 − 72 − 2 = 130 mm` na box → tytuł pełną szerokość, potem **3 równe kolumny** (~43 mm): żeton 12 mm nad etykietą.  
Nie układać etykiet w poziomie obok żetonu (3× „Przesłuchanie” nie mieści się).

**Twarde odciski:** Agent Ø20, żeton 20×20, Zużycie 12×12.  
Szerokość studni = liczba odcisków (+ pad), nie „wspólna kolumna z sąsiadem”.

Typografia (w budżecie): tytuł **18 pt** · cel **15 pt** · box **13 pt** · limity **12 pt** · tor/strefy Herezji **13 / 11 pt**.  
Nagłówek: rząd `auto` (nie sztywne mm) — dziura pod celem = błąd.  
Strefy Herezji: **bez** `margin-top: auto` — przyklejone pod tor 0–10.

---

## Strefy

| Strefa | Forma | Komponent |
| :--- | :--- | :--- |
| Herezja | tor 0–10 | 1 znacznik |
| Agenci | 3×○ | rezerwa |
| Złoto | tacka | stos monet |
| Haki (B+) | 2×□ | max 2 aktywne |
| Limity Ery | 1–3×□12 | żeton Zużycie |
| Postęp | 2–4×□ | żetony celu frakcji |

### Postęp

| Frakcja | n | Żeton |
| :--- | ---: | :--- |
| Oficjum | 4 | Stos |
| Cienie | 2 | Relikwia |
| Korona | 2 | Dekret |
| Kabała | 3 | Fragment |
| Gildia | 2 | Upadek |

### Świadomie poza matą

Pozycja Agenta = plansza/Areszt/Stos · ofiara Haka = na żetonie · Marionetka = nakładka na bazie · zero pól do pisania.

---

## Layout

```
┌─ 210 × 148 ─────────────────────────────────────────────┐
│ FRAKCJA                                                 │
│ Cel: …                                                  │  auto
├─────────────────────────────────────────────────────────┤
│ HEREZJA (*próg oskarżenia: 3p ≥6, 5p ≥8)                │
│ [0]…[10]                                                │
│ Czysta 0–3 | Obserwowana 4–6 | Krytyczna ≥7*            │  28 mm
├──────────┬────────────────────────────┬─────────────────┤
│ AGENCI   │ ZŁOTO (tacka)              │ HAKI            │
│ ○ ○ ○    │                            │ □ □             │  ~1fr
├──────────┴──────────────┬─────────────┴─────────────────┤
│ LIMITY  □ Nasłanie …    │ POSTĘP  □ □ (□ □)             │  ~1fr
└─────────────────────────┴───────────────────────────────┘
```
