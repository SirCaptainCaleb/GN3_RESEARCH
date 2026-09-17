# Parallel turns and three-vertex core signatures

**Status: UNAUDITED GN3 REWRITE.**

This module records two local five-vertex principles built from several tight triples with the same ordered endpoints. The exact text has not yet received independent GN3 audit.

## 1. Core-signature compression

Fix a three-vertex set

`C={a,b,c}`

in a boundary tournament `H`, and let `E` be a set of vertices disjoint from `C`.

For `x in E` and `d in C`, write `C-{d}={u,v}` and choose the order `(u,v)` for which `(u,d,v)` is tight. Define

`d in M_C(x)`

if and only if `(u,x,v)` is tight.

This is well-defined: reversing `u,v` reverses both tested triples, so boundary antisymmetry preserves whether their tightness agrees.

Define a graph `Gamma_C` on `E` by joining distinct `x,y` when `H[C union {x,y}]` has a Hamilton tight path.

Then:

1. for every `d in C`, the set

   `E_d={x in E:d in M_C(x)}`

   is a clique of `Gamma_C`;
2. if `U subseteq E` is independent in `Gamma_C`, then the sets `M_C(x)`, `x in U`, are pairwise disjoint, and therefore

   `sum_{x in U}|M_C(x)|<=3`;
3. if `U={x,y,z}` is independent, then, after relabelling the vertices of `C` and the three exterior vertices, the signature triple is exactly one of

   `(emptyset,emptyset,emptyset)`,

   `({a},emptyset,emptyset)`,

   `({a,b},emptyset,emptyset)`,

   `({a},{b},emptyset)`,

   `({a,b,c},emptyset,emptyset)`,

   `({a,b},{c},emptyset)`,

   `({a},{b},{c})`.

**Proof.** Fix `d in C` and suppose `x,y in E_d`. With `u,v` ordered so that `(u,d,v)` is tight, the triples

`(u,d,v)`, `(u,x,v)`, `(u,y,v)`

are all tight. Lemma 2.2 of the proof spine gives a Hamilton tight path on

`{u,v,d,x,y}=C union {x,y}`.

Thus `xy` is an edge of `Gamma_C`, proving that `E_d` is a clique.

Hence two vertices of an independent set cannot share a coordinate `d`, so their match sets are pairwise disjoint subsets of the three-element set `C`. This gives the sum bound.

For three exterior vertices, the possible multisets of sizes of three pairwise disjoint subsets of a three-element set are

`(0,0,0)`, `(1,0,0)`, `(2,0,0)`, `(1,1,0)`, `(3,0,0)`, `(2,1,0)`, `(1,1,1)`.

Relabelling the exterior vertices orders the three sizes, and relabelling `a,b,c` gives exactly the seven displayed representatives. ∎

## 2. Three parallel middle vertices admit a Hamilton five-path with an exterior endpoint

Let `a,c,p,q,r` be distinct vertices of a boundary tournament and suppose

`(a,p,c)`, `(a,q,c)`, `(a,r,c)`

are tight. Then `H[{a,c,p,q,r}]` has a Hamilton tight path with at least one endpoint in `{p,q,r}`.

In general one cannot prescribe in advance which of `p,q,r` is an endpoint.

**Proof.** Lemma 2.2 of the proof spine gives some Hamilton tight path on the five vertices. If one endpoint lies in `{p,q,r}`, there is nothing to prove. Suppose instead that the endpoints are `a,c`. After relabelling `p,q,r` as `x,y,z`, the path is one of

`(a,x,y,z,c)`, `(c,x,y,z,a)`.

### Case 1: `(a,x,y,z,c)` is tight

Set

`alpha=[(a,y,z) is tight]`,
`beta=[(z,c,x) is tight]`,
`gamma=[(z,c,y) is tight]`,
`delta=[(c,y,x) is tight]`,
`epsilon=[(x,a,y) is tight]`,
`eta=[(x,a,z) is tight]`.

Consider the seven candidate paths

`a,y,z,c,x`,
`a,z,c,y,x`,
`x,a,y,c,z`,
`x,a,z,c,y`,
`y,a,x,c,z`,
`z,a,x,y,c`,
`z,y,a,x,c`.

Using the three hypotheses and the triples already supplied by `(a,x,y,z,c)`, these candidates are tight respectively under the conditions

`alpha and beta`,
`gamma and delta`,
`epsilon and not gamma`,
`eta and gamma`,
`not epsilon and not beta`,
`not eta and not delta`,
`not alpha and not epsilon`.

Assume all seven fail. Failure of the last condition gives `alpha or epsilon`. If `alpha` is false then `epsilon` is true. If `alpha` is true, failure of the first condition gives `beta` false, and failure of the fifth again gives `epsilon` true. Thus `epsilon` is true. Failure of the third condition gives `gamma` true; failure of the second gives `delta` false; failure of the sixth gives `eta` true. The fourth candidate is then tight, a contradiction.

### Case 2: `(c,x,y,z,a)` is tight

Use

`beta=[(z,c,x) is tight]`,
`gamma=[(z,c,y) is tight]`,
`epsilon=[(x,a,y) is tight]`,
`eta=[(x,a,z) is tight]`.

The five candidates

`a,z,c,x,y`,
`x,a,z,c,y`,
`y,z,a,x,c`,
`x,a,y,c,z`,
`y,a,x,c,z`

are tight respectively under the conditions

`beta`,
`eta and gamma`,
`not eta`,
`epsilon and not gamma`,
`not epsilon and not beta`.

If all fail, then successively `beta` is false, `eta` is true, `gamma` is false, and `epsilon` is false; the fifth candidate is then tight, a contradiction.

Thus some Hamilton five-path has an endpoint in `{p,q,r}`. ∎

### Non-prescribability

Take five vertices `a,c,p,q,r` and order the ten ordinary edges by

`pq < ar < ac < qr < ap < cp < pr < aq < cr < cq`.

Let tight triples be those whose two consecutive ordinary edges increase in this order. Then

`ap<cp`, `aq<cq`, `ar<cr`,

so `(a,p,c),(a,q,c),(a,r,c)` are tight. The Hamilton increasing paths are exactly

`(a,p,r,c,q)` and `(r,a,p,c,q)`

and their reversals as tight-path orderings when applicable to the same consecutive comparisons; in particular `p` is not an endpoint of any Hamilton path in the displayed orientation family. Relabelling `p,q,r` shows that no fixed middle vertex can be prescribed universally.

## Legacy provenance

Section 1 rewrites the reusable part of A7C3 `S9018`. Section 2 is the endpoint strengthening in `S9022`; its basic Hamilton-path existence statement is already Lemma 2.2 of the proof spine.