[Strona główna](../../../../../README.md) > [v1.0-alpha.2](README.md) > [kandydaci_recznej_ablacji](kandydaci_recznej_ablacji.md)

---

# Kandydaci do ręcznej ablacji — Kanon 4P (v1.0-alpha.2)

**Wersja:** `v1.0-alpha.2` | **Patchy w sesji:** 1

Lista diagnostyczna — **audytor nie usuwa mechanik automatycznie**. Każdy punkt wymaga ręcznej decyzji po `feature_impact_4p.py` lub redesignie reguł.

| Priorytet | Kategoria | Setup | Problem | Rekomendacja ręczna |
| :---: | :--- | :--- | :--- | :--- |
| ŚREDNIA | TOKSYCZNA_TELEMETRIA | `4p-core` | **Deadlocki powyżej progu zdrowia stołu** — Paraliż Gry / Deadlocks 7.5% (>5%) | Ręcznie: sprawdź limity Er, stosy i tempo gry. Nie obniżaj progów zwycięstwa jako protezy — to decyzja projektowa. |