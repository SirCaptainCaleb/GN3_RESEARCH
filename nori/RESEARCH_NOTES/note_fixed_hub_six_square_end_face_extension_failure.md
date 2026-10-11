# A fixed-hub six-square cannot be extended by preserving both end faces

- Stable ID: note_fixed_hub_six_square_end_face_extension_failure
- Author: NORI editorial extraction; mathematical proofs from cited original composition
- Primary home: subsection:near_midpoint_hub_witnesses_and_concrete_splice_failure_tests
- Labels: obstruction, partial_argument
- Lifecycle: active
- Epistemic status: method_limitation
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r4593_2
- Updated session: session_nori_r4593_2
- Disposition: none
- Successor: none

## Related references

- subsection:near_midpoint_hub_witnesses_and_concrete_splice_failure_tests, exact version 1
- subsection:near_midpoint_hub_witnesses_and_concrete_splice_failure_tests, exact version 2

## Research note

# Editorial scope and exact provenance

This is the proof-level limitation of the fixed-hub extension mechanism. The positive two-seam splice and moving-hub witness constructions remain published.

Copied verbatim from Subsection `near_midpoint_hub_witnesses_and_concrete_splice_failure_tests`, publication composition v1. The original complete composition remains retrievable.

## Elevation: why a fixed-hub six-square cannot be extended by preserving its two end faces

Assume n>6, and fix disjoint triple supports A,B with ordered first/last physical face windows BOTH passing through the SAME physical vertex z, as in the theorem. Let C=[n]\(A union B), nonempty.

**Exact no-lift corollary.** NO full n-edge geodesic can have those two fixed physical windows as its first and last ordered-three-face windows. More strongly, any geodesic containing them in the corresponding order has window-index separation EXACTLY 3, with NO coordinate outside A union B traversed between them. Indeed for every i outside A union B, their fixed exterior bits are both z_i. The exact physical two-window incidence theorem says their intermediate support is precisely the directions with DIFFERENT exterior bits, so it is empty. To extend the six-path into an n-path while keeping those end windows, any remaining directions must be traversed BEFORE the first or AFTER the last named window; either choice prevents those two windows from being the first/last of a FULL n-geodesic. Thus the Kneser six-square CANNOT be inflated into a full geodesic by inserting n−6 unused directions between its two 3-blocks without altering at least one endpoint physical face.

Likewise its full four-window path has no nontrivial root-translation symmetry preserving ALL its physical window faces: the intersection of its four free-coordinate triples is EMPTY. A root bit toggle in any direction changes the physical face of at least one of the four windows. This explains why genuinely mobile-root higher-dimensional cells must compare DIFFERENT physical faces and track the resulting color changes rather than freezing a common hub z.

The no-lift is a geometric compatibility obstruction, NOT a NORI counterexample. It pinpoints what an equivariant transport theorem has to accomplish: move and reassign physical face windows while maintaining enough certified reachability memory to preserve the one-change extraction.




Additional extracted proof/scope from near_midpoint_hub_witnesses_and_concrete_splice_failure_tests, source composition v2

**Audit addendum (physical good-window quotient, 2026-10-09).** The "certified root squares" in Theorem 3 are squares ONLY in the redundant hub-coordinate PARAMETER graph. Toggling either shared free direction b or c fixes BOTH underlying ordered physical faces, so the four hub-chart comparisons all project to ONE and the SAME edge of the actual good-window complex W_good. Therefore these squares are DEGENERATE after physical-face identification and must NEVER be counted as nondegenerate 2-cells, an annulus, or evidence for a mixed cup product in W_good. The first genuine exterior-root transport (toggle a direction e outside {a,b,c,d}) is the six-window hexagon completely classified in proved Item nori_exterior_root_transport_hexagon_exact_good_triangles_rigidity_dichotomy_20261009. Its local triangles may fail simultaneously; when present they collapse across free chord edges and leave an induced S1. This addendum sharpens the precise scope of the earlier state-space observation while preserving its pointwise identities and averaging theorem.


The explicit bad rectangles show that a common midpoint and opposite central colors alone are not a closure certificate. The repair complex must also control physical seam windows and their root-bit dependence.
