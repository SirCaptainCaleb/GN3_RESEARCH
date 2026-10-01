# Deletion-cover dynamics

## Statement

Deletion-cover transition calculus: compatibility, crossing/order disagreement, endpoint restoration, omission swaps, cycle/wrap structure, the order-four double-clean obstruction, its sharp order-five failure, and the stabilized six-set deletion family forced by a double-clean five-component.

## Body

# Deletion-cover dynamics

# Disagreement between two exact two-path covers

Let `H` be a boundary tournament on a finite vertex set `W`, and let
`C=P|Q`
and
`C'=P'|Q'`
be exact two-path covers of `H`.

Then one of the following holds.

1. The unordered support partitions
   `{V(P),V(Q)}`
   and
   `{V(P'),V(Q')}`
   are different. In this case some ordinary edge of `C'` has endpoints in different components of `C`, and some ordinary edge of `C` has endpoints in different components of `C'`.
2. The unordered support partitions are equal. After swapping component names if necessary, `V(P)=V(P')` and `V(Q)=V(Q')`. If the corresponding ordered paths are not identical, then on at least one common support the two Hamilton paths have different relative orders. Hence the relative-order theorem in the path-intersection calculus gives at least one of:
   - an ordered edge of one path that is the reverse of an ordered edge of the other;
   - a tight triple on that support that reverses an ordered edge of one of the paths at an intersection;
   - a vertex-simple tight cycle on that support.

Thus two genuinely different exact two-path covers of the same vertex set expose either a component-partition crossing or an order-disagreement witness inside a common component.

## Proof

Suppose first that the support partitions differ. Then some component of `C'`, say `P'`, meets both `V(P)` and `V(Q)`; otherwise each component of `C'` would be contained in one part of the two-part partition `V(P)|V(Q)`, forcing the two unordered support partitions to agree. Since `P'` is an ordinary connected path and its vertices are not contained in one part of `V(P)|V(Q)`, some consecutive ordinary edge of `P'` has one endpoint in each part. This is an ordinary crossing edge of `C'` relative to `C`. By symmetry, some ordinary edge of `C` crosses the support partition of `C'`.

Now suppose the support partitions agree. Relabel so that `V(P)=V(P')` and `V(Q)=V(Q')`. If both corresponding ordered paths are identical, then the two covers are identical up to swapping component names. Otherwise, on at least one common support, say `V(P)`, the vertex sequences `P` and `P'` are distinct. Since both sequences contain every vertex of the common support exactly once, distinct sequences do not give the same relative order on all common vertices. Applying the relative-order theorem in the path-intersection calculus to `P,P'` gives the listed alternatives. ∎

---

# Two-deletion endpoint trichotomy

Let `K` be a boundary tournament with `pc(K)>2`, let `u,v` be distinct vertices, let `C_u` be an exact two-path cover of `K-u`, let `C_v` be an exact two-path cover of `K-v`, and let `T` be an exact two-path cover of `K-{u,v}`.

Then at least one of the following holds.

1. `v` is internal in its component of `C_u`. Deleting `v` from `C_u` leaves three nonempty tight path supports, and some ordinary edge of `T` crosses that three-part partition.
2. `u` is internal in its component of `C_v`. Deleting `u` from `C_v` leaves three nonempty tight path supports, and some ordinary edge of `T` crosses that three-part partition.
3. Both `v` in `C_u` and `u` in `C_v` are endpoints. Deleting them gives exact two-path covers
   `T_u=C_u-v`
   and
   `T_v=C_v-u`
   of `K-{u,v}`.

In the third case, if `T_u=T_v` as ordered two-path covers, then every exact two-path cover of `K-v` obtained by adjoining `u` to one end of one component of this common cover, and every analogous cover of `K-u` obtained by adjoining `v`, uses the same end of the same component. The common component has order at least two.

## Proof

Apply the deleted-vertex endpoint/crossing dichotomy to `C_u`, with deleted vertex `u` and second vertex `v`, comparing against `T`. Since the component of `C_u` containing `v` is nontrivial, either `v` is internal, yielding alternative 1, or it is an endpoint and deleting it gives the exact two-path cover `T_u`.

Apply the same argument symmetrically to `C_v`. Either alternative 2 holds, or deleting endpoint `u` gives the exact two-path cover `T_v`.

