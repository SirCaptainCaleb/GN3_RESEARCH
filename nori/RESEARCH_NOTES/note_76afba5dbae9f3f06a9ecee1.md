# Cyclic successor colorings concentrate two-color endpoint pairs at full rank

- Stable ID: note_76afba5dbae9f3f06a9ecee1
- Author: session_nori_r7948_2
- Primary home: subsection:two_color_rank_jumps_and_the_half_dimensional_reversal_obstruction
- Labels: counterexample, antipodal-coloring, endpoint-poset, cycle, rank-gap
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r7948_2
- Updated session: session_nori_r7948_2
- Disposition: none
- Successor: none

## Related references

- subsection:two_color_rank_jumps_and_the_half_dimensional_reversal_obstruction

## Research note

Let \(\sigma\) be a fixed-point-free permutation of \([n]\), \(n\ge3\). Define an undirected cube-edge coloring by
\[
\boxed{c(\{x,x\oplus e_i\})=x_{\sigma(i)}.}
\tag{1}
\]
Because \(\sigma(i)\ne i\), the right-hand side is independent of which endpoint represents the edge. Complementing every bit changes it by one, so the coloring is antipodally odd.

**Theorem (permutation-invariant supports control two-color endpoint coincidences).** Fix \(u\in Q_n\) and a nonempty set \(S\subseteq[n]\), with \(v=u\oplus\mathbf1_S\). If \(u,v\) are joined by monochromatic geodesics of both colors, then
\[
\boxed{\sigma(S)=S.}
\tag{2}
\]
Conversely, when \(\sigma(S)=S\), any color-zero geodesic from \(u\) to \(v\) yields a color-one geodesic from the same \(u\) to the same \(v\) by reversing the ordering of the traversed dimensions, and vice versa.

*Proof.* If \(\sigma(S)\ne S\), bijectivity of \(\sigma\) implies that some \(i\in S\) has \(\sigma(i)\notin S\). Every geodesic from \(u\) to \(v\) traverses direction \(i\) once but never changes bit \(\sigma(i)\). By (1), the color of the dimension-\(i\) edge on every such geodesic is therefore the same bit \(u_{\sigma(i)}\). Two geodesics of opposite constant colors cannot both exist.

Now suppose \(\sigma(S)=S\), and let \(\pi\) be a dimension ordering of \(S\). At the moment the edge in dimension \(i\) is crossed, its color is
\[
u_{\sigma(i)}+
[\sigma(i)\text{ occurs before }i\text{ in }\pi]\pmod2.
\tag{3}
\]
Because \(\sigma(i)\in S\) and differs from \(i\), reversing the ordering \(\pi\) flips the indicator in (3) for every \(i\in S\). Thus each dimension-\(i\) edge in the reversed-order geodesic has the opposite color of the corresponding dimension-\(i\) edge in the original path. If the original is monochromatic of color \(a\), the reversed ordering yields a monochromatic geodesic of color \(1-a\), between the same endpoints. \(\square\)

**Corollary (full-rank concentration for an \(n\)-cycle).** Take \(\sigma(i)=i+1\pmod n\). Then every proper nonempty \(S\subsetneq[n]\) violates (2). Consequently the intersection of the two monochromatic endpoint-poset complexes has no vertices of ranks \(1,\dots,n-1\); all its vertices have rank \(n\). Such vertices exist: take \(u=e_1\), \(v=\bar u\), and order the dimensions as \(1,2,\dots,n\). Every traversed dimension has color zero under (1), so this is a monochromatic full antipodal geodesic. The opposite order \(n,\dots,1\) is monochromatic in color one.

In fact a coloring of the form (1) with a general derangement \(\sigma\) can have two-color endpoint pairs only on supports which are unions of whole cycles of \(\sigma\). Therefore the allowable ranks in its red-blue endpoint intersection are sums of cycle lengths. The single-cycle case demonstrates that no theorem can force a proper bi-monochromatic endpoint pair in every legal coloring: the first such pair may occur only at full antipodal rank.

**Research implication.** The half-dimensional sphere target in Article XIV arises under a hypothetical failure of NORI1, where full-rank endpoint pairs are absent. In contrast, this legal coloring possesses full-rank pairs but has no lower-rank two-color intersections whatsoever. Therefore a proposed global chain transfer cannot rely on the universal nonemptiness or high connectivity of the proper-rank bi-monochromatic intersection. The construction is a method-specific obstruction; it preserves NORI1, rather than contradicting it.
