# Direct longest-path entrance and a rank-bearing cube route

**Status: supervised GN3 reconstruction. This revision incorporates the independent audit corrections and separates the shortest known route from the longer route that carries additional rank information. It is not yet a final GN3 certification.**

## 1. Common input

Work throughout under [`PRELIMINARIES.md`](PRELIMINARIES.md). Thus `H` is a smallest counterexample with

`pc(H)=3`, `|V(H)|>10`,

and deleting any two vertices leaves an exact two-path-coverable graph in which neither path is a singleton.

The preliminary document also proves the fixed-pair orientation fact used later: for any distinct `a,c`, every other vertex lies in exactly one of the two classes determined by `(a,x,c)` and `(c,x,a)`; and any exact two-path cover of `H-{a,c}` has at least five internal vertices, three of which have the same orientation through `{a,c}`.

## 2. The shortest route to the nonextendable three-path configuration

The Boolean-cube construction is not needed merely to reach the local configuration that was formerly treated as the next state of the proof. There is a direct route.

Choose a globally longest tight path

`A=(a_0,...,a_s)`.

If `A` spans `H`, the theorem is already proved. Otherwise `H-V(A)` is a proper induced subsystem. Minimality gives a cover by at most two tight paths, and it cannot be Hamiltonian because such a path together with `A` would two-cover `H`. Hence

`H-V(A)=B|C`

is an exact two-path cover.

Thus

`A|B|C`

is a spanning cover of `H` by three tight paths.

Global maximality of `A` implies that no endpoint of `B` or `C` can be transferred into either end of `A` so as to create a longer tight path. If an entire second path could be concatenated with `A`, the result together with the third path would be a spanning two-path cover. Therefore, in a counterexample, `A|B|C` is already a three-path configuration in which `A` cannot be enlarged by any of the elementary endpoint moves used below.

### 2.1 The longest path has at least three vertices

If `|A|=1`, all paths are singletons and `H` has only three vertices, impossible here.

If `|A|=2`, write `A=(a_0,a_1)`. Every other path has order at most two. If one of them is `(b_0,b_1)`, failure of the two endpoint extensions gives

`(b_0,a_1,a_0)` and `(a_1,a_0,b_1)`

tight, so

`(b_0,a_1,a_0,b_1)`

is a tight four-vertex path; together with the third path this two-covers `H`. If both other paths are singletons, `A` together with the ordered pair on those two vertices already gives a two-path cover. Hence

`|A|>=3`.

### 2.2 The case `|A|>=4`

For a nontrivial path `X=(x_0,...,x_m)` among `B,C`, failure to extend the right end of `A` implies

`(x_0,a_s,a_{s-1})`

is tight. Dually, failure to extend the left end implies

`(a_1,a_0,x_m)`

is tight.

Thus the two disjoint ordered pairs

`(a_s,a_{s-1})` and `(a_1,a_0)`

occur in retained tight ordered triples with witness vertices attached on opposite ends. The four vertices of these ordered pairs are distinct because `|A|>=4`.

This is exactly the local four-vertex input needed by the later continuation machinery. We also retain one ordinary consecutive tight ordered triple of `A`.

### 2.3 The case `|A|=3`

Write

`A=(a_0,a_1,a_2)`.

Delete `a_1`. The inherited paths

`(a_0)|(a_2)|B|C`

form a four-path cover of `H-a_1`.

Minimality gives a path cover of `H-a_1` by at most two paths. It cannot be Hamiltonian: a Hamilton path of `H-a_1` together with the singleton `(a_1)` would two-cover `H`. Hence `H-a_1` has an exact two-path cover.

Some selected edge `xy` of that exact cover joins two distinct components of the inherited four-path cover; otherwise two connected paths could not cover all four nonempty components. Boundary antisymmetry on `a_1,x,y` makes exactly one of

`(a_1,x,y)` and `(y,x,a_1)`

tight.

Thus the deleted singleton and the selected ordered pair are linked by an explicit tight ordered triple, again giving the local input required by the continuation problem.

### Direct-entrance conclusion

Every smallest counterexample therefore reaches, without any Boolean-cube argument, a spanning three-path cover with a distinguished path that admits no endpoint extension, together with one of the two explicit local configurations above.

This is the shortest known route to the present local frontier.

## 3. Why retain the Boolean cube at all?

