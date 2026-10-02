# Odd-edge bridge inequalities force synchronized crossing or global radius-three expansion

## Statement


In the order-thirteen mu=6 shell, let G be the Hamiltonian-support odd graph and J the graph on its nonisolated Hamiltonian six-sets joining supports at Johnson distance at most three. For every edge P--Q of G, with p=deg_G(P), q=deg_G(Q), a=deg_J(P), b=deg_J(Q), at least 14-p-q distinct G-edges join the proper J-neighborhoods of P and Q. Hence 14-p-q <= b+binom(a,2), 14-p-q <= a+binom(b,2), p<=b+1, and q<=a+1. If a=2, every legal single-transfer edge from P yields synchronized two-end support crossing for a three-label fixed-complement deletion family; in the subcase p,q<=2, b>=9 and every J-neighbor of Q has J-degree at least three. If no three-label synchronized-crossing producer exists anywhere in the shell, every G-vertex has degree at most two and delta(J)>=5, equivalently delta(Gamma)>=5 for the complementary deficient-support graph.


## Body


# Odd-edge bridge inequalities force synchronized crossing or global radius-three expansion

Work in the order-thirteen mu=6 shell. Let G be the Hamiltonian-support odd graph, and let J be the graph on nonisolated Hamiltonian six-sets in which two supports are adjacent when their Johnson distance is at most three. Complementation identifies J with the radius-three deficient-support graph Gamma.

Fix an edge P--Q of G with omitted label x, and write
p=deg_G(P), q=deg_G(Q), a=deg_J(P), b=deg_J(Q).

## Quantitative bridge inequality

For each y in P, edge-label surjectivity supplies a G-edge A_y--B_y labelled y. Relabel its endpoints so that |A_y intersect P|>=3. Then A_y is a proper J-neighbor of P. The other endpoint B_y contains at most two vertices of P, hence at least three vertices of Q, so B_y lies in the closed J-neighborhood of Q. It fails to be a proper neighbor only when B_y=Q, and this can happen for at most q-1 labels y.

Interchanging P and Q gives the symmetric construction. The twelve selected edges are distinct because their omitted labels are distinct. After discarding at most (q-1)+(p-1) edges incident with P or Q themselves, at least

E >= 14-p-q

distinct G-edges remain between N_J(P) and N_J(Q).

The odd graph G is C4-free: two distinct six-sets have at most one common disjoint six-set. If d_1,...,d_b are the degrees on the N_J(Q) side of the bridge bipartite graph, then

sum_j binom(d_j,2) <= binom(a,2).

Since d<=1+binom(d,2),

E <= b+binom(a,2),

and symmetrically

E <= a+binom(b,2).

Thus

14-p-q <= b+binom(a,2),
14-p-q <= a+binom(b,2).

Also every G-neighbor of P other than Q has the form (Q-{z}) union {x} and is a proper J-neighbor of Q. Hence

p-1<=b,  q-1<=a,

or equivalently p<=b+1 and q<=a+1.

## Degree-two states force synchronized crossing

Assume a=2. If max(p,q)>=3, choose A in {P,Q} with deg_G(A)>=3 and put X=V(H)-A. The exact odd-graph exchange model identifies the G-neighbors of A with Hamiltonian vertex deletions of X. Choose three good labels t_1,t_2,t_3 in X. The deletion covers

(X-{t_i}) | A

form a support-compatible three-label family with fixed Hamiltonian complement A. Fix a Hamilton order of A and arbitrary exact deletion covers at its two endpoints. The support-compatible-family crossing theorem says each endpoint cover is compatible with at most one family member, so one label t_i is support-incompatible with both endpoint covers. This is synchronized two-end crossing.

Now suppose p,q<=2. The bridge lower bound gives E>=10, while a=2 gives E<=b+1, hence b>=9. Since q<=2, low odd degree excludes degree-two J-neighbors of Q, so every J-neighbor of Q has degree at least three.

The same ten bridge edges also force synchronized crossing directly: their left endpoints lie among only two vertices of N_J(P), so one such vertex A is incident with at least five selected G-edges. Hence deg_G(A)>=5, and the preceding three-label argument applies to V(H)-A.

Therefore every J-degree-two state, equivalently every Gamma-degree-two D=1 state, yields synchronized two-end crossing. In the low-odd-degree branch the transfer target additionally has J-degree at least nine and no degree-two J-neighbor.

## Global minimum-degree consequence

Assume no three-label synchronized-crossing producer exists anywhere in the shell. Then deg_G(A)<=2 for every G-vertex A, since any vertex of degree at least three gives the three-label construction above.

Fix P in V(J) and choose a G-neighbor Q. The bridge inequality supplies at least ten edges between N_J(P) and N_J(Q). If deg_J(P)<=4, pigeonhole gives a vertex of N_J(P) incident with at least three selected G-edges, contradicting the global bound deg_G<=2. Thus deg_J(P)>=5. Since P was arbitrary,

delta(J)>=5.

Under complementation, delta(Gamma)>=5.

So the order-thirteen one-defect shell has the dichotomy: either synchronized two-end crossing is already produced, or the entire radius-three coupled graph has minimum degree at least five, with the stronger degree-two expansion conclusions above available locally.
