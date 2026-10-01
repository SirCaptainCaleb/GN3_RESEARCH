# Codimension-five endpoint normalization

## Statement

For a Hamiltonian side with a non-Hamiltonian five-vertex complement, at least four complement deletions stabilize exact two-covers; inherited-order endpoint attachments normalize to singletons, and endpoint analysis reduces to multiple crossings, order disagreement, or a successful-exchange path with non-Hamiltonian five-vertex complement.

## Body

# Codimension-five endpoint and deletion-family structure

Let `K` be a boundary tournament with `pc(K)>2`. Let `Y⊂V(K)` induce a Hamiltonian boundary tournament, put `F=V(K)-Y`, and assume `|F|=5` and that `K[F]` is non-Hamiltonian. Define
`G={g∈F: K[F-{g}] is Hamiltonian}`.

Then `|G|>=4`. For every `g∈G`, `K[Y∪{g}]` is non-Hamiltonian and, for any Hamilton paths `Q` on `Y` and `A_g` on `F-{g}`, the pair `Q|A_g` is an exact two-path cover of `K-g`.

Moreover, if `Q=(q_0,...,q_k)` with `k>=1`, then for every `g∈G` the triples
`(q_1,q_0,g)` and `(g,q_k,q_{k-1})`
are tight. Thus the same set `G` of at least four vertices satisfies these two endpoint conclusions simultaneously for every Hamilton ordering of `K[Y]`.

## Proof

Since `K[F]` is a non-Hamiltonian five-vertex boundary tournament, `the small-order structure module` Section 7 gives at most one vertex `g∈F` for which `K[F-{g}]` is non-Hamiltonian. Hence `|G|>=4`.

Fix `g∈G`. If `K[Y∪{g}]` were Hamiltonian, Hamilton paths on the complementary vertex sets `Y∪{g}` and `F-{g}` would form a spanning two-path cover of `K`, contrary to `pc(K)>2`. Thus `K[Y∪{g}]` is non-Hamiltonian.

Choose arbitrary Hamilton paths `Q` on `Y` and `A_g` on `F-{g}`. Their supports are disjoint and partition `V(K)-{g}`, so `Q|A_g` is a two-path cover of `K-g`. It is exact: if `K-g` were Hamiltonian, a Hamilton path on `K-g` together with the singleton `(g)` would two-cover `K`.

Write `Q=(q_0,...,q_k)`, `k>=1`. If `(g,q_0,q_1)` were tight, prepending `g` would give a Hamilton path `(g,Q)` on `Y∪{g}`, contradiction. Therefore `(g,q_0,q_1)` is non-tight and boundary antisymmetry gives `(q_1,q_0,g)` tight. Dually, if `(q_{k-1},q_k,g)` were tight, appending `g` would Hamiltonize `Y∪{g}`; hence its reverse `(g,q_k,q_{k-1})` is tight. The argument used no special property of the chosen Hamilton order `Q`, so it holds for every Hamilton ordering of `K[Y]`. ∎

# Singleton normalization

Let `K` be a boundary tournament with vertex partition
`V(K)=Y disjoint-union F`,
where `Q=(y_0,...,y_k)`, `k>=2`, is a Hamilton tight path of `K[Y]` and `|F|=5`.

For `g in F`, suppose `K[F-{g}]` is Hamiltonian.

1. If `(g,y_1,y_2)` is tight, then for every Hamilton tight path `A_g` of `K[F-{g}]`,
   `(g,y_1,...,y_k) | A_g`
   is an exact two-path cover of `K-y_0` with exactly one ordinary edge joining `Y` to `F`.
2. If `(y_{k-2},y_{k-1},g)` is tight, then
   `A_g | (y_0,...,y_{k-1},g)`
   is an exact two-path cover of `K-y_k` with exactly one ordinary edge joining `Y` to `F`.

## Proof

