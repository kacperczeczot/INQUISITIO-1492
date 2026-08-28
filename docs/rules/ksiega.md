[Strona główna](../../README.md) > [Dokumentacja](../README.md) > [Zasady](README.md) > Księga Zasad

---

# INQUISITIO 1492 — Księga Zasad

### Wariant kanoniczny: 4 graczy · wersja v1.0-alpha.83

> *„Toledo, Rok Pański 1492. Grenada upadła. Na starym moście Alcántara spotykają się ci, którzy wierzą w ogień, ci, którzy uciekają z relikwiami, mędrcy składający zakazany kodeks i królewscy poborcy. W tym mieście nikt nie jest bez winy — chodzi jedynie o to, kto spłonie pierwszy."*

---

## 1. Złote prawa stołu

1. **Tekst karty** (`Łamie regułę …` / karta signature) ma bezwzględne pierwszeństwo przed regułami ogólnymi.
2. **Księga Zasad i [Słownik](slownik.md)** stanowią pełną wykładnię procedur stołu.
3. **Wyrok surowy:** w sytuacji spornej lub braku zapisu rozstrzygaj na niekorzyść gracza, który najbardziej zyskuje; przy remisie korzyści spór przegrywa gracz o wyższej Herezji; graj dalej.

---

## 2. Kanon wariantu 4-osobowego

| Parametr | Wartość 4p |
| :--- | :---: |
| Liczba graczy | 4 |
| Agenci na gracza | 3 |
| Złoto startowe | 4 |
| Limit kart na ręce | 5 |
| Tury Intrygi na Erę | 2 (na gracza) |
| Dochód końca Ery | +1 złoto |
| Maksymalna liczba Er | 14 |
| Próg Strefy Obserwowanej | **5–6** Herezji |
| Próg Strefy Krytycznej (Oskarżenia) | **7–10** Herezji |
| Pierwsze Autodafé | najwcześniej od **Ery 3** |
| Cooldown Autodafé | co najmniej **3 pełne Ery** |

---

## 3. Komponenty

* **1 Plansza główna** (5 lokacji Toledo połączonych grafem ulic + slot Aresztu w Lochach).
* **1 Figurka Wielkiego Inkwizytora** + 2 żetony stanu: **Patrol** i **Autodafé**.
* **1 Talia Kroniki Dziejów** (10 kart Edyktów).
* **Żetony wspólne i puli:**
  * **Intryga & Kasa:** 12 Haków, 8 Nakładek Marionetki, 4 Znaczniki Herezji, ~40 monet Złota, 15 żetonów Piętna (limity akcji).
  * **Cele Frakcji:** 6 Stosów (Oficjum), 6 Relikwii (Cienie), 6 Fragmentów Kodeksu (Kabała), 2 Dekrety (Korona), 8 Upadków (Gildia).
  * **Oznaczenia stołu:** Znacznik 1. gracza, Znacznik Szlaku Morskiego.
* **Elementy 4 frakcji:** dla każdej talia 10 kart, 3 figurki Agentów, planszetka gracza z torem Herezji 0–10.

> W 4-osobowej grze jedna z pięciu frakcji nie bierze udziału. Rekomendacja na pierwszą sesję: wyłącz **Gildię Cieni**.

---

## 4. Plansza — Graf Lokacji

Ruch Agentów i Inkwizytora odbywa się wzdłuż krawędzi grafu (ruch o 1 = przejście na sąsiednią lokację).

```
                 (2) PAŁAC ─────────── (4) RYNEK
                ╱    │                    │
               ╱     │                    │
(1) TRYBUNAŁ ──      │                    │
               ╲     │                    │
                ╲    │                    │
                 (3) LOCHY ─────────── (5) GILDIA
```

| # | Lokacja | Sąsiedzi |
| :---: | :--- | :--- |
| **1** | **Trybunał Inkwizycji** | Pałac, Lochy |
| **2** | **Pałac Gubernatora** | Trybunał, Lochy, Rynek |
| **3** | **Lochy & Podziemia** | Trybunał, Pałac, Gildia |
| **4** | **Rynek i Plac Publiczny** | Pałac, Gildia |
| **5** | **Gildia / Dzielnica Garbarzy** | Rynek, Lochy |

