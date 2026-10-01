# A perfect matching in a fixed-pair extension graph is exactly the two orientation classes

## Statement

Let H be a boundary tournament, let a,b be distinct vertices, and let X be a four-vertex set disjoint from {a,b}. Define a graph J on X by xy in E(J) exactly when H[{a,b,x,y}] is Hamiltonian. If J is a perfect matching, then the two fixed-pair orientation classes C_+={x in X:(a,x,b) is tight} and C_-={x in X:(b,x,a) is tight} both have order two, and the two edges of J are exactly C_+ and C_-. Consequently every cross pair y in C_+, z in C_- gives a non-Hamiltonian four-set {a,b,y,z}.

## Body

Boundary antisymmetry partitions X into C_+ and C_-. By bd3c8d17ca06, each orientation class is a clique of J. Since J is a perfect matching, no clique has order three, so |C_+|,|C_-|<=2. Their sizes sum to four, hence both have order two. Each class's unique pair is therefore an edge of J; as J has exactly two edges, these are precisely its matching edges. Every cross pair is a nonedge and so gives a non-Hamiltonian four-set.
