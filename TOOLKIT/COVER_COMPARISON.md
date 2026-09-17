# Cover-comparison and matching lemmas

**Status: REVISED AFTER AUDIT; PENDING RE-AUDIT.**

These statements isolate general combinatorial facts that were previously embedded in A7C3 cover-comparison machinery. The mathematical content has been rewritten in intrinsic GN3 language; the revised exact text awaits independent re-audit.

## 1. A component drop forces a crossing edge

Let `H` be a boundary tournament and let `W subseteq V(H)`. Suppose `H[W]` has path covers

`R=R_1|...|R_c`

and

`T=T_1|...|T_r`

with `r<c`. Then some ordinary edge `xy` of a component of `T` has its endpoints in two different components of `R`.

If the `R`-component containing `x` is nontrivial and `p` is a neighbor of `x` along that component, then exactly one of

`(y,x,p)`, `(p,x,y)`

is tight.

**Proof.** Suppose every ordinary edge of every component of `T` had both endpoints in one component of `R`. Since each `T_i` is connected, every `T_i` would then lie in a single `R_j`. Because the `T_i` cover `W`, every one of the `c` nonempty components of `R` would contain at least one component of `T`. Distinct components of `R` are disjoint, so these components of `T` would be distinct. Hence `r>=c`, a contradiction.

Thus some edge `xy` of `T` crosses two components of `R`. If the component containing `x` is nontrivial, choose a path neighbor `p` of `x` in that component. The vertices `p,x,y` are distinct, and boundary antisymmetry gives exactly one tight member of the displayed reversal pair. ∎

Each singleton component contains no ordered triple, and every two-vertex ordering is a tight path vacuously. Thus the orders of two singleton components alone impose no tightness condition on any ordered triple of distinct vertices.

## 2. A Cartesian clause lemma

Let `I_1,...,I_m` be nonempty finite sets. For each `j` and each `i in I_j`, let `P_{j,i}` be a Boolean statement. Suppose that for every tuple

`(i_1,...,i_m) in I_1 x ... x I_m`

at least one of

`P_{1,i_1},...,P_{m,i_m}`

is true. Then for some `j`, every statement `P_{j,i}` with `i in I_j` is true.

**Proof.** If no coordinate family were entirely true, choose for every `j` an index `i_j` for which `P_{j,i_j}` is false. The resulting tuple would make all `m` statements false, contradicting the hypothesis. ∎

### Boundary-tournament form

Let `H` be a boundary tournament, and let `k>=1` be an integer with `pc(H)>k`. For `j=1,...,m`, let `{alpha_{j,i}:i in I_j}` be finite families of ordered triples of distinct vertices of `H`, and for each `alpha_{j,i}` let `h_{j,i}` be its reverse.

Assume that for every tuple `(i_1,...,i_m)` there exist `k` pairwise vertex-disjoint vertex-simple sequences whose vertex sets partition `V(H)` and such that:

- every consecutive ordered triple of every sequence, other than the listed triples

  `h_{1,i_1},...,h_{m,i_m}`,

  is tight; and
- each listed triple `h_{j,i_j}` occurs as a consecutive ordered triple of one of the `k` sequences.

Then for some `j`, every triple `alpha_{j,i}`, `i in I_j`, is tight.

**Proof.** Fix a tuple `(i_1,...,i_m)` and the corresponding `k` sequences. If every listed triple `h_{j,i_j}` were tight, then every consecutive triple in every vertex-simple sequence would be tight. The sequences would therefore be `k` tight paths forming a spanning `k`-path cover of `H`, contrary to `pc(H)>k`.

Hence at least one listed triple `h_{j,i_j}` is non-tight. Boundary antisymmetry makes its reverse `alpha_{j,i_j}` tight. Thus for every tuple at least one of the Boolean statements

`P_{j,i_j} := [alpha_{j,i_j} is tight]`

is true. The Cartesian clause lemma gives an index `j` for which every `alpha_{j,i}` is tight. ∎

## 3. A weighted symmetric-difference lemma for two matchings

Let `G=(V,E)` be a finite graph, and let `F` and `J` be matchings in `G`, with

`|F|=|J|+1`.

Let `w:E -> R_{>=0}` be a nonnegative edge weight such that every edge of `J` has weight zero, and suppose

`W=sum_{e in F} w(e)>0`.

Decompose `F triangle J` into its alternating connected components. For such a component `C`, put

`delta(C)=|F intersect C|-|J intersect C|`

and

`omega(C)=sum_{e in F intersect C} w(e)`.

Then exactly one of the following holds:

1. some union `S` of alternating components satisfies

   `sum_{C in S} delta(C)=1`

   and

   `sum_{C in S} omega(C)<W`;

2. there is a unique alternating path `C_*` with `delta(C_*)=1`; it satisfies `omega(C_*)=W`, there is no component with `delta=-1`, and every other alternating component has `delta=0` and weight zero.

**Proof.** Every alternating component of two matchings has `delta in {-1,0,1}`. Moreover

`sum_C delta(C)=|F|-|J|=1`

and

`sum_C omega(C)=W`.

Assume the first conclusion fails. In particular, every component with `delta=1` must have weight at least `W`, because that component alone would otherwise satisfy conclusion 1. Since all component weights are nonnegative, their total is `W`, and `W>0`, there can be at most one component with `delta=1`. The total excess is one, so such a component exists; call it `C_*`. Necessarily `omega(C_*)=W`, and every other component has weight zero.

If some component had `delta=-1`, then with only one component of excess `+1` the sum of all `delta` values could not equal `1`. Thus no such component exists, and every remaining component is balanced. A symmetric-difference component with one more `F`-edge than `J`-edge is an alternating path, so `C_*` is the unique `F`-heavy alternating path. ∎

The positivity hypothesis `W>0` is essential for this formulation: with zero total weight, several zero-weight `F`-heavy components can coexist with `J`-heavy components.

A useful specialization takes `w` to be the indicator of edges crossing a fixed vertex partition. If `J` uses no crossing edge, the second alternative says that one alternating path contains every crossing edge of `F`.

## Legacy provenance

Section 1 is the intrinsic content of A7C3 `S9002`; its singleton warning replaces the formal signed-singleton language of `S9007`. Section 2 rewrites `S9036`. Section 3 is the reusable matching core of `S9043(A)`, with the missing positive-total-weight hypothesis made explicit.