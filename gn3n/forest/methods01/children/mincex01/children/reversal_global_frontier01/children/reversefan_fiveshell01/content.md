# A complete reverse fan forces overlapping Hamiltonian five-sets

## Statement

Let H be a minimum counterexample and let T=(x,v,u) be a tight three-vertex path arising from a complete reverse fan, so in particular (x,v,u) is tight. Put L=V(H)-{x,v,u}. Define a graph J on L by ab in E(J) exactly when H[{x,v,u,a,b}] is Hamiltonian. Then alpha(J)<=2. Since |V(H)|>10, |L|>=8, so J has a vertex a of degree at least two. Consequently there exist distinct a,b,c in L such that both five-sets {x,v,u,a,b} and {x,v,u,a,c} are Hamiltonian; each has non-Hamiltonian path-cover-two complement.

## Body

# Proof

The ordered triple T=(x,v,u) is a tight path on three vertices. Apply the certified fixed-three-path extension theorem from smallset01 to T and any three distinct vertices a,b,c of L. At least one of the three five-sets T union {a,b}, T union {a,c}, T union {b,c} is Hamiltonian. Therefore every three vertices of L span an edge of J, equivalently alpha(J)<=2.

Minimum-counterexample calculus gives |V(H)|>10, hence |L|>=8. If every vertex of J had degree at most one, J would be a matching plus isolated vertices and would have an independent set of order at least ceil(|L|/2)>=4, contradicting alpha(J)<=2. Thus some a has two distinct neighbors b,c. By definition both T union {a,b} and T union {a,c} are Hamiltonian.

Each five-set is proper. If its complement were Hamiltonian, the two complementary Hamilton paths would form a spanning two-cover of H. Hence each complement is non-Hamiltonian; by minimality it has path-cover number two. ∎
