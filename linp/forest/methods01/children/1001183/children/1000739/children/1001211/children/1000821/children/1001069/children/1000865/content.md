# The joint edge in the exact 4555 rectangle is either rail-clean or hits only the private vertex of the third rail edge

## Statement

In the exact p=5 pattern 4555 of edc545e3d1e7, let
  f={x,v,u}
be the unique rank-four charged edge with canonical entrance rail
  R=(r_1,r_2,r_3),
let
  s=r_1∩r_2,
  q=r_2∩r_3,
and let
  j={v,s,t}
be the unique joint-type rank-five charged competitor.

Then
  t∉{x,u,q}.
Consequently either j is disjoint from r_3, or t is the private vertex of r_3 (the unique vertex of r_3\{x,q}).

## Body

Because j and f are distinct edges both containing v, linearity gives
  j∩f={v}.
Hence t is neither x nor u.

Now suppose t=q=r_2∩r_3. Since j also contains s=r_1∩r_2, the distinct edges j and r_2 would share the two vertices s and q, contradicting linearity. Thus t≠q.

The third edge r_3 consists of x, q, and its private vertex. Since t is neither x nor q, any contact of j with r_3 must occur at that private vertex. Otherwise j is disjoint from r_3.