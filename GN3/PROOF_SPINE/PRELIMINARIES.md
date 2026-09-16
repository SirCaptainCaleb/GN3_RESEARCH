# Preliminary reductions for a smallest counterexample

**Status: supervised GN3 reconstruction; not yet final GN3 certification.**

This document contains the common starting point for the two active proof-spine arguments. It is written independently of the legacy Engine organization. The later documents may assume every conclusion proved here.

## 1. Setup

Let `H` be a finite Strong Level-(1) boundary tournament. For distinct vertices `x,y,z`, call the ordered triple `(x,y,z)` **tight** when it is allowed by the boundary relation. Boundary antisymmetry says that exactly one of

`(x,y,z)`, `(z,y,x)`

is tight.

A **tight path** is an ordered list of distinct vertices in which every consecutive ordered triple is tight. A path cover is a collection of vertex-disjoint tight paths whose union is the whole vertex set. Write `pc(G)` for the minimum number of paths in such a cover.

Assume the two-path-cover theorem is false, and choose `H` with minimum order subject to

`pc(H)>2`.

Every proper induced subgraph of `H` then has path-cover number at most two.

### Proposition 1.1

`pc(H)=3`.

### Proof

Choose any vertex `v`. By minimality, `H-v` has a cover by at most two tight paths. Adding `(v)` as a singleton path gives a cover of `H` by at most three paths. Since `H` is a counterexample to the two-path-cover theorem, `pc(H)>2`. Therefore `pc(H)=3`. ∎

## 2. The small-order reduction

We use three previously proved finite statements, stated here only in the form needed below.

### Input A: extension of a three-vertex path

Let `P` be a tight path on three vertices, disjoint from three further vertices `x,y,z`. At least one of the three five-vertex sets

`V(P)∪{x,y}`, `V(P)∪{x,z}`, `V(P)∪{y,z}`

has a Hamilton tight path.

Two immediate consequences are useful.

1. Every six-vertex set contains a Hamilton tight path on five of its vertices.
2. Every six-vertex set contains at least four five-subsets having Hamilton tight paths.

For the second statement, if three distinct one-vertex deletions were all non-Hamiltonian, orient the complementary three vertices as a tight three-vertex path and apply Input A to the three deleted vertices.

### Input B: four-vertex density inside a five-set

Every five-vertex set contains at most three four-subsets having no Hamilton tight four-vertex path.

For a Hamiltonian five-set this follows by deleting the two endpoints of a Hamilton path. For a non-Hamiltonian five-set it is the previously proved five-vertex density result.

### Input C: the ten-vertex Johnson cut bound

Let `Omega` be a ten-element set, let `F` be a family of five-subsets containing no complementary pair, and put

`bar F={Omega-A:A∈F}`.

In the Johnson graph `J(10,5)`, where two five-sets are adjacent when they meet in four vertices,

`e(F,bar F)<=15|F|`.

We now prove the only small-order fact needed later.

### Theorem 2.1

`|V(H)|>10`.

### Proof

#### Orders at most eight

Every set of at most three vertices can be ordered as a tight path. Hence any graph of order at most six is covered by two tight paths.

If `|V(H)|` is seven or eight, choose six vertices. By Input A they contain a Hamilton tight path on five vertices. The complement has order two or three and is itself a tight path. Thus `H` is two-covered. Hence

`|V(H)|>=9`.

#### Order nine

Suppose `|V(H)|=9`. Let `F_5` be the family of five-subsets having Hamilton tight paths, and let `B_4` be the family of four-subsets having no Hamilton tight four-vertex path.

Each six-set contains at least four members of `F_5`, while each five-set lies in exactly four six-sets. Double-counting gives

`4|F_5| >= 4 C(9,6)`,

so

`|F_5|>=84`.

By Input B, each five-set contains at most three members of `B_4`. Each four-set lies in exactly five five-sets, so

`5|B_4| <= 3 C(9,5)=378`,

and therefore

`|B_4|<=75`.

If `H` had no two-path cover, then the complement of every Hamiltonian five-set would be a non-Hamiltonian four-set. Distinct five-sets have distinct complements, so

`|B_4|>=|F_5|>=84`,

contradicting `|B_4|<=75`. Thus order nine is impossible.

#### Order ten