For the first assertion, the only consecutive triple of `(g,y_1,...,y_k)` not inherited from `Q` is `(g,y_1,y_2)`, which is tight by hypothesis. Thus this is a tight path. Its support is `{g} union (Y-{y_0})`, while `A_g` covers exactly `F-{g}`; the two supports are disjoint and partition `V(K)-{y_0}`. The mixed path has exactly one ordinary edge joining `F` to `Y`, namely `{g,y_1}`. This proves the first assertion. The second is symmetric. ∎

## Consequence in a minimum five-complement counterexample

Assume now that `K` is a minimum-order counterexample to the statement that every boundary tournament admitting a partition
`V(K)=Y disjoint-union F`,
with `|F|=5` and `K[Y]` Hamiltonian, has path-cover number at most two. Keep the fixed Hamilton path
`Q=(y_0,...,y_k)`
on `Y`, and define
`G={g in F : K[F-{g}] is Hamiltonian}`.

Then `K[F]` is non-Hamiltonian, since otherwise a Hamilton path on `F` together with `Q` would be a spanning two-path cover of `K`. The stabilized five-complement deletion lemma therefore gives
`|G|>=4`.
Thus at most one vertex of `F` lies outside `G`.

Suppose an exact two-path cover of `K-y_0` has a mixed component
`(U,y_1,...,y_k)`,
where `U` is a nonempty tight path on vertices of `F`, and let `ell` be the terminal vertex of `U`. Tightness of this component gives
`(ell,y_1,y_2)`.
If `ell in G`, the first part above replaces this cover by an exact two-path cover
`(ell,y_1,...,y_k)|A_ell`
for any Hamilton path `A_ell` on `F-{ell}`. If `ell notin G`, then `ell` is the unique possible vertex of `F` whose deletion is non-Hamiltonian.

Dually, suppose an exact two-path cover of `K-y_k` has a mixed component
`(y_0,...,y_{k-1},V)`,
where `V` is a nonempty tight path on vertices of `F`, and let `r` be the initial vertex of `V`. If `r in G`, the second part replaces this cover by
`A_r|(y_0,...,y_{k-1},r)`;
otherwise `r` is the same unique possible vertex outside `G`. ∎

# Initial endpoint-cover reduction

# Initial endpoint covers reduce to crossing multiplicity, order disagreement, or singleton attachment

Let `K` be a minimum-order counterexample to the statement that every boundary tournament admitting a partition
`V(K)=Y disjoint-union F`,
with `|F|=5` and `K[Y]` Hamiltonian, has path-cover number at most two. Fix a Hamilton tight path
`Q=(y_0,...,y_k)`, `k>=2`,
of `K[Y]`. Put
`Q_L=(y_1,...,y_k)`
and
`Q_R=(y_0,...,y_{k-1})`.

Choose exact two-path covers `C_L` of `K-y_0` and `C_R` of `K-y_k`.

For each of `C_L,C_R`, at least one of the following occurs:

1. the cover has at least two ordinary edges between its surviving vertices of `Y` and `F`;
2. the cover has exactly one such edge, and after cutting it the Hamilton path on the surviving vertices of `Y` has an order different from `Q_L` or `Q_R`; consequently the two Hamilton paths on that common support expose a reversed common ordered edge, a tight triple reversing an ordered edge at an intersection, or a vertex-simple tight cycle;
3. the cover has exactly one such edge and the path on the surviving vertices of `Y` has the inherited order. Then the vertex `s in F` adjacent to that path satisfies `K[F-{s}]` Hamiltonian, so the cover can be replaced by one in which only `s` from `F` lies on the mixed component. In that replacement, `y_1` is internal on the left and `y_{k-1}` is internal on the right.

If both endpoint covers satisfy alternative 3 and `k>=3`, put
`M=(y_1,...,y_{k-1})`
and let `ell,r in F` be their singleton attachment vertices. If `ell!=r`, then `(ell,M,r)` is tight and its complementary five-set is non-Hamiltonian. If `ell=r=s`, then both `(s,M)` and `(M,s)` are tight, so either their common cyclic ordering is a tight cycle or `(y_1,s,y_{k-1})` is tight.

