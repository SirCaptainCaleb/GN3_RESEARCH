# Cube monochromatic rooted reachability can violate greedoid exchange

- Stable ID: note_nori_xi_reachability_not_a_greedoid
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

The same Q5 coloring with antipodal orbit mask 0x52e039ed14 and root x=30 has color-zero reachable resource subsets R={0,16,17,18,20,21,24,25,26}. This family is accessible (every nonempty feasible set has a shorter feasible prefix) but is neither union-closed nor a greedoid. Union-closure fails because 21 and 26 are reachable while their union 31 is not. Greedoid exchange fails for feasible A=21 (binary 10101, three resources) and B=18 (binary 10010, two resources): A minus B has bits 0 and 2, but neither B+1=19 nor B+4=22 is reachable. Therefore an arbitrary antipodally odd cube coloring does not make rooted monochromatic resource flats into a greedoid or antimatroid; one cannot invoke generic feasible-set exchange to glue independently reachable arms. The obstruction is within one root of a coloring that does have monochromatic full antipodal geodesics elsewhere, so it does not refute NORI1. The bitmask indexing convention is described in the related near-antipodal diameter research note.
