# Preliminaries

## 1. Definitions and minimal counterexample

Let `H` be a finite Strong Level-(1) boundary tournament. For distinct vertices `x,y,z`, call the ordered triple `(x,y,z)` **tight** when it is allowed by the boundary relation. Boundary antisymmetry says that exactly one of

`(x,y,z)`, `(z,y,x)`

is tight.

A **tight path** is an ordered list of distinct vertices in which every consecutive ordered triple is tight. A path cover is a collection of vertex-disjoint tight paths whose union is the whole vertex set. Write `pc(G)` for the minimum number of paths in such a cover.

Assume that the two-path-cover theorem is false, and choose `H` of minimum order subject to

`pc(H)>2`.

Every proper induced subgraph of `H` has path-cover number at most two.

### Proposition 1.1

`pc(H)=3`.

### Proof

Choose `v∈V(H)`. By minimality, `H-v` has a cover by at most two tight paths. Adding the singleton path `(v)` gives a cover of `H` by at most three paths. Since `pc(H)>2`, we have `pc(H)=3`. ∎

## 2. Three finite lemmas

### Lemma 2.1

Let `P` be a tight path on three vertices and let `x,y,z` be three distinct vertices outside `P`. At least one of

`V(P)∪{x,y}`, `V(P)∪{x,z}`, `V(P)∪{y,z}`

has a Hamilton tight path.

Consequently every six-vertex set contains a Hamilton tight path on five vertices, and every six-vertex set has at least four five-subsets with Hamilton tight paths.

### Lemma 2.2

Every five-vertex set contains at most three four-subsets having no Hamilton tight four-vertex path.

### Lemma 2.3

Let `Ω` be a ten-element set and `F` a family of five-subsets containing no complementary pair. Put

`\bar F={Ω-A:A∈F}`.

In the Johnson graph `J(10,5)`, where two five-sets are adjacent when they meet in four vertices,

`e(F,\bar F)≤15|F|`.

## 3. Order of a smallest counterexample

### Theorem 3.1

`|V(H)|>10`.

### Proof

Every set of at most three vertices can be ordered as a tight path. Hence any graph of order at most six has a two-path cover.

If `|V(H)|` is seven or eight, choose six vertices. By Lemma 2.1 they contain a Hamilton tight path on five vertices. The complement has order two or three and is a tight path. Hence

`|V(H)|≥9`.

Suppose `|V(H)|=9`. Let `F_5` be the family of five-subsets having Hamilton tight paths and let `B_4` be the family of four-subsets having no Hamilton tight four-vertex path.

Every six-set contains at least four members of `F_5`, while every five-set lies in exactly four six-sets. Therefore

`4|F_5|≥4 C(9,6)`,

so `|F_5|≥84`.

By Lemma 2.2, each five-set contains at most three members of `B_4`. Every four-set lies in exactly five five-sets, hence

`5|B_4|≤3 C(9,5)=378`,

so `|B_4|≤75`.

The complement of every member of `F_5` must lie in `B_4`, since two complementary Hamilton paths would form a two-path cover of `H`. Thus `|B_4|≥|F_5|≥84`, a contradiction. Hence `|V(H)|≠9`.

Suppose `|V(H)|=10`, and let `F` be the family of five-subsets having Hamilton tight paths. Lemma 2.1 implies

`⋃F=V(H)` and `⋂F=∅`.

No two members of `F` are disjoint. Put

`m=min{|A∩B|:A,B∈F, A≠B}`.

Then `1≤m≤3`. Indeed, if every two distinct members of `F` met in at least four vertices, choose distinct `A,B∈F` with

`A=C∪{a}`, `B=C∪{b}`, `|C|=4`.

Every `D∈F` either contains `C` or has the form

`D=(C-{c})∪{a,b}`

for some `c∈C`. If a set of the second form exists, any member of `F` containing a vertex outside `A∪B` must contain all of `C`, and then meets that second-form set in only three vertices. If none exists, every member of `F` contains `C`. Both alternatives contradict the definition of `F`. Thus `m≤3`.

Assume first `m=3`. Choose `A,B∈F` with `S=A∩B` and `|S|=3`. Order `S` as a tight path. By minimality, `H-S` has a cover by at most two tight paths, and it is not Hamiltonian, since a Hamilton path on `H-S` together with the path on `S` would two-cover `H`. Thus `H-S` has an exact two-path cover.

That seven-vertex graph contains a Hamiltonian five-set `D`: if one path has order at least five, use it or Lemma 2.1 inside a six-vertex subpath; in the only remaining size pattern `4+3`, take the three-vertex path and any three vertices of the four-vertex path and apply Lemma 2.1. Then `D∈F` and `D∩S=∅`, so `|A∩D|≤2`, contradicting `m=3`.

