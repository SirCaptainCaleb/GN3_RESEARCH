# Order-eleven stress test for transport

## Statement

A hypothetical order-eleven minimum counterexample has exact 5|5 deletion covers and balanced type 5|3|3. Its equitable omission graph has minimum degree at least six; each omission state contains two support-compatible deletion cliques of size at least four; and compatible triangles are cyclic. In the additional ordinary-extremal branch with no tight six-path (equivalently extremal type 5|5|1), every 5|5 state exposes an internal non-clean Hamiltonian deletion, hence crossing or order disagreement.

## Body

# Order-eleven stress test

Assume, only for this testbed, that an order-eleven minimum counterexample H exists. The order-ten exact-5|5 theorem in the extremal Hamiltonicity module implies that every deletion H-x has an exact 5|5 cover. Fix x and write one such cover as H-x=P|Q.

## Compatible triangles are cyclic

Take three exact 5|5 deletion covers that are pairwise compatible. The common-gap theorem gives two common support classes on the eight common vertices and inserts the three deleted labels into one class at a common gap. Since each deletion cover has component sizes 5|5, the exceptional common class has order three before the two surviving labels are inserted.

If the deleted-label precedence tournament were transitive, the two-deep-gap theorem in the common-gap geometry module would require at least two common vertices on each side of the gap, forcing that class to have order at least four. Contradiction. Hence every such compatible triangle has cyclic precedence.

## Clean replacements are nonconsecutive

For P=(p_0,...,p_4), call p_i clean when H-p_i has the same-slot replacement cover
(p_0,...,p_{i-1},x,p_{i+1},...,p_4)|Q.

Two consecutive clean positions would, together with P|Q, form a compatible deletion triangle whose precedence is transitive (p_i -> x -> p_{i+1}), contradicting the preceding paragraph. Thus clean positions are independent in the five-position path, so there are at most three; if there are three they are exactly {p_0,p_2,p_4}.

The six-set V(P) union {x} is non-Hamiltonian, while deleting x leaves the Hamiltonian path P. By the four-of-six theorem, at least three deletions by vertices p_i are Hamiltonian. Therefore either one of those Hamiltonian deletions is non-clean, hence exposes the crossing/order-disagreement machinery, or the only good deletions are the rigid alternating set {p_0,p_2,p_4} and all three are clean. The same holds for Q.

This testbed is useful for falsifying proposed transport mechanisms. It is not evidence that order eleven is the global bottleneck.


# Further order-eleven structural consequences

Let `H` be a minimum-order counterexample on eleven vertices.

By `the exact order-ten 5|5 theorem in the extremal Hamiltonicity module` (equivalently `the exact order-ten 5|5 theorem in the extremal Hamiltonicity module`), for every vertex `v` the deletion
`H-v`
has an exact Hamiltonian `5|5` cover
`U|V`.

## Theorem

For every vertex `v`, each such deletion cover yields two spanning three-path covers of `H` of component orders
`5,3,3`
via the balanced-cover construction `the balanced-three-cover theorem in the maximin module`.

Consequently, among all spanning three-path covers of `H` whose components all have order at least three, the lexicographically maximal decreasing component-order triple is exactly
`(5,3,3)`.

This conclusion requires no codimension-four hypothesis.

## Proof

Fix `v` and an exact Hamiltonian `5|5` cover
`U|V`
of `H-v`.

Both components have order five. Apply `the balanced-three-cover theorem in the maximin module` to either component, say
`U=(u_0,u_1,u_2,u_3,u_4)`.
Since `H` has no spanning two-cover, the endpoint barriers give the tight triples
`(u_1,u_0,v)`
and
`(v,u_4,u_3)`.

Hence
`(u_1,u_0,v) | (u_2,u_3,u_4) | V`
and
`(u_0,u_1,u_2) | (v,u_4,u_3) | V`
are spanning three-path covers.
Their component orders are
`3,3,5`.

Thus a balanced spanning three-cover of type `(5,3,3)` exists for every omitted vertex.

Now any spanning three-cover all of whose components have order at least three has three positive integers summing to eleven. In decreasing order the only possibilities with first coordinate at most five are
`(5,3,3)`
and
`(4,4,3)`.
If a balanced cover had first coordinate at least six, it would have remaining sum at most five, so one of the remaining components would have order at most two, contrary to balance.