## Proof

Consider `C_L`. It cannot have zero ordinary edges between `Q_L` and `F`: otherwise its two components would lie separately in the nonempty sets `Y-{y_0}` and `F`, forcing one component to be a Hamilton path on `F`; then that path together with `Q` would two-cover `K`. If it has at least two such edges, alternative 1 holds.

Suppose it has exactly one. The one-transition orientation-rigidity theorem says that cutting the unique crossing gives one Hamilton path on the full support of `Q_L` and two nonempty paths partitioning `F`. If that Hamilton path has a different order from `Q_L`, alternative 2 follows from the reversed-order common-vertex lemma.

If it has the inherited order, the mixed component has the form
`(U,Q_L)`
for a nonempty tight path `U` on vertices of `F`. Let `s` be the terminal vertex of `U`. The bad-four-deletion exclusion theorem gives `K[F-{s}]` Hamiltonian, and singleton replacement gives
`(s,Q_L)|A_s`
for a Hamilton path `A_s` on `F-{s}`. Since `k>=2`, the vertex `y_1` lies between `s` and `y_2), so it is internal. This proves alternative 3 on the left.

The right-hand argument is symmetric and makes `y_{k-1}` internal in the singleton-replaced mixed component.

Now suppose both sides satisfy alternative 3 and `k>=3`. We have tight paths
`(ell,M,y_k)`
and
`(y_0,M,r)`,
and the original Hamilton path contains `(y_0,M,y_k)`. If `ell!=r`, common-middle rectangle closure gives `(ell,M,r)` tight. Its complement has five vertices; if that complement were Hamiltonian, it and `(ell,M,r)` would form a spanning two-path cover of `K`, impossible.

If `ell=r=s`, choose the same Hamilton path on `F-{s}` in both singleton replacements. Deleting `y_k` from the left cover and `y_0` from the right leaves the tight paths `(s,M)` and `(M,s)`. Because `|M|>=2`, the opposite-concatenations lemma gives the stated cycle-or-triple alternative. ∎

# Two-end attachment dichotomy

Let `K` be a minimum-order counterexample to the statement that every boundary tournament admitting a partition
`V(K)=Y disjoint-union F`,
with `|F|=5` and `K[Y]` Hamiltonian, has path-cover number at most two. Fix a Hamilton tight path
`Q=(y_0,...,y_k)`, `k>=2`,
of `K[Y]`, and put
`M=(y_1,...,y_{k-1})`.

Suppose an exact two-path cover of `K-y_0` has mixed component
`(U,y_1,...,y_k)`
for a nonempty tight path `U` in `F`, and let `ell` be the terminal vertex of `U`.

Suppose an exact two-path cover of `K-y_k` has mixed component
`(y_0,...,y_{k-1},V)`
for a nonempty tight path `V` in `F`, and let `r` be the initial vertex of `V`.

Then exactly one of the following holds.

1. `ell!=r). Then `(ell,M,r)` is a tight path, and its complementary five-set
   `(F-{ell,r}) union {y_0,y_k}`
   is non-Hamiltonian.
2. `ell=r=s` and `K[F-{s}]` is Hamiltonian. Then both endpoint covers can be replaced using the same Hamilton path `A` on `F-{s}` by
   `(s,y_1,...,y_k)|A`
   and
   `A|(y_0,...,y_{k-1},s)`.
   If `k>=3`, then both `(s,M)` and `(M,s)` are tight, so either their common cyclic ordering is a tight cycle or `(y_1,s,y_{k-1})` is tight.
3. `ell=r=s` and `K[F-{s}]` is non-Hamiltonian. Then every `g in F-{s}` has `K[F-{g}]` Hamiltonian.

## Proof

