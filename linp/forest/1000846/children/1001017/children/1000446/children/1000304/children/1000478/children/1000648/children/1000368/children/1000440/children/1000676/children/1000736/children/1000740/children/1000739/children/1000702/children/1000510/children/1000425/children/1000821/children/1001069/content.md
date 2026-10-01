# The exact 4555 normal form is a crossed two-pole incidence rectangle

## Statement

In the p=5 charged pattern 4555, assume the exact normal form of b8d0dfa0af07. Let
  R=(r_1,r_2,r_3)
be the canonical rank-four entrance rail, with
  s=r_1∩r_2,
and let the two crossed rank-five edges be
  h_i={v,a_i,b_i}, i=1,2,
where
  {a_1,a_2}=r_1\{s},
  {b_1,b_2}=r_2\{s}.
Let j be the unique joint-type rank-five competitor, so {v,s}⊂j.

Then:
1. h_1,h_2 induce a perfect matching between r_1\{s} and r_2\{s};
2. j meets both rail edges r_1,r_2 at the common pole s;
3. j meets both crossed edges h_1,h_2 at the common pole v.

Thus the five-edge incidence pattern on
  {r_1,r_2,h_1,h_2,j}
is a rigid crossed rectangle with poles s and v. It is not a linear 4-cycle, because the nonconsecutive rail edges r_1,r_2 already meet at s.

## Body

By b8d0dfa0af07, the crossed edges are
  h_i={v,a_i,b_i},
where a_1,a_2 are exactly the two vertices of r_1\{s} and b_1,b_2 are exactly the two vertices of r_2\{s}. Hence the h_i give a perfect matching between those two 2-sets.

The joint competitor j contains both v and s. Since every rank-five competitor contains v and the hypergraph is linear, j∩h_i={v}. Since s lies in both r_1 and r_2, j meets each rail edge at s; linearity forbids any further intersection with either rail edge.

Therefore the incidence pattern is exactly the claimed crossed rectangle with two poles s and v. The warning about cycles is essential: r_1 and r_2 are adjacent rail edges and already share s, so r_1,h_1,r_2,h_2 is not a linear cycle under the standard nonconsecutive-disjointness convention.
