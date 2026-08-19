[Strona główna](../../README.md) > [Dokumentacja](../README.md) > [Zasady](README.md)

---

# Hierarchia Balansowania Gry — INQUISITIO-1492

Struktura hierarchiczna określająca ścisłą kolejność optymalizacji i dostrajania parametrów gry w oparciu o symulacje Monte Carlo i telemetrię 5 filarów.

---

## 0. Zasada Organicznego Projektowania i Zakaz Protez Konfiguracyjnych (Anti-Crutch Principle)

1. **Domyślna jedność zasad (Kanon 4p):**
   Podstawowym kanonem gry jest format 4-osobowy. Reguły Poziomu 1 (System) oraz Poziomu 2 (Warunki Zwycięstwa) powinny być domyślnie jednolite dla wszystkich składów (3p/4p/5p).

2. **Bezwzględny zakaz sztucznych protez balansowych:**
   **Kategorycznie zabrania się wprowadzania wyjątków dla 3p lub 5p, których celem jest jedynie zatuszowanie uszkodzonej mechaniki gry zamiast jej realnej naprawy.**
   - Wprowadzenie nienaturalnego progu (np. nagły skok progu herezji w 5p z 7 do 9) lub arbitralnych modyfikatorów tylko dlatego, że „w symulatorze podnosi to Global Score”, jest niedopuszczalne.
   - Jeśli format 3p lub 5p wykazuje odchylenie, **pierwszym obowiązkiem jest zdiagnozowanie mechaniki źródłowej** (dynamiki planszy, przepływu akcji, interakcji) i jej organiczne uzdrowienie.

3. **Kryteria dopuszczalności wyjątku — Ścisłe Uzasadnienie Fizyką Stołu:**
   Każdy wyjątek dla liczby graczy musi być **ściśle i logicznie uzasadniony fizyczną geometrią rozgrywki**:
   - **Skalowanie puli celów:** Liczba obcych agentów na planszy ($N=3 \rightarrow 6$ agentów, $N=4 \rightarrow 9$ agentów, $N=5 \rightarrow 12$ agentów) — wymóg stosów lub celów może rosnąć proporcjonalnie do puli rywali, aby zachować symetryczny wysiłek wygranej.
   - **Tożsamość obecności frakcji:** Np. brak Świętego Oficjum przy stole naturalnie zmienia warunki Gildii Cieni (3 Upadki zamiast 2).
   - **Zrozumiałość dla człowieka:** Wyjątek musi być prosty, elegancki i intuicyjny dla gracza czytającego instrukcję przy stole (np. w tabeli pomocy gracza), a nie stanowić ukrytego, zawiłego algorytmu.

4. **Ablacja ≠ gałka audytora:**
   Raport użyteczności może wyłączyć podsystem (Kronika, Szlak, patrol Inkwizytora, Gospodarcza = 0), żeby zmierzyć, czy żyje. Audytor **nie wdraża** wyłączeń ani skrajów — w tym `intrigue_gold` 1→0 (kasuje Akcję Gospodarczą, która dopiero dostała silnik). Kwota 1↔2 to żywe `±1`. Usunięcie mechaniki to decyzja po raporcie, nie pierwszy patch makro. Makro 4P: żywe `±1` L1/L2 (złoto, Gospodarcza **≥1**, próg oskarżenia, Obserwowana, Er, karty/erę, era Kabały/Cieni, CD Autodafé, ręka, liczniki C, szlak ±1). Lookahead 2D/3D **zapisuje** zweryfikowany wektor (komplementarność; gałka nie musi wygrywać 1D). Głębiej tylko gdy 4P score albo witalność bije held — jeździec Δ≈0 nie wchodzi. **Fundament przed wspinaczką:** poza czerwoną linią 15–35% makro **nie zapisuje** (HUD jak v0.98 ~4 pkt — gradient L2 to protezy). Najpierw ręczny L2/SSOT, aż ±1 wokół żywych celów psuje wynik (jak dekrety 2). Wspinaczka maximin tylko wewnątrz 15–35% w stronę 20–30%. Poza apply: agenci (SKU), Werdykt Tajny, tempo Kroniki (`freq` / OFF), split upadków, wskrzeszanie skasowanego YAML. **3p/5p nie ruszają gałek całego stołu.** Karty = audytor kanonu.

---

## 1. Poziom 1: Główne Mechaniki Systemowe (Global System Core)

Fundamenty systemu obowiązujące bezwzględnie we wszystkich wariantach gry:

- **Limit kart na ręce:** `5 kart`
- **Ekonomia:** `4 złote` na start · Dochód `+1 złoty` w Fazie III (Kronika) + opcja Akcji Gospodarczej (+1 zł) w Fazie I (Intryga)
- **Maksymalny limit Er:** `14 Er` (bezpiecznik + tie-break: najbliższy celowi, potem najniższa Herezja)
- **Strefy Herezji:** Czysta `0–4`; Obserwowana od `5` do `T−1`; Krytyczna `≥T`
- **Próg Obserwowanej:** `≥5` (Autodafé: Stos zamiast aresztu)
- **Próg Oskarżenia na Dworze:** `Herezja ≥ 7`
- **Liczba Agentów per gracz:** `3 Agenci`
- **Cooldown Autodafé Inkwizytora:** Max `co 3 Ery`

---

## 2. Poziom 2: Frakcyjne Warunki Zwycięstwa

Progi wygranej. Różnice 3p/4p/5p poniżej to wyjątki pod zasadą spłaszczania, nie wzorzec.

| Frakcja | Rozgrywka 3-osobowa (3p) | Rozgrywka 4-osobowa (4p) | Rozgrywka 5-osobowa (5p) |
| :--- | :--- | :--- | :--- |
| **Święte Oficjum** | **6 Stosy** lub 3 Skazania | **6 Stosy** lub 3 Skazania | **6 Stosy** lub 3 Skazania |
| **Cienie Al-Andalus** | **2 Relikwie** + Ścieżka | **2 Relikwie** + Ścieżka | **2 Relikwie** + Ścieżka |
| **Korona & Borgiowie** | **2 Dekrety** | **2 Dekrety** | **2 Dekrety** |
| **Kabała z Toledo** | **2 Fragmenty** (Era 6+) | **2 Fragmenty** (Era 6+) | **2 Fragmenty** (Era 6+) |
| **Gildia Cieni** | **8 Upadki** | **8 Upadki** | **8 Upadki** |

---

## 3. Poziom 3: Ekonomia i Koszty Kart Katalogu (Card Economy & Action Tuning)

Koszty złotowe oraz przydział efektów kart w poszczególnych warstwach:

- **Koszt zagrania kart:** Dociąg, alchemia, areszty i wymuszenia zbalansowane w Warstwach A, B i C.
- **Karty Signature (Warstwa C):**
  - Święte Oficjum `so-10`: koszt 5zł
  - Cienie Al-Andalus `caa-10`: koszt 0zł
  - Korona & Borgiowie `kb-10`: koszt 3zł
  - Kabała z Toledo `kt-10`: koszt 2zł
  - Gildia Cieni `gc-10`: koszt 4zł

---

## 4. Poziom 4: Mikro-Symetria i Warianty Setupów (Setup Edge-Cases)

Dostrajanie unikalnych zestawień frakcji przy stole:

- Warianty bez Oficjum (np. `3p-cienie-korona-gildia` / `4p-no-oficjum`)
- Warianty bez Korony / bez Cieni / bez Kabały
- Analityka 5 filarów (Pas Biedy < 30%, Deadlocki < 15%, Autodafé > 0.5)
