# Fixed-pair reduction

Let `H` satisfy the conclusions of `PRELIMINARIES.md`. Fix distinct vertices `a,c` and put

`X={x:(a,x,c) is tight}`,  
`Y={x:(c,x,a) is tight}`.

For `x∈X`, write

`L_x=(a,x)`, `R_x=(x,c)`.

For `x∈Y`, write

`L_x=(c,x)`, `R_x=(x,a)`.

Thus `L_x` and `R_x` are two-vertex tight paths. In each case the tight ordered triple through `a,c` extends `L_x` at its `x`-end and extends `R_x` at its `x`-end.

A **path system** is a family of pairwise vertex-disjoint tight paths.

An **end-extension certificate** is a named tight path `P=(v_0,...,v_k)` together with a named vertex `w∉V(P)` such that either

`(w,v_0,...,v_k)`

or

`(v_0,...,v_k,w)`

is tight. In the first case the protected end of `P` is `v_0`; in the second it is `v_k`.

A **configuration** consists of a current path system together with a set of named end-extension certificates and named conclusions previously obtained from Lemma 1.2. The certified paths need not belong to the current path system. They remain available as graph-theoretic objects in later applications of Lemma 1.2.

We use two established continuation operations.

1. **Endpoint selection.** Suppose the configuration contains end-extension certificates for two vertex-disjoint two-vertex paths `D_1,D_2`, one protected at its left end and the other at its right end. For either prescribed vertex `x∈V(D_1)`, there is a continuation ending either in a spanning two-path cover of `H` or in a configuration whose current path system contains singleton paths `(x)` and `(q)` for some vertex `q`. Every certificate already present remains present.
2. **Singleton replacement.** Suppose the current path system contains singleton paths `(x)` and `(q)`. For any prescribed vertex `y∉{x,q}`, there is a continuation ending either in a spanning two-path cover of `H` or in a configuration whose current path system contains singleton paths `(x)` and `(y)`. Every certificate already present remains present.

A **certificate-preserving lawful continuation** is a sequence of configurations obtained by these two operations, with any applications of Lemma 1.2 added to the certificate set. Thus a path that was used earlier may disappear from the current path system without disappearing from the hypotheses available to later contact arguments.

Initially we retain the end-extension certificates supplied by all of the tight triples through `a,c`; in particular every `L_x,R_x` above remains available throughout every certificate-preserving lawful continuation.

## 1. Two local lemmas

### Lemma 1.1 — prescribed endpoints for two disjoint two-vertex paths

Let a configuration contain end-extension certificates for vertex-disjoint two-vertex tight paths `D_1,D_2`, one protected at its left end and the other at its right end. For arbitrary prescribed vertices

`x∈V(D_1)`, `y∈V(D_2)`,

there is a certificate-preserving lawful continuation ending either in a spanning two-path cover of `H` or in a configuration whose current path system contains `(x)` and `(y)`.

### Proof

Apply endpoint selection to `D_1`, prescribing `x`. If a spanning two-path cover appears, stop. Otherwise the current path system contains `(x)` and some singleton `(q)`.

If `q=y`, stop. Otherwise apply singleton replacement with `(x)` fixed and target `y`. This gives either a spanning two-path cover or the singleton pair `(x),(y)`. All incoming certificates, including those of `D_1,D_2`, persist through both operations. ∎

### Lemma 1.2 — contact with an end-extended path

Let

`P=(v_0,...,v_k)`

be a tight path and let `w∉V(P)` be such that

`(w,v_0,...,v_k)`

is tight. Let `Q` be a proper tight path meeting `P`.

If `Q` avoids `v_0`, let

`i=min{j:v_j∈V(Q)}`.

Then

`P'=(v_0,...,v_{i-1})`

is a nonempty proper subpath of `P`, is disjoint from `Q`, and `(w,P')` is tight.

If `Q` contains `v_0`, then either `P=Q=(v_0)` or at least one of the following occurs:

1. a tight path properly containing `P`;
2. a tight path properly containing `Q`;
3. a vertex-simple proper tight cycle;
4. a reversed tight ordered triple joining an edge of one path to the other.

The statement obtained by reversing all path orders is also valid.

### Proof

Assume first that `Q` avoids `v_0`. The definition of `i` gives `i≥1`; hence `P'` is nonempty and disjoint from `Q`. Since

`(w,v_0,...,v_{i-1})`

is an initial segment of `(w,P)`, it is tight.

