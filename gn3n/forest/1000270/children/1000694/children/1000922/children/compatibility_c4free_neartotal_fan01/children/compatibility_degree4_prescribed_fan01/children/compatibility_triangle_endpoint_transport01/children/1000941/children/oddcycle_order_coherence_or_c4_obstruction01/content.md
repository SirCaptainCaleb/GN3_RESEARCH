# Balanced odd-cycle deletion supports admit a global order unless four vertices form an alternating order obstruction

## Statement

Assume the exceptional spanning odd-cycle support configuration on n=2k+1 deletion labels, with balanced Hamiltonian supports S_i of order k arranged cyclically. The Hamilton orders on the S_i induce a well-defined orientation of every nonedge of the ground cycle C_n. On each S_i this orientation is transitive. Hence either this orientation is acyclic, in which case one global linear order of V(H) restricts to the Hamilton order on every S_i, or it contains a directed induced cycle. For n>5 every such shortest directed cycle has length four and is supported on the endpoints of two disjoint edges of the ground cycle. Thus the only obstruction to global order coherence is a directed C4 in the complement of C_n.

## Body

Assume the exceptional spanning odd-cycle support configuration on n=2k+1 labels. Index the balanced Hamiltonian support sets cyclically as S_i, so consecutive selected deletion covers share one support and the support sets satisfy
S_{i+2}=S_i-{d_{i+1}}+{d_i}
with indices modulo n.

Because adjacent selected deletion covers are fully compatible in the residual branch, the displayed Hamilton orders on S_i and S_{i+2} agree on the common set S_i intersect S_{i+2}, of order k-1.

Define the ground cycle C_n on vertices d_0,...,d_{n-1}. Every S_i is an alternating maximum independent set of C_n. For every pair u,v that is a nonedge of C_n, choose any support S_i containing both and orient uv according to their relative order in the Hamilton order of S_i.

This orientation is well-defined. The supports containing a fixed nonadjacent pair u,v form a connected interval in the step-two cyclic ordering of the supports, and consecutive such supports have Hamilton orders agreeing on their overlap. Therefore the relative order of u,v is independent of the chosen support. On each S_i the induced orientation is exactly its Hamilton order and is therefore transitive.

Suppose first that the resulting orientation of the complement of C_n is acyclic. Any topological ordering of this orientation restricts to the unique Hamilton order on every S_i, so all selected balanced Hamilton orders are restrictions of one global linear order of V(H). In particular, every three vertices lying in one support appear in the global order as a tight consecutive-or-not-consecutive ordered triple according to that Hamilton order; equivalently all order information on pairs avoiding ground-cycle adjacency is globally coherent.

Suppose instead that the orientation has a directed cycle, and choose one of minimum length. Any chord of its underlying undirected cycle would, according to one of its two possible orientations, create a shorter directed cycle. Thus the shortest directed cycle is induced in the complement of C_n.

For n>5, every induced cycle of the complement of C_n has length four. Indeed, if r>=6 vertices induced a chordless r-cycle in the complement, then the induced subgraph of C_n on those r vertices would be the complement of C_r and hence have degree r-3>=3, impossible because every induced subgraph of C_n has maximum degree at most two. An induced 5-cycle in the complement would be self-complementary, so the same five vertices would induce a C5 in C_n; for n>5 this cannot occur because C_n has no proper cyclic component. Hence r=4.

A four-set induces a C4 in the complement of C_n exactly when, in the ground cycle, it consists of the endpoints of two disjoint cycle edges. Therefore the only obstruction to global order coherence is a directed C4 supported on the endpoints of two disjoint ground-cycle edges.