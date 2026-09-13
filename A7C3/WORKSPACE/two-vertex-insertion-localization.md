# Two-vertex insertion localization on the Hamilton spectator path

Status: **provisional working mathematics**. This is an unaudited exact reduction for the active source-complement / zipper line. It does not prove that any complementary support is Hamiltonian, and it does not replace the physical-realization gap in `source-complement-zipper.md`.

## Orientation

Work with a tight Hamilton spectator path

    B=(b_0,b_1,...,b_k)

and vertices outside `B`. The live source frame has `X={v,p,q,r}` and three complementary supports

    C_s = H[B union {v,s}],   s in {p,q,r},

all of which must be nonHamiltonian in a counterexample by the source-complement construction. The point here is to extract a coupled consequence of those three failures without pretending that a Hamilton path must preserve the displayed `B` order.

The reduction uses only R887/R3's exact turn-comparison interpretation and actual nonHamiltonicity of the supports.

## 1. Successful one-vertex insertion slots

Number the `k+2` slots of `B` by `0,1,...,k+1`:

- slot `0` is before `b_0`;
- slot `t`, for `1 <= t <= k`, is between `b_{t-1}` and `b_t`;
- slot `k+1` is after `b_k`.

For `x` outside `B`, let `B_t(x)` be the vertex word obtained by inserting `x` in slot `t` and otherwise preserving the order of `B`. Define

    I_B(x) = { t : B_t(x) is a tight path }.

This is only a prescribed-order insertion set. `I_B(x)=empty` does **not** say that `H[B union {x}]` is nonHamiltonian, because a Hamilton path could reorder `B`.

## 2. Disjoint-slot recompletion lemma

**Lemma.** Let `x,y` be distinct vertices outside `B`. If

    a in I_B(x),   c in I_B(y),   and |a-c| >= 2,

then `H[B union {x,y}]` has a tight Hamilton path preserving the original order of `B`, obtained by inserting `x` in slot `a` and `y` in slot `c`.

### Proof

For a slot `t`, inserting one vertex can change tight-turn conditions only locally:

- at the inserted vertex itself;
- at `b_0` for slot `0`;
- at `b_k` for slot `k+1`;
- at `b_{t-1}` and `b_t` for an internal slot `t`.

All other consecutive triples are unchanged triples of the already-tight word `B`.

If `|a-c|>=2`, the sets of old `B` vertices adjacent to the two slots are disjoint. Therefore every consecutive triple in the word with both insertions is of one of three kinds:

1. an unchanged consecutive triple of `B`;
2. a local triple occurring in `B_a(x)`;
3. a local triple occurring in `B_c(y)`.

The first kind is tight because `B` is tight, the second because `a in I_B(x)`, and the third because `c in I_B(y)`. Hence the combined word is tight and uses every vertex of `B union {x,y}` exactly once. QED.

The distance-one case is genuinely different: adjacent insertions share an old `B` vertex, and the combined word contains a new cross-turn not certified by either one-vertex insertion separately.

## 3. Necessary obstruction for a nonHamiltonian two-vertex support

**Corollary.** If `H[B union {x,y}]` is nonHamiltonian, then

    |a-c| <= 1

for every `a in I_B(x)` and every `c in I_B(y)`.

Equivalently, once `I_B(x)` is nonempty,

    I_B(y) subset W_B(x),

where

    W_B(x) = intersection over a in I_B(x) of ({a-1,a,a+1} intersect {0,...,k+1}).

This is only a necessary obstruction. It is safe despite possible reorderings of `B`: actual nonHamiltonicity forbids the particular `B`-order-preserving Hamilton path supplied by the lemma.

## 4. Three-complement common-window consequence

Return to the live source frame. Since every

    C_s = H[B union {v,s}],   s in {p,q,r},

is nonHamiltonian in a counterexample, the corollary applies simultaneously with the same anchor `v`. Hence, if `I_B(v)` is nonempty,

    I_B(p) union I_B(q) union I_B(r) subset W_B(v).

Thus all successful prescribed-order insertions of all three source spokes are trapped in one common slot window determined solely by `v`.

Writing `diam I_B(v)` for the maximum slot difference, when `I_B(v)` is nonempty:

- if `diam I_B(v) >= 3`, then `W_B(v)=empty`, so `I_B(p)=I_B(q)=I_B(r)=empty`;
- if `diam I_B(v)=2`, then `W_B(v)` is a singleton;
- if `diam I_B(v)=1`, then `W_B(v)` has at most two consecutive slots;
- if `diam I_B(v)=0`, then `W_B(v)` has at most three consecutive slots.

So the three simultaneous two-vertex failures do not behave independently. Unless `v` itself has no successful prescribed-order insertion, every successful one-vertex insertion of every source spoke is forced into a common window of width at most three slots, and often one or two.

## 5. Exact remaining branch for a parent theorem

This reduction exposes a sharp fork for the desired parent two-vertex extension/obstruction theorem.

### Nonempty-anchor branch

If `I_B(v)` is nonempty, the three support failures already produce a common localized obstruction window. Any stronger source-frame argument only has to consume this bounded window, not three unrelated Hamiltonicity failures. In particular, existing first-loss / comparison machinery should be tested against this one shared location rather than run independently in each `C_s`.

### Empty-anchor branch

If `I_B(v)=empty`, the lemma gives no localization at all. This is not a technical nuisance that may be silently discarded: arbitrary boundary-tournament comparison data can make every prescribed-order insertion of one outside vertex fail. A complete parent theorem therefore needs an additional source-frame reason either

1. to rule out `I_B(v)=empty`;
2. to convert that branch directly into a spanning two-cover or strict physical descent; or
3. to replace `v` by another anchor for which the live hypotheses really do provide a nonempty insertion set.

This is the precise residual obstruction left by the present reduction.

## Scope fence

- No claim is made that nonHamiltonicity of `C_s` is equivalent to failure of `B`-order-preserving insertion.
- No claim is made that a successful adjacency pattern is already a physical spanning cover beyond the explicit combined word constructed in the lemma.
- No arbitrary reversal of `B` or a residual path is used.
- D17.439's conditional recompletion interface is not being promoted to a physical theorem here.
- The result is independent of the provisional D17.433-D17.439 ancestry claims; it uses only the live complementary-support setup plus the exact tight-path semantics of R887/R3.

## Strategic consequence

The parent obstruction problem has contracted from “couple three arbitrary nonHamiltonian supports” to the following narrower target:

> eliminate or consume the empty-anchor branch, and in the nonempty-anchor branch consume one common window of at most three consecutive `B` slots.

That is the natural next interface to compare with the exact D17.421 first-loss rectangle and any source-frame constraint capable of turning a localized slot window into a literal tight recompletion or physical descent.
