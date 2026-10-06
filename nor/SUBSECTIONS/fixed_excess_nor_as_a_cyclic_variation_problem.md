# Fixed-excess NOR as a cyclic variation problem

## Metadata

- ID: fixed_excess_nor_as_a_cyclic_variation_problem
- Parent Section: higher_memory_norine_geodesics
- Position: 11
- Row version: 2
- Development version: 2
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development


## Fixed-excess cyclic formulation

Write (n=r+r), so a permutation has (r+1) sliding (r)-windows.

Fix a cyclic ordering
[
C=(v_1,ldots,v_n)
]
of the ground set, with indices modulo (n), and define its cyclic status word
[
c_i=h(v_i,v_{i+1},ldots,v_{i+r-1}),
qquad iin mathbb Z/nmathbb Z.
]

Cutting the cyclic order immediately before (v_i) gives the linear permutation
[
(v_i,v_{i+1},ldots,v_{i+n-1}).
]
Its ordinary NOR word consists exactly of
[
c_i,c_{i+1},ldots,c_{i+r},
]
because there are (r+1=n-r+1) nonwrapping (r)-windows.

Hence (N_k) for the pair ((n,r)) is equivalent to finding a cyclic coordinate order whose cyclic status word has some consecutive block of length (r+1) with at most one change.

Define the cyclic change word
[
d_i=c_ioplus c_{i+1}.
]
A counterexample would therefore have the property that, for every cyclic coordinate order and every index (i),
[
d_i+d_{i+1}+cdots+d_{i+r-1}ge 2.
]

Summing these (n) inequalities around one fixed cyclic order gives
[
rsum_{i=1}^n d_ige 2n.
]
Thus every cyclic coordinate order in a counterexample must have cyclic variation
[
q(C):=sum_i d_ige leftlceil rac{2n}{r}ightceil.
]
Since a cyclic binary word has an even number of changes, (q(C)) is even. Consequently any cyclic order satisfying
[
q(C)<rac{2n}{r}
]
immediately certifies the NOR conclusion.

### First consequences

- For (r=2), failure forces every pair of consecutive transition bits to have weight two, hence (d_i=1) for all (i). This is the cyclic form of the odd-overlap-cycle proof of the (n=r+2) theorem.
- For (r=3), failure forces every three consecutive transition bits to contain at least two ones. Equivalently, zero-transition edges are cyclically separated by at least two change edges. In addition (q(C)) is even. This gives a sharply constrained extremal pattern for the first unresolved excess.
- More generally, fixed-excess NOR can be attacked by minimizing cyclic variation over coordinate cycles rather than directly optimizing all linear permutations.

### Audit

The equivalence uses only the fact that every cut of a cyclic coordinate order is a permutation and that its nonwrapping (r)-windows are the indicated (r+1) consecutive cyclic windows. No reversal assumption is needed for the reformulation or the averaging inequality; reversal antisymmetry enters only when trying to prove that some cyclic order must have low variation.


## Frontier

- Development version when composed: None
- Development version now: 2
