# A common oriented fixed pair makes every two outside labels a Hamiltonian four-set

## Statement

Let H be a boundary tournament, let a,b be distinct vertices, and let Y be a set of vertices disjoint from {a,b} with |Y|>=2. Suppose (b,y,a) is tight for every y in Y. Then for every distinct y,z in Y, the induced four-set {a,b,y,z} is Hamiltonian. More precisely, exactly one of (y,b,z) and (z,b,y) is tight; in the first case (y,b,z,a) is a tight Hamilton path and in the second case (z,b,y,a) is a tight Hamilton path. Consequently, if H is a minimum counterexample and {a,b,y,z} is proper, its complement is non-Hamiltonian with path-cover number two.

## Body

# Proof

Fix distinct y,z in Y. By hypothesis, both (b,y,a) and (b,z,a) are tight. Boundary antisymmetry on the ordered triple pair (y,b,z) and (z,b,y) says exactly one of them is tight.

If (y,b,z) is tight, then (y,b,z,a) is a tight Hamilton path on {a,b,y,z}, using the consecutive triples (y,b,z) and (b,z,a). If instead (z,b,y) is tight, then (z,b,y,a) is a tight Hamilton path, using (z,b,y) and (b,y,a). Thus every distinct y,z in Y yield a Hamiltonian four-set containing the fixed pair {a,b}.

For the minimum-counterexample consequence, if the four-set is proper and its complement were Hamiltonian, Hamilton paths on the four-set and on its complement would form a spanning two-cover, impossible. Minimum-counterexample calculus therefore gives a non-Hamiltonian complement of path-cover number two.