*Kolejność rozpatrywania kart w Fazie II (1 → 2 → 3 → 4 → 5) wynika z numeracji lokacji i jest niezależna od połączeń grafu ruchu.*

---

## 5. Przygotowanie gry (Setup)

1. **Plansza:** rozłóż planszę na środku stołu. Postaw figurkę Inkwizytora na **Trybunale** (stan: Patrol). Połóż potasowaną talię Kroniki Dziejów zakrytą obok planszy.
2. **Frakcje:** każdy gracz wybiera 1 frakcję, bierze jej talię 10 kart (tasuje), 3 Agentów oraz planszetkę (znacznik Herezji na polu **0**).
3. **Zasoby początkowe:** każdy gracz pobiera **4 złota** oraz dobiera **5 kart** na rękę.
4. **Relikwie i Fragmenty:** umieść **1 Relikwię w Lochach** oraz **2 Relikwie** w dowolnych odkrytych lokacjach (uzgodnijcie wspólnie). Pula 6 Fragmentów Kodeksu leży obok planszy.
5. **Rozstawienie początkowe:** każdy gracz wystawia **do 2 Agentów** na planszę (dowolne lokacje; 3. Agent zostaje w rezerwie).
6. **Pierwszy gracz:** wybierzcie pierwszego gracza wspólnie przy stole.

---

## 6. Przebieg Gry — 3 Fazy Ery

Rozgrywka trwa maksymalnie 14 Er. Każda Era składa się z 3 następujących po sobie Faz:

```
Era N
 ├── Faza I:   Intryga             (2 tury akcji na gracza)
 ├── Faza II:  Sąd                 (Inkwizytor → Odkrycie kart → Lochy → Werdykt)
 └── Faza III: Kronika & Czystka   (Zwycięstwo? → Dochód i Dobór → Edykt Ery → Rotacja)
```

---

### Faza I: Intryga

Gracze wykonują naprzemiennie po **2 tury akcji** (Runda 1 i Runda 2), zaczynając od 1. gracza i idąc zgodnie z ruchem wskazówek zegara.

#### W swojej turze wybierasz JEDNĄ opcję:

* **Opcja A — Zagraj kartę Akcji:**
  1. Połóż kartę Akcji z ręki **zakrytą** pod wybraną lokacją.
  2. Natychmiast opłać jej **koszt w złocie**.
  3. *(Opcjonalnie)* Wystaw z rezerwy lub przesuń **1 Agenta** o 1 krawędź grafu.
* **Opcja B — Akcja Gospodarcza:**
  1. Pobierz **+1 złoto** z banku.
  2. *(Opcjonalnie)* Wystaw z rezerwy lub przesuń **1 Agenta** o 1 krawędź grafu.

#### Akcje dodatkowe i karty Reakcji:
* **Karty Reakcji:** leżą na ręce i zagrywa się je poza swoją turą, w momencie spełnienia warunku opisanego na karcie.
* **Wymuszenie Haka (opcja, max 1× na gracza na Erę):** przed lub po swojej akcji możesz zużyć posiadany żeton Haka i zażądać od ofiary:
  - zagłosowania w określony sposób w najbliższym Werdykcie,
  - nieoskarżania wskazanego gracza w tej Erze,
  - przesunięcia Agenta o 1 krawędź,
  - niezagrania karty pod wskazaną lokację,
  - oddania 1 złota.  
  *Jeśli ofiara spełni żądanie — żeton Haka znika. Jeśli odmówi — ofiara otrzymuje **+2 Herezji**, a Hak i tak znika.*  
  *Gracz może posiadać maksymalnie **2 aktywne Haki** naraz.*

---

### Faza II: Sąd

Faza Sądu składa się z 4 kolejnych kroków:

#### Krok 1: Wkroczenie Inkwizytora
1. **Nasłania (max 1× na gracza):** gracze mogą zgłosić preferowany kierunek ruchu Inkwizytora. Jeśli nasłanie zgłasza Święte Oficjum — wygrywa automatycznie; w innym wypadku decyduje 1. gracz (remis: gracz o najniższej Herezji).
2. **Ruch Inkwizytora:** Inkwizytor przemieszcza się o **0 lub 1 krawędź grafu** (po najkrótszej ścieżce do wskazanego celu lub wg decyzji gracza z najniższą Herezją).
3. **Autodafé (jeśli minęły $\ge 3$ Ery od ostatniego Autodafé, od Ery 3):**
   - Jeśli gracz ogłosi procedurę Autodafé w lokacji Inkwizytora:
     - Każdy wrogi Agent gracza o Herezji **0–4 (Czysta)** trafia do **Aresztu w Lochach** (+1 Herezja, bez Stosu).
     - Każdy wrogi Agent gracza o Herezji **$\ge 5$ (Obserwowana/Krytyczna)** zostaje **spalony na Stosie** (+1 Herezja dla właściciela, +1 Stos dla Oficjum, jeśli Oficjum ogłosiło Autodafé).
     - Relikwia znajdująca się w tej lokacji wraca do puli ogólnej.

#### Krok 2: Odkrycie kart
Karty są odkrywane i rozpatrywane lokacja po lokacji, w kolejności **od 1 do 5**:
1. Rozpatrz treść i efekty karty.
2. Zwiększ Herezję gracza zagrywającego (`heresy`) oraz ewentualnego wskazanego rywala (`target_heresy`).
3. Rozpatrz ewentualne areszty (`arrest`) — wskazany Agent trafia do strefy Aresztu w Lochach.
4. *Fiasko:* jeśli warunek zagrania karty nie jest spełniony w momencie odkrycia, karta nie wywołuje efektu i nie nalicza dodatkowej Herezji.

#### Krok 3: Lochy — Przesłuchania
Każdy gracz posiadający własnego Agenta w Lochach (lub odpowiednią kartę) może wykonać **1 Przesłuchanie na Erę**:
Wybierz aresztowanego Agenta rywala i wskaż 1 skutek:
* **Marionetka:** nałóż nakładkę Marionetki na figurkę rywala. Raz na Erę możesz poruszyć nią o 1 krawędź jak własnym pionkiem (nie daje dodatkowego głosu w Werdykcie). *Ujawnienie Marionetki (np. przez Inkwizytora) daje jej właścicielowi +2 Herezji.*
* **Hak:** weź 1 żeton Haka na właściciela tego Agenta.
* **Wymuszenie Herezji:** właściciel Agenta otrzymuje **+2 Herezji**, a Agent pozostaje w Areszcie.

#### Krok 4: Dwór — Oskarżenia i Werdykt
Jeśli dowolny gracz ma Herezję **$\ge 7$ (Strefa Krytyczna)**, inny gracz może wnieść **Oskarżenie** (max 1 oskarżenie przeciw temu samemu celowi na Erę):
1. **Głosowanie jawne:** wszyscy gracze **oprócz oskarżonego** głosują: *Skazać* lub *Uniewinnić* (siła głosu wynosi domyślnie 1).
2. **Remis:** oznacza Uniewinnienie.
3. **Skazanie:** 1 Agent oskarżonego trafia do Aresztu w Lochach, cel otrzymuje **+1 Herezji**, a jego frakcja zostaje odnotowana na torze Skazań Oficjum (+1 Stos dla Oficjum tylko wtedy, gdy to Oficjum wniosło oskarżenie).
4. **Uniewinnienie:** oskarżyciel otrzymuje **+1 Herezji** za bezpodstawny donos.

---

### Faza III: Kronika & Czystka

1. **Sprawdzenie Zwycięstwa:** jeśli gracz spełnia swój cel, gra kończy się natychmiast jego wygraną.
2. **Dobór kart:** każdy gracz dobiera karty ze swojej talii do limitu **5 na ręce** (przy wyczerpaniu talii przetasuj odrzuty).
3. **Dochód:** każdy gracz pobiera **+1 złoto** z banku.
4. **Edykt Ery:** odkryj wierzchnią kartę Kroniki Dziejów — jej zapis modyfikuje reguły w nadchodzącej Erze (poprzedni edykt traci moc, chyba że ma zapis o trwałości).
5. **Rotacja:** przekaż znacznik 1. gracza osobie po lewej. Zresetuj limity akcji na nową Erę.

