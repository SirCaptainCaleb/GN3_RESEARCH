# At every bichromatic hub, mixed-class cap colors are uniform and any cross-omitted near-spanning monochromatic core closes NORI

# A bichromatic hub forbids every monochromatic near-spanning core across each mixed omitted pair in a counterexample

Fix an active NORI ordered-three-face coloring of \(Q_n\), \(n\ge6\). Assume the **no-common-colored-certified-edge** alternative B of the square-edge-shadow dichotomy, so the connectedness theorem supplies a *bichromatic hub* \(z\) and two disjoint sets \(A,B\subset[n]\) of certified middle-edge directions of colors \(0,1\), respectively, \(|A|,|B|\ge2\), with at most one remaining isolated direction. The proved mixed-class selector rigidity says that every actual ordered face through \(z\) with middle free direction in \(A\) or \(B\), and one outer direction in the opposite class, has color equal to the middle-direction class.

**Theorem (all cross-pair codimension-two caps are uniform; immediate extension).** Choose **any** \(a\in A\), \(c\in B\) and write
\[
U=[n]\setminus\{a,c\},\qquad r=z|_U.
\]
For each \(i\in U\) and **every** cube vertex \(x_t\) whose \(U\)-coordinates equal \(r\) (the four choices of the omitted \(a,c\) bits), the genuine geometric cap labels obey
\[
\boxed{
c(F(x_t;\{a,c,i\}),(a,c,i))=1,\qquad
c(F(x_t;\{a,c,i\}),(c,a,i))=0.}
\tag{1}
\]
The values are independent of \(i\) and the two omitted-coordinate exterior assignments. Consequently **any monochromatic \((n-2)\)-edge geodesic** spanning all coordinates in \(U\), rooted at any \(x_t\) above projected root \(r\), forces a full NORI antipodal geodesic with at most one change.

**Proof.** Both cap faces in (1) have free coordinates \(\{a,c,i\}\), so varying the \(a,c\) bits of \(x_t\) leaves each physical face literally unchanged. At \(z\), the first ordered triple has middle direction \(c\in B\) and adjacent outer direction \(a\in A\), so its color is 1 by the mixed selector. The second has middle direction \(a\in A\) and adjacent outer direction \(c\in B\), so its color is 0. This proves (1).

Let \(P\) be any monochromatic \(U\)-spanning geodesic, with color \(q\), rooted at \(x_t\), first direction \(i\), last direction \(j\). If \(q=0\), **prepend** the omitted directions in order \((a,c)\) to \(P\), choosing the new root \(x_t\oplus e_a\oplus e_c\) so that the resulting path reaches \(x_t\) after the first two steps. Its first three window colors are \((1,s,0)\) for some \(s\in\{0,1\}\), and every later window is 0. The word changes color exactly once regardless of \(s\). If \(q=1\), instead **append** the omitted directions in order \((c,a)\) after \(P\). Its last three window colors are \((1,s,0)\), using the cap reversal-odd identity
\[
c(F(y_t;\{j,c,a\}),(j,c,a))
=1-c(F(x_t;\{a,c,j\}),(a,c,j))=0,
\]
where \(y_t=x_t\oplus\chi_U\) is the endpoint of \(P\) and the opposite physical face is used; all earlier windows are 1. Thus again exactly one change occurs. Both extensions use each coordinate exactly once. \(\square\)

**Corollary (uniform forbidden four-facet bundles under hypothetical grand failure).** If the grand conjecture fails and alternative B holds, then for **every** bichromatic hub \(z\) and **every** cross-class pair \(a\in A(z)\), \(c\in B(z)\), none of the four \(U\)-parallel facets based at projected root \(z|_U\) contains a monochromatic full \(U\)-geodesic **from its projected root**. Equivalently the four-facet monochromatic first–last memory graph \(\mathcal H_U(z|_U)\) is **empty**, not merely bipartite. In particular, there are at least \(|A||B|\ge2(n-3)\) distinct forbidden omitted-coordinate pairs (because \(|A|,|B|\ge2\) and \(|A|+|B|\ge n-1\), the product is at least \(2(n-3)\)) at each such hub.

This is a substantial strengthening of the generic four-facet cap-memory odd-cycle criterion: *every* near-spanning monochromatic core with a cross-class omitted pair is a grand-closure certificate, irrespective of its first and last directions or color.

**Exact open forcing implication.** The theorem does not supply a near-spanning monochromatic geodesic in any chosen facet; arbitrary ordered-face colorings can lack such paths at prescribed roots. A dimension-independent grand proof would follow if the physical-face incidences and antipodal symmetry guaranteed that at some bichromatic hub of alternative B, at least one of these \(4|A||B|\) root/facet cases has a monochromatic \(n-2\)-direction geodesic. The theorem isolates a concrete *global monochromatic-core transversal problem* in place of the broader one-change condition.
