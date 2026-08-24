# ADR-0004: Standardy Czasu Rozgrywki i Złote Okno Er (Era 4–6)

* **Status:** ACCEPTED
* **Data:** 2026-08-23
* **Autorzy:** Antigravity & Designer
* **Dotyczy:** `sim/inquisitio/runner/scoring.py`, `sim/inquisitio/engine/win.py`, `game_config.yaml`

---

## 1. Kontekst i Problem Projektowy
W toku playtestingu i symulacji obserwowano dwie skrajne patologie tempa rozgrywki:
1. **Przedwczesne Zakończenia (Sprinty w Erze 1–2):** Część partii kończyła się, zanim gracze zdołali rozwinąć intrygi, zagrać pierwsze akcje lub wejść w interakcję przy stole.
2. **Monotonia Czasowa i Sztywne Odcinanie:** Wprowadzenie sztucznych blokad er powodowało, że gry kończyły się falami w dokładnie jednym wyznaczonym momencie, uniemożliwiając dynamiczne tempo.

Ustalono fundamentalną zasadę psychologii graczy planszowych: **niedopuszczalne jest, aby gra planszowa kończyła się na samym początku, zanim gracze zdążą w nią zagrać**.

---

## 2. Decyzja Projektowa: Głębokie Złote Okno Rozgrywki (Ery 5–7)

W grze planszowej o intrygach 1492 roku 4 ery to zaledwie ~6–8 zagranych kart na gracza — stół dopiero wchodzi w fazę rozwinięcia. W związku z tym **Era 4 jest kwalifikowana jako szybka gra**, a prawdziwy ciężar gatunkowy i kulminacja intryg muszą przypadać na **Ery 5, 6 i 7**.

Ustala się następujący standard symetrycznego rozkładu czasu rozgrywki:

| Faza Gry | Ery | Status Gry | Dopuszczalny Udział | Charakterystyka Rozgrywki |
|---|---|---|---|---|
| **Ekstremalny Sprint** | **Era 1–2** | 🔴 Niedopuszczalny / Anomalia | **$\le 0.5\%$** | Skrajne anomalie dociągu lub błędy stołu |
| **Wczesna / Szybka Gra** | **Era 3–4** | 🟡 Żółte Okno Wczesne | **$15–25\%$** | Agresywne otwarcie i szybka realizacja przewagi |
| **GŁĘBOKIE ZŁOTE OKNO** | **Era 5–7** | 🟢 **SERCE GRY** | **$65–75\%$** | **Dojrzała, pełna partia**: wielostronne procesy, zdrady, walka 4 potęg o tron |
| **Przedłużona / Późna Gra** | **Era 8–10** | 🟡 Żółte Okno Późne | **$5–12\%$** | Zacięty endgame, wyczerpywanie talii Kroniki Dziejów i ostateczne ruchy |
| **Ekstremalny Deadlock** | **Era 11+** | 🔴 Niedopuszczalny / Anomalia | **$\le 0.5\%$** | Paraliż decyzyjny stołu po wyczerpaniu talii Kroniki Dziejów |

---

## 3. Szczegółowe Uzasadnienie Matematyczne i Psychologiczne

### 3.1. Dlaczego 4 Ery to wciąż Szybka Gra?
* Przy tempie dociągu 2 kart na erę, w Erze 4 gracz widział zaledwie 6–8 kart ze swojej 12-kartowej talii.
* Zakończenie partii w Erze 4 oznacza, że rywale nie mieli jeszcze możliwości użycia kart sygnaturowych Warstwy C ani wyprowadzenia pełnej kontry na zaawansowany stan stołu.

### 3.2. Cel Średniej Rozgrywki: 5.3 – 6.3 Ery
* **Średnia partia powinna trwać 5.5 – 6.0 Er.**
* W tym czasie:
  * Święte Oficjum zdąży zebrać dowody, przeprowadzić oskarżenia i wydać 2–3 wyroki.
  * Kabała zbierze sefiroty, ale musi walczyć o utrzymanie Pasma Herezji `[4, 6]`.
  * Cienie ewakuują relikwie przez otwarty w Erze 4 Szlak Morski.
  * Korona zbuduje sieć haków i przeforsuje dekrety królewskie.
  * Gildia doprowadzi rywali do upadków majątkowych.

---

## 4. Niezmienniki (Invariants)
* 🛑 **KARA VITALITY:** Moduł ewaluacji (`scoring.py`) wymaga, aby średnia długość partii wynosiła co najmniej **$5.0$ Er** (optymalnie $5.5–6.2$ Er).
* 🛡️ Udział partii kończących się w Erach 5–7 musi wynosić co najmniej **$60\%$** we wszystkich 5 setupach Kanonu 4P.
