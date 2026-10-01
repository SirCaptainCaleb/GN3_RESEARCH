# Any transversal of sharp-shell deletion covers is a forest or one odd support cycle

## Statement

Let H be a minimum counterexample in the sharp half-order shell n=2lambda+1. For each vertex v choose one lambda|lambda two-cover A_v|B_v of H-v. Form a simple graph J whose vertices are the distinct chosen Hamiltonian lambda-supports and whose edge e_v joins A_v to B_v. Then exactly one of the following holds: J is a forest, or J is a single odd cycle. In the cyclic case the cycle has all n selected edges.

## Body

The edge e_v is well-defined and the selected edges are distinct: a disjoint pair of lambda-sets determines its unique omitted vertex, since their union has order 2lambda=n-1.

Fix a ground vertex u in V(H), and let C_u be the set of support-vertices S of J with u in S. For the edge e_u=A_uB_u, neither endpoint contains u. For every other selected edge e_v=A_vB_v with v different from u, the two supports partition V(H)-{v}, so exactly one of A_v,B_v contains u. Therefore
delta_J(C_u)=E(J)-{e_u}.
In particular J-e_u is bipartite, with bipartition C_u and its complement, and the endpoints of e_u lie on the same side of this displayed bipartition.

This holds for every selected edge e.

Suppose first that J is bipartite. If some edge e lay on a cycle, then after deleting e its endpoints would remain connected by the rest of that even cycle. In every bipartition of J-e those endpoints would therefore lie on opposite sides, contradicting the displayed bipartition in which they lie on the same side. Hence every edge is a bridge, so J is a forest.

Suppose instead that J is non-bipartite, and choose an odd cycle C. For any edge e not belonging to C, the graph J-e would still contain C and would remain non-bipartite, contradicting the fact proved above that J-e is bipartite. Hence every edge of J lies on C. Thus J is exactly that odd cycle.

There are n selected edges, one for each ground vertex, so in the cyclic case C has length n. ∎