Therefore the lexicographically maximal balanced triple is exactly
`(5,3,3)`. ∎

## order-eleven consequence

The balanced side of the order-eleven collision is universal: any hypothetical order-eleven minimum counterexample, whether or not it has already been placed in codimension-four form, has balanced extremal type `5|3|3` and in fact receives such a cover from every vertex deletion.

# Omission graph has minimum degree six

Let `H` be a minimum-order counterexample of order eleven.

By `the exact order-ten 5|5 theorem in the extremal Hamiltonicity module`, every vertex deletion has an exact equitable `5|5` cover.

Fix one such state

`H-x=P|Q`

with

`|P|=|Q|=5`

and both supports Hamiltonian.

Then there are at least three distinct vertices `p in V(P)` such that

`(V(P)-{p}) union {x}`

is Hamiltonian, and at least three distinct vertices `q in V(Q)` such that

`(V(Q)-{q}) union {x}`

is Hamiltonian.

Consequently the spanning `5|5|1` state

`P|Q|(x)`

has at least six distinct reversible one-vertex omission swaps.

## Proof

The six-set

`V(P) union {x}`

is non-Hamiltonian: if it were Hamiltonian, a Hamilton path on that six-set together with the Hamilton path `Q` would give a spanning two-cover of `H`, contradiction.

Apply the four-of-six theorem `the small-set structure module` to this six-set.

At least four of its six five-vertex deletions are Hamiltonian. Deleting `x` leaves the already Hamiltonian set `V(P)`. Therefore at least three further deletions, by distinct vertices

`p in V(P)`,

leave Hamiltonian sets

`P_p=(V(P)-{p}) union {x}`.

For every such `p`,

`P_p | Q`

is an exact Hamiltonian `5|5` cover of `H-p`. Thus

`P|Q|(x) -> P_p|Q|(p)`

is an equitable omission swap.

The identical argument applied to the non-Hamiltonian six-set

`V(Q) union {x}`

gives at least three distinct vertices `q in V(Q)` with

`Q_q=(V(Q)-{q}) union {x}`

Hamiltonian, hence states

`P|Q_q|(q)`.

Since `P` and `Q` are disjoint, the three `P`-side and three `Q`-side omitted labels are distinct. Hence the original state has at least six distinct neighboring omission states.

Finally every such move is reversible. For example, from

`P_p|Q|(p)`

the six-set

`V(P_p) union {p}=V(P) union {x}`

has the Hamiltonian deletion obtained by deleting `x`, namely the original set `V(P)`. Thus the reverse swap restores

`P|Q|(x)`.

The same holds on the `Q` side. ∎

## State-graph formulation

Define the **equitable omission graph** of `H`:

- a vertex is a spanning `5|5|1` state, with the two five-supports Hamiltonian;
- two states are adjacent when one is obtained from the other by exchanging the singleton with one vertex of exactly one five-support, leaving the opposite support fixed.

Then every vertex of this graph has degree at least six.

By `the exact order-ten 5|5 theorem in the extremal Hamiltonicity module`, every label `x in V(H)` occurs as the singleton of at least one graph vertex.

Thus an order-eleven counterexample would require a globally nontrivial high-degree reversible reconfiguration graph covering all eleven singleton labels, while no graph state permits absorption of its singleton into either five-side as a Hamiltonian six-set. This is the balanced order-eleven state space. ∎

# Two support-compatible deletion cliques

Let `H` be a minimum-order counterexample on eleven vertices, and let
`H-x=P|Q`
be any exact Hamiltonian `5|5` cover.

Put
`R_P=V(P) union {x}`
and
`R_Q=V(Q) union {x}`.
Both induced six-sets are non-Hamiltonian: if, for example, `R_P` were Hamiltonian, a Hamilton path on `R_P` together with `Q` would two-cover `H`.

For a six-set `R`, write
`G(R)={d in R : H[R-{d}] is Hamiltonian}`.

## Theorem

Each of
`G(R_P)`
and
`G(R_Q)`
has order at least four.

For every `d in G(R_P)`, choose an arbitrary Hamilton path `P_d` on `R_P-{d}` and put
`F_d=P_d | Q`.
Then:

