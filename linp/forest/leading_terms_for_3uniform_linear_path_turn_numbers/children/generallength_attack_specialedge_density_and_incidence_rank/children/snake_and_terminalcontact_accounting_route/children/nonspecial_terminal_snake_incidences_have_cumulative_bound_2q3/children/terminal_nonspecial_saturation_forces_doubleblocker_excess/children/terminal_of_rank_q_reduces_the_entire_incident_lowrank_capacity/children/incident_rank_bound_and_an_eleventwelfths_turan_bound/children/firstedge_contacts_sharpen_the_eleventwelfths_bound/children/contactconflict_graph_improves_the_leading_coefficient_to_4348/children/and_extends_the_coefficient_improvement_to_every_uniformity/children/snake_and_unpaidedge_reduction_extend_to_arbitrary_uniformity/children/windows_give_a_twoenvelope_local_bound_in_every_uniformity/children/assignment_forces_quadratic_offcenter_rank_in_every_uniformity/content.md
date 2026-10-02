# Minimum-rank terminal assignment forces quadratic off-center rank in every uniformity

## Statement


Let H be a finite linear r-graph with r>=3. Fix a vertex v of rank p and a maximum p-edge path P ending at v. Let e_1,...,e_k be distinct ascending nonspecial edges terminal at v, all of edge rank less than p, and suppose every e_i has contact multiplicity one on P. Write q_i=phi(e_i), let x_i be the unique entrance of e_i, and relabel so that
  q_1<=...<=q_k.

Then for every i,
  q_i >= ceil(((r-1)p+i+2r-3)/(2(r-1))),
and therefore
  sum_{i=1}^k phi(x_i)
  >= sum_{i=1}^k [
       ceil(((r-1)p+i+2r-3)/(2(r-1)))-1
     ]
  >= kp/2 + k(k-1)/(4(r-1)).

If, in addition, v has minimum vertex rank among the r-1 terminal vertices of every e_i, then all (r-1)k vertices in union_i(e_i\{v}) are distinct, and the r-2 terminal vertices of e_i other than v all have rank at least p. Hence
  sum_{z in union_i(e_i\{v})} phi(z)
  >= ((2r-3)/2)pk + k(k-1)/(4(r-1)).

In particular this applies after assigning any family of globally unpaid signature-(0,1,...,1) ascending edges to a terminal of minimum vertex rank. For r=3 the entrance-rank conclusion becomes
  sum_i phi(x_i) >= kp/2+k(k-1)/8,
the same numerical packet bound as the certified 3-uniform minimum-terminal lemma on the terminal-single subclass.


## Body


Order the edges by q_1<=...<=q_k. For each i, the edges e_1,...,e_i all have rank at most q_i and contact multiplicity one on the fixed maximum p-edge path P. The central-window theorem 6af906e32265 therefore gives
  i <= B_r(p,q_i)
    = (r-1)(2q_i-p)-(2r-3).
The right side is positive because i>=1. Rearranging,
  2(r-1)q_i >= (r-1)p+i+2r-3,
and integrality gives
  q_i >= ceil(((r-1)p+i+2r-3)/(2(r-1))).

Since e_i is ascending with unique entrance x_i,
  phi(x_i)=q_i-1.
Summing the ceiling bounds proves the first displayed estimate. Dropping the ceilings gives
  sum_i phi(x_i)
  >= kp/2
     + [sum_i i + k(2r-3)]/[2(r-1)]
     - k
  = kp/2 + k(k-1)/(4(r-1)).

Any two distinct edges in the family already share v. By linearity they share no other vertex, so the sets e_i\{v} are pairwise disjoint. Each nonspecial r-edge has one unique entrance and r-1 terminal vertices. Under the minimum-rank assumption on v, the r-2 terminals other than v in every e_i have vertex rank at least p. Adding their total contribution (r-2)pk to the entrance-rank estimate yields
  ((r-2)+1/2)pk + k(k-1)/(4(r-1))
  = ((2r-3)/2)pk + k(k-1)/(4(r-1)).

Finally, an edge of signature (0,1,...,1) in the general contact-multiplicity reduction has multiplicity one at every terminal. Assigning each such edge to one of its minimum-rank terminals therefore satisfies the hypotheses at every assigned center.
