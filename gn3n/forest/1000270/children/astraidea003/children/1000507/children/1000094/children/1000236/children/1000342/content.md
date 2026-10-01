# The doubled-cross size-gap outcome retains both local reverse pivots

## Statement

Let H be a minimum counterexample and let P|Q|R be a spanning three-cover minimizing the quadratic potential in a connected component of the pairwise-repartition graph containing no two-cover. Write P=(p_1,...,p_a), Q=(q_1,...,q_b), R=(r_1,...,r_c), with a>=b>=c>=2 and a>=b+2. Then either H has a proper Hamiltonian support W of order four or five with pc(H-W)=2, or there are an endpoint x of P and indices 1<=i<b, 1<=j<c such that all six ordered triples (q_{i+1},q_i,x), (q_{i+1},x,q_i), (r_{j+1},r_j,x), (r_{j+1},x,r_j), (r_j,q_i,x), (q_i,r_j,x) are tight.

## Body

By 209aa2be10c0, each endpoint x of P is noninsertable into the displayed orders of both Q and R. Fix one endpoint x and apply the failed-insertion normal form separately on Q and R. If either application has its first alternative, 0425e03e2aa3 gives a Hamiltonian four-set or the matching-block four-vertex obstruction; in the latter case adjoining the other endpoint of P gives a Hamiltonian five-set. In a minimum counterexample the complement of each such proper Hamiltonian support has path-cover number two.

It remains that both applications have the second alternative, at gaps q_i|q_{i+1} and r_j|r_{j+1}. The second alternative itself contains the comparison arcs e_i->f_i and f_{i+1}->f_i. In ordered-triple language these are exactly
(q_{i+1},q_i,x) and (q_{i+1},x,q_i),
and likewise
(r_{j+1},r_j,x) and (r_{j+1},x,r_j).

Now apply 0b012e2e3816 to the two second-alternative pivots. If one of its mixed four-vertex orders is tight, that four-set is a proper Hamiltonian support and again its complement has path-cover number two. Otherwise the theorem gives both cross triples
(r_j,q_i,x) and (q_i,r_j,x).
Together with the four pivot triples already retained, these are the asserted six tight triples. ∎