[Strona główna](../README.md) > [Dokumentacja](README.md) > [Standardy](STANDARDS.md)

---

# Standardy Inżynieryjne Projektu — INQUISITIO 1492

Niniejszy projekt przestrzega globalnych standardów zdefiniowanych w **[devex-standards](https://github.com/kacperczeczot/devex-standards)**.

---

## 1. Zgodność ze Standardami Zewnętrznymi

| Standard | Implementacja w Projekcie | Oficjalna Specyfikacja |
| :--- | :--- | :--- |
| **Conventional Commits** | Commitlint + Husky | [conventionalcommits.org](https://www.conventionalcommits.org/pl/v1.0.0/) |
| **Semantic Versioning** | SemVer wewnętrzny (`v1.0-alpha.X`) w `data/game_config.yaml` | [semver.org](https://semver.org/lang/pl/) |
| **Keep a Changelog** | [`CHANGELOG.md`](../CHANGELOG.md) wg specyfikacji 1.1.0 | [keepachangelog.com](https://keepachangelog.com/pl/1.1.0/) |
| **ADR** | Rejestr w [`docs/adr/`](adr/README.md) (ADR-0001 do ADR-0016+) | [adr.github.io](https://adr.github.io/) |

---

## 2. Pokrycie Testami i Bramki Jakości

Projekt stosuje weryfikację Monte Carlo jako główną metodę walidacji balansu:

- **Symulacje Monte Carlo:** ≥ 50 000 partii per konfiguracja testowa
- **Win-rate bramka:** Maksymalna odchyłka frakcji od 25% (4P) ≤ ±3 pp
- **Złote okno rozgrywki:** ≥ 65% gier kończy się w Erach 5–7 (ADR-0004)
- **Testy jednostkowe:** 100% PASSED (`src/.venv/bin/pytest`)

---

## 3. Nadrzędne Źródło Prawdy (SSOT)

| Warstwa | Lokalizacja |
| :--- | :--- |
| Parametry gry | `data/game_config.yaml` |
| Reguły AI | `.agents/rules/project.md` |
| Decyzje architektoniczne | `docs/adr/` |
| Globalne standardy DevEx | [devex-standards](https://github.com/kacperczeczot/devex-standards) |
