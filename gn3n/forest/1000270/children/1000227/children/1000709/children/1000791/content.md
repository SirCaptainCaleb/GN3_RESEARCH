# Double-frozen enlarged supports are locally consistent at order thirteen

## Statement

There exists a 13-vertex boundary tournament H with a vertex x and disjoint Hamiltonian six-vertex paths P,Q covering H-x such that P union {x} and Q union {x} are both non-Hamiltonian and, in each enlarged seven-set, deleting x is the unique Hamiltonian six-vertex deletion. Thus simultaneous intrinsic freezing of both enlarged supports is consistent with the boundary-tournament axioms, although H-x itself may be Hamiltonian.

## Body

# Double-frozen enlarged supports are locally consistent at order thirteen

There exists a boundary tournament H on thirteen vertices with a vertex x and disjoint six-vertex sets P,Q such that:

- H[P] and H[Q] are Hamiltonian;
- H[P union {x}] and H[Q union {x}] are non-Hamiltonian;
- for every p in P, H[(P-{p}) union {x}] is non-Hamiltonian;
- for every q in Q, H[(Q-{q}) union {x}] is non-Hamiltonian.

Equivalently, in each of the enlarged seven-sets P union {x} and Q union {x}, the vertex x is the unique deletion whose remaining six-set is Hamiltonian. In particular P|Q is a 6|6 two-path cover of H-x. The construction does not assert that this cover is exact; omission-label exchange is nevertheless intrinsically frozen on both enlarged supports.

Proof.

The reusable counterexample module contains a seven-vertex boundary tournament J on A union {z}, where |A|=6, with the following properties:

- J[A] is Hamiltonian;
- J[A union {z}] is non-Hamiltonian and has maximum tight-path order six;
- for every a in A, J[(A-{a}) union {z}] is non-Hamiltonian.

Thus z is the unique Hamiltonian deletion of the seven-set A union {z}.

Take two disjoint copies of this witness, on P union {x_P} and Q union {x_Q}, and identify x_P and x_Q to a single vertex x. The two prescribed boundary-tournament structures are compatible: their vertex sets intersect only in x, so no reversal pair on three distinct vertices is prescribed by both copies.

Retain all tight-triple choices inside P union {x} and Q union {x}. For every remaining reversal pair, whose vertices meet both P and Q, choose either orientation arbitrarily. This completes the prescriptions to a boundary tournament H on P union Q union {x}.

The induced subtournaments on P union {x} and Q union {x} are unchanged copies of J. Therefore P and Q are Hamiltonian, each enlarged seven-set is non-Hamiltonian, and x is the unique Hamiltonian deletion on each side. Hence P|Q is a 6|6 two-path cover of H-x with both enlarged supports frozen. The mixed orientations may make H-x Hamiltonian, so no exactness claim is made.

This construction does not assert pc(H)>2; indeed it is only a local-consistency fence. Its consequence for the one-defect route is precise: the small-side threshold six from the synchronized-omission lemma is sharp even simultaneously on both sides. Therefore a universal no-trapping proof cannot rely on showing that one of the two enlarged supports always has an alternative Hamiltonian deletion. It must use triples mixing P and Q, or some other consequence of being a genuine counterexample.