The left mixed component contains the tight subpath
`(ell,M,y_k)`.
The right mixed component contains the tight subpath
`(y_0,M,r)`.
The original Hamilton path contains
`(y_0,M,y_k)`.

Assume first `ell!=r`. The four endpoints `y_0,ell,y_k,r` are distinct and lie outside `M`. Applying common-middle rectangle closure to `(ell,M,y_k)` and `(y_0,M,r)` gives `(ell,M,r)` tight. If its complementary five-set were Hamiltonian, a Hamilton path on that complement together with `(ell,M,r)` would be a spanning two-path cover of `K`, contradicting `pc(K)>2`. This proves 1.

Now suppose `ell=r=s` and `K[F-{s}]` is Hamiltonian. The two displayed mixed components give attachment triples
`(s,y_1,y_2)`
and
`(y_{k-2},y_{k-1},s)`.
Singleton replacement at both ends, using one Hamilton path `A` of `K[F-{s}]`, gives the two displayed covers. Deleting `y_k` from the first and `y_0` from the second leaves mixed paths `(s,M)` and `(M,s)`. When `k>=3`, `M` has order at least two, so the opposite-concatenations lemma gives the stated cycle-or-triple alternative. This proves 2.

Finally suppose `ell=r=s` and `K[F-{s}]` is non-Hamiltonian. Also `K[F]` is non-Hamiltonian, or else a Hamilton path on `F` together with `Q` would two-cover `K`. The stabilized five-complement deletion-family theorem therefore gives at least four vertices `g in F` for which `K[F-{g}]` is Hamiltonian. Since `s` is not one of them and `|F|=5`, every vertex of `F-{s}` is. ∎

# Common-attachment endpoint-swap orbit

# Swapping a common singleton attachment with a Hamilton-side endpoint

Let `K` be a minimum-order counterexample to the statement that every boundary tournament admitting a partition
`V(K)=Y disjoint-union F`,
with `|F|=5` and `K[Y]` Hamiltonian, has path-cover number at most two. Fix a Hamilton tight path
`Q=(y_0,...,y_k)`, `k>=3`,
of `K[Y]`, and put
`M=(y_1,...,y_{k-1})`.

Assume there is `s in F` and exact two-path covers
`(s,y_1,...,y_k)|A`
of `K-y_0` and
`B|(y_0,...,y_{k-1},s)`
of `K-y_k`, where `A,B` are Hamilton paths on `F-{s}`.

Define two new partitions
`Y_L=(Y-{y_0}) union {s}`, `F_L=(F-{s}) union {y_0}`,
and
`Y_R=(Y-{y_k}) union {s}`, `F_R=(F-{s}) union {y_k}`.

Then:

1. `K[Y_L]` is Hamiltonian in the order `(s,y_1,...,y_k)`, while `K[F_L]` is non-Hamiltonian;
2. `K[Y_R]` is Hamiltonian in the order `(y_0,...,y_{k-1},s)`, while `K[F_R]` is non-Hamiltonian;
3. relative to `(Y_L,F_L)`, the exact cover
   `(y_0,y_1,...,y_k)|A`
   of `K-s` has exactly one `Y_L-F_L` edge and, after cutting it, the path on `Y_L-{s}` has the inherited order `(y_1,...,y_k)`; whereas the exact cover
   `B|(y_0,M,s)`
   of `K-y_k` has exactly one `Y_L-F_L` edge but its path on `Y_L-{y_k}` is `(M,s)`, not the inherited order `(s,M)`;
4. the symmetric conclusions hold relative to `(Y_R,F_R)`.

## Proof

The two original endpoint covers show immediately that
`(s,y_1,...,y_k)`
and
`(y_0,...,y_{k-1},s)`
are tight Hamilton paths, proving Hamiltonicity of `Y_L` and `Y_R`.

