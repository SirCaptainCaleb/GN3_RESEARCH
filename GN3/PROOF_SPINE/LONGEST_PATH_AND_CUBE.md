# Longest paths and the three-vertex cube

Let `H` satisfy the conclusions of `PRELIMINARIES.md`.

## 1. Terminal three-path covers

Let

`A=(a_0,...,a_s)`, `X=(x_0,...,x_m)`

be two members of a spanning three-path cover. If `X` is nontrivial, the endpoint `x_0` is **transferable to the right end of `A`** when

`(a_{s-1},a_s,x_0)`

is tight: replace `A` by `(a_0,...,a_s,x_0)` and replace `X` by `(x_1,...,x_m)`. Define transfer of `x_m` to the left end of `A` symmetrically.

### Lemma 1.1 — terminal three-path lemma

Let

`A|B|C`

be a spanning three-path cover of `H`. Suppose `A` has maximum order among `A,B,C`, and no endpoint of a nontrivial path among `B,C` is transferable to either end of `A`.

Then `|A|≥3`, and one of the following holds.

1. `|A|≥4`, and there is a nontrivial path `X=(x_0,...,x_m)` among `B,C` such that, writing `A=(a_0,...,a_s)`,
   
   `(x_0,a_s,a_{s-1})` and `(a_1,a_0,x_m)`
   
   are tight. The ordered pairs `(a_s,a_{s-1})` and `(a_1,a_0)` are disjoint.
2. `|A|=3`, say `A=(a_0,a_1,a_2)`, and there is an exact two-path cover of `H-a_1` containing an edge `xy` whose endpoints lie in two distinct members of
   
   `(a_0)|(a_2)|B|C`;
   
   exactly one of `(a_1,x,y)` and `(y,x,a_1)` is tight.

### Proof

If `|A|=1`, then all three paths are singletons, contradicting `|V(H)|>10`.

Suppose `|A|=2`, say `A=(a_0,a_1)`. Since `A` is longest among the three paths, `B` and `C` have order at most two. If one of them is nontrivial, say `X=(x_0,x_1)`, then neither endpoint can be transferred into `A`. Hence

`(a_0,a_1,x_0)` and `(x_1,a_0,a_1)`

are both not tight. Boundary antisymmetry gives

`(x_0,a_1,a_0)` and `(a_1,a_0,x_1)`

tight, so `(x_0,a_1,a_0,x_1)` is a tight four-vertex path; together with the third path it gives a spanning two-path cover, a contradiction. If both `B,C` are singletons, their two vertices form a tight two-vertex path, which together with `A` again gives a spanning two-path cover. Thus `|A|≥3`.

Assume `|A|≥4`. At least one of `B,C` is nontrivial, since otherwise their two singleton vertices form a tight two-vertex path which, together with `A`, two-covers `H`. Choose a nontrivial path

`X=(x_0,...,x_m)`

among `B,C`. Since `x_0` is not transferable to the right end of `A`,

`(a_{s-1},a_s,x_0)`

is not tight, so `(x_0,a_s,a_{s-1})` is tight. Since `x_m` is not transferable to the left end,

`(x_m,a_0,a_1)`

is not tight, so `(a_1,a_0,x_m)` is tight. The two end pairs of `A` are disjoint because `|A|≥4`. This is outcome 1.

Now assume `|A|=3`, so `A=(a_0,a_1,a_2)`. The four paths

`(a_0)|(a_2)|B|C`

cover `H-a_1`. By minimality, `H-a_1` has a cover by at most two tight paths. It cannot be Hamiltonian, since a Hamilton path together with `(a_1)` would two-cover `H`. Thus it has an exact two-path cover `P|Q`.

Some edge of `P|Q` joins two distinct components of `(a_0)|(a_2)|B|C`; otherwise each of `P,Q` would lie in one component of that four-path cover and could not cover all four nonempty components. Let `xy` be such an edge. Boundary antisymmetry makes exactly one of `(a_1,x,y)` and `(y,x,a_1)` tight. This is outcome 2. ∎

### Theorem 1.2 — globally longest path

There is a spanning three-path cover

`A|B|C`

such that `A` is a globally longest tight path and the conclusion of Lemma 1.1 holds.

### Proof

Choose a globally longest tight path `A`. It is proper, since a Hamilton tight path would contradict `pc(H)=3`. By minimality, `H-V(A)` has a cover by at most two tight paths. It cannot be Hamiltonian, since a Hamilton path of `H-V(A)` together with `A` would form a spanning two-path cover of `H`. Hence

`H-V(A)=B|C`

is an exact two-path cover.

