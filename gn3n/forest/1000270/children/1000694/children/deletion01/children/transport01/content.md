# Endpoint transport and local obstruction geometry

## Statement

Endpoint replacement and bounded insertion-obstruction geometry; cyclic first-type kernels and pivot-pivot cross-swaps; and for the universal cyclic four-kernel, every three-kernel plus two exterior vertices is Hamiltonian, forcing quantitative two-for-one support-exchange density.

## Body

# Endpoint transport and bounded local obstruction geometry

# Opposite inherited endpoint attachments replace both path endpoints

Let

W=(w_0,w_1,...,w_k),  k>=3,

be a tight path in a boundary tournament. Let ell and r be vertices outside V(W). Assume

(ell,w_1,...,w_k)

and

(w_0,...,w_{k-1},r)

are tight paths.

## Lemma

If ell and r are distinct, then

(ell,w_1,...,w_{k-1},r)

is a tight path. It has the same order as W and is obtained by replacing the two endpoints w_0,w_k by ell,r while preserving the entire common interior order.

If ell=r=z, put M=(w_1,...,w_{k-1}). Then both zM and Mz are tight. Therefore the opposite-concatenation dichotomy in deletion-cover dynamics gives either the tight cycle

(z,w_1,...,w_{k-1})

or the tight wrap triple

(w_1,z,w_{k-1}).

## Proof

Assume first ell!=r. Every consecutive triple of

(ell,w_1,...,w_{k-1},r)

is tight. The first one, (ell,w_1,w_2), occurs in the first assumed path; the last one, (w_{k-2},w_{k-1},r), occurs in the second assumed path; all intervening triples are inherited from W. The vertices are distinct by hypothesis, so the displayed sequence is a tight path.

If ell=r=z, the first assumed path contains the tight prefix zM and the second contains the tight suffix Mz. Apply the opposite-concatenation dichotomy in deletion-cover dynamics to the singleton path (z) and the nontrivial path M. ∎

## Role in the current route

This is the basic transport move in the simple inherited-order endpoint case. When endpoint-deletion covers attach from opposite sides of a long inherited path, distinct attachments move the two endpoints without shortening the path; a repeated attachment produces cycle-or-wrap data instead. The remaining global task is to prove that repeated endpoint replacement either reaches an absorbable reversed end edge / spanning two-cover or admits a genuine well-founded descent.

---


Let `H` be a minimum-order counterexample and let
`W=(w_0,w_1,w_2,w_3,w_4)`
be a proper tight five-vertex path. Put `C=V(H)-V(W)`. By the minimum-counterexample path-complement lemma, `pc(H[C])=2`.

Consider an exact two-path cover `F_0` of `H-w_0`, and write
`S_0=(w_1,w_2,w_3,w_4)`.
Every such cover has at least one ordinary edge between `S_0` and `C`. If it has exactly one such edge, then cutting that edge leaves exactly one block on `S_0` and exactly two blocks on `C`; in particular the `S_0-block is a Hamilton path of `H[S_0]`, while the two `C-blocks form an exact two-path cover of `H[C]`.

If, in addition, the `S_0-block has the inherited order `(w_1,w_2,w_3,w_4)`, then the unique mixed component cannot have the form
`(w_1,w_2,w_3,w_4,R)`
for a nonempty `C-block `R`: prepending `w_0` would give
`(w_0,w_1,w_2,w_3,w_4,R)`,
still tight, and together with the other `C-block would two-cover `H`.
Hence the only inherited-order one-crossing form is
`(R,w_1,w_2,w_3,w_4)|R'`.

Symmetrically, for an exact two-cover `F_4` of `H-w_4`, put
`S_4=(w_0,w_1,w_2,w_3)`.
If there is exactly one `S_4-C` crossing and the `S_4-block has inherited order, then the only possible form is
`(w_0,w_1,w_2,w_3,R)|R'`;
the opposite form `(R,w_0,w_1,w_2,w_3)` would allow appending `w_4` and again two-cover `H`.

Consequently, if both endpoint deletions admit inherited-order one-crossing covers, there exist vertices `ell,r in C` such that the two mixed components contain respectively
`(ell,w_1,w_2,w_3,w_4)`
and
`(w_0,w_1,w_2,w_3,r)`.
Thus both covers share the common middle
`M=(w_1,w_2,w_3)`
with attachments from opposite sides.

