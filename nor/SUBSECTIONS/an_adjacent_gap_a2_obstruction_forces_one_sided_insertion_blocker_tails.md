# An adjacent-gap A2 obstruction forces one-sided insertion blocker tails

## Metadata

- ID: an_adjacent_gap_a2_obstruction_forces_one_sided_insertion_blocker_tails
- Parent Section: hartman_least_unreachable_connectors
- Position: 25
- Row version: 2
- Development version: 2
- Composition version: 1
- Composition stale: False

## Composition

Separated alternative insertion gaps give commuting absorptions and resolve a rank-two union. At a neighboring alternative gap the inserted vertex's switching choice may change, reversing its normalized mutual edge with the other vertex. Thus immediate-neighbor exclusion requires the new common-gauge mutual-edge check; unconditional one-sided avoidance of both 1100 and 0011 does not follow.

## Development

Let a be insertable at gap i and b at gap i+1 of a path-normalized connector, with the bad mutual orientation b->a.

If b has any other legal insertion gap strictly to the left of a's gap, then:
- when that gap is separated from a's gap, the two absorptions commute;
- when it is the immediately adjacent left gap, b is now the left inserted vertex and a the right inserted vertex, so the required mutual orientation is exactly b->a, which holds.
Either case produces a connector containing both a and b.

Therefore, in a genuine unresolved adjacent-gap obstruction, b has no legal insertion gap anywhere to the left of its original gap.

Symmetrically, a has no legal insertion gap anywhere to the right of its original gap: if a moves to the right of b, the same good mutual orientation b->a resolves the adjacent case, and farther gaps commute.

Hence the residual A2 obstruction canonically splits into two one-sided insertion-blocker tails:
- the left tail of b is blocked;
- the right tail of a is blocked.

In incidence-word language, each corresponding tail avoids 0011 and 1100. The central insertion collars remain the unique inward-facing thick-to-thick transitions on those sides.

This gives the proposed outward transport a rigorous domain: one need not transport an arbitrary defect through the whole connector. One tracks the blocked left tail of b and blocked right tail of a separately. Any new insertion opportunity on the forbidden side immediately closes the rank-two union problem.

Gauge audit: a second insertion position may require complementing the inserted vertex's switch bit relative to its original collar. In separated gaps the mutual a,b edge is absent, so the two absorptions still commute. At the immediately adjacent alternative gap, the mutual edge must be tested in the newly required common gauge. An original 1100 insertion and an alternative 0011 insertion switch b oppositely, reversing its normalized edge with a. Consequently the original bad orientation b→a does not automatically become the good orientation after moving b to the adjacent left gap. The valid blocker-tail conclusion excludes alternative separated absorptions; exclusion at the neighboring gap is conditional on the newly normalized mutual edge.
