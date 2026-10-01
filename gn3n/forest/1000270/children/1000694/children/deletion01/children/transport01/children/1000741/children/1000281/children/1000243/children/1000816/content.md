# From order eighteen every Phi-minimal three-cover yields order disagreement or a Hamiltonian four-set with path-cover-two complement

## Statement

Let H be a minimum counterexample of order n>=18, and let C=A|B|X be a spanning three-cover minimizing Phi in a connected component of the pairwise-repartition graph containing no cover with fewer than three paths. Then either H contains order disagreement, or H contains a proper Hamiltonian four-vertex set W such that H-W is non-Hamiltonian with path-cover number two.

## Body

Apply 4f8d912449ad. If it yields explicit order disagreement, we are done. Otherwise every component of C has order at least six. Let X be any one component and let E be the four displayed endpoints of the other two components A and B. Since |A|,|B|>=6, these are four distinct vertices outside X. Apply 8b213699c60c to the core V(X) and root set E. It gives either explicit order disagreement or a Hamiltonian four-set W containing at least two roots. In the latter case W is proper because n>=18. If H-W were Hamiltonian, a Hamilton path on W together with a Hamilton path on H-W would be a spanning two-cover of H, contradicting that H is a counterexample. Hence H-W is non-Hamiltonian; by minimum-counterexample calculus mincex01 it has path-cover number exactly two. This gives the Hamiltonian four-set alternative.