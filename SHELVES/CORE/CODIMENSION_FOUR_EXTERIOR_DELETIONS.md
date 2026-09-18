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
Suppose `P` is a tight path of `K` on more than `m=|V(K)|-4` vertices. If `P` spans `K`, then `pc(K)=1`, impossible. Otherwise its complement has order one, two, or three and is Hamiltonian, so a Hamilton path of the complement together with `P` gives a spanning two-path cover of `K`, again impossible. Thus no tight path has more than `m` vertices.

The set `S` is non-Hamiltonian, because otherwise Hamilton paths on `Y` and `S` would two-cover `K`.

If `S\cup\{L\}` were Hamiltonian, its Hamilton path together with the tight path obtained from the chosen ordering of `Y` by deleting `L` would two-cover `K`. Hence `S\cup\{L\}` is non-Hamiltonian, and the same argument applies to `S\cup\{R\}`. If `S\cup\{L,R\}` were Hamiltonian, its Hamilton path together with the nonempty interior subpath obtained by deleting `L,R` from `Y` would two-cover `K`; hence it too is non-Hamiltonian.

Fix `s\in S`. By Lemma 2.3 of the proof spine, the non-Hamiltonian five-set `S\cup\{L\}` has an edge-order representation. If `(S-\{s\})\cup\{L\}` were also non-Hamiltonian, then in this edge-ordered complete graph the two four-sets `S` and `(S-\{s\})\cup\{L\}` would both have no increasing Hamilton path and would meet in the three-set `S-\{s\}`. Lemma 2.4 of the proof spine would then give an increasing Hamilton path on all five vertices, a contradiction. Thus `(S-\{s\})\cup\{L\}` is Hamiltonian. The same argument applies with `R`.

Apply `TOOLKIT/LOCAL_HAMILTON_EXTENSIONS.md` Section 2 to the six-set `S\cup\{L,R\}`. At least four of its five-subsets are Hamiltonian. The two obtained by deleting `L` or `R` are `S\cup\{R\}` and `S\cup\{L\}`, which are non-Hamiltonian. Therefore all four sets `(S-\{s\})\cup\{L,R\}` are Hamiltonian.

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

The following three propositions are stated for an arbitrary Hamilton path with five-vertex complement. They are included here because deleting one endpoint of the codimension-four path `P` produces exactly this situation in the same ambient boundary tournament.

### Proposition 3.1

Let `K` be a boundary tournament with `pc(K)>2`, let `Y=(y_0,...,y_m)` be a Hamilton tight path with `m>=1`, and put `U=V(K)-V(Y)`. If `|U|=5`, then there exist distinct `u,v∈U` such that, for each `w∈{u,v}`, the three induced boundary tournaments
`K[U-{w}]`, `K[(U-{w})∪{y_0}]`, and `K[(U-{w})∪{y_m}]`
are Hamiltonian. Consequently, if `A_w^-` and `A_w^+` are Hamilton paths of the latter two induced subtournaments, then
`A_w^- | (w) | (y_1,...,y_m)`
and
`(y_0,...,y_{m-1}) | (w) | A_w^+`
are spanning three-path covers of `K`.

**Proof.**
As above, `K[U]` is non-Hamiltonian, so Lemma 2.7 gives a set
`A_0={w∈U:K[U-{w}] is Hamiltonian}`
with `|A_0|>=4`.

The induced subtournaments on `U∪{y_0}` and `U∪{y_m}` are non-Hamiltonian, since a Hamilton path on either set together with the complementary inherited suffix or prefix of `Y` would two-cover `K`. Each six-set has at least four Hamiltonian five-subsets, while its five-subset `U` is non-Hamiltonian. Hence
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

The three preceding propositions apply directly in `K` to the endpoint truncations `P_L=(x_1,\ldots,x_{m-1})` and `P_R=(x_0,\ldots,x_{m-2})`, whose complements are `S\cup\{L\}` and `S\cup\{R\}`, respectively, whenever their stated path-length hypotheses hold.

**Proof.**
Both truncations are inherited Hamilton tight paths on their vertex sets, and their vertex complements in the same ambient tournament `K` are exactly the two displayed five-sets. ∎