Suppose `|V(H)|=10`, and let `F` be the family of five-subsets having Hamilton tight paths.

The six-vertex consequence of Input A implies both

`union F=V(H)`

and

`intersection F=empty`.

Indeed, given a vertex `x`, choose a six-set containing it. At least four of its five-subsets are Hamiltonian, and only one omits `x`. Conversely, choose a six-set avoiding `x` and then a Hamiltonian five-subset of it.

No two members of `F` are disjoint, since two complementary Hamilton five-vertex paths would give a spanning two-path cover of `H`.

Let

`m=min{|A∩B|:A,B∈F, A!=B}`.

Then `1<=m<=3`. To see the upper bound, suppose every two distinct members of `F` meet in at least four vertices. Choose distinct `A,B∈F` with

`A=C∪{a}`, `B=C∪{b}`, `|C|=4`.

Any other `D∈F` either contains all of `C`, or has the form

`D=(C-{c})∪{a,b}`

for some `c∈C`. If a set of the second form exists, then any member of `F` containing a vertex outside `A∪B` must contain all of `C`, and therefore meets that second-form set in only three vertices, a contradiction. If no set of the second form exists, every member of `F` contains `C`, contradicting `intersection F=empty`. Hence `m<=3`.

We exclude `m=3,2,1` in turn.

**Case `m=3`.** Choose `A,B∈F` with `S=A∩B` and `|S|=3`. Order `S` as a tight three-vertex path. By minimality, `H-S` has a cover by at most two tight paths. It cannot be Hamiltonian, because a Hamilton path on `H-S` together with the path on `S` would two-cover `H`. Hence `H-S` has an exact two-path cover.

That seven-vertex graph contains a Hamiltonian five-set `D`: if one path in the cover has at least five vertices, use it or the six-vertex consequence of Input A; in the only remaining size pattern `4+3`, take the three-vertex path and any three vertices of the four-vertex path and apply Input A. Thus `D∈F` and `D∩S=empty`.

But `A-S` has only two vertices, so `|A∩D|<=2`, contradicting the definition of `m`. Hence `m!=3`.

**Case `m=2`.** Choose `A,B∈F` with `S=A∩B` and `|S|=2`. By Proposition 3.1 below, `H-S` has an exact two-path cover with both paths nontrivial. As in the preceding case, that eight-vertex graph contains a Hamiltonian five-set `D` disjoint from `S`: cover-size patterns `6+2` and `5+3` are immediate, and in the `4+4` case apply Input A to a consecutive three-vertex subpath of one path and three vertices of the other.

Put

`U=A-S`, `V=B-S`,

and let `R` be the remaining two vertices. Then `|U|=|V|=3` and `|R|=2`. Minimality of `m` gives

`|D∩U|>=2`, `|D∩V|>=2`.

Hence the intersection sizes of `D` with `U,V,R` are one of

`(2,2,1)`, `(2,3,0)`, `(3,2,0)`.

Choose `L∈{A,B}` with `|L∩D|=2`, let `M` be the other member, and set

`X=L∩M=S`, `Y=L∩D`, `Z=M∩D`.

Then `|X|=|Y|=2`, `Z` is disjoint from `L`, and `|Z|` is two or three.

If `|Z|=2`, write

`L=X∪Y∪{p}`, `M=X∪Z∪{b}`, `D=Y∪Z∪{d}`,

and let `e` be the tenth vertex. Order `{p,b,e}` as a tight three-vertex path. If `X={x_1,x_2}`, choose any `r∈D` and apply Input A to the three outside vertices `x_1,x_2,r`. The resulting Hamiltonian five-set meets `D` in at most one vertex, contradicting `m=2`.

If `|Z|=3`, write

`L=X∪Y∪{p}`, `M=X∪Z`, `D=Y∪Z`,

and let `e,f` be the two remaining vertices. Order `{p,e,f}` as a tight three-vertex path. No pair of vertices from `X∪Y∪Z` can extend this path to a Hamiltonian five-set: meeting both `M` and `D` in at least two vertices would force both added vertices into `Z`, but then the resulting five-set would meet `L` only in `p`. Applying Input A to any three distinct vertices of `X∪Y∪Z` gives a contradiction. Hence `m!=2`.

**Case `m=1`.** Fix `A∈F` and put `E=V(H)-A`. Then `E∉F`, since otherwise `A` and `E` would give two complementary Hamilton paths.

