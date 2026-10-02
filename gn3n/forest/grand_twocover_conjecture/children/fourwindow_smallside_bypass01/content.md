# An anchored four-window yields descent, a Hamiltonian five/six-side, or order at most fourteen

## Statement

Let H be a minimum counterexample, let W be a Hamiltonian four-vertex set, and let H-W=P|Q be a two-cover. Then at least one of the following holds: (1) the spanning three-cover W|P|Q admits a strict quadratic-potential decrease by an endpoint transfer; (2) H contains a proper Hamiltonian induced set S of order five or six such that H-S is non-Hamiltonian with path-cover number two; (3) |V(H)|<=14.

## Body

Apply independent_reconstruction. Its strict-descent alternative is (1), and its small-order alternative is (3).

It remains to consume the bounded six-window alternative. Let U be the six-set supplied there. If H[U] is Hamiltonian, then U is proper whenever |V(H)|>=15. If H-U were Hamiltonian, Hamilton paths on U and H-U would form a spanning two-cover of H, impossible. By minimum-counterexample calculus, H-U therefore has path-cover number two. Taking S=U gives (2).

If H[U] is non-Hamiltonian, the same certified six-window theorem supplies Hamiltonian one-vertex deletions of U (indeed at least four such deletions arise in its proof). Choose one such label u and put S=U-{u}. Then S is a Hamiltonian five-set. Again S is proper, H-S cannot be Hamiltonian because that would two-cover H, and minimum-counterexample calculus gives path-cover number two for H-S. Thus (2) holds.

Hence the order-disagreement subcase of the bounded six-window is not needed as a terminal output: the same local six-window already contains a Hamiltonian five-set with path-cover-two complement.