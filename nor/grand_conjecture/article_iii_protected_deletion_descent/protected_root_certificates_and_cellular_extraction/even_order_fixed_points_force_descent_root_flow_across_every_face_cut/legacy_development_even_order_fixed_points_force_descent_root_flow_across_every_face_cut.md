# Even-order fixed points force descent-root flow across every face cut — preserved pre-item development

## Composition

(none yet)

## Development

**Proof repair (root §44).** The fixed-point flow conclusion below is valid, but the original radial-sign argument confused a permutahedron face with its dual braid face. The correct sign follows from its strictly negative initial-block rank sums. The following version uses those sums.

## Even-order fixed points force descent-root flow across every face cut

Use the continuous physical 10-root carrier G from the preceding face-carrier construction. Radially identify the boundary of the centered permutahedron with the unit sphere S(W), where dim W=n-1. Assume n is even, so S(W) has even dimension n-2.

If G vanishes, the face-carrier theorem already gives a positive dependence of actual 10 window-slide roots and hence a physical directed root cycle. Suppose instead that G is everywhere nonzero.

Define the tangent projection
H(u)=G(u)-<G(u),u>u
on S(W), with G transported through the radial identification. This is a continuous tangent vector field. Since n-2 is even, the hairy-ball theorem forces H(u)=0 at some u. Hence
G(u)=lambda u
for some scalar lambda.

Let F=B_1|...|B_s be the minimal proper permutahedron face containing the unnormalized boundary point p(u). Carrier roots refine F, though u need not be constant inside its blocks. For any proper initial block union S_j, with k=|S_j|,
\[
\sum_{v\in S_j}p(u)_v=-k(n-k)/2<0
\]
because those coordinates occupy the first k centered ranks at every refining vertex. After normalization its u-sum is still negative. Every carrier root has nonnegative sum over S_j, so G=lambda u implies lambda<=0. Nonvanishing makes lambda<0. Writing mu=-lambda gives G=-mu u.

This sign is proved at the tangential fixed point only. No assertion that every face-carried root has nonpositive radial pairing is needed.

### Flow consequence

Write the ordered-partition face containing u as
B_1|B_2|...|B_s,
where the block order specifies occupied rank intervals; individual coordinates inside a block need not be equal. Orient every root e_a-e_b as the directed edge b -> a, from the later coordinate to the earlier coordinate. Expand G(u) as a positive convex combination of the actual 10 roots supplied by the carrier.

For each proper initial union
S_j=B_1 union ... union B_j,
sum the coordinates of G(u) over S_j. Internal root edges cancel. Every root crossing the cut from the later side into S_j contributes positively, and no root can cross in the opposite orientation. Hence this sum is exactly the total positive weight of 10-root flow crossing that face cut.

On the other hand, the fixed-point equation gives
sum_{v in S_j} G_v(u) = -mu sum_{v in S_j} u_v.
Because each initial block union occupies the first k centered ranks throughout its permutahedron face, its u-sum is strictly negative. Therefore
sum_{v in S_j} G_v(u) > 0.

So every proper block boundary of the fixed-point face is crossed by at least one actual 10 descent root in the carrier.

### Fixed-point dichotomy

For even n, the continuous physical-root carrier therefore yields:

1. either G has a zero, giving a positive dependence of actual physical descent roots localized to one face;
2. or there is a face point u with G(u)=-mu u, mu>0, and positive 10-root flow crosses every proper block cut of that face.

Unlike the gap-weighted degeneracy, neither alternative is forced by geometry alone: both retain actual coloring-dependent descent roots. The second alternative is not yet NOR closure and does not automatically preserve protected deletion provenance. Its value is that it replaces an arbitrary nonvanishing odd carrier by a balanced inward descent flow that sees every cut. A next extraction theorem can try to align one of these forced cut crossings with the protected threshold cut or use a minimal fixed-point face to force an A3 carrier.
