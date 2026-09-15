# S9011 — Line-Graph Comparison Representation Theorem

## Theorem

Let `H` be a finite Strong Level-(1) boundary tournament on vertex set `V`. Define a directed graph `Gamma(H)` whose vertices are the ordinary edges of the complete graph `K_V`.

Whenever

`e={u,v}` and `f={v,w}`

are distinct incident ordinary edges, orient the corresponding line-graph edge

`e -> f`

exactly when the ordered turn `(u,v,w)` is tight.

Then:

1. `Gamma(H)` is a well-defined orientation of the full line graph `L(K_V)`.
2. A vertex-simple sequence `P=(v_0,...,v_k)` is a tight path in `H` if and only if its consecutive ordinary edges

   `e_i={v_{i-1},v_i}`

   form a directed chain

   `e_1 -> e_2 -> ... -> e_k`

   in `Gamma(H)`.
3. `H` is realizable by a global total order `<` on `E(K_V)` satisfying

   `(u,v,w)` tight iff `{u,v} < {v,w}`

   if and only if `Gamma(H)` is acyclic. In the acyclic case, any topological ordering of `Gamma(H)` gives such an edge order.
4. If `Gamma(H)` is cyclic and `C` is a shortest directed cycle, then `C` is chordless in `L(K_V)`. Its underlying ordinary edges have one of the following forms:
   - a three-edge star about one vertex, giving a directed triangle in the local middle-vertex tournament;
   - the three edges of an ordinary triangle, with all three cyclic turns tight;
   - for length `r>=4`, the edges of a simple ordinary `r`-cycle, with every cyclic consecutive turn tight.

Thus failure of global edge-orderability always has a minimal holonomy certificate of star-triangle or vertex-simple cyclic-turn type.

## Proof

Create one vertex of `Gamma(H)` for each ordinary edge of `K_V`. Two such vertices are adjacent exactly when the ordinary edges meet, so the underlying undirected graph is `L(K_V)`.

If `e={u,v}` and `f={v,w}`, the two possible directions `e->f` and `f->e` correspond respectively to the complete-reversal pair `(u,v,w)` and `(w,v,u)`. Strong Level-(1) boundary antisymmetry says exactly one of these turns is tight. Hence exactly one orientation of every line-graph edge is present, proving (1).

For a vertex-simple sequence `P=(v_0,...,v_k)`, put `e_i={v_{i-1},v_i}`. By definition,

`e_i -> e_{i+1}`

is equivalent to tightness of the consecutive turn

`(v_{i-1},v_i,v_{i+1})`.

Therefore all consecutive turns of `P` are tight exactly when all consecutive comparison arcs point forward. This proves (2), with vertex-simplicity retained explicitly because an arbitrary directed path in the line graph may encode an ordinary trail with repeated original vertices.

Suppose a total order `<` on `E(K_V)` realizes `H`. Every comparison arc `e->f` then points from the earlier edge to the later edge, so `Gamma(H)` is acyclic.

Conversely, suppose `Gamma(H)` is acyclic. Choose any topological total ordering `<` of its vertices. For distinct `u,v,w`, the incident edges `e={u,v}` and `f={v,w}` are adjacent in `Gamma(H)`, and

`e->f` iff `(u,v,w)` is tight.

A topological order puts `e<f` exactly when `e->f`. Thus `<` reproduces every tight turn of `H`, proving (3).

Now suppose `Gamma(H)` is cyclic and choose a shortest directed cycle

`C=e_0 -> e_1 -> ... -> e_{r-1} -> e_0`.

If two nonconsecutive cycle vertices were adjacent in `L(K_V)`, their connecting line-graph edge has one of the two directions. Whichever direction it has, that chord together with one of the two directed segments of `C` would form a shorter directed cycle. Hence `C` is chordless.

For `r=3`, three pairwise incident ordinary 2-subsets are either the three edges of one ordinary triangle or three edges sharing a common ordinary vertex. In the star case, writing them `va,vb,vc` in cyclic comparison order gives

`(a,v,b), (b,v,c), (c,v,a)`

tight. In the ordinary-triangle case, cyclically label the original vertices so the comparison cycle is

`ab -> bc -> ca -> ab`; then

`(a,b,c), (b,c,a), (c,a,b)`

are tight.

For `r>=4`, chordlessness says nonconsecutive ordinary edges of `C` are disjoint while consecutive ones meet. Put

`v_i = e_{i-1} ∩ e_i`

with indices modulo `r`. The `v_i` are distinct and

`e_i={v_i,v_{i+1}}`.

Thus the ordinary edges of `C` are exactly the edges of a simple cycle

`v_0v_1...v_{r-1}v_0`.

Finally `e_i->e_{i+1}` is equivalent to tightness of

`(v_i,v_{i+1},v_{i+2})`

for every `i`. This proves (4). ∎

## Why this is reusable

This theorem gives a global representation dictionary for the entire tight-turn relation. It cleanly separates the **integrable branch**, where the tournament comes from an ordinary total edge order, from the **holonomy branch**, where a shortest comparison cycle provides a concrete obstruction.

It also turns tight paths into directed chains in one canonical auxiliary graph, which makes edge-order arguments and nonintegrability arguments speak the same language.

## Scope and nonclaims

A directed path in `Gamma(H)` need not correspond to a vertex-simple path in the original vertex set; the underlying ordinary walk may repeat vertices.

A shortest comparison cycle is a structural certificate of non-edge-orderability, not by itself a proof of small path-cover number.

## Provenance

Rescued from the accepted representation theorem historically recorded as `R887`. Citation-graph mining found it referenced from **43 distinct corpus files**, despite its vocabulary being too varied to rank near the top of simple phrase frequency.