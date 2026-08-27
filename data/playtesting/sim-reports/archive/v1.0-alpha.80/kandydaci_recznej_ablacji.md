# Kandydaci do ręcznej ablacji — Kanon 4P (v1.0-alpha.80)

**Wersja:** `v1.0-alpha.80` | **Patchy w sesji:** 0

Lista diagnostyczna — **audytor nie usuwa mechanik automatycznie**. Każdy punkt wymaga ręcznej decyzji po `feature_impact_4p.py` lub redesignie reguł.

| Priorytet | Kategoria | Setup | Problem | Rekomendacja ręczna |
| :---: | :--- | :--- | :--- | :--- |
| WYSOKA | Kastracja MECHANIKI | `4p-core` | **Mechanika frakcji praktycznie nie żyje przy stole** — Zanikanie Haków Korony (0.00/partię) | Ręcznie: sprawdź koszty, warunki kart i AI — czy mechanika jest zablokowana regułą. Usunięcie systemu tylko po potwierdzeniu ablacją. |
| WYSOKA | Kastracja MECHANIKI | `4p-no-cienie` | **Mechanika frakcji praktycznie nie żyje przy stole** — Zanikanie Infiltracji Gildii Cieni | Ręcznie: sprawdź koszty, warunki kart i AI — czy mechanika jest zablokowana regułą. Usunięcie systemu tylko po potwierdzeniu ablacją. |
| WYSOKA | TOKSYCZNA_TELEMETRIA | `4p-core` | **Deadlocki powyżej progu zdrowia stołu** — Paraliż Gry / Deadlocks 48.0% (>5%) | Ręcznie: sprawdź limity Er, stosy i tempo gry. Nie obniżaj progów zwycięstwa jako protezy — to decyzja projektowa. |