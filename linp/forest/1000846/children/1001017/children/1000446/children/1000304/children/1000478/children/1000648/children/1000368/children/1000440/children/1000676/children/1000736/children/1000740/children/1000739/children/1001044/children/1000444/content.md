# The low-low witness geometry is impossible in the p=5 pattern 4455

## Statement

In the p=5 charged pattern (4,4,5,5), the {b,c} rank-four witness geometry is impossible. Consequently every surviving 4455 obstruction must have rank-four witness set {a,b}, with a=g2∩g3 and b the private vertex of g3.

## Body

By 37e5daffc494, the two-contact state in the {b,c} geometry is impossible. It remains only the clean state from 96ce63c6b236.

In that clean state, let
  h={x,v,u}
be the second rank-five charged edge. Then h is disjoint from g2∪g3 and meets g4 exactly at its entrance x, which is the private vertex of g4.

By c88a9ec76475, for the rank-four edge
  f_b={b,v,u_b},
the opposite terminal u_b lies in g1. Thus
  g1∩f_b={u_b}.
Also f_b and h are distinct charged edges through v, hence
  f_b∩h={v}.

Consider
  g1,f_b,h,g4.

Consecutive intersections are u_b,v,x. The nonconsecutive pairs are disjoint:
- g1∩h=empty because the clean state has no h-contact in g1: if h met g1, that contact could not be the joint g1∩g2 (which would also be a g2-contact), so it would be private; but then the same four-edge sequence g2,g1,h,g4 would already give phi(c)>=4. Equivalently one may establish this private-g1 exclusion directly before the displayed splice.
- g1∩g4=empty by the original path property.
- f_b∩g4=empty because f_b={b,v,u_b}, with b in g3 but not g4, v off g4, and u_b in g1.

Hence g1,f_b,h,g4 is a four-edge linear path ending in g4. Its predecessor h meets g4 at x, while c=g3∩g4 is a distinct vertex of g4. Therefore c can be chosen as last vertex and
  phi(c)>=4.

But c is the entrance of the other rank-four charged edge in the {b,c} witness geometry, so phi(c)=3. Contradiction.

Thus the clean state is impossible as well. Together with 37e5daffc494, no {b,c} witness geometry exists. By e6eec0f670ed, the only remaining 4455 witness geometry is {a,b}.
