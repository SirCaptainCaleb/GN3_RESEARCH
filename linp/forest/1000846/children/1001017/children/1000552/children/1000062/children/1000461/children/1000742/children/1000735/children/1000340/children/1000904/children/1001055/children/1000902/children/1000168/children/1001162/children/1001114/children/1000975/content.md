# Every gap-one switching edge manufactures an endpoint lens on the maximum path

## Statement

Every switching edge in a gap-one anchor-to-maximum switching matching manufactures an endpoint lens on the maximum path P: if c is its unique retained off-v endpoint on P, then every maximum endpoint path P_c ending at c meets P in at least one additional vertex. Consequently a near-saturated gap-one vertex supports (5/8)q-O(1)-delta distinct endpoint-lens states attached to one maximum (q+1)-path.

## Body

Let v be in the gap-one shell phi(v)=q+1, and let
  P
be a maximum (q+1)-edge endpoint path ending physically at v.

Let f={v,c,d} be an ascending terminal edge at v that is single on P, with
  c in V(P)\last(P),
  d notin V(P).
Thus f is one of the anchor-to-maximum switching edges from fecba48a3ffd/f62e6a5ecb9a.

Let P_c be any maximum endpoint path ending physically at c, of length phi(c).

Then
  |V(P) intersect V(P_c)| >=2.

Indeed c belongs to both paths. If c were their unique common vertex, the universal unique-intersection theorem 5854d853a44b would force c to be a path joint on both P and P_c at one common index. But c is the physical endpoint of P_c, hence is not a path joint of P_c. Contradiction.

Therefore c lies on a genuine two-vertex overlap between the maximum v-path P and a maximum c-path. Passing to c and the nearest other common vertex along P_c produces an elementary endpoint lens based on P.

Distinct switching edges give distinct retained vertices c, because their non-v pairs are disjoint by linearity. Hence a switching matching of size s manufactures at least s distinct retained endpoint labels on P, each of whose maximum endpoint paths meets P in at least two vertices.

In particular, under the near-saturation hypothesis of fecba48a3ffd,
  s >= gamma(q)-ceil((3q-4)/4)-delta
    = (5/8)q-O(1)-delta,
so one maximum (q+1)-edge path P supports linearly many endpoint-lens states.

This statement is independent of whether c is the unique entrance or the opposite terminal of f:
- if c is the entrance, P_c is the chosen/source maximum path at c;
- if c is the opposite terminal, use any maximum terminal endpoint path at c.
The endpoint argument is identical.