The longer construction remains potentially useful because it carries additional information: it begins from a finite family of specific maximum spanning three-path forests and yields a **strict rank decrease relative to that family**.

That rank decrease is not yet known to iterate. It should therefore be viewed as extra structure, not as the reason we can reach the nonextendable configuration.

The rest of this document reconstructs that additional argument.

## 4. Three same-oriented internal vertices and the Boolean cube

Choose distinct `a,c` and an exact two-path cover

`H-{a,c}=U|V`.

By Proposition 4.1 of [`PRELIMINARIES.md`](PRELIMINARIES.md), both paths are nontrivial and there are internal vertices `p,q,r` having the same orientation through `{a,c}`. After interchanging `a,c` if necessary, assume

`(a,p,c)`, `(a,q,c)`, `(a,r,c)`

are tight.

Put

`P={p,q,r}`,  
`K={a,c,p,q,r}`,  
`W=V(H)-K`.

A direct boundary-antisymmetry argument gives a Hamilton tight path on `K`. Every set

`K-J={a,c}∪(P-J)`, `J⊆P`,

also has a Hamilton tight path.

For each `J⊆P`, define

`G_J=H[W∪J]`.

If some `G_J` were Hamiltonian, its Hamilton path together with a Hamilton path on `K-J` would two-cover `H`. Since `G_J` is proper, minimality therefore gives

`pc(G_J)=2`

for all eight choices of `J`.

An exact two-path cover of `G_J`, together with a Hamilton path on `K-J`, is a spanning three-path cover of `H`. Because `pc(H)=3`, such a cover has the minimum possible number of path components and exactly `|V(H)|-3` selected edges. Equivalently, it is a maximum spanning forest among spanning subgraphs whose components are tight paths. This verifies the exact hypothesis required by the rank argument in Section 6.

## 5. Cube comparison lemma

The downstream argument does not need five separate branches. The finite cube comparison has one usable conclusion.

### Lemma 5.1

From the cube above, one can select a comparison that produces either

1. a proper tight path in `H`; or
2. a proper tight cycle together with a specified edge at which to open it into a proper tight path,

while retaining the exact cube covers from which the comparison was made.

### Proof

Take an exact two-path cover of `G_J` for some nonempty `J`, delete the vertices of `J`, and split the two paths at the deletions. The maximal nonempty subpaths lying in `W` will be called the surviving `W`-subpaths.

There are at least two such subpaths. If there were only one, it would be a Hamilton path of `W`, which together with a Hamilton path on `K` would two-cover `H`.

#### Case 1: at least three surviving `W`-subpaths

Compare the inherited cover of `W` by at least three paths with an exact two-path cover of `W`. Some selected edge `xy` of the latter joins two distinct inherited components.

If one of those two inherited components is nontrivial, choose an endpoint of `xy`, say `x`, in that component and let `h` be its neighbor along the inherited path. Boundary antisymmetry on `h,x,y` gives a proper tight ordered triple in one of the two possible directions.

If both crossed inherited components are singletons, at least one has a neighbor in `J` in the original cover of `G_J`. Otherwise both singleton components would already be whole path components before deleting `J`, leaving no place for the vertices of `J` and the third surviving `W`-subpath. Use that neighbor in `J` in place of `h`. Boundary antisymmetry again gives a proper tight ordered triple.

Thus the component-drop situation always produces the required proper path.

#### Case 2: exactly two surviving `W`-subpaths

For a singleton set `J={s}`, the vertex `s` cannot be an entire singleton path: deleting it would leave a Hamilton path of `W`, contradicting `pc(W)=2`. Hence `s` is an endpoint attached to one of the two surviving `W`-paths, and deleting `s` leaves an exact two-path cover `F_s` of `W`.

Compare `F_p,F_q,F_r`.

If two of them induce different unordered bipartitions of `W` into path supports, some selected edge of one cover crosses the two path supports of the other. Since

`|W|=|H|-5 >= 6`,

those two crossed path supports cannot both be singletons. Choose a crossing endpoint in a nontrivial path support and its neighbor on that path. Boundary antisymmetry gives a proper tight ordered triple.

If the support bipartitions agree but one common support is traversed in two different Hamilton orders, compare the two orders. A first inversion yields either a reversed selected edge, a reverse tight ordered triple, or a vertex-simple proper tight cycle. In the cyclic case, specify any edge at which the cycle is to be opened.

