# Common-middle rectangle and endpoint barriers

## Statement

Two opposite common-middle paths force the full four-corner rectangle. Crossed-support comparison is cardinality-free; in a four-corner rectangle with a three-vertex exterior set, at least one—and unless universal, at least two—exterior vertices support three compatible complement deletions and therefore satisfy all four endpoint barriers.

## Body

# Common-middle rectangle and endpoint-barrier transport

Let `H` be a 3-uniform directed hypergraph. Let
`M=(m_1,...,m_h)`
be a tight path with `h>=2`, and let `a,ell,c,r` be distinct vertices outside `V(M)`.

Suppose both
`(a,M,c)`
and
`(ell,M,r)`
are tight paths.

Then the two mixed paths
`(a,M,r)`
and
`(ell,M,c)`
are also tight.

## Proof

Every consecutive triple wholly inside `M` is tight. The first consecutive triple of `(a,M,r)` is `(a,m_1,m_2)`, inherited from `(a,M,c)`, while its last consecutive triple is `(m_{h-1},m_h,r)`, inherited from `(ell,M,r)`. Hence `(a,M,r)` is tight.

The same argument with the two endpoint choices interchanged shows that `(ell,M,c)` is tight. ∎

## Application to successful exchange

In the successful middle-preserving exchange, take
`M=(y_1,...,y_{k-1})`, `a=y_0`, `c=y_k`.
The original Hamilton path `(a,M,c)` and the successful exchanged path `(ell,M,r)` therefore force the full common-middle square
`(a,M,c)`, `(a,M,r)`, `(ell,M,c)`, `(ell,M,r)`.

Thus the successful-exchange branch is naturally a four-corner common-middle configuration, not merely a pair of long paths. This is exactly the structural input required by the current four-endpoint barrier line once that result is independently audited.

# Cardinality-free crossed-support comparison

Let `K` be a boundary tournament with `pc(K)>2`. Let `w,u,v` be distinct vertices, and let `T,C` be disjoint nonempty vertex sets disjoint from `{w,u,v}`. Suppose `K-w` has exact two-path covers
`A^u | B^u` and `B^v | A^v`
with
`V(A^u)=T∪{u}`, `V(A^v)=T∪{v}`,
`V(B^u)=C∪{v}`, `V(B^v)=C∪{u}`.
Assume moreover that deleting `v` from the vertex sequence `B^u` and deleting `u` from the vertex sequence `B^v` both leave tight paths on `C`.

Then:

1. if `u` is internal in `A^u`, deleting `u` splits `A^u` into two nonempty tight subpaths `P,Q` whose supports partition `T`, and some ordinary edge of `A^v` has endpoints in two different members of `V(P) | V(Q) | {v}`;
2. symmetrically, if `v` is internal in `A^v`, some ordinary edge of `A^u` crosses the analogous three-part partition obtained by deleting `v` from `A^v`;
3. if `u` is an endpoint of `A^u` with path neighbor `t∈T`, then beginning with `(u,t,...)` forces `(t,u,w)` tight, while ending with `(...,t,u)` forces `(w,u,t)` tight;
4. the symmetric endpoint assertions hold for `v` in `A^v`.

No cardinality hypothesis on `T` or `C` is needed beyond nonemptiness.

## Proof

Suppose `u` is internal in `A^u`. Deleting `u` splits `A^u` into two nonempty tight subpaths `P,Q` whose supports partition `T`; together with `B^u` they form a three-path cover of `K-{w,u}`.

Deleting `u` from the second exact cover leaves `(B^v-u)|A^v`, a two-path cover of the same induced subtournament. By hypothesis `B^v-u` is a tight path on `C`. If `K-{w,u}` were Hamiltonian, a Hamilton path there together with the two-vertex path `(w,u)` would two-cover `K`; hence `pc(K-{w,u})=2`.

Apply the component-drop comparison theorem in the path-cover surgery module to the three-path cover `P|Q|B^u` and the two-path cover `(B^v-u)|A^v`. Some ordinary edge of the latter has endpoints in two different components of the former. Every vertex of `B^v-u` lies in `C⊆V(B^u)`, so every edge of `B^v-u` lies wholly inside the `B^u` component. Therefore the required crossing edge lies in `A^v`. Since `V(A^v)=T∪{v}` and `T=V(P)⊔V(Q)`, its endpoints lie in two different members of `V(P)|V(Q)|{v}`.

The assertion with `v` internal in `A^v` is symmetric.

Now suppose `u` is an endpoint of `A^u` with path neighbor `t∈T`. If `A^u` begins `(u,t,...)` and `(w,u,t)` were tight, prepending `w` would enlarge `A^u` and, together with `B^u`, give a spanning two-path cover of `K`. Hence `(w,u,t)` is non-tight and `(t,u,w)` is tight. If `A^u` ends `(...,t,u)`, the same restoration argument shows `(t,u,w)` is non-tight, so `(w,u,t)` is tight. The assertions for `v` are symmetric. ∎

# Four-endpoint barrier from a common-middle square

Let `K` be a boundary tournament with `pc(K)>2`. Let `M=(m_1,...,m_h)`, `h>=2`, be a tight path, let `a,ell,c,r` be four distinct vertices outside `M`, and let `T` be a three-vertex set disjoint from all of them. Assume `V(K)=V(M) sqcup {a,ell,c,r} sqcup T` and that all four paths `(a,M,c)`, `(a,M,r)`, `(ell,M,c)`, `(ell,M,r)` are tight.

