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
   ├─ HEREZJA      28 mm   tytuł 13 pt + tor 18 mm + strefy 11 pt (siatka 5:2:4 pod 11 pól)
   ├─ gap           1.5 mm
   └─ KORPUS       1fr     reszta mm (~96 mm)
        Warstwa C:
        ├─ rząd 1  ~1.07fr Agenci 70 | Złoto flex (~82 mm) | Haki 48
        ├─ gap      2 mm
        └─ rząd 2  ~1fr    Limity 116 mm (3 kolumny po ~36 mm) | Postęp flex (~86 mm)
        Warstwa A: jeden rząd 1fr
                   Agenci 70 | Złoto flex | Limit 36 | Postęp 72
```

**Limity Ery (C) — budżet szerokości:**  
`116 mm` na box → tytuł pełną szerokość, potem **3 równe kolumny** (~36 mm): żeton 12 mm nad etykietą.  
Mieści pełne etykiety (np. „Przesłuchanie”) bez obcinania.

**Postęp (C) — budżet szerokości i wysokości:**  
`86 mm` na box. Wszystkie frakcje mają zunifikowaną **tackę celu** z ikoną komponentu i docelową liczbą do zdobycia (`Cel: n`). Gracze odkładają na tackę zdobyte żetony (Stosy, Relikwie, Dekrety, Fragmenty, Upadki) bez sztucznych ograniczeń liczby stałych kratek.

**Twarde odciski:** Agent Ø20, żeton 20×20, Zużycie 12×12.  
Szerokość studni = liczba odcisków (+ pad), nie „wspólna kolumna z sąsiadem”.

Typografia (w budżecie): tytuł **18 pt** · cel **15 pt** · box **13 pt** · limity **11.5 pt** · tor/strefy Herezji **13 / 11 pt** · tacka celu **13 pt**.  
Nagłówek: rząd `auto` (nie sztywne mm) — dziura pod celem = błąd.  
Strefy Herezji: `grid-template-columns: 5fr 2fr 4fr;` — precyzyjnie dopasowane do 11 kratek (0–4: 5 pól, 5–6: 2 pola, 7–10: 4 pola).

---

## Strefy

| Strefa | Forma | Komponent |
| :--- | :--- | :--- |
| Herezja | tor 0–10 | 1 znacznik |
| Agenci | 3×○ | rezerwa |
| Złoto | tacka | stos monet |
| Haki (B+) | 2×□ | max 2 aktywne |
| Limity Ery | 1–3×□12 | żeton Zużycie |
| Postęp | tacka (Cel: n) | żetony celu frakcji |

### Postęp

| Frakcja | Cel | Komponent |
| :--- | ---: | :--- |
| Oficjum | 6 | Stosy |
| Cienie | 2 | Relikwie |
| Korona | 2 | Dekrety |
| Kabała | 2 | Fragmenty |
| Gildia | 8 | Upadki |

### Świadomie poza matą

Pozycja Agenta = plansza/Areszt/Stos · ofiara Haka = na żetonie · Marionetka = nakładka na bazie · zero pól do pisania.

---

## Layout

```
┌─ 210 × 148 ─────────────────────────────────────────────┐
│ FRAKCJA                                                 │
│ Cel: …                                                  │  auto
├─────────────────────────────────────────────────────────┤
│ HEREZJA                                                 │
│ [0]…[10]                                                │
│ Czysta | Obserwowana | Krytyczna (Oskarżenie)           │  28 mm
├──────────┬────────────────────────────┬─────────────────┤
│ AGENCI   │ ZŁOTO (tacka)              │ HAKI            │
│ ○ ○ ○    │                            │ □ □             │  ~1fr
├──────────┴──────────────┬─────────────┴─────────────────┤
│ LIMITY  □ Nasłanie …    │ POSTĘP (tacka: Cel n)         │  ~1fr
└─────────────────────────┴───────────────────────────────┘
```