The path `A` is longest among `A,B,C`. Any endpoint transfer from `B` or `C` into `A` would produce a tight path longer than `A`, contradicting global maximality. Lemma 1.1 therefore applies. ∎

## 2. Three internal vertices with the same orientation

Fix distinct vertices `a,c` and an exact two-path cover

`H-{a,c}=U|V`.

By Proposition 5.1 of `PRELIMINARIES.md`, there are internal vertices `p,q,r` having the same orientation through `{a,c}`. Interchanging `a,c` if necessary, assume

`(a,p,c)`, `(a,q,c)`, `(a,r,c)`

are tight.

Put

`P={p,q,r}`,  
`K={a,c,p,q,r}`,  
`W=V(H)-K`.

### Lemma 2.1

The set `K` has a Hamilton tight path. More generally, for every `J⊆P`, the set

`K-J={a,c}∪(P-J)`

has a Hamilton tight path.

### Proof

For distinct `x,y∈P`, write

`x→_a y` iff `(x,a,y)` is tight,

`x→_c y` iff `(x,c,y)` is tight.

Each relation is a tournament on `P`.

If distinct `x,y,z` satisfy `x→_a y→_c z`, then `(x,a,y,c,z)` is a Hamilton tight path on `K`. Suppose no such triple exists.

The tournament `→_a` cannot be transitive. If `x→_a y→_a z` and `x→_a z`, then absence of the paths `(x,a,y,c,z)` and `(x,a,z,c,y)` forces both `z→_c y` and `y→_c z`, impossible. Hence, after relabelling,

`p→_a q→_a r→_a p`.

Avoiding the three mixed-chain Hamilton paths forces

`r→_c q`, `p→_c r`, `q→_c p`.

Still assuming that `K` has no Hamilton tight path, inspect the following six words. In each row the first two consecutive triples are already tight, so the third must be non-tight; boundary antisymmetry then gives the displayed reversal.

| word | forced tight triple |
| --- | --- |
| `a p c r q` | `(q,r,c)` |
| `a q c p r` | `(r,p,c)` |
| `a r c q p` | `(p,q,c)` |
| `p q a r c` | `(a,q,p)` |
| `q r a p c` | `(a,r,q)` |
| `r p a q c` | `(a,p,r)` |

Using these six new tight triples, apply the same argument to another six words:

| word | forced tight triple |
| --- | --- |
| `a p r c q` | `(c,r,p)` |
| `a q p c r` | `(c,p,q)` |
| `a r q c p` | `(c,q,r)` |
| `p a q r c` | `(r,q,a)` |
| `q a r p c` | `(p,r,a)` |
| `r a p q c` | `(q,p,a)` |

Only the orientations of the three triples on `{p,q,r}` remain to be used. Put

`u=1` iff `(q,p,r)` is tight,  
`v=1` iff `(p,q,r)` is tight,  
`w=1` iff `(p,r,q)` is tight.

When one of `u,v,w` is zero, boundary antisymmetry supplies the complete reversal of the corresponding triple. For each of the eight values of `(u,v,w)`, the two candidate words below have every consecutive triple certified except for the displayed pair of complete reversals.

| `(u,v,w)` | first candidate | second candidate | remaining reversal pair |
| --- | --- | --- | --- |
| `000` | `a c q r p` | `r p q c a` | `(a,c,q)` / `(q,c,a)` |
| `100` | `c a r q p` | `q p r a c` | `(c,a,r)` / `(r,a,c)` |
| `010` | `a c p q r` | `q r p c a` | `(a,c,p)` / `(p,c,a)` |
| `110` | `a c p q r` | `q r p c a` | `(a,c,p)` / `(p,c,a)` |
| `001` | `c a p r q` | `r q p a c` | `(c,a,p)` / `(p,a,c)` |
| `101` | `c a p r q` | `r q p a c` | `(c,a,p)` / `(p,a,c)` |
| `011` | `a c r p q` | `p q r c a` | `(a,c,r)` / `(r,c,a)` |
| `111` | `c a q p r` | `p r q a c` | `(c,a,q)` / `(q,a,c)` |

In each row boundary antisymmetry makes exactly one triple in the last column tight. The corresponding candidate word is therefore a Hamilton tight path on `K`, contradicting the assumption. Hence `K` is Hamiltonian.

If `|P-J|=0`, the set `K-J={a,c}` is a two-vertex tight path. If `|P-J|=1`, the required path is `(a,s,c)`. If `P-J={s,t}`, then either `(s,c,t)` is tight and `(a,s,c,t)` is a tight path, or `(t,c,s)` is tight and `(a,t,c,s)` is a tight path. ∎

