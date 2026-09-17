# Cover augmentation lemmas

**Status: UNAUDITED GN3 REWRITE.**

These statements collect explicit cut-and-join moves and the local obstructions produced when such moves fail. The exact text has not yet received independent GN3 audit.

## 1. Seam alternatives for a spanning three-path cover

Let `H` be a boundary tournament with `pc(H)>2`, and let

`H=A|B|C`

be a spanning three-path cover in which all three components are nontrivial. Write

`A=(a_0,...,a_p)`, `B=(b_0,...,b_q)`

with `p,q>=1`.

If one attempts to concatenate `A` to `B`, the only new triples are

`(a_{p-1},a_p,b_0)`

and

`(a_p,b_0,b_1)`.

They cannot both be tight. Hence at least one of

`(b_0,a_p,a_{p-1})`, `(b_1,b_0,a_p)`

is tight.

The same conclusion holds for each of the six ordered pairs of distinct components among `A,B,C`.

**Proof.** Every consecutive triple inside `A` or `B` is already tight. If both seam triples were tight, their concatenation would be a tight path and, together with the untouched third component, would give a spanning two-path cover. Boundary antisymmetry reverses any failed seam. ∎

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

They are disjoint and span all vertices. The first displayed chain certifies every new comparison in the first path, and the second certifies the single new join in the second path. ∎

## 4. Repeated singleton transfers force an extreme triangle edge

Let `G` be an edge-ordered complete graph with no spanning cover by two increasing paths. Let `x,y` be distinct vertices.

Suppose there are spanning three-path covers

`A | (y,v,b_2,...,b_m) | (x)`

and

`A | (x,v,b_2,...,b_m) | (y)`.

Then

`vx<xy` and `vy<xy`.

Thus `xy` is the largest edge of the triangle `{x,y,v}`.

Dually, if there are spanning three-path covers

`A | (...,w,y) | (x)`

and

`A | (...,w,x) | (y)`, 

then

`xy<wx` and `xy<wy`,

so `xy` is the smallest edge of `{x,y,w}`.

If both kinds of replacement occur for the same pair `{x,y}`, with source-side neighbor `v` and terminal-side neighbor `w`, then

`vx,vy < xy < wx,wy`,

and both

`(v,x,y,w)`, `(v,y,x,w)`

are increasing paths.

**Proof.** In the first pair of covers, if `xy<yv`, then `(x,y,v,b_2,...)` is increasing and together with `A` gives a spanning two-path cover. Hence `yv<xy`. The other cover similarly gives `xv<xy`.

The terminal statement is the reverse argument: if `wy<xy`, append `x` after `y`; if `wx<xy`, append `y` after `x`. Either would produce a two-path cover, so both carrier edges exceed `xy`.

Combining the two sets of inequalities gives the final two increasing four-vertex paths. ∎

## 5. Extreme dimer barriers in an edge-ordered three-cover

Let `G` be an edge-ordered complete graph with no spanning cover by two increasing paths.

### Minimum-edge dimer

Suppose

`(x,y)|A|B`

is a spanning increasing three-cover and `xy` is the globally smallest edge. Let `p->v` be a path edge of `A`, and let `s` be the source of `B`. If

`L_A(p)<ps<U_B(s)`,

then

`xv>=U_A(v)` and `yv>=U_A(v)`.

### Maximum-edge dimer

Suppose instead

`(X,Y)|A|B`

is a spanning increasing three-cover and `XY` is the globally largest edge. Let `p->v` be a path edge of `A`, and let `t` be the terminal of `B`. If

`L_B(t)<tv<U_A(v)`,

then

`pX<=L_A(p)` and `pY<=L_A(p)`.

Here the inequalities use the formal endpoint values `-infinity,+infinity`; for example a conclusion `e>=+infinity` means that the stated antecedent cannot occur when the relevant vertex is terminal.

**Proof.** For the minimum-edge case, orient the dimer first as `(x,y)`. Since `xy` is globally smallest, `xy<yv`. If also `yv<U_A(v)`, then Section 2 applies with dimer terminal `y`, the cut edge `p->v`, and source `s`, producing a spanning two-path cover. Thus `yv>=U_A(v)`. Reverse the vacuous dimer order to `(y,x)` and repeat to obtain `xv>=U_A(v)`.

For the maximum-edge case, orient the dimer as `(X,Y)`. Since `pX<XY`, if also `L_A(p)<pX`, Section 2 applies using source `X` of the dimer and terminal `t` of `B`, again producing a two-path cover. Thus `pX<=L_A(p)`. Reverse the dimer and repeat for `pY`. ∎

## 6. Cap obstruction around a three-vertex component

Let `H` be a boundary tournament with `pc(H)>2`. Suppose

`(a,s,c)|R|Q`

is a spanning three-path cover, where

`R=(u_0,...,u_k)`, `k>=1`.

Then at least one of the following holds:

1. `(s,c,u_0)` is not tight;
2. `(u_k,a,s)` is not tight;
3. `k>=2` and both `(c,u_0,u_1)` and `(u_{k-1},u_k,a)` are not tight.

**Proof.** Cut an edge `u_i u_{i+1}` of `R` and attempt to form

`(u_{i+1},...,u_k,a,s,c,u_0,...,u_i)`.

Together with `Q`, this would be a spanning two-path cover if every new seam were tight.

When `k=1`, cutting the sole edge leaves only the two seams `(u_k,a,s)` and `(s,c,u_0)`, so at least one fails.

Assume `k>=2` and both of those seams are tight. Cutting the first edge of `R` leaves only one additional required seam, `(u_{k-1},u_k,a)`, so it must fail. Cutting the last edge leaves only `(c,u_0,u_1)`, which must also fail. ∎

Boundary antisymmetry therefore supplies the corresponding reversed tight triples whenever one of these seams fails.

## 7. Bridging a three-cover relative to a fixed two-cover

Let `G` be a boundary tournament. Let

`J=P|Q|R`

be a spanning three-path cover and let `F` be a spanning exact two-path cover of the same vertex set.

Choose an ordered pair of distinct components, say

`P=(p_0,...,p_k)`, `Q=(q_0,...,q_l)`,

and attempt to concatenate them across the edge `p_k q_0`. The only new triples that can occur are

`(p_{k-1},p_k,q_0)` when `k>=1`,

and

`(p_k,q_0,q_1)` when `l>=1`.

Hence either a displayed seam is not tight, in which case its reverse is a tight triple on three distinct vertices, or the bridge produces a spanning exact two-path cover.

Moreover, among the distinct endpoint bridge edges available between the three components of `J`, at most one can produce the same ordinary path forest as `F`. Consequently there is a bridge for which either a seam fails and supplies a reversed tight triple, or the resulting exact two-cover is different from `F`.

**Proof.** The first assertion follows because every triple internal to `P,Q,R` is inherited. If both existing seams are tight, the concatenation of `P` and `Q`, together with `R`, is an exact two-cover.

Every successful bridge adds exactly one ordinary edge to the ordinary path forest of `J`. If a successful bridge has the same ordinary forest as `F`, then the forest of `J` is contained in that of `F` and the added bridge is the unique edge of `F` not already in `J`. Thus at most one distinct bridge edge can reconstruct the forest of `F`. There are bridge edges between three different component pairs, so another distinct bridge is available. Apply the first assertion to such a bridge. ∎

## Legacy provenance

Sections 1–5 rewrite A7C3 `S9008`, `S9015`, `S9024`, `S9025`, and `S9037`, respectively. Section 6 extracts the intrinsic cut-and-join statement from `S9041`. Section 7 extracts the reusable three-cover bridge statement from `S9042`.