If `ell!=r`, the endpoint-replacement lemma above gives
`(ell,w_1,w_2,w_3,r)`
as a tight five-vertex path.
If `ell=r=s`, then both `(s,M)` and `(M,s)` are tight; the opposite-concatenation lemma in deletion-cover dynamics therefore yields either the tight cycle on
`(s,w_1,w_2,w_3)`
or the wrap triple `(w_1,s,w_3)`.

## Proof

Crossing and block counts are `the path-cover surgery and comparison module` Sections 1, 6, and 7, applied with deleted set `{w_0}` or `{w_4}`, Hamiltonian side equal to the whole five-set `W`, and complementary side `C`, whose path-cover number is exactly two. The restoration arguments prove the orientation restrictions. The final two conclusions are the common-middle rectangle and opposite-concatenation lemmas. ∎


---


Keep the setup of `the five-path endpoint-attachment theorem above`. Let
`W=(w_0,w_1,w_2,w_3,w_4)`,
`M=(w_1,w_2,w_3)`,
and `C=V(H)-V(W)`.

Assume both endpoint deletions admit the inherited-order one-crossing covers forced there. Thus for nonempty tight paths `R_0,R_0',R_4,R_4'` on `C`,
`F_0=(R_0,M,w_4)|R_0'`
is an exact two-cover of `H-w_0`, and
`F_4=(w_0,M,R_4)|R_4'`
is an exact two-cover of `H-w_4`.

Delete `w_4` from `F_0` and `w_0` from `F_4`. This gives exact two-covers of the common graph `H-{w_0,w_4}`:
`T_0=(R_0,M)|R_0'`,
`T_4=(M,R_4)|R_4'`.

These two ordered covers cannot be identical. In each, exactly one component contains the three vertices of `M`; hence equality would force the mixed components themselves to agree as ordered paths. But `(R_0,M)` starts with a vertex of `C`, whereas `(M,R_4)` starts with `w_1 in M`, and both `R_0,R_4` are nonempty. Therefore `T_0!=T_4`.

Applying the exact-cover disagreement theorem `the exact-cover disagreement theorem in deletion-cover dynamics` gives:

1. either the unordered support partitions of `T_0,T_4` differ, in which case each cover has an ordinary edge crossing the other's two support classes; or
2. the support partitions agree, in which case the common mixed support has two different Hamilton orders. Indeed every vertex of `R_0` precedes every vertex of `M` in `T_0`, while the same complement-support vertices follow every vertex of `M` in `T_4`. Hence the ordered-path intersection theorem yields a reversed common ordered edge, a tight triple reversing an ordered edge at an intersection, or a vertex-simple tight cycle.

Thus the completely simple endpoint-attachment branch for a specified Hamilton five-path cannot remain compatible after the two endpoints are deleted: it necessarily exposes support or order disagreement on one common two-deletion graph.

## Proof

All assertions before the application of `the exact-cover disagreement theorem in deletion-cover dynamics` follow by deleting the displayed endpoint from the two covers supplied by `the five-path endpoint-attachment theorem above`. The final alternatives are exactly `the exact-cover disagreement theorem in deletion-cover dynamics` and `the path restriction and intersection calculus`. ∎


---


Let `H` be a minimum-order counterexample and let
`W=(w_0,w_1,w_2,w_3,w_4)`
be any proper tight five-vertex path. Put `C=V(H)-V(W)`.
Choose arbitrary exact two-path covers
`F_0` of `H-w_0` and
`F_4` of `H-w_4`.

Then at least one of the following holds.

1. One of `F_0,F_4` has at least two ordinary edges between the surviving four vertices of `W` and `C`.

