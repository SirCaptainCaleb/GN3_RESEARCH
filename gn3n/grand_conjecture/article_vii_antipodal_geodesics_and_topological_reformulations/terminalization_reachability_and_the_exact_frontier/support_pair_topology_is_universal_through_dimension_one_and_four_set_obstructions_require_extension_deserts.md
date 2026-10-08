# Support-pair topology is universal through dimension one, and four-set obstructions require extension deserts

## Composition

(none yet)

## Development

## Universal low-rank structure in the Hamiltonian support-pair complex

Let P(H) be the ordered poset of disjoint Hamiltonian support pairs (A,B) with |A|,|B|>=2, ordered componentwise by inclusion, and let K(H)=Delta P(H) with free involution T(A,B)=(B,A).

### 1. The first Smith equation is automatic
Assume |V(H)|>=5. Every two-set and every three-set in a boundary tournament is Hamiltonian. Hence every vertex of K(H) is connected to its transpose.

Indeed, given (A,B), choose two-subsets A0 subset A, B0 subset B. Comparable inclusions connect (A,B) to (A0,B0). It therefore suffices to connect an ordered pair of disjoint two-sets to its transpose.

Write A0={a,b}, B0={c,d}, and choose a spare vertex e outside A0 union B0. Replacing one label at a time while preserving disjointness gives the sequence
(A0,B0) -> ({e,b},B0) -> ({e,b},{a,d}) -> ({e,c},{a,d}) -> ({e,c},A0) -> (B0,A0).
Each replacement is realized by a two-edge path in the order complex through the corresponding three-set union, which is Hamiltonian.

Thus every vertex is path-connected to its transpose. Over F_2, choosing any vertex c0 and any such path chain c1 gives
partial c1=(1+T)c0, aug(c0)=1.
So the first Smith equation uses no nontrivial Hamiltonicity at all. Any support-pair proof must obtain its real content in dimension at least two.

### 2. A non-Hamiltonian four-set obstructs only when it has no usable Hamiltonian extender
Fix disjoint supports A,B with |A|=2, |B|=4, and suppose H[B] is non-Hamiltonian. The proper Hamiltonian subsets of B of orders two and three form the familiar one-dimensional boundary cycle in the carrier with first side fixed to A; this is the support-contained obstruction recorded in [[a_non_hamiltonian_four_set_obstructs_support_contained_gale_carriers]].

However, let z lie outside A union B. If H[B union {z}] is Hamiltonian, then the single support-pair vertex (A,B union {z}) is comparable above every boundary vertex (A,D) with D a proper subset of B of order two or three. Hence it cones the entire four-set boundary cycle. The local one-cycle is therefore null-homologous and continuously fillable in K(H).

Consequently a genuine four-set obstruction to the support-pair Smith extension requires the much stronger condition that H[B union {z}] is non-Hamiltonian for every usable z outside A union B.

### Strategic consequence
The support-pair formulation is structurally empty through the first Smith equation. Its first tournament-specific local obstruction occurs where four-vertex Hamiltonicity enters, and even that obstruction disappears under one Hamiltonian five-extension. Therefore the relevant question is not whether non-Hamiltonian four-sets occur, but whether Article VII's four-/five-/six-set extension theorems prevent this all-bad-extension configuration in the kappa_2=2 layer.
