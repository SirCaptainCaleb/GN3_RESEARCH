# Local Hamilton extension lemmas

Throughout this file, `H` is an arbitrary boundary tournament.

## 1. Bad extension pairs around a tight three-vertex path form a triangle-free graph

Let `P` be a tight path on three vertices, and let `X` be a set of `m>=3` vertices disjoint from `V(P)`. Define a graph `B_P(X)` on vertex set `X` by joining distinct `x,y` exactly when

`H[V(P) union {x,y}]`

has no Hamilton tight path.

Then `B_P(X)` is triangle-free. Consequently

`|E(B_P(X))| <= floor(m^2/4)`,

so at least

`binom(m,2)-floor(m^2/4)`

pairs `{x,y}` extend `P` to a Hamilton five-vertex induced subgraph. Equality in the upper bound occurs exactly when `B_P(X)` is a complete bipartite graph with part sizes `floor(m/2)` and `ceil(m/2)`.

**Proof.** For any three distinct `x,y,z in X`, `SMALL_ORDER_HAMILTONICITY.md` Section 5 says that at least one of

`V(P) union {x,y}`, `V(P) union {x,z}`, `V(P) union {y,z}`

has a Hamilton tight path. Hence `xy,xz,yz` cannot all be edges of `B_P(X)`, so the graph is triangle-free. Mantel's theorem gives the bound and its equality case. ∎

## 2. Density of Hamilton five-sets through a fixed small subset

Let `W` be an `r`-vertex subset of a boundary tournament, where `r>=6`, and let `S subseteq W` have order `s in {0,1,2,3}`. Let `h_5(W;S)` be the number of five-element sets `F` satisfying

`S subseteq F subseteq W`

for which `H[F]` has a Hamilton tight path. Then

`h_5(W;S) >= ((4-s)/(6-s)) binom(r-s,5-s)`.

Thus at least two-thirds of all five-subsets of `W` are Hamiltonian; among the five-subsets containing a prescribed vertex, pair, or triple, the corresponding proportions are at least `3/5`, `1/2`, and `1/3`.

**Proof.** Count pairs `(U,F)` such that

`S subseteq F subset U subseteq W`, `|F|=5`, `|U|=6`,

and `H[F]` is Hamiltonian.

There are `binom(r-s,6-s)` possible six-sets `U`. By `SMALL_ORDER_HAMILTONICITY.md` Section 6, each `U` has at least four Hamiltonian five-subsets. At most `s` of those can fail to contain all of `S`, because a five-subset of `U` is obtained by deleting one vertex. Hence each `U` contributes at least `4-s` admissible pairs.

On the other hand, each Hamiltonian five-set `F` containing `S` lies in exactly `r-5` six-subsets of `W`. Therefore

`(r-5) h_5(W;S) >= (4-s) binom(r-s,6-s)`.

Using

`binom(r-s,6-s)/(r-5)=binom(r-s,5-s)/(6-s)`

gives the claimed bound. ∎

For the stronger Johnson-degree density hierarchy, which improves these fixed-subset bounds for every `r>10`, see `JOHNSON_DENSITY.md` Section 4.

## 3. Two parallel middle vertices force a Hamilton four-path

Let `a,c,x,y` be four distinct vertices of a boundary tournament. If

`(a,x,c)` and `(a,y,c)`

are tight, then at least one of

`(a,x,c,y)`, `(a,y,c,x)`

is a tight Hamilton path on `{a,c,x,y}`.

**Proof.** Exactly one of `(x,c,y)` and `(y,c,x)` is tight. In the first case `(a,x,c,y)` is tight; in the second `(a,y,c,x)` is tight. ∎
