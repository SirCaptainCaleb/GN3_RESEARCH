# A Hamiltonian five-side admits prescribed-pair two-for-two support switches

**Summary:** Let H be a minimum counterexample, let X be a proper Hamiltonian five-vertex set, and suppose H-X is non-Hamiltonian with path-cover number two. Fix any x in X and any two distinct vertices p,q outside X. Then for at least two distinct vertices d in X-{x}, the five-set U_d=(X-{x,d}) union {p,q} is Hamiltonian. For every such d, H-U_d is non-Hamiltonian with path-cover number two. Consequently, if H-X=P|Q is any displayed two-cover, one may prescribe one vertex p of P and one vertex q of Q and move both simultaneously into a new Hamiltonian five-side while forcing any prescribed x in X out of the five-side.

## Statement

Let H be a minimum counterexample, let X be a proper Hamiltonian five-vertex set, and suppose H-X is non-Hamiltonian with path-cover number two. Fix any x in X and any two distinct vertices p,q outside X. Then for at least two distinct vertices d in X-{x}, the five-set U_d=(X-{x,d}) union {p,q} is Hamiltonian. For every such d, H-U_d is non-Hamiltonian with path-cover number two. Consequently, if H-X=P|Q is any displayed two-cover, one may prescribe one vertex p of P and one vertex q of Q and move both simultaneously into a new Hamiltonian five-side while forcing any prescribed x in X out of the five-side.

## Body

Put A=X-{x}, so |A|=4, and put S={p,q}. The sets A and S are disjoint. Apply twofourhamdeletions01 to S and A. It gives at least two vertices d in A such that S union (A-{d})=(X-{x,d}) union {p,q} is Hamiltonian. Call this support U_d. Since X is proper and H is a minimum counterexample, |V(H)|>10; in particular each five-set U_d is proper. Minimum-counterexample calculus gives pc(H-U_d)<=2. If H-U_d were Hamiltonian, then a Hamilton path on U_d together with one on H-U_d would form a spanning two-cover of H, impossible. Hence H-U_d is non-Hamiltonian with path-cover number exactly two. The final sentence is the specialization when p and q are chosen from the two displayed components of H-X.

## Metadata

- ID: five_side_prescribed_pair_switch01
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Toolkit status: Limbo
