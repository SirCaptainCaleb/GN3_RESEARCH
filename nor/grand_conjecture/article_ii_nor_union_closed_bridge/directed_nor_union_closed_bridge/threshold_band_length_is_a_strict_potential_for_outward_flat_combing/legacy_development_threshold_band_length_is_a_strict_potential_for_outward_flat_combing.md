# Threshold band length is a strict potential for outward flat combing — preserved pre-item development

## Threshold-band length is a strict potential for outward flat combing

Fix a ternary one-change target with cut k and polarity eta in the coboundary-flat pure-orientation sector.

For a full coordinate order pi, let B(pi,k) be the number of consecutive window ranks in the maximal interval
[
[L,R]
]
containing the cut such that every actual window color agrees with the threshold target on that interval.

If all windows agree, NOR is proved. Otherwise suppose the nearest mismatch immediately to the left of the matched band is at rank L-1. Then rank L is matched. Hence the two adjacent statuses at L-1,L form a transition from wrong to correct.

If the supporting tetrahedron is flat, the left endpoint repair from subsection 148 changes this local pair to correct,correct and affects only windows farther to the left. Therefore:
- every previously matched rank in [L,R] remains matched;
- rank L-1 becomes matched.

Thus
[
B(pi',k)ge B(pi,k)+1.
]

The analogous rightward combing repair also strictly increases B.

### Theorem

Orient every available flat boundary repair away from the proposed switch cut, always repairing the nearest mismatch at one end of the current matched band. Then B is a strict integer potential. Consequently no directed cycle of such flat repairs exists.

Every maximal combing sequence terminates after finitely many moves in exactly one of two situations:

1. every threshold window is matched, giving a spanning one-change NOR order;
2. every unresolved boundary of the maximal matched band is supported by a fully-curved tetrahedron.

### Interpretation

This is a genuine termination principle for the mobile-flat part of the repair graph. The strategist's closed-component problem therefore reduces to curvature-barrier normal forms: a counterexample cannot be trapped by indefinitely circulating flat endpoint repairs while a fixed threshold cut is protected.

The remaining obstruction is not flat mobility but the inability to cross one or two fully-curved barriers bounding a target-compatible central band. Local fully-curved predecessor and five-set resolution lemmas should now be viewed as barrier-crossing moves, while the flat repairs merely comb defects outward until those barriers are exposed.
