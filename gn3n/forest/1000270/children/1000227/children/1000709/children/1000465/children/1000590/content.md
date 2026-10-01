# The order-thirteen radius-three deficient-support graph has no two-regular component

## Statement

Let H be a minimum counterexample of order thirteen with mu=6, and let Gamma be the graph of deficient seven-supports joined at Johnson distance at most three. Then Gamma has no connected component in which every vertex has degree two. Indeed, a hypothetical two-regular component has the sliding-triple form S_i=T_{i-1} disjoint-union T_i. For each i and each r in T_{i+1}, the legal transfer support S_i union {r} is a Gamma vertex at distance 1+|T_{i-1} intersect T_{i+2}| from R_{i+2}. The three choices of r would give three distinct neighbors of R_{i+2} unless T_{i-1}=T_{i+2}. Hence T_{i+3}=T_i for all i, forcing the component to be a 3-cycle. Such a 3-cycle is impossible by the surjective odd-graph edge-label model: a label outside its three Hamiltonian support triples produces a nonisolated Hamiltonian support within radius three and then a third neighbor of one cycle vertex.

## Body

# The order-thirteen radius-three deficient-support graph has no two-regular component

Let H be a minimum counterexample of order thirteen with mu=6. Let Gamma be the graph whose vertices are deficient seven-supports and whose edges join supports at Johnson distance at most three.

Assume for contradiction that one connected component of Gamma is 2-regular. Write its distinct cyclic vertices as
R_0,R_1,...,R_{m-1},
with indices modulo m, and let
S_i=V(H)-R_i
be the Hamiltonian six-support complementary to R_i.

By the sliding-triple theorem, there are three-sets T_i such that
S_i=T_{i-1} disjoint-union T_i,
every three consecutive T-sets are pairwise disjoint, and every vertex of
T_{i-2} union T_{i+1}
is a Hamiltonian deletion of R_i.

## 1. Degree two forces period three

Fix i and put
alpha_i=|T_{i-1} intersect T_{i+2}|.

For each r in T_{i+1}, the vertex r lies in R_i and is a Hamiltonian deletion of R_i. The one-defect transfer theorem therefore makes
P_r=S_i union {r}
a deficient seven-support, hence a vertex of Gamma.

The three sets P_r, r in T_{i+1}, are distinct.

Compare P_r with R_{i+2}. We have
R_{i+2}=V(H)-(T_{i+1} union T_{i+2})
and
P_r=T_{i-1} union T_i union {r}.

The vertex r belongs to T_{i+1}, so it is not in R_{i+2}. The whole triple T_i lies in R_{i+2}, because T_i is disjoint from both T_{i+1} and T_{i+2}. The triple T_{i-1} is disjoint from T_{i+1}, and exactly alpha_i of its vertices lie in T_{i+2}. Hence
|P_r intersect R_{i+2}|=3+(3-alpha_i)=6-alpha_i.

Both supports have order seven, so
d_J(P_r,R_{i+2})
 =7-|P_r intersect R_{i+2}|
 =1+alpha_i.

If alpha_i<=2, then all three distinct supports P_r are adjacent to R_{i+2} in Gamma. None equals R_{i+2}, since their Johnson distance is positive. Thus R_{i+2} has at least three neighbors, contradicting the assumption that its component is 2-regular.

Therefore alpha_i=3. Since both T_{i-1} and T_{i+2} have order three,
T_{i-1}=T_{i+2}.

This holds for every i, so
T_{i+3}=T_i
for every i. Consequently
S_{i+3}=S_i
and
R_{i+3}=R_i.

Because the displayed R_i are the distinct vertices of a simple cycle, the component can therefore only have length three.

## 2. A three-cycle is impossible

Assume now that the component is the 3-cycle R_0,R_1,R_2. Then T_0,T_1,T_2 are pairwise disjoint triples. Let
C=V(H)-(T_0 union T_1 union T_2),
so |C|=4.

The three Hamiltonian complements are
S_0=T_2 union T_0,
S_1=T_0 union T_1,
S_2=T_1 union T_2,
and none contains a vertex of C.

Fix c in C. In the certified sharp half-order odd-graph model, every vertex of H occurs as an edge label. Hence there is an odd-graph edge
A--B
labelled c: A and B are disjoint Hamiltonian six-sets and
A union B=V(H)-{c}.

The six vertices of S_0 are partitioned between A and B, so one endpoint, say A, meets S_0 in at least three vertices. Therefore
d_J(A,S_0)<=3.

Because A lies on an odd-graph edge, A is a nonisolated Hamiltonian support. Its deficient complement is therefore a vertex of Gamma. Complementation preserves Johnson distance, so this Gamma vertex is at distance at most three from R_0. Since the component of R_0 is assumed to be exactly the 3-cycle, A must equal one of S_0,S_1,S_2; write A=S_j.

Then
B=V(H)-{c}-S_j=R_j-{c}.
For a 3-cycle,
R_j=C disjoint-union T_{j+1},
so
B=(C-{c}) disjoint-union T_{j+1}.

Compare B with
S_{j+1}=T_j disjoint-union T_{j+1}.
Their intersection is exactly T_{j+1}, of order three, and hence
d_J(B,S_{j+1})=3.

The support B is Hamiltonian and nonisolated, so its deficient complement is a Gamma vertex adjacent to R_{j+1}. But B is not any of S_0,S_1,S_2, because B contains three vertices of C while those supports contain none. Thus R_{j+1} has a third neighbor outside the alleged 3-cycle, contradicting degree two.

This contradiction eliminates the last possibility.

Therefore Gamma has no 2-regular connected component. Equivalently, every connected component of the order-thirteen radius-three deficient-support graph contains a state of degree at least three. ∎