If `F_L=(F-{s}) union {y_0}` were Hamiltonian, a Hamilton path on `F_L` together with `(s,y_1,...,y_k)` would two-cover `K`, impossible. Thus `F_L` is non-Hamiltonian. The proof for `F_R` is symmetric.

Choose a Hamilton path `A` on `F-{s}`. Relative to `(Y_L,F_L)`, deleting `s` leaves the Hamilton-side support `Y_L-{s}={y_1,...,y_k}`. The exact cover
`(y_0,y_1,...,y_k)|A`
of `K-s` has exactly one edge between `F_L` and `Y_L-{s}`, namely `y_0y_1`, and the resulting path on the surviving Hamilton-side support has the inherited order `(y_1,...,y_k)`.

At the opposite endpoint `y_k`, the original right cover is
`B|(y_0,M,s)`.
Relative to `(Y_L,F_L)`, `y_0` belongs to `F_L`, while `M union {s}` is the surviving Hamilton-side support. There is exactly one crossing edge, `y_0y_1`, and the path on the Hamilton-side support is `(M,s)`. The inherited order on that support is `(s,M)`, so the two orders differ.

The right-swapped statement is the exact mirror image. ∎

# Final endpoint normalization

Let `K` be a minimum-order counterexample to the statement that every boundary tournament admitting a partition
`V(K)=Y disjoint-union F`,
with `|F|=5` and `K[Y]` Hamiltonian, has path-cover number at most two. Fix a Hamilton tight path
`Q=(y_0,...,y_k)`, `k>=3`,
of `K[Y]`.

Then at least one of the following holds.

1. An exact two-path cover of `K-y_0` or `K-y_k` has at least two ordinary edges between its surviving vertices of `Y` and `F`.
2. For the original partition, or for a partition obtained by replacing one endpoint of `Y` by a common singleton attachment vertex `s in F`, there is an endpoint-deletion exact two-path cover with exactly one edge between the two parts whose path on the surviving Hamiltonian-side support has a vertex order different from the inherited Hamilton order. Consequently two Hamilton paths on a common support expose a reversed common ordered edge, a tight triple reversing an ordered edge at an intersection, or a vertex-simple tight cycle.
3. There are distinct `ell,r in F` such that
   `(ell,y_1,...,y_{k-1},r)`
   is tight and its complementary five-set is non-Hamiltonian.

## Proof

Apply the initial endpoint-cover reduction to exact two-path covers of `K-y_0` and `K-y_k`. For either endpoint, every exact cover satisfies one of three alternatives: at least two edges cross between the surviving Hamiltonian-side support and `F`; exactly one crosses and the Hamilton-side order differs from the inherited order; or exactly one crosses with inherited order and the cover can be replaced by one having a single attachment vertex from `F`.

If the first or second alternative occurs on either side, conclusion 1 or 2 follows.

Assume therefore that both endpoint covers have singleton replacements. Write their attachment vertices as `ell` on the left and `r` on the right. Thus there are exact covers
`(ell,y_1,...,y_k)|A_L`
of `K-y_0` and
`A_R|(y_0,...,y_{k-1},r)`
of `K-y_k`,
where `A_L` is Hamiltonian on `F-{ell}` and `A_R` is Hamiltonian on `F-{r}`.

If `ell!=r`, the initial endpoint-cover reduction gives
`(ell,y_1,...,y_{k-1},r)`
tight with non-Hamiltonian complementary five-set. This is conclusion 3.

It remains that `ell=r=s`. Apply the endpoint-swap theorem. Replacing `y_0` by `s` in the Hamiltonian side produces another partition with Hamiltonian first part and non-Hamiltonian five-vertex complement. Relative to that partition, deleting the opposite endpoint `y_k` gives an exact two-path cover with exactly one crossing, but the path on the surviving Hamiltonian-side support is
`(y_1,...,y_{k-1},s)`
rather than the inherited order
`(s,y_1,...,y_{k-1})`.
Thus conclusion 2 holds. ∎
