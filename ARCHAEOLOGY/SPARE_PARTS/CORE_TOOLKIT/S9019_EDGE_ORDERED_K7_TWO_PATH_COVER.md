# S9019 — Edge-Ordered Complete Graphs Through Order Ten Have Two Increasing Paths

## Theorem

Let `G` be a complete graph on `n<=10` vertices with a strict total order on its ordinary edges. Then `V(G)` can be partitioned into at most two vertex-disjoint increasing paths.

Equivalently,

`pc_inc(G) <= 2`

for every edge-ordered `K_n` with `n<=10`.

This strengthens the original order-seven statement of archived `R971`. The proof below is entirely human and uses no SAT, DPLL, MILP, exhaustive enumeration, or computer-assisted case check.

## Ingredient 1 — three of the five K4 deletions of an edge-ordered K5 are Hamiltonian

We first prove a small local density lemma.

### Lemma

Every edge-ordered `K5` has at most two non-Hamiltonian induced `K4`s. Equivalently, at least three of its five vertex-deleted `K4`s have an increasing Hamilton `P4`.

### Proof

By `S9020`, a non-Hamiltonian edge-ordered `K4` has its three opposite-edge perfect matchings in strict height blocks. Consequently, on such a `K4`, taking the opposite edge preserves every comparison between adjacent edges: if `e` and `f` are adjacent, then

`e < f  iff  e* < f*`,

where `e*` and `f*` are their respective opposite edges in that `K4`.

Suppose for contradiction that an edge-ordered `K5` on vertices

`{a,b,c,d,e}`

has three non-Hamiltonian `K4`s. Relabel so these are the cells obtained by deleting `a`, `b`, and `c`.

In the bad cell on `{b,c,d,e}`, the edges `bd,be` are adjacent and their opposite edges are `ce,cd`. Hence

`bd < be  iff  ce < cd`.

In the bad cell on `{a,c,d,e}`, the edges `ce,cd` are adjacent and their opposite edges are `ad,ae`. Hence

`ce < cd  iff  ad < ae`.

In the bad cell on `{a,b,d,e}`, the edges `ad,ae` are adjacent and their opposite edges are `be,bd`. Hence

`ad < ae  iff  be < bd`.

Combining the three equivalences gives

`bd < be  iff  be < bd`,

impossible in a strict total edge order. Thus at most two vertex-deleted `K4`s are non-Hamiltonian. ∎

### Density corollary

Let `h_4(r)` denote the number of four-vertex subsets of an edge-ordered `K_r` that support an increasing Hamilton `P4`. For every `r>=5`,

`h_4(r) >= (3/5) * C(r,4)`.

Indeed, count incidences `(X,Y)` with `X` a Hamilton four-set and `Y` a five-set containing `X`. Every five-set contains at least three Hamilton four-sets by the lemma, while every four-set lies in exactly `r-4` five-sets. Hence

`(r-4) h_4(r) >= 3 C(r,5) = (3/5)(r-4) C(r,4)`.

## Ingredient 2 — Hamilton-five density

By `S9029`, every six-set in a Strong Level-(1) boundary tournament has at least four Hamilton-five deletions. Edge-ordered complete graphs form a subclass, so in every edge-ordered `K_r`, `r>=6`, the number `h_5(r)` of Hamilton five-sets satisfies

`h_5(r) >= (2/3) C(r,5)`.

We now prove the finite two-cover theorem.

## Proof of the theorem

For `n<=5` the conclusion is immediate. If `n<=3`, one increasing path suffices. For `n=4`, split the vertices into two dimers. For `n=5`, any three vertices have an increasing Hamilton `P3`, and the remaining two vertices form a dimer.

### Orders 6, 7, and 8

Take any six vertices. By `S9029` some five of them support an increasing Hamilton `P5`.

- For `n=6`, the remaining vertex is a singleton.
- For `n=7`, the remaining two vertices form a dimer.
- For `n=8`, the remaining three vertices form an edge-ordered triangle, which always has an increasing Hamilton `P3`: its smallest and largest edges meet, and traversing them in increasing order gives the path.

Thus `pc_inc(G)<=2` for `n=6,7,8`.

### Order 9

There are

`C(9,5)=C(9,4)=126`

five-sets and four-sets.

By `S9029`,

`h_5(9) >= (2/3) * 126 = 84`.

By the four-set density corollary above,

`h_4(9) >= (3/5) * 126 = 75.6`,

so integrality gives

`h_4(9) >= 76`.

Complementation is a bijection between the 126 five-sets and the 126 four-sets. If no Hamilton five-set had a Hamilton four-set as its complement, then the complements of the `h_5(9)` Hamilton five-sets would be disjoint from the family of `h_4(9)` Hamilton four-sets. Therefore

`h_5(9)+h_4(9) <= 126`.

But

`84+76=160>126`,

a contradiction. Hence some five-set `A` and its four-vertex complement `B` are both Hamiltonian. Their Hamilton paths form a spanning `5+4` increasing two-cover.

### Order 10

There are

`C(10,5)=252`

five-sets, paired into exactly

`252/2=126`

unordered complementary pairs `{A,V-A}`.

Again `S9029` gives

`h_5(10) >= (2/3) * 252 = 168`.

If no complementary pair had both members Hamiltonian, each of the 126 complementary pairs could contribute at most one Hamilton five-set, giving `h_5(10)<=126`. This contradicts `h_5(10)>=168`.

Therefore some complementary five-sets are both Hamiltonian. Their two increasing Hamilton `P5`s form a spanning `5+5` two-cover.

This completes the proof for every `n<=10`. ∎

## Why the old K7 computation was hiding the structure

The original `S9019`/`R971` proof encoded the order-seven case as a finite SAT/MILP infeasibility problem. Once the human Hamilton-five density theorem `S9029` is available, the order-seven case is immediate: one Hamilton `P5` leaves only a dimer.

More importantly, the same density mechanism automatically gives orders eight and ten, while the small opposite-matching lemma above supplies exactly the additional Hamilton-four density needed at order nine. Thus the natural finite theorem is not a special `K7` certificate but the complete range `n<=10`.

## Scope and what happens beyond ten

This argument does **not** prove the general edge-ordered two-cover conjecture `R888`.

The cutoff at ten is structural for this proof. Orders nine and ten work because complementation pairs the locally controlled Hamilton support sizes:

- `9 = 5+4`, where we have densities for Hamilton `P5` and Hamilton `P4`;
- `10 = 5+5`, where the Hamilton-five density alone exceeds one half.

At order eleven the complementary split becomes `5+6`. The present machinery gives strong Hamilton-five density but no corresponding density theorem forcing Hamilton `P6`s on six-sets. Indeed edge-ordered `K6`s need not themselves be Hamiltonian, so there is no automatic complement argument analogous to orders nine and ten.

Thus the proof genuinely generalizes the former `K7` base through `K10`, but it does not presently cross to `K11`.

## Provenance

The historical order-seven computational theorem is archived as `R971`. The human proof above is a later synthesis using the human `S9020` non-Hamiltonian `K4` matching-height classification and the human `S9029` Hamilton-five density hierarchy. The three-bad-`K4` opposite-edge contradiction and the resulting `3/5` Hamilton-four density are recorded here explicitly.