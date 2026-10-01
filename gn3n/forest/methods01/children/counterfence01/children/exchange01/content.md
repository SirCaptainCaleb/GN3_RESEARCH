# Support-exchange radius-two obstruction

## Statement

Equitable one-vertex addition at old-support exchange distance at most two is exactly a finite Hamiltonian-set exchange axiom, and that axiom fails already in an edge-orderable boundary tournament of order twelve. The exhibited example has minimum exchange distance three.

## Body

# Distance-two equitable addition is a Hamiltonian-set exchange axiom

Let `H` be a boundary tournament, let `x` be a vertex, and let `A,B` be disjoint Hamiltonian vertex sets whose union is `V(H)-{x}`. Because arbitrary reordering inside a target support is allowed, the existence of a target two-cover depends only on whether the two target vertex sets are Hamiltonian.

The old-support exchange distance of a target partition is the minimum number of old vertices that change sides after optimally matching the two target parts to `A,B`; `x` is not counted.

The assertion that equitable vertex addition is always possible at exchange distance at most two is exactly the following finite family of Hamiltonian-set exchange alternatives.

## Odd step

Assume
`|A|=|B|=k`.
The target orders are `k+1` and `k`.

Up to interchanging `A` and `B`, every target support partition at exchange distance at most two is of exactly one of the following forms.

0. **Adjoin.**
   `A union {x}` and `B`.

1. **Replace-and-transfer.**
   For some `b in B`,
   `A union {b}`
   and
   `(B-{b}) union {x}`.

2. **One-for-one swap plus x.**
   For some `a in A`, `b in B`,
   `(A-{a}) union {b,x}`
   and
   `(B-{b}) union {a}`.

Hence distance-two equitable addition in the odd step is equivalent to saying that at least one of these displayed pairs consists of two Hamiltonian sets, allowing the symmetric alternatives with `A,B` interchanged.

### Proof

Match the larger target part `R` of size `k+1` to `A` and the smaller target part `S` of size `k` to `B`. Let

`alpha=|A intersect S|`,
`beta=|B intersect R|`.

If `x in R`, the size equation
`|R|=(k-alpha)+beta+1=k+1`
gives `alpha=beta`. Exchange distance at most two gives
`alpha+beta<=2`, hence either
`alpha=beta=0`, yielding form 0, or
`alpha=beta=1`, yielding form 2.

If `x in S`, then
`|R|=(k-alpha)+beta=k+1`,
so
`beta=alpha+1`.
Now `alpha+beta<=2` forces
`alpha=0,beta=1`, yielding form 1.
Interchanging the matching of the two old sides gives the symmetric versions. ∎

## Even step

Assume
`|A|=k+1`,
`|B|=k`.
The target orders are `k+1,k+1`.

Up to interchanging the two unlabeled target components, every target support partition at exchange distance at most two is of exactly one of the following forms.

0. **Adjoin to the short side.**
   `A`
   and
   `B union {x}`.

1. **Replace from the long side.**
   For some `a in A`,
   `(A-{a}) union {x}`
   and
   `B union {a}`.

2. **One-for-one swap with x on the short side.**
   For some `a in A`, `b in B`,
   `(A-{a}) union {b}`
   and
   `(B-{b}) union {a,x}`.

Hence the even distance-two induction is equivalent to the assertion that at least one displayed pair consists of two Hamiltonian sets.

### Proof

Match one target part `R` to the old long side `A`, and the other `S` to `B`. Put

`alpha=|A intersect S|`,
`beta=|B intersect R|`.

If `x in S`, then
`|R|=(k+1-alpha)+beta=k+1`,
so `alpha=beta`. Exchange distance at most two yields either
`alpha=beta=0`, form 0, or
`alpha=beta=1`, form 2.

If `x in R`, then
`|R|=(k+1-alpha)+beta+1=k+1`,
so
`alpha=beta+1`.
The bound `alpha+beta<=2` forces
`alpha=1,beta=0`, which is form 1. ∎

## Consequence

The two-support-exchange moonshot from `the radius-two exchange proposal` is therefore an exchange axiom for the family of Hamiltonian vertex sets of a boundary tournament. No inherited path order appears in its statement.

A proof of these odd and even Hamiltonian-set exchange alternatives for arbitrary `k` would prove equitable two-coverability by induction, hence the grand two-cover conjecture. ∎

---

# Edge-ordered obstruction at order twelve

