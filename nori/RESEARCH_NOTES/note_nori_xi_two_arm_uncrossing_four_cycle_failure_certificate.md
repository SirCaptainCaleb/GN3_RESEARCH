# Failed two-arm local uncrossing forces an oriented four-cycle

- Stable ID: note_nori_xi_two_arm_uncrossing_four_cycle_failure_certificate
- Author: unspecified; session provenance retained
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: boundary-tournaments, two-arm-packing, graphic-circuit, exchange-obstruction, local-tournament
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6430_2
- Updated session: session_nori_r6430_2
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Local graphic-circuit uncrossing obstruction for boundary tournaments (research note). Fix color epsilon, a middle original vertex w, and four pairwise distinct neighbors a,c,d,e. Suppose two monochromatic tight path segments use triples (a,w,d) and (c,w,e) of color epsilon; in the local epsilon tournament T_w this means arcs a->d and c->e. A simultaneous tail-swap at w would use cross triples (a,w,e) and (c,w,d). If BOTH cross triples have color 1-epsilon, the local tournament contains the directed four-cycle a->d->c->e->a, since reversal oddness converts the failed arcs into d->c and e->a. Therefore all failures of both local cross-splices are witnessed by an oriented four-cycle, a graphic circuit in M(K_(V\{w})). If either cross color remains epsilon, at least one single-arm splice is available, but preserving both arms and their original-vertex disjointness may require further exchanges; neither a successful spanning swap nor the main one-turn conjecture follows. This links failed global resource-basis circuit uncrossings to local directed four-circuit obstructions. Such four-cycles are permitted in arbitrary tournaments, so parity alone cannot rule them out; a proof needs a potential or cancellation argument across many crossings. Preserve as a research note, not publication claim.
