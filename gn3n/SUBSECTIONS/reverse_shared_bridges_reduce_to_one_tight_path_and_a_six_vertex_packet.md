# Reverse shared bridges reduce to one tight path and a six-vertex packet

## Metadata

- ID: reverse_shared_bridges_reduce_to_one_tight_path_and_a_six_vertex_packet
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 79
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Retain the neighboring-cut setup and suppose the two bridge orientations are
(U,s,v,T) and (U,v,T,r).
Put R=(U,v,T) and S=A union {r,s}. Then R is a tight path, S has order six, and they partition the full span. There are also actual Hamilton orders on R+s and R+r:
L_s=(U,s,v,T), L_r=(U,v,T,r).

If either original bridge/deletion test succeeds, the span is already two-covered. Otherwise A+r and A+s are non-Hamiltonian, while S-w is Hamiltonian for every w in A, by four-of-six.

Assume further that the full span has no two-cover. Then:
(1) S is non-Hamiltonian, since S|R would otherwise cover it;
(2) R+w is non-Hamiltonian for every w in A, since (R+w)|(S-w) would otherwise cover it;
(3) R+r and R+s are Hamiltonian by the displayed orders;
(4) every vertex of A is noninsertable at every gap of the inherited order R, by (2).
Thus the two-tail residue has become one tight path with four globally forbidden single-vertex extensions and two explicitly permitted extensions. This is not just failure of endpoint bridges.

There is a sharper two-vertex absorption test. Define
G_r={w in A:H[V(R) union {r,w}] is Hamiltonian},
G_s={w in A:H[V(R) union {s,w}] is Hamiltonian}.
For w in G_r, a two-cover is obtained whenever (A-w)+s is Hamiltonian. For w in G_s, it is obtained whenever (A-w)+r is Hamiltonian.

Each of the two five-sets A+s and A+r is non-Hamiltonian, so each has at most one bad four-deletion. Consequently |G_r|>=2 or |G_s|>=2 suffices for a two-cover. The weaker combined condition |G_r union G_s|>=3 also suffices: at most two labels are exceptional across the two four-deletion tests, so a third label has a good complementary four-set in whichever absorption test it realizes.

If A itself is non-Hamiltonian, it is already the unique bad four-subset of both bad five-sets. Then every (A-w)+r and (A-w)+s, w in A, is Hamiltonian. In this case any nonempty G_r or G_s closes the span.

These tests may be witnessed by explicit insertions of w into the actual orders L_r or L_s; Hamiltonicity can also be supplied by an independent theorem. Successful insertion is a sufficient certificate, while failed insertion in one displayed order is not a proof of non-Hamiltonicity.

Therefore a persistent no-two-cover instance must have |G_r|,|G_s|<=1 and their union of order at most two. Every surviving label in G_r must be the unique bad deletion of A+s, and every label in G_s the unique bad deletion of A+r. If A is non-Hamiltonian both sets must be empty.

The conclusions use no minimal-counterexample induction or disturbance argument. They provide conditional absorption tests and exact residual restrictions, not a theorem forcing either absorption set to be nonempty. The inherited positive-depth repair and global carrier compatibility obligations are unchanged.

## Frontier

- Development version when composed: None
- Development version now: 1
