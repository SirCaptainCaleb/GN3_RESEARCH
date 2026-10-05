# Every ten-vertex boundary tournament has a two-cover

**Summary:** Every boundary tournament on ten vertices has two complementary Hamiltonian five-subsets and hence path-cover number at most two.

## Statement

Let H be a boundary tournament on ten vertices. Then pc(H)≤2; in fact some complementary five-subsets are both Hamiltonian.

## Body

By [[smallset01]], every six-vertex set contains at least four Hamiltonian five-subsets. Let (G) be the number of Hamiltonian five-subsets of (V(H)). Count incidences ((F,S)) with (|F|=5), (|S|=6), (Fsubset S), and (H[F]) Hamiltonian. Each of the (inom{10}{6}=210) six-sets contributes at least four incidences, while each Hamiltonian five-set lies in exactly five six-sets. Hence
[
5Gge4inom{10}{6}=840,
]
so (Gge168).

The (252) five-subsets split into (126) complementary pairs. If no complementary pair were both Hamiltonian, at most one member of each pair could be counted, giving (Gle126), contradiction. Thus some complementary five-subsets are both Hamiltonian, yielding a spanning two-cover.

## Metadata

- ID: ten_vertex_boundary_tournaments_have_two_cover
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
