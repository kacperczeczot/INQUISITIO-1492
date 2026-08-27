# Changelog — INQUISITIO 1492: Cienie Toledo

Wszystkie istotne zmiany w tym projekcie są dokumentowane w tym pliku.

Format oparty na [Keep a Changelog](https://keepachangelog.com/pl/1.1.0/).
Wersjonowanie zgodne z [Semantic Versioning](https://semver.org/lang/pl/).

---

## [Unreleased]

---

## [v1.0-alpha] — trwa

> Aktywna faza alpha-playtestingu i optymalizacji balansu Monte Carlo.
> Historia szczegółowych patchów balansu znajduje się w [`data/playtesting/balance-notes.md`](data/playtesting/balance-notes.md).

### Added
- Symulator Monte Carlo w Pythonie (`src/`) z modułem natywnym C++ (`src/native/`)
- Pełen zestaw 50 kart podzielony na 4 frakcje + talia czasu
- Rejestr 16 Decyzji Architektonicznych (ADR-0001 – ADR-0016) w `docs/adr/`
- Narzędzia audytorskie: `scripts/sim/audytor_3p.py`, `audytor_4p.py`, `audytor_5p.py`, `audytor_kanonu.py`
- Generator PnP kart (`scripts/pnp/`)
- Mechanizm SSOT: `data/game_config.yaml` → synchronizowany przez `scripts/sync_config.py`
