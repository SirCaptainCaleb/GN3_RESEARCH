# Edge-ordered comparison model and one-half fence

**Summary:** Edge-ordered local surgery and prescribed-removability tools yield the CCS one-half obstruction and connect the grand two-cover conjecture to asymptotic altitude one half.

## Statement

Reusable edge-ordered local surgery and prescribed-removability tools, together with the CCS bit-vector one-half obstruction and the implication that the grand two-cover conjecture would settle complete-graph altitude asymptotically at one half.

## Body

# Edge-ordered comparison model: local tools and sharp fences

Let `G` be an edge-ordered complete graph on four vertices, assume that `G` has an increasing Hamilton path, and prescribe a vertex `x`.

Then `G` has an increasing Hamilton path `A` such that deleting `x` from the vertex sequence of `A` leaves an increasing path on the other three vertices.

## Proof

If some increasing Hamilton path has `x` as an endpoint, deleting `x` leaves an increasing three-vertex path, so suppose `x` is internal in an increasing Hamilton path.

First suppose `A_0=(a,x,b,c)` with `ax<xb<bc`. If `ab<bc`, then deleting `x` from `A_0` leaves the increasing path `(a,b,c)`.

Assume instead `bc<ab`, and compare `ac` with the displayed edges.

- If `bc<ac`, then `(x,b,c,a)` is increasing.
- If `ax<ac<bc`, then `(x,a,c,b)` is increasing.
- If `ac<ax`, then `(c,a,x,b)` is increasing, and deleting `x` leaves `(c,a,b)`, which is increasing because `ac<ax<xb<bc<ab`.

Thus the claim holds whenever `x` is the second vertex of an increasing Hamilton path.

If `x` is the third vertex, reverse both the total edge order and the vertex order of the path. The reversed path is increasing in the reversed edge order and has `x` second. Apply the preceding case there, then reverse the resulting path again. Increasingness returns to the original edge order, and deleting `x` commutes with reversing the vertex sequence. ∎

# Sharpness: two prescribed removable vertices can fail

Let the vertices be `0,1,2,3`, with edge order
`01 < 02 < 13 < 23 < 03 < 12`.

The increasing Hamilton paths are exactly
`(0,1,3,2)`
and
`(1,0,2,3)`.

Indeed their edge sequences are respectively
`01 < 13 < 23`
and
`01 < 02 < 23`.
A direct check of the remaining vertex orders gives no other increasing Hamilton path.

Prescribe the two vertices `0,1`.

For `(0,1,3,2)`, deleting `0` leaves the increasing path `(1,3,2)`, but deleting `1` leaves `(0,3,2)`, which is not increasing because `03 > 23`.

For `(1,0,2,3)`, deleting `1` leaves the increasing path `(0,2,3)`, but deleting `0` leaves `(1,2,3)`, which is not increasing because `12 > 23`.

Hence no increasing Hamilton path has both prescribed vertices separately removable while preserving an increasing three-vertex path. ∎

This rules out the naive strengthening of the prescribed-removable-vertex lemma that would make one four-vertex short component simultaneously compatible with two adjacent common-middle exchanges. Pairwise compatibility must therefore be coordinated by another mechanism rather than demanded from a single Hamilton order.

# Edge-ordered cover surgery

## 2. One cut and two joins in an edge-ordered path cover

Let `G` be an edge-ordered complete graph and let `F` be a spanning cover by `c>=3` vertex-disjoint increasing paths. Orient each path increasingly.

For a vertex `v` of one of the paths, let `L(v)` be its incoming path edge when present and let `L(v)=-infinity` at a source. Let `U(v)` be its outgoing path edge when present and let `U(v)=+infinity` at a terminal.

Let `p->v` be an edge of one component `C`. Let `t` be the terminal vertex of a second component `A`, and let `s` be the source vertex of a third component `B`, with the three components distinct. If

`L(t) < tv < U(v)`

and

`L(p) < ps < U(s)`,

then deleting the path edge `pv` and inserting the edges `tv` and `ps` produces a spanning increasing path cover with `c-1` components.

The statement remains valid when `A` or `B` is a singleton, using the endpoint conventions above.

**Proof.** Write

`A=(a_0,...,t)`,

`C=(c_0,...,p,v,...,c_m)`,