If neither 1 nor 2 holds, alternative 3 follows. When additionally `T_u=T_v`, the common two-path cover admits endpoint extensions by both `u` and `v`. The common endpoint-extension lemma below therefore implies that all such extensions use the same end of the same component and that this component has order at least two. ∎

---

# Opposite concatenations: cycle-or-wrap dichotomy

Let `H` be a boundary tournament. Let
`U=(u_1,...,u_r)`, `r>=1`,
and
`M=(m_1,...,m_h)`, `h>=2`,
be vertex-disjoint tight paths. Assume both concatenations
`UM=(u_1,...,u_r,m_1,...,m_h)`
and
`MU=(m_1,...,m_h,u_1,...,u_r)`
are tight paths.

Then:

1. if `r>=2`, the cyclic ordering `UM` is a tight cycle;
2. if `r=1`, writing `U=(u)`, exactly one of the following holds:
   - the cyclic ordering `(u,m_1,...,m_h)` is a tight cycle;
   - `(m_1,u,m_h)` is tight.

## Proof

All consecutive triples lying wholly inside `U` or wholly inside `M` are tight.

Assume first `r>=2`. Tightness of `UM` supplies the two cyclic junction triples at the `U|M` boundary, namely `(u_{r-1},u_r,m_1)` and `(u_r,m_1,m_2)`. Tightness of `MU` supplies the two cyclic junction triples at the `M|U` boundary, namely `(m_{h-1},m_h,u_1)` and `(m_h,u_1,u_2)`. These, together with the internal triples of `U` and `M`, are exactly all cyclic consecutive triples of the cyclic ordering `UM`. Hence it is a tight cycle.

Now let `r=1` and write `U=(u)`. Tightness of `UM` supplies `(u,m_1,m_2)`, and tightness of `MU` supplies `(m_{h-1},m_h,u)`. Every cyclic triple of `(u,m_1,...,m_h)` is therefore tight except possibly `(m_h,u,m_1)`. If that triple is tight, the cyclic ordering is a tight cycle. If it is not tight, boundary antisymmetry gives its reverse `(m_1,u,m_h)` tight. The alternatives are exclusive. ∎

---

# Common endpoint-extension lemma


Let K be a boundary tournament with pc(K)>2, let u,v be distinct, and let
T=A|B
be an exact two-cover of K-{u,v}. Suppose an exact cover of K-v is obtained by adjoining u to an endpoint of one component of T, and an exact cover of K-u is obtained by adjoining v to an endpoint of one component of T.

Then the two extensions use the same end of the same component, and that component has order at least two.

## Proof

If u and v extend different components, take the u-extended component from the first cover and the v-extended component from the second. They are disjoint tight paths covering K, contradiction.

If they extend opposite ends of the same component, adjoin both simultaneously. The two new endpoint junctions are inherited independently from the two given covers, so the doubly extended component is tight; with the untouched other component it two-covers K, contradiction.

Thus both extensions use the same end of the same component. If that component were a singleton (w), then exactly one of (u,w,v) and (v,w,u) is tight by boundary antisymmetry. That three-path together with the other component of T would two-cover K, contradiction. Hence the common component has order at least two. ∎


---

# Curated current package

The current bottleneck is no longer finding disagreement; it is transporting and consuming it. This package gathers the exact legacy endpoint/crossing lemmas that form the input side of that bridge. Exact source proofs follow verbatim. Because the package is a new synthesis, it is pending audit.


---

Internal deletion covers localize to crossings or same-slot replacement

# Internal deletion covers: crossing, order disagreement, or same-slot replacement

Let `H` be a minimum counterexample and let `H-x=P|Q` be an exact two-path cover, with
`P=(p_0,...,p_m)`.
Fix an internal vertex `y=p_i`, `1<=i<=m-1`, and put
`L=(p_0,...,p_{i-1})`, `R=(p_{i+1},...,p_m)`.
Both `L,R` are nonempty tight paths.

Let `F_y` be any exact two-path cover of `H-y`.

## 1. Internal-deletion trichotomy

At least one of the following holds:

1. `F_y` has an ordinary edge joining two distinct members of `{L,R,Q}`.
2. On the common vertices with the original cover, `F_y` has a relative-order disagreement with the inherited order of `P` or `Q`.
3. `F_y` is exactly the same-slot replacement
   `(p_0,...,p_{i-1},x,p_{i+1},...,p_m)|Q`.

