# Explicit antipodally odd Q7 coloring realizes sharp 26-set middle Kneser bound at one root without rank-six reachability

- Stable ID: note_nori_xi_q7_kneser_extremal_root_reachability
- Author: unspecified; session provenance retained
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: Q7, Kneser, SAT, certificate, obstruction
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

Verified finite certificate accompanying the two-color Kneser publication. Give each antipodal edge orbit a bit using 224 canonical representatives (min(s,127 XOR (s OR (1<<i))),i), taken for all s in 0..127 with bit i zero, sorted by (direction i, representative lower endpoint). Assign bit k from hexadecimal mask 0x696b5dd3096b7f9709697c95017f7f9626999ba1a6999b90a6999898 and complement its antipodal mate. At root x=0, monotone monochromatic reachability R0^0 has 25 subsets, R0^1 has 31, union 53. Its rank-three layer has 26 subsets, partitioned into A={three-sets with at least two in T={0,1,2}} and B={three-sets containing 3 and at least one of {4,5,6}} union {{4,5,6}}, each thirteen. Every reachable set from root0 uses at most four coordinates, and the union is complement-free; in particular root0 has no rank-six monochromatic witness. Nevertheless a full monochromatic antipodal geodesic exists from root1 with color zero. Therefore maximum single-root middle-layer size and lack of any rank-six path at that root are compatible with a valid deck-odd coloring; a closure proof must couple multiple roots. Independently verified by running the supplied Python program verify_nori_q7_reachability.py, which asserts all 224 orbit parities, the specified middle-layer equality, maximum rank, complement-free union, and presence of a global full witness. Independent finite enumeration over 35 triangle-majority and 140 canonical thirteen-set Hilton-Milner families found 70 disjoint majority-majority pairs, 140 canonical-majority pairs, and no canonical-canonical pairs.
