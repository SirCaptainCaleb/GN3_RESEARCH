# Codimension-four exterior deletion structure

Let `K` be a boundary tournament with `pc(K)>2` and

`V(K)=S \sqcup V(P)`, `|S|=4`,

where

`P=(x_0,\ldots,x_{m-1})`

is a Hamilton tight path with `m>=3`. Put `Y=V(P)`, `L=x_0`, and `R=x_{m-1}`.

Only the displayed hypotheses are assumed throughout.

## 1. Universal four-vertex-complement structure

### Proposition 1.1

No tight path of `K` has more than `m` vertices. The induced boundary tournament `K[S]` is non-Hamiltonian.

Moreover, for every Hamilton ordering of `Y` with endpoints `L,R`:

1. `K[S\cup\{L\}]`, `K[S\cup\{R\}]`, and `K[S\cup\{L,R\}]` are non-Hamiltonian;
2. for every `s\in S`, each of `K[(S-\{s\})\cup\{L\}]`, `K[(S-\{s\})\cup\{R\}]`, and `K[(S-\{s\})\cup\{L,R\}]` is Hamiltonian;
3. `K[S]` has an edge-order representation in which the three opposite-edge perfect matchings occur as intrinsic strict blocks `M_{\mathrm{low}}<M_{\mathrm{mid}}<M_{\mathrm{high}}`.

**Proof.**
Suppose `Q` is a tight path of `K` on more than `m=|V(K)|-4` vertices. If `Q` spans `K`, then `pc(K)=1`, impossible. Otherwise its complement has order one, two, or three and is Hamiltonian, so a Hamilton path of the complement together with `Q` gives a spanning two-path cover of `K`, again impossible. Thus no tight path has more than `m` vertices.

The induced boundary tournament `K[S]` is non-Hamiltonian, because otherwise a Hamilton path on `Y` and a Hamilton path of `K[S]` would two-cover `K`.

If `K[S\cup\{L\}]` were Hamiltonian, its Hamilton path together with the tight path obtained from the chosen ordering of `Y` by deleting `L` would two-cover `K`. Hence `K[S\cup\{L\}]` is non-Hamiltonian, and the same argument applies to `K[S\cup\{R\}]`. If `K[S\cup\{L,R\}]` were Hamiltonian, its Hamilton path together with the nonempty interior subpath obtained by deleting `L,R` from `Y` would two-cover `K`; hence it too is non-Hamiltonian.

Fix `s\in S`. By Lemma 2.3 of the proof spine, the non-Hamiltonian induced subtournament `K[S\cup\{L\}]` has an edge-order representation. If `K[(S-\{s\})\cup\{L\}]` were also non-Hamiltonian, then in this edge-ordered complete graph the two four-sets `S` and `(S-\{s\})\cup\{L\}` would both have no increasing Hamilton path and would meet in the three-set `S-\{s\}`. Lemma 2.4 of the proof spine would then give an increasing Hamilton path on all five vertices, a contradiction. Thus `K[(S-\{s\})\cup\{L\}]` is Hamiltonian. The same argument applies with `R`.

Apply `TOOLKIT/LOCAL_HAMILTON_EXTENSIONS.md` Section 2 to the six-set `S\cup\{L,R\}`. At least four of its five-subsets induce Hamiltonian boundary tournaments. The two obtained by deleting `L` or `R` are `S\cup\{R\}` and `S\cup\{L\}`, whose induced subtournaments are non-Hamiltonian. Therefore every `K[(S-\{s\})\cup\{L,R\}]`, `s\in S`, is Hamiltonian.

Finally, an edge-order representation of `S\cup\{L\}` restricts to one of `K[S]`. Since `K[S]` is non-Hamiltonian, Lemma 2.4 places the six ordinary edges on `S` into three strict opposite-edge perfect-matching blocks. Any two edges from different perfect matchings meet, so their comparison is fixed by the boundary relation on `S`; hence the order of the three blocks is intrinsic. ∎


### Proposition 1.2

Assume `m\ge2`, and put `u=x_1`, `v=x_{m-2}`. Then for every `s\in S`, the triples `(u,L,s)` and `(s,R,v)` are tight.