Thus an internal deletion has a unique no-crossing/no-order-disagreement normal form: the omitted vertex `x` replaces the deleted internal vertex `y` in its original slot.

### Proof

Partition `V(H)-{y}` into the four nonempty classes `V(L),V(R),V(Q),{x}`. Apply the transition identity `the path-cover surgery and comparison module` Section 6 to the exact two-cover `F_y`. Each class is Hamiltonian, so if `t` is the number of cross-class ordinary edges of `F_y`, then `t>=4-2=2`.

If `t>=3`, the singleton `x` is incident with at most two ordinary edges of the path forest, so some cross-class edge avoids `x`; it joins two of `L,R,Q`, giving outcome 1. The same is true when `t=2` and at least one cross-class edge avoids `x`.

Suppose therefore that `t=2` and both cross-class edges are incident with `x`. Equality in the transition bound implies that each of `L,R,Q,{x}` occurs as exactly one block after the two cross edges are cut. Hence `x` is internal in one cover component and joins two of the three inherited path blocks, while the third inherited block is the other cover component.

If any inherited block is traversed in an order that disagrees with its displayed order, outcome 2 holds. If `x` joins `L` to `Q` or `R` to `Q`, the unjoined side of `P-y` remains in its inherited order; restoring `y` to that side using the original path `P` gives a spanning two-cover of `H`, impossible. If `x` joins `R` before `L`, then common vertices of `P` occur in the reverse block order, giving outcome 2. The only remaining possibility is `L,x,R` together with unchanged `Q`, which is outcome 3. ∎

## 2. Adjacent clean replacements form a transitive compatible triangle

Call outcome 3 a clean internal replacement. If `p_i` and `p_{i+1}` both admit clean internal replacements using chosen covers `F_{p_i},F_{p_{i+1}}`, then
`F_x=P|Q`, `F_{p_i}`, and `F_{p_{i+1}}`
are pairwise compatible. Their deleted-label precedence is
`p_i < x < p_{i+1}`.

Indeed, after deleting the two relevant labels, all three covers have the same two support classes and the same inherited order on their common vertices.

Therefore the transitive compatible-triangle theorem `the two-deep common-gap theorem` applies. The common insertion gap must have at least two common vertices on each side. Consequently
`2<=i<=m-3`.
In particular the adjacent pairs `{p_1,p_2}` and `{p_{m-2},p_{m-1}}` cannot both be clean.

## 3. Four consecutive clean replacements force a tight 3-cycle

Suppose `p_{i-1},p_i,p_{i+1},p_{i+2}` all admit clean internal replacements. Then
`(x,p_i,p_{i+1})`
is tight from the replacement of `p_{i-1}`, and
`(p_i,p_{i+1},x)`
is tight from the replacement of `p_{i+2}`.

If `(p_i,x,p_{i+1})` were tight, then the replacement of `p_{i+1}` supplies `(p_{i-1},p_i,x)` and the replacement of `p_i` supplies `(x,p_{i+1},p_{i+2})`; inserting `x` between `p_i,p_{i+1}` in the original order of `P` would therefore give a Hamilton path on `V(P) union {x}`, which together with `Q` would two-cover `H`. Hence `(p_i,x,p_{i+1})` is non-tight, so boundary antisymmetry gives
`(p_{i+1},x,p_i)`
tight.

Thus the three cyclic triples
`(x,p_i,p_{i+1})`, `(p_i,p_{i+1},x)`, `(p_{i+1},x,p_i)`
are all tight. ∎

This packages internal deletion dynamics at arbitrary path length: persistent clean behavior is not featureless; it becomes the one-gap compatibility geometry and, along a long clean run, literal tight-cycle structure.



---

# Endpoint-state trichotomy for direct vertex addition

Let `H` be a minimum-order counterexample to the two-cover conjecture. Fix a vertex `x` and an exact two-path cover
`H-x=P|Q`.

Then both `P` and `Q` have order at least three.

For an endpoint `y` of one component, let `T_y` be the exact two-cover of `H-{x,y}` obtained by deleting `y` from the displayed cover `P|Q`. Choose any exact two-cover `C_y` of `H-y`. Then at least one of the following holds.

1. **Internal-restoration crossing.** The vertex `x` is internal in a component of `C_y`, and `T_y` has an ordinary edge crossing the three nonempty inherited path supports obtained from `C_y-x`.

