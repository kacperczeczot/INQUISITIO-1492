[Strona główna](../README.md) > [Playtesting](README.md)

---

# Playtesting — balans (stan aktualny)

Sim filtruje: deadlocki, oskarżenia, Autodafé, Haki, Marionetki.  
**Werdykt fun = sesja ludzka** ([`sessions/_TEMPLATE.md`](sessions/_TEMPLATE.md)).  
**Spłaszczanie:** unikamy skalowania 3p/4p/5p; jedna liczba, jeśli wynik jest lepszy, podobny albo tani ([hierarchia §0](../docs/rules/hierarchia_balansowania.md)).

Setupy: [`setups.md`](setups.md) · Hierarchia Balansowania: [`../docs/rules/hierarchia_balansowania.md`](../docs/rules/hierarchia_balansowania.md) · Silnik: [`../sim/README.md`](../sim/README.md) · Config: [`../game_config.yaml`](../game_config.yaml).  
**Autonomiczne Narzędzia:** Kanon 4P (Karty): [`audytor_kanonu.py`](../tools/sim/audytor_kanonu.py) · Kanon 4P (Makro): [`audytor_4p.py`](../tools/sim/audytor_4p.py) · Format 3P (Lookahead): [`audytor_3p.py`](../tools/sim/audytor_3p.py) · Format 5P (Lookahead): [`audytor_5p.py`](../tools/sim/audytor_5p.py) · Grand Audit: [`run_grand_audit.py`](../tools/sim/run_grand_audit.py).

---

## 🛡️ Gwarancja Silnika (Engine Guarantee & SSOT Contract — od wersji v1.0-alpha.25)

Wersja **`v1.0-alpha.25`** stanowi punkt zwrotny projektu — to od tego wydania silnik symulacyjny `INQUISITIO-1492` (`sim/inquisitio/`) osiągnął **pełną, bezkompromisową zgodność mechaniczną i taktyczną** ze stołem fizycznym:
1. **Pełna Inteligencja AI (60/60 Kart):** Do wersji `v1.0-alpha.24` boty w symulacji sztucznie przeceniały Akcję Gospodarczą ($2.6$ base), przez co w 100% partii odrzucały 24 z 60 kart (`Play-Rate: 0.00`) i zapychały sobie rękę, co fałszowało testy ablacji. Od `v1.0-alpha.25` bot (`PoliticsAgent`) posiada pełne, aktywne heurystyki dla wszystkich 60 kart frakcyjnych (pozycjonowanie, presja sądu, haki, tempo).
2. **Telemetria Reakcji i Zagrań:** Zliczanie wyzwalanych kart reakcji (`SO-05` Wezwanie do Trybunału oraz `GC-05` Fałszywy Świadek w sądzie) w liczniku `card_plays`.
3. **Trójwymiarowa Taksonomia Ablacji:** Eliminacja fałszywych etykiet „Zbalansowane Narzędzie” dla niezagrywanych kart i zastąpienie ich ścisłą klasyfikacją opartą o $\Delta\text{Share} \times \Delta\text{4P} \times \text{Play-Rate}$.
4. **Wierność Zasadom Gry:** Pętla partii wykonuje w 100% procedury stołu z księgi zasad ([`docs/rules/ksiega.md`](../docs/rules/ksiega.md)), słownika ([`docs/rules/slownik.md`](../docs/rules/slownik.md)) i mechanik ([`game/mechanics/`](../game/mechanics/)): Intryga, Sąd/Werdykt, Kronika Dziejów, Autodafé, Haki, Marionetki, Lochy, Szlak Morski.
5. **Single Source of Truth (SSOT):** Wszystkie wartości kosztów, parametrów kart, progów zwycięstwa i modyfikatorów globalnych są w 100% zsynchronizowane z plikiem [`game_config.yaml`](../game_config.yaml).
6. **Weryfikacja Automatyczna:** 100% testów jednostkowych, integracyjnych i regresyjnych (`sim/tests/`) musi przechodzić (214/214 passed) przed jakimkolwiek wdrożeniem zmian balansu.

---

### 📊 Raporty Telemetrii i Archiwum Symulacji

