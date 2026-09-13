# Two-vertex insertion localization on the Hamilton spectator path

Status: **provisional working mathematics**. This is an unaudited exact reduction for the active source-complement / zipper line. It does not prove that any complementary support is Hamiltonian, and it does not replace the physical-realization gap in `source-complement-zipper.md`.

## Orientation

Work with a tight Hamilton spectator path

    B=(b_0,b_1,...,b_k)

and vertices outside `B`. The live source frame has `X={v,p,q,r}` and three complementary supports

    C_s = H[B union {v,s}],   s in {p,q,r},

all of which must be nonHamiltonian in a counterexample by the source-complement construction. The point here is to extract a coupled consequence of those three failures without pretending that a Hamilton path must preserve the displayed `B` order.

The disjoint-slot reduction uses only R887/R3's exact turn-comparison interpretation and actual nonHamiltonicity of the supports. The final common-certificate dichotomy also uses the provisional canonical prefix-barrier development in `two-vertex-extension-barrier.md`.

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

## 5. The empty-anchor branch has a common prefix barrier

The concurrent development `two-vertex-extension-barrier.md` constructs the positive-prefix automaton `A(B;v,s)` for all `B`-ordered words and proves that, before the companion `s` is consumed, its reachable geometry is exactly the same one-outside-vertex automaton `A(B;v)` for every companion.

This interacts cleanly with the insertion sets above. A `B`-ordered Hamilton word on `B union {v}` is exactly `B_t(v)` for one slot `t`. Therefore

    I_B(v)=empty

is equivalent to the absence of a positive terminal in `A(B;v)`. In that case its canonical positive-reachable region `R_0` excludes all terminals, and

    K_0 = delta^+(R_0)

is a cut consisting entirely of reversed comparison transitions. Because the whole `s`-free subautomaton of every `A(B;v,s)` is literally `A(B;v)`, this `K_0` is companion-independent: all three two-vertex extension problems inherit the same obstruction before `p`, `q`, or `r` is consumed.

This does **not** physically close the empty-anchor branch. It converts it into the common-cut certificate requested by the parent-obstruction strategy.

Provisional dependency: the canonical prefix-automaton/barrier argument in `A7C3/WORKSPACE/two-vertex-extension-barrier.md` (concurrent unaudited workspace mathematics).

## 6. Common-certificate dichotomy for the prescribed-B-order problem

Under the live counterexample premise that every `C_s` is nonHamiltonian, exactly one of the following applies.

### A. Empty anchor

    I_B(v)=empty.

Then all three companion problems share the same canonical pre-companion comparison cut `K_0` in `A(B;v)`.

### B. Nonempty anchor

    I_B(v) != empty.

Then every successful one-vertex insertion of every source companion lies in the common window

    W_B(v),

which has at most three consecutive slots; if `diam I_B(v)=2` it is one slot, and if `diam I_B(v)>=3` it is empty.

Thus the three failures always admit a companion-independent obstruction interface at the prescribed-order level: either one shared prefix barrier before companion consumption, or one common bounded slot window.

This is a classification of the **restricted B-order-preserving obstruction**, not a classification of full Hamiltonicity in `C_s`. The remaining G39 work is to use actual source-frame structure to consume the resulting common certificate physically.

## Scope fence

- No claim is made that nonHamiltonicity of `C_s` is equivalent to failure of `B`-order-preserving insertion.
- No claim is made that a successful adjacency pattern is already a physical spanning cover beyond the explicit combined word constructed in the lemma.
- No arbitrary reversal of `B` or a residual path is used.
- D17.439's conditional recompletion interface is not being promoted to a physical theorem here.
- The disjoint-slot/common-window result is independent of provisional D17.433-D17.439 ancestry claims.
- The common-prefix-barrier half of the final dichotomy uses the explicitly named provisional workspace dependency above and therefore remains provisional with it.

## Strategic consequence

At the prescribed-order level, the Vice Director's desired parent obstruction has contracted to a companion-independent certificate in every case. The remaining target is no longer “couple three arbitrary nonHamiltonian supports.” It is:

> consume either the common pre-companion prefix barrier `K_0`, or the common at-most-three-slot window `W_B(v)`, using the retained source-frame data.

The exact D17.421 first-loss rectangle, old source two-cover `F`, and source turns should now be tested as consumers of these two common certificates rather than as three separate companion-by-companion Hamiltonicity arguments.
