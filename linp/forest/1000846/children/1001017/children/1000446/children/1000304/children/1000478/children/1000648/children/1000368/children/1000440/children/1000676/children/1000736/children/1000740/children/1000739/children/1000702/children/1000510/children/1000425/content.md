# The p=5 pattern 4555 has a late/joint/crossed rail normal form

## Statement

In the p=5 pattern 4555, retain the setup of 7120b83b863a:
  f={x,v,u}
is the unique rank-four charged edge, phi(x)=3, and
  R=(r1,r2,r3)
is a canonical three-edge entrance path with last vertex x and avoiding v,u.

Let h be one of the three rank-five charged edges through v.

Then every h is either:

(L) late: h misses r1 and r2 and meets r3 at the unique free vertex of r3 distinct from x and r2∩r3;

or

(E) early: h meets both r1 and r2.

There is at most one late edge. Among early edges, at most one can meet r1 and r2 only at their common joint s=r1∩r2. Every other early edge is crossed and has the exact form
  h={v,a,b}
with
  a∈r1\{s}, b∈r2\{s}.

Consequently the three rank-five competitors contain at least two early edges and at least one crossed edge.

## Body

By 7120b83b863a, each rank-five charged edge h meets R; if it misses r1 then it misses r2 and hence meets r3, while if it meets r1 then it also meets r2.

Suppose h is late, so it misses r1,r2 and meets r3. Let
  t=r2∩r3.
The r3-contact cannot be x: the rank-four edge f contains both v and x, while h contains v, so if h also contained x then h and f would share two vertices, violating linearity.

The contact cannot be t either, because then h would meet r2 at t, contradicting the late assumption.

Thus the only possible r3-contact is the third vertex
  w∈r3\{x,t}.
Distinct rank-five competitors through v have pairwise disjoint non-v pairs by linearity, so at most one of them can contain w. Hence there is at most one late edge.

Therefore among the three rank-five charged competitors at least two are early.

Now let h be early. Put s=r1∩r2. If h meets r1 and r2 in the same vertex, that vertex must be s. Two distinct early edges cannot both be of this joint type, since they would share both v and s, violating linearity. Hence at most one early edge is joint type.

If h meets r1 and r2 in distinct vertices a,b, then a cannot equal s: if a=s then h also meets r2 at s, giving two vertices of intersection with r2 once b is included. Similarly b≠s. Thus
  a∈r1\{s}, b∈r2\{s}.
Since h is 3-uniform and already contains v,a,b,
  h={v,a,b}.
We call this crossed type.

With at least two early edges and at most one joint-type edge, at least one early edge is crossed.
