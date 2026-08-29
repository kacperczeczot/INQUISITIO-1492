# INQUISITIO-1492 — Systemowe Instrukcje i Dyscyplina Agenta

Ten dokument (`AGENTS.md`) jest automatycznie ładowany na początku każdej sesji i konwersacji w tym repozytorium. Każdy agent, model i asystent ma **bezwzględny obowiązek** przestrzegać poniższych reguł:

---

## 1. 🛑 Zero Samowolki (Bezwzględny Tryb Konsultacyjny)
* **Zakaz wprowadzania zmian w plikach bez wyraźnego polecenia:** Asystent NIE MA PRAWA modyfikować `data/game_config.yaml`, kodu silnika (`src/`), kart w `docs/` ani logiki decyzyjnej w odpowiedzi na luźne pytanie, hipotezę czy dyskusję.
* **Forma odpowiedzi:** Na pytania o balans, mechaniki i pomysły asystent odpowiada **WYŁĄCZNIE analizą, danymi z symulacji i propozycjami wariantów**.
* **Warunek edycji:** Zmiana plików następuje WYŁĄCZNIE po jednoznacznym poleceniu użytkownika (np. *„zmień”*, *„zastosuj”*, *„podbij wersję”*).

---

## 2. 🧪 Izolacja Badań i Zakaz Pętli na Żywym Archiwum
* Wszelkie testy „na sucho”, grid-search parametrów czy strojenie wag AI **MUSZĄ** działać w pamięci lub w odizolowanym folderze `scratch/`.
* **Kategoryczny zakaz nadpisywania oficjalnych raportów w `data/playtesting/sim-reports/archive/`** bez wcześniejszego formalnego podbicia wersji w `game_config.yaml`.
* Każda wersja w `archive/v1.0-alpha.X/` jest **niezmiennym snapshotem** — raport telemetrii i raport ablacji muszą być zawsze w 100% zsynchronizowane z tym samym stanem silnika.

---

## 3. ⚖️ Zgodność z Architekturą i Zasadami Projektu
* **Konstytucja ADR (`docs/adr/`):** Zakaz stosowania sztucznych blokad er (`if era < X`), ucinania talii czy psucia tożsamości frakcji. Balans musi wynikać w 100% z fizycznych mechanik gry.
* **Zasada Próby Minimalnej (ADR-0014):** Żaden oficjalny raport nie może być generowany ani zapisywany na próbie mniejszej niż **5 000 partii na setup** (dla pełnych raportów telemetrii: **10 000 partii na setup**).
* **Rygor Narzędziowy:** Zakaz używania komend powłoki typu `cat << EOF` do modyfikacji plików — wyłącznie natywne narzędzia edycyjne IDE.

---

## 4. 📂 Szczegółowy Rejestr Reguł
Wszystkie reguły szczegółowe znajdują się w katalogu `.agents/rules/`:
* [Dyscyplina Agenta i Zero Samowolki](.agents/rules/dyscyplina_agenta_i_zero_samowolki.md)
* [Organiczne Balansowanie i Integralność Silnika](.agents/rules/balansowanie.md)
* [Edycja Konfiguracji i SSOT](.agents/rules/edycja_konfiguracji.md)
* [Antidotum na Antywzorce Audytora](.agents/rules/antidote_antypatterns_audytora.md)
