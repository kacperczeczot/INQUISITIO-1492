[Strona główna](../../README.md) > [adr](README.md) > [0014-standardy-proby-statystycznej-i-wieloseedowej](0014-standardy-proby-statystycznej-i-wieloseedowej.md)

---

# ADR-0014: Standardy Próby Statystycznej i Walidacja Wieloseedowa

* **Status:** ACCEPTED
* **Data:** 2026-08-23
* **Autorzy:** Antigravity & Designer
* **Dotyczy:** `tools/sim/`, `sim/inquisitio/runner/`, `playtesting/`

---

## 1. Kontekst Problemu
Testowanie hipotez na małych próbach (np. 100–500 partii) lub na pojedynczym ziarnie losowości (seedzie) prowadziło do fałszywych wniosków o balansie – algorytm optymalizował układ pod konkretny rozkład losowy (seed overfitting).

---

## 2. Decyzja Projektowa
1. **Standardy Wielkości Próby:**
   - **Przesiew Wstępny (Szybka weryfikacja):** $\ge 1\,000$ partii per setup.
   - **Finalny Pomiar / Raport Wydania (Release Report):** $\ge 10\,000$ partii per setup (łącznie $\ge 50\,000$ partii dla Kanonu 4P).
2. **Obowiązkowa Walidacja Wieloseedowa (Cross-Seed Validation):**
   - Każda zmiana parametrów przed wdrożeniem musi zostać sprawdzona na co najmniej 2 niezależnych ziarnach losowości (np. `seed 42` i `seed 10041`).
   - Zmiana zostaje uznana za stabilną tylko wtedy, gdy wykazuje zysk balansu na obu ziarnach.

---

## 3. Szczegółowe Uzasadnienie (Data Science & Telemetria)
* **Eliminacja szumu statystycznego:** Przy 10 000 gier błąd statystyczny pomiaru win-share spada poniżej $\pm 0.5\%$.
* **Odporność na anomalie:** Eliminacja przypadkowych zwycięstw wynikających z anomalnego dociągu kart w pierwszych turach.

---

## 4. Niezmienniki Architektoniczne (Invariants)
* 🛑 **ZAKAZ:** Generowania oficjalnych raportów archiwalnych na próbach mniejszych niż 5000 gier per setup.
* 🛡️ **GWARANCJA:** Wszystkie raporty telemetryczne w `playtesting/sim-reports/` bazują na próbach rzędu 10 000 gier/setup.

---

## 5. Konsekwencje
* Stabilne, w 100% powtarzalne wyniki audytu balansu.
