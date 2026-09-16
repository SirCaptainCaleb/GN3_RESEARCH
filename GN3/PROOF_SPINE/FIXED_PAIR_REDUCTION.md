# Fixed-pair reduction

Let `H` satisfy the conclusions of `PRELIMINARIES.md`. Fix distinct vertices `a,c` and put

`X={x:(a,x,c) is tight}`,  
`Y={x:(c,x,a) is tight}`.

For `x∈X`, write

`L_x=(a,x)`, `R_x=(x,c)`.

For `x∈Y`, write

`L_x=(c,x)`, `R_x=(x,a)`.

Thus `L_x` and `R_x` are two-vertex tight paths, and the corresponding tight ordered triple through `a,c` extends each of them at the end containing `x`.

## 1. Two local lemmas

### Lemma 1.1 — prescribed endpoints for two disjoint two-vertex paths

Let `D_1,D_2` be vertex-disjoint two-vertex tight paths whose specified end extensions have opposite orientation. For arbitrary prescribed vertices

`x∈V(D_1)`, `y∈V(D_2)`,

there is a finite sequence of path systems ending either in a spanning two-path cover of `H` or in a path system whose two distinguished paths are the singletons `(x)` and `(y)`.

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

Let `s,t∈X` be distinct. Then there is a finite sequence `Σ_{s,t}` of path systems such that either `H` acquires a spanning two-path cover or the last distinguished paths are `(a)` and `(c)`, and within that sequence Lemma 1.2 yields the singleton paths `(s)` from `L_s=(a,s)` and `(t)` from `R_t=(t,c)`.

The same conclusion holds with `s,t` interchanged. The corresponding statement for two vertices of `Y` is obtained by interchanging `a,c`.

### Proof

The paths `L_s=(a,s)` and `R_t=(t,c)` are disjoint. The triples `(a,s,c)` and `(a,t,c)` extend them at opposite ends. Apply Lemma 1.1 with prescribed endpoints `a∈L_s` and `c∈R_t`.

If the first outcome of Lemma 1.1 occurs, `H` has a spanning two-path cover. Otherwise the terminal distinguished paths are `(a)` and `(c)`.

Apply the reversed form of Lemma 1.2 to `L_s=(a,s)` with the singleton path `(a)`. The end protected by the tight triple `(a,s,c)` is `s`, while `(a)` meets `L_s` only at the other end. Hence the remaining nonempty subpath is `(s)`.

Apply the corresponding form of Lemma 1.2 to `R_t=(t,c)` with `(c)`. The remaining nonempty subpath is `(t)`.

Interchanging `s,t` gives the second sequence. The case `s,t∈Y` is symmetric. ∎

## 3. The set `C_{a,c}`

Concatenate finitely many sequences of Lemma 2.1, always choosing the branch ending with the singleton pair `(a),(c)` unless a spanning two-path cover has already appeared. For such a concatenated sequence `Σ`, define `C_{a,c}(Σ)` to be the set of vertices `x∈V(H)-{a,c}` for which both of the following applications of Lemma 1.2 occur in `Σ`:

- the singleton at the outer vertex of `L_x` leaves the one-vertex path `(x)`;
- the singleton at the outer vertex of `R_x` leaves the one-vertex path `(x)`.

### Theorem 3.1

There is a finite sequence `Σ` such that either `H` has a spanning two-path cover or

`|V(H)-({a,c}∪C_{a,c}(Σ))|≤1`.

### Proof

Consider `X`. If `|X|≤1`, do nothing. If `|X|≥2`, choose `t∈X`. For each `s∈X-{t}`, apply Lemma 2.1 first to `(s,t)` and then to `(t,s)`. Unless a spanning two-path cover appears, these two applications put both `s` and `t` in `C_{a,c}(Σ)`. Repeating with the same `t` puts every vertex of `X` in `C_{a,c}(Σ)`.

Apply the same construction to `Y` with `a,c` interchanged. A class of order zero or one can leave at most one vertex outside `C_{a,c}(Σ)`. Since

`|X|+|Y|=|V(H)|-2≥9`,

both classes cannot have order at most one. Hence at most one vertex outside `{a,c}` is absent from `C_{a,c}(Σ)`. ∎

### Corollary 3.2

Let `D_1,D_2` be vertex-disjoint two-vertex paths on four distinct vertices appearing after the sequence `Σ` of Theorem 3.1. Then at least one of the four vertices belongs to `C_{a,c}(Σ)`.

### Proof

The complement of `C_{a,c}(Σ)` is contained in `{a,c}` together with at most one additional vertex, and therefore has order at most three. ∎

## 4. Contact through a vertex of `C_{a,c}`

### Proposition 4.1

Let `s∈C_{a,c}(Σ)∩X`, and let `Q=(s,u)` or `(u,s)` be a later two-vertex tight path with

`u∉{a,c}`.

Then Lemma 1.2, applied to `Q` and one of the fixed paths `L_s=(a,s)` or `R_s=(s,c)`, gives at least one of the following:

1. a tight path properly containing one of those two paths;
2. a tight path properly containing `Q`;
3. a vertex-simple proper tight cycle;
4. a reversed tight ordered triple containing `u`.

Consequently the only two-vertex supports through `s` not covered by this conclusion are

`{a,s}` and `{s,c}`.

### Proof

If `Q` has second endpoint outside `{a,c}`, then `Q` is not equal to either `L_s` or `R_s`. Since `s∈C_{a,c}(Σ)`, both endpoint contacts at `s` have occurred in `Σ`, and the fixed tight triple `(a,s,c)` supplies the required end extension for both `L_s` and `R_s`. Apply Lemma 1.2 at `s`. The exceptional singleton case is impossible because `Q` has two vertices. Every nonexceptional outcome listed in Lemma 1.2 contains the new endpoint `u` either in the extended path, the cycle, or the reversed ordered triple. ∎

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

For the sequence `Σ` of Theorem 3.1, unless `H` already has a spanning two-path cover, there exist distinct `x,y,z∈C_{a,c}(Σ)` such that either

`(x,a,y,c,z)`

or

`(x,c,y,a,z)`

is a tight path.

### Proof

One of `X,Y` has order at least five. At most one vertex outside `{a,c}` is absent from `C_{a,c}(Σ)`, so that larger class contains at least four vertices of `C_{a,c}(Σ)`. Apply Lemma 5.1, interchanging `a,c` if necessary. ∎