**Proof.**
If `(s,L,u)` were tight, then prepending `s` to the Hamilton ordering of `Y` would give a Hamilton path on `Y\cup\{s\}`. The complementary three-set `S-\{s\}` is Hamiltonian, so `K` would have a spanning two-path cover. Therefore `(s,L,u)` is not tight, and boundary antisymmetry gives `(u,L,s)`. The terminal assertion is identical. ∎


## 2. Exact covers after deleting exterior vertices

### Proposition 2.1

Put

`P_L=(x_1,\ldots,x_{m-1})`, `P_R=(x_0,\ldots,x_{m-2})`, and `Q=(x_1,\ldots,x_{m-2})`.

For every `s\in S` there exist Hamilton paths `A_s^L,A_s^R,A_s^{LR}` on, respectively,

`(S-\{s\})\cup\{L\}`, `(S-\{s\})\cup\{R\}`, `(S-\{s\})\cup\{L,R\}`.

The pairs

`A_s^L\mid P_L`, `P_R\mid A_s^R`, `A_s^{LR}\mid Q`

are exact two-path covers of `K-s`. Moreover every exact two-path cover of `K-s` has both components of order at least three.

For distinct `s,t\in S`, put `B=S-\{s,t\}`. Then `pc(K-\{s,t\})=2`, and exact two-path covers of `K-\{s,t\}` include

`P\mid B`, `P_L\mid C_L`, `P_R\mid C_R`,

where `B` has either of its two orders and `C_L,C_R` are any Hamilton paths on the three-vertex sets `B\cup\{L\}` and `B\cup\{R\}`.

**Proof.**
Proposition 1.1 supplies the three Hamilton paths for every `s\in S`. Each displayed pair has disjoint nonempty supports whose union is `V(K)-\{s\}`; the path `Q` is nonempty because `m>=3`. Thus each pair is a two-path cover of `K-s`.

If `K-s` were Hamiltonian, a Hamilton path on `K-s` together with the singleton path `(s)` would two-cover `K`. Hence `pc(K-s)=2`, and the displayed covers are exact.

Suppose an exact two-path cover of `K-s` had a component with support `C` of order one or two. Then `K[C\cup\{s\}]` has order at most three and is Hamiltonian. Replacing that component by a Hamilton path on `C\cup\{s\}` would give a spanning two-path cover of `K`, a contradiction. Thus both components have order at least three.

Now fix distinct `s,t\in S`. The set `B` has order two, so either ordering is a tight path. Each of `B\cup\{L\}` and `B\cup\{R\}` has order three and therefore has a Hamilton path. Hence the three displayed pairs are two-path covers of `K-\{s,t\}`. If `K-\{s,t\}` were Hamiltonian, a Hamilton path on it together with the two-vertex path `(s,t)` would two-cover `K`. Therefore `pc(K-\{s,t\})=2`, and all three displayed covers are exact. ∎

## 3. Five-vertex complements

The following three propositions concern an arbitrary Hamilton path with five-vertex complement.

### Proposition 3.1

Let `K` be a boundary tournament with `pc(K)>2`, let `Y=(y_0,...,y_m)` be a Hamilton tight path with `m>=1`, and put `U=V(K)-V(Y)`. If `|U|=5`, then there exist distinct `u,v∈U` such that, for each `w∈{u,v}`, the three induced boundary tournaments
`K[U-{w}]`, `K[(U-{w})∪{y_0}]`, and `K[(U-{w})∪{y_m}]`
are Hamiltonian. Consequently, if `A_w^-` and `A_w^+` are Hamilton paths of the latter two induced subtournaments, then
`A_w^- | (w) | (y_1,...,y_m)`
and
`(y_0,...,y_{m-1}) | (w) | A_w^+`
are spanning three-path covers of `K`.

**Proof.**
If `K[U]` were Hamiltonian, a Hamilton path of `K[U]` together with `Y` would two-cover `K`. Hence `K[U]` is non-Hamiltonian, so Lemma 2.7 gives a set
`A_0={w∈U:K[U-{w}] is Hamiltonian}`
with `|A_0|>=4`.

The induced subtournaments on `U∪{y_0}` and `U∪{y_m}` are non-Hamiltonian, since a Hamilton path on either set together with the complementary inherited suffix or prefix of `Y` would two-cover `K`. Each six-set has at least four Hamiltonian five-subsets, while `K[U]` is non-Hamiltonian. Hence
`A_L={w∈U:K[(U-{w})∪{y_0}] is Hamiltonian}`
and
`A_R={w∈U:K[(U-{w})∪{y_m}] is Hamiltonian}`
both have order at least four. Therefore `|A_0∩A_L∩A_R|>=2`.