# Edge-ordered counterexample — distance-two support exchange already fails in the acyclic comparison subclass

the same failure occurs in an **edge-ordered complete graph**, hence in a boundary tournament whose comparison digraph is acyclic.

Let the vertices be
`0,1,...,11`.
Put
`A={0,1,2,3,4,5}`,
`B={6,7,8,9,10}`,
and let the omitted vertex be
`x=11`.

Order the 66 ordinary edges of `K_12` as follows:

`2-11 < 4-8 < 0-1 < 6-7 < 3-5 < 5-6 < 7-10 < 2-4 < 8-11 < 3-10 < 3-6 < 4-11 < 6-10 < 0-8 < 2-7 < 9-11 < 6-11 < 2-9 < 0-9 < 1-2 < 5-8 < 0-3 < 4-7 < 7-8 < 3-8 < 5-9 < 1-4 < 7-9 < 2-3 < 1-6 < 5-10 < 2-8 < 1-10 < 3-4 < 0-10 < 5-7 < 1-9 < 10-11 < 3-9 < 5-11 < 0-5 < 0-11 < 3-7 < 1-3 < 6-9 < 2-6 < 1-8 < 2-5 < 6-8 < 2-10 < 0-7 < 4-9 < 8-9 < 9-10 < 3-11 < 0-2 < 4-6 < 4-5 < 7-11 < 1-7 < 4-10 < 1-11 < 1-5 < 0-4 < 0-6 < 8-10`.

Let `H` be the induced edge-orderable boundary tournament: a triple `(u,v,w)` is tight exactly when edge `uv` precedes edge `vw`.

## Starting deletion cover

The paths

`A=(0,1,2,3,4,5)`

and

`B=(6,7,8,9,10)`

are increasing. Their consecutive edge ranks are respectively

`2<19<28<33<57`

and

`3<23<52<53`.

Thus `H-x` has the displayed equitable `6|5` cover.

## Exhaustive distance-two failure

Enumerate every equitable support partition of `V(H)` into two six-sets.
There are

`(1/2) binom(12,6)=462`

unordered support partitions.

For each six-set, Hamiltonicity was checked exhaustively over all
`6!=720`
vertex orders using the displayed edge order.

Among the 462 equitable partitions, 310 have both sides Hamiltonian. However **none** has old-support exchange distance at most two from `A|B`.

Equivalently, checking the 37 support partitions classified by the preceding classification for exchange distance at most two gives zero successful partitions.

Hence this edge-orderable boundary tournament refutes universal distance-two support exchange.

## Minimum exchange distance is exactly three

There are 55 equitable Hamiltonian support partitions at exchange distance three, so the minimum distance is exactly three.

One explicit cover is

`(0,1,2,3,7,11) | (5,6,8,9,10,4)`.

The consecutive edge ranks are

`2<19<28<42<58`

and

`5<48<52<53<60`,

respectively, so both paths are increasing.

Relative to the old split `A|B`, after optimally matching the two new supports exactly three old vertices change sides.

Therefore the failure of distance-two support exchange at order twelve is **not** a phenomenon caused by directed cycles in the comparison digraph. It already occurs in the acyclic, edge-ordered subclass. Any scalable induction must either permit larger support exchange or use a different global invariant. ∎

# Structural cloning lemma


Suppose an edge-ordered complete graph on A union {z} has A Hamiltonian but every (A-a)+z non-Hamiltonian. Replace z by a disjoint set F. In the old total edge order replace each edge az by a consecutive block of edges ay, y in F, in any order. Insert all F-internal edges anywhere, respecting any prescribed total order on them. Then every induced A union {y} is an order-preserving copy of A union {z}. Consequently every (A-a)+y is non-Hamiltonian, simultaneously for all a in A and y in F.

## Proof
Restrict the expanded total order to A union {y}. Each block contributes exactly its single edge ay, at the old position of az, and every A-internal edge retains its relative position. Tight triples and Hamiltonicity on that induced set therefore agree under z -> y. This proves the claim. ∎

For equal sizes |A|=|F|=m, if F is also non-Hamiltonian, the initial partition A|F and every partition obtained by one cross-swap fail to be two Hamiltonian supports. If F-x is Hamiltonian, this gives an old m|(m-1) cover for which equitable addition at old-support exchange distance at most two fails: the classified options have either F or one replacement (A-a)+y as a component.

