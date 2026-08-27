[Strona główna](../../../../../README.md) > [v0.99.12](README.md) > [kandydaci_recznej_ablacji](kandydaci_recznej_ablacji.md)

---

# Kandydaci do ręcznej ablacji — Kanon 4P (v0.99.12)

**Wersja:** `v0.99.12` | **Patchy w sesji:** 0

Lista diagnostyczna — **audytor nie usuwa mechanik automatycznie**. Każdy punkt wymaga ręcznej decyzji po `feature_impact_4p.py` lub redesignie reguł.

| Priorytet | Kategoria | Setup | Problem | Rekomendacja ręczna |
| :---: | :--- | :--- | :--- | :--- |
| ŚREDNIA | TOKSYCZNA_TELEMETRIA | `4p-core` | **Deadlocki powyżej progu zdrowia stołu** — Paraliż Gry / Deadlocks 5.5% (>5%) | Ręcznie: sprawdź limity Er, stosy i tempo gry. Nie obniżaj progów zwycięstwa jako protezy — to decyzja projektowa. |