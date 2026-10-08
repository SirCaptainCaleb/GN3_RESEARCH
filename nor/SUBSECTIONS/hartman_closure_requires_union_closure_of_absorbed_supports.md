# Hartman closure requires union closure of absorbed supports

## Metadata

- ID: hartman_closure_requires_union_closure_of_absorbed_supports
- Parent Section: hartman_least_unreachable_connectors
- Position: 8
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

Individual targets reached in different states need not be absorbed together. Component-wise union closure supplies simultaneous support and makes a least missing target meaningful. If one component already reaches all singleton targets, finite union closure alone gives full absorption. Rank-two fillers are partial evidence for this law.

## Development

A repair component may reach each coordinate separately without reaching all of them simultaneously. Therefore the least-unreachable label is justified only after adding a union-closure hypothesis: whenever one oriented repair component reaches absorbed supports A and B, it also reaches a state containing A union B. Then reaching every singleton target forces the full support by finite iteration. Under this strengthened hypothesis, the two-polarity Sperner argument is valid. The same-gap and separated absorption fillers are exactly local pieces of this union-closure law; the adjacent-gap directed triangle is the remaining rank-two obstruction.
