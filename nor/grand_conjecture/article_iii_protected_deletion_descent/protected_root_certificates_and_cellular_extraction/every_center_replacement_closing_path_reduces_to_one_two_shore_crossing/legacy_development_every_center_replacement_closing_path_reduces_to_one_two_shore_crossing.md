# Every center-replacement closing path reduces to one two-shore crossing — preserved pre-item development

## Development

Strengthen root §144 from an arbitrary proper ordered partition to one two-block facet.

Root §144 gives, for every chosen actual 10 root
r_0=e_s-e_t,
a proper permutahedron face
G=B_1|...|B_m
and a directed path of actual 10 roots
t=x_0 -> x_1 -> ... -> x_l=s
such that every path root is carried by a refinement of G and is weakly forward in the G-block order, while s lies in a strictly later G-block than t.

Choose any block cut q strictly between the block containing t and the block containing s, and coarsen G to the facet
H=L|R,
where
L=B_1 union ... union B_q,
R=B_{q+1} union ... union B_m.
Then t is in L and s is in R.

Every order refining G also refines H. Hence every path root is still an actual 10 root carried by a refinement of the SAME facet H.

Moreover every path root is weakly forward for the two-block order L|R:
- an internal root has both endpoints in L or both in R;
- a crossing root goes from L to R;
- no root goes from R back to L.

Take the directed path simple, deleting any repeated-vertex loops if necessary. Since it starts in L and ends in R and never has a backward R-to-L edge, it crosses the facet exactly once.

Thus there are vertices u in L and v in R such that the path decomposes as

t -> ... -> u        entirely inside L,
u -> v              one actual cross-facet 10 root,
v -> ... -> s        entirely inside R.

Together with the chosen backward actual root
s -> t = r_0,
this gives a cycle with exactly one forward facet crossing and exactly one backward facet crossing.

### Internal-root locality

If an actual ternary slide root e_a-e_b is carried by a refinement of H and both a,b lie in L, then its four consecutive supporting coordinates all lie in L. Indeed every L-coordinate precedes every R-coordinate in any refinement of H; a four-window beginning and ending in L cannot contain an R-coordinate between them. The same holds in R.

Therefore the two internal path segments are built entirely from actual descents of the proper induced subinstances on L and R. Only the single root u->v uses both shores.

### Consequence

The non-tautological center replacement of §144 can always be sharpened to the following TWO-SHORE closing configuration:

For every chosen actual 10 root s->t, there is a proper bipartition V=L disjoint union R with t in L, s in R, one actual cross-facet root u->v from L to R, an actual-root path inside L from t to u, and an actual-root path inside R from v to s.

The remaining gluing problem is therefore not an arbitrary common-face path. It is one transverse 10 packet plus two internal paths living on strictly smaller coordinate sets.

By minimum-counterexamplehood, each shore L and R independently admits a spanning one-change order. The next theorem should replace or absorb the internal actual-root paths using these good shore orders and reduce closure to the boundary interaction of one L-to-R 10 packet with two shore-good orders.
