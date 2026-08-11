# Schemat karty

Każda karta to plik Markdown w odpowiednim katalogu frakcji lub Talii Czasu.

Nazwa pliku: `NN-slug.md` (np. `01-zamach-w-cieniu.md`).

## Frontmatter (zalecany)

```yaml
---
id: so-01
name: Zamach w Cieniu
faction: swiete-oficjum | cienie-al-andalus | korona-borgiowie | kabala-toledo | gildia-cieni | time
type: akcja | reakcja | permanent | wydarzenie
tier: basic | advanced | signature
cost: 0
heresy: 0          # ile punktów Herezji dodaje zagrywającemu (może być ujemne przy oczyszczeniu)
target_heresy: 0   # ile Herezji dodaje wskazanemu rywalowi
location: any | trybunal | palac | lochy | rynek | gildia
agents: 0          # wymagana liczba Agentów w lokacji
tags: [skrytobojstwo, proces, relikwia]
status: draft | playtest | locked
---
```

## Treść

```markdown
# Nazwa karty

**Efekt:** …

**Bluff / Uwagi projektowe:** …
```

## Konwencje balansu (punkt startowy)

| `heresy` | Siła efektu (orientacyjnie) |
| ---: | :--- |
| 0 | Bezpieczna, słaba / utility |
| +1 | Solidna akcja |
| +2 | Silna / kluczowa |
| +3 | Niszczycielska / signature |

Karty typu *Fabrykowanie Dowodów* / *Podrzucenie Księgi* powinny mieć niski `heresy` u zagrywającego i wysoki `target_heresy`.