`B=(s,...,b_q)`.

After deleting `pv`, replace the three components by

`(a_0,...,t,v,...,c_m)`

and

`(c_0,...,p,s,...,b_q)`.

The two displayed inequalities are exactly the comparisons needed at the two new joins. All inherited comparisons remain unchanged. The new paths are disjoint, span the same vertices, and replace three old components by two. ∎

## 3. Two cuts and a singleton cross-swap

Let an edge-ordered complete graph have a spanning three-path cover

`A|B|(z)`

with `A,B` nontrivial increasing paths. Orient `A,B` increasingly. Choose path edges

`q->w` in `A`, `p->v` in `B`.

With the same `L,U` notation, suppose

`L(q)<qz<zv<U(v)`

and

`L(p)<pw<U(w)`.

Then deleting `qw,pv` and adding `qz,zv,pw` gives a spanning cover by two increasing paths.

**Proof.** Let `A_q` be the prefix of `A` ending at `q`, `A_w` the suffix beginning at `w`, and similarly let `B_p,B_v` be the prefix and suffix of `B` determined by `p->v`. The two new paths are

`A_q,z,B_v`

and

`B_p,A_w`.

They are disjoint and span all vertices. The first displayed chain gives every new comparison in the first path, and the second gives the single new comparison in the second path. ∎

## 4. Repeated singleton transfers force an extreme triangle edge

Let `G` be an edge-ordered complete graph with no spanning cover by two increasing paths. Let `x,y` be distinct vertices.

Let `T=(v,t_1,...,t_r)`, `r>=0`, be an increasing path disjoint from an increasing path `A` and from `{x,y}`. Suppose

`A | (y,v,t_1,...,t_r) | (x)`

and

`A | (x,v,t_1,...,t_r) | (y)`

are spanning three-path covers of `G`. Then

`vx<xy` and `vy<xy`.

Thus `xy` is the largest edge of the triangle `{x,y,v}`.

Dually, let `S=(s_0,...,s_r,w)`, `r>=0`, be an increasing path disjoint from an increasing path `A` and from `{x,y}`. If

`A | (s_0,...,s_r,w,y) | (x)`

and

`A | (s_0,...,s_r,w,x) | (y)`

are spanning three-path covers of `G`, then

`xy<wx` and `xy<wy`,

so `xy` is the smallest edge of `{x,y,w}`.

If both pairs of covers exist for the same pair `{x,y}`, with the displayed vertices `v` and `w`, then

`vx,vy < xy < wx,wy`,

and both

`(v,x,y,w)`, `(v,y,x,w)`

are increasing paths.

**Proof.** In the first pair of covers, if `xy<yv`, then `(x,y,v,t_1,...,t_r)` is increasing and together with `A` gives a spanning two-path cover. Hence `yv<xy`. The other cover similarly gives `xv<xy`.

For the second pair of covers, if `wy<xy`, then `(s_0,...,s_r,w,y,x)` is increasing and together with `A` gives a spanning two-path cover. Hence `xy<wy`. If `wx<xy`, then `(s_0,...,s_r,w,x,y)` is increasing and together with `A` gives a spanning two-path cover. Hence `xy<wx`.

Combining the two sets of inequalities gives the final two increasing four-vertex paths. ∎

## 5. Extreme two-vertex-component constraints in an edge-ordered three-cover

Let `G` be an edge-ordered complete graph with no spanning cover by two increasing paths. For a named increasing path component `A`, write `L_A(v)` and `U_A(v)` for the incoming and outgoing path edges at `v`, with the same endpoint conventions `-infinity,+infinity` as in Section 2.

### Globally smallest two-vertex component

Suppose

`(x,y)|A|B`

is a spanning increasing three-cover and `xy` is the globally smallest edge. Let `p->v` be a path edge of `A`, and let `s` be the source of `B`. If

`L_A(p)<ps<U_B(s)`,

then

`xv>=U_A(v)` and `yv>=U_A(v)`.

### Globally largest two-vertex component

Suppose instead

`(X,Y)|A|B`

is a spanning increasing three-cover and `XY` is the globally largest edge. Let `p->v` be a path edge of `A`, and let `t` be the terminal of `B`. If

`L_B(t)<tv<U_A(v)`,

then

