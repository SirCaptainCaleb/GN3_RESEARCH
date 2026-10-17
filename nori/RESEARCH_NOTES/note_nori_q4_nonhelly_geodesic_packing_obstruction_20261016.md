# Q4 pairwise intersecting non-Helly geodesic supports

- Stable ID: note_nori_q4_nonhelly_geodesic_packing_obstruction_20261016
- Author: Independent NORI1 critical-star researcher
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: critical-star, Q4, packing, non-Helly
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11254_3
- Updated session: session_nori_r11254_3
- Disposition: none
- Successor: none

## Related references

- None

## Research note

**Q4 non-Helly support theorem (proved).** The antipodally odd coloring of Q4 whose red graph is the disjoint union of cycles
\[
(0,1,9,8,0),\qquad
(2,6,4,5,7,3,11,15,13,12,14,10,2)
\]
has four red full antipodal geodesics up to reversal. Their antipodal-pair support sets are pairwise intersecting and have empty common intersection. Thus the absence of a critical antipodal vertex pair does not imply two full monochromatic geodesics with disjoint antipodal-pair support.

**Proof.** Identify Q4 vertices with integers 0,...,15. Two integers are adjacent when their XOR is a power of two; the antipode is x xor 15. The cycles have 4+12=16 edges, and checking each edge shows none of its antipodal mates is among these edges. Since Q4 has 32 edges, coloring precisely these 16 edges red and the rest blue is legal. The red 4-cycle contains no antipodal vertex pair. The red 12-cycle contains just four antipodal pairs (2,13),(3,12),(4,11),(5,10). In each case the shorter cyclic arc has four edges and the longer arc eight, so the red full geodesics are
\[
(2,10,14,12,13),\quad(3,11,15,13,12),\quad(4,5,7,3,11),\quad(5,4,6,2,10).
\]
Identify an antipodal vertex pair by its smaller endpoint in {0,...,7}. The support sets are
\[
 \{1,2,3,5\},\ \{0,2,3,4\},\ \{3,4,5,7\},\ \{2,4,5,6\}.
\]
Every pair of sets intersects, but their fourfold intersection is empty. The antipodal map changes red geodesics into blue geodesics and preserves support classes. Hence the same four supports account for the monochromatic geodesics of either color.

**Finite reproducibility.** Check the antipodal mate of each edge in the two listed cycles. For roots x=0,...,7, enumerate all 24 orders of the four direction flips, and select the red paths; those four lists are the complete result. This requires no solver or probabilistic inference.

**Scope.** This refutes two-path support packing as a prerequisite for pair avoidance. It does not refute NORI1 or existence of avoiding paths for each prescribed pair.
