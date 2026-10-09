# Any color-free antipodal reachability overlap generates an antipodally invariant 2n-cycle of good roots

# The color-free antipodal-overlap root set has a 2n-cycle gap phenomenon

Let c be an antipodally odd binary UNDIRECTED edge coloring of Q_n, n>=2. Define R(x) to consist of all endpoints of monochromatic shortest paths starting at x, allowing either color and including the empty path. Define the **good-overlap root set**
\[
G=\{x\in Q_n:R(x)\cap\overline{R(x)}\ne\varnothing\}.
\]
The antipodal oddness law R(bar x)=bar(R(x)) makes G invariant under complement.

**Theorem (cycle amplification of any overlap).** Either G is empty, or G contains a simple 2n-cycle C made of TWO internally vertex-disjoint antipodal n-geodesics between the same antipodal endpoint pair \(\{u,\bar u\}\), with C globally invariant under cube antipodality. In particular, nonemptiness implies
\[
|G|\ge2n,\qquad |G/\tau|\ge n.
\]
Moreover every vertex x on this cycle witnesses the SAME antipodal target pair \(\{u,\bar u\}\subseteq R(x)\).

**Proof.** If G is nonempty, the exact color-free reachability extraction theorem gives a full MONOCHROMATIC antipodal n-geodesic P=(u=v_0,v_1,...,v_n=\bar u) of some color q (possibly after rotating a one-switch connector). For every vertex v_j of P, the two subpaths from v_j toward u and toward \bar u are monochromatic q geodesics, because the original edge color is undirected and every subpath of a geodesic is geodesic. Thus u,\bar u∈R(v_j), proving V(P)⊆G.

The antipodal image \bar P consists of a monochromatic (1-q) antipodal n-geodesic between \bar u and u. All its vertices also belong to G, witnessed by the SAME target pair \{u,\bar u\}. A full cube geodesic P contains exactly one pair of antipodal vertices, namely its endpoints: Hamming distance between v_i and v_j equals |j-i|, so it is n only for i=0,j=n. Therefore P and \bar P share precisely u and \bar u. Their union is a simple cycle with 2n distinct vertices and 2n edges, globally invariant under complement. Every vertex on it belongs to G. The claims follow. QED.

**Topological implication.** The fixed-point condition on the reachability nerve cannot first become true at an isolated root orbit: any actual monochromatic-geodesic witness automatically creates a root-mobile antipodally invariant certificate cycle of length 2n. A future topological forcing theorem may profit from targeting this robust carrier or its equivariant homology rather than an arbitrary balanced single ridge. The theorem is a consequence of closure/extraction; it does not by itself force G to be nonempty.