Assume next `m=2`. Choose `A,B∈F` with `S=A∩B` and `|S|=2`. Proposition 4.1 below gives an exact two-path cover of `H-S` with both paths nontrivial. As above, `H-S` contains a Hamiltonian five-set `D` disjoint from `S`: size patterns `6+2` and `5+3` are immediate, and in the `4+4` case apply Lemma 2.1 to a consecutive three-vertex subpath of one path and three vertices of the other.

Put

`U=A-S`, `V=B-S`,

and let `R` be the remaining two vertices. Then `|U|=|V|=3` and `|R|=2`. Minimality of `m` gives

`|D∩U|≥2`, `|D∩V|≥2`,

so the intersection sizes of `D` with `U,V,R` are one of

`(2,2,1)`, `(2,3,0)`, `(3,2,0)`.

Choose `L∈{A,B}` with `|L∩D|=2`, let `M` be the other member, and put

`X=L∩M=S`, `Y=L∩D`, `Z=M∩D`.

Then `|X|=|Y|=2`, `Z∩L=∅`, and `|Z|∈{2,3}`.

If `|Z|=2`, write

`L=X∪Y∪{p}`, `M=X∪Z∪{b}`, `D=Y∪Z∪{d}`,

and let `e` be the tenth vertex. Order `{p,b,e}` as a tight three-vertex path. If `X={x_1,x_2}`, choose `r∈D` and apply Lemma 2.1 to `x_1,x_2,r`. The resulting Hamiltonian five-set meets `D` in at most one vertex, contradicting `m=2`.

If `|Z|=3`, write

`L=X∪Y∪{p}`, `M=X∪Z`, `D=Y∪Z`,

and let `e,f` be the two remaining vertices. Order `{p,e,f}` as a tight three-vertex path. No pair of vertices from `X∪Y∪Z` can extend it to a Hamiltonian five-set: meeting both `M` and `D` in at least two vertices would force both added vertices into `Z`, and then the five-set would meet `L` only in `p`. Lemma 2.1 applied to any three distinct vertices of `X∪Y∪Z` gives a contradiction.

Hence `m≠2`.

Finally assume `m=1`. Fix `A∈F` and put `E=V(H)-A`. Then `E∉F`. Fix `a∈A`; for each `z∈E` put

`B_z=(E-{z})∪{a}`.

At most one of the five sets `B_z` is non-Hamiltonian. Otherwise, if `B_x,B_y` were both non-Hamiltonian, order `E-{x,y}` as a tight three-vertex path and apply Lemma 2.1 to the outside vertices `x,y,a`; one of `E,B_y,B_x` would be Hamiltonian.

Thus every `A∈F` has at least twenty one-vertex replacements belonging to `F`. Let

`\bar F={V(H)-B:B∈F}`.

For each successful replacement `B_z=(E-{z})∪{a}`, the complement

`(A-{a})∪{z}`

lies in `\bar F` and is adjacent to `A` in `J(10,5)`. Hence

`e(F,\bar F)≥20|F|`,

contradicting Lemma 2.3. Therefore `m≠1`.

All possible values of `m` are excluded, so `|V(H)|>10`. ∎

## 4. Deleting two vertices

### Proposition 4.1

For distinct vertices `p,t`,

`pc(H-{p,t})=2`,

and neither path in an exact two-path cover of `H-{p,t}` is a singleton.

### Proof

Minimality gives `pc(H-{p,t})≤2`.

If `H-{p,t}` has a Hamilton path beginning at `w`, order `{p,w,t}` as a tight path. That three-vertex path together with the suffix of the Hamilton path beginning after `w` gives a two-path cover of `H`, a contradiction.

If an exact two-path cover of `H-{p,t}` has singleton component `(u)`, order `{p,u,t}` as a tight path. Together with the other path this gives a two-path cover of `H`, again a contradiction. ∎

## 5. A fixed pair

Fix distinct vertices `a,c`. For every `x∈V(H)-{a,c}`, exactly one of

`(a,x,c)`, `(c,x,a)`

is tight. Define

`X_{a,c}={x:(a,x,c) is tight}`,

`Y_{a,c}={x:(c,x,a) is tight}`.

Then `X_{a,c},Y_{a,c}` partition `V(H)-{a,c}` and

`|X_{a,c}|+|Y_{a,c}|≥9`.

### Proposition 5.1

Let

`H-{a,c}=U|V`

be an exact two-path cover. Then `U,V` are nontrivial and at least five vertices of `U|V` are internal vertices of their paths. Consequently at least three internal vertices belong to the same one of `X_{a,c},Y_{a,c}`.

### Proof

The paths `U,V` are nontrivial by Proposition 4.1. They have at most four endpoints altogether. Since `|V(H)-{a,c}|≥9`, at least five vertices are internal. The two sets `X_{a,c},Y_{a,c}` partition those internal vertices, so one contains at least three of them. ∎