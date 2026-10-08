# Legitimate NORI coloring with four parallel codimension-two facets all lacking monochromatic spanning cores

# Valid NORI coloring with NO monochromatic spanning geodesic in any of four parallel codimension-two facets

Fix n>=7, choose U⊆[n] of size m=n-2>=5, and let [n]\U={a,b}. Mark any two distinct coordinate directions u*,v* inside U, and call all other directions of U unmarked. For every ordered triple (i,j,k) of distinct directions FROM U define
\[
f(i,j,k)=
\begin{cases}
1,& j\text{ is unmarked and at least one of }i,k\text{ is marked},\\
0,&\text{otherwise}.
\end{cases}
\]
This f is reversal-even, f(k,j,i)=f(i,j,k). Define colors on ALL physical ordered three-faces whose free directions lie in U by
\[
c(F,(i,j,k))=f(i,j,k)\oplus t_a(F),
\]
where t_a(F) is the fixed exterior a-bit. Since a lies outside U, it is fixed on each such face. If \bar F is antipodal, t_a(\bar F)=1-t_a(F), and reversal-evenness gives
\[
c(\bar F,(k,j,i))=f(k,j,i)\oplus(1-t_a(F))=1-c(F,(i,j,k)).
\]
Thus this partial coloring respects the active NORI axiom. Extend arbitrarily, orbit by orbit, to all ordered faces with at least one free direction outside U; the involution (F,pi)↦(\bar F,rev pi) is free so this always yields a globally valid NORI coloring.

**THEOREM.** For this full valid coloring, NONE of the FOUR parallel U-facets contains a monochromatic complete U-geodesic, in EITHER traversal orientation or from ANY projected root. Consequently the color-free four-facet first–last direction graph H_U(r) of the canonical cap theorem is EMPTY for every r∈Q_U.

**Proof.** Fix a permutation p=(p1,...,pm) of U and any facet exterior bits. Its m-2 ordered-three-face window colors equal
\[
f(p_i,p_{i+1},p_{i+2})\oplus t_a,\qquad 1\le i\le m-2.
\]
The physical U-exterior bits do not appear in f, so the word is root-independent inside the facet up to the fixed global flip t_a.

We prove its f-word contains BOTH symbols 0 and1. If either marked coordinate appears in an internal position 2,...,m-1, the window centered there has f=0, since the middle direction is marked. If instead both marked positions are endpoints 1,m, the window (p2,p3,p4) consists entirely of unmarked directions for m>=5, so again f=0.

For f=1, it suffices to find two adjacent positions k,k+1, with one position marked and the other unmarked, such that the unmarked position is internal (2,...,m-1). Such a pair must exist: otherwise any marked-to-unmarked boundary could only have its unmarked position at one of the endpoints, forcing the entire interval of internal positions to be marked or all transitions to occur only at ends. The first is impossible since m-2>=3 but only two marked directions exist. The latter possibility would make the marked positions consist only of a subset of the two endpoints, with both marks at endpoints; then positions 1 and 2 form a boundary whose unmarked index 2 is internal, a contradiction. More directly, if the marks are adjacent at positions 1,2 or m-1,m, the boundary at positions 2,3 or m-2,m-1 works; in all other arrangements at least one marked coordinate has an internal unmarked neighbor. Choose the triple centered at this internal unmarked position and having the marked adjacent position as an endpoint; then f=1.

Hence the f-word contains 0 and1 for EVERY direction permutation, so no full U-geodesic is monochromatic. Complementing the word by t_a does not change this. There are no actual monochromatic U-spanning witnesses in any of four facets, and H_U(r) has no edges. QED.

**Important strategic guardrail.** A dimension-independent proof of grand NORI closure CANNOT begin by claiming that for every (or every prescribed) n-2 support U the four-facet memory graph H_U(r) is nonempty or nonbipartite. This fully legal coloring annihilates that graph for the selected U, while grand closure itself may hold elsewhere. Thus the cap-cycle extraction theorem, although correct, must be combined with a global support-selection argument or with shorter monochromatic reachability. The example is direction-only within U plus one exterior-bit affine twist, so it is not an exotic nonlinear obstruction.
