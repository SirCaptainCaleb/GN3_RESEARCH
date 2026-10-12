# Near-antipodal reachable pairs can overlap and invalidate diameter shortcut

- Stable ID: note_nori_xi_near_antipodal_diameter_failure
- Author: unspecified; session provenance retained
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: 
- Lifecycle: active
- Epistemic status: computational
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6430_3
- Updated session: session_nori_r6430_3
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Counterexample to a tempting strengthening of the antipodal frontier theorem: Q5 coloring with representative edge-orbit bits 0x52e039ed14. Representatives are enumerated for x=0..31 and directions i=0..4 with x_i=0, using the lexicographically smaller of each sorted edge and its antipodal mate, appending unseen orbit representatives in traversal order. At root x=30 the color-zero monotone reachable subsets are {0,16,17,18,20,21,24,25,26}. This family has no complementary pair, yet contains S=21 and T=26, whose symmetric difference has four coordinates, namely Hamming distance n-1. Since S and T share coordinate bit16, they do not violate the valid frontier exclusion of disjoint S,T whose sizes sum to n-1. Thus the reachability set need not have Hamming diameter at most n-2; one cannot directly apply Kleitman diameter bounds. Any stronger bound needs path-history uncrossing or further root compatibility.
