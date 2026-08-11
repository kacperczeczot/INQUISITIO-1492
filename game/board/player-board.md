# Planszetka gracza — Tor Herezji (prototyp)

Wydrukuj **1 na gracza** (A5 lub pół A4). Uniwersalna planszetka — wpisz / wklej cel frakcji z [`../factions/`](../factions/).

Szczegóły stref: [`../mechanics/poziom-herezji.md`](../mechanics/poziom-herezji.md).

---

## Layout do wydruku

```
┌─────────────────────────────────────────────────────────────┐
│  INQUISITIO 1492 — PLANSZETKA GRACZA                        │
│  Frakcja: _______________________________                   │
│  Cel zwycięstwa: _________________________________________  │
│  _________________________________________________________  │
├─────────────────────────────────────────────────────────────┤
│  TOR HEREZJI  (znacznik start: 0)                           │
│                                                             │
│   CZYSTA          OBSERWOWANA         KRYTYCZNA / HERETYK   │
│  ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐             │
│  │ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │10 │             │
│  └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘             │
│    brak podejrzeń   alchemia / pakty    oskarżenie możliwe  │
│    (bezpieczne)     (sweet spot Kabały) (próg prototypu: 7) │
├──────────────────────┬──────────────────────────────────────┤
│  ZŁOTO               │  WPŁYW / KONTROLA                    │
│  ○ ○ ○ ○ ○ ○ ○ ○     │  Trybunał □□  Pałac □□  Rynek □□     │
│  (żetony)            │  (wg frakcji)                        │
├──────────────────────┼──────────────────────────────────────┤
│  AGENCI (3)          │  SCHOWEEK                            │
│  na planszy: ○ ○ ○   │  Relikwie: [ ][ ][ ]                 │
│  w Lochach:  □ □ □   │  Wskazówki Kodeksu: [ ][ ][ ][ ]     │
│  na stosie:  ▲ ▲ ▲   │  Żetony Upadku (Gildia): [ ][ ]      │
│                      │  Stosy (Oficjum): [ ][ ][ ]          │
├──────────────────────┴──────────────────────────────────────┤
│  RĘKA / LIMIT: 5     ODRZUCONE: _____                       │
│  Notatki sesji: ___________________________________________ │
└─────────────────────────────────────────────────────────────┘
```

---

## Pola — skrót

| Pole | Start | Uwagi |
| :--- | :--- | :--- |
| Tor Herezji | **0** | Znacznik płomienia / pionek |
| Złoto | **2** (prototyp) | Bank wspólny poza planszetką |
| Agenci | **3** na planszy | Max 3–4 wg inventory; prototyp = 3 |
| Relikwie / Wskazówki | 0 | Frakcja-specific |
| Cel zwycięstwa | tekst | Skopiuj z karty frakcji |

## Cele do wklejenia (skrót)

| Frakcja | Cel |
| :--- | :--- |
| Święte Oficjum | Skazać **2** Agentów na stos (lub 4 Wpływ → 1 Stos) |
| Cienie Al-Andalus | Ewakuować **2** Relikwie poza planszę |
| Korona & Borgiowie | Kontrola **Pałacu 2** + **Rynku 2** (żetony) |
| Kabała z Toledo | Zebrać **4** Wskazówki Kodeksu |
| Gildia Cieni | Doprowadzić do **upadku 2** frakcji |

## Strefy (przypomnienie)

| Zakres | Strefa | Efekt |
| :---: | :--- | :--- |
| 0–3 | Czysta | Bezpieczne, słabsze akcje |
| 4–6 | Obserwowana | Czujność Inkwizycji; dostęp do zakazanych efektów |
| 7–10 | Krytyczna | Inni mogą **Rzucić Oskarżenie** (próg prototypu: **7**; wariant **8** → Faza 2) |