---

## 7. Tor Herezji (0–10)

Herezja odzwierciedla uwagę, jaką Inkwizycja skupia na danym rodzie:

| Zakres | Strefa | Konsekwencje |
| :---: | :--- | :--- |
| **0–4** | **Czysta** | Pełne bezpieczeństwo przed Stosem w Autodafé (tylko Areszt). |
| **5–6** | **Obserwowana** | Autodafé pali Agentów na Stosie. Zagrożenie wejściem w stan oskarżenia. |
| **7–10** | **Krytyczna** | Każdy rywal może postawić cię przed Trybunałem w Fazie Dworu (Werdykt). |

*Wartość Herezji nigdy nie może przekroczyć 10 (nadmiarowe punkty przepadają).*

---

## 8. Frakcje i Warunki Zwycięstwa

Warunki zwycięstwa sprawdzane są na początku Fazy III (kolejno od 1. gracza):

### ✝ Święte Oficjum
* **Cel:** **6 Stosów** (spaleni Agenci rywali) **LUB 3 Skazania** rywali Werdyktem Trybunału (w 3p: **2 Skazania**).
* **Styl gry:** kierowanie ruchem Inkwizytora, areszty, wymuszanie procedury Autodafé i oskarżenia przy stole.
* **Karta Signature (so-10):** *Oczyść Miasto* — łamie cooldown Autodafé i pozwala przeprowadzić natychmiastową czystkę.

### 🌙 Cienie Al-Andalus
* **Cel:** **2 Relikwie ewakuowane** poza planszę (przez Szlak Morski lub dedykowane karty).
* **Styl gry:** utrzymywanie niskiej Herezji, przemykanie tunelami, manipulacja pionkami przez Marionetki.
* **Karta Signature (caa-10):** *Echo Alhambry* — pozwala ewakuować do 2 Relikwii naraz bez wymogu otwartego Szlaku Morskiego.

### 👑 Korona & Borgiowie
* **Cel:** **2 Dekrety** wprowadzone kartami signature (*Dekret Królewski* i *Pieczęć Korony*).
* **Styl gry:** akumulacja złota, handel wpływami, podwójna siła głosu w sądzie i sieć Haków.
* **Karta Signature (kb-10):** *Pieczęć Korony* — natychmiastowe zwycięstwo przy posiadaniu aktywnych Haków na $\ge 2$ rywalach.

### 📜 Kabała z Toledo
* **Cel:** **2 Fragmenty Kodeksu** — możliwe do rozliczenia najwcześniej od **Ery 6**.
* **Styl gry:** balansowanie Herezją w Strefie Obserwowanej (4–6), zabezpieczanie uczonych w Lochach i Trybunale.
* **Karta Signature (kt-10):** *Pieczęć Salomona* — natychmiastowe zwycięstwo przy 3 Fragmentach i Herezji 4–6.

### 🗡 Gildia Cieni
* **Cel:** **8 Upadków** narzuconych rywalom (przez Haki, Marionetki i wyroki).
* **Styl gry:** fałszywi świadkowie (zmiana głosu po ujawnieniu większości), skrytobójstwa i wymuszenia.
* **Karta Signature (gc-10):** *Upadek Domu* — oznaczenie Upadku na rywalu posiadającym ujawniony Hak lub Marionetkę.

---

## 9. Koniec Gry i Rozstrzyganie Remisów

* Jeśli w Fazie III którykolwiek gracz spełnia swój cel — gra kończy się **natychmiast**. Jeśli warunek spełnia kilku graczy jednocześnie, wygrywa ten, który siedzi bliżej 1. gracza (zgodnie z kolejnością rundy).
* Jeśli po zakończeniu **Ery 11** nikt nie osiągnął pełnego celu:
  1. Wygrywa gracz **najbliższy realizacji swojego warunku** (procentowo / logicznie).
  2. Przy remisie: wygrywa gracz z **najniższym poziomem Herezji**.
  3. Dalszy remis oznacza wspólne zwycięstwo.
