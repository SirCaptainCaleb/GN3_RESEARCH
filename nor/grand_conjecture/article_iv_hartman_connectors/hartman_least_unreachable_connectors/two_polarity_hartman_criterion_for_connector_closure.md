# Two-polarity Hartman criterion for connector closure

## Composition

Conditional Hartman criterion: choose two-orientation proper-support connector states with same-orientation coherence, component-wise union closure of absorbed supports, and Sperner boundary exclusion. Then a least missing target is well defined and component constant; a fully labeled chain contradicts the two-color repetition. Construction of those hypotheses remains open.

## Development

Let S be a minimal shore support with no full connector. For each nonempty missing set U choose an oriented connector on the complement, with orientation color beta in {0,1}. Let R(q) be the shore coordinates whose absorbed-boundary targets are reached inside the reversible beta-component of q. Label q by the least coordinate not in R(q). Because coordinates outside U are already absorbed in q, the label belongs to U, so this is a Sperner labeling of the barycentric subdivision. If the chosen states have the coherence property that nested missing sets with the same beta lie in the same reversible component, then a fully labeled barycentric simplex is impossible: its vertices form a chain, two have the same beta, coherence gives the same reachable-target set and hence the same least-unreachable label. Therefore coherent two-polarity connector states on all proper supports force a full connector. The remaining task is to build this coherence from local absorption squares and the adjacent-gap triangle residue.

Required hypothesis from §8: component-wise reachable absorbed supports must be union-closed, or another theorem must show that reaching each singleton target gives a state absorbing their union. Without that hypothesis R(q) may contain every shore coordinate in separate states, so a least unreachable coordinate need not exist. Same-orientation component coherence, a well-defined least missing label, and Sperner boundary exclusion are separate requirements. All connector sizes, including the empty-complement two-coordinate connector (z,x), are included in the general state model.