Choose distinct `u,v` in this intersection. For either `w`, each displayed three-path cover consists of a Hamilton path on one five-set, the singleton `w`, and the complementary inherited subpath of `Y`; their vertex sets are pairwise disjoint and cover `V(K)`. ∎

### Proposition 3.2

Let `K` be a boundary tournament with `pc(K)>2`, let `Y=(y_0,...,y_m)` be a Hamilton tight path with `m>=2`, and put `U=V(K)-V(Y)`. If `|U|=5`, then there exist distinct `u,v∈U` such that, for each `w∈{u,v}`, writing `A=U-{w}`, the induced boundary tournament `K-w` has exact two-path covers
`A_w^- | (y_1,...,y_m)`
and
`(y_0,...,y_{m-1}) | A_w^+`,
where `A_w^-` is a Hamilton path on `A∪{y_0}` and `A_w^+` is a Hamilton path on `A∪{y_m}`.

**Proof.**
Proposition 3.1 gives distinct `u,v∈U` such that, for each `w∈{u,v}`, both induced subtournaments `K[(U-{w})∪{y_0}]` and `K[(U-{w})∪{y_m}]` are Hamiltonian. Choose Hamilton paths `A_w^-` and `A_w^+` on these two sets.

For each such `w`, the paths `A_w^-` and `(y_1,...,y_m)` are nonempty, vertex-disjoint, and their supports partition `V(K)-{w}`; likewise `(y_0,...,y_{m-1})` and `A_w^+` are nonempty, vertex-disjoint, and partition `V(K)-{w}`. Hence the two displayed pairs are two-path covers of `K-w`.

They are exact. If `K-w` were Hamiltonian, a Hamilton path on `K-w` together with the singleton path `(w)` would form a spanning two-path cover of `K`, contradicting `pc(K)>2`. ∎

### Proposition 3.3

Let `K` be a boundary tournament with `pc(K)>2`, let `Y=(y_0,y_1,...,y_m)` be a Hamilton tight path with `m>=3`, and put `U=V(K)-V(Y)`. If `|U|=5`, then there exist distinct `u,v∈U` such that, for each `w∈{u,v}`, all four triples
`(y_1,y_0,w)`, `(y_2,y_1,w)`, `(w,y_m,y_{m-1})`, and `(w,y_{m-1},y_{m-2})`
are tight.

**Proof.**
Since `Y` is Hamiltonian and `pc(K)>2`, `K[U]` is non-Hamiltonian. Lemma 2.7 therefore gives at least four vertices `w∈U` for which `K[U-{w}]` is Hamiltonian; call their set `A_0`.

The six-vertex induced subtournament `K[U∪{y_0}]` is non-Hamiltonian, because otherwise its Hamilton path together with the inherited suffix `(y_1,...,y_m)` would two-cover `K`. At least four of its five-vertex induced subtournaments are Hamiltonian. Since `K[U]` is not, at least four vertices `w∈U` make `K[(U-{w})∪{y_0}]` Hamiltonian; call this set `A_L`. The same argument at `y_m` gives a set `A_R⊆U` of order at least four.

Thus
`|A_0∩A_L∩A_R|>=4+4+4-2·5=2`.
Choose distinct `u,v` in the intersection and fix `w∈{u,v}`.

If `(w,y_0,y_1)` were tight, then `(w,y_0,y_1,...,y_m)` together with a Hamilton path on `U-{w}` would two-cover `K`. Hence `(y_1,y_0,w)` is tight. The right-end argument gives `(w,y_m,y_{m-1})`.

If `(w,y_1,y_2)` were tight, then `(w,y_1,y_2,...,y_m)` together with a Hamilton path on `(U-{w})∪{y_0}` would two-cover `K`. Hence `(y_2,y_1,w)` is tight. The right-hand argument using `K[(U-{w})∪{y_m}]` gives `(w,y_{m-1},y_{m-2})`. ∎

### Corollary 3.4

The three preceding propositions apply directly in `K` to the endpoint truncations `P_L=(x_1,\ldots,x_{m-1})` and `P_R=(x_0,\ldots,x_{m-2})`, whose complements are `S\cup\{L\}` and `S\cup\{R\}`, respectively. Proposition 3.1 applies when the original path has `m>=3`, Proposition 3.2 when `m>=4`, and Proposition 3.3 when `m>=5`.

