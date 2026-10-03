# A Hamiltonian one-vertex enlargement forces every complementary deletion cover to cross the underlying cut

**Summary:** A Hamiltonian one-vertex enlargement forces every complementary deletion cover to cross the underlying cut.

## Statement

Let H be a boundary tournament with path-cover number greater than two, let v be a vertex, and let V(H)-{v}=A disjoint-union B with A,B nonempty. If H[A union {v}] is Hamiltonian, then every two-path cover T of H-v contains an ordinary path edge with one endpoint in A and the other in B. Equivalently, no two-cover of H-v respects the support bipartition A|B.

## Body

Let T=T_1|T_2 be a two-cover of H-v and suppose no ordinary path edge of either displayed component crosses A|B. Along a tight path, if vertices from both A and B occurred then some consecutive ordinary path edge would cross the cut. Hence each T_i is contained entirely in one side. Since A and B are both nonempty and T_1,T_2 together cover all of H-v, after relabelling T_1 is a Hamilton path on A and T_2 is a Hamilton path on B. By hypothesis H[A union {v}] is Hamiltonian; choose a Hamilton path R on A union {v}. Then R|T_2 is a spanning two-path cover of H, contradicting pc(H)>2. Therefore every two-cover of H-v must contain an ordinary edge with endpoints on opposite sides of A|B. No minimum-counterexample, endpoint, component-size, or permanent-internal hypothesis is used.

## Metadata

- ID: hamiltonian_enlargement_forces_cut_edge01
- Kind: toolkit
- Version: 2
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Toolkit status: Promoted