2. **Bridge disagreement.** The vertex `x` is an endpoint in `C_y`, deleting it gives an exact two-cover `T'_y` of `H-{x,y}`, and `T'_y` differs from `T_y` as an ordered two-path cover. Then `T_y,T'_y` expose either a support-partition crossing or, on a common support, a reversed common edge, a reversing tight triple, or a vertex-simple tight cycle.

3. **Clean omission swap.** The vertex `x` is an endpoint in `C_y`, deleting it gives exactly `T_y`, and `C_y` is obtained from `T_y` by restoring `x` at the same end of the same component at which `y` restores the original cover `P|Q`.

Thus every endpoint either produces explicit crossing/order complexity or permits a rigid swap of the omitted vertex.

## Proof of the trichotomy

First suppose one component of `H-x`, say `P=(p_0,p_1)`, had order two. Deleting `p_0` from `P|Q` would give the exact two-cover
`(p_1)|Q`
of `H-{x,p_0}` with a singleton component, contradicting the minimum-counterexample calculus. Hence every component has order at least three.

Fix an endpoint `y` of one component. Because that component has order at least three, deleting `y` leaves two nonempty displayed paths, so `T_y` is indeed an exact two-cover of `H-{x,y}`.

Apply the two-end bridge trichotomy `the two-deletion endpoint trichotomy above` to the covers `P|Q` of `H-x`, `C_y` of `H-y`, and `T_y` of `H-{x,y}`.

The vertex `y` is an endpoint in the displayed cover of `H-x`, so the branch in which `y` is internal there is impossible. If `x` is internal in `C_y`, `the two-deletion endpoint trichotomy above` gives outcome 1.

Otherwise both deleted vertices are endpoints. Deleting them gives two exact covers of the common two-deletion graph: `T_y` from the original state and `T'_y=C_y-x` from the new state. If they differ as ordered two-path covers, the bridge-disagreement theorem `the exact-cover disagreement theorem above` gives outcome 2.

If they agree, `the two-deletion endpoint trichotomy above` says that every endpoint extension by `x` or `y` uses the same end of the same component of the common cover. Since restoring `y` there recovers the displayed state `P|Q`, restoring `x` must occur at that same component end. This is outcome 3. ∎

## Two clean swaps on one component

Assume that neither endpoint of
`P=(p_0,...,p_m)`
produces outcomes 1 or 2. Then both endpoint swaps are clean, so exact two-covers exist in the explicit forms
`(x,p_1,...,p_m)|Q`
of `H-p_0` and
`(p_0,...,p_{m-1},x)|Q`
of `H-p_m`.

If `|P|>=4`, put
`M=(p_1,...,p_{m-1})`.
Then `|M|>=2`, and the two clean covers show that both concatenations
`(x,M)`
and
`(M,x)`
are tight. Applying the opposite-concatenation lemma `the opposite-concatenation theorem above` with the singleton path `(x)`, at least one of the following conclusions holds:

- the cyclic ordering
  `(x,p_1,...,p_{m-1})`
  is a tight cycle; or
- the wrap triple
  `(p_1,x,p_{m-1})`
  is tight.

If instead `|P|=3`, write
`P=(p_0,p_1,p_2)`.
The four-set
`V(P) union {x}`
is non-Hamiltonian, since a Hamilton path on it together with `Q` would two-cover `H`.
The original path and the right clean swap give
`(p_0,p_1,p_2)`
and
`(p_0,p_1,x)`
tight. The four-vertex classification `the small-set structure module` therefore gives one of its two matching-block edge-order forms. The left clean swap additionally gives
`(x,p_1,p_2)`
tight, which selects the unique block order
`{p_0p_1,p_2x} < {p_0p_2,p_1x} < {p_0x,p_1p_2}`.

Hence complete absence of endpoint crossing/order complexity is itself rigid: every component of order at least four yields a cycle-or-wrap configuration around the omitted vertex, while every component of order three yields the displayed unique non-Hamiltonian matching-block K4. ∎

This is a direct-induction state theorem. It does not supply a termination potential by itself, but it reduces a featureless omission slide to explicit intrinsic structure and applies at arbitrary component orders.



---

# Clean omission swaps cannot iterate without order disagreement

Let `H` be a minimum-order counterexample to the two-cover conjecture. Fix a vertex `x` and an exact two-cover
`H-x=P|Q`,
where
`P=(p_0,...,p_m)`.
By `the endpoint-state trichotomy above`, `|P|>=3`.

