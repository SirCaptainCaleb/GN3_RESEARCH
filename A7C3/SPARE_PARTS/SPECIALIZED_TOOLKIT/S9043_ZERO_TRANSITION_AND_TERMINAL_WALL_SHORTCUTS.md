# S9043 — Zero-Transition and Terminal-Wall Shortcuts

## Theorem A — Zero-transition symmetric-difference contraction

Let `F` and `J` be split-copy matchings on the same vertex set with

`|F|=|J|+1`

and

`tau(J)=0`.

Decompose `F triangle J` into alternating components `C`. For each component put

`delta(C)=|F intersect C|-|J intersect C| in {-1,0,1}`

and

`w(C)=tau(F intersect C)-tau(J intersect C)`.

Then exactly one of the following alternatives is available.

1. Some union `S` of alternating components satisfies

   `sum_{C in S} delta(C)=1`

   and

   `sum_{C in S} w(C)<tau(F)`.

2. There is a unique `F`-heavy alternating path `C*` with `delta(C*)=1`; it carries every transition of `F`, there is no `J`-heavy component, and every other alternating component is matching-balanced and has transition weight zero.

### Proof

Because `tau(J)=0`, every selected state of `J` is same-side. Hence for every alternating component

`w(C)=tau(F intersect C)>=0`.

Moreover

`sum_C delta(C)=|F|-|J|=1`

and

`sum_C w(C)=tau(F)`.

Assume Alternative 1 fails. In particular, every individual `F`-heavy component, for which `delta(C)=1`, must have weight at least `tau(F)`. Since all weights are nonnegative and their total is exactly `tau(F)`, there can be at most one `F`-heavy component. The total cardinality excess is one, so at least one exists; call it `C*`. Necessarily

`w(C*)=tau(F)`,

and every other component has weight zero.

If a `J`-heavy component with `delta=-1` existed, the identity `sum delta=1` would require at least one additional `F`-heavy component besides `C*`, impossible. Therefore there is no `J`-heavy component. All components other than `C*` are balanced and have weight zero. Finally, an alternating component with edge-count excess one for `F` is an alternating path, so `C*` is the unique `F`-heavy alternating path. Since its weight is all of `tau(F)`, it carries every transition of `F`. ∎

## Theorem B — One-ended source rooting forces first-positive index one

Assume the synchronized singleton-star setting with

`G=H-{A,C}=X union B`, `X={v,p,q,r}`,

and let `F` be the retained top exact two-cover. Suppose

`tau(F)>=3`.

For a source `s`, let

`J_s=(s)|J_{tu}|B`

be the synchronized zero-transition spanning three-forest, where `{t,u}={p,q,r}-{s}`. Apply Theorem A to `F,J_s` and suppose its lower-transition union alternative does not occur. Then one can choose `s` so that, after orienting the unique heavy path `C*` appropriately, the first `F`-edge of `C*` is already an `X|B` transition. In the usual alternating zipper notation, the first-positive index is therefore

`r=1`.

### Proof

The exact cover `F` has at least three selected `X|B` transitions. The nonsource vertex `v` has selected degree at most two in a path cover, so at most two of those transition edges can be incident with `v`. Hence some selected transition is incident with a retained source; choose such a source `s`.

In `J_s`, the source `s` is a singleton. Both split copies of `s` are therefore unmatched by `J_s`. Let `xi` be the split copy of `s` used by the chosen transition edge of `F`. In `F triangle J_s`, the vertex `xi` is an endpoint of its alternating component, and that component contains an `F` transition. Since `tau(J_s)=0`, its transition weight is positive.

In the second alternative of Theorem A, the unique positive-weight component is the unique `F`-heavy path `C*`. Therefore `xi` is an endpoint of `C*`. Orient `C*` from `xi`. Because `xi` is `F`-only, the first alternating state is an `F`-state `e_1`, and by construction it is the chosen transition. Every `J_s` state has transition indicator zero. Hence

`S_1=chi(e_1)-chi(f_1)=1`

