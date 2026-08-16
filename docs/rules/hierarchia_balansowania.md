[Strona główna](../../README.md) > [Dokumentacja](../README.md) > [Zasady](README.md)

---

# Hierarchia Balansowania Gry — INQUISITIO-1492

Struktura hierarchiczna określająca ścisłą kolejność optymalizacji i dostrajania parametrów gry w oparciu o symulacje Monte Carlo i telemetrię 5 filarów.

---

## 0. Zasada spłaszczania

**Unikamy skalowania po liczbie graczy.** Jedna wartość na 3p/4p/5p jest domyślna.

Spłaszcz, gdy pomiar (ten sam seed, ten sam N gier) daje wynik **lepszy**, **podobny**, albo gorszy tylko **małym kosztem**. Zostaw schodek `3p`/`4p`/`5p` wyłącznie gdy jedna liczba realnie psuje czerwone linie — i nazwij powód. V-kształt (osobny 4p) i „proteza na setup” nie są skalowaniem.

Dozwolone wyjątki to tożsamość stołu, nie liczba krzeseł: np. Gildia **3 upadki bez Oficjum**. Strefy Herezji mogą iść za **jednym** progiem oskarżenia, nie odwrotnie.

---

## 1. Poziom 1: Główne Mechaniki Systemowe (Global System Core)

Fundamenty systemu obowiązujące bezwzględnie we wszystkich wariantach gry:

- **Limit kart na ręce:** `5 kart`
- **Ekonomia:** `4 złote` na start · Dochód `+1 złoty` w Fazie III (Kronika) + opcja Akcji Gospodarczej (+1 zł) w Fazie I (Intryga)
- **Maksymalny limit Er:** `11 Er` (remis po 8 Er -> gracz najbliższy celowi, następnie najniższa Herezja)
- **Strefy i pasma Herezji:** 
  - **Czysta:** `0–3 Herezji`
  - **Obserwowana:** `4–5 Herezji (3p) / 4–6 (4–5p)`
  - **Krytyczna / Heretyk:** `6–10 Herezji (3p) / 7–10 (4–5p)`
- **Próg Oskarżenia na Dworze:** `Herezja ≥ 6 (3p) / ≥ 7 (4–5p)`
- **Liczba Agentów per gracz:** `3 Agenci`
- **Cooldown Autodafé Inkwizytora:** Max `co 3 Ery`

---

## 2. Poziom 2: Frakcyjne Warunki Zwycięstwa

Progi wygranej. Różnice 3p/4p/5p poniżej to wyjątki pod zasadą spłaszczania, nie wzorzec.

| Frakcja | Rozgrywka 3-osobowa (3p) | Rozgrywka 4-osobowa (4p) | Rozgrywka 5-osobowa (5p) |
| :--- | :--- | :--- | :--- |
| **Święte Oficjum** | **3 Stosy** lub 2 Skazania | **3 Stosy** lub 3 Skazania | **4 Stosy** lub 4 Skazania |
| **Cienie Al-Andalus** | **2 Relikwie** + Ścieżka (Era 6+) | **2 Relikwie** + Ścieżka (Era 5+) | **2 Relikwie** + Ścieżka (Era 5+) |
| **Korona & Borgiowie** | **2 Dekrety** + ≥0 Haków (Era 5+) | **2 Dekrety** + ≥1 Hak (Era 5+)<br>lub **1 Dekret + 2 Haki** | **2 Dekrety** + ≥1 Hak (Era 5+)<br>lub **1 Dekret + 2 Haki** |
| **Kabała z Toledo** | **3 Fragmenty** + Pasmo 3–8 (Era 7+) | **3 Fragmenty** + Pasmo 3–8 (Era 6+) | **3 Fragmenty** + Pasmo 3–8 (Era 6+) |
| **Gildia Cieni** | **2 Upadki** *(3 bez Oficjum)* | **2 Upadki** *(3 bez Oficjum)* | **2 Upadki** *(3 bez Oficjum)* |

---

## 3. Poziom 3: Ekonomia i Koszty Kart Katalogu (Card Economy & Action Tuning)

Koszty złotowe oraz przydział efektów kart w poszczególnych warstwach:

- **Koszt zagrania kart:** Dociąg, alchemia, areszty i wymuszenia zbalansowane w Warstwach A, B i C.
- **Karty Signature (Warstwa C):**
  - Święte Oficjum `so-10`: koszt 2zł
  - Cienie Al-Andalus `caa-10`: koszt 2zł
  - Korona & Borgiowie `kb-10`: koszt 2zł
  - Kabała z Toledo `kt-10`: koszt 1zł
  - Gildia Cieni `gc-10`: koszt 2zł

---

## 4. Poziom 4: Mikro-Symetria i Warianty Setupów (Setup Edge-Cases)

Dostrajanie unikalnych zestawień frakcji przy stole:

- Warianty bez Oficjum (np. `3p-cienie-korona-gildia` / `4p-no-oficjum`)
- Warianty bez Korony / bez Cieni / bez Kabały
- Analityka 5 filarów (Pas Biedy < 30%, Deadlocki < 15%, Autodafé > 0.5)