Fix `a∈A`. For each `z∈E`, put

`B_z=(E-{z})∪{a}`.

At most one of the five sets `B_z` is non-Hamiltonian. For if `B_x,B_y` were both non-Hamiltonian, order the three-set `E-{x,y}` as a tight path and apply Input A with the three outside vertices `x,y,a`; one of `E,B_y,B_x` would then be Hamiltonian, a contradiction.

Thus each `A∈F` has at least twenty one-vertex replacements belonging to `F`.

Let

`bar F={V(H)-B:B∈F}`.

The families `F` and `bar F` are disjoint. For each successful replacement `B_z=(E-{z})∪{a}`, the complement

`(A-{a})∪{z}`

lies in `bar F` and is adjacent to `A` in `J(10,5)`. Therefore

`e(F,bar F)>=20|F|`,

contradicting Input C, which gives

`e(F,bar F)<=15|F|`.

Hence `m!=1`.

All possible values of `m` are excluded, so order ten is impossible. Together with the preceding cases,

`|V(H)|>10`.

∎

## 3. Deleting two vertices

The following elementary consequence of minimality is used in both later arguments.

### Proposition 3.1

For any distinct vertices `p,t`,

`pc(H-{p,t})=2`,

and neither path in an exact two-path cover of `H-{p,t}` is a singleton.

### Proof

Minimality gives `pc(H-{p,t})<=2`.

Suppose first that `H-{p,t}` has a Hamilton path beginning at `w`. The three-set `{p,w,t}` can be ordered as a tight path. That three-vertex path together with the suffix of the Hamilton path beginning after `w` gives a spanning two-path cover of `H`, a contradiction.

Now suppose an exact two-path cover of `H-{p,t}` has singleton component `(u)`. The three-set `{p,u,t}` can be ordered as a tight path. Together with the other path, it gives a spanning two-path cover of `H`, again a contradiction.

Therefore the pair-deleted graph has path-cover number exactly two and both paths in every exact two-path cover are nontrivial. ∎

## 4. Orientation through a fixed pair

Fix distinct vertices `a,c`. For every `x∈V(H)-{a,c}`, boundary antisymmetry makes exactly one of

`(a,x,c)`, `(c,x,a)`

tight. Thus

`X_{a,c}={x:(a,x,c) is tight}`,

`Y_{a,c}={x:(c,x,a) is tight}`

partition `V(H)-{a,c}`.

Since `|V(H)|>10`,

`|X_{a,c}|+|Y_{a,c}|>=9`.

This partition is the common local geometry used by both later arguments.

### Proposition 4.1

Let

`H-{a,c}=U|V`

be an exact two-path cover. Then both `U,V` are nontrivial, and at least five vertices of `U|V` are internal vertices of their paths. Consequently at least three internal vertices lie in the same one of `X_{a,c},Y_{a,c}`.

### Proof

The two paths are nontrivial by Proposition 3.1. They have at most four endpoints altogether. Since `H-{a,c}` has at least nine vertices, at least five vertices are internal. The two orientation classes partition those internal vertices, so one class contains at least three of them. ∎

After interchanging `a,c` when convenient, the three vertices may therefore be written `p,q,r` with

`(a,p,c)`, `(a,q,c)`, `(a,r,c)`

all tight.

## 5. Common starting package

The two later proof-spine documents use only the following common facts from this file.

1. `H` is a smallest counterexample and `pc(H)=3`.
2. `|V(H)|>10`.
3. Deleting any two vertices leaves an exact two-path-coverable graph, and neither path in such a cover is a singleton.
4. For every fixed pair `{a,c}`, the other vertices split into the two orientation classes `X_{a,c},Y_{a,c}` above.
5. Any exact two-path cover of `H-{a,c}` contains at least five internal vertices, three of which have the same orientation through `{a,c}`.

No later proof should re-establish these reductions unless it needs a stronger statement.

## Provenance

The small-order proof is the language-reduced form of the certified E8997 argument. Input A is the fixed three-vertex-path extension theorem; Input B packages the two five-vertex results used only to bound bad four-subsets; Input C is the complement-free Johnson `J(10,5)` cut bound. Proposition 3.1 is the pair-deletion argument already embedded in the certified small-order proof.
