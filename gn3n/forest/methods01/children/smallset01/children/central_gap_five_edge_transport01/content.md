# A central-gap leaf pair has a fixed-anchor five-edge deletion transport package

## Statement


Let H be a minimum counterexample. Let k_1,k_2,k_3,k_4,a,b be six distinct vertices such that both
(k_1,k_2,a,k_3,k_4)
and
(k_1,k_2,b,k_3,k_4)
are tight Hamilton paths on their respective five-sets. Put
K={k_1,k_2,k_3,k_4}
and
U=K union {a,b}.

Then the four one-vertex deletions
U-a, U-b, U-k_1, U-k_4
are Hamiltonian.

Moreover the following five two-vertex deletions are Hamiltonian:
U-{a,k_1}, U-{a,k_4}, U-{b,k_1}, U-{b,k_4}, U-{k_1,k_4}.

Consequently either:

(1) U is Hamiltonian, in which case H-U is non-Hamiltonian with path-cover number two; or

(2) U is non-Hamiltonian. Writing L=H-U and D for the Hamiltonian-deletion set of U, one has
{a,b,k_1,k_4} subseteq D.
For every d in {a,b,k_1,k_4}, L+d is non-Hamiltonian with path-cover number two, and for each of the five pairs
{a,k_1}, {a,k_4}, {b,k_1}, {b,k_4}, {k_1,k_4},
the corresponding two-label state L+d+e is non-Hamiltonian with path-cover number two.

Thus the non-Hamiltonian central-gap six-set carries an explicit good-deletion graph containing K_{2,2} between {a,b} and {k_1,k_4}, together with the anchor edge k_1k_4.


## Body


The deletions U-a and U-b are Hamiltonian by hypothesis.

For U-k_1, boundary antisymmetry says exactly one of
(a,k_2,b), (b,k_2,a)
is tight. In the first case
(a,k_2,b,k_3,k_4)
is a tight Hamilton path, because its remaining consecutive triples are inherited from the displayed path through b. In the second case
(b,k_2,a,k_3,k_4)
is tight by the same argument using the displayed path through a. Hence U-k_1 is Hamiltonian.

Similarly exactly one of
(a,k_3,b), (b,k_3,a)
is tight. In the first case
(k_1,k_2,a,k_3,b)
is a tight Hamilton path on U-k_4; in the second case
(k_1,k_2,b,k_3,a)
is. Thus U-k_4 is Hamiltonian.

Four of the asserted two-deletions are immediate displayed four-paths:
U-{a,k_1} has path (k_2,b,k_3,k_4),
U-{a,k_4} has path (k_1,k_2,b,k_3),
U-{b,k_1} has path (k_2,a,k_3,k_4),
and U-{b,k_4} has path (k_1,k_2,a,k_3).

For U-{k_1,k_4}, again exactly one of
(a,k_2,b), (b,k_2,a)
is tight. Together with the inherited triples (k_2,b,k_3) or (k_2,a,k_3), this gives respectively the Hamilton four-path
(a,k_2,b,k_3)
or
(b,k_2,a,k_3).
Hence U-{k_1,k_4} is Hamiltonian.

Finally apply the certified common-four-core six-set transport theorem to the two Hamiltonian five-sets K union {a}=U-b and K union {b}=U-a. If U is Hamiltonian, its complement is non-Hamiltonian with path-cover number two. If U is non-Hamiltonian, every Hamiltonian deletion d of U yields L+d non-Hamiltonian with path-cover number two, and every Hamiltonian two-deletion U-{d,e} yields L+d+e non-Hamiltonian with path-cover number two. The explicit deletion calculations above therefore give all four one-label and all five two-label states claimed.