2. One endpoint-deletion cover has exactly one such crossing, but its unique four-vertex block on `W-{w_i}` orders those four vertices differently from the inherited order of `W). Comparing that block with the inherited tight four-path yields a reversed common ordered edge, a tight triple reversing an ordered edge, or a vertex-simple tight cycle.

3. Both endpoint-deletion covers have exactly one crossing and preserve the inherited four-vertex order. Then, after deleting both endpoints `w_0,w_4`, the induced exact two-covers of `H-{w_0,w_4}` are distinct. Hence either their support partitions cross, or a common support carries different Hamilton orders and therefore exposes a reversed common edge, reversing tight triple, or tight cycle.

Thus every proper tight five-path carries unavoidable support/order complexity at its two endpoint deletions; there is no featureless endpoint-deletion state.

## Proof

By `the five-path endpoint-attachment theorem above`, every endpoint-deletion cover has at least one crossing between the surviving four-set and `C`. If either has at least two, outcome 1 holds.

Assume an endpoint cover has exactly one crossing. The block-count conclusion of `the five-path endpoint-attachment theorem above` says the four surviving vertices of `W` form one Hamilton path block. If its order differs from the inherited order, apply the ordered-path intersection theorem `the path restriction and intersection calculus`; this is outcome 2.

The only remaining case is that both endpoint covers have one crossing and inherited order. The forced opposite attachment geometry is then `the five-path endpoint-attachment theorem above`, and `the opposite-attachment bridge-disagreement theorem above` gives outcome 3. ∎


---


Let `H` be a minimum-order counterexample to the two-cover conjecture, fix `x in V(H)`, and let
`H-x=P|Q`
be an exact two-path cover.

The omitted vertex `x` cannot be inserted into the displayed order of `P` at any position: such an insertion would produce a tight path on `V(P) union {x}`, which together with `Q` would be a spanning two-path cover of `H`. The same holds for `Q`.

By the endpoint-state theorem `the endpoint-state trichotomy in deletion-cover dynamics`, both components have order at least three. Therefore the local insertion-obstruction theorem `the insertion and endpoint-replacement calculus` applies separately to each component.

More explicitly, let
`R=(r_1,...,r_m)`
be either `P` or `Q`, define comparison-digraph vertices
`e_i={r_i,r_{i+1}}` for `1<=i<m`
and
`f_i={x,r_i}` for `1<=i<=m`.
Then for some `1<=t<m`, one of the following holds:

1. `2<=t<=m-1` and
   `f_t -> e_{t-1} -> e_t -> f_t`;

2. `e_t -> f_t` and `f_{t+1} -> f_t`, together with
   `e_{t-1} -> f_t` when `t>1`,
   `f_{t+1} -> e_{t+1}` when `t<m-1`,
   and `f_m -> e_{m-1}` when `t=m-1`.

Thus every arbitrary-length deletion state contains two bounded local obstruction windows, one on each component, each supported on `x` and at most four consecutive vertices of that component. The unresolved global step is no longer to understand arbitrary insertion failure along entire paths; it is to couple the two bounded obstruction windows so as to force a component reduction or defect-span compression.

## Proof

Noninsertability on each component follows immediately from `pc(H)>2`. The two local alternatives are exactly the conclusion of `the insertion and endpoint-replacement calculus` applied separately to `P` and `Q`. ∎


---

# First-type insertion obstructions are Hamiltonian four-windows or universal cyclic four-kernels

Let `H` be a minimum counterexample, let
`H-x=P|Q`
be an exact deletion two-cover, and write
`P=(p_0,...,p_m)`.

Suppose the local noninsertion obstruction supplied by `the insertion and endpoint-replacement calculus` on `P` is of its first type. Thus for some internal index `i`, with
`1<=i<=m-1`, putting
`a=p_{i-1}`, `b=p_i`, `c=p_{i+1}`, and `z=x`,
the comparison-cycle conclusion is exactly that

`(z,b,a)`, `(a,b,c)`, and `(c,b,z)`

are tight.

Put `X={a,b,c,z}`.

## Theorem

Exactly one of the following structural alternatives holds.

1. `H[X]` is Hamiltonian. Then `H-X` is non-Hamiltonian and, by minimality, has path-cover number exactly two.

2. `H[X]` is non-Hamiltonian. Then its boundary orientation is forced uniquely by the three displayed triples: after the labels above, its twelve tight reversal representatives are

`abc, bca, cab, zba, azb, baz, acz, cza, zac, zcb, bzc, cbz`.

Hence `X` is exactly the cyclic non-Hamiltonian four-vertex configuration of `the small-set structure module` Section 2. Consequently, for every vertex `d outside X`, the five-set `X union {d}` is Hamiltonian, with a Hamilton path in which `d` lies one position from an endpoint. For every such `d`, the complement `H-(X union {d})` is non-Hamiltonian and has path-cover number exactly two.

Thus a first-type insertion obstruction never remains a generic four-vertex local failure: it either exposes a Hamiltonian four-set with exact-two-cover complement, or a single rigid cyclic four-kernel whose every exterior one-vertex extension is Hamiltonian.

## Proof

The three first-type comparison arcs of `the insertion and endpoint-replacement calculus` are
`f_i -> e_{i-1} -> e_i -> f_i`.
Translating the comparison arcs back to tight triples gives exactly
`zba`, `abc`, `cbz`.

If `H[X]` is Hamiltonian, its complement cannot be Hamiltonian, since the two Hamilton paths would two-cover `H`. Minimality gives `pc(H-X)<=2`, hence `pc(H-X)=2`. This proves alternative 1.

Assume now that `H[X]` is non-Hamiltonian. We force the remaining reversal pairs using only the rule that a four-letter word cannot have both consecutive triples tight.

Starting from `zba,abc,cbz`:

- `abcz` forces `zcb`;
- `acbz` forces `bca`;
- `azcb` forces `cza`;
- `bcaz` forces `zac`;
- `bzac` forces `azb`;
- `czab` forces `baz`;
- `czba` forces `bzc`;
- `bzca` forces `acz`;
- `bacz` forces `cab`.

Together with the three initial triples, these are precisely
`abc,bca,cab,zba,azb,baz,acz,cza,zac,zcb,bzc,cbz`.
Therefore `X` is the exceptional cyclic non-Hamiltonian four-set of `the small-set structure module` Section 2.

That theorem says that adjoining any exterior vertex `d` makes `X union {d}` Hamiltonian, with `d` one position from an endpoint of some Hamilton path. Since `|V(H)|>10`, every such five-set is proper. Its complement cannot be Hamiltonian, or it and the five-path would two-cover `H`; minimality therefore gives path-cover number exactly two. ∎

# Cyclic first-type insertion kernels

Assume the non-Hamiltonian alternative of `the first-type insertion-kernel theorem above`. Thus
`X={a,b,c,x}`
is the exceptional cyclic four-kernel arising from a first-type insertion obstruction, and for every
`d in V(H)-X`
the five-set
`X union {d}`
is Hamiltonian.

Put
`K=H-X`.

## Theorem

The induced tournament `K` has path-cover number exactly two and is non-Hamiltonian. Moreover, for every vertex `d in V(K)`,

`pc(K-d)=2`

and `K-d` is non-Hamiltonian.

Consequently every exact two-path cover of `K` has both components nontrivial.

Thus the exceptional cyclic first-type branch leaves behind a deletion-stable pc-two obstruction: neither the complement itself nor any one-vertex deletion of it is Hamiltonian.

## Proof

Because `K` is a proper induced subgraph of the minimum counterexample `H`, minimality gives
`pc(K)<=2`.

Suppose first that `K` were Hamiltonian. Let
`R=(r_0,...,r_t)`
be a Hamilton path of `K`, and choose the endpoint `d=r_0`. Then
`R-d=(r_1,...,r_t)`
is a Hamilton path of `K-d`.

By the universal extension conclusion of `the first-type insertion-kernel theorem above`, the five-set
`X union {d}`
is Hamiltonian. It is disjoint from `K-d`, and together the two sets partition `V(H)`. Hence a Hamilton path on `X union {d}` together with `R-d` would be a spanning two-path cover of `H`, contradiction.

Therefore `K` is non-Hamiltonian. Since `pc(K)<=2`, we have `pc(K)=2`.

Now fix arbitrary `d in V(K)`. Again `X union {d}` is Hamiltonian. If `K-d` were Hamiltonian, those two disjoint Hamilton paths would two-cover `H`. Hence `K-d` is non-Hamiltonian. Since `K-d` is also a proper induced subgraph of `H`, minimality gives `pc(K-d)<=2`, and therefore `pc(K-d)=2`.

Finally, if an exact two-cover of `K` had a singleton component `(d)`, its other component would be a Hamilton path of `K-d`, contradicting the preceding paragraph. Thus both components of every exact two-cover of `K` are nontrivial. ∎

# Pivot-pivot cross-swap kernel


Let `H` be a minimum-order counterexample and let
`H-x=P|Q`
be an exact two-path cover, where
`P=(p_0,...,p_m)` and `Q=(q_0,...,q_s)`.

Assume the bounded insertion obstruction of `the bounded insertion-obstruction theorem earlier in this module` is of the second type on both components at interior gaps
`p_i|p_{i+1}` and `q_j|q_{j+1}`,
with
`1<=i<=m-2` and `1<=j<=s-2`.
Then the pivot pattern implies that
`(p_0,...,p_i,x)`, `(x,p_{i+1},...,p_m)`,
`(q_0,...,q_j,x)`, and `(x,q_{j+1},...,q_s)`
are tight paths, while insertion of `x` across either displayed gap fails.

Put
`P_L=(p_0,...,p_i)`, `P_R=(p_{i+1},...,p_m)`,
`Q_L=(q_0,...,q_j)`, `Q_R=(q_{j+1},...,q_s)`.

Consider the two cross-swaps.

First,
`(P_L,x,Q_R) | (Q_L,P_R)`
would be a spanning two-path cover if all three triples
`(p_i,x,q_{j+1})`,
`(q_{j-1},q_j,p_{i+1})`,
`(q_j,p_{i+1},p_{i+2})`
were tight.
Since `pc(H)>2`, at least one is non-tight. Hence at least one of
`(q_{j+1},x,p_i)`,
`(p_{i+1},q_j,q_{j-1})`,
`(p_{i+2},p_{i+1},q_j)`
is tight.

Second,
`(Q_L,x,P_R) | (P_L,Q_R)`
would be a spanning two-path cover if all three triples
`(q_j,x,p_{i+1})`,
`(p_{i-1},p_i,q_{j+1})`,
`(p_i,q_{j+1},q_{j+2})`
were tight.
Therefore at least one of
`(p_{i+1},x,q_j)`,
`(q_{j+1},p_i,p_{i-1})`,
`(q_{j+2},q_{j+1},p_i)`
is tight.

Thus the interior pivot-pivot branch is governed by two explicit three-way clauses, all supported on
`{x,p_{i-1},p_i,p_{i+1},p_{i+2},q_{j-1},q_j,q_{j+1},q_{j+2}}`.
The arbitrary lengths of `P,Q` disappear from this residual cross-swap obstruction.

## Proof

The pivot conclusions are the second local pattern in `the insertion and endpoint-replacement calculus`, as imported by `the bounded insertion-obstruction theorem earlier in this module`. Each proposed cross-swap preserves all internal triples of the four path pieces. The three displayed triples are exactly the new consecutive triples required at its joins. If all three were tight, that cross-swap would give a spanning two-path cover, impossible. Boundary antisymmetry converts a failed triple into its displayed tight reverse. ∎


# Central five-set closure for viable pivot joins

Let `H-x=P|Q` be an exact deletion two-cover in a minimum counterexample, and suppose the bounded insertion obstructions on both components are second-type interior pivots at gaps
`p_i|p_{i+1}` and `q_j|q_{j+1}`
as in `the pivot-pivot cross-swap theorem above`.

Put
`W={x,p_i,p_{i+1},q_j,q_{j+1}}`.

Because insertion of `x` across each pivot gap fails, boundary antisymmetry gives
`(p_{i+1},x,p_i)` and `(q_{j+1},x,q_j)` tight.

If both cross-join triples
`(p_i,x,q_{j+1})` and `(q_j,x,p_{i+1})`
are tight, then `H[W]` is Hamiltonian. Consequently `H-W` is non-Hamiltonian and, by minimality, has path-cover number exactly two.

Equivalently, outside the five-complement frontier at least one of
`(q_{j+1},x,p_i)`, `(p_{i+1},x,q_j)`
is tight.

## Proof

Assume both displayed cross-join triples are tight. If `H[W]` were non-Hamiltonian, the five-vertex theorem `the small-set structure module` Section 3 would give an edge order representing `H[W]`.

Write the four ordinary edges incident with `x` as
`A=xp_{i+1}`, `a=xp_i`, `B=xq_{j+1}`, `b=xq_j`.
The four tight triples give the strict inequalities
`A<a`, `B<b`, `a<B`, `b<A`.
Thus
`A<a<B<b<A`,
a contradiction to transitivity of a strict edge order. Therefore `H[W]` is Hamiltonian.

Since a minimum counterexample has order greater than ten, `W` is proper. If `H-W` were Hamiltonian, Hamilton paths on `W` and `H-W` would two-cover `H`, impossible. Minimality then gives `pc(H-W)=2`.

The final formulation follows by boundary antisymmetry: if neither reverse cross-join were tight, both forward cross-joins would be tight and the preceding argument would put the state in the five-complement frontier. ∎

# Cyclic four-kernel exterior forcing

Assume the exceptional cyclic four-kernel
`X={a,b,c,z}`
from `the cyclic four-kernel theorem earlier in this module`. Thus one tight representative from each reversal pair on `X` is

`abc, bca, cab,`
`zba, azb, baz,`
`acz, cza, zac,`
`zcb, bzc, cbz`.

Let `u in X`, and let `d,e` be any two distinct vertices outside `X`.

## Theorem

The five-set
[
(X-{u})cup{d,e}
]
is Hamiltonian.

Consequently, in a minimum counterexample `H` containing this cyclic kernel, with `K=H-X`, for every
`u in X`
and every distinct
`d,e in V(K)`,
the complementary induced tournament
[
H[(K-{d,e})cup{u}]
]
is non-Hamiltonian and has path-cover number exactly two.

Equivalently, all four exchange graphs `G_u` defined in `the exchange-density theorem below` are complete graphs. The earlier two-of-four exchange-density conclusion strengthens to four-of-four.

## Proof

Every three-vertex subset of `X` carries a directed 3-cycle in the comparison digraph.

Indeed, for the four possible triples:

- on `{a,b,c}`, the tight triples `abc,bca,cab` give
  `ab -> bc -> ca -> ab`;
- on `{a,b,z}`, the tight triples `baz,azb,zba` give
  `ab -> az -> bz -> ab`;
- on `{a,c,z}`, the tight triples `acz,cza,zac` give
  `ac -> cz -> az -> ac`;
- on `{b,c,z}`, the tight triples `cbz,bzc,zcb` give
  `bc -> bz -> cz -> bc`.

Fix `uin X` and put
`T=X-{u}`.
Thus the comparison digraph of `H[T]` is cyclic.

Now consider
`F=T union {d,e}`.
If `H[F]` were non-Hamiltonian, the non-Hamiltonian-five-set theorem `the small-order structure theorem` would make its entire comparison digraph acyclic. But the restriction of that comparison digraph to the ordinary edges of `T` already contains the directed 3-cycle above. Contradiction.

Hence `F` is Hamiltonian for every choice of `u,d,e`.

In a minimum counterexample, the complement of such a proper Hamiltonian five-set cannot itself be Hamiltonian, or the two Hamilton paths would form a spanning two-cover. Minimality therefore makes the complement non-Hamiltonian of path-cover number exactly two. ∎

# Two-for-one exchange density from a universal cyclic kernel

Assume the cyclic first-type insertion-kernel setup of `the cyclic four-kernel theorem earlier in this module` and `the cyclic first-type deletion-stability theorem above`. Thus `X` is the exceptional non-Hamiltonian cyclic four-set in a minimum counterexample `H`, every five-set `X union {d}` with `d outside X` is Hamiltonian, and with
`K=H-X`
we have `pc(K)=2` while `K` and every `K-d` are non-Hamiltonian.

For each `u in X`, define a graph `G_u` on `V(K)` by joining distinct `d,e` exactly when
`H[(X-{u}) union {d,e}]`
is Hamiltonian.

## Theorem

Every pair `{d,e} subseteq V(K)` belongs to at least two of the four graphs `G_u`.

For every incidence
`de in E(G_u)`,
the complementary induced tournament
`H[(K-{d,e}) union {u}]`
is non-Hamiltonian and has path-cover number exactly two.

Consequently
[
sum_{uin X} e(G_u)ge 2inom{|K|}{2},
]
so some kernel vertex `u` satisfies
[
e(G_u)ge rac12inom{|K|}{2}.
]
Likewise, for every fixed exterior vertex `d`,
[
sum_{uin X}deg_{G_u}(d)ge2(|K|-1),
]
so some `uin X` has
[
deg_{G_u}(d)ge leftlceilrac{|K|-1}{2}ightceil.
]

Thus the exceptional cyclic insertion branch carries a dense synchronized exchange system: every exterior pair can replace at least two different kernel vertices while preserving a Hamiltonian five-side and a non-Hamiltonian exact-two-cover complement.

## Proof

Fix distinct `d,e in V(K)` and consider the six-set
`S=X union {d,e}`.

By the universal-extension property of the cyclic kernel, both
`S-d=X union {e}`
and
`S-e=X union {d}`
are Hamiltonian.

The four-of-six theorem says that at least four of the six vertex deletions of `S` are Hamiltonian. Two are already accounted for by deleting `d` and `e`. Hence for at least two distinct vertices `u in X`, the deletion
`S-u=(X-{u}) union {d,e}`
is Hamiltonian. Equivalently, `de` belongs to at least two of the graphs `G_u`.

Now fix such a triple `u,d,e`. The complement in `H` of the Hamiltonian five-set `(X-{u}) union {d,e}` is exactly
`(K-{d,e}) union {u}`.
If that complement were Hamiltonian, its Hamilton path together with one on the five-set would give a spanning two-path cover of `H`, impossible. Since it is a proper induced subgraph of the minimum counterexample, minimality gives path-cover number at most two; non-Hamiltonicity makes it exactly two.

Summing the pair multiplicities over all `{d,e}` gives the edge-count inequality. Summing only the pairs incident with a fixed `d` gives the degree inequality. The pigeonhole conclusions follow immediately. ∎
