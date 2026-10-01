# Compatible two-rail criterion for Hamiltonicity of a one-bit Boolean lift

## Statement

Let B be a finite nonzero subset of an elementary abelian 2-group with |B|=2r+1. Suppose H(B) has two spanning P_r paths P and Q sharing a common endpoint vertex b. Let A=((B union {0}) x F_2)\{(0,0)} be the full one-bit lift. If every even subhypergraph of P union Q contains an even number of Q-edges, then H(A) has a spanning P_{2r+1}. In particular it is enough that the binary incidence vectors of the 2r edges in P union Q are linearly independent.

## Body

Write the one-bit lift vertices as (u,epsilon), u in B, epsilon in F_2, together with x=(0,1). A lifted cross triple above a base triple e={u,v,w} is legal exactly when epsilon_u+epsilon_v+epsilon_w=0.

We seek a bit function sigma:B->F_2 such that
  sum_{u in e} sigma(u)=0 for every e in P,
and
  sum_{u in e} sigma(u)=1 for every e in Q.
Let M be the binary edge-vertex incidence matrix of the hypergraph P union Q, with one row per selected base edge, and let eta be the right-hand side which is 0 on P-edges and 1 on Q-edges. The system M sigma = eta is solvable if and only if eta is orthogonal to every vector in the left kernel of M. A left-kernel vector is exactly the indicator of an edge subset D subset P union Q in which every base vertex has even degree, i.e. an even subhypergraph. Orthogonality says precisely
  |D intersect E(Q)| == 0 mod 2.
Thus the stated even-subhypergraph condition is necessary and sufficient for the bit system. If the 2r row vectors are linearly independent then the left kernel is trivial, so the condition holds automatically.

Fix a solution sigma. Lift P by assigning to every base label u the copy (u,sigma(u)). The parity-zero equations on P make every lifted P-edge legal. Since P is spanning on B, this lifted rail uses exactly one copy of every u in B.

Lift Q using the complementary copies (u,1+sigma(u)). For any Q-edge e={u,v,w},
  (1+sigma(u))+(1+sigma(v))+(1+sigma(w))
  =1+sum_{z in e}sigma(z)
  =1+1=0,
so every complementary Q-edge is legal. This second rail uses exactly the other copy of every base label and is disjoint from the first rail.

Orient both base paths so that their common endpoint b is terminal. The lifted rails then end at (b,sigma(b)) and (b,1+sigma(b)). Insert the vertical block
  {(0,1),(b,0),(b,1)}
between the two rails, reversing the second rail after the connector. Consecutive edges meet in exactly the required endpoint copy; the two rails are otherwise vertex-disjoint; and the vertical block contains the new vertex x and meets each rail only at its endpoint. Therefore the concatenation is a linear path with
  r + 1 + r = 2r+1
edges.

Its vertex set is all 2|B|+1=4r+3 vertices of A, so it is spanning. This proves the criterion.