Now suppose `Q` contains `v_0`. If `k=0`, either `Q=(v_0)` or `Q` properly contains `P`. Assume `k≥1`.

Compare the orders in which the common vertices of `P` and `Q` occur. If some pair of consecutive common vertices occurs in opposite order, take a shortest subpath of `Q` joining such a reversed pair. If it consists of one edge, that edge reverses an edge of `P`. Otherwise test the two ordered triples where this subpath meets `P`. A failed test gives, by boundary antisymmetry, a reversed tight ordered triple; if both tests are tight, the subpath of `Q` together with the corresponding segment of `P` forms a vertex-simple tight cycle.

We may therefore assume that the common vertices occur in the same order on `P` and `Q`, so `v_0` is the first common vertex along `Q`.

If `Q` has a predecessor `u` immediately before `v_0`, test `(u,v_0,v_1)`. If it is tight, the initial segment of `Q` ending at `v_0` followed by `P` properly contains `P`; otherwise boundary antisymmetry gives `(v_1,v_0,u)` tight.

Suppose instead that `v_0` is the first vertex of `Q`. If `Q=(v_0)`, the path `(w,v_0)` properly contains `Q`. Otherwise write `Q=(v_0,q_1,...)`. If `w∉V(Q)`, test `(w,v_0,q_1)`. Tightness gives the proper extension `(w,Q)`; failure gives `(q_1,v_0,w)` tight. If `w∈V(Q)`, the paths `(w,P)` and `Q` contain `w,v_0` in opposite orders, so the preceding reversed-pair argument gives a reversed tight ordered triple or a proper tight cycle. ∎

## 2. Two vertices of the same orientation

### Lemma 2.1

Let `s,t∈X` be distinct. There is a certificate-preserving lawful continuation such that either a spanning two-path cover of `H` occurs or the terminal current path system contains `(a)` and `(c)` and the certificate set contains both conclusions

- contact of the retained path `L_s=(a,s)` with `(a)` leaves the singleton `(s)`;
- contact of the retained path `R_t=(t,c)` with `(c)` leaves the singleton `(t)`.

The same conclusion holds with `s,t` interchanged. The corresponding statement for two vertices of `Y` is obtained by interchanging `a,c`.

### Proof

The paths `L_s=(a,s)` and `R_t=(t,c)` are disjoint. Their source triples give end-extension certificates protected at `s` and `t`, respectively. Apply Lemma 1.1 with prescribed endpoints `a∈L_s` and `c∈R_t`.

If a spanning two-path cover occurs, stop. Otherwise the current path system contains `(a)` and `(c)`, while the end-extension certificates for `L_s,R_t` remain available.

Apply the reversed form of Lemma 1.2 to the retained path `L_s=(a,s)` and the current singleton `(a)`. Since the protected end is `s`, the remaining nonempty subpath is `(s)`. Add this conclusion to the certificate set.

Apply the corresponding form of Lemma 1.2 to the retained path `R_t=(t,c)` and the current singleton `(c)`. The remaining nonempty subpath is `(t)`. Add this conclusion as well.

Interchanging `s,t` gives the second continuation. The case `s,t∈Y` is symmetric. ∎

## 3. The set `C_{a,c}`

For `x∈X`, call the two conclusions

- `L_x=(a,x)` contacted by `(a)` leaves `(x)`;
- `R_x=(x,c)` contacted by `(c)` leaves `(x)`

the two **source reductions at `x`**. For `x∈Y`, define the source reductions analogously with `a,c` interchanged.

For a certificate-preserving lawful continuation `Σ`, define `C_{a,c}(Σ)` to be the set of vertices `x∈V(H)-{a,c}` for which both source reductions at `x` occur in the certificate set of the terminal configuration of `Σ`.

### Theorem 3.1

There is a certificate-preserving lawful continuation `Σ` such that either a spanning two-path cover of `H` occurs or

`|V(H)-({a,c}∪C_{a,c}(Σ))|≤1`.

### Proof

Consider `X`. If `|X|≤1`, do nothing. If `|X|≥2`, choose `t∈X`. For each `s∈X-{t}`, apply Lemma 2.1 first to `(s,t)` and then to `(t,s)`, concatenating the two lawful continuations at their common terminal singleton pair `(a),(c)`. Unless a spanning two-path cover appears, these two applications add both source reductions at `s` and at `t` to the certificate set. Repeating with the same `t` puts every vertex of `X` in `C_{a,c}(Σ)`.

