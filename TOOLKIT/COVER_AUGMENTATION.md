# Cover augmentation lemmas

## 1. Concatenating two components forces a reversed joining triple

Let `H` be a boundary tournament with `pc(H)>2`, and let

`A|B|C`

be a spanning three-path cover of `H` in which all three components are nontrivial. Write

`A=(a_0,...,a_p)`, `B=(b_0,...,b_q)`

with `p,q>=1`.

If `A` is followed by `B`, the only new consecutive triples are

`(a_{p-1},a_p,b_0)`

and

`(a_p,b_0,b_1)`.

They cannot both be tight. Hence at least one of

`(b_0,a_p,a_{p-1})`, `(b_1,b_0,a_p)`

is tight.

The same conclusion holds for each of the six ordered pairs of distinct components among `A,B,C`.

**Proof.** Every consecutive triple wholly inside `A` or `B` is tight. If both new consecutive triples were tight, the concatenation of `A` and `B` would be a tight path and, together with the untouched third component, would give a spanning two-path cover. Boundary antisymmetry gives the reverse of each non-tight joining triple. ∎

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

## 5. Extreme two-vertex-component barriers in an edge-ordered three-cover

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

## 6. Cutting a component around a three-vertex component

Let `H` be a boundary tournament with `pc(H)>2`. Suppose

`(a,s,c)|R|Q`

is a spanning three-path cover, where

`R=(u_0,...,u_k)`, `k>=1`.

Then at least one of the following holds:

1. `(s,c,u_0)` is not tight;
2. `(u_k,a,s)` is not tight;
3. `k>=2` and both `(c,u_0,u_1)` and `(u_{k-1},u_k,a)` are not tight.

**Proof.** Delete an edge `u_i u_{i+1}` of `R` and consider the vertex sequence

`(u_{i+1},...,u_k,a,s,c,u_0,...,u_i)`.

Together with `Q`, this would be a spanning two-path cover if every new consecutive triple were tight.

When `k=1`, deleting the sole edge leaves only the two new triples `(u_k,a,s)` and `(s,c,u_0)`, so at least one is non-tight.

Assume `k>=2` and both of those triples are tight. Deleting the first edge of `R` leaves only one additional new triple, `(u_{k-1},u_k,a)`, so it must be non-tight. Deleting the last edge leaves only `(c,u_0,u_1)`, which must also be non-tight. ∎

Boundary antisymmetry supplies the corresponding reversed tight triple whenever one of the displayed joining triples is non-tight.

## 7. Joining two components relative to a fixed two-cover

Let `G` be a boundary tournament. Let

`J=P|Q|R`

be a spanning three-path cover and let `F` be a spanning exact two-path cover of the same vertex set.

Choose an ordered pair of distinct components, say

`P=(p_0,...,p_k)`, `Q=(q_0,...,q_l)`,

and concatenate them using the ordinary edge `p_k q_0`. The only new consecutive triples that can occur are

`(p_{k-1},p_k,q_0)` when `k>=1`,

and

`(p_k,q_0,q_1)` when `l>=1`.

Hence either one of the displayed triples is non-tight, in which case its reverse is a tight triple on three distinct vertices, or the concatenation gives a spanning exact two-path cover.

Moreover, among distinct ordinary edges joining endpoints of two components of `J` and used to concatenate those components, at most one can produce the same ordinary path forest as `F`. Consequently there is a concatenation for which either a new consecutive triple is non-tight and supplies its tight reverse, or the resulting exact two-cover has ordinary path forest different from that of `F`.

**Proof.** Every consecutive triple wholly inside `P,Q,R` is inherited. If both existing new triples are tight, the concatenation of `P` and `Q`, together with `R`, is an exact two-cover.

Every successful concatenation adds exactly one ordinary edge to the ordinary path forest of `J`. If such a concatenation has the same ordinary forest as `F`, then the forest of `J` is contained in that of `F` and the added joining edge is the unique edge of `F` not already in `J`. Thus at most one distinct joining edge can reconstruct the forest of `F`.

The three unordered pairs of components of `J` supply three distinct ordinary endpoint-joining edges, since the components are pairwise vertex-disjoint. Choose one different from the possible unique edge that reconstructs `F`, orient the corresponding pair of components in either concatenation order, and apply the first assertion. ∎
