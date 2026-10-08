# Type I labels are impossible, so the Johnson block is spanning

## Composition

(none yet)

## Development

## Type I exterior labels are impossible; the saturated Johnson block is spanning

Retain a minimum-degree saturated Johnson block U of degree d from [[minimum_degree_full_stars_form_saturated_johnson_blocks]].

Suppose, for contradiction, that W=V(H)-U is nonempty. Every y in W has Type I polarity relative to every full-star d-set F subset U.

Choose y in W and any (d-1)-subset R of U. By the Johnson-block theorem,
K=R union {y}
is Hamiltonian.

For each u in U-R, put
F=R union {u}.
Then F is a degree-d full-star source. Since y has Type I polarity relative to F, the vertex F+y is a source and all coordinates of F are active. In particular the edge removing u is selected:
F+y -> R+y=K.

As u ranges over U-R, these are distinct incoming selected edges at K. Hence K is a sink of indegree at least
|U|-|R|=|U|-d+1.

The cubical core is antipodally invariant, and antipodality exchanges sinks with sources while preserving degree. Therefore a source of positive outdegree at least |U|-d+1 exists. Since d is the minimum positive source outdegree,
d <= |U|-d+1,
so
|U| >= 2d-1.

On the other hand U is a proper induced subtournament of the minimum-order counterexample H because W is nonempty. Hence H[U] has a spanning two-cover.

No Hamiltonian subset of U can have order at least d: a Hamilton path on such a set would contain a contiguous d-vertex Hamiltonian subpath, contradicting that every d-subset of U is non-Hamiltonian.

Therefore each component of every two-cover of H[U] has order at most d-1. Consequently
|U| <= 2d-2.

This contradicts |U|>=2d-1.

Hence
U=V(H).

Combining with [[all_exchangeable_johnson_blocks_force_the_exact_odd_universal_state]], every nonempty surviving cubical core in a minimum counterexample forces
n=2d-1,
with every (d-1)-subset Hamiltonian and every d-subset non-Hamiltonian.

Thus all Type I/exterior-label branches are eliminated scale-independently. The sole remaining cubical-core residue is the spanning odd universal balanced state.
