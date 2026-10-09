# Kneser forces four actual six-edge paths through every hub with one root, endpoint, and a 2×2 reversal-signature color square

# Kneser forces a same-root, same-center, two-sided reversal square of genuine six-edge geodesics

Let n>=8 and let c be ANY binary coloring of actual physical ORDERED 3-faces of Q_n, not necessarily satisfying antipodal oddness. Fix ANY physical cube vertex z. For each ordered triple alpha=(a,b,c) of distinct direction names, define h_z(alpha) to be the physical color of the ordered 3-face through z with ordered free directions alpha.

**Theorem (unconditional centered six-edge two-sided reversal square).** There exist DISJOINT unordered direction triples A,B with ordered orientations alpha=(a1,a2,a3) on A and gamma=(b1,b2,b3) on B, and two bits q,r∈{0,1}, such that
\[
h_z(\alpha)=h_z(\operatorname{rev}\gamma)=q,\qquad
h_z(\operatorname{rev}\alpha)=h_z(\gamma)=r.
\tag{1}
\]
Consequently from the ONE SAME ROOT x=z XOR A to the ONE SAME ENDPOINT y=z XOR B there exist FOUR ACTUAL six-edge direction-distinct geodesics:
\[
P_{00}=(\alpha,\operatorname{rev}\gamma),\quad
P_{01}=(\alpha,\gamma),\quad
P_{10}=(\operatorname{rev}\alpha,\operatorname{rev}\gamma),\quad
P_{11}=(\operatorname{rev}\alpha,\gamma).
\tag{2}
\]
All four traverse the SAME physical hub z at their midpoint after three moves, and ALL FOUR physical ordered-three-face window faces of EVERY path contain z. Their initial/final ordered-window color pairs are the complete two-by-two table
\[
\begin{array}{c|cc}
 &\operatorname{rev}\gamma&\gamma\\
\hline
\alpha&(q,q)&(q,r)\\
\operatorname{rev}\alpha&(r,q)&(r,r)
\end{array}.
\tag{3}
\]
In particular the two diagonal paths P00 and P11 each have either ZERO or EXACTLY TWO ordered-window color changes (since their four-window color words begin and end with the same bit). The other two have opposite endpoint colors precisely when q≠r. NO conclusion is asserted about the two interior window bits or the existence of a monochromatic/one-switch SIX-edge path.

**Proof.** Associate to each unordered 3-set T the pair (h_z(alpha_T),h_z(rev alpha_T)), for an arbitrarily selected orientation alpha_T. Orientation reversal interchanges the two bits. Up to this interchange there are exactly THREE orbit types: 00,11,{01,10}. Thus the unordered 3-subsets of [n] are colored with THREE types. The classical Kneser chromatic theorem gives chi(KG(n,3))=n-4>3 for n>=8, so two DISJOINT triples A,B have the same orbit type. Reorient alpha and gamma so that the second triple signature is the SWAPPED signature of the first, yielding precisely the two equations (1). For n>=10 one may avoid the named Kneser input and instead use the elementary cyclic-interval disjoint-triple count already proved in Item nori_same_order_antipodal_root_pairs_endpoint_opposition_disjoint_triple_orbits_20261008.

Every word in (2) uses the same six distinct directions A union B, first the A directions then B, so from root x=z XOR A each reaches z after 3 moves and then ends at y=z XOR B. The four length-three free-coordinate windows begin at path positions1,2,3,4. In window1 the already fixed directions outside the first triple are still at their z-bits, because root differs from z only in the three FREE A bits. In windows2,3 the remaining untraversed A directions are still the only differing bits from z and are FREE in the window. After the third move the path is at z; window4 is the B-face through z. Hence ALL four physical face windows contain z. Their first and last ordered free triples are just the selected A and B orientations; (1) gives their color pairs (3). An even-parity number of changes follows for a four-bit word whose first/last bits agree, so the diagonal words have 0 or2 changes. \(\square\)

**Topology-first significance.** This creates at EVERY physical hub a literal four-vertex square in the space of genuine SAME-root/SAME-endpoint six-edge paths, indexed by two INDEPENDENT reversals of 3-direction prefix/suffix blocks. Unlike a fixed-root pair of unrelated endpoint-balanced full paths, these four certificates have a COMMON midpoint z and complete agreement of their used support. The input is a TOPLOGICAL Kneser coloring obstruction with only three signature orbits. Under active NORI oddness the four-path square also has the usual physically antipodal mate centered at bar z with complemented-reversed ordered windows.

The unresolved step is to transport this certified six-edge square through the other n−6 directions, using physical face incidence/root slides, so that an equivariant fixed-point collision produces a complete n-edge path with ≤1 change. The diagonal endpoint-equality condition alone is weaker than monochromaticity, and cannot be inflated to a global grand result without controlling the two middle seam windows and later exterior-bit changes.
## Elevation: why a fixed-hub six-square cannot be extended by preserving its two end faces

Assume n>6, and fix disjoint triple supports A,B with ordered first/last physical face windows BOTH passing through the SAME physical vertex z, as in the theorem. Let C=[n]\(A union B), nonempty.

**Exact no-lift corollary.** NO full n-edge geodesic can have those two fixed physical windows as its first and last ordered-three-face windows. More strongly, any geodesic containing them in the corresponding order has window-index separation EXACTLY 3, with NO coordinate outside A union B traversed between them. Indeed for every i outside A union B, their fixed exterior bits are both z_i. The exact physical two-window incidence theorem says their intermediate support is precisely the directions with DIFFERENT exterior bits, so it is empty. To extend the six-path into an n-path while keeping those end windows, any remaining directions must be traversed BEFORE the first or AFTER the last named window; either choice prevents those two windows from being the first/last of a FULL n-geodesic. Thus the Kneser six-square CANNOT be inflated into a full geodesic by inserting n−6 unused directions between its two 3-blocks without altering at least one endpoint physical face.

Likewise its full four-window path has no nontrivial root-translation symmetry preserving ALL its physical window faces: the intersection of its four free-coordinate triples is EMPTY. A root bit toggle in any direction changes the physical face of at least one of the four windows. This explains why genuinely mobile-root higher-dimensional cells must compare DIFFERENT physical faces and track the resulting color changes rather than freezing a common hub z.

The no-lift is a geometric compatibility obstruction, NOT a NORI counterexample. It pinpoints what an equivariant transport theorem has to accomplish: move and reassign physical face windows while maintaining enough certified reachability memory to preserve the one-change extraction.
