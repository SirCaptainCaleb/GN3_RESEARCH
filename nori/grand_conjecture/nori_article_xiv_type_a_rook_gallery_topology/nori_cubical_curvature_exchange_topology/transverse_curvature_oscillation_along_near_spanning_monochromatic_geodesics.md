# Transverse curvature oscillation along near-spanning monochromatic geodesics

# Transverse curvature oscillation along near-spanning monochromatic geodesics

This subsection extracts an all-dimensional rigidity theorem from the complementary-arm residual-face barrier (Article XIV, Subsection 41). It directly links full-rank monochromatic reachability to **changes of ordinary square curvature along two transverse strips**. No restricted coloring subclass, regularity condition, or small-order enumeration is assumed.

Let \(n\ge3\), \(D=[n]\), and let \(c\) be any undirected binary cube-edge coloring with \(c(\tau e)=1-c(e)\). Use red \(0\), blue \(1\), and let \(\kappa(F)=\sum_{e\subset\partial F}c(e)\pmod2\). Suppose, for contradiction, that \(c\) admits **no monochromatic full antipodal geodesic**. Equivalently, it admits no full antipodal geodesic with at most one color change, since moving the root across the unique change converts such a path into a monochromatic one.

## Theorem 1 (a residual-face barrier propagates along an entire monochromatic geodesic)

Let \(P=(v_0,v_1,\ldots,v_m)\) be a monochromatic red cube geodesic of length \(m=n-|M|\), where \(M\ne\varnothing\) is the set of dimensions not traversed by \(P\). For every \(0\le t\le m\), and for every permutation \(\sigma\) of \(M\), the monotone path across the face
\[
F_t=F_M(v_t)
\tag{1}
\]
starting at \(v_t\) and following the dimensions of \(M\) in order \(\sigma\) has a blue-to-red descent \(1\to0\).

The \(m+1\) residual faces \(F_0,\ldots,F_m\) are pairwise distinct and have disjoint vertex sets. If \(|M|\ge2\), each face contains at least \(|M|(|M|-1)\) descending directed two-edge turns, so the union of these faces contains at least
\[
\boxed{(n-|M|+1)|M|(|M|-1)}
\tag{2}
\]
distinct such turns.

*Proof.* Split \(P\) at \(v_t\) into its initial and terminal portions and reverse the first portion. These give two red geodesics from \(v_t\) to \(v_0\) and \(v_m\), with disjoint dimension supports partitioning \(D\setminus M\). Apply the two-arm residual-face gluing theorem of Subsection 41, at root \(v_t\). If a monotone route through the face \(F_M(v_t)\) lacked a blue-to-red descent, then gluing the two red arms across that route would give a complete antipodal geodesic with at most one switch, contrary to hypothesis. The faces \(F_t\) have free dimensions \(M\), and the fixed bits outside \(M\) are the pairwise different vertices of the simple geodesic \(P\). Hence they are pairwise disjoint. Each has at least \(|M|(|M|-1)\) descending two-edge turns by the sharp residual-face turn inequality of Subsection 41. Disjointness makes the counts additive. \(\square\)

For \(|M|=1\), the theorem gives an immediate contradiction: a one-edge path has no two-edge descent. This recovers the observation that a monochromatic geodesic of length \(n-1\) forces a full monochromatic antipodal geodesic somewhere.

## Theorem 2 (the two transverse curvature words must oscillate in both directions)

Suppose \(|M|=2\), say \(M=\{i,j\}\). Write \(m=n-2\), and let \(d_t\) be the dimension traversed from \(v_{t-1}\) to \(v_t\), \(1\le t\le m\). Then at every vertex \(v_t\) of \(P\),
\[
\boxed{
c_i(v_t)=c_j(v_t)=1,\quad
c_j(v_t\oplus e_i)=c_i(v_t\oplus e_j)=0.
}
\tag{3}
\]
For each missing dimension \(a\in\{i,j\}\), define a **transverse curvature word**
\[
\boxed{
W^{(a)}_t
=\kappa\!\left(F_{\{a,d_t\}}(v_{t-1})\right),
\qquad 1\le t\le m.
}
\tag{4}
\]
Then each \(W^{(a)}\) contains **both** transitions
\[
\boxed{01\quad\text{and}\quad10}
\tag{5}
\]
as adjacent two-letter subwords. Equivalently, the curvature of the successive side squares is neither nonincreasing nor nondecreasing. In particular, each of the two strips contains a curved square and a flat square, and has at least two changes in its curvature word.

*Proof.* The two-dimensional part of Theorem 1 says that for every \(t\), both monotone paths across \(F_{\{i,j\}}(v_t)\) must have color word \(10\). This gives the blue-out/red-in gate (3).

For \(a=i\), the strip square \(F_{\{i,d_t\}}(v_{t-1})\) has longitudinal base edge \(v_{t-1}v_t\) red, and its two transverse dimension-\(i\) edges incident with \(v_{t-1},v_t\) are blue by (3). Their contributions cancel modulo two, so
\[
\boxed{
W^{(i)}_t
=c(\{v_{t-1}\oplus e_i,v_t\oplus e_i\}).
}
\tag{6}
\]
The same argument holds with \(i\) replaced by \(j\). Thus the curvature word along either strip is the color word of the translated path \(P+a\), which uses all dimensions of \(D\setminus\{i,j\}\) once.

