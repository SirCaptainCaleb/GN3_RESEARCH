# Above order seventeen two central-gap leaves already descend or disagree

## Statement

Let H be a minimum counterexample of order n>=18. Let k_1,k_2,k_3,k_4,a,b be six distinct vertices such that both
(k_1,k_2,a,k_3,k_4)
and
(k_1,k_2,b,k_3,k_4)
are tight Hamilton paths. Put
U={k_1,k_2,k_3,k_4,a,b}.

Then H contains either:

(1) explicit relative-order disagreement between Hamilton paths on overlapping induced supports; or

(2) a spanning three-cover lying in a pairwise-repartition component with strictly smaller quadratic potential.

Thus, above order seventeen, a repeated central-gap insertion on one ordered four-core is already a standard no-trapping disturbance.

## Body

The deletions U-a and U-b are Hamiltonian by the two displayed five-paths.

For U-k_1, boundary antisymmetry says exactly one of
(a,k_2,b), (b,k_2,a)
is tight. In the first case
(a,k_2,b,k_3,k_4)
is a Hamilton path, and in the second case
(b,k_2,a,k_3,k_4)
is. Hence U-k_1 is Hamiltonian.

Likewise exactly one of
(a,k_3,b), (b,k_3,a)
is tight. In the first case
(k_1,k_2,a,k_3,b)
is a Hamilton path on U-k_4, and in the second case
(k_1,k_2,b,k_3,a)
is. Hence U-k_4 is Hamiltonian.

Therefore U has at least four Hamiltonian one-vertex deletions. Apply the certified four-good-six interface.

If U is non-Hamiltonian, that theorem directly yields explicit relative-order disagreement between Hamilton paths on two distinct five-vertex deletions of U.

If U is Hamiltonian, the same interface gives that H-U is non-Hamiltonian with path-cover number two. Since n>=18, the certified Hamiltonian-six large-escape theorem applies to U and gives either explicit order disagreement or a spanning three-cover in a pairwise-repartition component with strictly smaller quadratic potential.

These cases exhaust the possibilities.
