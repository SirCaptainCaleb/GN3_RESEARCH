# The paired opposite-end four-window fork collapses to an endpoint-aligned four- or five-window

## Statement

Let H be a minimum counterexample of order at least fifteen, let W be a Hamiltonian four-set, and suppose the paired opposite-end fork of 1000764 occurs. Thus there are a three-set D, d in D, one displayed endpoint e of one component of H-W, and the two displayed endpoints f,g of the other component such that
W_f=(D-{d}) union {e,f} and W_g=(D-{d}) union {e,g}
are Hamiltonian four-sets with non-Hamiltonian path-cover-two complements.

Then at least one of the following holds:
(1) there is a Hamiltonian four-set Z containing all three displayed endpoints e,f,g, and H-Z is non-Hamiltonian with path-cover number two;
(2) the five-set S=(D-{d}) union {e,f,g} is Hamiltonian, H-S is non-Hamiltonian with path-cover number two, and S has a Hamilton path whose two displayed endpoints both belong to {e,f,g}.

Consequently the paired-fork alternative of 1000764 is not an unpositioned migration residue: it always produces a proper Hamiltonian support of order four or five whose Hamiltonian structure is explicitly aligned with the three relevant complement endpoints.

## Body

Put A=D-{d} and C=A union {e}, so |C|=3, W_f=C union {f}, and W_g=C union {g}. Apply 1000557 to the adjacent Hamiltonian four-windows W_f and W_g.

If S=C union {f,g} is non-Hamiltonian, 1000557 gives at least two distinct c in C such that S-{c} is a Hamiltonian four-set with non-Hamiltonian path-cover-two complement. At most one of those deletions can be c=e. Hence for some c in A, Z=S-{c} is Hamiltonian and contains e,f,g. This is (1).

Now suppose S is Hamiltonian. Minimum-counterexample calculus gives H-S non-Hamiltonian with path-cover number two. If S-{a} is Hamiltonian for either a in A, then S-{a} contains e,f,g and again gives (1). Otherwise both A-vertex deletions are non-Hamiltonian.

Choose any Hamilton path R on S. Deleting either displayed endpoint of R leaves an inherited Hamilton path on the corresponding four-subset. Therefore neither endpoint of R can lie in A, because both A-deletions are non-Hamiltonian. The two endpoints of R must consequently lie in the three-set {e,f,g}. This is (2).

In the application from 1000764, e is a displayed endpoint of one complementary path and f,g are the two displayed endpoints of the other, so the conclusion is genuinely endpoint-positioned.