For either \(a\), let \(b\) be the other missing dimension. Starting from \(v_0\), take the blue dimension-\(a\) edge to \(v_0+a\), traverse the translated path \(P+a\), and finally take the red dimension-\(b\) edge from \(v_m+a\) to \(v_m+i+j=\tau v_0\). The gate (3) guarantees both endpoint colors. This is a complete dimension-simple antipodal geodesic with word
\[
\boxed{1\,W^{(a)}\,0.}
\tag{7}
\]
If \(W^{(a)}\) had no ascending transition \(01\), its word would belong to \(1^*0^*\), so (7) would have at most one change, contradicting the hypothesis. Thus \(W^{(a)}\) contains \(01\).

Now reverse the original red geodesic \(P\). Its vertices run from \(v_m\) back to \(v_0\), so it remains red and the same gates (3) hold at each vertex. Repeating the construction from the reversed path gives the complete word
\[
1\,\operatorname{rev}(W^{(a)})\,0.
\]
It must also have more than one switch, forcing an ascending transition \(01\) in the reversed curvature word, equivalently a descending transition \(10\) in \(W^{(a)}\). This proves (5). \(\square\)

**Corollary 3 (two-dimensional long-path obstruction).** Every red geodesic using all but two dimensions in a hypothetical NORI1 counterexample determines two **different transverse square-curvature strips**. Along each strip the curvature must change at least twice, in both binary directions; in particular each contains at least one face of curvature \(1\) and one of curvature \(0\). The \(n-1\) parallel residual squares along the original path have curvature zero and carry the unique blue-out/red-in pattern. The same theorem holds with the colors exchanged.

For \(n=4\), the translated strip words have length \(2\) and cannot contain both kinds of transition. Therefore Theorem 2, together with the earlier rank-\((n-1)\) geodesic extension principle, rules out any monochromatic geodesic of length \(n-2\) in a hypothetical counterexample. This is an incidental low-dimensional consequence; the theorem's main content is the uniform all-rank curvature-oscillation requirement.

**Remark (why this is stronger than the square gate alone).** The flatness of each residual \(\{i,j\}\)-square is a single local parity condition. Theorem 2 forces *variability of the ordinary curvature on other squares*, in two separate dimensions, **along the entire ordered red path**. The two transitions are constrained in the path's dimension order. This is new color-sensitive incidence information that the projective class \([\bar\kappa]\) does not capture by itself. It is a necessary condition under the no-full-geodesic hypothesis, not a proof that such a coloring exists. The next proof question is whether the imposed red-prefix corridor barriers and two transverse curvature oscillations can be incompatible with the all-rank Coxeter exchange homotopies after aggregating them across roots and dimension orders.

## Corollary 4 (one-sided Freudenthal defects on every transverse strip)

Under Theorem 2's hypotheses, consider the side square
\[
G_t^{(a)}=F_{\{a,d_t\}}(v_{t-1}),\qquad a\in\{i,j\}.
\]
Let \(\Omega_b(G_t^{(a)};z)\) denote the mod-two parity of monochromatic color-\(b\) two-step routes across this square, rooted at any corner \(z\) of the square (as in Subsections 21 and 39). Then **for all four corners**,
\[
\boxed{
\Omega_0(G_t^{(a)};z)=0,\qquad
\Omega_1(G_t^{(a)};z)=\kappa(G_t^{(a)})=W_t^{(a)}.
}
\tag{8}
\]
Thus the blue exchange-defect sequence along each strip contains both binary transitions \(01\) and \(10\), while the red exchange defect vanishes identically along that strip.

*Proof.* The longitudinal base edge in dimension \(d_t\) has color \(0\). Both transverse edges in dimension \(a\) have color \(1\) by the gate condition (3). The remaining longitudinal edge has color \(W_t^{(a)}\), by equation (6). The two root-based routes therefore have respective color words \(01\) and \(1W_t^{(a)}\). Neither route is red-monochromatic; precisely one is blue-monochromatic if and only if \(W_t^{(a)}=1\). This proves (8) at the base corner. The formula for the two root-relative route counts is unchanged at the other corners, because the two parallel \(a\)-edges both have color \(1\), giving zero parallel-edge discrepancy in dimension \(a\). Apply the root-corner transport identity in Subsection 31 to conclude corner independence. The oscillation assertion follows from Theorem 2. \(\square\)

**Implication for color-filtered chain corrections.** Along any near-spanning red geodesic under a hypothetical counterexample, the two transverse strips are rank-simple sequences of adjacent squares with \(\Omega_0=0\) and non-monotone \(\Omega_1\). This supplies a forced, position-dependent pattern **directly on the internal Freudenthal facet defects** of Subsection 39, rather than only on their color-blind sum. For a blue base geodesic, the two color roles are interchanged. Any proposed global cancellation must respect these one-sided defect profiles, since they follow from the original unrestricted coloring and the no-full-geodesic assumption.
