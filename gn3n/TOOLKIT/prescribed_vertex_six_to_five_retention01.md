# A Hamiltonian six-support reduces to a five-support retaining any prescribed vertex

**Summary:** A proper Hamiltonian six-set with two-coverable complement can be reduced to a Hamiltonian five-set retaining any prescribed vertex, while its new complement remains non-Hamiltonian of path-cover number two.

## Statement

Let H be a minimum counterexample, let U be a proper Hamiltonian six-vertex set, and suppose K=H-U is non-Hamiltonian with path-cover number two. For every prescribed vertex a in U, there exists d in U-{a} such that U-{d} is Hamiltonian, contains a, and H-(U-{d})=K+d is non-Hamiltonian with path-cover number two.

## Body

Fix a Hamilton path on U. At least one endpoint differs from the prescribed vertex a; call it d. Deleting d leaves an inherited Hamilton path on U-{d}. By [[ham6goodsquare01]], adjoining either Hamilton-path endpoint to K gives a non-Hamiltonian induced subtournament of path-cover number two. Thus K+d has path-cover number two and U-{d} retains a.

## Metadata

- ID: prescribed_vertex_six_to_five_retention01
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
