[Strona główna](../../README.md) > [Gra](../README.md) > [Mechaniki](README.md)

---

# Wielki Inkwizytor

> **Źródło szczegółów** dla haseł [Inkwizytor](../../docs/rules/slownik.md#inkwizytor), [Autodafé](../../docs/rules/slownik.md#autodafé), [Nasłanie](../../docs/rules/slownik.md#nasłanie) w [`slownik.md`](../../docs/rules/slownik.md).  
> **Patrz także:** [`ksiega.md`](../../docs/rules/ksiega.md) (E.I) · [`poziom-herezji.md`](poziom-herezji.md) · [`../board/locations.md`](../board/locations.md)

NPC na planszy — **broń publiczna**. Spala **lokacje**; gracze manewrują wokół niego albo nasyłają go na siebie nawzajem. Święte Oficjum ma łatwiejszy dostęp do nasłań, **nigdy** 100% własności.

## Komponent

1 figurka (większa niż Agent). Stany prototypu:

| Stan | Znaczenie |
| :--- | :--- |
| **Patrol** | Stoi w lokacji. Sam obecność nie aresztuje — robią to karty, Autodafé i reguły edyktów. |
| **Autodafé** | Lokacja płonie w Fazie Inkwizytora (patrz procedura). |

> **Obława** nie jest trzecim żetonem stanu — to efekt karty / Talii Czasu / „miękkie” Autodafé opisane tekstem.

## Faza I — procedura

1. **Reset / sprawdź** czy Autodafé jest dostępne (min. 1 pełna Era od ostatniego, chyba że karta specjalna łamie).
2. **Nasłania:** każdy gracz może raz na Erę ogłosić nasłanie (karta, Hak, reguła Oficjum). Konflikt: Oficjum wygrywa; potem 1. gracz; potem najniższa Herezja.
3. **Ruch Patrol:** przesuń Inkwizytora o **0 lub 1** lokację wzdłuż **krawędzi grafu** (sąsiedztwo w `game/board/locations.md`); przy nasłaniu / edykcie „w stronę X” — jeden krok po **najkrótszej ścieżce**; **bez nasłania** — najniższa Herezja wybiera, remis → 1. gracz.
4. **Autodafé (opcjonalne):** jeśli wolno i ktoś (zwykle Oficjum / karta) ogłasza — wykonaj procedurę poniżej w **bieżącej** lokacji Inkwizytora.

### Autodafé

1. Ogłoś lokację (tam, gdzie stoi figurka).
2. Każdy Agent rywala w lokacji:
   * **Strefa Czysta (0–3 Herezji):** Agent trafia do **Aresztu w Lochach** (+1 Herezja dla właściciela, bez Stosu dla Oficjum).
   * **Strefa Obserwowana / Krytyczna (≥4 Herezji):** Agent zostaje **spalony na Stosie** (+1 Herezja dla właściciela, +1 Stos dla Oficjum po **Ogłoś Autodafé**).
3. **Stos:** połóż **1 żeton Stosu** za wyeliminowanego Agenta rywala $\ge$4 Herezji po **Ogłoś Autodafé**. **Wymuś Autodafé** (edykt) = kroki 1–2 i 4–5 **bez** Stosu.
4. Relikwia w lokacji: **wraca do puli**.
5. Stan wraca do Patrol; zapisz „Autodafé w Erze N”.

## Limit anti-AP

- **1 nasłanie / gracza / Erę**
- **Autodafé max co 2 Ery** (bazowo)

## Warstwa A

Wystarczy ruch + rzadkie Autodafé + Herezja obecnych. Gate: stół **czuje** zagrożenie lokacją.

## Playtest

Czy Autodafé >1 / 2 Ery = za częste? Czy Oficjum snowballuje Stosami? Czy stół sojuszy się przeciw nasłaniom?
