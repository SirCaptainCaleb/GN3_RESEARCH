# Every quadratic-minimal 3|5|5 profile lies on a nontrivial neutral cycle

**Summary:** At a Phi-minimal 3|5|5 state, the 3-side has distinct neutral endpoint rotations with each 5-side; hence the finite equal-Phi 3|5|5 state graph has minimum degree at least two and contains a cycle.

## Statement

Let H be a minimum counterexample and let T|A|B be a Phi-minimal spanning three-cover with |T|=3 and |A|=|B|=5. Then T|A admits a nontrivial equal-Phi repartition of orders 5|3, and independently T|B admits another such repartition. The two resulting three-covers are distinct and still have profile 3|5|5. Consequently, in the graph of Phi-minimal 3|5|5 covers in the same pairwise-repartition component, every vertex has degree at least two; in particular every connected component contains a cycle of length at least three.

## Body

Write A=(a1,a2,a3,a4,a5). If T union {a1} or T union {a5} were Hamiltonian, then T|A would repartition from orders (3,5) to (4,4), changing the quadratic contribution by 16+16-9-25=-2, contradicting Phi-minimality. Hence both endpoint four-extensions are non-Hamiltonian. By [[three_vertex_component_long_neighbor_rotation01]], T union {a1,a5} is Hamiltonian and (a2,a3,a4) is an inherited tight path, so T|A has a nontrivial neutral repartition (3,5)->(5,3). The same argument with B gives a second neutral neighbor. The two neighbors are distinct because in the first the new 3-side is contained in A, while in the second it is contained in B, and A,B are disjoint. Every equal-Phi neighbor is again Phi-minimal in the same repartition component. Therefore every vertex of the finite graph of Phi-minimal 3|5|5 states has at least two distinct neighbors. Every finite graph of minimum degree at least two contains a cycle; because the repartition graph is simple, the cycle has length at least three.

## Metadata

- ID: minimal_355_profile_has_a_neutral_cycle01
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
