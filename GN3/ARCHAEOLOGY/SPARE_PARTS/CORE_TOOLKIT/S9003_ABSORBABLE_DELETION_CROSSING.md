# S9003 — Absorbable-Deletion Crossing Lemma

## Theorem

Let `H` be a finite boundary tournament with path-cover number `pc(H)>2`. Let `D` be a nonempty proper vertex set, put

`W = V(H) \ D`,

and let `S` be a nonempty proper subset of `W`. Suppose there is a vertex-simple tight path `Q` whose vertex set is exactly

`D ∪ S`.

Then every literal spanning two-path cover

`T = T_1 | T_2`

of `H-D` selects an adjacent directed state with one endpoint in `S` and the other in `W\S`.

Equivalently, if the deleted vertices together with one remainder block `S` can already be absorbed into a certified tight path, then no two-cover of the deletion can keep `S` completely separated from the complementary remainder.

No Strong Level-(1) antisymmetry, smallest-counterexample minimality, endpoint hypothesis, or extremality assumption is needed once the displayed objects exist.

## Proof

Assume for contradiction that `T` selects no adjacent state crossing the cut

`S | (W\S)`.

A path component of `T` cannot contain vertices from both sides of this cut. Indeed, if some ordered rail did, then while traversing that rail there would be a first adjacent pair at which the vertex sequence leaves one side and enters the other. That adjacent selected state would cross the cut.

Hence each of `T_1,T_2` lies wholly inside `S` or wholly inside `W\S`. Both sides are nonempty and the two rails together cover all of `W`, so after exchanging the two rail names if necessary,

`V(T_1)=S`,

`V(T_2)=W\S`.

But `Q` is a tight path on exactly `D∪S`. Therefore `Q` and `T_2` are vertex-disjoint tight paths and

`V(Q) ∪ V(T_2) = D ∪ S ∪ (W\S) = V(H)`.

Thus `Q | T_2` is a spanning two-cover of `H`, contradicting `pc(H)>2`.

So every two-cover of `H-D` must contain a selected crossing of `S | (W\S)`. ∎

## Why this is reusable

The lemma is a generic **crossing compiler**. It does not care how the deletion two-cover was produced or why the block `S` is absorbable. Once one certified path absorbs `D∪S`, every two-cover of the deletion is forced to reveal a physical crossing between `S` and its complement.

That crossing can then be consumed by whatever downstream mechanism is appropriate: component-drop comparison, signed-support birth, local splice analysis, or a more specialized current-frame argument.

## Scope and nonclaims

The theorem does not produce the deletion two-cover. It does not prescribe the direction, rail, or endpoint location of the crossing, and it does not assert that the crossing persists in another representative.

The conclusion is purely the existence of an actual selected crossing in the displayed cover `T`; any stronger consequence requires a separate consumer.

## Provenance

Rescued from the accepted order-free parent theorem historically recorded as `R508`. Corpus mining repeatedly surfaced `selected crossing` and deletion/recompletion vocabulary across the project; theorem-level archaeology showed that this is the clean general mechanism beneath several later specialized crossing arguments.