1. `F_d` is an exact two-path cover of `H-d`;
2. the family `{F_d : d in G(R_P)}` is pairwise compatible on **component membership**;
3. all support incompatibility disappears: every pair of covers has the same two support classes on its common intersection, namely
   `R_P-{d,e}` and `V(Q)`;
4. consequently every remaining disagreement inside this family is purely an **order** disagreement inside the critical six-set `R_P`.

The symmetric statement holds for `R_Q`, with the fixed untouched support `P`.

Thus every equitable `5|5|1` state in an order-eleven minimum counterexample contains two support-compatible deletion cliques of order at least four, intersecting in the original omitted label `x`.

## Proof

Consider `R_P`.
Since it is a non-Hamiltonian six-set, the four-of-six theorem gives at least four vertices `d in R_P` for which
`R_P-{d}`
is Hamiltonian. Hence
`|G(R_P)|>=4`.

Fix `d in G(R_P)` and choose a Hamilton path `P_d` on `R_P-{d}`.
The supports
`R_P-{d}`
and
`V(Q)`
are disjoint, nonempty, and partition
`V(H)-{d}`.
Thus
`F_d=P_d|Q`
is a two-path cover of `H-d`.

It is exact. If `H-d` were Hamiltonian, a Hamilton path on `H-d` together with the singleton `(d)` would give a spanning two-cover of `H`, contradiction.

Now fix distinct
`d,e in G(R_P)`.
On the common vertex set
`V(H)-{d,e}`,
the cover `F_d` restricts to the support partition

`(R_P-{d,e}) | V(Q)`.

The cover `F_e` restricts to exactly the same two support classes.
Therefore `F_d,F_e` agree on component membership for every pair of common vertices.

This holds for every pair in the family, so the family is a clique in the support-compatibility relation.
The only possible incompatibility is the relative order assigned to vertices of
`R_P-{d,e}`;
the untouched class `Q` may be normalized to the same Hamilton order throughout.

The argument for `R_Q` is symmetric. ∎

## Order-eleven interpretation

The dense singleton-swap phenomenon is stronger at the support level than the ordinary omission graph suggests. Around every state, both sides generate a four-or-larger coherent support clique. Hence an order-eleven obstruction cannot hide behind arbitrary repartitioning there: its local difficulty is entirely ordered-path incompatibility inside overlapping bad six-sets.

# Internal non-clean deletion theorem

Let `H` be an order-eleven minimum counterexample with ordinary extremal type `(5,5,1)`. Equivalently, `H` has no tight path of order six.

Fix any exact equitable deletion state

`H-x=P|Q`,

where

`P=(p_0,p_1,p_2,p_3,p_4)`,
`Q=(q_0,q_1,q_2,q_3,q_4)`.

For a vertex of one displayed component, call its Hamiltonian deletion **clean** when replacing that vertex by `x` in the same displayed slot gives a tight five-path, as in `the clean-replacement classification earlier in this testbed`.

## Theorem

At least one of the two components contains an **internal** vertex whose deletion from the corresponding six-set `V(P) union {x}` or `V(Q) union {x}` is Hamiltonian but non-clean.

Consequently, choosing the resulting canonical exact cover of that vertex deletion and applying `the internal-deletion localization theorem in the deletion-cover dynamics module`, one obtains either

1. an ordinary crossing edge joining two of the inherited path pieces; or
2. a relative-order disagreement with the inherited order.

Thus every order-eleven max-path-five deletion state exposes explicit crossing/order complexity at an internal vertex.

## Proof

We need three elementary steps.

### Step 1: positions 1 and 3 can never be clean

Let
`R=(r_0,r_1,r_2,r_3,r_4)`
be either component.

Suppose `r_1` were clean. Then

`(r_0,x,r_2,r_3,r_4)`

is tight.
Inspect the reversal pair

`(x,r_0,r_1)`, `(r_1,r_0,x)`.

If the first triple is tight, then

`(x,r_0,r_1,r_2,r_3,r_4)`

is a tight six-path, using the inherited path `R` after its first two vertices.

If the reverse triple is tight, then

`(r_1,r_0,x,r_2,r_3,r_4)`

is a tight six-path, using the clean replacement path after `r_0`.

Both alternatives are impossible. Hence `r_1` is not clean.

