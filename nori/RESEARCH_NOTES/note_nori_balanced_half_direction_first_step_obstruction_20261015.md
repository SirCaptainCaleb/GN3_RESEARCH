# Balanced odd cubes with half the directions unavailable as first monochromatic steps

- Stable ID: note_nori_balanced_half_direction_first_step_obstruction_20261015
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: balanced, geodesic, root-rotation, scope-obstruction
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r9962_4
- Updated session: session_nori_r9962_4
- Disposition: none
- Successor: none

## Related references

- None

## Research note

For every m>=2 let Q_(2m) have direction labels A_j,B_j (j modulo m). Define
\[
c_{A_j}(x)=x_{A_{j+1}},\qquad c_{B_j}(x)=1-x_{A_{j+1}}.
\tag{1}
\]
These are undirected edge-color rules because A_(j+1) differs from A_j and B_j. Each rule is antipodally odd; each pair (A_j,B_j) contributes one zero incident edge at every vertex, so the coloring is vertex-balanced.

**Theorem (half-direction obstruction to root-first reordering).** The set of directions occurring as the first step of some all-zero full antipodal geodesic is precisely {B_0,...,B_(m-1)}. Every A_j is forbidden as both the first and the last direction, although all-zero full antipodal geodesics exist.

*Proof.* In any all-zero full geodesic, the traversed A_j edge and B_j edge must see complementary values of x_(A_(j+1)), since their colors are x_(A_(j+1)) and 1-x_(A_(j+1)). The unique traversal of A_(j+1) therefore occurs strictly between A_j and B_j in its direction order. Hence no A_j may occur first or last.

Conversely, the direction order
\[
B_{m-1},A_0,A_1,B_0,A_2,B_1,\ldots,A_{m-1},B_{m-2}
\tag{2}
\]
places A_(j+1) strictly between A_j and B_j for every j. Choose initial bits x_(A_0)=1 and x_(A_j)=0 for 1<=j<m, leaving every B-bit arbitrary. Then B_(m-1) is traversed before A_0 and has color 1-x_(A_0)=0; its paired A_(m-1) occurs after A_0 and sees x_(A_0)=0. For 0<=j<m-1, A_j occurs before A_(j+1) and sees x_(A_(j+1))=0, whereas B_j occurs after A_(j+1) and sees 1-(0 xor 1)=0. Thus (2) is an all-zero full antipodal geodesic. Cyclic relabeling j makes any specified B_j the first direction. QED.

**Scope.** Even in the balanced antipodally odd reduction class, existence of a monochromatic full geodesic need not allow its first direction to be prescribed arbitrarily; n/2 directions may be excluded. An approach that attempts to realize one monochromatic profile and obtain every profile-bit toggle by moving a chosen direction to the first position therefore requires a different exchange mechanism. This is a limitation of that strategy, not a counterexample to NORI1.