For `J⊆P`, put

`G_J=H[W∪J]`.

### Proposition 2.2

`pc(G_J)=2` for every `J⊆P`.

### Proof

If `G_J` had a Hamilton tight path, that path together with a Hamilton tight path on `K-J` from Lemma 2.1 would form a spanning two-path cover of `H`. Since `G_J` is proper, minimality gives `pc(G_J)≤2`; hence `pc(G_J)=2`. ∎

Every exact two-path cover of `G_J`, together with a Hamilton tight path on `K-J`, is a spanning three-path cover of `H`. Since `pc(H)=3`, it is a spanning path forest with the maximum possible number `|V(H)|-3` of edges among spanning forests whose components are tight paths.

## 3. Comparing the eight induced subgraphs

### Lemma 3.1 — two different Hamilton orders

Let

`P_0=(v_0,...,v_k)`

and `Q_0` be vertex-simple tight paths on the same vertex set. If their vertex orders differ, then at least one of the following exists:

1. an edge of `Q_0` reversing a consecutive edge of `P_0`;
2. a tight ordered triple crossing one of the two paths in the reverse direction;
3. a vertex-simple proper tight cycle.

### Proof

Read the vertices of `P_0` in their order along `Q_0`. Choose two consecutive common vertices `v_i,v_j` along `Q_0` with `i>j`, and let `E` be the subpath of `Q_0` from `v_i` to `v_j`; its internal vertices contain no vertex of `P_0`.

If `E` is the edge `v_i v_j` with `i=j+1`, outcome 1 holds. Otherwise let `x` be the successor of `v_i` on `E` and `y` the predecessor of `v_j`. Test

`(v_{i-1},v_i,x)` and `(y,v_j,v_{j+1})`.

If either triple is not tight, boundary antisymmetry gives the corresponding reversed tight ordered triple. If both are tight, traverse `E` from `v_i` to `v_j`, then follow `P_0` from `v_j` to `v_{i-1}` and close through the first tested triple. The resulting tight cycle is vertex-simple because `v_i,v_j` were consecutive common vertices along `Q_0`. ∎

### Theorem 3.2

The family of exact two-path covers of the eight graphs `G_J`, `J⊆P`, determines either a proper tight path in `H` or a vertex-simple proper tight cycle together with an edge at which the cycle may be opened into a proper tight path.

### Proof

Fix a nonempty `J⊆P` and an exact two-path cover `T_J` of `G_J`. Delete the vertices of `J` from the two paths of `T_J` and split at the deleted vertices. Let the maximal nonempty subpaths contained in `W` be

`R_1,...,R_m`.

We have `m≥2`: otherwise `W` has a Hamilton tight path, which together with a Hamilton tight path on `K` would two-cover `H`.

Suppose `m≥3`. Compare `R_1|...|R_m` with an exact two-path cover of `W`. Some edge `xy` of the latter joins two distinct paths `R_i,R_j`. If one of these paths is nontrivial, let `h` be a neighbor of the corresponding endpoint, say `x`, on that path. Boundary antisymmetry on `h,x,y` gives a proper tight three-vertex path. If both crossed paths are singletons, at least one of them has a neighbor in `J` in `T_J`; otherwise those two singleton paths would already be the two components of `T_J`, leaving no place for a third nonempty `R_k`. Using that neighbor in place of `h` gives the same conclusion.

Hence assume every deletion leaves exactly two nonempty subpaths of `W`.

For `s∈P`, choose an exact two-path cover of `G_{\{s\}}`. The vertex `s` cannot itself be one path component, because deleting it would leave a Hamilton path of `W`, contrary to Proposition 2.2. Hence `s` is an endpoint, and deleting it leaves an exact two-path cover `F_s` of `W`.

Compare `F_p,F_q,F_r`. If two induce different unordered partitions of `W` into path vertex sets, an edge of one cover crosses the two path vertex sets of the other. Since `|W|=|V(H)|-5≥6`, both crossed path vertex sets cannot be singletons. Choose a crossing endpoint on a nontrivial path and its neighbor on that path; boundary antisymmetry gives a proper tight three-vertex path.

If the unordered partitions agree but one common vertex set is traversed in two different orders, Lemma 3.1 gives a reversed edge, a reversed tight ordered triple, or a proper tight cycle.

We may therefore assume, after exchanging the two paths when necessary, that

`F_p=F_q=F_r=F=A|B`

as ordered path covers. For each `s∈P`, let `e_s` be the endpoint of `F` adjacent to `s` in the chosen exact cover of `G_{\{s\}}`.

