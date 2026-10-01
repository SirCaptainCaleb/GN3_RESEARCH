# A 2q-3 cut has three rank patterns, with only explicit low-rank boundary cycles obstructing the normal forms

## Statement

Let
v_0v_1...v_k
be a rainbow terminal-pair path whose parent hyperedges belong to U_11 and have nondecreasing edge ranks. Fix a cut with
  r_t=q,
  r_{t+1}=2q-3,
and let x_i=v_j be an interior color-terminal collision crossing the cut.

Then exactly one of the following rank patterns occurs.

(T_even)
  r_i=2q-2,
  r_j=r_{j+1}=q.
If q=3, this is the rank-4 low boundary and the collision closes a local linear 3-cycle. If q>=4, it is a nonboundary tight even collision and
  |V(R_i) intersect V(R_j)|>=2.

(T_odd)
  r_i=2q-3,
  r_j=q-1,
  r_{j+1}=q.
Necessarily q>=4. If q=4 and E_{j+1} is the host last edge h of R_i, the collision closes the explicit rank-5 boundary triangle. Otherwise
  |V(R_i) intersect V(R_j)|>=2.

(P_3)
  r_i=2q-3,
  r_j=r_{j+1}=q,
so
  r_j+r_{j+1}=r_i+3.
Necessarily q>=4. Put
  R_i=(g_1,...,g_{2q-4})
and h=g_{2q-4}.
If one of E_j,E_{j+1} equals h, then q=4 and the boundary-cycle alternative of 20ee63fa1617 holds.
If neither adjacent parent equals h, both have genuine exact contacts c_j,c_{j+1} on R_i. Either their occurrence intervals overlap, in which case some edge of R_i together with E_j,E_{j+1} forms a linear 3-cycle, or the intervals are disjoint. In the disjoint case, after naming c_- the earlier contact and c_+ the later contact,
  c_-=g_{q-3} intersect g_{q-2},
while c_+ is either the private vertex of g_{q-1} or
  g_{q-1} intersect g_q.

Thus all crossing states at a 2q-3 cut are finite-state after two explicit low-rank boundary-cycle exceptions are separated.

## Body

Because the collision crosses the cut,
  r_i>=2q-3
and
  r_j,r_{j+1}<=q.
The universal bound 867efd696575 gives
  r_i+2<=r_j+r_{j+1}<=2q.
Hence
  r_i in {2q-3,2q-2}.

First suppose r_i=2q-2. Equality throughout forces
  r_j=r_{j+1}=q.
This is (T_even). If q=3, then r_i=4 and 9b023ed3d700 gives the local rank-4 triangle. If q>=4, put m=q-1>=3. Then f0f28f03b0d9 applies, and the exact contact belonging to E_j is its unique entrance x_j. Hence x_j belongs to R_i. If R_i and R_j met only at x_j, 5854d853a44b would force x_j to be an internal aligned joint of R_j, contradicting that x_j is the last vertex of R_j. Thus
  |V(R_i) intersect V(R_j)|>=2.

Now let r_i=2q-3. If equality holds in the plus-two bound, then
  r_j+r_{j+1}=2q-1,
so monotonicity and the upper bound q force
  r_j=q-1,
  r_{j+1}=q.
This is (T_odd). The case q=3 is impossible: then r_i=3 while 608468bb403b would give r_{j+1}<=r_i-1=2. Hence q>=4. If q=4 and E_{j+1}=h, 9b023ed3d700 gives the explicit rank-5 boundary triangle. Otherwise 9b00516e2965 applies; its exact contact of E_j is x_j, so the same unique-intersection argument with 5854d853a44b gives
  |V(R_i) intersect V(R_j)|>=2.

It remains to consider strict inequality in the plus-two bound. Integrality and the upper bound 2q force
  r_j+r_{j+1}=2q=r_i+3,
hence
  r_j=r_{j+1}=q.
This is (P_3). Again q=3 is impossible by 608468bb403b, so q>=4. The host path has length
  p=r_i-1=2q-4.

If an adjacent parent equals h, then its edge rank q also equals the host-last-edge rank p; hence q=2q-4 and q=4. The boundary-cycle alternative of 20ee63fa1617 applies.

Assume neither adjacent parent equals h. By 608468bb403b there are two distinct genuine exact contacts c_j,c_{j+1}. If their path-edge occurrence intervals overlap, a common host edge together with E_j,E_{j+1} forms a linear 3-cycle.

Suppose the intervals are disjoint, and name c_- the earlier contact and c_+ the later one. The separated-singleton theorem 2cc651f9fa5d gives
  q+q>=p+4,
and here equality holds. We now record the equality locations directly.

For the earlier contact, the terminal-suffix wrong-entrance argument gives
  b(c_-)>=p-q+2=q-2,
while a path vertex occupies at most two consecutive host edges, so
  a(c_-)>=q-3.
The prefix followed by the two adjacent parent edges is a wrong-entrance path for the later parent unless
  a(c_-)<=q-3.
Thus
  a(c_-)=q-3,
  b(c_-)=q-2,
and therefore
  c_-=g_{q-3} intersect g_{q-2}.

Disjointness gives
  a(c_+)>=q-1.
If c_+ is the unique entrance of its parent edge, the host prefix ending at c_+ has length a(c_+), so a(c_+)<=q-1. If c_+ is the opposite terminal, adjoining that parent edge gives a wrong-entrance path and the stronger bound a(c_+)<=q-2. Therefore
  a(c_+)=q-1,
and c_+ must be the unique entrance. A host-path vertex with first occurrence q-1 is either the private vertex of g_{q-1} or the joint
  g_{q-1} intersect g_q.
This proves the stated classification.
