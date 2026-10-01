# Potential-five pattern 4555 reduces to exactly two crossed edges and one joint edge

## Statement

In the p=5 charged pattern (4,5,5,5), retain the canonical rank-four entrance rail
  R=(r1,r2,r3)
from 5ef77fe98dff, with
  f={x,v,u},
  phi(x)=3,
and s=r1∩r2.

Then none of the three rank-five charged competitors can be late. Consequently all three are early, exactly two are crossed, and exactly one is joint type.

More precisely:
- the joint-type edge contains v and s;
- the two crossed edges are
    h_i={v,a_i,b_i}, i=1,2,
  where {a_1,a_2}=r1\{s} and {b_1,b_2}=r2\{s}.
Thus the two crossed edges saturate all four non-joint vertices of r1∪r2.

## Body

By 5ef77fe98dff, at least one rank-five competitor is crossed. Let
  h_C={v,a,b}
be a crossed edge, with
  a∈r1\{s}, b∈r2\{s}.

Suppose a late competitor h_L also exists. By the same normal form, h_L misses r1,r2 and meets r3 at the unique free vertex
  w∈r3\{x,r2∩r3}.
In particular w≠x.

Consider
  r1,h_C,h_L,r3.

Consecutive intersections are:
  r1∩h_C={a},
  h_C∩h_L={v},
  h_L∩r3={w}.

All nonconsecutive pairs are disjoint:
- r1∩h_L=empty because h_L is late;
- r1∩r3=empty because R is a linear path;
- h_C∩r3=empty because the two non-v vertices of h_C are a∈r1 and b∈r2.

Hence this is a four-edge linear path.

Its final edge is r3, entered through w. Since x is a distinct vertex of r3, x can be chosen as the last vertex. Thus
  phi(x)>=4,
contradicting phi(x)=3.

Therefore no late competitor exists.

All three rank-five competitors are early. By 5ef77fe98dff, at most one early edge is joint type, so at least two are crossed.

There are at most two crossed edges: distinct rank-five edges through v have disjoint non-v pairs by linearity, while every crossed edge uses one vertex of the two-element set r1\{s}. Thus three crossed edges cannot coexist.

Hence exactly two competitors are crossed and the third is joint type.

Write the two crossed edges h_i={v,a_i,b_i}. Their r1-contacts a_i are distinct and lie in the two-element set r1\{s}, so they exhaust it. Likewise their r2-contacts b_i are distinct and exhaust r2\{s}.
