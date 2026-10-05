# Every ten-vertex boundary tournament has a two-cover

**Summary:** Every boundary tournament on ten vertices can be partitioned into two Hamiltonian five-vertex supports.

## Statement

Let H be a boundary tournament on exactly ten vertices. Then pc(H)<=2. In fact, H has two complementary Hamiltonian five-subsets.

## Body

By [[smallset01]], every six-vertex set contains at least four Hamiltonian five-subsets. Let G be the number of Hamiltonian five-subsets of V(H). Count incidences (F,S) with |F|=5, |S|=6, F subset S, and H[F] Hamiltonian. Each of the C(10,6)=210 six-sets contributes at least four incidences, while each Hamiltonian five-set is contained in exactly five six-sets. Hence 5G>=4*C(10,6)=840, so G>=168. The 252 five-subsets of a ten-set split into 126 complementary pairs {F,V-F}. If no complementary pair were both Hamiltonian, at most one member of each pair would be counted, giving G<=126, contradiction. Therefore some complementary five-sets are both Hamiltonian. Choosing Hamilton paths on them gives a spanning two-cover.

## Metadata

- ID: ten_vertex_boundary_tournaments_have_two_cover
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: passed
- Refutation: unrefuted
- Toolkit status: Limbo