Now fix distinct `s,t∈P` and an exact two-path cover `T_{st}` of `G_{\{s,t\}}`.

If `s` or `t` is internal on its path, deleting that vertex gives a three-path cover of the corresponding one-vertex extension of `W`. Compare it with the exact two-path cover already chosen there. A crossing edge yields a proper tight path as above. If both crossed pieces are singleton pieces created by deleting the internal vertex, one of the two edges incident with that deleted vertex supplies the neighboring edge needed for the boundary-antisymmetry argument.

Hence assume both `s,t` are endpoints. Neither is an entire singleton path, since deleting such a singleton would leave a Hamilton path of the corresponding one-vertex extension of `W`, contrary to Proposition 2.2.

Deleting `s` or `t` from `T_{st}` therefore leaves exact two-path covers. If either differs in support or order from the chosen one-vertex cover, the preceding arguments already give the conclusion. Otherwise

`T_{st}-s=F_t`,  
`T_{st}-t=F_s`.

Thus the two edges incident with `s,t` are exactly

`s e_s`, `t e_t`.

A two-path forest on `|W|+2` vertices has `|W|` edges, while `F` has `|W|-2` edges. Hence

`E(T_{st})=E(F)∪{s e_s,t e_t}`.

Two vertices of `P` cannot attach to the same endpoint of a nontrivial path of `F`, since that endpoint would have degree three in `T_{st}`. Thus a common attachment point can only be an isolated singleton path `(v)` of `F`, in which case the corresponding three vertices form a tight three-vertex path.

Adjoin all three edges `p e_p,q e_q,r e_r` to `F`. Unless all three vertices attach to the same isolated singleton `v`, the resulting graph is an exact two-path cover of `G_P` in which at least one of `p,q,r` is an endpoint. The original cover `U|V` of `G_P=H-{a,c}` has all three internal. Comparing these two covers gives either different supports or different Hamilton orders, and hence a proper tight path or cycle by the preceding arguments.

It remains to consider

`F=(v)|B`

with all three vertices `p,q,r` attached to `v`. For every distinct `s,t∈P`, the exact two-path cover of `G_{\{s,t\}}` consists of the tight three-vertex path on `{s,v,t}` together with `B`. The set `{v,p,q,r}` has no Hamilton tight four-vertex path, since such a path together with `B` would give an exact cover of `G_P` in which a member of `P` is an endpoint.

Fix `s∈P` and write `{t,u}=P-{s}`. Since `s` is internal in the original cover `U|V`, deleting `s` gives a three-path cover of `G_{\{t,u\}}`. Compare it with the exact two-path cover consisting of the tight path on `{t,v,u}` and `B`. A crossing edge again gives a proper tight path. If both crossed pieces are the singleton pieces created by deleting `s`, one of the two original edges incident with `s` supplies the adjacent edge required by boundary antisymmetry.

Thus every case gives a proper tight path or a proper tight cycle. ∎

## 4. Endpoint transfers from a proper path

### Theorem 4.1

Let `F_1,...,F_r` be a family of spanning three-path covers of `H`, each having the maximum possible number `|V(H)|-3` of edges, and let `M_i` be the order of a longest path in `F_i`. Put

`M=max_i M_i`.

Suppose a proper tight path `Q` is given. Repeated endpoint transfers yield at least one of the following:

1. a spanning two-path cover of `H`;
2. a spanning three-path cover containing a path of order at least `M+1`;
3. a spanning three-path cover `A|B|C` satisfying the hypotheses, and hence the conclusion, of Lemma 1.1.

### Proof

Since `Q` is proper, minimality gives a cover of `H-V(Q)` by at most two tight paths. It cannot be Hamiltonian, since a Hamilton path of the complement together with `Q` would two-cover `H`. Write

`H-V(Q)=R|S`.

Then `Q|R|S` is a spanning three-path cover. Choose a longest path `A` and write the other two paths as `B,C`. If `|A|≥M+1`, outcome 2 holds.

Assume `|A|≤M`. If a nontrivial path `X=(x_0,...,x_m)` among `B,C` has an endpoint transferable into either end of `A`, perform that transfer. If `X` is a singleton and its vertex can be appended or prepended to `A`, merging it with `A` gives a spanning two-path cover with the third path.

Every nonclosing transfer increases `|A|` by one and decreases one of the other two paths by one, so `A` remains longest among the three current paths. Repeat while a transfer is possible. Since `|A|≤|V(H)|`, the process terminates: either a spanning two-path cover appears, `|A|` reaches `M+1`, or no endpoint transfer remains. In the last case `A` is still longest among the three current paths, so Lemma 1.1 applies and gives outcome 3. ∎