# Terminal-single packets obey both central-window and fixed-capacity rank profiles

## Statement


Let H be a finite linear r-graph with r>=3. Fix a vertex v of rank p and a maximum p-edge path P ending at v. Let e_1,...,e_k be distinct ascending nonspecial edges terminal at v, each of edge rank less than p and each having contact multiplicity one on P. Write
  q_i=phi(e_i)
and relabel so that q_1<=...<=q_k.

Then for every i,
  q_i >= max{
    ceil((8i+4r-14)/(6r-7)),
    ceil(((r-1)p+i+2r-3)/(2(r-1)))
  }.

Equivalently, the central-window lower profile controls the initial segment of the ordered packet, while the fixed-entrance capacity lower profile controls its dense upper tail. Their real-valued profiles cross at
  i_*=
  ((6r-7)(r-1)p+4r^2+4r-7)/(10r-9).

If x_i is the unique entrance of e_i, then
  sum_i phi(x_i)
  >= sum_i [
    max{
      ceil((8i+4r-14)/(6r-7)),
      ceil(((r-1)p+i+2r-3)/(2(r-1)))
    }-1
  ].

If, moreover, v has minimum vertex rank among the r-1 terminal vertices of every e_i, then the r-2 other terminals on each e_i have rank at least p and all off-v vertices are pairwise distinct across the family. Hence their total off-v rank is at least
  (r-2)pk
plus the displayed entrance-rank sum.

This simultaneously strengthens the two separate packet bounds 34f8dc7df3f6 and 5198e921de4f on their common terminal-single domain.


## Body


Fix i. Since q_1<=...<=q_i, the first i edges all have edge rank at most q_i.

First apply the fixed-entrance capacity bound a570a11f0001 at v. The first i edges belong to J_{q_i}(v), so
  i<=((6r-7)/8)q_i+(7-2r)/4.
Rearranging and using integrality gives
  q_i>=ceil((8i+4r-14)/(6r-7)).

Second apply the single-contact central-window theorem 6af906e32265 to the same first i edges on P. It gives
  i<=(r-1)(2q_i-p)-(2r-3).
Therefore
  q_i>=ceil(((r-1)p+i+2r-3)/(2(r-1))).

Both inequalities hold simultaneously, proving the maximum profile.

To locate the crossover of the underlying real-valued profiles, solve
  (8i+4r-14)/(6r-7)
  =((r-1)p+i+2r-3)/(2(r-1)).
After clearing denominators,
  (10r-9)i
  =(6r-7)(r-1)p+4r^2+4r-7,
which gives i_*.

Because e_i is ascending, its unique entrance x_i has
  phi(x_i)=q_i-1.
Summing the pointwise maximum profile gives the entrance-rank estimate.

Finally, under minimum-terminal assignment, linearity makes the sets e_i\{v} pairwise disjoint, and each e_i contains r-2 terminal vertices other than v, each of rank at least p. Adding their rank contribution proves the last assertion.