We may therefore assume that, after exchanging the two paths when necessary,

`F_p=F_q=F_r=F=A|B`

as ordered path covers.

For each `s∈P`, let `e_s` be the endpoint of `F` to which `s` is attached in the corresponding singleton extension.

Now consider an exact two-path cover `T_{st}` of `W∪{s,t}`.

If `s` or `t` is internal on its path, deleting that vertex splits one path into two nonempty subpaths and gives a three-path cover of the corresponding singleton set. Compare it with the exact two-path cover already available there. A crossing selected edge again yields a proper tight path. If a crossed piece is nontrivial, use an inherited neighboring edge. If both crossed pieces are singletons, they are the two sides of a length-three path through the deleted internal vertex, and one of the two original edges through that vertex supplies the needed adjacent edge. Boundary antisymmetry then gives the proper three-vertex path.

Thus we may assume both `s,t` are endpoints.

Neither can be an entire singleton path. If, for example, `(s)` were one whole component of `T_{st}`, deleting `s` would leave a Hamilton path on `W∪{t}`, contradicting `pc(G_{\{t\}})=2`.

Hence deleting either endpoint leaves an exact two-path cover. Comparing these one-vertex deletions with the already fixed singleton extensions produces either one of the support/order discrepancies above or the literal equalities

`T_{st}-s = F_t`,  
`T_{st}-t = F_s`.

In the latter case the attachments at `s,t` are exactly

`s e_s` and `t e_t`.

There can be no additional edge joining `s` to `t` or any hidden extra splice. A two-path forest on `|W|+2` vertices has `|W|` selected edges, whereas `F` has `|W|-2` selected edges. The two displayed attachments already account for the entire difference of two edges. Therefore

`E(T_{st})=E(F)∪{s e_s,t e_t}`.

Two of `p,q,r` cannot attach to the same endpoint of a nontrivial path of `F`, because that endpoint would then have degree three in one of the two-vertex extensions. If two added vertices share an attachment point, that point must be an isolated singleton component `(v)` of `F`, and the corresponding three vertices form a tight path.

Now install the three verified attachments simultaneously.

Unless all three added vertices attach to the same isolated singleton `v`, this gives an exact two-path cover of `G_P` in which at least one of `p,q,r` is an endpoint. The original cover `U|V` of `G_P=H-{a,c}` had all three internal. Comparing these two exact covers of the same residue returns to one of the support/order comparison arguments already handled above and produces a proper path or specified cycle.

The only remaining case is

`F=(v)|B`

with every one-vertex extension using the edge `vs` and every two-vertex extension using the tight three-vertex path on `{s,v,t}`. In addition, `{v,p,q,r}` has no Hamilton tight four-vertex path, because such a path together with `B` would produce the preceding endpoint/internal discrepancy.

Fix `s∈P` and let `{t,u}=P-{s}`. Delete the internal vertex `s` from the original top cover `U|V`. This gives a three-path cover of the same residue covered exactly by the two paths consisting of the tight path on `{t,v,u}` and `B`. Comparing the three-path cover with that exact two-path cover yields a crossing. If a crossed piece is nontrivial, use its inherited neighboring edge. If the two crossed pieces are the singleton sides created by deleting `s`, then the original path through `s` had order three and one of its two edges through `s` supplies the needed adjacent edge. Boundary antisymmetry again produces a proper tight path.

Thus every outcome of the finite cube comparison yields the conclusion of the lemma. ∎

## 6. Strict rank decrease relative to the initial family

Let

`F_1,...,F_r`

be the finite family of maximum spanning three-path forests participating in the comparison of Section 5. In each `F_i`, choose a longest path of order `M_i` and set

`rho(F_i)=(1,n-M_i)`,  
`n=|V(H)|`.

Let

`M_*=max_i M_i`.

By Lemma 5.1, the comparison produces a proper tight path `Q`, possibly after opening a specified proper tight cycle.

If `Q` spans `H`, the theorem is proved. Otherwise `H-V(Q)` is proper. Minimality gives a cover by at most two tight paths, and it cannot be Hamiltonian because a Hamilton path of the complement together with `Q` would two-cover `H`. Hence

`H-V(Q)=R|S`

is an exact two-path cover.

Thus

`Q|R|S`

is a spanning three-path forest. Choose a longest path `A` in it and let `L=|A|`.

