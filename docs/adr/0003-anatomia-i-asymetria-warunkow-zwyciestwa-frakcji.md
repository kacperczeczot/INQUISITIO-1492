[Strona główna](../../README.md) > [adr](README.md) > [0003-anatomia-i-asymetria-warunkow-zwyciestwa-frakcji](0003-anatomia-i-asymetria-warunkow-zwyciestwa-frakcji.md)

---

# ADR-0003: Anatomia i Asymetria Warunków Zwycięstwa 5 Frakcji

* **Status:** ACCEPTED
* **Data:** 2026-08-23
* **Autorzy:** Antigravity & Designer
* **Dotyczy:** `sim/inquisitio/engine/win.py`, `game_config.yaml`, `sim/inquisitio/engine/effects/registry.py`

---

## 1. Kontekst Problemu
W INQUISITIO-1492 każda z 5 frakcji posiada całkowicie asymetryczną ścieżkę do zwycięstwa. 
Bez formalnego opisu ich mechaniki, kosztów, interakcji i podatności na kontrę rywali, dochodziło do zaburzeń, w których niektóre frakcje były niegrywalne w późnej grze, a inne wygrywały automatycznie bez możliwości interakcji.

---

## 2. Zestawienie i Szczegółowe Uzasadnienie dla Każdej Frakcji

### 1. Święte Oficjum (Inkwizycja)
* **Ścieżka Zwycięstwa:**
  * **Ścieżka Główna (Procesy):** Prawomocne skazanie 3 rywali na stos (`len(condemned_rivals) >= 3`).
  * **Ścieżka Alternatywna (Stosy):** Zbudowanie 6 stosów w miastach (`stacks >= 6`).
* **Klimat i Mechanika:** Inkwizycja nie zbiera punktów pasywnie — musi aktywnie śledzić, aresztować i stawiać przed Trybunałem agentów rywali.
* **Gospodarka:** Dofinansowany skarbiec (`so-02`, 3 zł) pozwala na opłacenie procesów bez wpadania w pas biedy.
* **Kontra Rywali:** Rywale mogą zbijać swój poziom herezji, uciekać z lochów lub przekupywać sędziów Trybunału.

---

### 2. Cienie Al-Andalus (Maurzy / Moriskowie)
* **Ścieżka Zwycięstwa:**
  * Ewakuacja 2 relikwii z Półwyspu Iberyjskiego (`relics_evacuated >= 2`) za pomocą jednej z legalnych dróg ucieczki:
    1. Otwarty Szlak Morski (`sea_route_open`)
    2. Siatka Podwójnego Agenta (`path_via_double`)
    3. Przetrwanie Stosu / Ucieczka z Autodafé (`avoided_autodafe`)
    4. Cichy Szlak Nocny (`shadow_exit`)
* **Klimat i Mechanika:** Ruch oporu ratujący dziedzictwo kulturowe i relikwie przed zniszczeniem przez Trybunał.
* **Gospodarka i Koszt:** Ewakuacja przez kuriera wymaga opłacenia logistyki (`caa-05`, koszt 2 zł).
* **Late-Game Viability:** W Erach 4+ otwarcie szlaku morskiego pozwala Cieniom na przeprowadzenie wielkiej operacji ewakuacyjnej, dając im silne szanse w długich partiach.
* **Kontra Rywali:** Inkwizytor może przejąć relikwie w lokacjach i zamknąć je w archiwum Trybunału.

---

### 3. Kabała Toledo (Mistycy / Astrologowie)
* **Ścieżka Zwycięstwa:**
  * Zgromadzenie 3 fragmentów świętego tekstu (`fragments >= 3`) ORAZ
  * Utrzymanie poziomu herezji w **Złotym Paśmie Herezji `[4, 6]`** ORAZ
  * Zagranie pieczęci rytualnej (`kt-10 Pieczęć Salomona`, koszt 3 zł).
* **Klimat i Mechanika:** Mistycy nie mogą być ani zbyt "święci" (brak dostępu do wiedzy tajemnej), ani zbyt "heretyccy" (natychmiastowy stos od Inkwizycji).
* **Zlikwidowanie Pasywnego Zegara:** Kabała nie wygrywa automatycznie samą obecnością na planszy. Wymaga zgromadzenia funduszy i precyzyjnej manipulacji poziomem podejrzeń.
* **Kontra Rywali:** Inkwizycja może podbić herezję Kabały na 7+ (blokując rytuał i otwierając proces), a Gildia może zbić jej herezję na 2–3 (odbierając moc sefirot).

---

### 4. Korona Borgiowie (Polityka / Monarchia)
* **Ścieżka Zwycięstwa:**
  * Zagranie 2 Królewskich Dekretów (`decrees_played >= 2`) ORAZ
  * Posiadanie haków politycznych na co najmniej 2 różnych rywalach (`distinct_hooks >= 2`).
* **Klimat i Mechanika:** Centralizacja władzy i wymuszenie posłuszeństwa rodów szlacheckich i kościoła.
* **Kontra Rywali:** Rywale mogą wykupywać i niszczyć kompromitujące ich haki za złoto lub przysługi.

---

### 5. Gildia Cieni (Kupcy / Syndykat)
* **Ścieżka Zwycięstwa:**
  * Doprowadzenie rywali do 6 upadków majątkowych / politycznych (`falls >= 6`).
* **Klimat i Mechanika:** Czerpanie zysków z chaosu i bankructwa innych graczy.
* **Kontra Rywali:** Mądre zarządzanie skarbcem, unikanie lichwy i solidarność przeciwko szantażom Gildii.

---

## 3. Niezmienniki (Invariants)
* 🛡️ Każdy cel zwycięstwa musi wymagać co najmniej **dwóch niezależnych warunków** (np. relikwie + droga ucieczki; fragmenty + pasmo herezji; dekrety + haki; procesy + obecność inkwizytora).
* 🛡️ Wszystkie warunki muszą być w pełni kontrowalne przez pozostałych graczy przy stole za pomocą standardowych akcji.