**Proof.**
Both truncations are inherited Hamilton tight paths on their vertex sets, and their vertex complements in the same ambient tournament `K` are exactly the two displayed five-sets. ∎

## 4. A five-vertex endpoint construction

Assume now that `m\ge4`.

### Proposition 4.1

There are `s\in S` and a Hamilton ordering `M=(m_0,\ldots,m_4)` of `\{L,R\}\cup(S-\{s\})` such that one of the following holds.
For `0<=i<=j<=4`, write `M[i,j]=(m_i,\ldots,m_j)`; when `i>j`, take `M[i,j]` to be the empty sequence.

1. `L=m_p` for some `p\in\{0,3,4\}`, and the two vertex sequences `M[0,p](x_1,\ldots,x_{m-2})` and `(s)M[p+1,4]`, with empty pieces omitted, partition `V(K)` and have exactly one non-tight consecutive triple.
2. `R=m_q` for some `q\in\{0,1,4\}`, and the two vertex sequences `M[0,q-1](s)` and `(x_1,\ldots,x_{m-2})M[q,4]`, with empty pieces omitted, partition `V(K)` and have exactly one non-tight consecutive triple.

**Proof.**
Write the intrinsic matching blocks of `S` as `M_{\mathrm{low}}<M_{\mathrm{mid}}<M_{\mathrm{high}}`. By `TOOLKIT/FOUR_VERTEX_STRUCTURE.md` Section 3, relative to each of `L,R`, one edge of `M_{\mathrm{mid}}` is incoming and the other is outgoing.

Relabel `S=\{a,b,c,z\}` so that
`M_{\mathrm{low}}=\{ab,cz\}`,
`M_{\mathrm{mid}}=\{ac,bz\}`,
`M_{\mathrm{high}}=\{az,bc\}`,
and so that `bz` is outgoing from `L` while `ac` is incoming to `L`. Thus
`(L,b,z),(L,z,b),(a,c,L),(c,a,L)`
are tight. The matching-block order also gives
`(z,b,c),(c,a,z),(z,c,a),(a,c,b),(b,a,c),(b,a,z)`
tight.

For `s\in S`, call a Hamilton ordering of `\{L,R\}\cup(S-\{s\})` favorable if `L` occurs in position `0,3,4` or `R` occurs in position `0,1,4`. Suppose no favorable ordering exists for any `s\in S`.

There are two possibilities for the edge of `M_{\mathrm{mid}}` incoming to `R`.

If `ac` is incoming to `R`, then `(a,c,R),(c,a,R),(R,b,z),(R,z,b)` are tight. Successively testing the Hamilton orders
`(L,R,z,b,c)`, `(R,z,c,a,L)`, and `(c,z,R,L,a)`
forces `(z,R,L)`, `(c,z,R)`, and `(a,L,R)`, respectively. Then `(z,c,a,L,R)` is a favorable Hamilton ordering, a contradiction.

If `bz` is incoming to `R`, then `(b,z,R),(z,b,R),(R,a,c),(R,c,a)` are tight. Successively testing
`(L,b,z,R,c)`,
`(c,L,b,z,R)`,
`(L,R,c,a,z)`,
`(z,c,a,L,R)`,
`(L,R,a,c,b)`,
`(b,a,c,L,R)`,
`(c,R,L,a,z)`,
`(c,R,z,a,L)`,
`(L,b,a,z,R)`,
and `(R,a,b,L,c)`
forces respectively
`(c,R,z)`,
`(b,L,c)`,
`(c,R,L)`,
`(R,L,a)`,
`(a,R,L)`,
`(R,L,c)`,
`(z,a,L)`,
`(a,z,R)`,
`(a,b,L)`,
and `(b,a,R)`.
Then `(b,a,R,L,c)` is a favorable Hamilton ordering, again a contradiction.

Hence a favorable ordering exists. In the first alternative of the statement, the only consecutive triple not inherited from `M` or the Hamilton ordering of `Y` is, according as `p=0,3,4`,
`(s,m_1,m_2)`, `(m_2,L,x_1)`, or `(m_3,L,x_1)`.
In the second alternative, the only such triple is, according as `q=0,1,4`,
`(x_{m-2},R,m_1)`, `(x_{m-2},R,m_2)`, or `(m_2,m_3,s)`.
If this single new triple were tight, the two displayed sequences would form a spanning two-path cover of `K`, contrary to `pc(K)>2`. Therefore it is non-tight. ∎

