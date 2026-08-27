[Strona główna](../README.md) > [docs](README.md) > [AUDYTOR_KANONU](AUDYTOR_KANONU.md)

---

# 🎯 Audytor Kanonu 4P (Anchor-Based 4P Optimizer) — Instrukcja Użytkownika

**Audytor Kanonu 4P** (`tools/sim/audytor_kanonu.py`) to specjalistyczny optymalizator balansu gry **INQUISITIO-1492**, skupiony w 100% na doprowadzeniu **kanonicznej rozgrywki 4-osobowej (4P)** do absolutnego optimum (99–100 pkt), bez wprowadzania sztucznych kompromisów pod 3p i 5p.

---

## 🧠 Dlaczego Kotwica Kanonu 4P (Anchor Theory)?

1. **Eliminacja Kompromisów Psujących Grę:**
   * Globalny optymalizator próbujący dogodzić 3p, 4p i 5p naraz często wprowadzał nienaturalne zmiany kart (np. zawyżał koszt kluczowej karty), by sztucznie podciągnąć słaby setup w 3p.
   * Audytor Kanonu 4P optymalizuje **wyłącznie 5 kanonicznych setupów 4-osobowych**:
     `4p-core`, `4p-no-cienie`, `4p-no-kabala`, `4p-no-korona`, `4p-no-oficjum`.
2. **Obnażanie Realnych Anomalii 3p i 5p:**
   * Doprowadzenie 4P do perfekcji tworzy **nieskazitelny punkt odniesienia**.
   * Po każdym patchu skrypt wykonuje pomiar kolateralny na 3p i 5p. Wyjątki formatu zapisują **tylko** `audytor_3p.py` / `audytor_5p.py` pod kluczami `3p:` / `5p:` — nie skalują kanonu 4P „na wszelki wypadek”.

---

## ⚡ 3-Stopniowy Błyskawiczny Lejek Selekcji (5 setupów)

Dzięki badaniu 5 setupów (zamiast 16), Audytor Kanonu 4P działa ponad **3-krotnie szybciej**:

1. **Etap 1: Szybki Przesiew Zgrubny (~30 sekund):**
   - Bada ~350 kandydatów atomowych na próbie **200 gier / setup** ($\times 5$ setupów).
   - Wyłania **TOP 48 Półfinalistów**.
2. **Etap 2: Głęboki Przesiew (~4 sekundy):**
   - Bada TOP 48 na próbie **1 000 gier / setup**.
   - Wyłania **TOP 24 Finalistów**.
3. **Etap 3: Weryfikacja Ultra (~18 sekund):**
   - Bada TOP 24 na próbie **5 000 gier / setup (25 000 gier per wariant)** z użyciem *Common Random Numbers (CRN)*.
   - Wdraża zwycięski patch, mierzy wpływ na 3p i 5p, archiwizuje raporty i aktualizuje dokumentację.

---

## 🚀 Przykłady Uruchomienia z Terminala

```bash
# 1. Sesja ciągła na określony czas (np. 2 godziny):
sim/.venv/bin/python tools/sim/audytor_kanonu.py --hours 2.0

# 2. Działanie do osiągnięcia optimum (lub do naciśnięcia Ctrl+C):
sim/.venv/bin/python tools/sim/audytor_kanonu.py

# 3. Ograniczenie do zadanej liczby udanych patchów (np. 3 patche):
sim/.venv/bin/python tools/sim/audytor_kanonu.py --max-iters 3

# 4. Tryb symulacyjny (Dry-Run — diagnostyka bez zapisu):
sim/.venv/bin/python tools/sim/audytor_kanonu.py --dry-run
```

---

## 📊 Automatycznie Generowane Raporty i Archiwa

Po każdym wdrożonym patchu Audytor Kanonu 4P automatycznie tworzy i aktualizuje:

1. **`playtesting/sim-reports/archive/{wersja}/canon_4p_log.md`:** Pełny dziennik iteracji i zmian wyników 4p, 3p, 5p i global.
2. **`playtesting/sim-reports/archive/{wersja}/raport_optymalizacji_kanonu.md`:** Szczegółowy raport z rankingiem finalistów i diagnostyką wpływu kolateralnego.
3. **`playtesting/sim-reports/archive/{wersja}/raport_telemetrii.md`:** Pełny raport telemetrii 5 filarów dla 16 setupów (ze snapshotem `game_config.yaml`).
4. **`playtesting/balance-notes.md`:** Dodanie oficjalnej notatki patcha z datą, zyskiem i telemetrią.
5. **Księga zasad, karta pomocy i edytor kart:** Pełna synchronizacja przez `tools/sync_config.py`.

Makro (`audytor_4p.py`) zapisuje lookahead 2D/3D na żywych `±1`. Poza apply: agenci (SKU), Werdykt Tajny, tempo Kroniki, ablacja. Jeździec Δ≈0 nie wchodzi. Patrz [`rules/hierarchia_balansowania.md`](rules/hierarchia_balansowania.md) §0.

---

## Audytory makro i formatu (wolno odpalać)

`audytor_kanonu.py` = karty 4P. `audytor_4p.py` = skalary kanonu 4P (w tym Obserwowana, karty/erę, Gospodarcza, Er).  
`audytor_3p.py` / `audytor_5p.py` = **tylko** wyjątki `3p:` / `5p:` (próg oskarżenia, złoto startowe, L2). Nie zapisują gałek całego stołu.

```bash
# bez zapisu YAML
sim/.venv/bin/python tools/sim/audytor_4p.py --workers 10 --dry-run
sim/.venv/bin/python tools/sim/audytor_3p.py --workers 10 --dry-run
sim/.venv/bin/python tools/sim/audytor_5p.py --workers 10 --dry-run
```

Bez `--dry-run` 4P podbija wersję SSOT; 3p/5p podbijają wersję, ale zostawiają kanon 4P nietknięty.