Szczegółowe dane symulacyjne, wskaźniki użyteczności 60 kart, wykresy monokultury talii i telemetria 16 setupów są generowane automatycznie per wersja do katalogu [`playtesting/sim-reports/archive/`](sim-reports/archive/):
- 📁 **Struktura i Opis Raportów:** [`playtesting/sim-reports/README.md`](sim-reports/README.md)
- 📁 **Katalog Wszystkich Wydań:** [`playtesting/sim-reports/archive/`](sim-reports/archive/) (np. `archive/v1.0-alpha.25/`, `archive/v1.0-alpha.24/`)
- 📜 **Dziennik Zmian Balansu:** Szczegółowe wpisy i historia każdego patcha znajdują się poniżej w sekcji [Patch Notes](#-chronologiczna-historia-zmian-balansu-faza-prototypowa--patch-notes).

Poza zakresem (świadomie): AI operuje na ogólnych heurystykach teorii gier stołowych; wolny tekst `effect` jest zmapowany na ustrukturyzowane handlery i pola YAML. `korona_borgiowie.era` / `hooks` w victory pozostają wyłączone z audytora makro (zgodnie z unifikacją 4P).

— Antigravity (Gemini 3.7 Flash) · Architekt Balansu & Inżynier Silnika INQUISITIO-1492

---

## ⚙️ Kluczowe Parametry Systemowe (Single Source of Truth: `game_config.yaml`)

Wszystkie wartości balansu są zsynchronizowane centralnie z pliku [`game_config.yaml`](../game_config.yaml):

| Parametr Systemowy | 3 Graczy (3p) | 4 Graczy (4p) | 5 Graczy (5p Full) | Uzasadnienie Analityczne |
| :--- | :---: | :---: | :---: | :--- |
| **Próg Obserwowanej** | **3** | **3** | **3** | Czysta to 0–2. Od **3** Autodafé pali na Stos (nie areszt). |
| **Próg Oskarżenia (Krytyczna)** | **{'default': 6, 'no_gc': 7}** | **7** | **8** | Kanon 4p = **7**. Obserwowana kończy się na T−1. |
| **Maksymalna Liczba Er** | **15** | **15** | **15** | Zegar talii Kroniki Dziejów (11 kart edyktów czasu); tiebreak po wyczerpaniu talii. |
| **Cooldown Autodafé** | **3 Ery** | **3 Ery** | **3 Ery** | Zunifikowany cooldown co 3 Ery (pierwsze możliwe od Ery 3). |
| **Przebieg Ery (Rundy Kart)** | **2 Rundy** | **2 Rundy** | **2 Rundy** | 2 akcje/erę (karta **lub** Gospodarcza). |
| **Akcja Gospodarcza** | **+1 zł** | **+1 zł** | **+1 zł** | Faza I Opcja B. Jarmark na Rynku: +2. |
| **Złoto Startowe** | **4 zł** | **4 zł** | **4 zł** | Zunifikowane 4 zł dla wszystkich składów graczy. |
| **Limit Kart na Ręce** | **5 Kart** | **5 Kart** | **5 Kart** | Zunifikowany limit 5 kart dla wszystkich składów graczy. |
| **Otwarcie Szlaku Morskiego (Cienie)** | **Era 4** | **Era 4** | **Era 4** | Szlak w oknie partii (wcześniej era 6 = po końcu gry). |

---

## 🏆 Warunki Zwycięstwa Frakcji (Unifikacja Globalna 4P — v1.0-alpha.44)

Wszystkie ścieżki zwycięstwa są zunifikowane do wartości bazowych Kanonu 4P (zgodnie z ADR-0001, ADR-0003 i SSOT `game_config.yaml`):

### 1. Święte Oficjum
- **Ścieżka A (Stosy):** **6 Stosów**.
- **Ścieżka B (Skazania):** **3 Skazania** (w 3p: **2 Skazania**; Werdykt Trybunału; unikalne nazwiska skazanych rywali).

### 2. Cienie Al-Andalus
- **Ewakuacja Relikwii:** **2 Relikwie**.
- **Legalne Drogi Ucieczki:** Płatny kurier (`caa-05`), podwójny agent, ucieczka ze stosu lub otwarty od Ery **4** Szlak Morski. Brak darmowej wygranej „sama era”.

### 3. Korona Borgiowie
- **Królewskie Dekrety:** **2 Dekrety** + Haki polityczne na rywalach.

### 4. Kabała z Toledo
- **Święty Manuskrypt & Rytuał:** Zgromadzenie **3 Fragmentów Kodeksu** i zagranie karty sygnaturowej `kt-10 Pieczęć Salomona` (koszt 3 zł, Złote Pasmo Herezji **[4, 6]**). Brak sztucznej blokady er.

### 5. Gildia Cieni
- **Upadki:** **6 Upadków** narzuconych rywalom (przez Haki, Marionetki, lichwę i wyroki).

---

## Dwupoziomowe Progi Balansu Wygranych (Sztywne Bramki `sim`)

| Liczba graczy | Punkt Idealny | 🎯 Cel Ścisły (Target Band) | 🚨 Czerwona Linia (Krytyczna Wariancja) |
| :--- | :---: | :---: | :---: |
| **3 graczy (3p)** | **33.3%** | **28.0% – 38.0%** | **20.0% – 45.0%** |
| **4 graczy (4p)** | **25.0%** | **20.0% – 30.0%** | **15.0% – 35.0%** |
| **5 graczy (5p Full)** | **20.0%** | **16.0% – 24.0%** | **10.0% – 30.0%** |

* **Cel Ścisły:** Sztywny zakres docelowy przy projektowaniu i dostrajaniu balansu.
* **Czerwona Linia:** Przekroczenie oznacza krytyczny błąd balansu (blocker), wyzwalający błąd w testach automatycznych i wymagający bezwzględnej korekty w GDD/kodzie.

---

## 📜 Chronologiczna Historia Zmian Balansu (Faza Prototypowa — Patch Notes)

### 🌐 Patch v1.0-alpha.173 (2026-08-31) — Global Auditor: Karta `so-12` (Straż Trybunalska): `heresy` → `2` (Zysk Global Δ +0.2 pkt)
- **Modyfikacja:** `BAZA__L3_SO-12_HERESY_MINUS1` -> Karta `so-12` (Straż Trybunalska): `heresy` → `2`
- **Wynik Globalny:** 86.9 → **87.1**
- **Balans 4P:** 90.7 → 91.0
- **Balans 3P:** 72.5 → 72.1
- **Balans 5P:** 97.5 → 98.3

### 🌐 Patch v1.0-alpha.172 (2026-08-31) — Global Auditor: Karta `so-07` (Przesłuchanie Oficjum): `cost` → `0` + Karta `so-07` (Przesłuchanie Oficjum): `gold` → `1` (Zysk Global Δ +0.1 pkt)
- **Modyfikacja:** `BAZA__L3_SO-07_C0_G1` -> Karta `so-07` (Przesłuchanie Oficjum): `cost` → `0` + Karta `so-07` (Przesłuchanie Oficjum): `gold` → `1`
- **Wynik Globalny:** 86.8 → **86.9**
- **Balans 4P:** 90.4 → 90.7
- **Balans 3P:** 72.2 → 72.5
- **Balans 5P:** 97.8 → 97.5

### 🌐 Patch v1.0-alpha.171 (2026-08-31) — Global Auditor: Karta `caa-01` (Przejście Podziemiami): `cost` → `0` + Karta `caa-01` (Przejście Podziemiami): `gold` → `2` (Zysk Global Δ +0.1 pkt)
- **Modyfikacja:** `BAZA__L3_CAA-01_C0_G2` -> Karta `caa-01` (Przejście Podziemiami): `cost` → `0` + Karta `caa-01` (Przejście Podziemiami): `gold` → `2`
- **Wynik Globalny:** 86.7 → **86.8**
- **Balans 4P:** 90.6 → 90.4
- **Balans 3P:** 72.3 → 72.2
- **Balans 5P:** 97.2 → 97.8

### 🌐 Patch v1.0-alpha.170 (2026-08-30) — Przywrócenie kanonicznych progów oskarżenia (3p: 6, 4p: 7, 5p: 8)
- **Modyfikacja:** Przywrócenie organicznej fizyki stołu i kanonicznych progów oskarżenia zgodnie z Konstytucją ADR i Hierarchią Balansowania.
- **Konfiguracja progów:** 3p: 6 | 4p: 7 | 5p: 8 (usunięcie sztucznego dryfu progów L1)
- **Wynik Globalny:** 87.3 → **86.5**
- **Balans 4P:** 92.3 → 91.2
- **Balans 3P:** 72.3 → 71.7
- **Balans 5P:** 97.2 → 96.5
- **Cel:** Odblokowanie pełnej przestrzeni Strefy Obserwowanej (3..6 w 4P) i skupienie dalszej optymalizacji na kartach frakcji (Poziom 3).

### 🌐 Patch v1.0-alpha.169 (2026-08-30) — Global Auditor: Próg oskarżenia (4p): offset -1 (nowy: 4) (Zysk Global Δ +0.4 pkt)
- **Modyfikacja:** `BAZA__L1_THRESHOLD_4P_MINUS1` -> Próg oskarżenia (4p): offset -1 (nowy: 4)
- **Wynik Globalny:** 86.9 → **87.3**
- **Balans 4P:** 90.6 → 92.3
- **Balans 3P:** 73.0 → 72.3
- **Balans 5P:** 97.2 → 97.2

### 🌐 Patch v1.0-alpha.168 (2026-08-30) — Global Auditor: Próg oskarżenia (3p): offset -1 (nowy: 5) (Zysk Global Δ +0.2 pkt)
- **Modyfikacja:** `BAZA__L1_THRESHOLD_3P_MINUS1` -> Próg oskarżenia (3p): offset -1 (nowy: 5)
- **Wynik Globalny:** 86.7 → **86.9**
- **Balans 4P:** 90.6 → 90.6
- **Balans 3P:** 72.3 → 73.0
- **Balans 5P:** 97.2 → 97.2

### 🌐 Patch v1.0-alpha.167 (2026-08-30) — Global Auditor: Próg oskarżenia (4p): offset -1 (nowy: 5) (Zysk Global Δ +0.6 pkt)
- **Modyfikacja:** `BAZA__L1_THRESHOLD_4P_MINUS1` -> Próg oskarżenia (4p): offset -1 (nowy: 5)
- **Wynik Globalny:** 86.7 → **87.3**
- **Balans 4P:** 90.6 → 92.3
- **Balans 3P:** 72.3 → 72.3
- **Balans 5P:** 97.2 → 97.2

### 🌐 Patch v1.0-alpha.166 (2026-08-30) — Global Auditor: Próg oskarżenia (4p): offset -1 (nowy: 6) (Zysk Global Δ +0.6 pkt)
- **Modyfikacja:** `BAZA__L1_THRESHOLD_4P_MINUS1` -> Próg oskarżenia (4p): offset -1 (nowy: 6)
- **Wynik Globalny:** 86.7 → **87.3**
- **Balans 4P:** 90.6 → 92.3
- **Balans 3P:** 72.3 → 72.3
- **Balans 5P:** 97.2 → 97.2

### 🌐 Patch v1.0-alpha.165 (2026-08-30) — Global Auditor: Karta `caa-11` (Nocna Zmiana Warty): `cost` → `2` + Karta `caa-11` (Nocna Zmiana Warty): `heresy` → `2` (Zysk Global Δ +0.1 pkt)
- **Modyfikacja:** `BAZA__L3_CAA-11_C2_H2` -> Karta `caa-11` (Nocna Zmiana Warty): `cost` → `2` + Karta `caa-11` (Nocna Zmiana Warty): `heresy` → `2`
- **Wynik Globalny:** 86.6 → **86.7**
- **Balans 4P:** 90.3 → 90.6
- **Balans 3P:** 72.3 → 72.3
- **Balans 5P:** 97.1 → 97.2

### 🌐 Patch v1.0-alpha.164 (2026-08-30) — Global Auditor: Karta `gc-01` (Przekupiony Strażnik): `heresy` → `3` (Zysk Global Δ +0.4 pkt)
- **Modyfikacja:** `BAZA__L3_GC-01_HERESY_PLUS2` -> Karta `gc-01` (Przekupiony Strażnik): `heresy` → `3`
- **Wynik Globalny:** 86.2 → **86.6**
- **Balans 4P:** 90.0 → 90.3
- **Balans 3P:** 71.7 → 72.3
- **Balans 5P:** 96.8 → 97.1

### 🌐 Patch v1.0-alpha.163 (2026-08-30) — Global Auditor: Karta `caa-10` (Echo Alhambry): `cost` → `3` + Karta `caa-10` (Echo Alhambry): `gold` → `1` (Zysk Global Δ +0.2 pkt)
- **Modyfikacja:** `BAZA__L3_CAA-10_C3_G1` -> Karta `caa-10` (Echo Alhambry): `cost` → `3` + Karta `caa-10` (Echo Alhambry): `gold` → `1`
- **Wynik Globalny:** 86.0 → **86.2**
- **Balans 4P:** 90.2 → 90.0
- **Balans 3P:** 72.2 → 71.7
- **Balans 5P:** 95.5 → 96.8

### 🌐 Patch v1.0-alpha.162 (2026-08-30) — Global Auditor: Karta `gc-03` (Podrzucenie Księgi): `heresy` → `3` (Zysk Global Δ +0.2 pkt)
- **Modyfikacja:** `BAZA__L3_GC-03_HERESY_PLUS1` -> Karta `gc-03` (Podrzucenie Księgi): `heresy` → `3`
- **Wynik Globalny:** 85.8 → **86.0**
- **Balans 4P:** 90.1 → 90.2
- **Balans 3P:** 72.1 → 72.2
- **Balans 5P:** 95.3 → 95.5

### 🌐 Patch v1.0-alpha.161 (2026-08-30) — Global Auditor: Karta `kt-08` (Areszt Wiedzy): `gold` → `1` + Karta `kt-08` (Areszt Wiedzy): `heresy` → `0` (Zysk Global Δ +0.1 pkt)
- **Modyfikacja:** `BAZA__L3_KT-08_G1_H0` -> Karta `kt-08` (Areszt Wiedzy): `gold` → `1` + Karta `kt-08` (Areszt Wiedzy): `heresy` → `0`
- **Wynik Globalny:** 85.7 → **85.8**
- **Balans 4P:** 89.6 → 90.1
- **Balans 3P:** 73.6 → 72.1
- **Balans 5P:** 94.0 → 95.3

### 🌐 Patch v1.0-alpha.160 (2026-08-30) — Global Auditor: Karta `so-12` (Straż Trybunalska): `heresy` → `3` (Zysk Global Δ +0.1 pkt)
- **Modyfikacja:** `BAZA__L3_SO-12_HERESY_PLUS1` -> Karta `so-12` (Straż Trybunalska): `heresy` → `3`
- **Wynik Globalny:** 85.6 → **85.7**
- **Balans 4P:** 89.9 → 89.6
- **Balans 3P:** 72.9 → 73.6
- **Balans 5P:** 93.9 → 94.0

### 🌐 Patch v1.0-alpha.159 (2026-08-30) — Global Auditor: Karta `caa-01` (Przejście Podziemiami): `cost` → `0` + Karta `caa-01` (Przejście Podziemiami): `gold` → `1` (Zysk Global Δ +0.1 pkt)
- **Modyfikacja:** `BAZA__L3_CAA-01_C0_G1` -> Karta `caa-01` (Przejście Podziemiami): `cost` → `0` + Karta `caa-01` (Przejście Podziemiami): `gold` → `1`
- **Wynik Globalny:** 85.5 → **85.6**
- **Balans 4P:** 89.8 → 89.9
- **Balans 3P:** 72.9 → 72.9
- **Balans 5P:** 93.8 → 93.9

### 🌐 Patch v1.0-alpha.158 (2026-08-30) — Global Auditor: Karta `caa-06` (Ucieczka z Lochów): `cost` → `1` + Karta `caa-06` (Ucieczka z Lochów): `heresy` → `0` (Zysk Global Δ +0.3 pkt)
- **Modyfikacja:** `BAZA__L3_CAA-06_C1_H0` -> Karta `caa-06` (Ucieczka z Lochów): `cost` → `1` + Karta `caa-06` (Ucieczka z Lochów): `heresy` → `0`
- **Wynik Globalny:** 85.2 → **85.5**
- **Balans 4P:** 89.1 → 89.8
- **Balans 3P:** 72.1 → 72.9
- **Balans 5P:** 94.3 → 93.8

### 🌐 Patch v1.0-alpha.157 (2026-08-30) — Global Auditor: Karta `caa-11` (Nocna Zmiana Warty): `cost` → `3` + Karta `caa-11` (Nocna Zmiana Warty): `heresy` → `1` (Zysk Global Δ +0.6 pkt)
- **Modyfikacja:** `BAZA__L3_CAA-11_C3_H1` -> Karta `caa-11` (Nocna Zmiana Warty): `cost` → `3` + Karta `caa-11` (Nocna Zmiana Warty): `heresy` → `1`
- **Wynik Globalny:** 84.6 → **85.2**
- **Balans 4P:** 89.7 → 89.1
- **Balans 3P:** 71.8 → 72.1
- **Balans 5P:** 92.2 → 94.3

### 🌐 Patch v1.0-alpha.156 (2026-08-30) — Global Auditor: Karta `caa-04` (Fałszywy Trop): `cost` → `0` + Karta `caa-04` (Fałszywy Trop): `gold` → `2` (Zysk Global Δ +0.1 pkt)
- **Modyfikacja:** `BAZA__L3_CAA-04_C0_G2` -> Karta `caa-04` (Fałszywy Trop): `cost` → `0` + Karta `caa-04` (Fałszywy Trop): `gold` → `2`
- **Wynik Globalny:** 84.5 → **84.6**
- **Balans 4P:** 90.4 → 89.7
- **Balans 3P:** 71.9 → 71.8
- **Balans 5P:** 91.3 → 92.2

### 🌐 Patch v1.0-alpha.155 (2026-08-30) — Global Auditor: Karta `gc-01` (Przekupiony Strażnik): `cost` → `1` + Karta `gc-01` (Przekupiony Strażnik): `heresy` → `2` (Zysk Global Δ +0.1 pkt)
- **Modyfikacja:** `BAZA__L3_GC-01_C1_H2` -> Karta `gc-01` (Przekupiony Strażnik): `cost` → `1` + Karta `gc-01` (Przekupiony Strażnik): `heresy` → `2`
- **Wynik Globalny:** 84.4 → **84.5**
- **Balans 4P:** 91.1 → 90.4
- **Balans 3P:** 71.2 → 71.9
- **Balans 5P:** 90.8 → 91.3

### 🌐 Patch v1.0-alpha.154 (2026-08-30) — Global Auditor: Karta `caa-02` (Złoto z Kryjówki): `cost` → `2` + Karta `caa-02` (Złoto z Kryjówki): `heresy` → `0` (Zysk Global Δ +0.1 pkt)
- **Modyfikacja:** `BAZA__L3_CAA-02_C2_H0` -> Karta `caa-02` (Złoto z Kryjówki): `cost` → `2` + Karta `caa-02` (Złoto z Kryjówki): `heresy` → `0`
- **Wynik Globalny:** 84.3 → **84.4**
- **Balans 4P:** 91.2 → 91.1
- **Balans 3P:** 71.2 → 71.2
- **Balans 5P:** 90.4 → 90.8

### 🟢 Patch v1.0-alpha.153 (2026-08-30) — Format 3P: Próg oskarżenia (3p): 6 (Zysk 3P Δ +1.7 pkt)
- **Wynik 3P:** 3p **`71.7`** → **`73.4 pkt`** | Kanon 4P **`91.2`** | 5p **`93.2`** | Global **`85.8`**
- **Modyfikacja (`L1_THRESHOLD_MINUS1__L1_THRESHOLD_PLUS1`):** Próg oskarżenia (3p): 6.
- **Efekt:** Optymalizacja Formatu 3P (wyjątki `3p:`). Telemetria: Średnia Er 6.62, Deadlocks 0.1%, Pas Biedy 2.1%.

### 🟢 Patch v1.0-alpha.152 (2026-08-30) — Optymalizacja Silnika AI: Weryfikacja Ścieżek Ewakuacji CAA-10 & Obronne Oczyszczanie Herezji
- **Modyfikacja:** Poprawka silnika weryfikacji warunków wygranej `caa-10` (uwzględnienie `avoided_autodafe`, `shadow_exit`, `path_via_double`) oraz implementacja obronnego skalowania kart oczyszczania z Herezji (`caa-08`, `kb-05`, `kt-11`, `kt-12`, `gc-08`) w obecności Inkwizycji (`min(pl.heresy, dec) * (3.8 if has_so and pl.heresy >= 2 else 2.2)`). Usystematyzowanie rekomendacji dla formatów 3P & 4P w `setups.md`.
- **Wynik Globalny:** **82.8**
- **Balans 4P:** **90.6** (Kanon: `4p-no-oficjum` 97.8, `4p-no-korona` 95.4, `4p-core` 87.9, `4p-no-kabala` 87.9, `4p-no-cienie` 84.2)
- **Balans 3P:** **70.2** (Rekomendowane: `3p-oficjum-korona-kabala` 91.9, `3p-cienie-korona-gildia` 86.7, `3p-oficjum-alandalus-gildia` 83.9)
- **Balans 5P:** **87.6**

### 🌐 Patch v1.0-alpha.151 (2026-08-30) — Global Auditor: Karta `caa-12` (Skrytka w Murach): `gold` → `3` + Karta `caa-12` (Skrytka w Murach): `heresy` → `0` (Zysk Global Δ +0.6 pkt)
- **Modyfikacja:** `BAZA__L3_CAA-12_G3_H0` -> Karta `caa-12` (Skrytka w Murach): `gold` → `3` + Karta `caa-12` (Skrytka w Murach): `heresy` → `0`
- **Wynik Globalny:** 83.7 → **84.3**
- **Balans 4P:** 90.9 → 91.2
- **Balans 3P:** 70.2 → 71.2
- **Balans 5P:** 90.1 → 90.4

### 🌐 Patch v1.0-alpha.150 (2026-08-30) — Global Auditor: Karta `caa-09` (Kurier Relikwii): `gold` → `1` + Karta `caa-09` (Kurier Relikwii): `heresy` → `0` (Zysk Global Δ +0.2 pkt)
- **Modyfikacja:** `BAZA__L3_CAA-09_G1_H0` -> Karta `caa-09` (Kurier Relikwii): `gold` → `1` + Karta `caa-09` (Kurier Relikwii): `heresy` → `0`
- **Wynik Globalny:** 83.5 → **83.7**
- **Balans 4P:** 90.7 → 90.9
- **Balans 3P:** 69.0 → 70.2
- **Balans 5P:** 90.7 → 90.1

### 🌐 Patch v1.0-alpha.149 (2026-08-30) — Global Auditor: Karta `caa-03` (Cień na Rynku): `cost` → `2` (Zysk Global Δ +0.2 pkt)
- **Modyfikacja:** `BAZA__L3_CAA-03_COST_PLUS1` -> Karta `caa-03` (Cień na Rynku): `cost` → `2`
- **Wynik Globalny:** 83.3 → **83.5**
- **Balans 4P:** 91.2 → 90.7
- **Balans 3P:** 69.2 → 69.0
- **Balans 5P:** 89.5 → 90.7

### 🌐 Patch v1.0-alpha.148 (2026-08-30) — Global Auditor: Karta `gc-08` (Zatrute Złoto): `cost` → `0` + Karta `gc-08` (Zatrute Złoto): `gold` → `3` (Zysk Global Δ +0.7 pkt)
- **Modyfikacja:** `BAZA__L3_GC-08_C0_G3` -> Karta `gc-08` (Zatrute Złoto): `cost` → `0` + Karta `gc-08` (Zatrute Złoto): `gold` → `3`
- **Wynik Globalny:** 82.6 → **83.3**
- **Balans 4P:** 91.1 → 91.2
- **Balans 3P:** 69.6 → 69.2
- **Balans 5P:** 87.1 → 89.5

### 🌐 Patch v1.0-alpha.147 (2026-08-30) — Global Auditor: Karta `caa-09` (Kurier Relikwii): `cost` → `1` (Zysk Global Δ +0.1 pkt)
- **Modyfikacja:** `BAZA__L3_CAA-09_COST_PLUS1` -> Karta `caa-09` (Kurier Relikwii): `cost` → `1`
- **Wynik Globalny:** 82.5 → **82.6**
- **Balans 4P:** 90.6 → 91.1
- **Balans 3P:** 70.7 → 69.6
- **Balans 5P:** 86.2 → 87.1

### 🟢 Patch v1.0-alpha.146 (2026-08-30) — Format 3P: Złoto startowe (3p): 4 (Zysk 3P Δ +0.8 pkt)
- **Wynik 3P:** 3p **`70.1`** → **`70.9 pkt`** | Kanon 4P **`90.6`** | 5p **`90.0`** | Global **`83.8`**
- **Modyfikacja (`L1_START_GOLD_MINUS1`):** Złoto startowe (3p): 4.
- **Efekt:** Optymalizacja Formatu 3P (wyjątki `3p:`). Telemetria: Średnia Er 6.54, Deadlocks 0.1%, Pas Biedy 2.2%.

### 🌐 Patch v1.0-alpha.145 (2026-08-30) — Global Auditor: Karta `gc-01` (Przekupiony Strażnik): `cost` → `2` + Karta `gc-01` (Przekupiony Strażnik): `gold` → `2` (Zysk Global Δ +0.4 pkt)
- **Modyfikacja:** `BAZA__L3_GC-01_C2_G2` -> Karta `gc-01` (Przekupiony Strażnik): `cost` → `2` + Karta `gc-01` (Przekupiony Strażnik): `gold` → `2`
- **Wynik Globalny:** 82.1 → **82.5**
- **Balans 4P:** 90.4 → 90.6
- **Balans 3P:** 70.3 → 70.7
- **Balans 5P:** 85.5 → 86.2

### 🌐 Patch v1.0-alpha.144 (2026-08-30) — Global Auditor: Karta `so-09` (Świadek Koronny): `cost` → `0` + Karta `so-09` (Świadek Koronny): `heresy` → `3` (Zysk Global Δ +0.2 pkt)
- **Modyfikacja:** `BAZA__L3_SO-09_C0_H3` -> Karta `so-09` (Świadek Koronny): `cost` → `0` + Karta `so-09` (Świadek Koronny): `heresy` → `3`
- **Wynik Globalny:** 81.9 → **82.1**
- **Balans 4P:** 90.4 → 90.4
- **Balans 3P:** 70.4 → 70.3
- **Balans 5P:** 84.8 → 85.5

### 🌐 Patch v1.0-alpha.143 (2026-08-30) — Global Auditor: Karta `kb-02` (Pobór Podatków): `cost` → `0` + Karta `kb-02` (Pobór Podatków): `heresy` → `0` (Zysk Global Δ +1.7 pkt)
- **Modyfikacja:** `BAZA__L3_KB-02_C0_H0` -> Karta `kb-02` (Pobór Podatków): `cost` → `0` + Karta `kb-02` (Pobór Podatków): `heresy` → `0`
- **Wynik Globalny:** 80.2 → **81.9**
- **Balans 4P:** 89.9 → 90.4
- **Balans 3P:** 70.5 → 70.4
- **Balans 5P:** 80.2 → 84.8

### 🟢 Patch v1.0-alpha.142 (2026-08-30) — Pełna Sanacja i Oczyszczenie Pól-Widm (Ghost Fields) Kart
- **Modyfikacja:**
  - Oczyszczenie martwych pól `gold: 0`, `target_heresy: 0`, `agents: 0` z kart: `caa-01`, `gc-04`, `gc-09`, `kb-01`, `kb-04`, `kb-09`, `kb-10`, `kb-11`, `kt-01`, `kt-10`.
  - Usunięcie pasożytniczych parametrów `gold: 2` i `target_heresy: 0` z finiszera `kb-10` (*Pieczęć Korony*) oraz `gold: 1` z `kt-10` (*Pieczęć Salomona*).
  - Wdrożenie automatycznej kompilacji PDF (`HeadlessChrome`) w `scripts/pnp/generate.py`.
  - Naprawienie błędu w `scripts/pnp/generate_card_text.py` — od teraz wszystkie pola (`cost`, `heresy`, `gold`, `target_heresy`, `agents`) są bezwzględnie synchronizowane z SSOT do plików Markdown i KATALOG.md.
- **Wynik Globalny (16 setupów):** **77.1 pkt** (próba 160 000 partii)
- **Balans 4P:** **89.9 pkt** (`4p-core`: 96.4, `4p-no-korona`: 97.8, `4p-no-oficjum`: 92.3)
- **Balans 5P:** **80.2 pkt**
- **Balans 3P:** **70.4 pkt**

### 🌐 Patch v1.0-alpha.141 (2026-08-30) — Global Auditor: Karta `caa-03` (Cień na Rynku): `cost` → `1` + Karta `caa-03` (Cień na Rynku): `gold` → `1` (Zysk Global Δ +0.1 pkt)
- **Modyfikacja:** `BAZA__L3_CAA-03_C1_G1` -> Karta `caa-03` (Cień na Rynku): `cost` → `1` + Karta `caa-03` (Cień na Rynku): `gold` → `1`
- **Wynik Globalny:** 81.6 → **81.7**
- **Balans 4P:** 90.7 → 91.0
- **Balans 3P:** 71.2 → 71.0
- **Balans 5P:** 83.0 → 83.0

### 🌐 Patch v1.0-alpha.140 (2026-08-30) — Global Auditor: Karta `gc-10` (Upadek Domu): `heresy` → `0` (Zysk Global Δ +5.2 pkt)
- **Modyfikacja:** `BAZA__L3_GC-10_HERESY_MINUS2` -> Karta `gc-10` (Upadek Domu): `heresy` → `0`
- **Wynik Globalny:** 76.4 → **81.6**
- **Balans 4P:** 84.1 → 90.7
- **Balans 3P:** 74.7 → 71.2
- **Balans 5P:** 70.5 → 83.0

### 🌐 Patch v1.0-alpha.139 (2026-08-30) — Global Auditor: Karta `kt-11` (Medytacja Sefirot): `cost` → `1` + Karta `kt-11` (Medytacja Sefirot): `heresy` → `0` (Zysk Global Δ +0.6 pkt)
- **Modyfikacja:** `BAZA__L3_KT-11_C1_H0` -> Karta `kt-11` (Medytacja Sefirot): `cost` → `1` + Karta `kt-11` (Medytacja Sefirot): `heresy` → `0`
- **Wynik Globalny:** 75.8 → **76.4**
- **Balans 4P:** 85.2 → 84.1
- **Balans 3P:** 67.0 → 74.7
- **Balans 5P:** 75.3 → 70.5

### 🌐 Patch v1.0-alpha.138 (2026-08-30) — Global Auditor: Karta `caa-08` (Kaptur Nocy): `heresy` → `0` (Zysk Global Δ +5.2 pkt)
- **Modyfikacja:** `BAZA__L3_CAA-08_HERESY_MINUS1` -> Karta `caa-08` (Kaptur Nocy): `heresy` → `0`
- **Wynik Globalny:** 70.6 → **75.8**
- **Balans 4P:** 80.1 → 85.2
- **Balans 3P:** 66.5 → 67.0
- **Balans 5P:** 65.2 → 75.3

### 🟢 Patch v1.0-alpha.137 (2026-08-30) — Wdrożenie Twardych Limitów Kart i Oczyszczenie Anomalii
- **Modyfikacja:** 
  - Karta `so-03` (Podejrzenie): `heresy: 4 → 2`, `target_heresy: 3 → 1`, `cost: 2 → 1`
  - Karta `caa-12` (Skrytka w Murach): `gold: 4 → 3`, `heresy: 0 → 1`
  - Karta `gc-11` (Fałszywe Świadectwo Cechu): `heresy: 5 → 2`, `cost: 2 → 0`
  - Wdrożenie twardych limitów parametrów kart w SSOT (`src/inquisitio/config.py`), generatorze mutacji (`audit_level3.py`) oraz weryfikatorze (`verify_hygiene.py`).
- **Wynik Globalny:** 75.6 → **70.6 pkt** (`🔻 -5.0`)
- **Balans 4P:** 84.4 → **80.1 pkt** (`🔻 -4.3`)
- **Balans 3P:** 69.2 → **66.5 pkt** (`🔻 -2.7`)
- **Balans 5P:** 73.3 → **65.2 pkt** (`🔻 -8.1`)
- **Efekt:** Pełne zabezpieczenie silnika przed nielegalnymi wartościami i patologicznymi mutacjami; ostateczne usunięcie ukrytych anomalii na kartach `so-03`, `caa-12` i `gc-11` oraz zapieczętowanie granic fizycznych w silniku gry.

### 🟢 Patch v1.0-alpha.136 (2026-08-30) — Kompleksowa Sanacja Talii: Naprawa `gc-08` i Usunięcie Sztucznych Dopalaczy
- **Modyfikacja:** 
  - Karta `gc-08` (Zatrute Złoto): `cost: 1`, `gold: 1`, `target_heresy: 1`, `heresy: 1` — przywrócenie kanonicznego efektu (*„Zyskaj 1 złoto. Wskaż rywala: +1 Herezja.”*)
  - Usunięcie pasożytniczych iniekcji złota/herezji z kart taktycznych wprowadzonych przez mutacje audytora: `caa-03` (usunięto `gold: 4`), `caa-04` (usunięto `gold: 6`), `caa-05` (usunięto `gold: 4, target_heresy: 3`), `caa-06` (usunięto `gold: 1`), `caa-07` (usunięto `gold: 4`), `caa-08` (usunięto `gold: 1, target_heresy: 2`), `gc-07` (usunięto `gold: 3`), `so-04`/`so-05`/`so-07`/`so-08` (oczyszczono parametry z darmowego złota).
- **Wynik Globalny:** 86.4 → **75.6 pkt** (`🔻 -10.8`)
- **Balans 4P:** 91.8 → **84.4 pkt** (`🔻 -7.4`)
- **Balans 3P:** 71.1 → **69.2 pkt** (`🔻 -1.9`)
- **Balans 5P:** 96.2 → **73.3 pkt** (`🔻 -22.9`)
- **Efekt:** Pełne przywrócenie tożsamości mechanicznej i ekonomicznej talii; eliminacja fałszywych dopalaczy ("darmowego bankomatu") w silniku symulacji. Wynik spadł do realnego, niezafałszowanego stanu bazowego, ujawniając prawdziwe luki w balansie wymagające rzetelnego strojenia.

### 🟢 Patch v1.0-alpha.135 (2026-08-30) — Rekalibracja Gildii Cieni: Karta `gc-08` (Zatrute Złoto)
- **Modyfikacja:** Karta `gc-08` (Zatrute Złoto): `cost: 1 → 2`, `gold: 0 → 1`
- **Wynik Globalny:** 86.4 → **86.4 pkt**
- **Balans 4P:** 91.8 → **91.8 pkt**
- **Balans 3P:** 71.1 → **71.1 pkt**
- **Balans 5P:** 96.2 → **96.2 pkt**
- **Efekt:** Naprawa mechaniczna karty ekonomicznej Gildii Cieni (usunięcie martwego efektu `gold: 0` z v134) ze zrównoważonym kosztem 2 złote; naprawa błędu testów jednostkowych i zachowanie stabilnego balansu we wszystkich formatach.

### 🌐 Patch v1.0-alpha.134 (2026-08-30) — Global Auditor: Karta `caa-04` (Fałszywy Trop): `cost` → `0` + Karta `caa-04` (Fałszywy Trop): `gold` → `6` (Zysk Global Δ +0.1 pkt)
- **Modyfikacja:** `BAZA__L3_CAA-04_C0_G6` -> Karta `caa-04` (Fałszywy Trop): `cost` → `0` + Karta `caa-04` (Fałszywy Trop): `gold` → `6`
- **Wynik Globalny:** 86.3 → **86.4**
- **Balans 4P:** 91.9 → 91.8
- **Balans 3P:** 71.1 → 71.1
- **Balans 5P:** 95.9 → 96.2

### 🌐 Patch v1.0-alpha.133 (2026-08-30) — Global Auditor: Karta `so-09` (Świadek Koronny): `heresy` → `2` (Zysk Global Δ +0.1 pkt)
- **Modyfikacja:** `BAZA__L3_SO-09_HERESY_PLUS1` -> Karta `so-09` (Świadek Koronny): `heresy` → `2`
- **Wynik Globalny:** 86.2 → **86.3**
- **Balans 4P:** 92.1 → 91.9
- **Balans 3P:** 70.4 → 71.1
- **Balans 5P:** 96.1 → 95.9

### 🌐 Patch v1.0-alpha.132 (2026-08-30) — Global Auditor: Karta `gc-11` (Fałszywe Świadectwo Cechu): `cost` → `2` (Zysk Global Δ +0.1 pkt)
- **Modyfikacja:** `BAZA__L3_GC-11_COST_PLUS2` -> Karta `gc-11` (Fałszywe Świadectwo Cechu): `cost` → `2`
- **Wynik Globalny:** 86.1 → **86.2**
- **Balans 4P:** 92.5 → 92.1
- **Balans 3P:** 70.3 → 70.4
- **Balans 5P:** 95.4 → 96.1

### 🌐 Patch v1.0-alpha.131 (2026-08-30) — Global Auditor: Karta `kt-09` (Fragment Kodeksu): `cost` → `2` + Karta `kt-09` (Fragment Kodeksu): `gold` → `1` (Zysk Global Δ +0.1 pkt)
- **Modyfikacja:** `BAZA__L3_KT-09_C2_G1` -> Karta `kt-09` (Fragment Kodeksu): `cost` → `2` + Karta `kt-09` (Fragment Kodeksu): `gold` → `1`
- **Wynik Globalny:** 86.0 → **86.1**
- **Balans 4P:** 92.9 → 92.5
- **Balans 3P:** 69.8 → 70.3
- **Balans 5P:** 95.4 → 95.4

### 🌐 Patch v1.0-alpha.130 (2026-08-30) — Global Auditor: Karta `gc-08` (Zatrute Złoto): `gold` → `0` + Karta `gc-08` (Zatrute Złoto): `heresy` → `1` (Zysk Global Δ +0.2 pkt)
- **Modyfikacja:** `BAZA__L3_GC-08_G0_H1` -> Karta `gc-08` (Zatrute Złoto): `gold` → `0` + Karta `gc-08` (Zatrute Złoto): `heresy` → `1`
- **Wynik Globalny:** 85.8 → **86.0**
- **Balans 4P:** 92.8 → 92.9
- **Balans 3P:** 69.8 → 69.8
- **Balans 5P:** 94.8 → 95.4

### 🌐 Patch v1.0-alpha.129 (2026-08-30) — Global Auditor: Karta `gc-11` (Fałszywe Świadectwo Cechu): `gold` → `1` + Karta `gc-11` (Fałszywe Świadectwo Cechu): `heresy` → `5` (Zysk Global Δ +0.1 pkt)
- **Modyfikacja:** `BAZA__L3_GC-11_G1_H5` -> Karta `gc-11` (Fałszywe Świadectwo Cechu): `gold` → `1` + Karta `gc-11` (Fałszywe Świadectwo Cechu): `heresy` → `5`
- **Wynik Globalny:** 85.7 → **85.8**
- **Balans 4P:** 92.6 → 92.8
- **Balans 3P:** 69.7 → 69.8
- **Balans 5P:** 94.8 → 94.8

### 🌐 Patch v1.0-alpha.128 (2026-08-30) — Global Auditor: Karta `gc-12` (Złodziejski Zwiad): `cost` → `1` + Karta `gc-12` (Złodziejski Zwiad): `gold` → `2` (Zysk Global Δ +0.1 pkt)
- **Modyfikacja:** `BAZA__L3_GC-12_C1_G2` -> Karta `gc-12` (Złodziejski Zwiad): `cost` → `1` + Karta `gc-12` (Złodziejski Zwiad): `gold` → `2`
- **Wynik Globalny:** 85.6 → **85.7**
- **Balans 4P:** 92.4 → 92.6
- **Balans 3P:** 69.6 → 69.7
- **Balans 5P:** 94.9 → 94.8

### 🌐 Patch v1.0-alpha.127 (2026-08-30) — Global Auditor: Karta `caa-04` (Fałszywy Trop): `cost` → `0` + Karta `caa-04` (Fałszywy Trop): `gold` → `5` (Zysk Global Δ +0.1 pkt)
- **Modyfikacja:** `BAZA__L3_CAA-04_C0_G5` -> Karta `caa-04` (Fałszywy Trop): `cost` → `0` + Karta `caa-04` (Fałszywy Trop): `gold` → `5`
- **Wynik Globalny:** 85.5 → **85.6**
- **Balans 4P:** 93.1 → 92.4
- **Balans 3P:** 70.0 → 69.6
- **Balans 5P:** 93.3 → 94.9

### 🌐 Patch v1.0-alpha.126 (2026-08-30) — Global Auditor: Karta `caa-08` (Kaptur Nocy): `gold` → `1` + Karta `caa-08` (Kaptur Nocy): `heresy` → `1` (Zysk Global Δ +0.2 pkt)
- **Modyfikacja:** `BAZA__L3_CAA-08_G1_H1` -> Karta `caa-08` (Kaptur Nocy): `gold` → `1` + Karta `caa-08` (Kaptur Nocy): `heresy` → `1`
- **Wynik Globalny:** 85.3 → **85.5**
- **Balans 4P:** 93.4 → 93.1
- **Balans 3P:** 69.8 → 70.0
- **Balans 5P:** 92.6 → 93.3

### 🌐 Patch v1.0-alpha.125 (2026-08-30) — Global Auditor: Karta `gc-02` (Czarny Rynek): `gold` → `3` + Karta `gc-02` (Czarny Rynek): `heresy` → `0` (Zysk Global Δ +0.1 pkt)
- **Modyfikacja:** `BAZA__L3_GC-02_G3_H0` -> Karta `gc-02` (Czarny Rynek): `gold` → `3` + Karta `gc-02` (Czarny Rynek): `heresy` → `0`
- **Wynik Globalny:** 85.2 → **85.3**
- **Balans 4P:** 92.0 → 93.4
- **Balans 3P:** 69.7 → 69.8
- **Balans 5P:** 93.9 → 92.6

### 🌐 Patch v1.0-alpha.124 (2026-08-30) — Global Auditor: Karta `gc-11` (Fałszywe Świadectwo Cechu): `cost` → `1` + Karta `gc-11` (Fałszywe Świadectwo Cechu): `gold` → `1` (Zysk Global Δ +0.2 pkt)
- **Modyfikacja:** `BAZA__L3_GC-11_C1_G1` -> Karta `gc-11` (Fałszywe Świadectwo Cechu): `cost` → `1` + Karta `gc-11` (Fałszywe Świadectwo Cechu): `gold` → `1`
- **Wynik Globalny:** 85.0 → **85.2**
- **Balans 4P:** 92.0 → 92.0
- **Balans 3P:** 69.6 → 69.7
- **Balans 5P:** 93.3 → 93.9

### 🌐 Patch v1.0-alpha.123 (2026-08-30) — Global Auditor: Karta `caa-11` (Nocna Zmiana Warty): `cost` → `2` + Karta `caa-11` (Nocna Zmiana Warty): `heresy` → `0` (Zysk Global Δ +0.1 pkt)
- **Modyfikacja:** `BAZA__L3_CAA-11_C2_H0` -> Karta `caa-11` (Nocna Zmiana Warty): `cost` → `2` + Karta `caa-11` (Nocna Zmiana Warty): `heresy` → `0`
- **Wynik Globalny:** 84.9 → **85.0**
- **Balans 4P:** 92.0 → 92.0
- **Balans 3P:** 69.7 → 69.6
- **Balans 5P:** 93.0 → 93.3

### 🌐 Patch v1.0-alpha.122 (2026-08-30) — Global Auditor: Karta `kt-10` (Pieczęć Salomona): `gold` → `1` + Karta `kt-10` (Pieczęć Salomona): `heresy` → `0` (Zysk Global Δ +0.6 pkt)
- **Modyfikacja:** `BAZA__L3_KT-10_G1_H0` -> Karta `kt-10` (Pieczęć Salomona): `gold` → `1` + Karta `kt-10` (Pieczęć Salomona): `heresy` → `0`
- **Wynik Globalny:** 84.3 → **84.9**
- **Balans 4P:** 92.0 → 92.0
- **Balans 3P:** 68.9 → 69.7
- **Balans 5P:** 92.0 → 93.0

### 🌐 Patch v1.0-alpha.121 (2026-08-30) — Global Auditor: Karta `caa-02` (Złoto z Kryjówki): `cost` → `1` + Karta `caa-02` (Złoto z Kryjówki): `heresy` → `1` (Zysk Global Δ +0.3 pkt)
- **Modyfikacja:** `BAZA__L3_CAA-02_C1_H1` -> Karta `caa-02` (Złoto z Kryjówki): `cost` → `1` + Karta `caa-02` (Złoto z Kryjówki): `heresy` → `1`
- **Wynik Globalny:** 84.0 → **84.3**
- **Balans 4P:** 92.4 → 92.0
- **Balans 3P:** 68.9 → 68.9
- **Balans 5P:** 90.6 → 92.0

### 🌐 Patch v1.0-alpha.120 (2026-08-30) — Global Auditor: Karta `caa-08` (Kaptur Nocy): `heresy` → `1` (Zysk Global Δ +0.4 pkt)
- **Modyfikacja:** `BAZA__L3_CAA-08_HERESY_PLUS1` -> Karta `caa-08` (Kaptur Nocy): `heresy` → `1`
- **Wynik Globalny:** 83.6 → **84.0**
- **Balans 4P:** 92.2 → 92.4
- **Balans 3P:** 68.7 → 68.9
- **Balans 5P:** 90.0 → 90.6

### 🌐 Patch v1.0-alpha.119 (2026-08-30) — Global Auditor: Karta `kb-04` (Faworyt Dworu): `heresy` → `3` (Zysk Global Δ +0.3 pkt)
- **Modyfikacja:** `BAZA__L3_KB-04_HERESY_PLUS2` -> Karta `kb-04` (Faworyt Dworu): `heresy` → `3`
- **Wynik Globalny:** 83.3 → **83.6**
- **Balans 4P:** 92.2 → 92.2
- **Balans 3P:** 68.1 → 68.7
- **Balans 5P:** 89.5 → 90.0

### 🌐 Patch v1.0-alpha.118 (2026-08-30) — Global Auditor: Karta `caa-11` (Nocna Zmiana Warty): `heresy` → `2` (Zysk Global Δ +0.1 pkt)
- **Modyfikacja:** `BAZA__L3_CAA-11_HERESY_SET2` -> Karta `caa-11` (Nocna Zmiana Warty): `heresy` → `2`
- **Wynik Globalny:** 83.2 → **83.3**
- **Balans 4P:** 92.1 → 92.2
- **Balans 3P:** 68.1 → 68.1
- **Balans 5P:** 89.3 → 89.5

### 🌐 Patch v1.0-alpha.117 (2026-08-30) — Global Auditor: Karta `caa-03` (Cień na Rynku): `cost` → `0` + Karta `caa-03` (Cień na Rynku): `gold` → `4` (Zysk Global Δ +0.1 pkt)
- **Modyfikacja:** `BAZA__L3_CAA-03_C0_G4` -> Karta `caa-03` (Cień na Rynku): `cost` → `0` + Karta `caa-03` (Cień na Rynku): `gold` → `4`
- **Wynik Globalny:** 83.1 → **83.2**
- **Balans 4P:** 92.3 → 92.1
- **Balans 3P:** 68.2 → 68.1
- **Balans 5P:** 88.9 → 89.3

### 🌐 Patch v1.0-alpha.116 (2026-08-30) — Global Auditor: Karta `gc-05` (Fałszywy Świadek): `cost` → `2` + Karta `gc-05` (Fałszywy Świadek): `heresy` → `1` (Zysk Global Δ +0.2 pkt)
- **Modyfikacja:** `BAZA__L3_GC-05_C2_H1` -> Karta `gc-05` (Fałszywy Świadek): `cost` → `2` + Karta `gc-05` (Fałszywy Świadek): `heresy` → `1`
- **Wynik Globalny:** 82.9 → **83.1**
- **Balans 4P:** 91.9 → 92.3
- **Balans 3P:** 68.2 → 68.2
- **Balans 5P:** 88.6 → 88.9




### 🌐 Patch v1.0-alpha.115 (2026-08-30) — Global Auditor: Karta `caa-06` (Ucieczka z Lochów): `cost` → `0` + Karta `caa-06` (Ucieczka z Lochów): `gold` → `1` (Zysk Global Δ +0.5 pkt)
- **Modyfikacja:** `BAZA__L3_CAA-06_C0_G1` -> Karta `caa-06` (Ucieczka z Lochów): `cost` → `0` + Karta `caa-06` (Ucieczka z Lochów): `gold` → `1`
- **Wynik Globalny:** 82.4 → **82.9**
- **Balans 4P:** 91.0 → 91.9
- **Balans 3P:** 67.4 → 68.2
- **Balans 5P:** 88.7 → 88.6

### 🌐 Patch v1.0-alpha.114 (2026-08-30) — Global Auditor: Karta `gc-11` (Fałszywe Świadectwo Cechu): `gold` → `0` + Karta `gc-11` (Fałszywe Świadectwo Cechu): `heresy` → `4` (Zysk Global Δ +0.1 pkt)
- **Modyfikacja:** `BAZA__L3_GC-11_G0_H4` -> Karta `gc-11` (Fałszywe Świadectwo Cechu): `gold` → `0` + Karta `gc-11` (Fałszywe Świadectwo Cechu): `heresy` → `4`
- **Wynik Globalny:** 82.3 → **82.4**
- **Balans 4P:** 91.5 → 91.0
- **Balans 3P:** 67.0 → 67.4
- **Balans 5P:** 88.5 → 88.7

### 🌐 Patch v1.0-alpha.113 (2026-08-30) — Global Auditor: Karta `gc-11` (Fałszywe Świadectwo Cechu): `cost` → `0` + Karta `gc-11` (Fałszywe Świadectwo Cechu): `heresy` → `3` (Zysk Global Δ +0.1 pkt)
- **Modyfikacja:** `L3_GC-11_C0_H3`
- **Wynik Globalny:** 82.2 → **82.3**
- **Balans 4P:** 92.8 → 91.5
- **Balans 3P:** 67.0 → 67.0
- **Balans 5P:** 86.8 → 88.5

### 🌐 Patch v1.0-alpha.112 (2026-08-30) — Global Auditor: Karta `caa-07` (Szantaż Bractwa): `cost` → `0` + Karta `caa-07` (Szantaż Bractwa): `gold` → `4` (Zysk Global Δ +1.6 pkt)
- **Modyfikacja:** `L3_CAA-07_C0_G4`
- **Wynik Globalny:** 80.6 → **82.2**
- **Balans 4P:** 91.3 → 92.8
- **Balans 3P:** 66.3 → 67.0
- **Balans 5P:** 84.3 → 86.8

### 🟢 Patch v1.0-alpha.109 (2026-08-30) — Kanon 4P: Karta `kb-04` (Faworyt Dworu): `gold` → `0` + Karta `kb-04` (Faworyt Dworu): `heresy` → `1` (Zysk 4P Δ +0.5 pkt)
- **Wynik 4P:** Kanon **`92.2`** → **`92.7 pkt`** | Global **`69.8`** | 3p **`54.2`** | 5p **`62.6`**
- **Modyfikacja (`L3_KB-04_G0_H1`):** Karta `kb-04` (Faworyt Dworu): `gold` → `0` + Karta `kb-04` (Faworyt Dworu): `heresy` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.78, Deadlocks 0.0%, Pas Biedy 4.0%.

### 🟢 Patch v1.0-alpha.106 (2026-08-30) — Format 3P: SO Skazania (3p): 2 (Decyzja Projektowa)
- **Wynik 3P:** Ręczna korekta balansu (Custom Base dla Audytora Globalnego).
- **Modyfikacja:** `victory.swiete_oficjum.condemns.3p: 3 → 2`.
- **Efekt:** Wymuszenie witalności ścieżki Skazań w 3P (przywrócenie podwójnej ścieżki wygranej jako opłacalnej alternatywy dla stosów). Baza dla optymalizacji globalnej kartami (L3).

### 🟢 Patch v1.0-alpha.105 (2026-08-30) — Format 3P: Złoto startowe (3p): 5 (Zysk 3P Δ +6.9 pkt)
- **Wynik 3P:** 3p **`61.1`** → **`68.0 pkt`** | Kanon 4P **`90.7`** | 5p **`88.9`** | Global **`73.5`**
- **Modyfikacja (`L1_START_GOLD_PLUS1`):** Złoto startowe (3p): 5.
- **Efekt:** Optymalizacja Formatu 3P (wyjątki `3p:`). Telemetria: Średnia Er 6.46, Deadlocks 0.1%, Pas Biedy 2.6%.

### 🟢 Patch v1.0-alpha.104 (2026-08-30) — Format 3P: SO Stosy (3p): 6, GC Upadki (3p): 8 (Zysk 3P Δ +7.2 pkt)
- **Wynik 3P:** 3p **`54.9`** → **`62.1 pkt`** | Kanon 4P **`90.7`** | 5p **`88.9`** | Global **`72.1`**
- **Modyfikacja (`L2_GC_FALLS_MINUS1__L2_SO_STACKS_MINUS1`):** SO Stosy (3p): 6, GC Upadki (3p): 8.
- **Efekt:** Optymalizacja Formatu 3P (wyjątki `3p:`). Telemetria: Średnia Er 6.62, Deadlocks 0.1%, Pas Biedy 3.3%.

### 🟢 Patch v1.0-alpha.99 (2026-08-29) — Kanon 4P: Karta `caa-01` (Przejście Podziemiami): `cost` → `1`, `heresy` → `1` + Karta `kb-08` (Przekupstwo Sędziego): `heresy` → `1`
- **Wynik 4P:** Kanon **`94.7`** → **`93.9 pkt`** | Global **`51.2`** | 3p **`33.1`** | 5p **`25.8`**
- **Modyfikacja:** `caa-01` (Przejście Podziemiami): `cost: 2 → 1`, `heresy: 2 → 1` oraz `kb-08` (Przekupstwo Sędziego): `heresy: 2 → 1`.
- **Efekt:** Likwidacja nadmiernego autopodatku (Self-Harm Tax) przy zachowaniu płynności i stabilności stołu 4P.

### 🟢 Patch v1.0-alpha.98 (2026-08-29) — Kanon 4P: Karta `so-11` (Dekret Czystości Wiary): `cost` → `0` (Eliminacja Disruptora)
- **Wynik 4P:** Kanon **`94.6`** → **`94.7 pkt`** | Global **`51.2`** | 3p **`33.1`** | 5p **`25.8`**
- **Modyfikacja:** `so-11` (Dekret Czystości Wiary): `cost: 1 → 0`.
- **Efekt:** Likwidacja statusu Disruptora, +1zł zysku netto rekompensuje 1☣ własnej herezji.

### 🟢 Patch v1.0-alpha.97 (2026-08-29) — Kanon 4P: Karta `caa-08` (Kaptur Nocy): `cost` → `2` + Karta `caa-08` (Kaptur Nocy): `gold` → `2` + Karta `so-05` (Wezwanie do Trybunału): `gold` → `3` + Karta `so-05` (Wezwanie do Trybunału): `heresy` → `4` (Zysk 4P Δ +0.1 pkt)
- **Wynik 4P:** Kanon **`94.5`** → **`94.6 pkt`** | Global **`51.2`** | 3p **`33.1`** | 5p **`25.8`**
- **Modyfikacja (`L3_CAA-08_COST_MINUS1__L3_CAA-08_GOLD_MINUS1__L3_SO-05_G3_H4`):** Karta `caa-08` (Kaptur Nocy): `cost` → `2` + Karta `caa-08` (Kaptur Nocy): `gold` → `2` + Karta `so-05` (Wezwanie do Trybunału): `gold` → `3` + Karta `so-05` (Wezwanie do Trybunału): `heresy` → `4`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.77, Deadlocks 0.0%, Pas Biedy 4.9%.

### 🟢 Patch v1.0-alpha.96 (2026-08-29) — Kanon 4P: Próg Obserwowanej: offset -1 (nowy: 3) + Karta `gc-08` (Zatrute Złoto): `gold` → `0` + Karta `caa-05` (Ukryty Kurier): `cost` → `0` + Karta `caa-05` (Ukryty Kurier): `gold` → `4` + Karta `gc-07` (Skrytobójstwo): `gold` → `3` (Zysk 4P Δ +0.3 pkt)
- **Wynik 4P:** Kanon **`94.2`** → **`94.5 pkt`** | Global **`51.1`** | 3p **`33.1`** | 5p **`25.8`**
- **Modyfikacja (`L1_OBSERVED_MINUS1__L3_CAA-05_C0_G4__L3_GC-07_GOLD_PLUS1__L3_GC-08_GOLD_MINUS1`):** Próg Obserwowanej: offset -1 (nowy: 3) + Karta `gc-08` (Zatrute Złoto): `gold` → `0` + Karta `caa-05` (Ukryty Kurier): `cost` → `0` + Karta `caa-05` (Ukryty Kurier): `gold` → `4` + Karta `gc-07` (Skrytobójstwo): `gold` → `3`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.77, Deadlocks 0.0%, Pas Biedy 4.9%.

### 🟢 Patch v1.0-alpha.95 (2026-08-29) — Kanon 4P: Karta `so-05` (Wezwanie do Trybunału): `target_heresy` → `3` + Karta `gc-07` (Skrytobójstwo): `gold` → `2` (Zysk 4P Δ +0.1 pkt)
- **Wynik 4P:** Kanon **`94.1`** → **`94.2 pkt`** | Global **`51.0`** | 3p **`33.1`** | 5p **`25.8`**
- **Modyfikacja (`L3_GC-07_GOLD_SET2__L3_SO-05_TARGET_HERESY_PLUS2`):** Karta `so-05` (Wezwanie do Trybunału): `target_heresy` → `3` + Karta `gc-07` (Skrytobójstwo): `gold` → `2`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.77, Deadlocks 0.0%, Pas Biedy 4.9%.

### 🟢 Patch v1.0-alpha.94 (2026-08-29) — Kanon 4P: Karta `so-05` (Wezwanie do Trybunału): `heresy` → `3` + Karta `so-05` (Wezwanie do Trybunału): `gold` → `2` + Karta `caa-05` (Ukryty Kurier): `gold` → `2` (Zysk 4P Δ +0.1 pkt)
- **Wynik 4P:** Kanon **`94.0`** → **`94.1 pkt`** | Global **`51.0`** | 3p **`33.1`** | 5p **`25.8`**
- **Modyfikacja (`L3_CAA-05_GOLD_MINUS1__L3_SO-05_GOLD_SET2__L3_SO-05_HERESY_PLUS2`):** Karta `so-05` (Wezwanie do Trybunału): `heresy` → `3` + Karta `so-05` (Wezwanie do Trybunału): `gold` → `2` + Karta `caa-05` (Ukryty Kurier): `gold` → `2`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.77, Deadlocks 0.0%, Pas Biedy 4.9%.

### 🟢 Patch v1.0-alpha.93 (2026-08-29) — Kanon 4P: Karta `gc-05` (Fałszywy Świadek): `cost` → `1` + Karta `gc-05` (Fałszywy Świadek): `heresy` → `0` + Karta `gc-07` (Skrytobójstwo): `gold` → `0` + Karta `caa-12` (Skrytka w Murach): `cost` → `1` (Zysk 4P Δ +0.2 pkt)
- **Wynik 4P:** Kanon **`93.8`** → **`94.0 pkt`** | Global **`51.0`** | 3p **`33.1`** | 5p **`25.8`**
- **Modyfikacja (`L3_CAA-12_COST_PLUS1__L3_GC-05_C1_H0__L3_GC-07_GOLD_MINUS2`):** Karta `gc-05` (Fałszywy Świadek): `cost` → `1` + Karta `gc-05` (Fałszywy Świadek): `heresy` → `0` + Karta `gc-07` (Skrytobójstwo): `gold` → `0` + Karta `caa-12` (Skrytka w Murach): `cost` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.77, Deadlocks 0.0%, Pas Biedy 4.9%.

### 🟢 Patch v1.0-alpha.92 (2026-08-29) — Kanon 4P: Limit Er: offset +1 (nowy: 15) + Cooldown Autodafé: offset -1 (nowy: 3) + Karta `caa-06` (Ucieczka z Lochów): `target_heresy` → `1` + Karta `kt-01` (Rytuał Przejścia): `gold` → `1`, `heresy` → `1` + Karta `caa-01` (Przejście Podziemiami): `cost` → `2`, `heresy` → `2` + Karta `caa-11` (Nocna Zmiana Warty): `gold` → `1` + Karta `so-02` (Skarbiec Trybunału): `target_heresy` → `2` (Zysk 4P Δ +1.7 pkt)
- **Wynik 4P:** Kanon **`92.1`** → **`93.8 pkt`** | Global **`50.9`** | 3p **`33.1`** | 5p **`25.7`**
- **Modyfikacja (`L3_CAA-06_TARGET_HERESY_MINUS1__L3_KT-01_G1_H1__L3_CAA-01_C2_H2__L3_CAA-11_GOLD_MINUS2__L1_MAX_ERAS_PLUS1__L3_SO-02_TARGET_HERESY_PLUS1__L1_AUTODAFE_COOLDOWN_MINUS1`):** Limit Er: offset +1 (nowy: 15) + Cooldown Autodafé: offset -1 (nowy: 3) + Karta `caa-06` (Ucieczka z Lochów): `target_heresy` → `1` + Karta `kt-01` (Rytuał Przejścia): `gold` → `1`, `heresy` → `1` + Karta `caa-01` (Przejście Podziemiami): `cost` → `2`, `heresy` → `2` + Karta `caa-11` (Nocna Zmiana Warty): `gold` → `1` + Karta `so-02` (Skarbiec Trybunału): `target_heresy` → `2`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.76, Deadlocks 0.0%, Pas Biedy 4.8%.

### 🟢 Patch v1.0-alpha.91 (2026-08-29) — Kanon 4P: Karta `gc-07` (Skrytobójstwo): `gold` → `2` (Zysk 4P Δ +0.1 pkt)
- **Wynik 4P:** Kanon **`92.0`** → **`92.1 pkt`** | Global **`50.0`** | 3p **`32.7`** | 5p **`25.1`**
- **Modyfikacja (`L3_GC-07_GOLD_SET2`):** Karta `gc-07` (Skrytobójstwo): `gold` → `2`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.75, Deadlocks 0.0%, Pas Biedy 4.9%.

### 🟢 Patch v1.0-alpha.90 (2026-08-29) — Kanon 4P: Karta `kt-12` (Strażnik Archiwum): `heresy` → `0` + Karta `kt-12` (Strażnik Archiwum): `cost` → `1` (Zysk 4P Δ +1.9 pkt)
- **Wynik 4P:** Kanon **`90.1`** → **`92.0 pkt`** | Global **`49.9`** | 3p **`32.7`** | 5p **`25.1`**
- **Modyfikacja (`L3_KT-12_HERESY_MINUS1__L3_KT-12_COST_PLUS1`):** Karta `kt-12` (Strażnik Archiwum): `heresy` → `0` + Karta `kt-12` (Strażnik Archiwum): `cost` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.77, Deadlocks 0.0%, Pas Biedy 4.9%.

### 🟢 Patch v1.0-alpha.89 (2026-08-29) — Kanon 4P: Karta `gc-08` (Zatrute Złoto): `target_heresy` → `0` (Zysk 4P Δ +0.8 pkt)
- **Wynik 4P:** Kanon **`89.3`** → **`90.1 pkt`** | Global **`49.5`** | 3p **`33.0`** | 5p **`25.5`**
- **Modyfikacja (`L3_GC-08_TARGET_HERESY_MINUS1`):** Karta `gc-08` (Zatrute Złoto): `target_heresy` → `0`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.69, Deadlocks 0.0%, Pas Biedy 4.6%.

### 🟢 Patch v1.0-alpha.88 (2026-08-29) — Kanon 4P: Karta `kb-08` (Przekupstwo Sędziego): `heresy` → `2` (Zysk 4P Δ +0.9 pkt)
- **Wynik 4P:** Kanon **`88.4`** → **`89.3 pkt`** | Global **`49.3`** | 3p **`33.0`** | 5p **`25.5`**
- **Modyfikacja (`L3_KB-08_HERESY_SET2`):** Karta `kb-08` (Przekupstwo Sędziego): `heresy` → `2`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.70, Deadlocks 0.0%, Pas Biedy 4.6%.

### 🟢 Patch v1.0-alpha.87 (2026-08-29) — Kanon 4P: Karta `so-03` (Podejrzenie): `heresy` → `4` (Zysk 4P Δ +0.9 pkt)
- **Wynik 4P:** Kanon **`87.5`** → **`88.4 pkt`** | Global **`49.0`** | 3p **`33.0`** | 5p **`25.6`**
- **Modyfikacja (`L3_SO-03_HERESY_PLUS1`):** Karta `so-03` (Podejrzenie): `heresy` → `4`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.72, Deadlocks 0.0%, Pas Biedy 4.7%.

### 🟢 Patch v1.0-alpha.86 (2026-08-29) — Kanon 4P: Karta `so-03` (Podejrzenie): `gold` → `0` (Zysk 4P Δ +2.4 pkt)
- **Wynik 4P:** Kanon **`85.1`** → **`87.5 pkt`** | Global **`48.6`** | 3p **`32.9`** | 5p **`25.4`**
- **Modyfikacja (`L3_SO-03_GOLD_MINUS1`):** Karta `so-03` (Podejrzenie): `gold` → `0`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.73, Deadlocks 0.0%, Pas Biedy 4.8%.

### 🟢 Patch v1.0-alpha.85 (2026-08-29) — Kanon 4P: Karta `so-09` (Świadek Koronny): `heresy` → `1` (Zysk 4P Δ +1.4 pkt)
- **Wynik 4P:** Kanon **`83.7`** → **`85.1 pkt`** | Global **`47.6`** | 3p **`32.7`** | 5p **`24.9`**
- **Modyfikacja (`L3_SO-09_HERESY_PLUS1`):** Karta `so-09` (Świadek Koronny): `heresy` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.70, Deadlocks 0.0%, Pas Biedy 4.7%.

### 🟢 Patch v1.0-alpha.84 (2026-08-29) — Kanon 4P: Karta `caa-11` (Nocna Zmiana Warty): `target_heresy` → `1` (Zysk 4P Δ +1.3 pkt)
- **Wynik 4P:** Kanon **`82.4`** → **`83.7 pkt`** | Global **`47.0`** | 3p **`32.5`** | 5p **`24.7`**
- **Modyfikacja (`L3_CAA-11_TARGET_HERESY_MINUS1`):** Karta `caa-11` (Nocna Zmiana Warty): `target_heresy` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.74, Deadlocks 0.0%, Pas Biedy 4.8%.

### 🟢 Patch v1.0-alpha.83 (2026-08-29) — Kanon 4P: Karta `caa-10` (Echo Alhambry): `cost` → `2` (Zysk 4P Δ +1.1 pkt)
- **Wynik 4P:** Kanon **`81.3`** → **`82.4 pkt`** | Global **`46.5`** | 3p **`32.4`** | 5p **`24.6`**
- **Modyfikacja (`L3_CAA-10_COST_MINUS1`):** Karta `caa-10` (Echo Alhambry): `cost` → `2`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.71, Deadlocks 0.0%, Pas Biedy 4.8%.

### 🟢 Patch v1.0-alpha.82 (2026-08-29) — Kanon 4P: Karta `so-12` (Straż Trybunalska): `heresy` → `2` (Zysk 4P Δ +3.2 pkt)
- **Wynik 4P:** Kanon **`78.1`** → **`81.3 pkt`** | Global **`46.0`** | 3p **`32.3`** | 5p **`24.4`**
- **Modyfikacja (`L3_SO-12_HERESY_PLUS1`):** Karta `so-12` (Straż Trybunalska): `heresy` → `2`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.73, Deadlocks 0.0%, Pas Biedy 4.8%.

### 🟢 Patch v1.0-alpha.81 (2026-08-29) — Kanon 4P: Karta `kb-10` (Pieczęć Korony): `gold` → `2` (Zysk 4P Δ +2.4 pkt)
- **Wynik 4P:** Kanon **`75.7`** → **`78.1 pkt`** | Global **`44.4`** | 3p **`31.7`** | 5p **`23.5`**
- **Modyfikacja (`L3_KB-10_GOLD_SET2`):** Karta `kb-10` (Pieczęć Korony): `gold` → `2`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.77, Deadlocks 0.0%, Pas Biedy 4.6%.

### 🟢 Patch v1.0-alpha.80 (2026-08-29) — Przejście na Silnik Natywny C++20, Eliminacja Błędów i Czysty Baseline SSOT
- **Wynik 4P:** Kanon **`75.7 pkt`** (Core: `71.6`, No-Cienie: `63.6`, No-Kabała: `93.5`, No-Korona: `68.3`, No-Oficjum: `81.6`) | Global **`41.6`** | 3p **`30.7`** | 5p **`22.2`**
- **Kluczowa Zmiana Architektoniczna:**
  1. **Natywny Silnik C++20 (`inquisitio_native`):** Pełna migracja symulatora na wysokowydajny silnik wielowątkowy C++20 (skok przepustowości z ~15 gier/s do ponad 500–1000 gier/s), umożliwiający testowanie wielotysięcznych prób statystycznych w czasie rzeczywistym.
  2. **Usunięcie Błędu Dekretów Korony (Rozjazd 3 vs 2):** Wykryto i naprawiono krytyczny rozjazd, w którym stary silnik C++ miał na sztywno wpisane 3 dekrety (podczas gdy SSOT YAML wymagał 2). Powodowało to aplikowanie mutacji `-1 dekret`, co obniżało wymóg do zaledwie 1 dekretu i psuło balans stołu (75% wygranych Korony). Ujednolicono bazę w całym projekcie na sztywne **2 Dekrety**.
  3. **Usunięcie Błędu Stosów Oficjum (7 vs 8):** Ujednolicono wymóg stosów Świętego Oficjum na **7 Stosów** we wszystkich plikach zasad, kart i silnika.
  4. **Dynamiczne Nadpisywanie Wszystkich Atrybutów Kart:** Rozszerzono C-API o dynamiczną obsługę modyfikacji w locie dla parametrów: `cost`, `heresy`, `target_heresy` oraz `gold`. Silnik C++ w 100% dynamicznie uwzględnia mutacje kart optymalizatora bez konieczności rekompilacji.
  5. **Żelazna Bramka Walidacji 10k (Zero Ujemnych Delt):** Wprowadzono bezwzględny wymóg walidacji kandydata na benchmarku $10\,000$ partii na stałym ziarnie przed jakąkolwiek akceptacją patcha ($\Delta \ge +0.05\text{ pkt}$). Wyeliminowano fałszywe alarmy z mikro-prób i zagwarantowano idealną ciągłość historyczną (wynik startowy wersji $N$ jest zawsze równy wynikowi końcowemu wersji $N-1$).
- **Telemetria Bazowa:** Średnia Er `5.79`, Deadlocks `0.0%`, Pas Biedy `4.6%`, Autodafé / partię `1.50`, Oskarżenia / partię `7.80`.

### 🟢 Patch v1.0-alpha.79 (2026-08-24) — Kanon 4P: Karta `kt-07` (Archiwum Ukryte): `heresy` → `0` (Zysk 4P Δ +2.1 pkt)
- **Wynik 4P:** Kanon **`83.2`** → **`85.3 pkt`** | Global **`44.0`** | 3p **`31.0`** | 5p **`16.6`**
- **Modyfikacja (`L3_KT-07_HERESY_MINUS1`):** Karta `kt-07` (Archiwum Ukryte): `heresy` → `0`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.78, Deadlocks 0.0%, Pas Biedy 4.2%.

### 🟢 Patch v1.0-alpha.78 (2026-08-24) — Kanon 4P: Karta `gc-04` (Informator): `target_heresy` → `0` + Karta `caa-05` (Ukryty Kurier): `target_heresy` → `3` (Zysk 4P Δ +1.6 pkt)
- **Wynik 4P:** Kanon **`83.3`** → **`84.9 pkt`** | Global **`41.5`** | 3p **`29.1`** | 5p **`16.3`**
- **Modyfikacja (`L3_GC-04_TARGET_HERESY_MINUS1__L3_CAA-05_TARGET_HERESY_PLUS1`):** Karta `gc-04` (Informator): `target_heresy` → `0` + Karta `caa-05` (Ukryty Kurier): `target_heresy` → `3`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.78, Deadlocks 0.0%, Pas Biedy 4.2%.

### 🟢 Patch v1.0-alpha.77 (2026-08-24) — Kanon 4P: Karta `gc-03` (Podrzucenie Księgi): `heresy` → `2` (Zysk 4P Δ +2.8 pkt)
- **Wynik 4P:** Kanon **`79.6`** → **`82.4 pkt`** | Global **`41.7`** | 3p **`30.2`** | 5p **`13.9`**
- **Modyfikacja (`L3_GC-03_HERESY_SET2`):** Karta `gc-03` (Podrzucenie Księgi): `heresy` → `2`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.75, Deadlocks 0.0%, Pas Biedy 4.2%.

### 🟢 Patch v1.0-alpha.76 (2026-08-24) — Kanon 4P: Karta `gc-06` (Szantaż): `cost` → `3` (Zysk 4P Δ +2.1 pkt)
- **Wynik 4P:** Kanon **`80.2`** → **`82.3 pkt`** | Global **`41.4`** | 3p **`28.1`** | 5p **`17.3`**
- **Modyfikacja (`L3_GC-06_COST_PLUS1`):** Karta `gc-06` (Szantaż): `cost` → `3`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.75, Deadlocks 0.0%, Pas Biedy 4.2%.

### 🟢 Patch v1.0-alpha.75 (2026-08-24) — Kanon 4P: Karta `caa-11` (Nocna Zmiana Warty): `target_heresy` → `2` (Zysk 4P Δ +4.3 pkt)
- **Wynik 4P:** Kanon **`79.2`** → **`83.5 pkt`** | Global **`40.8`** | 3p **`28.1`** | 5p **`17.8`**
- **Modyfikacja (`L3_CAA-11_TARGET_HERESY_SET2`):** Karta `caa-11` (Nocna Zmiana Warty): `target_heresy` → `2`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.74, Deadlocks 0.0%, Pas Biedy 4.2%.

### 🟢 Patch v1.0-alpha.74 (2026-08-24) — Kanon 4P: Karta `so-12` (Straż Trybunalska): `target_heresy` → `1` (Zysk 4P Δ +2.8 pkt)
- **Wynik 4P:** Kanon **`78.3`** → **`81.1 pkt`** | Global **`41.2`** | 3p **`28.5`** | 5p **`25.8`**
- **Modyfikacja (`L3_SO-12_TARGET_HERESY_SET1`):** Karta `so-12` (Straż Trybunalska): `target_heresy` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.77, Deadlocks 0.0%, Pas Biedy 4.2%.

### 🟢 Patch v1.0-alpha.73 (2026-08-24) — Kanon 4P: Karta `so-07` (Przesłuchanie Oficjum): `gold` → `2` + Karta `caa-01` (Przejście Podziemiami): `heresy` → `1` (Zysk 4P Δ +3.1 pkt)
- **Wynik 4P:** Kanon **`78.0`** → **`81.1 pkt`** | Global **`47.5`** | 3p **`29.9`** | 5p **`40.5`**
- **Modyfikacja (`L3_SO-07_GOLD_SET2__L3_CAA-01_HERESY_SET1`):** Karta `so-07` (Przesłuchanie Oficjum): `gold` → `2` + Karta `caa-01` (Przejście Podziemiami): `heresy` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.78, Deadlocks 0.0%, Pas Biedy 4.3%.

### 🟢 Patch v1.0-alpha.72 (2026-08-24) — Kanon 4P: Karta `so-01` (Patrol Familiariuszy): `heresy` → `2` + Karta `caa-08` (Kaptur Nocy): `cost` → `2` + Karta `caa-05` (Ukryty Kurier): `gold` → `3` (Zysk 4P Δ +3.4 pkt)
- **Wynik 4P:** Kanon **`76.6`** → **`80.0 pkt`** | Global **`36.6`** | 3p **`34.5`** | 5p **`3.2`**
- **Modyfikacja (`L3_SO-01_HERESY_SET2__L3_CAA-08_COST_PLUS1__L3_CAA-05_GOLD_SET3`):** Karta `so-01` (Patrol Familiariuszy): `heresy` → `2` + Karta `caa-08` (Kaptur Nocy): `cost` → `2` + Karta `caa-05` (Ukryty Kurier): `gold` → `3`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.73, Deadlocks 0.0%, Pas Biedy 4.6%.

### 🟢 Patch v1.0-alpha.71 (2026-08-24) — Kanon 4P: Karta `so-07` (Przesłuchanie Oficjum): `cost` → `1` + Karta `caa-08` (Kaptur Nocy): `target_heresy` → `2` (Zysk 4P Δ +2.6 pkt)
- **Wynik 4P:** Kanon **`74.5`** → **`77.1 pkt`** | Global **`41.4`** | 3p **`32.0`** | 5p **`22.1`**
- **Modyfikacja (`L3_SO-07_COST_MINUS1__L3_CAA-08_TARGET_HERESY_PLUS1`):** Karta `so-07` (Przesłuchanie Oficjum): `cost` → `1` + Karta `caa-08` (Kaptur Nocy): `target_heresy` → `2`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.82, Deadlocks 0.0%, Pas Biedy 4.3%.

### 🟢 Patch v1.0-alpha.70 (2026-08-24) — Kanon 4P: Próg Obserwowanej: offset -1 (nowy: 4) + Karta `caa-01` (Przejście Podziemiami): `cost` → `1` (Zysk 4P Δ +2.3 pkt)
- **Wynik 4P:** Kanon **`73.3`** → **`75.6 pkt`** | Global **`41.2`** | 3p **`32.1`** | 5p **`20.6`**
- **Modyfikacja (`L1_OBSERVED_MINUS1__L3_CAA-01_COST_PLUS1`):** Próg Obserwowanej: offset -1 (nowy: 4) + Karta `caa-01` (Przejście Podziemiami): `cost` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.78, Deadlocks 0.0%, Pas Biedy 4.2%.

### 🟢 Patch v1.0-alpha.69 (2026-08-24) — Kanon 4P: Karta `so-04` (Publiczne Ostrzeżenie): `target_heresy` → `1` (Zysk 4P Δ +3.3 pkt)
- **Wynik 4P:** Kanon **`69.8`** → **`73.1 pkt`** | Global **`40.5`** | 3p **`30.6`** | 5p **`27.2`**
- **Modyfikacja (`L3_SO-04_TARGET_HERESY_PLUS1`):** Karta `so-04` (Publiczne Ostrzeżenie): `target_heresy` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.82, Deadlocks 0.0%, Pas Biedy 4.3%.

### 🟢 Patch v1.0-alpha.68 (2026-08-24) — Kanon 4P: Karta `so-08` (Nasłanie Inkwizytora): `gold` → `3` + Karta `caa-08` (Kaptur Nocy): `target_heresy` → `1` (Zysk 4P Δ +2.1 pkt)
- **Wynik 4P:** Kanon **`72.3`** → **`74.4 pkt`** | Global **`41.2`** | 3p **`31.9`** | 5p **`25.7`**
- **Modyfikacja (`L3_SO-08_GOLD_SET3__L3_CAA-08_TARGET_HERESY_MINUS1`):** Karta `so-08` (Nasłanie Inkwizytora): `gold` → `3` + Karta `caa-08` (Kaptur Nocy): `target_heresy` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.80, Deadlocks 0.0%, Pas Biedy 4.4%.

### 🟢 Patch v1.0-alpha.67 (2026-08-24) — Kanon 4P: Karta `kb-01` (Rozkaz Dworu): `target_heresy` → `0` (Zysk 4P Δ +1.0 pkt)
- **Wynik 4P:** Kanon **`72.5`** → **`73.5 pkt`** | Global **`32.1`** | 3p **`31.9`** | 5p **`3.2`**
- **Modyfikacja (`L3_KB-01_TARGET_HERESY_MINUS1`):** Karta `kb-01` (Rozkaz Dworu): `target_heresy` → `0`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.84, Deadlocks 0.0%, Pas Biedy 5.1%.

### 🟢 Patch v1.0-alpha.66 (2026-08-24) — Interwencja Architektoniczna: Przywrócenie Prędkości Inkwizytora = 1 (Ochrona Fizycznych Zasad Planszy)
- **Wynik 4P:** Kanon **`73.1 pkt`** (stan po Patchu v1.0-alpha.64) | Global **`36.0`** | 3p **`32.5`**
- **Modyfikacja:** Wycofano modyfikator `L4_INQUISITOR_SPEED2` (`inquisitor_speed: 2 → 1`). Dodano `INQUISITOR_SPEED` do zamrożonych niezmienników (`_FROZEN_ID_MARKERS`).
- **Efekt:** Zachowanie fizycznej integralności stołu (ruch Inkwizytora o dokładnie 1 pole). 100% testów `pytest` (w tym `test_board_graph_neighbors`) przechodzi natychmiast na zielono.

### 🟢 Patch v1.0-alpha.65 (2026-08-24) — Kanon 4P: Wariant: Prędkość Ruchu Inkwizytora = 2 (Zysk 4P Δ +1.9 pkt) [WYCOFANY W v1.0-alpha.66]
- **Wynik 4P:** Kanon **`69.6`** → **`71.5 pkt`** | Global **`26.1`** | 3p **`28.9`** | 5p **`2.2`**
- **Modyfikacja (`L4_INQUISITOR_SPEED2`):** Wariant: Prędkość Ruchu Inkwizytora = 2.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.78, Deadlocks 0.0%, Pas Biedy 5.3%.

### 🟢 Patch v1.0-alpha.64 (2026-08-24) — Kanon 4P: Karta `gc-08` (Zatrute Złoto): `heresy` → `2` (Zysk 4P Δ +4.3 pkt)
- **Wynik 4P:** Kanon **`68.8`** → **`73.1 pkt`** | Global **`36.0`** | 3p **`32.5`** | 5p **`2.8`**
- **Modyfikacja (`L3_GC-08_HERESY_PLUS1`):** Karta `gc-08` (Zatrute Złoto): `heresy` → `2`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.80, Deadlocks 0.0%, Pas Biedy 5.3%.

### 🟢 Patch v1.0-alpha.63 (2026-08-24) — Kanon 4P: Karta `caa-05` (Ukryty Kurier): `target_heresy` → `2` (Zysk 4P Δ +3.5 pkt)
- **Wynik 4P:** Kanon **`67.9`** → **`71.4 pkt`** | Global **`31.3`** | 3p **`30.0`** | 5p **`2.4`**
- **Modyfikacja (`L3_CAA-05_TARGET_HERESY_SET2`):** Karta `caa-05` (Ukryty Kurier): `target_heresy` → `2`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.81, Deadlocks 0.0%, Pas Biedy 5.3%.

### 🟢 Patch v1.0-alpha.62 (2026-08-24) — Kanon 4P: Karta `so-01` (Patrol Familiariuszy): `gold` → `2` (Zysk 4P Δ +1.5 pkt)
- **Wynik 4P:** Kanon **`66.4`** → **`67.9 pkt`** | Global **`30.6`** | 3p **`27.9`** | 5p **`2.6`**
- **Modyfikacja (`L3_SO-01_GOLD_SET2`):** Karta `so-01` (Patrol Familiariuszy): `gold` → `2`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.83, Deadlocks 0.0%, Pas Biedy 5.3%.

### 🟢 Patch v1.0-alpha.61 (2026-08-23) — Kanon 4P: Karta `so-03` (Podejrzenie): `heresy` → `3` (Zysk 4P Δ +7.4 pkt)
- **Wynik 4P:** Kanon **`59.4`** → **`66.8 pkt`** | Global **`37.9`** | 3p **`28.1`** | 5p **`20.1`**
- **Modyfikacja (`L3_SO-03_HERESY_PLUS1`):** Karta `so-03` (Podejrzenie): `heresy` → `3`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.83, Deadlocks 0.0%, Pas Biedy 5.9%.

### 🟢 Patch v1.0-alpha.60 (2026-08-23) — Kanon 4P: Gildia Cieni: Upadki offset +1 (Zysk 4P Δ +4.4 pkt)
- **Wynik 4P:** Kanon **`56.0`** → **`60.4 pkt`** | Global **`27.7`** | 3p **`21.4`** | 5p **`7.3`**
- **Modyfikacja (`L2_GC_FALLS_PLUS1`):** Gildia Cieni: Upadki offset +1.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.82, Deadlocks 0.0%, Pas Biedy 5.6%.

### 🟢 Patch v1.0-alpha.59 (2026-08-23) — Przywrócenie Zrównoważonej Gry: Stabilizacja Rytuału Salomona (kt-10: -2☣), Wymóg 2 Haków Korony i Symetria 4P
- **Cel i Uzasadnienie:** Likwidacja asymetrii matematycznej i przywrócenie pełnej grywalności wszystkich 5 frakcji w Kanonie 4P z zachowaniem czystego silnika (Zero Hacks):
  1. **Kabała z Toledo (`kt-10 Pieczęć Salomona`):** Karta sygnaturowa legalnie zmniejsza Herezję o 2 (`heresy_decrease: 2`, `heresy: 0`, `cost: 4 zł`), dając graczowi naturalne narzędzie do zniwelowania wrogich oskarżeń i stabilizacji pasma `[4, 6]`.
  2. **Korona i Borgiowie:** Wymóg zwycięstwa oparty na **2 Dekretach oraz 2 Aktywnych Hakach** (`decrees: 2`, `hooks: 2`). Kalibracja kosztu kart: `kb-08: 3 zł`, `kb-09: 2 zł` (0 zł zysku), `kb-10: 4 zł` (+1☣), co naturalnie przesuwa dominację dworu z Ery 3 do Er 5–6.
  3. **Cienie Al-Andalus:** Utrzymanie wymogu **2 Relikwii** (`relics: 2`) przy zasileniu gospodarczym (`caa-02: 3 zł`, `caa-07: 3 zł`, `caa-08: 3 zł`), co wspiera ewakuację 2. Relikwii przez Szlak Morski w Erach 5–7.
  4. **Gildia Cieni:** Stonowanie darmowego zysku złota (`gc-08: 1 zł`, `gc-09 cost: 1 zł`), co stabilizuje win-share Gildii na poziomie 25–35%.
- **Efekt Telemetrii (50 000 partii 4P):**
  * **Ery 1–2 (Sprint):** **`0.1%`** (zablokowany)
  * **Era 3 (Wczesna):** **`2.5%`** (rzadka wygrana tylko przy idealnym układzie)
  * **Era 4 (Wczesna):** **`16.8%`**
  * **Ery 5–7 (Głębokie Złote Okno):** **`68.5%`** gier (szczyt w Erze 6: `27.8%`)
  * **Pełna Równowaga Frakcji:** Wszystkie 5 frakcji osiąga zdrowy, stabilny udział w zwycięstwach (~18–33%).

### 🟢 Patch v1.0-alpha.58 (2026-08-23) — Harmonizacja Warunków Zwycięstwa (Korona 3 Dekrety, Cienie 3 Relikwie, kt-03 +2☣) i Pacing Wczesnej Gry
- **Cel i Uzasadnienie:** Likwidacja asymetrii tempa gry i wczesnych sprintów w Erach 2–4. Zrównanie dojrzałości celów Korony i Cieni do wzorcowego profilu czasowego Gildii Cieni (8 Upadków):
  1. **Korona i Borgiowie:** Podniesienie wymogu dekretów z 2 do **3 Dekrety** (`victory.korona_borgiowie.decrees: 3`), eliminujące natychmiastowe zakończenie gry w Erze 3 dwoma kartami.
  2. **Cienie Al-Andalus:** Podniesienie wymogu relikwii z 2 do **3 Relikwie** (`victory.cienie_al_andalus.relics: 3`), wymagające wykorzystania pełnego szlaku morskiego.
  3. **Kabała z Toledo (`kt-03 Zakazana Wiedza`):** Nadanie karcie klimatycznego kosztu ryzyka `heresy: 2` (zamiast 0☣), realizujące zamysł lore (*„świadome wejście w Obserwowaną”*).
  4. **Kabała z Toledo (`kt-10 Pieczęć Salomona`):** Usunięcie automatycznego dopasowania Herezji (`fallback_heresy = 5`). Kabała musi aktywnie kontrolować swoje pasmo 4–6☣.
- **Efekt Telemetrii:**
  * **Ery 1–2 (Sprint):** **`0.0%`** (całkowicie zablokowany).
  * **Era 3 (Wczesna):** **`0.6%`** (zredukowana z 6.5% — wygrana w Erze 3 jest teraz unikalnym, rzadkim wydarzeniem).
  * **Era 4 (Wczesna):** **`9.4%`** (zredukowana z 18.8%).
  * **Ery 5–7 (Złote Okno):** **`72.3%`** gier (szczyt w Erze 6: `27.9%` oraz Erze 7: `23.3%`).

### 🟢 Patch v1.0-alpha.57 (2026-08-23) — Oczyszczenie Silnika Symulacji (Engine Integrity & Zero Hacks Audit)
- **Cel i Uzasadnienie:** Całkowite wyeliminowanie ukrytych protez, skrótów i zafałszowań w silniku symulacji ([`sim/inquisitio/engine/effects/registry.py`](../sim/inquisitio/engine/effects/registry.py)), aby telemetria w 100% odzwierciedlała fizyczne karty na stole bez „sztucznego” sterowania rozkładem:
  1. **Usunięcie sztucznego ograniczenia ery dla Korony:** Usunięto kod `if card.id == "kb-04" and state.era < 4: allowed = False`. Karta `kb-04 Faworyt Dworu` działa teraz w 100% zgodnie z danymi YAML.
  2. **Usunięcie ukrytego mnożnika podrzucenia dla Gildii:** Usunięto kod `if state.layer == "A" and card.id == "gc-03": amt = max(amt, 2)`. Efekt `target_heresy` czyta dokładnie wartość z karty.
  3. **Kabała (`kt-10 Pieczęć Salomona`):** Wprowadzono bezwzględne sprawdzanie warunku `fragments_eq_3` (`_card_condition_satisfied`) przed aktywacją pieczęci — zlikwidowano błąd pozwalający na nielegalne zaliczanie sygnatury z wyprzedzeniem.
  4. **Cienie (`caa-10 Echo Alhambry`):** Zredukowano limit ewakuacji przez `caa-10` do maksymalnie **1 Relikwii na zagranie** (zamiast natychmiastowej podwójnej ewakuacji kończącej grę jednym ruchem) oraz poprawnie ustawiono flagę `shadow_exit`.
  5. **Korona (`kb-05 List Żelazny`):** Usunięto historyczny relikt naliczający punkt Dekretu przy zagraniu karty w Warstwie A (dekrety wynikają wyłącznie z kart dekretowych `kb-09` i `kb-10`).
- **Efekt Telemetrii:** Prawdziwy, niezafałszowany rozkład tempa gry:
  * **Ery 1–2 (Sprint):** **`0.2%`** (zablokowany sprint anomalii).
  * **Era 3 (Wczesna):** **`6.5%`** (bardzo trudna).
  * **Era 4 (Wczesna):** **`18.8%`** (trudna faza dojrzewania stołu).
  * **Ery 5–7 (Złote Okno):** **`68.1%`** (właściwy środek ciężkości gry ze szczytem w Erze 5–6).
  * **Odsłonięcie prawdziwego balansu kart:** Zidentyfikowano realne odchylenia kart: Korona (33.1%) i Gildia (29.7%) są zbyt silne po zdjęciu blokad, natomiast Kabała (19.8%) i Cienie (15.3%) wymagają właściwego dostrojenia w kartach `game_config.yaml`.

### 🟢 Patch v1.0-alpha.56 (2026-08-23) — Wzmocnienie Finiszerów Gildii (gc-10: 3 zł, gc-08: 2 zł) i Tonowanie Skarbca Oficjum (so-02: 2 zł)
- **Cel i Uzasadnienie:** Likwidacja asymetrii win-share w Kanonie 4P (podciągnięcie Gildii Cieni z 21.1% i stonowanie dominacji Oficjum z 30.1%):
  1. **Gildia Cieni:** Karta sygnaturowa `gc-10 Upadek Domu` kosztuje **3 zł** (z 4 na 3 zł), a `gc-08 Zatrute Złoto` generuje **2 zł** (z 1 na 2 zł), co ożywia finiszer Gildii i pozwala domykać Upadki w Erze 6–7.
  2. **Święte Oficjum:** Karta `so-02 Skarbiec Trybunału` generuje **2 zł** (z 3 na 2 zł), co zapobiega nadmiernej kumulacji kapitału na natychmiastowe oskarżenia i procesy.
  3. **Heurystyka AI:** Zaktualizowano priorytety AI dla `gc-10` oraz mobilności Cieni `caa-01` i płynności `caa-02`.
- **Efekt Telemetrii:** Win share Gildii Cieni wzrósł z 21.1% do **`23.9%`** (zbliżając się do 25.0% ideału), win share Oficjum ustabilizował się na poziomie **`25.7%`**, udział Złotego Okna (Ery 5–7) wzrósł do **`67.8%`**, a szczyt partii wypada pewnie w **Erze 6 (`28.7%`)**.

### 🟢 Patch v1.0-alpha.55 (2026-08-23) — Harmonizacja Stosów Oficjum (7 Stosów) i Balans Finiszera Cieni (caa-10: 3 zł)
- **Cel i Uzasadnienie:** Usunięcie degradacji witalności zidentyfikowanych w audycie 4P:
  1. **Święte Oficjum:** Przywrócenie progu `victory.swiete_oficjum.stacks: 7` (z 8 na 7), co ożywia ścieżkę Autodafé w setupach `4p-no-cienie` oraz `4p-no-korona`, przywracając status **🟢 Pełna Witalność** (0 kar).
  2. **Cienie Al-Andalus:** Zwiększenie kosztu karty sygnaturowej `caa-10 Echo Alhambry` z 2 zł do **3 zł**, co wymaga przygotowania ekonomicznego i ogranicza wczesne podwójne ewakuacje w Erze 1–2.
- **Efekt Telemetrii:** W setupie `4p-no-cienie` całkowicie zlikwidowano ostrzeżenie o martwej ścieżce stosów. Udział Złotego Okna (Ery 5–7) wynosi **`66.6%`**, a szczyt rozkładu stabilnie przypada na Erę 6 (`27.9%`).

### 🟢 Patch v1.0-alpha.54 (2026-08-23) — Kanon 4P: Karta `so-03` (Podejrzenie): `gold` → `1` (Zysk 4P Δ +0.1 pkt)
- **Wynik 4P:** Kanon **`75.5`** → **`75.6 pkt`** | Global **`18.5`** | 3p **`13.5`** | 5p **`2.7`**
- **Modyfikacja (`L3_SO-03_GOLD_SET1`):** Karta `so-03` (Podejrzenie): `gold` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.62, Deadlocks 0.0%, Pas Biedy 5.0%.

### 🟢 Patch v1.0-alpha.53 (2026-08-23) — Rzeczywiste Przesunięcie Krzywej Gry do Złotego Okna (Ery 5–7): Cykl Autodafé (4 Ery), Próg Stosów (8 Stosów) i Koszt Pieczęci Salomona (5 zł)
- **Cel i Uzasadnienie:** Rzeczywiste i trwałe przesunięcie rozkładu końca partii do standardu ADR-0004 (Ery 5–7 jako serce gry, z redukcją Er 1–4 do < 23% i wzrostem Er 6–7).
- **Modyfikacje SSOT:**
  1. **Cykl Autodafé:** `system.autodafe_cooldown: 4` (z 3 na 4 Ery) — opóźnia pierwszą falę procesów do Ery 4, synchronizując rozstrzygnięcia z dojrzałą fazą gry.
  2. **Święte Oficjum:** `victory.swiete_oficjum.stacks: 8` (z 7 na 8) — synchronizuje wygraną Inkwizycji z 2. cyklem Autodafé.
  3. **Kabała Toledo:** `kt-10 Pieczęć Salomona: cost 5` (z 4 na 5 zł) — wymaga pełnego przygotowania ekonomicznego przed rzuceniem finiszera.
  4. **Gildia Cieni:** `victory.gildia_cieni.falls: default: 7, no_oficjum: 8` — stabilizuje dynamikę upadków majątkowych przy braku procesów Inkwizycji.
- **Efekt Telemetrii:** Gry wczesne (Ery 1–4) spadły z 31.5% do **`22.7%`**, udział Złotego Okna (Ery 5–7) wynosi **`66.4%`**, udział Ery 7 wzrósł niemal dwukrotnie do **`13.9%`**, a szczyt partii wypada pewnie w **Erze 6 (`28.5%`)**.

### 🟢 Patch v1.0-alpha.52 (2026-08-23) — Złoto Startowe 4 zł i Pieczęć Salomona 4 zł
- **Cel i Uzasadnienie:** Przesunięcie szczytu rozkładu partii z Ery 5 na Erę 6 oraz synchronizacja krzywej gry ze standardem ADR-0004 poprzez kalibrację zasobów otwarcia.
- **Modyfikacje SSOT:**
  1. **Złoto Startowe:** `system.start_gold: 4` (z 5 na 4 zł) — eliminuje natychmiastowe zagrania drogich kart ofensywnych w Turze 1, wymuszając 1 turę pozycjonowania i budowania przewagi ekonomicznej.
  2. **Pieczęć Salomona:** `kt-10.cost: 4` (z 3 na 4 zł) — zapobiega wczesnym sprintom Kabały w Erze 3.
- **Efekt Telemetrii:** Szczyt rozkładu partii przesuwa się na **Erę 6 (`28.8%`)**, Złote Okno Rozgrywki (Ery 5–7) osiąga **65.0%**, a gry w Erze 1–2 spadają do **< 0.9%**.

### 🟢 Patch v1.0-alpha.51 (2026-08-23) — Korekta Logistyki Portowej Cieni (caa-10) i Pacing Złotego Okna Rozgrywki (Ery 5–7)
- **Cel i Uzasadnienie:** Usunięcie błędu logicznego w karcie `caa-10 Echo Alhambry` (wymóg obecności w Porcie: Rynek/Gildia dla cichej ewakuacji morskiej poza miasto) w celu definitywnej eliminacji nienaturalnych zwycięstw w Erze 1–2 oraz synchronizacja szczytu rozgrywki w Złotym Oknie (Ery 5–7).
- **Modyfikacje Silnika i Kart:**
  1. **Logistyka Cieni:** `caa-10` wymaga lokacji portowej (`rynek`/`gildia`) dla cichej ewakuacji morskiej bez Inkwizytora (lub otwartego Szlaku Morskiego).
  2. **Ekonomia i Płynność:** Utrzymano `so_stacks: 7`, `kt-02: 3 zł`, `caa-05: 1 zł`, `caa-08: 2 zł`, `kb-08: 3 zł`.
- **Efekt Telemetrii:** Gry w Erze 1 zredukowane do 0.0%, Gry w Erze 2 zredukowane do < 1.0%, Złote Okno Rozgrywki (Ery 5–7) obejmuje ponad 63% wszystkich partii.

### 🟢 Patch v1.0-alpha.50 (2026-08-23) — Harmonizacja Kanonu 4P: Próg Stosów Oficjum (7 Stosów), Płynność Kabały i Logistyka Cieni
- **Cel i Uzasadnienie:** Ręczna harmonizacja 5 setupów Kanonu 4P z zachowaniem 3 agentów na gracza:
  1. **Święte Oficjum:** Podniesienie progu stosów z 6 do **7 Stosów** (`victory.swiete_oficjum.stacks: 7`), co zapobiega zdominowaniu stołu przez łatwe wyroki przy 3 agentach.
  2. **Kabała Toledo:** Karta `kt-02 Transmutacja Złota` generuje **3 zł** (z 2 na 3 zł), zapewniając budżet na opłacenie Pieczęci Salomona w late-game.
  3. **Cienie Al-Andalus:** Karta `caa-05 Ukryty Kurier` kosztuje **1 zł** (z 2 na 1 zł), a `caa-08 Kaptur Nocy` generuje **2 zł** (z 1 na 2 zł), co wspiera logistykę portową.
  4. **Korona Borgiowie:** Karta `kb-08 Przekupstwo Sędziego` kosztuje **3 zł** (z 2 na 3 zł), co tonuje dominację dekretów w setupach bez Oficjum.

### 🟢 Patch v1.0-alpha.49 (2026-08-23) — Przywrócenie Kanonicznej Liczby Agentów (3 Agenci) i Twarda Blokada Niezmienników Fizycznych
- **Cel i Uzasadnienie:** Bezwzględne przywrócenie kanonicznej liczby agentów `system.agents_per_player: 3` (revert samowolnej próby redukcji do 2 z v47). Liczba figurek (3 pionki agentów na gracza) jest nienaruszalnym filarem fizycznego wydania gry.
- **Modyfikacja SSOT:** `system.agents_per_player: 3`.
- **Zabezpieczenie Audytora (FROZEN):** Wprowadzenie twardej blokady `_FROZEN_ID_MARKERS` na parametr `agents_per_player` i `agents_offset`, uniemożliwiającej automatycznym skryptom jakąkolwiek modyfikację liczby agentów.

### 🟢 Patch v1.0-alpha.48 (2026-08-23) — Kanon 4P: Karta `caa-06` (Ucieczka z Lochów): `target_heresy` → `2` (Zysk 4P Δ +10.9 pkt)
- **Wynik 4P:** Kanon **`61.1`** → **`72.0 pkt`** | Global **`22.5`** | 3p **`16.2`** | 5p **`4.9`**
- **Modyfikacja (`L3_CAA-06_TARGET_HERESY_SET2`):** Karta `caa-06` (Ucieczka z Lochów): `target_heresy` → `2`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.40, Deadlocks 0.0%, Pas Biedy 3.9%.

### 🟢 Patch v1.0-alpha.47 (2026-08-23) — Kanon 4P: Liczba agentów: offset -1 (nowa: 2) (Zysk 4P Δ +8.1 pkt)
- **Wynik 4P:** Kanon **`51.6`** → **`59.7 pkt`** | Global **`18.7`** | 3p **`13.5`** | 5p **`5.7`**
- **Modyfikacja (`L1_AGENTS_MINUS1`):** Liczba agentów: offset -1 (nowa: 2).
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.43, Deadlocks 0.0%, Pas Biedy 4.0%.

### 🟢 Patch v1.0-alpha.46 (2026-08-23) — Równowaga Organiczna Kanonu 4P: Rytuał Pieczęci Salomona, Logistyka Ucieczki Relikwii i Kalibracja Gildii Cieni
- **Wynik 4P:** Kanon 4P Balance **`63.0`** – **`72.0 pkt`** | Stabilizacja Er 5–7 (58% partii w Złotym Oknie)
- **Modyfikacje Mechanik i SSOT (`ADR-0001`, `ADR-0003`, `ADR-0004`):**
  - **Kabała Toledo:** Zagranie `kt-10 Pieczęć Salomona` przy posiadaniu 3 Fragmentów Kodeksu aktywnie stabilizuje Herezję w Paśmie `[4, 6]` i domyka rytuał zwycięstwa.
  - **Cienie Al-Andalus:** Urealnienie logistyki ucieczki — karta `caa-05 Ukryty Kurier` przemieszcza relikwie w stronę bezpiecznych traktów, a ewakuację poza planszę przeprowadza w warunkach cichej operacji (`inquisitor != location`). Karta sygnaturowa `caa-10` ewakuuje 1 relikwię.
  - **Gildia Cieni:** Podniesienie progu upadków w 4P z 6 do **7 Upadków** (`gildia_cieni.falls: 7`), synchronizując tempo przewrotu ze zbalansowanym oknem Er 5–7.
  - **Gwarancja Systemowa:** Zachowanie `autodafe_cooldown: 3` (lokalne oczyszczenie w lokacji Inkwizytora) oraz tożsamości ekonomicznej `so-02 Skarbiec Trybunału` (3 zł).

### 🟢 Patch v1.0-alpha.45 (2026-08-23) — Wdrożenie Ścieżki A: Naturalna Kalibracja Finisherów i Złote Okno Er 5–7
- **Wynik 4P:** Zrównoważenie tempa rozgrywki, eliminacja nadpłynności wczesnych finisherów
- **Modyfikacje SSOT (`ADR-0001`, `ADR-0003`, `ADR-0004`):**
  - **Cienie Al-Andalus:** Podniesienie kosztu karty sygnaturowej `caa-10 Echo Alhambry` (`cost` 1 → 2 zł), co zapobiega darmowej podwójnej ewakuacji relikwii w otwarciu.
  - **Kabała Toledo:** Wymóg aktywnego zagrania `kt-10 Pieczęć Salomona` (`cost: 3 zł`, 3 fragmenty, Herezja `[4, 6]`) bez sztucznych blokad er.
  - **Klasyfikacja Tempa:** Dostosowanie modułu `era_analytics.py` do pełnej zgodności z ADR-0004 (Ery 5–7 jako Złote Okno Rozgrywki).

### 🟢 Patch v1.0-alpha.44 (2026-08-23) — Wdrożenie ADR-0001/0003: Organiczna Progresja Er, Złote Okno Er 5–7 i Pieczęć Salomona jako Aktywny Finisher
- **Wynik 4P:** Kanon **`76.2`** → **`78.5 pkt`** | Zrównoważenie Er 5–7
- **Modyfikacje SSOT (`ADR-0001`, `ADR-0003`, `ADR-0004`):**
  - **Zwycięstwo Kabały Toledo:** Zastąpienie sztucznej bramki `era: 6` aktywnym wymogiem zgromadzenia 3 fragmentów i zagrania karty `kt-10 Pieczęć Salomona` (koszt 3 zł, pasmo `[4, 6]`).
  - **Święte Oficjum:** Dofinansowanie skarbca `so-02` (dochód `gold` 2 → 3 zł) na prowadzenie procesów inkwizycyjnych.
  - **Cienie Al-Andalus:** Urealnienie logistyki ucieczki `caa-05 Ukryty Kurier` (koszt `cost` 0 → 2 zł) zapobiegające natychmiastowej ewakuacji w 1. turze i wspierające late-game szlaku morskiego.
  - **Eliminacja Sztucznych Blokad:** Usunięcie twardych bramek `state.era >= X` z silnika `win.py` per ADR-0001.
- **Efekt:** Likwidacja monopolu Kabały w Erze 6 i zapaści Cieni. Wyrównana rywalizacja 4 frakcji w dojrzałym oknie Er 5–7.

### 🟢 Patch v1.0-alpha.43 (2026-08-23) — Kanon 4P: Karta `gc-01` (Przekupiony Strażnik): `cost` → `1` + Karta `caa-08` (Kaptur Nocy): `gold` → `1` + Karta `caa-01` (Przejście Podziemiami): `target_heresy` → `1` (Zysk 4P Δ +1.8 pkt)
- **Wynik 4P:** Kanon **`74.4`** → **`76.2 pkt`** | Global **`28.1`** | 3p **`22.6`** | 5p **`7.6`**
- **Modyfikacja (`L3_GC-01_COST_MINUS1__L3_CAA-08_GOLD_PLUS1__L3_CAA-01_TARGET_HERESY_PLUS1`):** Karta `gc-01` (Przekupiony Strażnik): `cost` → `1` + Karta `caa-08` (Kaptur Nocy): `gold` → `1` + Karta `caa-01` (Przejście Podziemiami): `target_heresy` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 4.78, Deadlocks 0.0%, Pas Biedy 3.5%.

### 🟢 Patch v1.0-alpha.42 (2026-08-23) — Kanon 4P: Karta `caa-11` (Nocna Zmiana Warty): `gold` → `3` + Karta `gc-09` (Lista Dłużników): `gold` → `0` (Zysk 4P Δ +3.4 pkt)
- **Wynik 4P:** Kanon **`72.1`** → **`75.5 pkt`** | Global **`39.9`** | 3p **`25.9`** | 5p **`21.6`**
- **Modyfikacja (`L3_CAA-11_GOLD_SET3__L3_GC-09_GOLD_MINUS1`):** Karta `caa-11` (Nocna Zmiana Warty): `gold` → `3` + Karta `gc-09` (Lista Dłużników): `gold` → `0`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 4.79, Deadlocks 0.0%, Pas Biedy 3.5%.

### 🟢 Patch v1.0-alpha.41 (2026-08-23) — Kanon 4P: Karta `kt-11` (Medytacja Sefirot): `target_heresy` → `1` (Zysk 4P Δ +1.3 pkt)
- **Wynik 4P:** Kanon **`73.7`** → **`75.0 pkt`** | Global **`39.3`** | 3p **`22.8`** | 5p **`22.6`**
- **Modyfikacja (`L3_KT-11_TARGET_HERESY_PLUS1`):** Karta `kt-11` (Medytacja Sefirot): `target_heresy` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 4.83, Deadlocks 0.0%, Pas Biedy 3.5%.

### 🟢 Patch v1.0-alpha.40 (2026-08-23) — Kanon 4P: Karta `caa-04` (Fałszywy Trop): `gold` → `3` + Karta `gc-02` (Czarny Rynek): `heresy` → `0` (Zysk 4P Δ +2.2 pkt)
- **Wynik 4P:** Kanon **`69.1`** → **`71.3 pkt`** | Global **`39.9`** | 3p **`23.6`** | 5p **`22.4`**
- **Modyfikacja (`L3_CAA-04_GOLD_SET3__L3_GC-02_HERESY_MINUS1`):** Karta `caa-04` (Fałszywy Trop): `gold` → `3` + Karta `gc-02` (Czarny Rynek): `heresy` → `0`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 4.83, Deadlocks 0.0%, Pas Biedy 3.5%.

### 🟢 Patch v1.0-alpha.39 (2026-08-23) — Kanon 4P: Karta `gc-09` (Lista Dłużników): `heresy` → `0` (Zysk 4P Δ +3.7 pkt)
- **Wynik 4P:** Kanon **`65.2`** → **`68.9 pkt`** | Global **`38.8`** | 3p **`27.4`** | 5p **`19.0`**
- **Modyfikacja (`L3_GC-09_HERESY_MINUS1`):** Karta `gc-09` (Lista Dłużników): `heresy` → `0`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 4.78, Deadlocks 0.0%, Pas Biedy 3.4%.

### 🟢 Patch v1.0-alpha.38 (2026-08-23) — Kanon 4P: Karta `gc-04` (Informator): `heresy` → `0` (Zysk 4P Δ +4.0 pkt)
- **Wynik 4P:** Kanon **`62.4`** → **`66.4 pkt`** | Global **`36.7`** | 3p **`25.5`** | 5p **`17.4`**
- **Modyfikacja (`L3_GC-04_HERESY_MINUS1`):** Karta `gc-04` (Informator): `heresy` → `0`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 4.78, Deadlocks 0.0%, Pas Biedy 3.4%.

### 🟢 Patch v1.0-alpha.37 (2026-08-23) — Kanon 4P: Karta `caa-07` (Szantaż Bractwa): `gold` → `3` (Zysk 4P Δ +3.7 pkt)
- **Wynik 4P:** Kanon **`62.0`** → **`65.7 pkt`** | Global **`33.9`** | 3p **`24.7`** | 5p **`13.6`**
- **Modyfikacja (`L3_CAA-07_GOLD_SET3`):** Karta `caa-07` (Szantaż Bractwa): `gold` → `3`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 4.77, Deadlocks 0.0%, Pas Biedy 3.4%.

### 🟢 Patch v1.0-alpha.36 (2026-08-23) — Kanon 4P: Karta `kb-04` (Faworyt Dworu): `heresy` → `0` (Zysk 4P Δ +3.7 pkt)
- **Wynik 4P:** Kanon **`59.5`** → **`63.2 pkt`** | Global **`35.0`** | 3p **`27.2`** | 5p **`16.9`**
- **Modyfikacja (`L3_KB-04_HERESY_MINUS1`):** Karta `kb-04` (Faworyt Dworu): `heresy` → `0`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 4.74, Deadlocks 0.0%, Pas Biedy 3.3%.

### 🟢 Patch v1.0-alpha.35 (2026-08-23) — Kanon 4P: Usunięcie Dublowania Akcji Gospodarczej na `gc-02` i `kt-02` (Zysk 4P: 59.2 pkt)
- **Modyfikacja Kart Frakcyjnych L3 (`game_config.yaml`):**
  - `gc-02` (*Czarny Rynek*): koszt obniżony z **`1` $\to$ `0` zł** (`gold: 2`, `heresy: 1`). Zapewnia natychmiastowy zysk netto **`+2 zł`** bez wpisowego za cenę podejrzeń (+1 Herezja za brudny handel).
  - `kt-02` (*Transmutacja Złota*): koszt obniżony z **`1` $\to$ `0` zł** (`gold: 2`, `heresy: 0`). Alchemiczna transmutacja tworzy **`+2 zł`** netto bez dublowania zwykłego pasu gospodarczego.
- **Efekt:** Pełna unikalność ekonomiczna wszystkich 5 frakcji — każda karta ekonomiczna daje wyraźną przewagę strategiczną i tożsamość klimatyczną względem bazowej Akcji Gospodarczej.

### 🟢 Patch v1.0-alpha.34 (2026-08-23) — Kanon 4P: Cięcie Inflacji Złota na Kartach-Bankomatach (Zysk 4P Δ +2.1 pkt, Śr. Złoto End 5.92 zł → 4.85 zł)
- **Wynik 4P:** Kanon **`57.3`** → **`59.4 pkt`** | Podłoga najsłabszego setupu (`4p-no-cienie`) **`22.5`** → **`34.9 pkt`** (Δ +12.4 pkt).
- **Modyfikacja Kart Frakcyjnych L3 (`game_config.yaml`):**
  - `so-02` (*Skarbiec Trybunału*): zysk złota `gold` obniżony z **`3` $\to$ `2` zł**.
  - `caa-02` (*Złoto z Kryjówki*): zysk złota `gold` obniżony z **`3` $\to$ `2` zł**.
  - `gc-02` (*Czarny Rynek*): zysk złota `gold` obniżony z **`4` $\to$ `2` zł**.
- **Efekt i Telemetria:**
  - Średnia ilość złota w sakiewkach na koniec gry spadła z **`5.92 zł`** do **`4.85 zł`** (spadek o ponad 1 monetę na gracza).
  - Wskaźnik wymuszonych pasów biedy pozostał na optymalnym poziomie **`3.6%`** (płynny obieg bez zatorów).
  - Wzrost równości szans w setupach pobocznych (`4p-no-kabala` do 68.3 pkt, `4p-no-korona` do 56.7 pkt).

### 🟢 Patch v1.0-alpha.32 (2026-08-22) — Kanon 4P: Karta `kb-09` (Dekret Królewski): `heresy` → `0` (Zysk 4P Δ +8.1 pkt)
- **Wynik 4P:** Kanon **`62.2`** → **`70.3 pkt`** | Global **`24.7`** | 3p **`19.9`** | 5p **`23.5`**
- **Modyfikacja (`L3_KB-09_HERESY_MINUS1`):** Karta `kb-09` (Dekret Królewski): `heresy` → `0`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 4.79, Deadlocks 0.0%, Pas Biedy 3.4%.

### 🟢 Patch v1.0-alpha.31 (2026-08-22) — Kanon 4P: Święte Oficjum: Skazania offset +1 (Zysk 4P Δ +16.8 pkt)
- **Wynik 4P:** Kanon **`48.9`** → **`65.7 pkt`** | Global **`23.4`** | 3p **`16.5`** | 5p **`20.5`**
- **Modyfikacja (`L2_SO_CONDEMNS_PLUS1`):** Święte Oficjum: Skazania offset +1.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 4.82, Deadlocks 0.0%, Pas Biedy 3.4%.

### 🟢 Patch v1.0-alpha.30 (2026-08-22) — Zamrożenie Akcji Gospodarczej na 1 zł (Reset `intrigue_gold: 1` & Blokada Audytorów)
- **Modyfikacja Systemowa SSOT (`game_config.yaml`):** `intrigue_gold` zresetowane z `2` do **`1`** (przywrócenie bazowej reguły Księgi Zasad: Akcja Gospodarcza = +1 zł, na Rynku z Jarmarkiem = +2 zł).
- **Blokada w Audytorach (`audytor_4p.py`):** Parametr `intrigue_gold` został na stałe dodany do `_FROZEN_ID_MARKERS` i `_FROZEN_PARAM_KEYS`. Żaden automatyczny optymalizator nie może modyfikować złota z akcji gospodarczej.
- **Uzasadnienie Projektowe:** Podbijanie złota za pas (Opcja B Fazy I) było sztuczną inflacyjną protezą makro, która zachęcała boty i graczy do bierności zamiast zagrywania kart frakcyjnych. Strojenie balansu finansowego i tempa odbywa się w 100% na kartach frakcyjnych (poziom L3).

### 🟢 Patch v1.0-alpha.29 (2026-08-22) — Kanon 4P Makro: Akcja Gospodarcza: offset +1 (nowy: 2) (Zysk 4P Δ +5.6 pkt)
- **Wynik 4P (win share):** **`54.5 pkt`** (baza `48.9`) | blended `48.9` → `54.5` | Global **`27.6`** | 3p **`20.2`** | 5p **`7.3`**
- **Modyfikacja (`L1_INTRIGUE_GOLD_PLUS1`):** Akcja Gospodarcza: offset +1 (nowy: 2).
- **Efekt:** Makro L1/L2/L4. Telemetria: Średnia Er 4.67, Deadlocks 0.0%, Pas Biedy 2.8%. Witalność `0.000` → `0.000`.

### 🟢 Patch v1.0-alpha.28 (2026-08-22) — Kanon 4P Makro: Zastosowano regułę L1_INTRIGUE_GOLD_DOUBLE (Zysk 4P Δ +5.6 pkt)
- **Wynik 4P (win share):** **`54.5 pkt`** (baza `48.9`) | blended `48.9` → `54.5` | Global **`27.6`** | 3p **`20.2`** | 5p **`7.3`**
- **Modyfikacja (`L1_INTRIGUE_GOLD_DOUBLE`):** Zastosowano regułę L1_INTRIGUE_GOLD_DOUBLE.
- **Efekt:** Makro L1/L2/L4. Telemetria: Średnia Er 4.67, Deadlocks 0.0%, Pas Biedy 2.8%. Witalność `0.000` → `0.000`.

### 🟢 Patch v1.0-alpha.27 (2026-08-22) — Kanon 4P: Gildia Cieni: Upadki offset -1 (Zysk 4P Δ +13.4 pkt)
- **Wynik 4P:** Kanon **`35.3`** → **`48.7 pkt`** | Global **`24.4`** | 3p **`16.9`** | 5p **`6.1`**
- **Modyfikacja (`L2_GC_FALLS_MINUS1`):** Gildia Cieni: Upadki offset -1.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 4.68, Deadlocks 0.0%, Pas Biedy 3.4%.

### 🟢 Patch v1.0-alpha.26 (2026-08-22) — Kanon 4P: Gildia Cieni: Upadki offset -1 (Zysk 4P Δ +7.9 pkt)
- **Wynik 4P:** Kanon **`27.6`** → **`35.5 pkt`** | Global **`20.9`** | 3p **`25.8`** | 5p **`2.9`**
- **Modyfikacja (`L2_GC_FALLS_MINUS1`):** Gildia Cieni: Upadki offset -1.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 4.78, Deadlocks 0.0%, Pas Biedy 3.4%.

### 🌟 Patch v1.0-alpha.25 (2026-08-22) — Przełom: Pełne AI 60 Kart, Telemetria Play-Rate & Patch `KB-09` (Zysk 4P Δ +15.3 pkt)
- **Wynik 4P:** Kanon **`11.9`** → **`27.2 pkt`** | Global **`17.6`** | 3p **`24.2`** | 5p **`1.9`** | Podłoga najsłabszego setupu `4.2` → `6.6 pkt` (na setupie flagowym `4p-core` skok do **`66.3 pkt`**)
- **Modyfikacja Silnika & AI (`PoliticsAgent`):**
  - **Usunięcie sztucznej barier pasywności:** Obniżono zawyżony próg Akcji Gospodarczej ($2.6 \to 1.2$), likwidując zjawisko zrzucania 40% talii do kosza (`Play-Rate: 0.00`) i zapychana ręki.
  - **Wdrożenie pełnych heurystyk taktycznych dla 60 kart:** Każda karta ma teraz aktywną wycenę (pozycjonowanie agentów, budowanie haków, presja sądu, ucieczki, odzyskiwanie złota).
  - **Zliczanie kart reakcji:** Wpięto liczniki zagrań dla `so-05` (*Wezwanie do Trybunału*) oraz `gc-05` (*Fałszywy Świadek* w sądzie).
- **Modyfikacja Taksonomii (`impact_taxonomy.py`):**
  - Trójwymiarowa matryca ablacji: $\Delta\text{Share} \times \Delta\text{4P} \times \text{Play-Rate}$.
  - Wprowadzono kategorię `TEMPO_FILLER (Rozcieńczalnik Talii)` eliminując fałszywe alarmy „Autopodatków”.
  - Zablokowano fałszywe klasyfikowanie niezagrywanych kart jako „Zbalansowane Narzędzia”.
- **Modyfikacja Kart SSOT (`game_config.yaml`):**
  - Karta `kb-09` (Dekret Królewski): `gold` → `3` (wzmocnienie tempa ekonomicznego Korony, skok win share w Kanonie z 1.8% do 17.9%).
- **Efekt i Rozkład:** Ujawnienie prawdziwego balansu w pełni grającego stołu AI. Telemetria: Średnia Er 4.81, Deadlocks 0.0%, Pas Biedy 3.5%, 214/214 testów zaliczonych.

### 🟢 Patch v1.0-alpha.24 (2026-08-22) — Kanon 4P Makro: Startowe złoto: offset +1 (Zysk 4P Δ +1.9 pkt)
- **Wynik 4P (win share):** **`84.0 pkt`** (baza `82.1`) | blended `82.1` → `84.0` | Global **`54.4`** | 3p **`31.9`** | 5p **`45.6`**
- **Modyfikacja (`L1_START_GOLD_PLUS1`):** Startowe złoto: offset +1.
- **Efekt:** Makro L1/L2/L4. Telemetria: Średnia Er 5.98, Deadlocks 0.1%, Pas Biedy 1.0%. Witalność `0.000` → `0.000`.

### 🌟 Patch v1.0-alpha.23 (2026-08-22) — Przełom: Dynamic Threat Assessment AI & Skok Balansu Kanonu 4P (80.24 pkt)
- **Wynik 4P:** Kanon **`74.9 pkt`** → **`80.24 pkt`** | Podłoga najsłabszego setupu **`61.5 pkt`** → **`74.70 pkt`** (Próba: 10 000 gier/setup | 50 000 gier łącznie)
- **Modyfikacja Silnika & AI (`PoliticsAgent`):**
  - **Diagnoza bariery lokalnego optimum:** Poprzednie wersje audytora (v1.0-alpha.1 do alpha.22) operowały wyłącznie na mikro-mutacjach kart (np. `gold ±1`, `cost ±1`), co dawało zyski rzędu Δ +0.1–0.5 pkt, lecz nie było w stanie rozwiązać problemu strukturalnego załamania `4p-core` (~61 pkt) wynikającego z braku reakcji stołu na liderów.
  - **Wdrożenie Dynamic Threat Assessment (Teoria Gier):** Wprowadzono dynamiczną kalkulację zagrożenia punktu meczowego (`threat` 0.0–1.0) dla wszystkich frakcji (1 relikwia u Cieni, 2 haki u Korony, 2 fragmenty u Kabały, 6+ upadków u Gildii, 2 skazania u Oficjum).
  - **Obrona przed Autodafé (`observed_threshold = 5`):** Boty przestały beztrosko wchodzić w strefę 5 herezji, gdy zbliża się Autodafé (eliminacja darmowych wygranych Oficjum).
  - **Kontekstowa obrona stołu:** Pod obecność Inkwizycji stół używa herezji do eliminowania liderów; pod nieobecność Inkwizycji stół natychmiast przestawia się na fizyczne aresztowania i przesłuchania.
  - **Eliminacja Overfittingu:** 100% ogólnych reguł – zero hardkodowanych nazw setupów czy warunków `if Faction not in game`.
- **Modyfikacje Kart SSOT (`game_config.yaml`):**
  - Karta `caa-12` (Skrytka w Murach): `gold` → `4` (płynność finansowa Cieni w portach).
  - Karta `so-02` (Donos): `target_heresy` → `1` (wygładzenie agresji donosów).
- **Efekt i Rozkład Wygranych:** `4p-no-kabala` **87.3 pkt**, `4p-core` **80.2 pkt**, `4p-no-cienie` **79.5 pkt**, `4p-no-korona` **79.5 pkt**, `4p-no-oficjum` **74.7 pkt**. Telemetria: Średnia Er 6.04, Deadlocks 0.1%, Pas Biedy 1.1%, 214/214 testów zaliczonych.

### 🟢 Patch v1.0-alpha.22 (2026-08-21) — Kanon 4P: Karta `so-10` (Oczyść Miasto): `heresy` → `1` (Zysk 4P Δ +0.2 pkt)
- **Wynik 4P:** Kanon **`80.1`** → **`80.3 pkt`** | Global **`45.7`** | 3p **`24.3`** | 5p **`29.2`**
- **Modyfikacja (`L3_SO-10_HERESY_MINUS1`):** Karta `so-10` (Oczyść Miasto): `heresy` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.24, Deadlocks 0.3%, Pas Biedy 1.5%.

### 🟢 Patch v1.0-alpha.21 (2026-08-21) — Kanon 4P: Karta `so-09` (Świadek Koronny): `cost` → `1` (Zysk 4P Δ +0.1 pkt)
- **Wynik 4P:** Kanon **`80.0`** → **`80.1 pkt`** | Global **`46.1`** | 3p **`24.4`** | 5p **`30.5`**
- **Modyfikacja (`L3_SO-09_COST_MINUS1`):** Karta `so-09` (Świadek Koronny): `cost` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.23, Deadlocks 0.3%, Pas Biedy 1.5%.

### 🟢 Patch v1.0-alpha.20 (2026-08-21) — Kanon 4P: Karta `so-06` (Areszt Trybunalski): `target_heresy` → `1` + Karta `gc-11` (Fałszywe Świadectwo Cechu): `heresy` → `2` (Zysk 4P Δ +0.1 pkt)
- **Wynik 4P:** Kanon **`79.9`** → **`80.0 pkt`** | Global **`45.9`** | 3p **`24.4`** | 5p **`30.2`**
- **Modyfikacja (`L3_SO-06_TARGET_HERESY_PLUS1__L3_GC-11_HERESY_PLUS1`):** Karta `so-06` (Areszt Trybunalski): `target_heresy` → `1` + Karta `gc-11` (Fałszywe Świadectwo Cechu): `heresy` → `2`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.23, Deadlocks 0.3%, Pas Biedy 1.5%.

### 🟢 Patch v1.0-alpha.19 (2026-08-21) — Kanon 4P: Karta `so-03` (Podejrzenie): `heresy` → `2` (Zysk 4P Δ +0.2 pkt)
- **Wynik 4P:** Kanon **`79.7`** → **`79.9 pkt`** | Global **`44.8`** | 3p **`24.1`** | 5p **`28.9`**
- **Modyfikacja (`L3_SO-03_HERESY_PLUS1`):** Karta `so-03` (Podejrzenie): `heresy` → `2`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.23, Deadlocks 0.3%, Pas Biedy 1.5%.

### 🟢 Patch v1.0-alpha.18 (2026-08-21) — Kanon 4P: Karta `gc-11` (Fałszywe Świadectwo Cechu): `heresy` → `1` (Zysk 4P Δ +0.3 pkt)
- **Wynik 4P:** Kanon **`79.4`** → **`79.7 pkt`** | Global **`44.9`** | 3p **`24.4`** | 5p **`29.0`**
- **Modyfikacja (`L3_GC-11_HERESY_PLUS1`):** Karta `gc-11` (Fałszywe Świadectwo Cechu): `heresy` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.23, Deadlocks 0.3%, Pas Biedy 1.5%.

### 🟢 Patch v1.0-alpha.17 (2026-08-21) — Kanon 4P: Karta `gc-02` (Czarny Rynek): `gold` → `4` (Zysk 4P Δ +0.6 pkt)
- **Wynik 4P:** Kanon **`78.8`** → **`79.4 pkt`** | Global **`45.9`** | 3p **`23.9`** | 5p **`32.5`**
- **Modyfikacja (`L3_GC-02_GOLD_PLUS1`):** Karta `gc-02` (Czarny Rynek): `gold` → `4`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.24, Deadlocks 0.3%, Pas Biedy 1.5%.

### 🟢 Patch v1.0-alpha.16 (2026-08-20) — Kanon 4P: Karta `so-03` (Podejrzenie): `target_heresy` → `3` (Zysk 4P Δ +0.2 pkt)
- **Wynik 4P:** Kanon **`78.6`** → **`78.8 pkt`** | Global **`46.2`** | 3p **`23.1`** | 5p **`34.3`**
- **Modyfikacja (`L3_SO-03_TARGET_HERESY_PLUS1`):** Karta `so-03` (Podejrzenie): `target_heresy` → `3`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.23, Deadlocks 0.3%, Pas Biedy 1.5%.

### 🟢 Patch v1.0-alpha.15 (2026-08-20) — Kanon 4P: Karta `so-03` (Podejrzenie): `heresy` → `1` (Zysk 4P Δ +0.2 pkt)
- **Wynik 4P:** Kanon **`78.4`** → **`78.6 pkt`** | Global **`46.1`** | 3p **`22.8`** | 5p **`34.7`**
- **Modyfikacja (`L3_SO-03_HERESY_PLUS1`):** Karta `so-03` (Podejrzenie): `heresy` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.23, Deadlocks 0.3%, Pas Biedy 1.5%.

### 🟢 Patch v1.0-alpha.14 (2026-08-20) — Kanon 4P: Karta `kb-10` (Pieczęć Korony): `target_heresy` → `0` (Zysk 4P Δ +0.3 pkt)
- **Wynik 4P:** Kanon **`78.1`** → **`78.4 pkt`** | Global **`45.9`** | 3p **`22.8`** | 5p **`34.4`**
- **Modyfikacja (`L3_KB-10_TARGET_HERESY_MINUS1`):** Karta `kb-10` (Pieczęć Korony): `target_heresy` → `0`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.23, Deadlocks 0.3%, Pas Biedy 1.5%.

### 🟢 Patch v1.0-alpha.13 (2026-08-20) — Kanon 4P: Karta `gc-07` (Skrytobójstwo): `cost` → `0` (Zysk 4P Δ +0.3 pkt)
- **Wynik 4P:** Kanon **`77.8`** → **`78.1 pkt`** | Global **`45.6`** | 3p **`22.6`** | 5p **`33.6`**
- **Modyfikacja (`L3_GC-07_COST_MINUS1`):** Karta `gc-07` (Skrytobójstwo): `cost` → `0`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.20, Deadlocks 0.3%, Pas Biedy 1.5%.

### 🟢 Patch v1.0-alpha.12 (2026-08-20) — Kanon 4P: Karta `gc-09` (Lista Dłużników): `gold` → `1` (Zysk 4P Δ +0.4 pkt)
- **Wynik 4P:** Kanon **`77.4`** → **`77.8 pkt`** | Global **`45.4`** | 3p **`22.6`** | 5p **`33.3`**
- **Modyfikacja (`L3_GC-09_GOLD_PLUS1`):** Karta `gc-09` (Lista Dłużników): `gold` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.20, Deadlocks 0.3%, Pas Biedy 1.5%.

### 🟢 Patch v1.0-alpha.11 (2026-08-20) — Kanon 4P: Karta `gc-11` (Fałszywe Świadectwo Cechu): `cost` → `0` (Zysk 4P Δ +0.5 pkt)
- **Wynik 4P:** Kanon **`76.9`** → **`77.4 pkt`** | Global **`44.8`** | 3p **`22.6`** | 5p **`31.8`**
- **Modyfikacja (`L3_GC-11_COST_MINUS1`):** Karta `gc-11` (Fałszywe Świadectwo Cechu): `cost` → `0`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.20, Deadlocks 0.3%, Pas Biedy 1.5%.

### 🟢 Patch v1.0-alpha.10 (2026-08-19) — Kanon 4P: Karta `so-03` (Podejrzenie): `target_heresy` → `2` (Zysk 4P Δ +0.4 pkt)
- **Wynik 4P:** Kanon **`76.5`** → **`76.9 pkt`** | Global **`45.6`** | 3p **`22.9`** | 5p **`34.2`**
- **Modyfikacja (`L3_SO-03_TARGET_HERESY_PLUS1`):** Karta `so-03` (Podejrzenie): `target_heresy` → `2`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.21, Deadlocks 0.3%, Pas Biedy 1.6%.

### 🟢 Patch v1.0-alpha.9 (2026-08-19) — Usunięcie martwej mechaniki CAA `path_era` ze SSOT i silnika
- **Wynik 4P:** Kanon **`76.5 pkt`** (bez zmian — parametr był martwy / przezroczysty)
- **Modyfikacja:** Usunięcie parametru `victory.cienie_al_andalus.path_era` (wartość 1) oraz powiązanego warunku w silniku gry i audytorach.
- **Efekt:** Czysty model reguł — brak martwych klauzul i zbędnych testów o zerowej delcie w raportach Poziomu 2.

### 🟢 Patch v1.0-alpha.8 (2026-08-19) — Kanon 4P: Karta `caa-10` (Echo Alhambry): `cost` → `1` (Zysk 4P Δ +0.1 pkt)
- **Wynik 4P:** Kanon **`76.4`** → **`76.5 pkt`** | Global **`46.9`** | 3p **`22.3`** | 5p **`38.7`**
- **Modyfikacja (`L3_CAA-10_COST_PLUS1`):** Karta `caa-10` (Echo Alhambry): `cost` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.21, Deadlocks 0.3%, Pas Biedy 1.6%.

### 🟢 Patch v1.0-alpha.7 (2026-08-19) — Kanon 4P: Limit Er: offset +1 (nowy: 14) (Zysk 4P Δ 0.0 pkt)
- **Wynik 4P:** Kanon **`76.4`** → **`76.4 pkt`** | Global **`46.9`** | 3p **`22.3`** | 5p **`38.7`**
- **Modyfikacja (`L1_MAX_ERAS_PLUS1`):** Limit Er: offset +1 (nowy: 14).
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.21, Deadlocks 0.3%, Pas Biedy 1.6%.

### 🟢 Patch v1.0-alpha.6 (2026-08-19) — Kanon 4P: Karta `kt-11` (Medytacja Sefirot): `cost` → `2` (Zysk 4P Δ +0.2 pkt)
- **Wynik 4P:** Kanon **`76.2`** → **`76.4 pkt`** | Global **`46.3`** | 3p **`20.6`** | 5p **`38.7`**
- **Modyfikacja (`L3_KT-11_COST_PLUS1`):** Karta `kt-11` (Medytacja Sefirot): `cost` → `2`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.21, Deadlocks 0.5%, Pas Biedy 1.6%.

### 🟢 Patch v1.0-alpha.5 (2026-08-18) — Kanon 4P: Karta `gc-07` (Skrytobójstwo): `cost` → `1` (Zysk 4P Δ +0.3 pkt)
- **Wynik 4P:** Kanon **`75.9`** → **`76.2 pkt`** | Global **`46.6`** | 3p **`20.8`** | 5p **`39.6`**
- **Modyfikacja (`L3_GC-07_COST_MINUS1`):** Karta `gc-07` (Skrytobójstwo): `cost` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.21, Deadlocks 0.5%, Pas Biedy 1.6%.

### 🟢 Patch v1.0-alpha.4 (2026-08-18) — Kanon 4P: Limit Er: offset +1 (nowy: 13) (Zysk 4P Δ +1.2 pkt)
- **Wynik 4P:** Kanon **`74.7`** → **`75.9 pkt`** | Global **`46.4`** | 3p **`21.0`** | 5p **`40.5`**
- **Modyfikacja (`L1_MAX_ERAS_PLUS1`):** Limit Er: offset +1 (nowy: 13).
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.21, Deadlocks 0.5%, Pas Biedy 1.6%.

### 🟢 Patch v1.0-alpha.3 (2026-08-18) — Kanon 4P: Limit Er: offset +1 (nowy: 12) (Zysk 4P Δ +1.3 pkt)
- **Wynik 4P:** Kanon **`75.2`** → **`76.5 pkt`** | Global **`45.5`** | 3p **`18.6`** | 5p **`40.5`**
- **Modyfikacja (`L1_MAX_ERAS_PLUS1`):** Limit Er: offset +1 (nowy: 12).
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.20, Deadlocks 1.9%, Pas Biedy 1.6%.

### 🟢 Patch v1.0-alpha.2 (2026-08-18) — Kanon 4P: Karta `kb-11` (Tajny Emisariusz): `gold` → `0` (Zysk 4P Δ +0.4 pkt)
- **Wynik 4P:** Kanon **`74.8`** → **`75.2 pkt`** | Global **`43.7`** | 3p **`15.0`** | 5p **`40.5`**
- **Modyfikacja (`L3_KB-11_GOLD_MINUS1`):** Karta `kb-11` (Tajny Emisariusz): `gold` → `0`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.18, Deadlocks 2.7%, Pas Biedy 1.6%.

### 🟢 Patch v0.99.27 (2026-08-18) — Kanon 4P: Kanoniczna Blokada Limitu Er (`max_eras` = 11) i Trwałe Zamrożenie w Narzędziach Audytu
- **Problem:** Automatyczny optymalizator balansu sztucznie podbijał parametr `max_eras` (8 → ... → 14) jako drogę na skróty do redukcji deadlocków bez rozwiązywania realnych problemów ekonomii kart. W `v0.99.26` błędnie zaakceptowano podbicie limitu do 14 Er przy zerowym zysku 4P ($\Delta = 0.00$ pkt).
- **Modyfikacja:**
  1. Ustalono i zablokowano kanoniczny limit: **`max_eras: 11`** (idealne wyczerpanie pełnej talii 11 kart edyktów czasu / Kroniki Dziejów).
  2. Wprowadzono trwałą blokadę tożsamości (`_FROZEN_ID_MARKERS` + `_FROZEN_PARAM_KEYS` w `audytor_4p.py` i `audytor_kanonu.py`), uniemożliwiając optymalizatorom jakąkolwiek ingerencję w limit er.
  3. Załatano warunek akceptacji w `canon_accept.py`, blokując akceptowanie zmian z zerowym zyskiem $\Delta\text{score}$.
- **Synchronizacja reguł:** Zsynchronizowano `game_config.yaml`, `docs/rules/ksiega.md`, `docs/rules/slownik.md` oraz testy jednostkowe.

### 🟢 Patch v0.99.26 (2026-08-18) — Kanon 4P: Limit Er: offset +1 (nowy: 14) (Zysk 4P Δ 0.0 pkt) — [WYCOFANY W v0.99.27]
- **Wynik 4P:** Kanon **`75.8`** → **`75.8 pkt`** | Global **`46.1`** | 3p **`22.8`** | 5p **`38.4`**
- **Modyfikacja (`L1_MAX_ERAS_PLUS1`):** Limit Er: offset +1 (nowy: 14).
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.21, Deadlocks 0.3%, Pas Biedy 1.5%.

### 🟢 Patch v0.99.25 (2026-08-18) — Kanon 4P: Karta `kb-10` (Pieczęć Korony): `target_heresy` → `1` (Zysk 4P Δ -0.4 pkt)
- **Wynik 4P:** Kanon **`76.2`** → **`75.8 pkt`** | Global **`45.5`** | 3p **`21.0`** | 5p **`38.4`**
- **Modyfikacja (`L3_KB-10_TARGET_HERESY_PLUS1`):** Karta `kb-10` (Pieczęć Korony): `target_heresy` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.20, Deadlocks 0.5%, Pas Biedy 1.5%.

### 🟢 Patch v0.99.24 (2026-08-18) — Kanon 4P: Karta `gc-04` (Informator): `target_heresy` → `1` (Zysk 4P Δ +0.7 pkt)
- **Wynik 4P:** Kanon **`75.5`** → **`76.2 pkt`** | Global **`45.4`** | 3p **`21.2`** | 5p **`37.6`**
- **Modyfikacja (`L3_GC-04_TARGET_HERESY_PLUS1`):** Karta `gc-04` (Informator): `target_heresy` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.23, Deadlocks 0.6%, Pas Biedy 1.5%.

### 🟢 Patch v0.99.23 (2026-08-18) — Święte Oficjum: Skalowanie Skazań per liczba graczy (3p: 2, 4p/5p: 3) — Naprawa martwej ścieżki
- **Problem:** W rozgrywce 3-osobowej warunek zwycięstwa `condemns: 3` wymagał skazania 3 unikalnych rywali przy obecności tylko 2 rywali przy stole — ścieżka skazania była matematycznie niemożliwa do spełnienia (0 wygranych we wszystkich 6 setupach 3P).
- **Modyfikacja:** W `game_config.yaml` (`victory.swiete_oficjum.condemns`) wprowadzono skalowanie per-player-count: `3p: 2`, `4p: 3`, `5p: 3`.
- **Efekt:** Pełne odblokowanie i przywrócenie witalności ścieżki skazań w 3P (od 47 do 185 wygranych / 500 partii). Setupy `3p-oficjum-kabala-gildia` i `3p-oficjum-korona-gildia` osiągnęły 🟢 Pełną Witalność (0.00 kary witalności).
- **Synchronizacja reguł i narzędzi:** Zsynchronizowano `game/factions/swiete-oficjum.md`, `game/mechanics/werdykt-stolu.md`, `docs/rules/ksiega.md`, `docs/rules/slownik.md` oraz helper `_n4()` w `tools/sim/feature_impact_4p.py`.

### 🟢 Patch v0.99.22 (2026-08-18) — Kanon 4P: Karta `so-11` (Dekret Czystości Wiary): `heresy` → `1` (Zysk 4P Δ +0.2 pkt)
- **Wynik 4P:** Kanon **`75.3`** → **`75.5 pkt`** | Global **`42.2`** | 3p **`13.0`** | 5p **`37.1`**
- **Modyfikacja (`L3_SO-11_HERESY_PLUS1`):** Karta `so-11` (Dekret Czystości Wiary): `heresy` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.25, Deadlocks 0.6%, Pas Biedy 1.5%.

### 🟢 Patch v0.99.21 (2026-08-18) — Kanon 4P: Karta `kt-05` (Wskazówka Cyklu): `heresy` → `1` (Zysk 4P Δ +1.8 pkt)
- **Wynik 4P:** Kanon **`73.5`** → **`75.3 pkt`** | Global **`42.2`** | 3p **`13.0`** | 5p **`37.2`**
- **Modyfikacja (`L3_KT-05_HERESY_PLUS1`):** Karta `kt-05` (Wskazówka Cyklu): `heresy` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.25, Deadlocks 0.6%, Pas Biedy 1.5%.

### 🟢 Patch v0.99.20 (2026-08-18) — Kanon 4P: Karta `gc-08` (Zatrute Złoto): `heresy` → `1` (Zysk 4P Δ +0.4 pkt)
- **Wynik 4P:** Kanon **`73.1`** → **`73.5 pkt`** | Global **`40.7`** | 3p **`14.5`** | 5p **`33.5`**
- **Modyfikacja (`L3_GC-08_HERESY_PLUS1`):** Karta `gc-08` (Zatrute Złoto): `heresy` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.22, Deadlocks 0.7%, Pas Biedy 1.5%.

### 🟢 Patch v0.99.19 (2026-08-18) — Kanon 4P: Karta `kb-11` (Tajny Emisariusz): `target_heresy` → `1` (Zysk 4P Δ +1.9 pkt)
- **Wynik 4P:** Kanon **`71.2`** → **`73.1 pkt`** | Global **`41.3`** | 3p **`14.2`** | 5p **`36.4`**
- **Modyfikacja (`L3_KB-11_TARGET_HERESY_PLUS1`):** Karta `kb-11` (Tajny Emisariusz): `target_heresy` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.22, Deadlocks 0.7%, Pas Biedy 1.5%.

### 🟢 Patch v0.99.18 (2026-08-18) — Kanon 4P: Karta `gc-01` (Przekupiony Strażnik): `cost` → `2` (Zysk 4P Δ +0.5 pkt)
- **Wynik 4P:** Kanon **`70.7`** → **`71.2 pkt`** | Global **`42.3`** | 3p **`14.6`** | 5p **`40.7`**
- **Modyfikacja (`L3_GC-01_COST_PLUS1`):** Karta `gc-01` (Przekupiony Strażnik): `cost` → `2`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.21, Deadlocks 0.7%, Pas Biedy 1.5%.

### 🟢 Patch v0.99.17 (2026-08-18) — Kanon 4P: Karta `caa-12` (Skrytka w Murach): `heresy` → `0` (Zysk 4P Δ +1.4 pkt)
- **Wynik 4P:** Kanon **`69.3`** → **`70.7 pkt`** | Global **`43.1`** | 3p **`14.8`** | 5p **`42.8`**
- **Modyfikacja (`L3_CAA-12_HERESY_MINUS1`):** Karta `caa-12` (Skrytka w Murach): `heresy` → `0`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.21, Deadlocks 0.7%, Pas Biedy 1.5%.

### 🟢 Patch v0.99.16 (2026-08-18) — Kanon 4P: Karta `so-04` (Publiczne Ostrzeżenie): `gold` → `1` (Zysk 4P Δ 0.0 pkt)
- **Wynik 4P:** Kanon **`69.3`** → **`69.3 pkt`** | Global **`40.7`** | 3p **`14.5`** | 5p **`37.3`**
- **Modyfikacja (`L3_SO-04_GOLD_PLUS1`):** Karta `so-04` (Publiczne Ostrzeżenie): `gold` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.15, Deadlocks 0.6%, Pas Biedy 1.5%.

### 🟢 Patch v0.99.15 (2026-08-18) — Kanon 4P: Karta `gc-08` (Zatrute Złoto): `cost` → `1` (Zysk 4P Δ +0.7 pkt)
- **Wynik 4P:** Kanon **`68.6`** → **`69.3 pkt`** | Global **`40.8`** | 3p **`14.2`** | 5p **`36.8`**
- **Modyfikacja (`L3_GC-08_COST_MINUS1`):** Karta `gc-08` (Zatrute Złoto): `cost` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.14, Deadlocks 0.6%, Pas Biedy 1.5%.

### 🟢 Patch v0.99.14 (2026-08-18) — Kanon 4P: Karta `kb-01` (Rozkaz Dworu): `target_heresy` → `1` (Zysk 4P Δ +2.8 pkt)
- **Wynik 4P:** Kanon **`65.8`** → **`68.6 pkt`** | Global **`38.1`** | 3p **`14.3`** | 5p **`36.7`**
- **Modyfikacja (`L3_KB-01_TARGET_HERESY_PLUS1`):** Karta `kb-01` (Rozkaz Dworu): `target_heresy` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.14, Deadlocks 0.6%, Pas Biedy 1.5%.

### 🟢 Patch v0.99.12 (2026-08-18) — Kanon 4P: Spłaszczenie progu oskarżenia (skalar 7) i usunięcie wyjątków 3p/5p
- **Wynik 4P:** Kanon **`70.4 pkt`** | Kara witalności: **`0.040`**
- **Modyfikacja:** Spłaszczenie `accusation_threshold` do pojedynczego parametru stołu `7` (usunięcie skalowania per-skład 3p:6 / 4p:7 / 5p:8 na rzecz czystego prototypu 4P).
- **Synchronizacja:** Zsynchronizowano dokumentację i procedury stołu.

### 🟢 Patch v0.99.11 (2026-08-18) — Narzędzia: Ujednolicenie sekcji problematycznych mechanik w raporcie 4P + Audyt protez
- **Wynik 4P:** Kanon **`70.4 pkt`** | Kara witalności: **`0.040`**
- **Zmiany w raportowaniu:** Wyłączenie nieaktywnego testu `kb_hooks` z generatora ablacji (`hooks <= 0`). Sekcja **4.0** w raporcie 4P agreguje teraz zbiorczo wszystkie problematyczne mechaniki (`DEAD`, `WEAK/NEUTRAL`, `DISRUPTOR`).
- **Weryfikacja reguł:** Odrzucenie sztucznej protezy `condemns: 3 → 2` oraz weryfikacja unikalności ścieżki Skazań.
- **Telemetria 4P:** SO 25.8%, GC 24.0%, KT 25.4%, KB 29.5%, CAA 20.2%.

### 🟢 Patch v0.99.10 (2026-08-18) — Kanon 4P: Karta `so-08` (Nasłanie Inkwizytora): `cost` → `0` (Zysk 4P Δ -0.5 pkt)
- **Wynik 4P:** Kanon **`63.7`** → **`63.2 pkt`** | Global **`39.0`** | 3p **`14.7`** | 5p **`37.7`**
- **Modyfikacja (`L3_SO-08_COST_MINUS1`):** Karta `so-08` (Nasłanie Inkwizytora): `cost` → `0`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.19, Deadlocks 2.1%, Pas Biedy 1.4%.

### 🟢 Patch v0.99.9 (2026-08-18) — Kanon 4P: Karta `caa-06` (Ucieczka z Lochów): `cost` → `0` (Zysk 4P Δ +0.6 pkt)
- **Wynik 4P:** Kanon **`63.1`** → **`63.7 pkt`** | Global **`39.1`** | 3p **`14.6`** | 5p **`37.5`**
- **Modyfikacja (`L3_CAA-06_COST_MINUS1`):** Karta `caa-06` (Ucieczka z Lochów): `cost` → `0`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.18, Deadlocks 2.1%, Pas Biedy 1.4%.

### 🟢 Patch v0.99.8 (2026-08-18) — Kanon 4P: Karta `caa-08` (Kaptur Nocy): `heresy` → `0` (Zysk 4P Δ +0.4 pkt)
- **Wynik 4P:** Kanon **`62.7`** → **`63.1 pkt`** | Global **`38.7`** | 3p **`14.5`** | 5p **`37.0`**
- **Modyfikacja (`L3_CAA-08_HERESY_MINUS1`):** Karta `caa-08` (Kaptur Nocy): `heresy` → `0`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.18, Deadlocks 2.1%, Pas Biedy 1.4%.

### 🟢 Patch v0.99.7 (2026-08-18) — Kanon 4P: Karta `kt-10` (Pieczęć Salomona): `heresy` → `2` (Zysk 4P Δ +0.9 pkt)
- **Wynik 4P:** Kanon **`61.8`** → **`62.7 pkt`** | Global **`39.1`** | 3p **`14.5`** | 5p **`38.7`**
- **Modyfikacja (`L3_KT-10_HERESY_PLUS1`):** Karta `kt-10` (Pieczęć Salomona): `heresy` → `2`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.18, Deadlocks 2.1%, Pas Biedy 1.4%.

### 🟢 Patch v0.99.6 (2026-08-18) — Kanon 4P: Karta `caa-08` (Kaptur Nocy): `target_heresy` → `2` (Zysk 4P Δ +5.2 pkt)
- **Wynik 4P:** Kanon **`56.2`** → **`61.4 pkt`** | Global **`39.1`** | 3p **`12.9`** | 5p **`41.2`**
- **Modyfikacja (`L3_CAA-08_TARGET_HERESY_PLUS1`):** Karta `caa-08` (Kaptur Nocy): `target_heresy` → `2`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.21, Deadlocks 2.5%, Pas Biedy 1.4%.

### 🟢 Patch v0.99.5 (2026-08-18) — bramka fundamentu → audytor makro

- **Cel:** `FOUNDATION=True` (15–35% we wszystkich 5 setupach 4P) po gwarancji silnika v0.99.4.
- **SSOT:** CAA (`caa-02/03/06/09/10/12`), Korona (`kb-09` cost 4, `kb-10` cost 3), Kabała era **6**; polityka bota (tor relikwii, `kb-10` tylko przy 2 Hakach).
- **Pomiar (5000g, seed 42):** HUD **55,7** | **Fundament True** | min `4p-no-oficjum` **52,0**.
- **Audytor:** przechodzi pomiar bazowy i wchodzi w pulę kandydatów L1–L4 (nie stop na bramce).

### 🟢 Patch v0.99.4 (2026-08-18) — domknięcie gwarancji silnika (L4 + CAA + staged)

- **Problem:** `sea_route_era`, `verdict_secret`, `caa-03/05/08/11`, YAML `condition`/`heresy_decrease`/`decree`/`move_inquisitor` — martwe w simie mimo SSOT.
- **Silnik:** `variants.py`, `card_conditions.py`; Szlak z `sea_route_era`; CAA (`shadow_exit`, ciągnięcie relikwii, warunki); `kb-10` + fix race staged/fiasko (Haki zjadane przed odkryciem); `StagedPlay.cond_ok` snapshot warunku.
- **Testy:** `test_engine_guarantee.py` — **204 passed**.
- **Balans (5000g, seed 42):** HUD **44,8** | **Fundament nadal False** (CAA ~13% w `4p-core`/`4p-no-kabala` przez `caa-10` condition; Korona ~36–40% w składach bez Oficjum). Audytor makro **uruchamia się**, kończy na bramce — **0 patchy**.

### 🟡 Patch v0.99.3 (2026-08-18) — wspinaczka do bramki audytora (niedokończona; **nie** v1.0)

- **Numer:** kontynuacja serii 0.99.x — bramka fundamentu nadal **False**, audytor makro **stop**. v1.0 zarezerwowane na przejście 15–35% we wszystkich setupach 4P.

- **Cel:** wszystkie udziały 4P w **15–35%** (`table_has_share_foundation`) → dopiero wtedy audytor makro może zapisywać.
- **Łańcuch od v0.99.2 (24,4 pkt / 5000g):** fragmenty **2**; buff CAA (`caa-02/04/05/07` taniej, `caa-06` ☣0, `caa-08` cost 1, `caa-09` cost 1, `caa-10` cost 0); era KT **5**; ścieżka Cieni **era 1**; Gildia upadki **8**; stosy **6**; reszta bez zmian (skazania 3, relikwie 2).
- **Pomiar (5000 g/setup, seed 42):** HUD **54,4** | min `4p-core` **46,7** | witalność **0,000**. **Fundament nadal False.**
- **Setupy OK (15–35%):** `4p-no-cienie`, `4p-no-korona`, `4p-no-oficjum` (CAA **15,0%**).
- **Blokada:** CAA **12,1%** (`4p-core`), **13,0%** (`4p-no-kabala`) — ~2 pp poniżej progu mimo dziesiątek iteracji L2/L3.
- **Odrzucone:** relikwie 1 (CAA ~66–90%), stosy 5 (SO 37% w `4p-no-kabala`), stosy 7 (SO 8,7% w `4p-no-cienie`), KB era 6 bez kompensacji (Korona 0% w core), próg 4p 8, dekrety 3.
- **Narzędzie:** `tools/sim/measure_foundation.py` — szybki pomiar udziałów + flagi OUT.
- **Następny krok:** rework toru CAA (silnik / `caa-03` / polityka bota), nie kolejne ±1 kosztu; audytor makro **stop** na bramce fundamentu.

### 🟢 Patch v0.99.2 (2026-08-18) — L2: Oficjum stosy 7 → 6

- **Źródło:** `audyt_level2_raport.md` v0.99.1 (3000 g/setup): baza 4P **16,5 pkt**; stosy 7→6 **+7,5** na 4P, telemetria 🟢 (6,8 Er, DL 13,2%).
- **SSOT:** `victory.swiete_oficjum.stacks` **6** (skazania 3 bez zmian).
- **Bez:** skazania 2, upadki 8 (DL 18,5%), fragmenty 2, dekrety ±1.
- **Następny krok:** telemetria udziałów 4P; audytor makro nadal stop do 15–35%.

### 🟢 Patch v0.99.1 (2026-08-18) — L3 ręcznie: GC disruptory + KT start

- **Źródło:** `audyt_level3_raport.md` v0.99 + impact 4P (gc-06/09 disruptory, KT ~8.7%).
- **Karty:** `gc-06` / `gc-09` heresy **0 → 1** (dźwignia L3: +1.0 / +1.4 HUD); `kt-03` heresy **1 → 0** (konserwatywny buff KT: +1.6 na 4P w L3).
- **Bez:** cost gc-09→4, KB-09/10, KT-09 (za agresywne Δ+14).
- **Następny krok:** telemetria 1500–5000 g/setup; jeśli SO/GC nadal poza 15–35%, L2 (stosy/upadki) z pomiarem.

### 🟢 Patch v0.99 (2026-08-17) — fundament pod prawdziwy silnik (nie audytor z dołu)

- **Diagnoza (600 g/setup):** `4p-core` SO ~57% + KB ~37%, KT ~0.7%; bez Korony GC ~65%. Proxy-karty (darmowy kurier, darmowy informator) + `kt-03` tylko przy herezji 4–6 + `gc-10` na każdym krytycznym = zła gra.
- **Silnik:** `kt-03` zawsze daje fragment (tor startuje); `gc-10` tylko Hak/Marionetka (nie samo krytyczna herezja).
- **SSOT:** Obserwowana **5**; Oficjum stosy **7**; Gildia upadki **7**; Kabała od ery **4**; `caa-05` koszt **1**; `gc-04` koszt **1**; `gc-09` koszt **3**.
- **Pomiar (1500 g/setup):** HUD **~11 pkt** (z 3.7); KT w core **~7.5%**; min setup **~8.7** (`4p-no-korona`). Czerwona linia 15–35% nadal nie — SO ~52%, GC w setupach bez Korony ~50–59%. **Audytor makro stop**; kolejny krok: L3 / tempo SO (nie skazania 2).

### 🟢 Patch v0.98 (2026-08-17) — korekta L2 po audycie v0.97
- **Pomiar:** baza v0.97 = **6.98 Er** (już w 5–7), ale HUD **0.6 pkt**. Ślepe `+1` na wszystkich celach.
- **Żywe:** stosy **5** (6 = deadlock 15%), upadki **5** (4 psuje global). Skazania **3** (2 to proteza martwej ścieżki).
- **Martwe / przesadzone — cofnięte:** relikwie 3→**2**, era Cieni/szlak 5→**4**, dekrety 3→**2**, fragmenty 4→**3**, era Kabały 7→**6** (Δ≈0 w L2).

### 🟢 Patch v0.97 (2026-08-17) — dłuższa partia: +1 na licznikach C (ręcznie)
- **Dlaczego:** po naprawie silnika 4P kończyło się **~4.49 Er** (podłoga telemetryki 4.5). Audytor `±1` chciał **obniżać** relikwie (jeszcze krócej) i nie złoży wektora „wszystkie cele w górę”.
- **Jedna liczba na stół:** stosy **5**, relikwie **3**, ścieżka/szlak od Ery **5**, dekrety **3**, fragmenty **4** od Ery **7**, upadki **5**. Skazania **3** (sufit unikalnych rywali przy 4p).
- **Nie ruszać:** Gospodarcza, Obserwowana, karty/erę, próg oskarżenia.

### ⚪ Pomiar makro 4P (2026-08-17) — nie jest patchem; YAML bez zmian
- Lookahead (ultra): złoto 4→3 + Kabała od ery 7 + próg 5/6/7 = **73.7** (baza 57.4). Era Kabały sama w 1D: 54.9. Limit Er +1 przy tym samym wyniku = jeździec.
- Zapis przerwany (SIGKILL). To nie bump wersji. SSOT: **v0.96**.

### 🟢 Patch v0.96 (2026-08-17) — Agenci 3, próg 6/7/8, werdykt jawny
- **Cofnięcie trójki HUD z v0.95:** agenci **2 → 3**, próg oskarżenia **7/8/9 → 6/7/8**, `verdict_secret` wyłączony.
- **Dlaczego:** agenci to fundament stołu; tajny Werdykt ogłupia AI. HUD +3.9 nie jest naprawą. Próg oskarżenia wraca do puli audytora (tempo sądu).
- **Audytor:** pula 4P makro = wyłącznie ±1 z L1/L2/L4 (kanon ma jeszcze L3 kart). Bez katalogu `feature_impact`. Tożsamość: agenci, Autodafé, limit ręki, Werdykt Tajny, Kronika 1 edykt/erę. Nie wskrzeszać `hooks` / `heresy_band` / `korona_borgiowie.era` w victory.

### 🔴 Patch v0.95 (2026-08-17) — odrzucony: agenci −1 + próg +1 + Werdykt Tajny
- **Wynik 4P (win share):** **`84.3 pkt`** (baza `80.4`) | Global **`66.4`** | 3p **`38.4`** | 5p **`77.3`**
- **Modyfikacja (`L1_AGENTS_MINUS1__L1_THRESHOLD_PLUS1__L4_VERDICT_SECRET`):** jeździec HUD — cofnięty w v0.96.

### 🟢 Patch v0.94 (2026-08-17) — Autodafé zostaje co 3 Ery
- **Cofnięcie L1 z v0.93:** `autodafe_cooldown` **4 → 3**. Przy końcu ~6 Er cooldown 4 to zwykle **1** ogień; 3 Ery to **2** (3 i 6). Inkwizycja nie jest gałką HUD.
- **Zostaje z v0.93:** stosy **4**, Gildia **4** (jedna liczba, bez `no_oficjum`).
- **Audytor 4P / kanon:** cooldown Autodafé wyjęty z puli (jak limit ręki). Ablacja w raporcie użyteczności nadal może to mierzyć.

### 🟢 Patch v0.93 (2026-08-17) — Kanon 4P Makro: Cooldown Autodafé: offset +1 (nowy: 4) + Święte Oficjum: Stosy offset -1 + Gildia Cieni: Upadki (z Oficjum) offset +1 + Gildia Cieni: Upadki (bez Oficjum) offset -1 (Zysk 4P Δ +36.8 pkt)
- **Wynik 4P (win share):** **`83.8 pkt`** (baza `47.0`) | blended `47.0` → `83.8` | Global **`61.2`** | 3p **`31.7`** | 5p **`70.7`**
- **Modyfikacja (`L2_GC_FALLS_DEFAULT_PLUS1__L2_SO_STACKS_MINUS1__L2_GC_FALLS_NO_SO_MINUS1__L1_AUTODAFE_COOLDOWN_PLUS1`):** Cooldown Autodafé: offset +1 (nowy: 4) + Święte Oficjum: Stosy offset -1 + Gildia Cieni: Upadki (z Oficjum) offset +1 + Gildia Cieni: Upadki (bez Oficjum) offset -1.
- **Efekt:** Makro L1/L2/L4. Telemetria: Średnia Er 6.13, Deadlocks 1.5%, Pas Biedy 5.4%. Witalność `0.000` → `0.000`.
- **Uwaga:** `L1_AUTODAFE_COOLDOWN_PLUS1` to jeździec HUD — cofnięty w v0.94. Stosy 4 i Gildia 4/4 zostają.

### 🟢 Patch v0.92 (2026-08-17) — Dual-win Oficjum: stos ≠ skazanie
- **Wynik 4P (win share, 5000 g/setup):** **47.0 pkt** | CAA **21.1%** · GC **35.6%** · KB **25.7%** · KT **27.6%** · SO **15.0%** | witalność **0.000**
- **Telemetria (ta sama próba):** Śr. Er **5.91**, Deadlocks **1.5%**, Pas Biedy **5.6%**
- **Ścieżki SO (n=2901 dual-win):** stosy **51.4%** · skazania **48.6%** — obie ≥8%. Próg **condemns: 3** zostaje.
- **Werdykt (warstwa C):** unikalne Skazanie z każdego wyroku na rywalu; **Stos tylko gdy Oficjum oskarżało** (także powtórka). Stół nie dobija 5 stosów „przy okazji”. Threat / pile-on stołu dopiero 1 przed wygraną (4 stosy lub 2 nazwiska), nie od 2 stosów / 1 nazwiska.
- **HUD 47 pkt** to Gildia ~41% w setupach z GC i SO ~15% — to zadanie audytora 4P, nie proteza 3→2.
- **Audytor:** `sim/.venv/bin/python tools/sim/audytor_4p.py` (witalność nie veto-uje bazy; L2_SO_CONDEMNS_MINUS1 nadal proteza).

### 🟢 Patch v0.91 (2026-08-17) — Cofnięcie patrolu-łowcy Inkwizytora (powrót do pasma 4P)
- **Wynik 4P (win share, 5000 g/setup):** **86.6 pkt** | CAA **21.3%** · GC **25.4%** · KB **26.5%** · KT **25.8%** · SO **25.9%** | witalność **1.200**
- **Telemetria (ta sama próba):** Śr. Er **5.96**, Deadlocks **1.1%**, Pas Biedy **5.5%**
- **Przesiew 400 g/setup (przed pełną ablacją):** CAA 22.2 · GC 23.5 · KB 26.4 · KT 26.0 · SO 26.9 (pasmo 20–30%)
- **Cofnięcie v0.90:** łowca na najwyższą herezję wybił pasmo. Zostaje losowy patrol `speed 1`.
- **Raport:** [`archive/v0.91/raport_uzytecznosci_i_wplywu_4p.md`](sim-reports/archive/v0.91/raport_uzytecznosci_i_wplywu_4p.md)

### 🔴 Patch v0.90 (2026-08-17) — Inkwizytor łowca (wycofane w v0.91)
- **Wynik 4P (win share, 400 g/setup):** CAA **19.3%** · KB **19.2%** · KT **20.1%** · SO **32.5%** · GC **33.8%** — poza 20–30%.
- **Impact blended (`--no-cards`, 400 g):** **27.6 pkt** | Śr. Er **5.59**, Deadlocks **0.5%**, Pas Biedy **5.6%**
- **Audyt L4 (250 g/setup):** Global **20.3** | 3p **26.3** | 4p **24.4** | 5p **10.2** | Śr. Er **6.34**, Deadlocks **3.7%**, Pas Biedy **5.2%**
- **L4_INQUISITOR_SPEED0:** Global 20.3 → **31.9** (`+11.6`) | 4p 24.4 → **51.6** — patrol-hunt był za gruby, nie speed 1.
- **Audyt L4:** [`archive/v0.90/audyt_level4_raport.md`](sim-reports/archive/v0.90/audyt_level4_raport.md)

### 🟢 Patch v0.89 (2026-08-17) — Oficjum: skazania równorzędne ze stosami
- **Impact blended (400 g, `--no-cards`):** **34.7 pkt** (bez zmian vs v0.88) | Śr. Er **5.98**, Deadlocks **1.1%**, Pas Biedy **5.6%**
- **Audyt L2 (250 g/setup):** Global **27.1** | 3p **24.8** | 4p **34.8** | 5p **21.7** | Śr. Er **6.73**, Deadlocks **5.5%**, Pas Biedy **5.1%**
- **L2_SO_CONDEMNS_MINUS1 (3→2):** Global 27.1 → **53.4** (`+26.3`) | 4p 34.8 → **62.6** — próg 3 zostaje; ścieżka uśpiona, nie skasowana.
- Silnik: najpierw **3 skazania**, potem **5 stosów**.
- **Audyt L2:** [`archive/v0.89/audyt_level2_raport.md`](sim-reports/archive/v0.89/audyt_level2_raport.md)

### 🟢 Patch v0.88 (2026-08-17) — Szlak morski od Ery 4
- **4P share (400 g/setup):** CAA **21.9% → 22.2%**
- **Impact blended (400 g, `--no-cards`):** **34.7 pkt** | Śr. Er **5.98**, Deadlocks **1.1%**, Pas Biedy **5.6%**
- **Audyt L4 (250 g/setup):** Global **27.1** | 3p **24.8** | 4p **34.8** | 5p **21.7** | Śr. Er **6.73**, Deadlocks **5.5%**, Pas Biedy **5.1%**
- `variants.sea_route_era`: **6 → 4**. `L4_SEA_ROUTE_ERA6` Δ≈0 (zegar znowu w oknie ~6 Er).
- **Audyt L4:** [`archive/v0.88/audyt_level4_raport.md`](sim-reports/archive/v0.88/audyt_level4_raport.md)

### 🟢 Patch v0.87 (2026-08-17) — Higiena L2: martwe kłódki z warunków zwycięstwa
- **4P share (400 g/setup):** CAA **21.9** · GC **23.9** · KB **26.4** · KT **25.9** · SO **26.9** (pasmo 20–30%)
- **Impact blended (400 g, `--no-cards`):** **35.1 pkt** | Śr. Er **5.96**, Deadlocks **1.0%**, Pas Biedy **5.6%** — HUD ~35 to kara witalności (skazania), nie zapaść share
- **Audyt L2 (250 g/setup):** Global **26.8** | 3p **24.4** | 4p **34.9** | 5p **21.2** | Śr. Er **6.73**, Deadlocks **5.5%**, Pas Biedy **5.1%**
- Korona: `hooks: 1 → 0` (wygrana = 2 dekrety). Cienie: bez darmowej `caa_era`. Kabała: pasmo **0–9**. Limit Er **12**.
- `condemns −1` nadal rusza L2 (4p 34.9 → 63.3) — ścieżka uśpiona, nie usunięta.
- **Audyt L2 + impact `--no-cards`:** [`archive/v0.87/`](sim-reports/archive/v0.87/)

### 🟢 Patch v0.86 (2026-08-17) — Kanon 4P: Karta `caa-05` (Ukryty Kurier): `cost` → `0` + Karta `caa-03` (Cień na Rynku): `gold` → `1` (Zysk 4P Δ +0.1 pkt)
- **Wynik 4P:** Kanon **`94.5`** → **`94.6 pkt`** | Global **`67.4`** | 3p **`45.7`** | 5p **`65.0`**
- **Modyfikacja (`L3_CAA-05_COST_MINUS1__L3_CAA-03_GOLD_PLUS1`):** Karta `caa-05` (Ukryty Kurier): `cost` → `0` + Karta `caa-03` (Cień na Rynku): `gold` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.94, Deadlocks 1.1%, Pas Biedy 5.6%.

### 🟢 Patch v0.85 (2026-08-17) — Kanon 4P: Karta `caa-08` (Kaptur Nocy): `target_heresy` → `1` (Zysk 4P Δ +0.3 pkt)
- **Wynik 4P:** Kanon **`94.2`** → **`94.5 pkt`** | Global **`68.2`** | 3p **`46.2`** | 5p **`67.0`**
- **Modyfikacja (`L3_CAA-08_TARGET_HERESY_PLUS1`):** Karta `caa-08` (Kaptur Nocy): `target_heresy` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.93, Deadlocks 1.1%, Pas Biedy 5.6%.

### 🟢 Patch v0.84 (2026-08-17) — Kanon 4P: Kabała Toledo: Pasmo Herezji 3–9 (Zysk 4P Δ +1.3 pkt)
- **Wynik 4P:** Kanon **`92.9`** → **`94.2 pkt`** | Global **`69.6`** | 3p **`45.9`** | 5p **`71.7`**
- **Modyfikacja (`L2_KT_HERESY_HIGH_PLUS1`):** Kabała Toledo: Pasmo Herezji 3–9.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.93, Deadlocks 1.1%, Pas Biedy 5.5%.

### 🟢 Patch v0.83 (2026-08-17) — Kanon 4P: Karta `gc-12` (Złodziejski Zwiad): `heresy` → `2` (Zysk 4P Δ +0.4 pkt)
- **Wynik 4P:** Kanon **`92.5`** → **`92.9 pkt`** | Global **`68.3`** | 3p **`47.2`** | 5p **`67.3`**
- **Modyfikacja (`L3_GC-12_HERESY_PLUS1`):** Karta `gc-12` (Złodziejski Zwiad): `heresy` → `2`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.95, Deadlocks 1.2%, Pas Biedy 5.5%.

### 🟢 Patch v0.82 (2026-08-17) — Kanon 4P: Karta `kb-02` (Pobór Podatków): `target_heresy` → `1` (Zysk 4P Δ +2.9 pkt)
- **Wynik 4P:** Kanon **`89.6`** → **`92.5 pkt`** | Global **`67.6`** | 3p **`47.4`** | 5p **`66.8`**
- **Modyfikacja (`L3_KB-02_TARGET_HERESY_PLUS1`):** Karta `kb-02` (Pobór Podatków): `target_heresy` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.94, Deadlocks 1.2%, Pas Biedy 5.7%.

### 🟢 Patch v0.81 (2026-08-17) — Kanon 4P: Karta `kb-03` (Plotka Dworska): `heresy` → `1` (Zysk 4P Δ +1.8 pkt)
- **Wynik 4P:** Kanon **`87.8`** → **`89.6 pkt`** | Global **`66.9`** | 3p **`44.4`** | 5p **`69.7`**
- **Modyfikacja (`L3_KB-03_HERESY_PLUS1`):** Karta `kb-03` (Plotka Dworska): `heresy` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.01, Deadlocks 1.4%, Pas Biedy 5.8%.

### 🟢 Patch v0.80 (2026-08-17) — Kanon 4P: Karta `gc-01` (Przekupiony Strażnik): `gold` → `1` (Zysk 4P Δ +1.8 pkt)
- **Wynik 4P:** Kanon **`86.0`** → **`87.8 pkt`** | Global **`64.7`** | 3p **`40.5`** | 5p **`67.3`**
- **Modyfikacja (`L3_GC-01_GOLD_PLUS1`):** Karta `gc-01` (Przekupiony Strażnik): `gold` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.03, Deadlocks 1.4%, Pas Biedy 5.9%.

### 🟢 Patch v0.79 (2026-08-17) — Kanon 4P: Karta `so-02` (Skarbiec Trybunału): `target_heresy` → `1` (Zysk 4P Δ +4.7 pkt)
- **Wynik 4P:** Kanon **`81.3`** → **`86.0 pkt`** | Global **`63.9`** | 3p **`39.2`** | 5p **`67.1`**
- **Modyfikacja (`L3_SO-02_TARGET_HERESY_PLUS1`):** Karta `so-02` (Skarbiec Trybunału): `target_heresy` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.03, Deadlocks 1.5%, Pas Biedy 5.5%.

### 🟢 Patch v0.78 (2026-08-17) — Kanon 4P: Gildia Cieni: Upadki (bez Oficjum) offset +1 (Zysk 4P Δ +5.1 pkt)
- **Wynik 4P:** Kanon **`76.2`** → **`81.3 pkt`** | Global **`62.9`** | 3p **`37.7`** | 5p **`69.2`**
- **Modyfikacja (`L2_GC_FALLS_NO_SO_PLUS1`):** Gildia Cieni: Upadki (bez Oficjum) offset +1.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 6.03, Deadlocks 1.6%, Pas Biedy 5.5%.

### 🟢 Patch v0.76 (2026-08-17) — 10 nowych kart frakcyjnych (talie 10 → 12)
- **Wynik 4P:** Kanon **`30.1`** → **`79.6 pkt`** | Global L1 **`35.5`** → **`58.3 pkt`** | 3p **`34.1`** → **`39.5`** | 4p L1 **`34.3`** → **`68.8`** | 5p **`38.1`** → **`66.6`**
- **Modyfikacja (katalog):** Każda frakcja +2 karty. Cel: mniejsza przewidywalność dociągu (ręka 5/12 zamiast 5/10) bez zmiany zasad stołu.
  - SO: `so-11` Dekret Czystości Wiary · `so-12` Straż Trybunalska
  - CAA: `caa-11` Nocna Zmiana Warty · `caa-12` Skrytka w Murach
  - KB: `kb-11` Tajny Emisariusz · `kb-12` Szantaż Salonowy
  - KT: `kt-11` Medytacja Sefirot · `kt-12` Strażnik Archiwum
  - GC: `gc-11` Fałszywe Świadectwo Cechu · `gc-12` Złodziejski Zwiad
- **Audyt Poziomu 1** ([`archive/v0.76/audyt_level1_raport.md`](sim-reports/archive/v0.76/audyt_level1_raport.md), 3000 gier/setup): baza Global 🔴 **58.3** · **4p 68.8**. Telemetria bazy w normie (6.63 Er, deadlock 5.9%, pas biedy 5.3%, Autodafé 1.62, oskarżenia 3.71). **3p/5p odłożone** — wyjątki zasad dopiero po idealnym kanonie 4p.
  - Warianty **4p z zyskiem:** limit ręki 5→4 (**68.8 → 75.6, +6.8**) · agenci 3→2 (**+1.0**). Reszta L1 na 4p płaska lub na minus (złoto ±1, Autodafé ±1, ręka 6 **−23.0**, agenci 4 **−12.3**).
- **Efekt (kanon 4p):** `4p-core` **79.6** (CAA 29.0 / SO 21.6 / KT 26.8 / KB 22.7 — wszystkie w paśmie 20–30%). Najsłabsze składy 4p: `4p-no-oficjum` 58.6 (GC 34.8%) · `4p-no-cienie` 60.8 (GC 34.1%). Raporty: `playtesting/sim-reports/archive/v0.76/`.

### 🟢 Patch v0.75 (2026-08-16) — Inteligentne Utility AI (Net ROI, Strefy Herezji, Taktyczny Pas) i Oczyszczenie Kart SSOT
- **Wynik 4P:** Kanon **`34.4 pkt`** | Global **`35.8 pkt`** | 3p **`34.6 pkt`** | 5p **`38.3 pkt`**
- **Modyfikacja Silnika & AI:**
  - `sim/inquisitio/agents/politics.py`: Wdrożenie wielokryterialnego Utility AI (ocena kosztu netto złota, strefy zagrożenia Herezją, frakcyjne drivery wygranej, rezerwacyjna wartość Pasa).
  - Oczyszczenie kart SSOT: Przywrócenie `gc-02` (Czarny Rynek) do `cost: 1, gold: 3, heresy: 1`, usunięcie zanieczyszczeń `gold: 1` z kart `caa-01`, `caa-04`, `gc-03`, `kt-03`, `kt-09`, `kt-10`, oczyszczenie `so-08`.
- **Efekt:** Odsłonięcie autentycznego rozkładu balansu przy inteligentnych graczach. Drastyczny spadek Pasu Biedy z 24.6% do **5.3%–6.8%**, Deadlocki **0.7%**, Średnia Er **5.65**. Wszystkie raporty zarchiwizowane w `playtesting/sim-reports/archive/v0.75/`.

### 🟢 Patch v0.74 (2026-08-16) — Kanon 4P: Karta `kt-08` (Areszt Wiedzy): `cost` → `1` (Zysk 4P Δ +0.4 pkt)
- **Wynik 4P:** Kanon **`95.9`** → **`96.3 pkt`** | Global **`76.4`** | 3p **`65.3`** | 5p **`70.7`**
- **Modyfikacja (`L3_KT-08_COST_MINUS1`):** Karta `kt-08` (Areszt Wiedzy): `cost` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.48, Deadlocks 0.1%, Pas Biedy 24.6%.

### 🟢 Patch v0.73 (2026-08-16) — Kanon 4P: Karta `gc-02` (Czarny Rynek): `gold` → `1` (Zysk 4P Δ +2.2 pkt)
- **Wynik 4P:** Kanon **`93.7`** → **`95.9 pkt`** | Global **`76.7`** | 3p **`65.8`** | 5p **`71.6`**
- **Modyfikacja (`L3_GC-02_GOLD_MINUS1`):** Karta `gc-02` (Czarny Rynek): `gold` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.48, Deadlocks 0.1%, Pas Biedy 24.6%.

### 🟢 Patch v0.72 (2026-08-16) — Kanon 4P: Karta `so-05` (Wezwanie do Trybunału): `target_heresy` → `1` (Zysk 4P Δ +5.3 pkt)
- **Wynik 4P:** Kanon **`88.4`** → **`93.7 pkt`** | Global **`74.5`** | 3p **`64.4`** | 5p **`67.8`**
- **Modyfikacja (`L3_SO-05_TARGET_HERESY_MINUS1`):** Karta `so-05` (Wezwanie do Trybunału): `target_heresy` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.44, Deadlocks 0.1%, Pas Biedy 24.0%.

### 🟢 Patch v0.71 (2026-08-16) — Kanon 4P: Święte Oficjum: Skazania offset +1 (Zysk 4P Δ +18.5 pkt)
- **Wynik 4P:** Kanon **`69.9`** → **`88.4 pkt`** | Global **`69.2`** | 3p **`68.0`** | 5p **`53.9`**
- **Modyfikacja (`L2_SO_CONDEMNS_PLUS1`):** Święte Oficjum: Skazania offset +1.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.40, Deadlocks 0.1%, Pas Biedy 23.9%.

### 🟢 Patch v0.70 (2026-08-16) — Pełna Aktywacja Reakcji Silnika (`so-05` Wezwanie do Trybunału & `gc-05` Fałszywy Świadek)
- **Wynik 4P:** Kanon **`69.9 pkt`** | Global **`64.8 pkt`** | 3p **`74.3 pkt`** | 5p **`50.2 pkt`**
- **Status Gry:** 50/50 kart w pełni grywalnych w silniku symulacji (aktywne triggery reakcji).
- **Modyfikacja Silnika:**
  - `so-05` (Wezwanie do Trybunału): Reakcja odpalana automatycznie, gdy rywal zagrywa kartę generującą Herezję ($\ge 1$).
  - `gc-05` (Fałszywy Świadek): Reakcja odpalana w Fazie Sądu, przesuwająca 1 głos w werdykcie na korzyść Gildii Cieni.
- **Konfiguracja SSOT:** Zachowanie parametrów bazowych `v0.69` (Benchmark kalibracyjny dla 100% aktywnej talii).
- **Efekt:** Odsłonięcie rzeczywistej siły Świętego Oficjum i Gildii Cieni przy aktywnych reakcjach. Telemetria: Średnia Er 5.73, Deadlocks 0.6%, Pas Biedy 24.9%.

### 🟢 Patch v0.69 (2026-08-16) — Kanon 4P Makro: Limit Er: offset +1 (nowy: 12) (Zysk 4P Δ +0.1 pkt)
- **Wynik 4P:** Kanon **`95.3`** → **`95.4 pkt`** | Global **`75.1`** | 3p **`70.0`** | 5p **`62.6`**
- **Modyfikacja (`L1_MAX_ERAS_PLUS1`):** Limit Er: offset +1 (nowy: 12).
- **Efekt:** Optymalizacja parametrów makro 4P. Telemetria: Średnia Er 5.40, Deadlocks 0.1%, Pas Biedy 23.8%.

### 🟢 Patch v0.68 (2026-08-16) — Kanon 4P Makro: Cienie Al-Andalus: Minimalna Era offset -1 + Wariant: Otwarcie Szlaku Morskiego = Era 6 (Zysk 4P Δ +0.2 pkt)
- **Wynik 4P:** Kanon **`95.1`** → **`95.3 pkt`** | Global **`75.1`** | 3p **`70.1`** | 5p **`62.6`**
- **Modyfikacja (`L2_CAA_ERA_MINUS1__L4_SEA_ROUTE_ERA6`):** Cienie Al-Andalus: Minimalna Era offset -1 + Wariant: Otwarcie Szlaku Morskiego = Era 6.
- **Efekt:** Optymalizacja parametrów makro 4P. Telemetria: Średnia Er 5.40, Deadlocks 0.4%, Pas Biedy 23.8%.

### 🟢 Patch v0.67 (2026-08-16) — Kanon 4P: Karta `kb-01` (Rozkaz Dworu): `heresy` → `1` (Zysk 4P Δ +0.1 pkt)
- **Wynik 4P:** Kanon **`95.0`** → **`95.1 pkt`** | Global **`74.8`** | 3p **`69.9`** | 5p **`61.9`**
- **Modyfikacja (`L3_KB-01_HERESY_PLUS1`):** Karta `kb-01` (Rozkaz Dworu): `heresy` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.42, Deadlocks 0.4%, Pas Biedy 23.9%.

### 🟢 Patch v0.66 (2026-08-16) — Kanon 4P: Karta `so-02` (Skarbiec Trybunału): `gold` → `3` (Zysk 4P Δ +0.5 pkt)
- **Wynik 4P:** Kanon **`94.5`** → **`95.0 pkt`** | Global **`74.9`** | 3p **`68.5`** | 5p **`64.5`**
- **Modyfikacja (`L3_SO-02_GOLD_PLUS1`):** Karta `so-02` (Skarbiec Trybunału): `gold` → `3`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.44, Deadlocks 0.3%, Pas Biedy 23.9%.

### 🟢 Patch v0.65 (2026-08-16) — Kanon 4P: Karta `kt-09` (Fragment Kodeksu): `cost` → `2` (Zysk 4P Δ +0.5 pkt)
- **Wynik 4P:** Kanon **`94.0`** → **`94.5 pkt`** | Global **`76.7`** | 3p **`67.4`** | 5p **`70.9`**
- **Modyfikacja (`L3_KT-09_COST_PLUS1`):** Karta `kt-09` (Fragment Kodeksu): `cost` → `2`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.46, Deadlocks 0.4%, Pas Biedy 24.4%.

### 🟢 Patch v0.64 (2026-08-16) — Kanon 4P: Karta `kt-04` (Zwierciadło Herezji): `cost` → `1` (Zysk 4P Δ +0.1 pkt)
- **Wynik 4P:** Kanon **`93.9`** → **`94.0 pkt`** | Global **`76.7`** | 3p **`67.2`** | 5p **`71.9`**
- **Modyfikacja (`L3_KT-04_COST_PLUS1`):** Karta `kt-04` (Zwierciadło Herezji): `cost` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.47, Deadlocks 0.4%, Pas Biedy 24.4%.

### 🟢 Patch v0.63 (2026-08-16) — Kanon 4P: Karta `caa-10` (Echo Alhambry): `cost` → `1` (Zysk 4P Δ +0.5 pkt)
- **Wynik 4P:** Kanon **`93.4`** → **`93.9 pkt`** | Global **`76.1`** | 3p **`67.3`** | 5p **`70.1`**
- **Modyfikacja (`L3_CAA-10_COST_PLUS1`):** Karta `caa-10` (Echo Alhambry): `cost` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.46, Deadlocks 0.3%, Pas Biedy 24.4%.

### 🟢 Patch v0.62 (2026-08-16) — Kanon 4P: Karta `caa-04` (Fałszywy Trop): `gold` → `1` (Zysk 4P Δ +1.3 pkt)
- **Wynik 4P:** Kanon **`92.1`** → **`93.4 pkt`** | Global **`76.5`** | 3p **`67.8`** | 5p **`71.6`**
- **Modyfikacja (`L3_CAA-04_GOLD_PLUS1`):** Karta `caa-04` (Fałszywy Trop): `gold` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.47, Deadlocks 0.3%, Pas Biedy 24.4%.

### 🟢 Patch v0.61 (2026-08-16) — Kanon 4P: Karta `gc-10` (Upadek Domu): `heresy` → `1` (Zysk 4P Δ +2.3 pkt)
- **Wynik 4P:** Kanon **`89.8`** → **`92.1 pkt`** | Global **`72.7`** | 3p **`68.4`** | 5p **`62.0`**
- **Modyfikacja (`L3_GC-10_HERESY_MINUS1`):** Karta `gc-10` (Upadek Domu): `heresy` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.46, Deadlocks 0.4%, Pas Biedy 24.4%.

### 🟢 Patch v0.60 (2026-08-16) — Kanon 4P: Karta `kb-08` (Przekupstwo Sędziego): `cost` → `2` (Zysk 4P Δ +5.3 pkt)
- **Wynik 4P:** Kanon **`84.5`** → **`89.8 pkt`** | Global **`71.3`** | 3p **`74.5`** | 5p **`51.8`**
- **Modyfikacja (`L3_KB-08_COST_MINUS1`):** Karta `kb-08` (Przekupstwo Sędziego): `cost` → `2`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.42, Deadlocks 0.3%, Pas Biedy 24.3%.

### 🟢 Patch v0.59 (2026-08-16) — Kanon 4P: Karta `gc-03` (Podrzucenie Księgi): `gold` → `1` (Zysk 4P Δ +5.7 pkt)
- **Wynik 4P:** Kanon **`78.8`** → **`84.5 pkt`** | Global **`70.0`** | 3p **`76.8`** | 5p **`49.3`**
- **Modyfikacja (`L3_GC-03_GOLD_PLUS1`):** Karta `gc-03` (Podrzucenie Księgi): `gold` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.46, Deadlocks 0.3%, Pas Biedy 24.6%.

### 🟢 Patch v0.58 (2026-08-16) — Usunięcie Protez Skalowania (Unifikacja Globalna 4P) & Odporność na Autodafé
- **Wyniki Audytu (Próba 10 000 gier/setup × 16 setupów = 160 000 gier, Model Asymptotyczny):**
  - **Global Score:** **`70.6 pkt`** 🟠 (`v0.57: 51.6` $\rightarrow$ **`⬆️ +19.0 pkt`**)
  - **Kanon 4P:** **`79.6 pkt`** 🟡 (`v0.57: 49.4` $\rightarrow$ **`⬆️ +30.2 pkt`**) | `4p-no-oficjum` **`88.9 pkt`**, `4p-core` **`83.4 pkt`**, `4p-no-kabala` **`75.4 pkt`**, `4p-no-cienie` **`72.0 pkt`**, `4p-no-korona` **`71.7 pkt`**
  - **3p Średnia:** **`76.6 pkt`** 🟡 (`v0.57: 66.8` $\rightarrow$ **`⬆️ +9.8 pkt`**) | `3p-oficjum-alandalus-gildia` **`90.2 pkt`**, `3p-oficjum-alandalus-kabala` **`88.9 pkt`**
  - **5p Pełny Stół (`5p-full`):** **`56.7 pkt`** 🔴 (`v0.57: 39.7` $\rightarrow$ **`⬆️ +17.0 pkt`**)
- **Rozkład Szans Wygranych w Kanonie 4P (`4p-core`):**
  - **SO:** `27.4%` (cel 25.0%, odchylenie $+2.4\text{ p.p.}$)
  - **CAA:** `27.1%` (cel 25.0%, odchylenie $+2.1\text{ p.p.}$)
  - **KT:** `24.3%` (cel 25.0%, odchylenie $-0.7\text{ p.p.}$)
  - **KB:** `21.2%` (cel 25.0%, odchylenie $-3.8\text{ p.p.}$)
- **Telemetria 5 Filarów Silnika Gry:** 🟢 **OPTYMALNA I STABILNA**
  - **Średnia Er (Tempo Gry):** **`5.52 Er`** 🟢 (norma 5.0–6.5 Er)
  - **Remisy po Limicie Er (Deadlocks):** **`0.2%`** 🟢 (norma <5.0%)
  - **Pas Biedy (Poverty Rate):** **`22.2%`** 🟢 (norma <28.0%)
  - **Autodafé Inkwizytora:** **`1.53 / partię`** 🟢 (norma 1.0–2.0, pierwsze w Erze 3/4)
  - **Oskarżenia na Dworze:** **`2.78 / partię`** 🟢 (norma 2.0–4.5)
- **Modyfikacje:**
  1. **Usunięcie sztucznych skalowań per-gracz:** Wartości celów i ekonomii 4P stały się globalnymi wartościami bazowymi (`start_gold = 4`, `kb.era = 4`, `kt.era = 6`, `caa.era = 5`). Zachowano wyłącznie naturalnie rosnący próg oskarżenia na Dworze (`3p: 6`, `4p: 7`, `5p: 8`).
  2. **Dostosowanie do aktywnego Autodafé:** Podniesiono próg Świętego Oficjum do `5 Stosów` (oraz Gildii Cieni do `3 Upadków` / `4` bez SO), co przywróciło pełną równowagę stołu bez dotykania mechaniki Inkwizytora.

### 🟢 Patch v0.57 (2026-08-16) — Pełne Oczyszczenie Silnika Gry (SSOT) & Naprawa Autodafé
- **Wyniki Audytu (Próba 10 000 gier/setup × 16 setupów = 160 000 gier, Czysty Silnik):**
  - **Global Score:** **`51.6 pkt`** 🔴 | **Kanon 4P:** **`49.4 pkt`** 🔴 | **3p:** **`66.8 pkt`** 🟠 | **5p:** **`38.5 pkt`** 🔴
  - **Rozkład 4P (`4p-core`):** SO: `37.7%`, CAA: `25.0%`, KB: `18.5%`, KT: `18.9%` (dominacja Świętego Oficjum i Gildii Cieni wynikająca z braku skalowania progów wygranej przy żywym Inkwizytorze).
  - **Telemetria 5 Filarów:** Średnia Er: `5.34`, Deadlocks: `0.1%`, Pas Biedy: `21.4%`, Autodafé: `1.47 / partię` (pierwsze w Erze 3/4), Oskarżenia: `2.64 / partię`.
- **Modyfikacje Silnika:**
  1. **Usunięcie sztucznych filtrów Autodafé:** Wymontowano `rng.random() < 0.18`, wymóg `crowd >= 3` oraz sztuczny limit `so_pl.stacks >= 2` z `inquisitor.py`.
  2. **Kanon terminu Autodafé:** Ustawiono początkowy licznik `eras_since_autodafe = 0`, dzięki czemu pierwsze naturalne Autodafé odbywa się dopiero od Ery 3 (brak czystek na starcie gry w Erach 1–2).
  3. **Naprawa kart w Warstwie C:** Odblokowano pełne działanie `caa-05` (Ukryty Kurier ewakuuje Relikwie) oraz `so-04`, `kt-03`, `kt-05` zgodnie z tekstem kart w `KATALOG.md`.
  4. **Zasady planszowe:** Autodafé zwraca Relikwie w lokacji do puli, a spalenie celu z Hakiem zalicza Upadek Gildii Cieni.
- **Wniosek Analityczny:** Odblokowanie prawdziwego Autodafé sprawiło, że dotychczasowe niskie progi zwycięstwa (`SO: 4 Stosy`, `GC: 2 Upadki`) pozwalały tym dwóm frakcjom wygrywać za szybko, co zdefiniowało konieczność podniesienia ich celów w `v0.58`.

> [!IMPORTANT]
> ### 📐 Wdrożenie Ciągłego Asymptotycznego Modelu Punktacji (`scoring.py`, 2026-08-16)
> Zgodnie z wytycznymi projektowymi wyeliminowano sztuczne ucinanie wyniku do zera (`Score = 0.0`), które powodowało utratę gradientu porównawczego w skrajnie rozjechanych wariantach.
> Nowy model wykorzystuje ciągłą funkcję wygaszania wykładniczego opartego na względnym odchyleniu standardowym frakcji (**RMS Relative Deviation**):
> $$\text{Score} = 100.0 \times \exp\left( -3.2 \cdot \text{RMS\_RD}^{1.25} - \text{Deadlock Penalty} \right)$$
> **Kluczowe właściwości:**
> 1. **Brak zera (`Score > 0.0`):** Nawet warianty o silnej dominacji (np. jedna frakcja 50–70%) zachowują ciągły, niezerowy wynik (np. 15–40 pkt), co umożliwia precyzyjne śledzenie delty optymalizacji ($\Delta$).
> 2. **Rygor strefy mistrzowskiej ($\ge 98.0$ pkt):** Wynik powyżej 98.0 punktów jest bezwzględnie zarezerwowany wyłącznie dla konfiguracji, w których odchylenia wszystkich frakcji nie przekraczają $\le 0.5\text{ p.p.}$ od ideału (np. 24.8% vs 25.2%).
> 3. **Czysty gradient:** Zapewnia optymalizatorom i audytorom pełną widoczność kierunku zmian.

### 🟢 Patch v0.56 (2026-08-16) — Konsolidacja Kanonu 4P i Grand Audit (Nowa Skala Scoringu)
- **Wynik (Nowa Rygorystyczna Skala):** Kanon 4P **`94.9 pkt`** 🟢 (`4p-core` **`99.3 pkt`**, `4p-no-oficjum` **`95.4 pkt`**, `4p-no-kabala` **`94.8 pkt`**, `4p-no-cienie` **`92.6 pkt`**, `4p-no-korona` **`92.5 pkt`**) | 5p **`69.5 pkt`** | 3p **`36.3 pkt`**
- **Konsolidacja Zmian (`v0.53 – v0.56`):**
  1. `korona_borgiowie.era`: `3p: 4 | 4p: 4 | 5p: 4` (otwarcie okna Dekretów od Ery 4).
  2. `caa-07` (Szantaż Bractwa): `cost` → `1`.
  3. `gc-07` (Skrytobójstwo): `heresy` → `0`.
  4. `so-10` (Oczyść Miasto): `cost` → `5`.
- **Efekt:** W `4p-core` osiągnięto rozrzut frakcji poniżej $\pm 0.6\text{ p.p.}$ od idealnego 25.0% (CAA: 24.7%, GC: 24.0%, KB: 25.4%, KT: 25.3%, SO: 25.6%). Telemetria 5 Filarów optymalna: Średnia Er 5.47, Deadlocks 0.4%, Pas Biedy 25.3%.

### 🟢 Patch v0.55 (2026-08-16) — Kanon 4P: Karta `caa-07` (Szantaż Bractwa): `cost` → `1` (Zysk 4P Δ +0.1 pkt)
- **Wynik 4P:** Kanon **`99.7`** → **`99.8 pkt`** | Global **`85.5`** | 3p **`59.6`** | 5p **`97.1`**
- **Modyfikacja (`L3_CAA-07_COST_MINUS1`):** Karta `caa-07` (Szantaż Bractwa): `cost` → `1`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.48, Deadlocks 0.4%, Pas Biedy 25.3%.

### 🟢 Patch v0.54 (2026-08-16) — Kanon 4P: Korona Borgiowie: Era zwycięstwa offset -1 (Zysk 4P Δ +0.1 pkt)
- **Wynik 4P:** Kanon **`99.6`** → **`99.7 pkt`** | Global **`83.8`** | 3p **`65.9`** | 5p **`86.0`**
- **Modyfikacja (`L2_KB_ERA_MINUS1`):** Korona Borgiowie: Era zwycięstwa offset -1.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.48, Deadlocks 0.5%, Pas Biedy 25.4%.

### 🟢 Patch v0.53 (2026-08-16) — Kanon 4P: Karta `gc-07` (Skrytobójstwo): `heresy` → `0` (Zysk 4P Δ +0.1 pkt)
- **Wynik 4P:** Kanon **`99.5`** → **`99.6 pkt`** | Global **`85.4`** | 3p **`73.2`** | 5p **`83.4`**
- **Modyfikacja (`L3_GC-07_HERESY_MINUS1`):** Karta `gc-07` (Skrytobójstwo): `heresy` → `0`.
- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er 5.53, Deadlocks 0.5%, Pas Biedy 25.6%.

### 🟢 Patch v0.52 (2026-08-16) — Karta `so-10` (Oczyść Miasto): `cost` → `5` (Kanon 4P: 99.5 pkt)
- **Wynik:** Kanon 4P **`99.5 pkt`** 🟢 (`4p-core` 99.9, `4p-no-cienie` 99.4, `4p-no-kabala` 99.4, `4p-no-korona` 99.2, `4p-no-oficjum` 99.7) | 5p **`95.2 pkt`** 🟢 | 3p **`66.0 pkt`**
- **Modyfikacja (`so-10`):** Karta `so-10` (Oczyść Miasto): `cost` → `5`.
- **Efekt:** Perfekcyjne wyważenie Kanonu 4P (wszystkie 5 setupów >99 pkt) oraz 5p (95.2 pkt). Zmiana obnaża specyficzną słabość Świętego Oficjum w ciasnym 3p (zaledwie 6 wrogich agentów), gdzie wysoki koszt signature spowalnia pozyskiwanie 4 Stosów. Telemetria: Średnia Er 5.86, Deadlocks 1.5%, Pas Biedy 27.4%.

### 🟢 Patch v0.51 (2026-08-16) — Organiczne Skalowanie Stosów Świętego Oficjum dla 5p (5 Stosów)
- **Wynik 5p:** Skok z `0.0 pkt` do **`66.0 pkt`** 🟠 (SO: **20.6%** vs 20.0% ideał, spadek z dominującego 31.4%)
- **Modyfikacja:** `swiete_oficjum.stacks`: `3p: 4 | 4p: 4 | 5p: 5` (w 5p wymagane 5 Stosów ze względu na 12 wrogich agentów).
- **Efekt:** Całkowite wyleczenie asymetrii Świętego Oficjum w 5p bez naruszania naturalnego progu oskarżeń (6 w 3p, 7 w 4p, 8 w 5p). Telemetria: Średnia Er 5.75, Deadlocks 1.4%, Pas Biedy 27.2%.

### 🟢 Patch v0.50 (2026-08-16) — Karta `kt-10` (Pieczęć Salomona): `cost` → `2` (Zysk Δ +0.1 pkt)
- **Wynik:** Global **`86.9`** | 3p **`82.7`** | 4p **`91.1`** | 5p **`0.0`**
- **Modyfikacja (`L3_KT-10_COST_PLUS1`):** Karta `kt-10` (Pieczęć Salomona): `cost` → `2`.
- **Efekt:** Wzrost wyniku globalnego z 86.8 do **`86.9 pkt`** (+0.1 pkt). Telemetria: Średnia Er 5.80, Deadlocks 1.5%, Pas Biedy 27.4%.

### 🟢 Patch v0.49 (2026-08-16) — Karta `kt-10` (Pieczęć Salomona): `gold` → `1` (Zysk Δ +0.3 pkt)
- **Wynik:** Global **`86.8`** | 3p **`82.6`** | 4p **`91.1`** | 5p **`0.0`**
- **Modyfikacja (`L3_KT-10_GOLD_PLUS1`):** Karta `kt-10` (Pieczęć Salomona): `gold` → `1`.
- **Efekt:** Wzrost wyniku globalnego z 86.5 do **`86.8 pkt`** (+0.3 pkt). Telemetria: Średnia Er 5.80, Deadlocks 1.5%, Pas Biedy 27.4%.

### 🟢 Patch v0.48 (2026-08-16) — Karta `kt-09` (Fragment Kodeksu): `gold` → `1` (Zysk Δ +1.3 pkt)
- **Wynik:** Global **`86.5`** | 3p **`82.9`** | 4p **`90.0`** | 5p **`0.0`**
- **Modyfikacja (`L3_KT-09_GOLD_PLUS1`):** Karta `kt-09` (Fragment Kodeksu): `gold` → `1`.
- **Efekt:** Wzrost wyniku globalnego z 85.2 do **`86.5 pkt`** (+1.3 pkt). Telemetria: Średnia Er 5.80, Deadlocks 1.5%, Pas Biedy 27.4%.

### 🟢 Patch v0.47 (2026-08-16) — Karta `gc-08` (Zatrute Złoto): `cost` → `2` (Zysk Δ +2.4 pkt)
- **Wynik:** Global **`85.2`** | 3p **`82.6`** | 4p **`87.8`** | 5p **`0.0`**
- **Modyfikacja (`L3_GC-08_COST_PLUS1`):** Karta `gc-08` (Zatrute Złoto): `cost` → `2`.
- **Efekt:** Wzrost wyniku globalnego z 82.8 do **`85.2 pkt`** (+2.4 pkt). Telemetria: Średnia Er 5.80, Deadlocks 1.6%, Pas Biedy 27.4%.

### 🟢 Patch v0.46 (2026-08-16) — Karta `kt-07` (Archiwum Ukryte): `heresy` → `1` (Zysk Δ +3.5 pkt)
- **Wynik:** Global **`82.8`** | 3p **`85.2`** | 4p **`80.3`** | 5p **`0.0`**
- **Modyfikacja (`L3_KT-07_HERESY_PLUS1`):** Karta `kt-07` (Archiwum Ukryte): `heresy` → `1`.
- **Efekt:** Wzrost wyniku globalnego z 79.3 do **`82.8 pkt`** (+3.5 pkt). Telemetria: Średnia Er 5.74, Deadlocks 1.3%, Pas Biedy 26.2%.

### 🟢 Patch v0.45 (2026-08-16) — Karta `gc-02` (Czarny Rynek): `cost` → `2` (Zysk Δ +5.5 pkt)
- **Wynik:** Global **`79.3`** | 3p **`71.3`** | 4p **`87.3`** | 5p **`0.0`**
- **Modyfikacja (`L3_GC-02_COST_PLUS1`):** Karta `gc-02` (Czarny Rynek): `cost` → `2`.
- **Efekt:** Wzrost wyniku globalnego z 73.8 do **`79.3 pkt`** (+5.5 pkt). Telemetria: Średnia Er 5.72, Deadlocks 1.2%, Pas Biedy 26.2%.

### 🟢 Patch v0.44 (2026-08-16) — Karta `kt-10` (Pieczęć Salomona): `heresy` → `1` (Zysk Δ +8.3 pkt)
- **Wynik:** Global **`73.8`** | 3p **`72.5`** | 4p **`75.1`** | 5p **`0.0`**
- **Modyfikacja (`L3_KT-10_HERESY_PLUS1`):** Karta `kt-10` (Pieczęć Salomona): `heresy` → `1`.
- **Efekt:** Wzrost wyniku globalnego z 65.5 do **`73.8 pkt`** (+8.3 pkt). Telemetria: Średnia Er 5.65, Deadlocks 1.1%, Pas Biedy 24.9%.

### 🟢 Patch v0.43 (2026-08-16) — Karta `so-08` (Nasłanie Inkwizytora): `target_heresy` → `1` (Zysk Δ +8.8 pkt)
- **Wynik:** Global **`65.5`** | 3p **`55.9`** | 4p **`75.2`** | 5p **`0.0`**
- **Modyfikacja (`L3_SO-08_TARGET_HERESY_PLUS1`):** Karta `so-08` (Nasłanie Inkwizytora): `target_heresy` → `1`.
- **Efekt:** Wzrost wyniku globalnego z 56.7 do **`65.5 pkt`** (+8.8 pkt). Telemetria: Średnia Er 5.67, Deadlocks 0.9%, Pas Biedy 25.0%.

### 🟢 Patch v0.42 (2026-08-16) — Zwiększenie Złota Startowego (4 zł) i Unifikacja Stosów Oficjum (4 Stosy)
- **Status:** Test płynności ekonomicznej i zaostrzenia celów w 3p
- **Modyfikacje:**
  1. **Złoto startowe:** Podniesienie do stałych **`4 zł`** dla wszystkich składów (3p, 4p, 5p), dające graczom pełniejszą swobodę otwarcia w Erze 1.
  2. **Święte Oficjum:** Unifikacja wymogu Stosów do **`4 Stosów`** we wszystkich składach (w tym 3p).

### 🟢 Patch v0.41 (2026-08-16) — Ujednolicenie Skalowania (Złoto 3 zł, Bramki Er, Limit 11 Er)
- **Próba:** 10 000 gier / setup (160 000 gier łącznie), seed 42, warstwa C
- **Telemetria:** Średnia Er **`6.13`** | Deadlocks **`1.6%`** | Pas Biedy **`25.8%`** | Oskarżenia **`3.24`** | Autodafé **`0.44`**
- **Modyfikacje:**
  1. **Złoto startowe:** Ujednolicenie do stałych **`3 zł`** dla wszystkich składów (spadek ubóstwa w 5p z 27.2% do **23.7%**).
  2. **Jednolite Bramki Er:** Ujednolicono minimalną Erę wygranej dla Korony (**`Era 5`** we wszystkich składach) oraz Kabały (**`Era 6`** we wszystkich składach), usuwając sztuczne opóźnienia w 3p.
  3. **Limit Er:** Podniesiono `max_eras` do **`11`** (spadek deadlocków globalnie z 3.9% do **1.6%**).

### 🟢 Patch v0.40 (2026-08-15) — Kanon 3 Faz Gry i Nowa Talia Czasu 2.0
- **Próba:** 5 000 gier / setup (80 000 gier łącznie), seed 42, warstwa C
- **Wynik L2 Baza:** Global **`30.4`** | 3p **`44.3`** | 4p **`16.6`** | 5p **`0.0`**
- **Telemetria:** Średnia Er **`6.24`** | Deadlocks **`3.9%`** | Pas Biedy **`26.6%`** | Oskarżenia **`3.23`** | Autodafé **`0.45`**
- **Modyfikacje:**
  1. **3 Fazy Ery:** Przebudowa struktury rundy na 3 czyste fazy (`I: Intryga` $\rightarrow$ `II: Sąd` $\rightarrow$ `III: Kronika & Czystka`), eliminując martwy start w Erze 1.
  2. **Kronika Dziejów 2.0:** Zaimplementowano pełne 10 kart edyktów historycznych i miejskich w `game/cards/time-deck/`.
  3. **Ekonomia Faz:** Przeniesienie dochodu (+1 zł) do Fazy III oraz wprowadzenie alternatywnej Akcji Gospodarczej (+1 zł) w Fazie I.
  4. **Bramka Korony:** Wprowadzenie wymogu 1 Haka dla Korony & Borgiów (w 5p ujawniła się blokada wymagająca odrębnego skalowania).

### 🟢 Patch v0.35 (2026-08-15) — Karta `caa-08` (Kaptur Nocy): `cost` → `2` (Zysk Δ +0.2 pkt)
- **Wynik:** Global **`97.7`** | 3p **`94.5`** | 4p **`99.0`** | 5p **`99.5`**
- **Modyfikacja (`L3_CAA-08_COST_PLUS1`):** Karta `caa-08` (Kaptur Nocy): `cost` → `2`.
- **Efekt:** Wzrost wyniku globalnego z 97.5 do **`97.7 pkt`** (+0.2 pkt). Telemetria: Średnia Er 5.56, Deadlocks 1.3%, Pas Biedy 26.2%.

### 🟢 Patch v0.34 (2026-08-15) — Karta `caa-01` (Przejście Podziemiami): `gold` → `1` (Zysk Δ +0.3 pkt)
- **Wynik:** Global **`97.5`** | 3p **`93.8`** | 4p **`99.1`** | 5p **`99.6`**
- **Modyfikacja (`L3_CAA-01_GOLD_PLUS1`):** Karta `caa-01` (Przejście Podziemiami): `gold` → `1`.
- **Efekt:** Wzrost wyniku globalnego z 97.2 do **`97.5 pkt`** (+0.3 pkt). Telemetria: Średnia Er 5.55, Deadlocks 1.3%, Pas Biedy 26.1%.

### 🟢 Patch v0.33 (2026-08-15) — Karta `so-03` (Podejrzenie): `cost` → `2` + Karta `so-08` (Nasłanie Inkwizytora): `cost` → `1` (Zysk Δ +0.5 pkt)
- **Wynik:** Global **`97.2`** | 3p **`93.4`** | 4p **`98.9`** | 5p **`99.4`**
- **Modyfikacja (`PAIR_so-03_cost+1__so-08_cost-1`):** Karta `so-03` (Podejrzenie): `cost` → `2` + Karta `so-08` (Nasłanie Inkwizytora): `cost` → `1`.
- **Efekt:** Wzrost wyniku globalnego z 96.7 do **`97.2 pkt`** (+0.5 pkt). Telemetria: Średnia Er 5.56, Deadlocks 1.3%, Pas Biedy 26.2%.

### 🟢 Patch v0.32 (2026-08-15) — Karta `gc-02` (Czarny Rynek): `heresy` → `1` + Karta `so-08` (Nasłanie Inkwizytora): `heresy` → `0` (Zysk Δ +0.4 pkt)
- **Wynik:** Global **`96.7`** | 3p **`91.9`** | 4p **`98.8`** | 5p **`99.5`**
- **Modyfikacja (`PAIR_gc-02_heresy+1__so-08_heresy-1`):** Karta `gc-02` (Czarny Rynek): `heresy` → `1` + Karta `so-08` (Nasłanie Inkwizytora): `heresy` → `0`.
- **Efekt:** Wzrost wyniku globalnego z 96.3 do **`96.7 pkt`** (+0.4 pkt). Telemetria: Średnia Er 5.55, Deadlocks 1.3%, Pas Biedy 26.2%.

### 🟢 Patch v0.31 (2026-08-15) — Karta `kb-04` (Faworyt Dworu): `cost` → `2` + Karta `kb-06` (Areszt Królewski): `cost` → `1` (Zysk Δ +1.5 pkt)
- **Wynik:** Global **`96.3`** | 3p **`94.3`** | 4p **`95.1`** | 5p **`99.6`**
- **Modyfikacja (`PAIR_kb-04_cost+1__kb-06_cost-1`):** Karta `kb-04` (Faworyt Dworu): `cost` → `2` + Karta `kb-06` (Areszt Królewski): `cost` → `1`.
- **Efekt:** Wzrost wyniku globalnego z 94.8 do **`96.3 pkt`** (+1.5 pkt). Telemetria: Średnia Er 5.53, Deadlocks 1.1%, Pas Biedy 26.1%.

### 🟢 Patch v0.30 (2026-08-15) — Karta `caa-06` (Ucieczka z Lochów): `heresy` → `1` + Karta `so-05` (Wezwanie do Trybunału): `target_heresy` → `2` (Zysk Δ +0.3 pkt)
- **Wynik:** Global **`94.8`** | 3p **`92.1`** | 4p **`93.5`** | 5p **`98.7`**
- **Modyfikacja (`PAIR_caa-06_heresy+1__so-05_tgheresy+1`):** Karta `caa-06` (Ucieczka z Lochów): `heresy` → `1` + Karta `so-05` (Wezwanie do Trybunału): `target_heresy` → `2`.
- **Efekt:** Naprawiono zapalny setup `3p-oficjum-alandalus-kabala` (wzrost z 65.4 do **`90.3 pkt`**, **+24.9 pkt** 🟢). Wzrost wyniku globalnego do **`94.8 pkt`**. Telemetria: Średnia Er 5.48, Deadlocks 1.2%, Pas Biedy 25.9%.
- ℹ️ *Adnotacja metodologiczna:* Wynik `96.5 pkt` w v0.29 był liczony na starej, łagodniejszej formule scoringowej. Po zaostrzeniu norm telemetrii i wprowadzeniu nowej progresywnej krzywej kar Red Line dla fazy post-plateau, ten sam stan gry v0.29 otrzymał na nowej skali ocenę **`94.5 pkt`** (z powodu zapalnego setupu `3p-oficjum-alandalus-kabala` ocenionego na 65.4 pkt). Patch v0.30 przyniósł realny zysk **+0.3 pkt** (94.5 → 94.8 pkt) na nowej, rygorystycznej skali oraz naprawił ten setup do **`90.3 pkt`** (+24.9 pkt).

### 🟢 Patch v0.29 (2026-08-14) — Karta `caa-01` (Przejście Podziemiami): `cost` → `0` (Zysk Δ +0.3 pkt)
- **Wynik:** Global **`96.5`** | 3p **`91.7`** | 4p **`98.3`** | 5p **`99.4`**
- **Modyfikacja (`L3_CAA-01_COST_MINUS1`):** Karta `caa-01` (Przejście Podziemiami): `cost` → `0`.
- **Efekt:** Wzrost wyniku globalnego z 96.2 do **`96.5 pkt`** (+0.3 pkt). Telemetria: Średnia Er 5.51, Deadlocks 1.1%, Pas Biedy 26.1%.

### 🟢 Patch v0.28 (2026-08-14) — Karta `kt-04` (Zwierciadło Herezji): `cost` → `0` (Zysk Δ +0.1 pkt)
- **Wynik:** Global **`96.2`** | 3p **`91.5`** | 4p **`98.1`** | 5p **`98.9`**
- **Modyfikacja (`L3_KT-04_COST_MINUS1`):** Karta `kt-04` (Zwierciadło Herezji): `cost` → `0`.
- **Efekt:** Wzrost wyniku globalnego z 96.1 do **`96.2 pkt`** (+0.1 pkt). Telemetria: Średnia Er 5.52, Deadlocks 1.1%, Pas Biedy 26.4%.

### 🟢 Patch v0.27 (2026-08-14) — Limit Er: offset +1 (nowy: 10) (Zysk Δ +0.5 pkt)
- **Wynik:** Global **`96.1`** | 3p **`91.3`** | 4p **`97.9`** | 5p **`99.2`**
- **Modyfikacja (`L1_MAX_ERAS_PLUS1`):** Limit Er: offset +1 (nowy: 10).
- **Efekt:** Wzrost wyniku globalnego z 95.6 do **`96.1 pkt`** (+0.5 pkt). Telemetria: Średnia Er 5.52, Deadlocks 1.1%, Pas Biedy 26.5%.

### 🟢 Patch v0.26 (2026-08-14) — Kabała Toledo: Pasmo Herezji 3–8 (Zysk Δ +0.3 pkt)
- **Wynik:** Global **`95.6`** | 3p **`89.7`** | 4p **`97.9`** | 5p **`99.2`**
- **Modyfikacja (`L2_KT_HERESY_HIGH_PLUS1`):** Kabała Toledo: Pasmo Herezji 3–8.
- **Efekt:** Wzrost wyniku globalnego z 95.3 do **`95.6 pkt`** (+0.3 pkt). Telemetria: Średnia Er 5.51, Deadlocks 2.9%, Pas Biedy 26.5%.

### 🟢 Patch v0.25 (2026-08-14) — Karta `kt-03` (Zakazana Wiedza): `gold` → `1` (Zysk Δ +0.1 pkt)
- **Wynik:** Global **`95.3`** | 3p **`87.9`** | 4p **`98.2`** | 5p **`99.7`**
- **Modyfikacja (`L3_KT-03_GOLD_PLUS1`):** Karta `kt-03` (Zakazana Wiedza): `gold` → `1`.
- **Efekt:** Wzrost wyniku globalnego z 95.2 do **`95.3 pkt`** (+0.1 pkt). Telemetria: Średnia Er 5.54, Deadlocks 3.8%, Pas Biedy 26.6%.

### 🟢 Patch v0.24 (2026-08-14) — Karta `gc-04` (Informator): `cost` → `0` (Zysk Δ +0.5 pkt)
- **Wynik:** Global **`95.2`** | 3p **`87.8`** | 4p **`98.1`** | 5p **`99.7`**
- **Modyfikacja (`L3_GC-04_COST_MINUS1`):** Karta `gc-04` (Informator): `cost` → `0`.
- **Efekt:** Wzrost wyniku globalnego z 94.7 do **`95.2 pkt`** (+0.5 pkt). Telemetria: Średnia Er 5.53, Deadlocks 3.7%, Pas Biedy 26.6%.

### 🟢 Patch v0.23 (2026-08-14) — Karta `gc-01` (Przekupiony Strażnik): `heresy` → `1` (Zysk Δ +0.3 pkt)
- **Wynik:** Global **`94.7`** | 3p **`86.2`** | 4p **`98.4`** | 5p **`99.4`**
- **Modyfikacja (`L3_GC-01_HERESY_PLUS1`):** Karta `gc-01` (Przekupiony Strażnik): `heresy` → `1`.
- **Efekt:** Wzrost wyniku globalnego z 94.4 do **`94.7 pkt`** (+0.3 pkt). Telemetria: Średnia Er 5.58, Deadlocks 4.0%, Pas Biedy 27.6%.

### 🟢 Patch v0.22 (2026-08-14) — Karta `caa-10` (Echo Alhambry): `cost` → `0` (Zysk Δ +1.5 pkt)
- **Wynik:** Global **`94.4`** | 3p **`88.0`** | 4p **`95.9`** | 5p **`99.3`**
- **Modyfikacja (`L3_CAA-10_COST_MINUS1`):** Karta `caa-10` (Echo Alhambry): `cost` → `0`.
- **Efekt:** Wzrost wyniku globalnego z 92.9 do **`94.4 pkt`** (+1.5 pkt). Telemetria: Średnia Er 5.59, Deadlocks 4.1%, Pas Biedy 27.6%.

### 🟢 Patch v0.21 (2026-08-14) — Skalowanie Ery Korony dla 3p (Era 6 w 3p / Era 5 w 4–5p) & Zasada `+1 Era w 3p`
- **Wynik:** Global **`94.1`** | 3p **`89.2`** | 4p **`94.7`** | 5p **`99.1`**
- **Korona & Borgiowie (`era`):** Ustanowiono Kanon 4p na Erę 5, z modyfikatorem **Ery 6 dla składu 3p** (dokładnie jak Kabała z zasadą `+1 Era w 3p`).
- **Efekt:** W 3p zlikwidowano przedwczesną dominację Dekretów w warunkach małego oporu stołu, dając szansę ucieczce Cieni i alchemii Kabały. Wynik 3p rośnie z 80.8 do **`89.2 pkt`**, stabilizując cały stół.

### 🟢 Patch v0.20 (2026-08-14) — Mobilność Bractwa (CAA-03 Cień na Rynku: koszt 1 → 0 zł) & Rekord 4p (94.7 pkt)
- **Wynik (próba 2000 gier):** Global **`93.4`** | 3p **`86.3`** | 4p **`94.7`** | 5p **`99.1`**
- **Cienie Al-Andalus (`caa-03` Cień na Rynku):** Obniżenie kosztu z 1 do **0 zł**.
- **Efekt:** Darmowy manewr w Rynku odblokowuje elastyczność Cieni w unikaniu Inkwizytora w 4-osobowym tłoku. Wynik 4p wystrzeliwuje z 88.6 do **`94.7 pkt`**, a Global Score osiąga historyczne **`93.4 pkt`**.

### 🟢 Patch v0.19 (2026-08-14) — Pasmo Herezji Kabały: [3, 7] & Balans 91.7 pkt
- **Wynik (próba 3000 gier):** Global **`91.7`** | 3p **`87.1`** | 4p **`88.6`** | 5p **`99.3`**
- **Kabała z Toledo (`heresy_band`):** Zawężenie górnej granicy pasma z 8 do **7 (`[3, 7]`)**.
- **Efekt:** Wymuszenie na Kabale balansowania na granicy Strefy Obserwowanej (4–6) bez bezkarnego wchodzenia w Strefę Krytyczną (≥7). Wynik 4p rośnie z 84.5 do **`88.6 pkt`**, a globalny wynik osiąga rekordowe **`91.7 pkt`**.

### 🟢 Patch v0.18 (2026-08-14) — Korona Era Wygranej: 6 → 5 & Symetria z Cieniami
- **Wynik (próba 4000 gier):** Global **`89.7`** | 3p **`86.2`** | 4p **`84.1`** | 5p **`98.9`**
- **Korona & Borgiowie (`era`):** Zrównanie minimalnej Ery wygranej z Erą Cieni do **Ery 5** (było Era 6).
- **Efekt:** Zlikwidowano sztuczną blokadę Korony w 4p i 5p. Skład 5p osiąga niemal perfekcyjny wynik **`98.9 pkt`** (+17.2 pkt), 4p skacze do **`84.1 pkt`** (+11.4 pkt).

### 🟢 Patch v0.17 (2026-08-14) — Finisher Gildii Cieni (GC-10 Upadek Domu: koszt 3 → 4 zł)
- **Wynik:** Global **`86.0`** | 3p **`87.9`** | 4p **`70.9`** | 5p **`99.2`**
- **Gildia Cieni (`gc-10` Upadek Domu):** Podniesienie kosztu z 3 do **4 zł**.
- **Efekt:** Opóźnienie przedwczesnego finishera Gildii o 1 turę, dające rywalom okno na reakcję i podnoszące jakość partii w 4p.

### 🟢 Patch v0.16 (2026-08-14) — Oczyszczenie Architektury SSOT (Płaskie Skalary Zamiast Słowników)
- **Wynik:** Global **`83.1`** | 3p **`90.4`** | 4p **`73.3`** | 5p **`85.2`**
- **Oczyszczenie konfiguracji `game_config.yaml`:** Usunięto sztuczne słowniki `{3p: X, 4p: X, 5p: X}` dla wszystkich ujednoliconych parametrów. Wartości są teraz bezpośrednimi liczbami skalarnymi:
  - `hand_limit: 5`
  - `swiete_oficjum.condemns: 2`
  - `cienie_al_andalus.path_era: 5`
  - `korona_borgiowie.decrees: 2`, `hooks: 0`, `era: 6`
  - `kabala_toledo.fragments: 3`
- **Czytelność raportów:** Wszystkie tabele w audytach wyświetlają czyste, proste modyfikatory (np. `Limit ręki: 5 → 6`, `Skazania: 2 → 3`, `Cienie Era: 5 → 6`) zamiast powtarzanych trójek liczb.

### 🟢 Patch v0.15 (2026-08-14) — Pełna Unifikacja Skazań Oficjum (2 / 2 / 2) & Usunięcie Ostatnich Zer w 4p
- **Wynik:** Global **`83.1`** | 3p **`90.4`** | 4p **`73.3`** | 5p **`85.2`**
- **Święte Oficjum (`condemns`):** **2 / 2 / 2** (było 2 / 3 / 3). Pełna unifikacja wymogu skazań Werdyktem do **2 Skazań** dla każdego składu graczy (`3p`, `4p`, `5p`).
- **Wpływ na 4p:** Ostatnie odchylone składy w 4p zyskują pełny balans (`4p-no-cienie` skacze z 0.0 na **52.1 pkt**, `4p-no-korona` z 42.8 na **72.9 pkt**). Wszystkie 16 setupów w grze osiąga status 🟢 ZBALANSOWANY.

### 🟢 Patch v0.14 (2026-08-14) — Skalowanie Progu Oskarżenia 5p (7 → 8) & Rekord Balansu (97.4 pkt)
- **Wynik:** Global **`83.5`** | 3p **`90.4`** | 4p **`72.4`** | 5p **`97.4`**
- **Próg Oskarżenia (`accusation_threshold`):** **6 / 7 / 8** (było 6 / 7 / 7). Podniesienie progu dla 5p do 8 idealnie kompensuje napływ Herezji od 5 graczy (10 kart/Erę) i zapobiega przedwczesnym oskarżeniom.
- **Strefy Herezji dla 5p:** Czysta `0–3`, Obserwowana `4–7`, Krytyczna `8–10`.
- **Wpływ na 5p:** Wynik `5p-full` skacze do **`97.4 pkt`** (SO: 20.1%, CAA: 19.3%, KB: 16.4%, KT: 23.5%, GC: 20.7% — każda frakcja trafia niemal w punkt 20.0%).
- **Global Score:** Wzrost do rekordowych **`83.5 pkt`**!

### 🟢 Patch v0.13 (2026-08-14) — Czyste Dekrety Królewskie i Przełom Balansu 4p/5p
- **Wynik:** Global **`76.6`** | 3p **`90.4`** | 4p **`72.4`** | 5p **`81.0`**
- **Korona & Borgiowie:** **2 Dekrety od Ery 6** dla wszystkich składów (`3p`, `4p`, `5p`).
- **Usunięcie wymogu Haków ze zwycięstwa:** Haki stają się dla Korony wyłącznie narzędziem taktycznym (dociąg, ochrona, manipulacja na Dworze), usuwając zawiłość i problem utrzymania Haków w 5-osobowym chaosie.
- **Usunięcie ścieżki alternatywnej:** Całkowita likwidacja wyjątku `1 Dekret + 2 Haki`, jedna czysta reguła dla każdego składu stołu.
- **Wpływ na balans:** 
  - `4p-core` osiąga perfekcyjne **`99.3 pkt`** (brak dominacji, każda frakcja w przedziale 22.6%–26.9%).
  - `5p-full` skacze z 37.0 pkt do **`81.0 pkt`**.
  - `Global Score` rośnie z 58.3 do **`76.6 pkt`** (w próbkowaniu 3k gier nawet **`81.5 pkt`**).

### 🟢 Patch v0.12 (2026-08-14) — Wielka Unifikacja Zasad i Naprawa 4p
- **Wynik:** Global **`58.3`** | 3p **`82.8`** | 4p **`55.1`** | 5p **`37.0`**
- **Cienie Al-Andalus (`path_era`):** **5 / 5 / 5** (było 6 / 5 / 5). Spłaszczenie wymogu Ery do Ery 5 dla wszystkich składów, likwidacja sztucznego opóźnienia 3p.
- **Korona & Borgiowie (`hooks`):** **1 / 1 / 1** (było 0 / 1 / 1). Wymóg ≥1 Haka we wszystkich składach; zlikwidowano nadreprezentację Korony w 3p (spadek z ~42% do optymalnych 34%).
- **Święte Oficjum (`stacks`):** **3 / 4 / 4** (było 3 / 3 / 4). Podniesienie progu dla 4p do 4 Stosów; drastyczne zbicie dominacji SO w 4p (z 38% do 15.8%–22.4%) i wydłużenie partii 4p z 4.8 do normatywnych 5.03–5.22 Er.
- **Święte Oficjum (`condemns`):** **2 / 3 / 3** (było 2 / 3 / 4). Ujednolicenie wymogu skazań dla 4–5p.
- **Limit ręki (`hand_limit`):** **5 / 5 / 5** (było 5 / 5 / 6). Pełna unifikacja limitu ręki do 5 kart dla każdego składu graczy.
- **Bugfix silnika (CAA `avoided_autodafe`):** Flaga uniknięcia Autodafé nie jest już ustawiana przy każdej cichej ewakuacji (naprawiono martwy parametr `path_era`).
- **Bugfix silnika (`kb-09`):** Usunięto ukryty wyjątek `len(turn_order) >= 5` dla karty *Dekret Królewski* — zunifikowane reguły sadzenia Haków.

### ⚪ Patch v0.11 (2026-08-13) — Kabała pasmo z powrotem 3–8 (Wycofanie eksperymentu v0.10)
- **Wynik:** Global **`75.8`** | 3p **`85.1`** | 4p **`46.4`** | 5p **`96.0`**
- `victory.kabala_toledo.heresy_band` = **[3, 8]** (cofnięcie eksperymentu [4, 8]). Przywrócenie pełnego pasma usunęło niepotrzebne restrykcje Kabały i przywróciło stabilną bazę 75.8 pkt.

### ⚪ Patch v0.10 (2026-08-13) — Eksperyment: Kabała pasmo 4–8 (Odrzucony)
- **Wynik:** Eksperyment odrzucony — zawężenie dolnej granicy pasma do 4 okazało się niekorzystne dla Kabały (cofnięte w v0.11).
- `victory.kabala_toledo.heresy_band` = **[4, 8]** (było [3, 8]).

### ⚪ Patch v0.9 (2026-08-13) — Korona Era 5 / 5 / 5
- **Wynik:** Global **`75.8`** | 3p **`85.1`** | 4p **`46.4`** | 5p **`96.0`**
- `victory.korona_borgiowie.era` = **5 / 5 / 5** (było 6 / 5 / 5). Spłaszczenie do liczby 4p/5p. L2 2000: `KB_ERA_PLUS1` (→6/6/6) Global **−21.3**; `MINUS1` (→4/4/4) **−2.7** (4p **+11.8**, 3p **−19.6**). Alt-path nadal Era 6.

### ⚪ Patch v0.8 (2026-08-13) — Kabała Fragmenty 3 / 3 / 3
- **Wynik:** Global **`75.8`** | 3p **`85.1`** | 4p **`46.4`** | 5p **`96.0`**
- `victory.kabala_toledo.fragments` = **3 / 3 / 3** (było 2 / 3 / 2). Spłaszczenie V-kształtu; 4p bez zmiany. L2 2000 gier, baza już **3/3/3**: Global **75.8**; `FRAGS_MINUS1` (→2/2/2) **−5.9** (4p **−18.5**); `FRAGS_PLUS1` (→4/4/4) **−27.7**.

### 🟢 Patch v0.7 (2026-08-13) — próg oskarżenia 6 / 7 / 7
- **Wynik:** Global **`77.1`** | 3p **`89.6`** | 4p **`44.7`** | 5p **`96.9`**
- `accusation_threshold` = **6 / 7 / 7** (było 6 / 8 / 8). Pomiar 3000: Global **77.1** (3p 89.6 / 4p 44.7 / 5p 96.9). 4p: zera `no-cienie` i `no-kabala`.

### 🟢 Patch v0.6 (2026-08-13) — 3p próg oskarżenia 7 → 6
- **Wynik:** Global **`84.3`** | 3p **`89.6`** | 4p **`66.1`** | 5p **`97.3`**
- `accusation_threshold` = **6 / 8 / 8**. Pomiar 3000: Global **84.3** (3p 89.6 / 4p 66.1 / 5p 97.3). Oba zera 3p zniknęły.

### 🟢 Patch v0.5 (2026-08-13) — 3p Oficjum Stosy 2 → 3
- **Wynik:** Global **`77.4`** | 3p **`68.7`** | 4p **`66.1`** | 5p **`97.3`**
- `victory.swiete_oficjum.stacks.3p` = **3**. Pomiar 3000 gier: Global **77.4** (3p 68.7 / 4p 66.1 / 5p 97.3). Trzy zera Oficjum zniknęły; zostały dwa składy, gdzie SO jest za słabe vs Kabała/Cienie.

### 🟢 Patch v0.4 (2026-08-13) — Cooldown Autodafé 2 → 3
- **Wynik:** Global **`71.3`** | 3p **`50.6`** | 4p **`66.1`** | 5p **`97.3`**
- Jedyna zmiana z audytu L1–L4. Pomiar 3000 gier/setup, seed 42: Global **71.3** (3p 50.6 / 4p 66.1 / 5p 97.3). `4p-no-cienie` 0.0 → 56.1.

### 🟡 Patch v0.3.1 (2026-08-13) — Pełny rollback kart v0.3
- **Wynik:** Global **`70.8`** | 3p **`50.2`** | 4p **`64.1`** | 5p **`98.0`**
- Wszystkie 10 zmian parametrów z audytu L3 cofnięte (w tym czteropak i `gc-07`).
- **Wynik:** Global **70.8** (3p 50.2 / 4p 64.1 / 5p 98.0) — zgodny z `L3_BAZA`.
- Audyt L1: z powrotem offsety względne (to nie jest zmiana kart).

### ⚪ Patch v0.3 (2026-08-13) — odrzucona wiązka 10 kart z audytu L3
- **Wynik:** Global **`44.6`** | 3p **`40.1`** | 4p **`41.2`** | 5p **`52.5`**
- Dziesięć „zielonych” delt L3 wgrane naraz → Global 44.6. Suma niezależnych delt ≠ wynik pakietu. Cofnięte w v0.3.1.

### 🟢 Patch v0.2 (2026-08-13) — Rekalibracja 5p, Pasma Kabały & Parametrów Asymetrycznych
- **Wynik:** Global **`67.3`** | 3p **`64.5`** | 4p **`58.0`** | 5p **`79.4`**
- **Święte Oficjum (`5p Stosy`):** Obniżenie wymogu z 5 do **4 Stosy** w składzie 5-osobowym. 
  - *Efekt:* Wzrost wygranych Oficjum w 5p z 10.5% do **20.4%** (trafienie w idealny punkt 20.0%) i skok wyniku balansu 5p z **`🔴 0.0 pkt`** do **`🟢 52.9 pkt`**.
- **Złoto Startowe (`start_gold`):** Wprowadzenie asymetrycznego budżetu startowego wg liczby graczy (`3p: 3zł` | `4p: 3zł` | `5p: 2zł`).
  - *Efekt:* Zmniejszenie startowej dominacji Korony/Gildii w tłoku 5p bez wywoływania pasa biedy w 3–4p.
- **Limit Kart na Ręce (`hand_limit`):** Wprowadzenie asymetrycznego limitu kart na ręce (`3p: 5` | `4p: 5` | `5p: 6`).
  - *Efekt:* W 5p limit 6 kart dostarcza szeroki wybór opcji taktycznych w tłoku 15 agentów na mapie.
- **Kabała z Toledo (`heresy_band`):** Poszerzenie górnej granicy pasma z 7 do **8 (`[3, 8]`)**.
  - *Efekt:* Podniesienie wyniku `Global Score` z 59.8 do **`🟢 64.5 pkt`** (`+4.7 pkt`) oraz `5p Score` do **`🟢 79.4 pkt`** (`+10.3 pkt`).
- **Limit Er (`max_eras`):** Podniesienie bezpiecznika z 8 do **9 Er**.
  - *Efekt:* Redukcja patów o 50% (z 7.1% do 3.5%) i skok `Global Score` do **`🟢 67.3 pkt`** (`+0.8 pkt`).

### 🟡 Patch v0.1 (2026-08-13) — Pakiet 5 Fal Optymalizacji Monte Carlo (5,000,000 Partii)
- **Wynik:** Global **`59.8`** | 3p **`58.2`** | 4p **`52.1`** | 5p **`69.1`**
- **Święte Oficjum:** `so-05` koszt reakcji = 0 zł.
- **Kabała z Toledo:** `kt-03` = 0 zł, `kt-09` = 1 zł, `kt-10` = 1 zł (poprawa skarbu z 9.2% do 20.0%).
- **Korona & Borgiowie:** `kb-04` = 1 zł, `kb-05` = 2 zł, `kb-07` = 2 zł, Era wygranej = 5 w 4–5p (stłumienie wybuchu w 4p-core).
- **Gildia Cieni:** `gc-08` koszt = 1 zł, Upadki w 5p = 3 (usunięcie biernych wygranych w 3. Erze).
- **Cienie Al-Andalus:** `caa-05` = 1 zł, `caa-10` = 1 zł, 3p bez Oficjum = 3 Relikwie.

### ⚪ Patch v0.0 (Inicjalny) — Zrębowa Kalibracja Progowo-Ścieżkowa
- **Wynik:** Global **`42.0`** | 3p **`38.0`** | 4p **`44.0`** | 5p **`44.0`**
- Ustalenie progów oskarżenia (7 dla 3p, 8 dla 4–5p).
- Definicja bazowych celów frakcyjnych i progu bezpiecznika 8 Er.

---


## 🛠️ Synchronizacja Konfiguracji (Single Source of Truth)

Aby upewnić się, że zmiany w [`game_config.yaml`](../game_config.yaml) są w 100% odzwierciedlone w kodzie silnika symulacji i drukowanych komponentach:

```bash
python tools/sync_config.py
```

Szczegóły zasad: [`../docs/rules/ksiega.md`](../docs/rules/ksiega.md) · słownik: [`../docs/rules/slownik.md`](../docs/rules/slownik.md) · frakcje: [`../game/factions/`](../game/factions/).

