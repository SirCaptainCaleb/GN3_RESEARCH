# The even-order fixed-point flow theorem is proved by face prefix sums — preserved pre-item development

## Composition

(none yet)

## Development

## The even-order fixed-point flow theorem is proved by face prefix sums

This is a proof repair of root §35, preserving its fixed-point dichotomy and cut-flow conclusion.

The published proof claims that a point u in a permutahedron face F=B_1|...|B_s has equal coordinates inside each block, hence that every root carried by a refinement satisfies <u,rho><=0. That identifies a permutahedron face with its dual braid-arrangement face. In a permutahedron face the coordinates inside a block may differ. An internal root carried by another refinement may have positive radial pairing. Thus that radial-sign justification is unavailable.

The theorem is nevertheless valid for the actual physical-root face carrier, by its block-prefix sums.

### Corrected theorem and proof

Let P be the centered rank permutahedron, identify its boundary radially with S(W), and transport the continuous carrier G of root §32. Suppose n is even and G has no zero. Tangential projection
\[
H(u)=G(u)-\langle G(u),u\rangle u
\]
is a continuous tangent vector field on the even-dimensional sphere S^{n-2}. Hairy ball gives H(u)=0, hence
\[
G(u)=\lambda u,\qquad\lambda\ne0.
\]

Choose the minimal permutahedron face F containing the unnormalized boundary point p(u), and write it as B_1|...|B_s, with s>=2. The barycentric carrier value is a convex combination of actual 10 slide roots whose carrying orders refine F. This carrier property does not require the coordinates of u to be equal inside a block.

For a proper initial union S_j=B_1 union ... union B_j, put k=|S_j|. At every vertex refining F, those k physical coordinates occupy exactly the first k centered ranks. Therefore throughout the face,
\[
\sum_{v\in S_j}p(u)_v
=\sum_{\ell=1}^k\left(\ell-\frac{n+1}{2}\right)
=-\frac{k(n-k)}2<0.
\]
After radial normalization,
\[
\sum_{v\in S_j}u_v=-\frac{k(n-k)}{2\|p(u)\|}<0.
\]

Every root carried by F crosses such a block cut only from its later side to its earlier side in the circulation convention. Thus
\[
\sum_{v\in S_j}G_v(u)\ge0.
\]
Insert G=lambda u. The strictly negative u-prefix sum forces lambda<=0. Since lambda is nonzero, lambda<0. Put mu=-lambda>0.

Moreover for every proper initial block union,
\[
\sum_{v\in S_j}G_v(u)
=\frac{\mu\,k(n-k)}{2\|p(u)\|}>0.
\]
Expanding the convex combination shows that this is precisely the positive weight of actual 10-root flow crossing that cut. No other root can contribute negatively across that cut. Hence every block boundary has an actual crossing descent in the carrier.

This proves the root §35 dichotomy: a physical-root zero, or a nonzero tangential fixed point with inward radial scalar and positive root flow across every proper face cut.

### Scope

Only the sign at the fixed point is established. The carrier need not have nonpositive radial pairing at an arbitrary face point, and its roots need not be cooriented with that point's strict coordinate order.

The corrected argument also gives an explicit prefix-flow profile proportional to k(n-k) at a fixed point. It keeps the coloring-dependent actual roots and their common-face compatibility. It still supplies neither a protected deletion witness for every averaged root nor a spanning one-change surgery.

Root §42 uses an inward face-normal functional for zero-free interpolation. That functional is distinct from the radial vector u. Both arguments are compatible after this distinction is made.
