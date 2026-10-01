# Incidence-code constraint for a spanning linear path

## Statement

Let H be a 3-uniform hypergraph on 2ell+1 vertices and let C over F_2 be the binary span of its edge-incidence vectors. If H has a spanning linear path P_ell with joint set J of size ell-1, then 1_V + 1_J lies in C. Equivalently, for every vector y in C^perp one has |J intersect supp(y)| congruent to |supp(y)| mod 2.

## Body

Sum over F_2 the incidence vectors of the ell edges of a spanning linear path. Every non-joint vertex belongs to exactly one path edge, while every joint belongs to exactly two consecutive path edges and cancels. Thus the sum is exactly the characteristic vector of V\J, which over F_2 is 1_V+1_J. Since it is a sum of edge-incidence vectors, it belongs to C.

Taking inner product with any y in C^perp gives <y,1_V+1_J>=0, i.e. |supp(y)|+|J intersect supp(y)| is even.

For PG(d-1,2), hyperplane complements/equivalent dual-code words recover the hyperplane-parity conditions used in the P7 obstruction. This formulation suggests searching low-2-rank Steiner triple systems for coset/weight restrictions on possible joint sets before undertaking path enumeration.