Apply the same construction to `Y` with `a,c` interchanged. A class of order zero or one can leave at most one vertex outside `C_{a,c}(Σ)`. Since

`|X|+|Y|=|V(H)|-2≥9`,

both classes cannot have order at most one. Hence at most one vertex outside `{a,c}` is absent from `C_{a,c}(Σ)`. ∎

### Corollary 3.2

Let `Σ'` be any certificate-preserving lawful continuation extending the continuation `Σ` of Theorem 3.1. If a current path system occurring in `Σ'` contains two vertex-disjoint two-vertex paths `D_1,D_2` on four distinct vertices, then at least one of those four vertices belongs to `C_{a,c}(Σ)`.

### Proof

The complement of `C_{a,c}(Σ)` is contained in `{a,c}` together with at most one additional vertex, and therefore has order at most three. ∎

## 4. Contact with a new endpoint

### Proposition 4.1

Let `s∈X`, and let `Σ'` be a certificate-preserving lawful continuation from the fixed-pair source configuration. Suppose a current path system occurring in `Σ'` contains a two-vertex tight path

`Q=(s,u)` or `Q=(u,s)`

with `u∉{a,c}`. Then contact of `Q` with one of the retained source paths `L_s=(a,s)` or `R_s=(s,c)` gives at least one of the following:

1. a tight path properly containing one of `L_s,R_s`;
2. a tight path properly containing `Q`;
3. a vertex-simple proper tight cycle;
4. a reversed tight ordered triple containing `u`.

Consequently the only two-vertex supports through `s` not covered by this conclusion are

`{a,s}` and `{s,c}`.

### Proof

The initial configuration contains end-extension certificates for both source paths `L_s,R_s`, and certificate preservation keeps them available throughout `Σ'`. Since `u∉{a,c}`, the path `Q` is neither `L_s` nor `R_s`. Apply Lemma 1.2 at their common vertex `s`. The exceptional singleton case is impossible because `Q` has two vertices. Every remaining outcome contains `u` in the extended path, the cycle, or the reversed ordered triple. ∎

If in addition `s∈C_{a,c}(Σ)` for the continuation of Theorem 3.1, then the certificate set also contains both source reductions at `s`. Those two earlier reductions are not needed for Proposition 4.1 itself; their role is to constrain a later recurrence on the two exceptional supports `{a,s}` and `{s,c}`.

## 5. Four vertices of one orientation

### Lemma 5.1

Let `S` be a set of four vertices disjoint from `{a,c}` such that

`(a,s,c)`

is tight for every `s∈S`. Then there exist distinct `x,y,z∈S` such that

`(x,a,y,c,z)`

is a tight path.

### Proof

Define tournaments `A` and `C` on `S` by

`x→_A y` iff `(x,a,y)` is tight,

`x→_C y` iff `(x,c,y)` is tight.

Suppose there are no distinct `x,y,z` with `x→_A y→_C z`. Any vertex with `A`-indegree at least two must then have `C`-outdegree zero. Since the total `A`-indegree is six, some vertex `y` has `A`-indegree at least two, so `y` is the `C`-sink. Every other vertex has positive `C`-outdegree and hence `A`-indegree at most one. The total indegree count forces `y` to have `A`-indegree three and each other vertex to have `A`-indegree one, so `y` is also the `A`-sink.

Choose `v≠y`. Since `y` is the `C`-sink, `v→_C y`. The unique `A`-predecessor of `v` cannot be a vertex `x≠y`, since then `x→_A v→_C y`; hence it is `y`, contradicting that `y` is the `A`-sink.

Thus there are distinct `x,y,z` with `x→_A y→_C z`. The triples `(x,a,y)`, `(a,y,c)`, `(y,c,z)` are tight, so `(x,a,y,c,z)` is a tight path. ∎

### Corollary 5.2

For the continuation `Σ` of Theorem 3.1, unless `H` already has a spanning two-path cover, there exist distinct `x,y,z∈C_{a,c}(Σ)` such that either

`(x,a,y,c,z)`

or

`(x,c,y,a,z)`

is a tight path.

### Proof

One of `X,Y` has order at least five. At most one vertex outside `{a,c}` is absent from `C_{a,c}(Σ)`, so that larger class contains at least four vertices of `C_{a,c}(Σ)`. Apply Lemma 5.1, interchanging `a,c` if necessary. ∎