For each endpoint `p_0,p_m`, apply the endpoint-state trichotomy of `the endpoint-state trichotomy above`.

## Theorem

Either one endpoint of `P` already produces an internal-restoration crossing or bridge-disagreement witness, or both endpoint swaps are clean and then, after performing either clean swap, the opposite endpoint necessarily produces bridge disagreement.

More explicitly, if both original endpoint swaps are clean, then there are exact covers

`C_0=(x,p_1,...,p_m)|Q`
of `H-p_0`

and

`C_m=(p_0,...,p_{m-1},x)|Q`
of `H-p_m`.

Regard `C_0` as the new near-spanning state with omitted vertex `p_0`, and inspect its endpoint `p_m`. The inherited common deletion cover of
`H-{p_0,p_m}`
is

`T=(x,p_1,...,p_{m-1})|Q`.

Using `C_m` as the comparison cover of `H-p_m`, deleting the new omitted vertex `p_0` gives

`T'=(p_1,...,p_{m-1},x)|Q`.

The support partitions of `T,T'` agree, but their Hamilton orders on
`{x,p_1,...,p_{m-1}}`
disagree. Hence the bridge-disagreement branch is forced.

Consequently every component of every near-spanning state
`P|Q|(x)`
in a minimum counterexample yields explicit crossing/order complexity either immediately at an endpoint or after at most one clean omission swap. In particular there is no sequence of two consecutive clean swaps that traverses opposite ends of one component without exposing order disagreement.

## Proof

If either endpoint of `P` gives outcome 1 or 2 of `the endpoint-state trichotomy above`, there is nothing to prove. Assume therefore that both endpoints give outcome 3. The two displayed covers `C_0,C_m` are exactly the clean-swap conclusion of that theorem.

Now use `C_0` as a near-spanning cover of `H-p_0`. Its first component is
`P_0=(x,p_1,...,p_m)`,
whose endpoint `p_m` may be deleted. This gives the inherited exact two-cover

`T=(x,p_1,...,p_{m-1})|Q`

of `H-{p_0,p_m}`.

For the endpoint-state comparison at `p_m`, choose the already existing exact cover
`C_m`
of `H-p_m`. The omitted vertex for the new state is `p_0`, and it is the first endpoint of the first component of `C_m`. Deleting it yields

`T'=(p_1,...,p_{m-1},x)|Q`.

Thus the two common deletion covers have exactly the same two supports. They are not the same ordered cover. Indeed, since `m>=2`, both contain the distinct vertices `x,p_1`; in `T`, `x` precedes `p_1`, while in `T'`, `p_1` precedes `x`.

Therefore the clean-swap branch of the endpoint-state trichotomy is impossible at this second step. The support partitions agree, so the disagreement is purely an ordered-path disagreement on the common support. The ordered-path intersection lemma consequently yields a reversed common ordered edge, a tight triple reversing an ordered edge at an intersection, or a vertex-simple tight cycle.

The argument with left and right interchanged is identical. ∎



# Order-four double-clean endpoint obstruction

## Corollary — order-four components cannot be clean at both ends

Let H be a minimum counterexample, let x be a vertex, and let

H-x=P|Q

be an exact two-cover with

P=(p_0,p_1,p_2,p_3).

Apply the endpoint-state trichotomy earlier in this module to p_0 and p_3. The two endpoint probes cannot both be clean omission swaps.

Indeed, if both were clean, then H-p_0 would contain the tight path

(x,p_1,p_2,p_3),

while H-p_3 would contain the tight path

(p_0,p_1,p_2,x).

Together with the original tight path P, the lemma applies with

a=p_0, u=p_1, v=p_2, b=p_3, c=x.

Hence H[V(P) union {x}] is Hamiltonian. Its Hamilton path together with the unchanged path Q gives a spanning exact two-cover of H, contradiction.

Therefore every order-four component of every near-spanning deletion cover exposes an internal-restoration crossing or bridge-disagreement witness at at least one of its two endpoints. ∎

# Stabilized deletion family from a double-clean five-component

Let `H` be a minimum-order counterexample to the two-cover conjecture.
Fix a vertex `x` and an exact two-cover

`H-x=P|Q`,

where

`P=(p_0,p_1,p_2,p_3,p_4)`