Then there is a vertex `s in T` for which all four triples `(m_1,a,s)`, `(m_1,ell,s)`, `(s,c,m_h)`, and `(s,r,m_h)` are tight.

More precisely, for this `s`, at least three of the four displayed common-middle paths occur as one component of exact two-path covers of `K-s`, and the complementary four-vertex components may be chosen compatibly across adjacent corners.

## Proof

For `u in {a,ell}` and `v in {c,r}`, let `P_{uv}=(u,M,v)` and let `C_{uv}=V(K)-V(P_{uv})`. Each `C_{uv}` has five vertices. Since `P_{uv}` is tight and `pc(K)>2`, the induced boundary tournament `K[C_{uv}]` is non-Hamiltonian.

A non-Hamiltonian five-vertex boundary tournament has at most one non-Hamiltonian four-vertex induced subtournament. Hence, for each of the four pairs `(u,v)`, at least two vertices `s in T` have `K[C_{uv}-{s}]` Hamiltonian. Across the four pairs there are therefore at least eight good incidences. Since `|T|=3`, some `s in T` is good for at least three of the four pairs.

Any three corners of a `2 x 2` square contain both a pair with the same right endpoint and different left endpoints, and a pair with the same left endpoint and different right endpoints.

Fix the chosen `s`.

### The left endpoints

Let `v in {c,r}` be a right endpoint for which both `(a,v)` and `(ell,v)` are good. Then `K-s` has exact two-path covers `(a,M,v) | B_a` and `(ell,M,v) | B_ell`, where the supports of `B_a,B_ell` differ by exchanging `a` and `ell`.

Each short support is a Hamiltonian four-set lying inside a non-Hamiltonian five-set and therefore inherits an edge-order representation. By the prescribed-removable-vertex theorem in the edge-ordered comparison module, choose `B_a,B_ell` so that deleting `ell` from `B_a`, respectively `a` from `B_ell`, leaves a tight path on their common three-vertex support.

Apply the crossed-support theorem above to these two covers of `K-s`, with the long components as the exchanged supports. Both exchanged vertices are initial endpoints of their long paths, with common path neighbor `m_1`. Hence `(m_1,a,s)` and `(m_1,ell,s)` are tight.

### The right endpoints

Similarly, choose `u in {a,ell}` for which both `(u,c)` and `(u,r)` are good. We obtain exact two-path covers `(u,M,c) | D_c` and `(u,M,r) | D_r` of `K-s`, with the short paths chosen so that deletion of the exchanged right endpoint leaves a tight path on the common three-vertex support.

Apply the crossed-support comparison again, now exchanging the terminal vertices `c,r` of the long paths. Their common path neighbor is `m_h`, so `(s,c,m_h)` and `(s,r,m_h)` are tight.

Thus the same vertex `s` satisfies all four asserted endpoint barriers. ∎

# Multiplicity of compatible deletions across the square

Keep the setup of the four-endpoint-barrier theorem. For each `u in {a,ell}` and `v in {c,r}`, let
`C_{uv}=V(K)-V(u,M,v)`
and define
`D_{uv}={x in T : K[C_{uv}-{x}] is Hamiltonian}`.

Then either:

1. some vertex of `T` belongs to all four sets `D_{uv}`; or
2. two distinct vertices of `T` each belong to at least three of the four sets `D_{uv}`.

Moreover, every vertex `x in T` belonging to at least three of the four sets satisfies all four endpoint barriers
`(m_1,a,x)`, `(m_1,ell,x)`, `(x,c,m_h)`, and `(x,r,m_h)`
tight.

## Proof

For each `u in {a,ell}` and `v in {c,r}`, the path `(u,M,v)` is tight. Since `pc(K)>2`, its five-vertex complement `K[C_{uv}]` is non-Hamiltonian. A non-Hamiltonian five-vertex boundary tournament has at most one non-Hamiltonian four-vertex induced subtournament. Hence `|D_{uv}|>=2` for all four pairs `(u,v)`.

For `x in T`, let `d(x)=|{(u,v):x in D_{uv}}|`. Double counting incidences gives
`sum_{x in T} d(x)=sum_{u,v}|D_{uv}|>=8`.

If some `x` has `d(x)=4`, the first alternative holds. Otherwise every `d(x)<=3`. If at most one vertex had degree at least three, then `sum_{x in T}d(x)<=3+2+2=7`, contrary to the preceding bound. Thus two distinct vertices of `T` each belong to at least three of the four sets.

Now let `x` belong to at least three of the four sets. Any three members of the `2 x 2` family indexed by `{a,ell} x {c,r}` contain two with a common right endpoint and different left endpoints, and two with a common left endpoint and different right endpoints.

Choose `v in {c,r}` with `x in D_{av} intersection D_{ell v}`. Then `K-x` has exact two-path covers `(a,M,v) | B_a` and `(ell,M,v) | B_ell`, where the short components are Hamilton paths on the corresponding four-vertex complements. Choose these Hamilton paths so that deleting the exchanged left endpoint leaves a tight path on the common three-vertex support. The crossed-support endpoint comparison gives `(m_1,a,x)` and `(m_1,ell,x)` tight.

Similarly choose `u in {a,ell}` with `x in D_{uc} intersection D_{ur}`. Compatible Hamilton paths on the two short complements and the terminal form of the crossed-support theorem above give `(x,c,m_h)` and `(x,r,m_h)` tight. ∎

Thus failure of a universal compatible deletion cannot leave only one highly compatible vertex: it forces two distinct vertices carrying the same four endpoint barriers.