whenever the paired `J_s` state `f_1` exists. Thus the first positive prefix occurs at index one. Since `C*` carries all `tau(F)>=3` transitions, the path is not the degenerate single-`F`-edge case. ∎

### Warning

This theorem is deliberately one-ended. It does **not** imply that both split copies of `s` lie on `C*`. The other source port may lie on a balanced zero-weight alternating path.

## Theorem C — Globally longest path gives the terminal-wall interface directly

Let `H` be a hypothetical smallest counterexample. Choose a globally longest vertex-simple tight path

`A=(a_0,...,a_s)`.

Then the complement `H-V(A)` has an exact two-cover `B|C`, and

`A|B|C`

is already a no-slide terminal marked three-forest of the first-source phase-descent engine. Consequently the terminal-wall construction yields its certified opposite-polarity pair together with a retained tight turn, without any preceding qualification-engine geometry.

### Proof

The path `A` is proper: a spanning tight path would itself contradict `pc(H)>2`. The complement `H-V(A)` is a proper induced subsystem, so minimality gives a cover by at most two paths. It cannot be Hamiltonian, because a Hamilton path of the complement together with `A` would form a spanning two-cover of `H`. Thus

`H-V(A)=B|C`

is an exact two-cover and `A|B|C` is a literal spanning three-cover.

Global maximality of `A` is stronger than the terminal no-slide condition. Let `X=(x_0,...,x_m)` be either donor rail. At the right endpoint of `A`, if

`(a_{s-1},a_s,x_0)`

were tight, then appending `x_0` would produce a tight path longer than `A`, contradiction. Hence this inward gate is bad, and boundary antisymmetry gives

`(x_0,a_s,a_{s-1})`

tight. Dually the left inward gate is bad and

`(a_1,a_0,x_m)`

is tight. Thus no endpoint-growth move is available from either donor rail: the three-forest is already a terminal wall.

Every three distinct vertices admit one tight orientation by boundary antisymmetry, so `|A|>=3`.

If `|A|>=4`, the disjoint reverse boundary dimers

`D_L=(a_1,a_0)`, `D_R=(a_s,a_{s-1})`

carry the two opposite endpoint polarities furnished by the donor witnesses above. They are exactly the terminal-wall `2+2` opposite-sign pair. Retain any consecutive tight turn of `A` as the fixed turn.

If `|A|=3`, write `A=(a_0,a_1,a_2)` and delete the hinge `a_1`. The residue `H-a_1` cannot be Hamiltonian, else its Hamilton path together with singleton `(a_1)` would two-cover `H`; minimality therefore gives an exact two-cover `T` of `H-a_1`. Deleting the hinge from `A|B|C` leaves the literal four-cover

`(a_0)|(a_2)|B|C`.

Some selected edge of `T` must cross two of these four inherited components, since two connected rails cannot otherwise span all four. Combining such a crossing with the hinge and applying boundary antisymmetry exactly as in the order-three terminal-wall argument produces the certified opposite-polarity singleton/dimer `1+2` pair, while the original turn `(a_0,a_1,a_2)` is retained.

Hence the complete terminal-wall phase-zero interface exists directly from a globally longest path. ∎

## Why this is reusable

Theorem A isolates the exact algebra behind zero-transition comparison states. Theorem B shows that, once a transition-bearing source is chosen, the synchronized zero-transition comparison has no long pre-positive zipper corridor. Theorem C is independent of the synchronized source geometry altogether: a globally longest tight path produces the terminal-wall interface immediately.

## Scope and nonclaims

Theorem C constructs the terminal-wall **interface**; it does not by itself prove a strict descent from a previously retained phase-one checkpoint, nor does it prove global extinction after entering phase zero. Theorem B relies only on one source port and must not be strengthened to a two-ended source-rooting statement without additional hypotheses.

## Provenance

Theorem A is the surviving audited core of workspace result `R2154`. Theorem B is the independently audited repair `R2160`. Theorem C is the independently audited global shortcut `R2156`. The withdrawn two-ended synchronized application originally attached to `R2154` is intentionally not included.