If `L>M_*`, then

`(1,n-L)<(1,n-M_*)<=rho(F_i)`

for every `i`. This is already the desired strict decrease relative to the entire initial family.

Assume therefore `L<=M_*`.

### 6.1 Endpoint-transfer process

Write the current three paths as

`A|B|C`.

At either end of `A`, test whether an endpoint of `B` or `C` can be moved into `A`.

For example, write `A=(a_0,...,a_s)` and `X=(x_0,...,x_m)`. At the right end, test `(a_{s-1},a_s,x_0)`.

- If it is tight and `X` is a singleton, `A` and `X` merge, giving a spanning two-path cover with the third path.
- If it is tight and `X` is nontrivial, test `(a_s,x_0,x_1)`. If that is tight, concatenate all of `X` to `A` and again obtain a two-path cover. If it is not tight, delete the edge `x_0x_1` and add `a_sx_0`; the distinguished path grows by one vertex.

The left end is symmetric.

Perform any available endpoint transfer. Each successful transfer increases `|A|` by exactly one. The process therefore stops in finite time in one of three ways:

1. a spanning two-path cover is obtained;
2. `|A|` first reaches `M_*+1`;
3. no endpoint transfer is available at either end.

Case 2 gives rank at most

`(1,n-M_*-1)`,

strictly below every `rho(F_i)`.

Case 3 is exactly the nonextendable three-path configuration described directly in Section 2.

### 6.2 Explicit local data in the nonextendable case

The same two size cases from Section 2 apply.

If `|A|>=4`, failure of endpoint transfers gives the two disjoint ordered pairs at the ends of `A` together with tight ordered triples witnessing extension on opposite ends.

If `|A|=3`, delete the middle vertex. As in Section 2.3, the remaining graph has an exact two-path cover: minimality gives at most two paths, and Hamiltonicity would combine with the deleted singleton to two-cover `H`. A selected edge of the exact cover crosses two components of the inherited four-path cover, and boundary antisymmetry with the deleted middle vertex gives the required tight ordered triple.

For bookkeeping only, assign every configuration of this nonextendable type a rank whose first coordinate is `0`. Then it is strictly below every initial rank `(1,n-M_i)`.

We have therefore proved:

### Rank-decrease theorem

If the finite initial family of maximum spanning three-path forests emits a proper tight path or a specified proper tight cycle, there is a finite continuation to a spanning two-path cover or to a configuration with rank strictly below every member of that initial family.

The decrease is **relative to this initial family**. The theorem does not say that the same argument may be restarted from the final configuration.

## 7. What the Boolean cube adds—and what it does not

The direct longest-path construction of Section 2 already reaches the same nonextendable three-path configuration. Therefore the Boolean cube is not needed merely to reach the current local frontier.

Its extra contribution is the strict decrease from the ranks

`(1,n-M_i)`

attached to the particular maximum three-path forests used in the cube comparison.

At present, no accepted theorem uses that numerical decrease to construct a recursive global order after the nonextendable configuration has been reached. Thus the extra rank information is potentially valuable but not yet load-bearing for closure.

## 8. Exact unresolved statement

The remaining problem on this line is:

> Starting from the nonextendable three-path configuration of Section 2, together with its explicit local ordered-pair/triple data, prove a continuation that either produces a spanning two-path cover or reaches a strictly smaller state in a genuinely well-founded global order.

The rank theorem of Section 6 gives one strict decrease from its own initial family but does not provide such a recursive rule.

The invalidated E9007 compositions and the flagged E9006 composition do not supply the missing continuation.

A particularly promising synthesis with the fixed-pair document is the following **unproved strategy**:

> Construct a recursive order in which the generic continuation is strictly decreasing, and show that equality can occur only when the construction stays on one of the two old two-vertex supports through a previously reduced middle vertex. Then use the fixed-pair reduction history to eliminate that equality case.

This is a research direction, not a theorem.

## 9. Provenance and integrity

The legacy sources for the mathematics retained here are:

- three-vertex cube construction and comparison: E8998 / R2143;
- cube-to-proper-path/cycle reduction: R2136 and R2153;
- rank-decrease theorem and direct longest-path entrance: E9003 / R2147.

The common small-order theorem, pair-deletion argument, and fixed-pair orientation count now live in [`PRELIMINARIES.md`](PRELIMINARIES.md).
