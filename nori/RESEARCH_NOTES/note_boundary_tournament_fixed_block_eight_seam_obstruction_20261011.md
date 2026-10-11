# Eight-way block reversal does not repair boundary-tournament seams

- Stable ID: note_boundary_tournament_fixed_block_eight_seam_obstruction_20261011
- Author: unspecified; session provenance retained
- Primary home: article:nori_article_ix_unification
- Labels: obstruction, boundary-tournament, seam, proved
- Lifecycle: active
- Epistemic status: method_limitation
- Current version: 3
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6176_1
- Updated session: session_nori_r6202_2
- Disposition: none
- Successor: none

## Related references

- article:nori_article_ix_unification

## Research note

# Fixed monochromatic blocks cannot always be repaired across a triple seam

**Proposition.** An ordinary reversal-odd boundary tournament on six vertices admits two disjoint positive monochromatic tight paths \(A=(0,1,2)\) and \(B=(3,4,5)\) such that every path obtained by independently reversing these blocks and concatenating them in either order has at least two changes among its four consecutive triple colors.

**Construction.** For pairwise distinct \(a,b,c\in\{0,\dots,5\}\), define
\[
h(a,b,c)=x_{\min(a,c),b,\max(a,c)}\oplus [a>c].
\]
Set \(x_{a,b,c}=1\) precisely for
\[
(0,1,2),\ (1,0,3),\ (1,0,5),\ (2,5,4),\ (3,4,5)
\]
(with \(a<c\)); set every remaining \(x\) to zero. Then \(h(c,b,a)=1-h(a,b,c)\) and \(h(0,1,2)=h(3,4,5)=1\).

**Exhaustive eight-order certificate.**
\[
\begin{array}{c|c|c}
\text{order}&\text{triple word}&\text{changes}\\
012345&1001&2\\
012543&1010&3\\
210345&0101&3\\
210543&0100&2\\
345012&1101&2\\
345210&1010&3\\
543012&0101&3\\
543210&0110&2
\end{array}
\]
Every entry follows directly from the displayed five-bit assignment and reversal oddness.

**Scope.** This refutes the fixed-block repair rule, even when the two originally given blocks have equal color. It does not refute the existence of a different full ordering with at most one change, nor does it refute midpoint co-reachability. Two complementary-support cube geodesics do concatenate geometrically, but this fact alone leaves the two ordered-triple windows crossing their seam uncontrolled. A topological carrier targeting a full one-change ordered-triple sequence therefore needs further seam data.
