# Leaf-support endpoint rigidity under support-incompatible deletions

In the forest case, a leaf deletion cover H-x=P|Q forces each endpoint deletion of Q either to use a direct P-to-(Q-y) mixed edge or to Hamiltonize (Q-y)+x. If neither endpoint deletion crosses P to Q, the two restored Hamilton paths are forced into a four-pattern near-end insertion menu; absent an order disagreement or a local backward traversal at an end edge of Q, x must occupy opposite extreme endpoints in the two restorations.

Let H be a minimum counterexample, choose one deletion cover F_v for each vertex v, and suppose the selected support graph J is a forest. Let e_x=PQ be a leaf edge with P the leaf support, and write Q=(q_0,...,q_m), m>=2.

For y in {q_0,q_m}, the selected deletion cover F_y is support-incompatible with F_x on H-{x,y}. Put B=Q-{y}. The endpoint-comparison lemma gives at least two path edges of F_y joining distinct classes of P | B | {x}. If F_y has no edge joining P directly to B, then every interclass edge is incident with x. Since x lies on one path of the two-cover F_y, at most two path edges are incident with x. Hence there are exactly two interclass edges, and the endpoint-comparison lemma yields that B union {x} is Hamiltonian.

Consequently, if neither endpoint deletion F_{q_0},F_{q_m} contains a direct edge from P to the surviving part of Q, then both L=(Q-{q_0}) union {x} and R=(Q-{q_m}) union {x} are Hamiltonian supports.

Assume Hamilton orders of L and R preserve the inherited relative order of the surviving Q-vertices. Since Q union {x} cannot be Hamiltonian, the insertion position of x in L must be either before q_1 or between q_1 and q_2; any later insertion permits q_0 to be prepended. Dually, the insertion position of x in R must be either after q_{m-1} or between q_{m-2} and q_{m-1}; any earlier insertion permits q_m to be appended.

Thus the no-crossing, order-preserving case has only four insertion patterns. Moreover, if L begins (q_1,x,q_2,...), then (q_0,q_1,x) is non-tight and therefore (x,q_1,q_0) is tight. If R ends (...,q_{m-2},x,q_{m-1}), then (x,q_{m-1},q_m) is non-tight and therefore (q_m,q_{m-1},x) is tight.

Hence, unless one obtains a direct P-Q mixed edge, an order disagreement, or one of these explicit backward end-edge traversals, the only surviving pattern is L=(x,q_1,...,q_m) and R=(q_0,...,q_{m-1},x).

The remaining mathematical question is whether this opposite-extreme restoration pattern, together with the boundary-reversal triples forced by H-x=P|Q, yields defect compression, quadratic descent, or a bounded mixed Hamiltonian support.