The argument for `r_3` is symmetric. If `r_3` is clean, inspect
`(r_3,r_4,x)`
versus
`(x,r_4,r_3)`.
The first orientation appends `x` to the original path, while the second appends `r_3` to
`(r_0,r_1,r_2,x,r_4)`.
Either way a tight six-path results.

Therefore clean positions on a five-component are contained in
`{0,2,4}`.

### Step 2: absence of an internal non-clean good deletion forces the central position clean

Put
`R^+=V(R) union {x}`.
This six-set is non-Hamiltonian, since `H` has no six-path. Deleting `x` leaves the Hamiltonian path `R`.

By four-of-six, at least three vertices `r_i` have
`H[R^+-{r_i}]`
Hamiltonian.

Assume there is no internal non-clean good deletion in this component.

If `r_1` or `r_3` were good, Step 1 says it is not clean, giving exactly such an internal non-clean deletion. Hence both `r_1,r_3` are bad.

Therefore all three remaining positions
`r_0,r_2,r_4`
are good. Since `r_2` is internal and by assumption no internal good deletion is non-clean, `r_2` must be clean.

Thus: if a component has no internal non-clean good deletion, its central position is clean.

### Step 3: the two central positions cannot both be clean

Suppose for contradiction that neither component has an internal non-clean good deletion. By Step 2, both `p_2` and `q_2` are clean.

Thus the following replacement paths are tight:

`(p_0,p_1,x,p_3,p_4)`,
`(q_0,q_1,x,q_3,q_4)`.

Inspect the reversal pair
`(p_3,x,q_3)`
and
`(q_3,x,p_3)`.
The hypotheses are symmetric under interchanging the names `P,Q`, so it suffices to treat
`(p_3,x,q_3)`
tight.

Assume no six-path exists. Repeatedly, whenever all but one consecutive triple of a displayed six-vertex order are already tight, the remaining triple must be non-tight and boundary antisymmetry forces its reverse.

| # | forbidden six-vertex order | forced tight triple |
|---:|---|---|
|1|`(p_0,p_1,p_2,p_3,x,q_3)`|`(x,p_3,p_2)`|
|2|`(p_3,q_0,q_1,x,q_3,q_4)`|`(q_1,q_0,p_3)`|
|3|`(q_1,q_0,p_3,x,q_3,q_4)`|`(x,p_3,q_0)`|
|4|`(q_2,q_0,q_1,x,q_3,q_4)`|`(q_1,q_0,q_2)`|
|5|`(p_0,p_1,x,p_3,p_2,q_2)`|`(q_2,p_2,p_3)`|
|6|`(p_0,p_1,x,p_3,q_0,q_2)`|`(q_2,q_0,p_3)`|
|7|`(q_0,q_1,q_2,p_2,p_3,p_4)`|`(p_2,q_2,q_1)`|
|8|`(q_1,q_0,q_2,p_2,p_3,p_4)`|`(p_2,q_2,q_0)`|
|9|`(p_2,q_2,q_1,x,q_3,q_4)`|`(x,q_1,q_2)`|
|10|`(p_0,p_1,p_2,q_2,q_0,p_3)`|`(q_2,p_2,p_1)`|
|11|`(p_0,p_1,x,q_1,q_2,q_3)`|`(q_1,x,p_1)`|
|12|`(q_1,x,p_1,p_2,p_3,p_4)`|`(p_2,p_1,x)`|

Now row 10 gives
`(q_2,p_2,p_1)`
tight, row 12 gives
`(p_2,p_1,x)`
tight, and central cleanliness of `p_2` gives
`(p_1,x,p_3)`
and
`(x,p_3,p_4)`
tight.

Hence

`(q_2,p_2,p_1,x,p_3,p_4)`

is a tight six-path, contradiction.

The opposite initial orientation `(q_3,x,p_3)` is identical after interchanging `P` and `Q`.

Thus the two central positions cannot both be clean.

Combining Steps 2 and 3, at least one component has an internal good deletion that is non-clean.

Finally choose a Hamilton path on that good five-set and pair it with the untouched opposite component to obtain the canonical exact cover of the corresponding vertex deletion. Outcome 3 of `the internal-deletion localization theorem in the deletion-cover dynamics module` would be the same-slot clean replacement, which has been excluded. Therefore outcome 1 or 2 holds: crossing or relative-order disagreement. ∎
