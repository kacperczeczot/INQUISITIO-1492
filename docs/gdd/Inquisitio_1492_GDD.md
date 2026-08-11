# INQUISITIO 1492: Cienie Toledo
## Game Design Document (prototyp)

| Pole | Wartość |
| :--- | :--- |
| **Tytuł** | INQUISITIO 1492: Cienie Toledo |
| **Status** | Prototyp polityczny (warstwy A → B → C) |
| **Gatunek** | Card-driven board game / ciężka intryga polityczna |
| **Gracze** | **3–5** |
| **Czas** | 60–90+ min |
| **Złożoność** | Zaawansowana (teach 15–20 min + demo Ery) |
| **Estetyka** | Mroczny pixel art: czerwień, złoto, czerń, pergamin |

Lore: [`../lore/sekret-1492.md`](../lore/sekret-1492.md)  
Zasady playable: [`../rules/README.md`](../rules/README.md)  
Roadmap (dane + stół): [`../roadmap.md`](../roadmap.md)

---

## 1. Wizja

**INQUISITIO 1492** to gra o strachu instytucjonalnym i prywatnej władzy tajemnic. Gracze nie ścigają się po torach VP — manewrują wokół **Wielkiego Inkwizytora**, pchają się wzajemnie w **Herezję**, łamią Agentów w **Lochach**, trzymają **Haki** i w krytycznym momencie **głosują**, kto spłonie.

> Oficjalna historia 1492 to zasłona. Pod Toledo i Alhambrą leżą *Fragmenty Przedwiecznego Kodeksu*. Inkwizycja nie poluje na heretyków — poluje na Relikwie.

**Prawo gry:** kto kontroluje ciała (Agentów / Podwójnych) i tajemnice (Haki), ten kontroluje stół. Inkwizytor to broń publiczna do nasyłania — Oficjum ma łatwiejszy dostęp, nigdy pełną własność.

Sim filtruje deadlocki; dramat mierzy sesja ludzka.

---

## 2. Pięć filarów

| Filar | Co robi przy stole |
| :--- | :--- |
| **Poziom Herezji** (ikona) | Tor 0–10; Czysta / Obserwowana / Krytyczna. Moc kosztuje spalenie publiczne. Krytyczna → Oskarżenie → Werdykt. |
| **Wielki Inkwizytor** | Figurka NPC: Patrol i Autodafé. Spala lokacje; gracze manewrują lub nasyłają go na siebie. |
| **Lochy / Podwójni** | Areszt → jedno Przesłuchanie: Podwójny, Hak albo +Herezja. Zaufanie do liczby Agentów pęka. |
| **Haki** | Jeden typ żetonu. Wymuszenie żądania albo ujawnienie (+Herezja). Prywatna władza strachu. |
| **Karty signature** | Asymetria łamiąca reguły (warstwa C) — rzadkie, czytelne, bolesne. |

Szczegóły procedur: [`../../game/mechanics/`](../../game/mechanics/).

---

## 3. Plansza — instytucje

Pięć lokacji w łańcuchu. Każda ma **Światło** (jawne) i **Cień** (ukryte / ryzykowne).

| # | Lokacja | Światło | Cień |
| :---: | :--- | :--- | :--- |
| 1 | Trybunał | Poparcie Kościoła | Procesy, konfiskaty |
| 2 | Pałac | Dekrety, podatki | Przekupstwo, fałszerstwa |
| 3 | Lochy | Nadzór jawny | Areszt, Podwójni, egzekucje |
| 4 | Rynek | Handel, nastroje | Herezja publiczna, zamieszki |
| 5 | Gildia / Smogi | Informatorzy | Szantaż, handel Relikwiami |

Inkwizytor stoi w jednej lokacji. Agenci poruszają się o 1 wzdłuż łańcucha (chyba że Signature łamie regułę).

→ [`../../game/board/locations.md`](../../game/board/locations.md)

---

## 4. Frakcje i cele

Cele wymagają **brudnych rąk** (Herezja, silniki), nie czystego zbieractwa.

| Frakcja | Fantazja | Wygrana |
| :--- | :--- | :--- |
| **Święte Oficjum** | Terror prawa Bożego | 2 Stosy (Autodafé/Werdykt) **lub** 2 skazania rywali z Krytycznej |
| **Cienie Al-Andalus** | Stealth, Relikwie | 2 Relikwie ewakuowane; ≥1 ścieżka przez Podwójnego lub unik Autodafé |
| **Korona & Borgiowie** | Dekrety, pieczęć | 2 Dekrety signature **oraz** aktywne Haki na 2 graczach |
| **Kabała z Toledo** | Kodeks, sweet spot | 3 Fragmenty z Przesłuchań/Imienia; przy wygranej Herezja 4–6 |
| **Gildia Cieni** | Szantaż, upadek | 2 upadki frakcji (publiczny Hak / Podwójny / spalona lokacja kluczowa) |

Opisy: [`../../game/factions/`](../../game/factions/).

---

## 5. Przebieg Ery

1. **Start** — reset limitów anti-AP; ewentualny dobór.
2. **Inkwizytor** — Patrol (0–1 lokacji) lub Autodafé (max co 2 Ery).
3. **Plan / Intryga** — naprzemiennie zakryte karty pod lokacje + ruch Agentów; Haki wymuszają (B+).
4. **Odkrycie** — lokacje 1→5; efekty; Herezja rośnie.
5. **Lochy** — Przesłuchania (B+).
6. **Dwór** — Oskarżenia jeśli ktoś w Krytycznej → Werdykt stołu.
7. **Czystka** — dobór do limitu ręki; Talia Czasu / edykt (C); znacznik 1. gracza.

---

## 6. Komponenty

Tor Herezji, figurka Inkwizytora, żeton Hak (1 typ), znacznik Podwójny na Agentach, Relikwie/Fragmenty/Stosy, złoto (koszty kart).

→ [`../../game/components/inventory.md`](../../game/components/inventory.md)

**Anti-AP (twarde):** 1 wymuszenie Haka / 1 Przesłuchanie / 1 nasłanie Inkwizytora na gracza na Erę; Autodafé max co 2 Ery.

---

## 7. Wdrożenie warstwowe (dane × stół)

| Warstwa | Dane | Stół |
| :--- | :--- | :--- |
| **A** | Herezja + Inkwizytor + Werdykt + 5 prostych kart | Solo feel → PnP A → sesja: czy Werdykt boli? |
| **B** | Lochy + Haki + narzędzia | PnP B → sesja: pazur bez paraliżu AP |
| **C** | 10 kart + Signature + Talia Czasu | PnP C → sesje → teach → pełny rulebook → freeze → art |

Szczegóły cyklu wydawniczego: [`../roadmap.md`](../roadmap.md).

---

## 8. Estetyka

Pixel art w duchu *Blasphemous* / ciężkiego historycznego horroru instytucjonalnego. Ikony: płomień Herezji, hak, kaptur Podwójnego, krzyż Inkwizytora, Relikwia. Final art dopiero po freeze tekstów.
