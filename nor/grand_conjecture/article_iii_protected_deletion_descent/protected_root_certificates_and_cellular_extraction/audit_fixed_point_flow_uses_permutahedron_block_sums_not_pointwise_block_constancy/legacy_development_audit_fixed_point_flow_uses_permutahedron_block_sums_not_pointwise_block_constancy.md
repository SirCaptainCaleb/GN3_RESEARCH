# Audit: fixed-point flow uses permutahedron block sums, not pointwise block constancy — preserved pre-item development

## Audit: fixed-point flow uses permutahedron block sums, not pointwise block constancy

The fixed-point conclusion of the even-order physical-root carrier survives, but one step in its first proof was too strong.

A point y in a proper face of the centered permutahedron is not generally constant on each block of the ordered partition. Thus one may not assert that every root e_a-e_b carried by a refinement satisfies <e_a-e_b,y><=0 merely from the face label when a and b lie in the same block.

The correct argument uses sums over initial block unions.

Let the carrying face be
B_1|...|B_s
and let
S_j=B_1 union ... union B_j
be a proper initial union, with m=|S_j|. Every vertex refining this face assigns exactly the first m ranks to S_j. Hence, in the centered permutahedron, every point y of the face satisfies the fixed identity
sum_{v in S_j} y_v
=
[1+...+m] - m(n+1)/2
=
-m(n-m)/2
<0.
Radial normalization to the sphere multiplies this by a positive scalar, so the sign remains negative.

Now expand the physical carrier G(y) as a positive convex combination of actual 10 slide roots e_a-e_b carried by refinements of the same face. Because every refinement lists all coordinates of B_1 before B_2 before ... before B_s, a root crossing the cut S_j | S_j^c can only have a in S_j and b outside S_j. Such a root contributes +1 to the coordinate sum over S_j. Roots with both endpoints on the same side contribute zero. Therefore
sum_{v in S_j} G_v(y) >= 0
for every proper initial block cut.

At a tangential zero of the sphere field,
G(y)=lambda y.
Since the left side is nonnegative while the corresponding sum of y is strictly negative, lambda<=0. If G is assumed nonzero, then lambda is nonzero, so lambda<0. Put mu=-lambda>0. Then
G(y)=-mu y.

Moreover, for every proper initial block union,
sum_{v in S_j} G_v(y)
=
mu m(n-m)/(2||y||)
>0.
Hence at least one actual 10 root crosses every block boundary.

Thus the fixed-point dichotomy and its descent-flow conclusion are valid, but the proof should use the permutahedron's fixed initial-block sums rather than pointwise constancy or a global inner-product sign. This correction is important exactly on A3-or-larger blocks, where roots may have both endpoints inside one tied block and the discarded pointwise claim can fail.
