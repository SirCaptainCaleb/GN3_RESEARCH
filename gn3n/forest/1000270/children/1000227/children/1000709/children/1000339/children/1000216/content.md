# Four synchronized omission labels force order disagreement or Hamiltonian six-windows at both ends

## Statement

Let H be a minimum counterexample and H-x=P|Q an exact deletion two-cover with 3<=|P|<=5. Put C=V(P) union {x}, let G be the good-deletion set from 6f72075b0b54, and choose four distinct labels D subseteq G. Write Q=(q_0,...,q_s), s>=2. Define
S_L=D union {q_0,q_2},
S_R=D union {q_{s-2},q_s}.
For each Z in {S_L,S_R}, either H[Z] is non-Hamiltonian and Hamiltonian deletion paths of Z exhibit explicit relative-order disagreement, or H[Z] is Hamiltonian and H-Z is non-Hamiltonian with path-cover number exactly two. Thus each end of Q supplies either a six-vertex order-disagreement kernel or a Hamiltonian six-window with pc-two complement.

## Body

By 6f72075b0b54, for every three distinct labels a,b,c in G the five-set {q_0,q_2,a,b,c} is Hamiltonian, and similarly {q_{s-2},q_s,a,b,c} is Hamiltonian.

Fix Z=S_L. For every d in D, the five-set
Z-{d}=(D-{d}) union {q_0,q_2}
is Hamiltonian, because D-{d} consists of three distinct good labels. Hence Z has at least four Hamiltonian one-vertex deletions.

If H[Z] is non-Hamiltonian, apply the certified theorem astra004fourgooddisagree to arbitrary Hamilton paths on four of these deletions. It forces relative-order disagreement between two such paths, giving the first conclusion.

If H[Z] is Hamiltonian, then Z is a proper vertex set of H. The complement H-Z is a proper induced subtournament, so minimum-counterexample calculus gives path-cover number at most two. It cannot be Hamiltonian, because a Hamilton path on Z together with a Hamilton path on H-Z would be a spanning two-cover of H. Therefore pc(H-Z)=2 and H-Z is non-Hamiltonian.

The proof for S_R is identical using the right-end five-set fan in 6f72075b0b54. No compatibility choice or orientation symmetry is used.
