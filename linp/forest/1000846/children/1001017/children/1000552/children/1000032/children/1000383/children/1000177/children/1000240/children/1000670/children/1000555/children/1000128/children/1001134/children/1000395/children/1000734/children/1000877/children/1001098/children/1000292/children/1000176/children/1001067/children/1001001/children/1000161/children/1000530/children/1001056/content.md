# Every whole chord on a canonical common anchor has source and terminal returns

## Statement

Let h={y,v,w} be an ascending nonspecial anchor of rank q and let
  R=(g_1,...,g_{q-1})
be a canonical maximum source rail ending at y, so R,h is a longest q-edge h-path and R avoids v,w.

Let e={x,v,u} be a distinct ascending nonspecial edge terminal at v such that both x and u lie on R. Let S_x be a canonical maximum source rail ending at x, and let P_u be any maximum endpoint path ending at u.

Then both
  |V(S_x) intersect V(R)| >= 2
and
  |V(P_u) intersect V(R)| >= 2.

If moreover e is terminal-single on P_u, exactly one of x,v lies on P_u away from u. Hence:
- in reciprocal type X, x lies on P_u, so x and u are two explicit common vertices of P_u and R;
- in reciprocal type V, x is absent from P_u and v is absent from R, so the second common vertex of P_u and R is external to e.

Thus every whole chord on a canonical common anchor carries two independent maximum-path return certificates to the anchor: one from its clean source rail at x and one from its opposite-terminal path at u.

## Body

The source-rail assertion is 76a6a3666ad9.

For the opposite-terminal assertion, R is a maximum endpoint path ending at y because h is ascending of rank q, so phi(y)=q-1 and |R|=q-1. The path P_u is maximum ending at u. Since u lies on R and u!=y, suppose for contradiction that
  V(P_u) intersect V(R)={u}.
By the unique-intersection theorem 5854d853a44b, the sole common vertex u would have to be an internal joint on both maximum endpoint paths at the same index. But u is the last vertex of P_u, contradiction. Therefore P_u and R share another vertex besides u.

Now impose terminal-singleness of e at u. Since q_e=phi(e)<phi(u) in the strict-gap application, e is not the last edge of P_u. Its unique off-u e-contact on the precursor is exactly one of x or v. If it is x, then x belongs to both P_u and R, giving the explicit pair {u,x}. If it is v, then x is absent from P_u by terminal-singleness, while v is absent from R because R is the anchor source precursor. Hence the forced additional P_u/R common vertex is neither x nor v and is external to e.

No payment or minimum-terminal hypothesis is used in the two-return assertion.
