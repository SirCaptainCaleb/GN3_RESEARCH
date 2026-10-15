# Two-step bi-monochromatic diamonds and splitting of the top-rank reversal cover

# Two-step bi-monochromatic diamonds and the top-rank reversal parity barrier

Suppose an antipodally odd coloring of Q_n, n>=5, admits no monochromatic full antipodal geodesic. Let I be the intersection of the two monochromatic directed endpoint complexes, with involution R(u,v)=(bar v,bar u). The previous rank-gap result gives ranks 2<=r(p)<=n-3 for its vertices and rank increment at least two for comparable vertices.

**Lemma 1 (two-step comparisons).** If p=(u,v)<q=(u',v') is a comparison in I of rank increment two, then either u'=u or v'=v. At the changed endpoint, the red and blue extension certificates are two monochromatic two-edge routes of opposite colors across the same cube square. Therefore
\[
|u'|_1=|u|_1\pmod2.
\tag{1}
\]

*Proof.* A comparison simultaneously witnessed in both colors cannot insert a single edge before or after the smaller interval, since that edge would require both colors. An insertion of positive length at one endpoint must therefore use at least two dimensions. The total increment is two, so all insertions occur at one endpoint. Its red and blue routes are the two distinct two-edge geodesics of a cube square. The initial endpoint changes by zero or two bits, proving (1).

**Lemma 2 (reversal parity).** For every endpoint pair p=(u,v) of rank r, the first endpoint of Rp=(bar v,bar u) satisfies
\[
|\bar v|_1=|u|_1+n+r\pmod2.
\tag{2}
\]
This follows from the Hamming parity difference r between u and v, together with the parity change n under complementation.

**Theorem 3 (top three rank layers split under reversal).** Let I_top be the induced subcomplex of I on ranks at least n-5. Its connected components are paired by R, with no R-invariant component. Consequently the double-cover class of I_top/R vanishes. The same is true for the support stratum I_T of bi-monochromatic interval pairs using any prescribed set T of n-5 dimensions.

*Proof.* The allowed ranks in I_top are n-5,n-4,n-3, intersected with the universal interval rank bounds. All comparison edges have rank difference at least two, hence join the first and last of these ranks; the middle-rank vertices are isolated. There are no higher simplices. By Lemma 1, the parity of the first endpoint is constant along each comparison edge, hence on each nontrivial graph component. For ranks n-5 and n-3, the value n+r is odd. Lemma 2 shows that R flips the first-endpoint parity and must exchange a connected component with a distinct one. Isolated rank vertices also have distinct R-mates because no rank less than n endpoint pair is fixed by R. The resulting double cover splits componentwise. The support stratum I_T is contained in I_top because its interval ranks are at least n-5, so inherits the splitting.

**Corollary 4.** For n=7 the complete seam I has only ranks 2,3,4, hence I=I_top and alpha_I=0. The seam transgression theorem then yields
\[
\boxed{\alpha_{K_0\cup K_1}^2=0,}
\]
improving the earlier purely rank-derived bound that its third power vanishes. In dimensions five and six, I has no comparison edges, and the same square-zero conclusion holds.

**Meaning.** The top-rank seam alone cannot sustain a reversal-index obstruction. Any invariant connected seam component in higher dimensions must reach lower-rank intervals: rank-two opposite-color extension diamonds near the maximal interval rank cannot connect a vertex to its reversal. The theorem is a conditional obstruction and does not settle NORI1.
