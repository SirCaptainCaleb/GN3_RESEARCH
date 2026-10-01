# Universal six-set Hamiltonicity alone forces deletion sides of order at least six

## Statement

Let H be a minimum counterexample in which every six-vertex induced subtournament is Hamiltonian. Then every component of every exact one-vertex deletion two-cover has order at least six.

## Body

Let H-x=P|Q be any exact deletion two-cover, and suppose |P|<=|Q|. Every deletion-cover component has order at least three.

If |P|=5, then V(P) union {x} is a six-set and is Hamiltonian by hypothesis. A Hamilton path on this six-set together with Q gives a spanning two-cover of H, contradiction.

If |P|=4, let q_0 be an endpoint of the displayed path Q. The six-set
S=V(P) union {x,q_0}
is Hamiltonian. Since |Q|>=3, deleting q_0 from the displayed endpoint leaves a nonempty tight path Q-q_0. A Hamilton path on S together with Q-q_0 spans H with two paths, contradiction.

If |P|=3, let q_0,q_1 be the first two vertices of the displayed path Q=(q_0,q_1,...). The six-set
S=V(P) union {x,q_0,q_1}
is Hamiltonian. Since |Q|>=3, the remaining suffix Q-(q_0,q_1) is a nonempty tight path. Again S together with that suffix gives a spanning two-cover of H.

Thus |P| cannot be three, four, or five. Hence |P|>=6. As the chosen deletion cover was arbitrary, every deletion-cover component has order at least six.
