# SCHEMA kart — prototyp intrygi

Frontmatter YAML + pełny opis efektu po `---`.

## Pola

| Pole | Typ | Opis |
| :--- | :--- | :--- |
| `id` | string | np. `so-01`, `caa-03`, `time-01` |
| `name` | string | Nazwa karty |
| `faction` | string | `swiete-oficjum` \| `cienie-al-andalus` \| `korona-borgiowie` \| `kabala-toledo` \| `gildia-cieni` \| `time` |
| `type` | string | `akcja` \| `reakcja` \| `permanent` \| `signature` \| `wydarzenie` |
| `cost` | int | Koszt złota (0+) |
| `heresy` | int | Herezja na zagrywającego (0+) |
| `target_heresy` | int | Herezja na wskazanego rywala (0+) |
| `location` | string\|null | Wymagana / docelowa lokacja |
| `agents` | int | Wystaw / przesuń Agentów (0+) |
| `tags` | list | np. `[move]`, `[gold]`, `[arrest]`, `[hook]`, `[interrogation]` |
| `creates_hook` | bool | Czy daje żeton Haka |
| `breaks_rule` | bool | Signature łamiące regułę (opis w tekście) |
| `gold` | int | Złoto zyskiwane (opcjonalne, default 0) |
| `arrest` | bool | Aresztuj Agenta (B+) |
| `layer` | string | `A` \| `B` \| `C` — warstwa wprowadzenia |
| `status` | string | `prototyp` |

## Warstwy

- **A:** dokładnie 5 kart/frakcję — ruch, zasoby, prosta Herezja. **Zero** signature / breaks_rule / hooks / doubles.
- **B:** dokładka narzędzi (Lochy, Haki) — nadal bez signature.
- **C:** pełne 10 + signature; Talia Czasu ≥8 edyktów.

## Format body (po `---`)

```
# {Name}

**Efekt:** {2–5 zdań grywalnych reguł PL zgodnych z frontmatter; przy signature/breaks_rule — jawna złamana reguła.}

**Przy stole:** {1–2 zdania o bluffie, polityce, groźbie lub dramacie.}

**Warstwa:** {A|B|C} — krótko dlaczego ta warstwa.
```

## Przykład

```yaml
---
id: so-01
name: Patrol Familiariuszy
faction: swiete-oficjum
type: akcja
cost: 1
heresy: 0
target_heresy: 0
location: null
agents: 1
tags: [move]
creates_hook: false
breaks_rule: false
gold: 0
arrest: false
layer: A
status: prototyp
---

# Patrol Familiariuszy

**Efekt:** Zapłać 1 złoto. Przesuń 1 swojego Agenta o 1 lokację. Familiariusze obchodzą miasto pod szyldem porządku — bez Herezji na Ciebie.

**Przy stole:** Cichy reposition przed Patrol-em Inkwizytora albo zbliżenie do rywala, którego chcesz mieć w zasięgu aresztu.

**Warstwa:** A — fundament ruchu bez haków i terroru.
```
