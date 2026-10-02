# Double-frozen deletion states are isolated odd edges with twelve forced radius-three bridge edges

## Statement


In the order-thirteen mu=6 shell, an exact deletion state H-x=P|Q is double-frozen at x exactly when P--Q is an isolated edge of the Hamiltonian-support odd graph G. For either deficient support P union {x} or Q union {x}, every Johnson-radius-three neighbor has degree at least three. More quantitatively, if J is the radius-three graph on nonisolated Hamiltonian six-supports and a=deg_J(P), b=deg_J(Q), then the twelve labels in P union Q force twelve distinct G-edges between the proper J-neighborhoods of P and Q. These bridge edges are C4-free, so 12<=b+binom(a,2) and 12<=a+binom(b,2). Hence max(a,b)>=5; if a=2,3,4 then b>=11,9,6 respectively, with symmetric conclusions.


## Body


# Double-frozen deletion states are isolated odd edges with twelve forced radius-three bridge edges

Work in the order-thirteen mu=6 shell, where maximum tight-path order is six and the exact odd-graph exchange model applies.

Let
H-x=P|Q
be an exact 6|6 deletion cover. Say the state is double-frozen at x when P and Q are Hamiltonian but, for every p in P and q in Q,
(P-{p}) union {x}
and
(Q-{q}) union {x}
are non-Hamiltonian.

## Double freezing is exactly an isolated odd edge

In the Hamiltonian-support disjointness graph G, P and Q are adjacent with edge-label x.

Let B be any Hamiltonian six-set disjoint from P. Since
V(H)=P disjoint-union Q disjoint-union {x},
B is a six-subset of Q union {x}, so
B=(Q union {x})-{v}
for some v in Q union {x}. Double freezing says the only Hamiltonian such deletion is v=x, giving B=Q. Hence deg_G(P)=1. Symmetrically deg_G(Q)=1. Thus P--Q is an isolated edge component.

Conversely, suppose P--Q is an isolated G-edge with unique omitted label x. If for some q in Q the set
(Q-{q}) union {x}
were Hamiltonian, it would be another Hamiltonian six-set disjoint from P, hence a second G-neighbor of P. Contradiction. The same argument on the other side shows double freezing. Thus the two notions are equivalent.

## Frozen supports cannot border radius-three equality

Put R=P union {x}; its complement Q is Hamiltonian, so R is deficient. Let R' be a Johnson-radius-three deficient-support neighbor of R. If deg_Gamma(R')=2, degree-two rigidity makes the acquired set
Y=R-R'
a three-set and says that for every s in Y,
(R-{s}) | Q
is the support partition of every exact cover of H-s. In particular R-{s} is Hamiltonian for all three s in Y.

But freezing says x is the unique Hamiltonian deletion of R. Impossible. Therefore every radius-three neighbor of R has degree at least three. The argument for Q union {x} is symmetric.

## Twelve label bridges

Let J be the graph on nonisolated vertices of G joining supports at Johnson distance at most three. Put
a=deg_J(P), b=deg_J(Q).

Fix y in P. Edge-label surjectivity supplies an odd edge A--B labelled y, with
A union B=V(H)-{y}.
The five vertices P-{y} are split between A and B. Rename the endpoints so
|A intersect P|>=3.
Then
d_J(A,P)<=3,
and A!=P because y is in P but not A. So A is a proper J-neighbor of P.

The other endpoint B contains at most two P-vertices. Since B has six vertices and at most x lies outside P union Q, B contains at least three Q-vertices. Hence
d_J(B,Q)<=3.
Also B!=Q: otherwise A=(P-{y}) union {x}, non-Hamiltonian by freezing. Therefore B is a proper J-neighbor of Q.

Thus each y in P labels an odd edge from N_J(P) to N_J(Q). Interchanging P,Q gives one for every y in Q. Edge labels are unique, so these twelve selected edges are distinct.

The odd graph G is C4-free: two distinct six-sets have at most one common disjoint six-set. Therefore the selected bipartite bridge graph between N_J(P) and N_J(Q) is C4-free.

Let d_1,...,d_b be its degrees on the Q side. Any pair of left vertices has at most one common right neighbor, so
sum_j binom(d_j,2)<=binom(a,2).
Since d<=1+binom(d,2),
12<=sum_j d_j<=b+binom(a,2).
Symmetrically,
12<=a+binom(b,2).

Consequently max(a,b)>=5. More explicitly, a=2 forces b>=11; a=3 forces b>=9; a=4 forces b>=6, and the symmetric bounds hold after exchanging P,Q.

Thus double freezing is not a locally trapped low-expansion phenomenon: it is exactly an isolated odd edge whose twelve labels force substantial radius-three expansion on the surrounding support neighborhoods.
