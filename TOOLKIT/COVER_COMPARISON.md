# Cover-comparison and matching lemmas

**Status: UNAUDITED GN3 REWRITE.**

These statements isolate general combinatorial facts that were previously embedded in A7C3 cover-comparison machinery. The exact text below has not yet received independent GN3 audit.

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

A crossing between two singleton components gives no three-vertex information by itself. In particular, an ordered two-vertex path is tight vacuously in either direction, so assigning opposite roles to two singleton paths cannot create a new tight triple. Any argument using two singleton components must retain some additional vertex or triple information.

## 2. A Cartesian clause lemma

Let `I_1,...,I_m` be nonempty finite sets. For each `j` and each `i in I_j`, let `P_{j,i}` be a Boolean statement. Suppose that for every tuple

`(i_1,...,i_m) in I_1 x ... x I_m`

at least one of

`P_{1,i_1},...,P_{m,i_m}`

is true. Then for some `j`, every statement `P_{j,i}` with `i in I_j` is true.

**Proof.** If no coordinate family were entirely true, choose for every `j` an index `i_j` for which `P_{j,i_j}` is false. The resulting tuple would make all `m` statements false, contradicting the hypothesis. ∎

### Boundary-tournament form

Suppose `pc(H)>k`. For `j=1,...,m`, let `{alpha_{j,i}:i in I_j}` be finite families of ordered triples. Assume that for every tuple `(i_1,...,i_m)` there is a spanning `k`-path proposal whose only triples not already known to be tight are

`h_{1,i_1},...,h_{m,i_m}`,

where `alpha_{j,i}` is the reverse of `h_{j,i}`. Then for some `j`, every triple `alpha_{j,i}` is tight.

Indeed, each proposed `k`-cover must contain a non-tight displayed triple; boundary antisymmetry therefore makes at least one corresponding `alpha_{j,i_j}` tight. The Cartesian clause lemma applies.

## 3. A weighted symmetric-difference lemma for two matchings

Let `F` and `J` be matchings in the same finite graph, with

`|F|=|J|+1`.

Let `w:E -> R_{>=0}` be a nonnegative edge weight such that every edge of `J` has weight zero, and suppose

`W=sum_{e in F} w(e)>0`.

Decompose `F triangle J` into its alternating connected components. For such a component `C`, put

`delta(C)=|F intersect C|-|J intersect C|`

and

`omega(C)=sum_{e in F intersect C} w(e)`.

Then exactly one of the following conclusions is available:

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