## 5. Exact covers on the eight endpoint/complement vertices

Assume now that `m\ge6`, and put `u=x_1`, `v=x_{m-2}`, and `N=(x_2,\ldots,x_{m-3})`. The path `N` is nonempty.

Let the two edges of `M_{\mathrm{mid}}` be denoted `I,O`, where `I` is incoming and `O` is outgoing at `L`.

### Proposition 5.1

At `R` exactly one of the following occurs.

1. `I` is incoming and `O` outgoing. Writing `O=\{o_0,o_1\}` and `I=\{i_0,i_1\}`, every choice of orientations gives an exact two-path cover
   `(u,L,o_0,o_1)\mid(i_0,i_1,R,v)`
   of the induced boundary tournament on `S\cup\{L,u,v,R\}`.
2. `O` is incoming and `I` outgoing. Every orientation `(o_0,o_1)` of `O`, together with either orientation of the two-vertex path on `I`, gives an exact two-path cover
   `(u,L,o_0,o_1,R,v)\mid I`.

In either case the induced boundary tournament on `S\cup\{L,u,v,R\}` has path-cover number two.

**Proof.**
By Proposition 1.1, both `S\cup\{L\}` and `S\cup\{R\}` are non-Hamiltonian. Applying `TOOLKIT/FOUR_VERTEX_STRUCTURE.md` Section 3 at each endpoint shows that exactly one edge of `M_{\mathrm{mid}}` is incoming and the other outgoing there. Relative to the fixed names `I,O` at `L`, the assignment at `R` is therefore exactly one of the two cases in the statement.

In the first case, for either orientation `(o_0,o_1)` of `O`, the triple `(L,o_0,o_1)` is tight; Proposition 1.2 gives `(u,L,o_0)`, so `(u,L,o_0,o_1)` is a tight four-vertex path. Similarly, for either orientation `(i_0,i_1)` of `I`, the triple `(i_0,i_1,R)` is tight and Proposition 1.2 gives `(i_1,R,v)`, so `(i_0,i_1,R,v)` is a tight four-vertex path. Their supports partition the eight vertices.

In the second case, `O` is outgoing at `L` and incoming at `R`. Hence for either orientation `(o_0,o_1)`, both `(L,o_0,o_1)` and `(o_0,o_1,R)` are tight. Together with Proposition 1.2 this makes `(u,L,o_0,o_1,R,v)` a tight six-vertex path. The remaining two vertices are exactly `I`, which form a two-vertex path in either orientation.

Thus the induced boundary tournament on `S\cup\{L,u,v,R\}` has path-cover number at most two. If it were Hamiltonian, a Hamilton path on those eight vertices together with the disjoint nonempty tight path `N` would two-cover `K`, impossible. Hence its path-cover number is exactly two. ∎

### Proposition 5.2

Suppose the second case of Proposition 5.1 holds. Write `O=\{b,z\}` and `W=V(K)-I`. Then `K[W]` has the four exact two-path covers
`(u,L,b,z)\mid(x_2,\ldots,x_{m-1})`,
`(u,L,z,b)\mid(x_2,\ldots,x_{m-1})`,
`(x_0,\ldots,x_{m-3})\mid(z,b,R,v)`,
and
`(x_0,\ldots,x_{m-3})\mid(b,z,R,v)`.

**Proof.**
Proposition 1.2 gives `(u,L,s)` and `(s,R,v)` tight for every `s\in S`. Since `O=\{b,z\}` is outgoing at `L`, both `(L,b,z)` and `(L,z,b)` are tight, giving the two left four-vertex paths. Since `O` is incoming at `R`, both `(z,b,R)` and `(b,z,R)` are tight, giving the two right four-vertex paths. The complementary long pieces are contiguous subpaths of `P`, so all four displayed pairs are literal two-path covers of `W`.

If `K[W]` were Hamiltonian, a Hamilton path on `W` together with the two-vertex path on `I` would give a spanning two-path cover of `K`, impossible. Therefore `pc(K[W])=2`, and all four displayed covers are exact. ∎
