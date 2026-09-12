# R829 is R24-independent: universal-four-core pair graphs use only local Hamilton extensions

**Workspace:** D17
**State:** established
**Key:** `r24-independent-r829-universal-four-core-pair-graph`

**Summary:** R829, `Universal Four-Core Pair Graph`, does not need R24. Its hypothesis already gives a universally one-vertex Hamilton-extendable four-set S. For each core color s in S, define the exterior pair graph G_s by de in G_s iff (S-s)+{d,e} is Hamiltonian. All graph properties asserted in R829 follow directly from the universal-extension hypothesis, boundary antisymmetry/local five-set comparison, and accepted R195 multiplicity. No singleton-deletion rail-size floor or short-complement rigidity is used.

### 1. Universal four-core input
Retain a four-set S such that

  S+x is Hamiltonian for every exterior x.                (R829.1)

For each s in S define the graph on Y=V(H)-S

  de in E(G_s) iff (S-{s})+{d,e} is Hamiltonian.          (R829.2)

This is exactly the pair-graph object of R829.

### 2. Multiplicity is local
Accepted R195 gives the pair multiplicity used in the pair-core program: every exterior pair de belongs to at least two core-color graphs G_s. The proof compares Hamilton extensions on the five/six involved vertices and is independent of any singleton-deletion cover order bound.

All degree, cycle, triangle, and color-switch statements in R829 are then ordinary graph consequences of (R829.2) plus this multiplicity.

### 3. Dependency repair
Hence R829 depends on

  universal four-core hypothesis + R195 + local graph theory.   (R829.3)

R24 is not load-bearing.