has order five and

`Q=(q_0,...,q_m)`.

Assume the endpoint-state trichotomy `the endpoint-state trichotomy earlier in this module` is clean at both endpoints `p_0,p_4` of `P`.
Thus

`(x,p_1,p_2,p_3,p_4)|Q`

is an exact two-cover of `H-p_0`, and

`(p_0,p_1,p_2,p_3,x)|Q`

is an exact two-cover of `H-p_4`.

Put

`S=V(P) union {x}`.

## Theorem

The induced six-set `H[S]` is non-Hamiltonian.

Let

`G={z in S : H[S-{z}] is Hamiltonian}`.

Then

`|G|>=4`

and

`{x,p_0,p_4} subseteq G`.

For every `z in G`, if `R_z` is any Hamilton path on `S-{z}`, then

`R_z|Q`

is an exact two-cover of `H-z`.

Consequently every `z in G` satisfies the same two endpoint barriers relative to the fixed outside path `Q`:

`(q_1,q_0,z)`

and

`(z,q_m,q_{m-1})`

are tight.

Thus a double-clean five-component does not remain an isolated endpoint phenomenon: it creates a fixed six-set with at least four Hamiltonian deletions, all synchronized against the same exterior path.

## Proof

If `H[S]` were Hamiltonian, a Hamilton path on `S` together with `Q` would form a spanning two-cover of `H`, impossible. Hence `H[S]` is non-Hamiltonian.

The deletion `S-{x}=V(P)` is Hamiltonian because `P` itself is a tight Hamilton path.
The two clean endpoint swaps show that

`S-{p_0}`

and

`S-{p_4}`

are Hamiltonian as well.
Therefore

`x,p_0,p_4 in G`.

By the four-of-six theorem, every six-vertex boundary tournament has at least four Hamiltonian five-vertex deletions. Hence
`|G|>=4`.
In particular at least one of the three internal vertices
`p_1,p_2,p_3`
also belongs to `G`.

Fix `z in G` and a Hamilton path `R_z` on `S-{z}`.
Since
`V(H-z)=(S-{z}) disjoint-union V(Q)`,
the two paths
`R_z|Q`
form an exact two-cover of `H-z`.

Apply the deleted-vertex endpoint barrier to this cover, with omitted vertex `z` and the fixed component
`Q=(q_0,...,q_m)`.
Both components of a deletion cover in a minimum counterexample are nontrivial, so `m>=1`, and the endpoint barriers give

`(q_1,q_0,z)`

and

`(z,q_m,q_{m-1})`

tight.

The conclusion holds for every `z in G`. ∎

# Sharpness at order five: clean swaps at both ends need not absorb

# Counterexample — two clean endpoint swaps do not Hamiltonize a five-vertex component

Let the vertices be

p_0,p_1,p_2,p_3,p_4,x.

Give the complete graph the following strict edge order from least to greatest:

p_1x < p_1p_3 < p_0p_2 < p_0p_1 < p_0x < p_2p_4 < p_4x < p_0p_3 < p_0p_4 < p_1p_2 < p_1p_4 < p_2p_3 < p_3x < p_2x < p_3p_4.

Let H be the induced edge-orderable boundary tournament.

Then all three sequences

P=(p_0,p_1,p_2,p_3,p_4),

P_L=(x,p_1,p_2,p_3,p_4),

P_R=(p_0,p_1,p_2,p_3,x)

are tight paths.

Indeed, their consecutive edge ranks are respectively

p_0p_1 < p_1p_2 < p_2p_3 < p_3p_4,

p_1x < p_1p_2 < p_2p_3 < p_3p_4,

p_0p_1 < p_1p_2 < p_2p_3 < p_3x.

Nevertheless H has no Hamilton tight path on all six vertices.

This last assertion is an exact finite verification: among the 6!=720 vertex orders, none has its five consecutive ordinary edges increasing in the displayed edge order.

Thus the order-four consequence of the order-four double-clean obstruction above is sharp. For a component of order five, both endpoint omission swaps may be clean while adjoining the omitted vertex still fails to Hamiltonize that component support.

The direct the defect-compression / endpoint-restoration program argument therefore cannot proceed by induction on component order using only the two clean endpoint swaps of one component. It must also use interaction with the second path, such as the cross-component barriers of the four-clean-swap cross-component barrier theorem, or a genuinely global reorder. ∎