`pX<=L_A(p)` and `pY<=L_A(p)`.

Here the inequalities use the formal endpoint values `-infinity,+infinity`; for example a conclusion `e>=+infinity` means that the stated antecedent cannot occur when the relevant vertex is terminal.

**Proof.** For the minimum-edge case, orient the two-vertex component as `(x,y)`. Since `xy` is globally smallest, `xy<yv`. If also `yv<U_A(v)`, then Section 2 applies with terminal `y` of the two-vertex component, cut edge `p->v`, and source `s`, producing a spanning two-path cover. Thus `yv>=U_A(v)`. Reverse the order to `(y,x)` and repeat to obtain `xv>=U_A(v)`.

For the maximum-edge case, orient the two-vertex component as `(X,Y)`. Since `pX<XY`, if also `L_A(p)<pX`, Section 2 applies using source `X` of that component and terminal `t` of `B`, again producing a two-path cover. Thus `pX<=L_A(p)`. Reverse the order to `(Y,X)` and repeat for `pY`. ∎



# CCS one-half obstruction

For n=2^k, identify V(K_n) with GF(2)^k.

Label the edge xy by the nonzero vector x+y. For each fixed vector a, the edges with label a form a perfect matching: they are the pairs {x,x+a}. Order the vector labels lexicographically, place all edges with one vector label consecutively, and order edges inside a label class arbitrarily.

Let a_1,...,a_t be the vector labels encountered along an increasing simple path. Consecutive path edges cannot have the same vector label because one label class is a matching, so the a_i are lexicographically strictly increasing.

If the path has vertices v_0,...,v_t, then

v_j = v_0 + a_1 + ... + a_j.

Simplicity of the path is therefore equivalent to requiring every consecutive block sum

a_i + a_{i+1} + ... + a_j

to be nonzero. Conversely, any lexicographically increasing sequence of nonzero vectors with every consecutive block sum nonzero yields a simple increasing path by these cumulative sums.

Thus the maximum increasing-path length in this edge order is exactly the extremal length f(k) of the corresponding nonzero-block-sum sequence problem.

Calderbank, Chung, and Sturtevant proved

f(k) <= (1/2+o(1)) 2^k.

Hence this explicit edge ordering of K_{2^k} has no increasing path longer than (1/2+o(1))n.

## Fence meaning

This is stronger than a numerical altitude benchmark. It shows that even inside the edge-ordered subclass of boundary tournaments, a highly algebraic family of perfect-matching edge classes can obstruct every long single path at the one-half scale.

Accordingly, no GN3 argument may rely on forcing one tight path substantially beyond n/2 in every boundary tournament. A proof of the two-cover conjecture must use genuinely two-path structure, compatibility between deletions, or another mechanism not reducible to a universal long-single-path theorem.

External source: A. R. Calderbank, F. R. K. Chung, D. G. Sturtevant, Increasing sequences with nonzero block sums and increasing paths in edge-ordered graphs, Discrete Mathematics 50 (1984), 15-28.

# Altitude consequence of the grand conjecture

Let K_n carry an arbitrary strict total order on its ordinary edges. Define a boundary tournament H on the same vertex set by declaring

(a,b,c) tight iff ab<bc

for distinct a,b,c.

By the comparison representation in the small-set structure module, a vertex-simple sequence is a tight path in H exactly when its consecutive ordinary edges form an increasing path in the given edge order.

Suppose the grand two-cover conjecture holds. Then H has a spanning cover by at most two tight paths. One of those paths contains at least ceil(n/2) vertices, hence the original edge-ordering of K_n contains an increasing path of length at least

ceil(n/2)-1.

Therefore, writing alpha(K_n) for the classical altitude of K_n,

alpha(K_n) >= ceil(n/2)-1.

Calderbank, Chung, and Sturtevant (Discrete Mathematics 50 (1984), 15-28) proved

alpha(K_n) <= (1/2+o(1))n.

Consequently the grand conjecture would imply

alpha(K_n)=(1/2+o(1))n.

This is not a proof step toward the grand conjecture. It is a hardness/benchmark observation: even the acyclic-comparison (edge-ordered) subclass contains a long-standing increasing-path problem, and a universal two-cover theorem would settle its asymptotic constant at one half. ∎

## Metadata

- ID: edgeorder01
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
