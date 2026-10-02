# Path restriction and intersection calculus

**Summary:** Tight paths satisfy canonical restriction and intersection rules, together with a maximum-path splicing lemma that forces a two-sided extension.

## Statement

Canonical restriction, deletion, relative-order and extended-end intersection lemmas for tight paths, together with a maximum-path splicing lemma that forces a two-sided extension of one ordered pair from two disjoint maximum paths.

## Body

# Path restriction and intersection calculus

Throughout the boundary-tournament statements below, `H` is arbitrary.

If `P=(v_0,...,v_k)` and `w∉V(P)`, write `(w,P)` for `(w,v_0,...,v_k)` and `(P,w)` for `(v_0,...,v_k,w)`. A **left-extended path** is a pair `(w;P)` for which `(w,P)` is tight. A **right-extended path** is a pair `(P;w)` for which `(P,w)` is tight.

For a tight path `P=(p_0,...,p_k)`, an **ordered edge of `P`** is an ordered pair `(p_i,p_{i+1})`. A tight triple `(x,y,z)` **reverses an ordered edge of `P`** if `(z,y)` or `(y,x)` is an ordered edge of `P`.

## 1. Restricting an extended path

Let `(w;P)` be a left-extended path, where

`P=(v_0,...,v_k)`.

Let `Q` be a tight path meeting `P` but not containing `v_0`, and let

`i=min{j : v_j∈V(Q)}`.

Then

`P'=(v_0,...,v_{i-1})`

is a nonempty tight path disjoint from `Q`, and `(w;P')` is left-extended by the same vertex `w`.

If `(P;w)` is right-extended and `Q` meets `P` but avoids `v_k`, let

`j=max{h : v_h∈V(Q)}`.

Then

`P''=(v_{j+1},...,v_k)`

is a nonempty tight path disjoint from `Q`, and `(P'';w)` is right-extended by the same vertex `w`.

**Proof.** Since `Q` avoids `v_0`, the first intersection index satisfies `i>=1`. The sequence `(w,v_0,...,v_{i-1})` is an initial segment of the tight path `(w,P)`, so it is tight. The definition of `i` gives disjointness from `Q`.

For the right-extended case, `Q` avoids `v_k`, so `j<=k-1`. The sequence `(v_{j+1},...,v_k,w)` is a terminal segment of the tight path `(P,w)`, so it is tight. The definition of `j` gives disjointness from `Q`. ∎

## 2. End-interval inheritance

Let `P=(v_0,...,v_k)` be a tight path.

If `(w,P)` is tight and some but not all vertices of `P` are deleted, let

`I=(v_i,...,v_j)`

be the first nonempty interval that remains in the order of `P`. Then `I` is left-extended by `w` when `i=0`, and by the deleted predecessor `v_{i-1}` when `i>0`.

If `(P,w)` is tight and `J=(v_i,...,v_j)` is the last nonempty interval that remains, then `J` is right-extended by `w` when `j=k`, and by the deleted successor `v_{j+1}` when `j<k`.

**Proof.** If `i=0`, `(w,I)` is an initial segment of `(w,P)`. If `i>0`, `(v_{i-1},I)` is a contiguous subpath of `P`.

If `j=k`, `(J,w)` is a terminal segment of `(P,w)`. If `j<k`, `(J,v_{j+1})` is a contiguous subpath of `P`. ∎

If `F` is an ordinary graph and `S⊆V(F)`, write `F-S` for the induced subgraph on `V(F)-S`, `deg_F(v)` for the ordinary degree of `v`, `e_F(S)` for the number of ordinary edges of `F` with both endpoints in `S`, and `comp(F)` for the number of connected components of `F`, counting isolated vertices.

## 3. Counting components after deletion

Let `F` be an ordinary path forest with `k` components and let `S⊆V(F)`. Then

`comp(F-S)=k+sum_{v in S}(deg_F(v)-1)-e_F(S)`.


If `F` is the ordinary path forest of a tight-path cover, every nonempty component of `F-S` inherits from its path component before deletion a tight vertex order.

**Proof.** Let `N=|V(F)|`. Since `F` is a path forest with `k` components, it has `N-k` edges. Deleting `S` removes

`sum_{v in S} deg_F(v)-e_F(S)`

edges: the degree sum counts an edge internal to `S` twice, so one copy must be subtracted. The remaining graph has

`N-|S|`

vertices and

`N-k-sum_{v in S}deg_F(v)+e_F(S)`

edges. A forest has number of components equal to vertices minus edges, which gives the displayed formula. Tightness of inherited path orders follows because every surviving component is a contiguous subpath of an original tight path. ∎

## 4. Reversed order of common vertices

Let `P=(v_0,...,v_k)` and `Q` be tight paths. Suppose the common vertices of `P,Q` do not occur in the same relative order. Then at least one of the following exists:

1. an ordered edge of `Q` that is the reverse of an ordered edge of `P`;
2. a tight triple on `V(P)∪V(Q)` that reverses an ordered edge of one of the two paths at an intersection with the other;
3. a vertex-simple tight cycle on `V(P)∪V(Q)`.

In particular the lemma applies to two different Hamilton orders on the same vertex set.

**Proof.** Read the common vertices in their order along `Q`. Since the relative orders disagree, there are two consecutive common vertices along `Q`, say `v_i,v_j`, with `i>j`. Let `E` be the subpath of `Q` from `v_i` to `v_j`. By choice, the interior of `E` contains no vertex of `P`.

If `E` is the single ordinary edge from `v_i` to `v_j` and `i=j+1`, outcome 1 holds. Otherwise let `x` be the successor of `v_i` on `E` and `y` the predecessor of `v_j` on `E`. Since `i>j`, we have `i>=1` and `j<=k-1`, so the triples

`(v_{i-1},v_i,x)`, `(y,v_j,v_{j+1})`

are defined. If either is not tight, boundary antisymmetry gives its tight reverse, which gives outcome 2. If both are tight, traverse `E` from `v_i` to `v_j`, then traverse `P` from `v_j` to `v_{i-1}`, and close to `v_i`. The two displayed tight triples supply the joins. The interior of `E` is disjoint from `P`, so the resulting tight cycle is vertex-simple. ∎

## 5. Intersection at an extended end

Let `(w;P)` be a left-extended path with

`P=(v_0,...,v_k)`,

and let `Q` be a tight path containing `v_0`. Then at least one of the following exists:

1. a tight path properly containing `P` as an ordered subpath;
2. a tight path properly containing `Q` as an ordered subpath;
3. a vertex-simple tight cycle;
4. a tight triple that reverses an ordered edge of `P` or `Q`.

All vertices in the conclusion lie in `V(P)∪V(Q)∪{w}`.

The same four alternatives hold if `(P;w)` is right-extended and `Q` contains `v_k`; again all vertices in the conclusion lie in `V(P)∪V(Q)∪{w}`.

**Proof.** First suppose `(w;P)` is left-extended. If `k=0`, then either `Q=(v_0)`, in which case `(w,v_0)` is a tight path properly containing both `P` and `Q`, or `Q` properly contains `P`. Hence assume `k>=1`.

If the common vertices of `P,Q` occur in different relative orders, apply Section 4. Outcomes 2 and 3 there already suffice. If outcome 1 there gives a reversed common edge, choose a consecutive tight triple of `(w,P)` containing that edge. Such a triple exists because `(w,P)` has order at least three. This gives outcome 4 here.

Now assume the common vertices occur in the same order. Since `Q` contains `v_0`, the vertex `v_0` is the first common vertex along `Q`.

If `Q` has a predecessor `u` immediately before `v_0`, test `(u,v_0,v_1)`. If it is tight, the initial segment of `Q` ending at `v_0` followed by `P` is a tight path properly containing `P`; the initial segment has no other vertex of `P`. If it is not tight, `(v_1,v_0,u)` is tight and gives outcome 4.

It remains that `Q` starts at `v_0`. If `Q=(v_0)`, then `(w,v_0)` properly contains `Q`. Otherwise write the next vertex of `Q` as `q_1`. If `w∉V(Q)`, test `(w,v_0,q_1)`. If it is tight, `(w,Q)` properly contains `Q`; otherwise `(q_1,v_0,w)` is tight and gives outcome 4.

Finally suppose `w∈V(Q)`. The paths `(w,P)` and `Q` contain the common vertices `w,v_0` in opposite orders. Apply Section 4 to these two paths. Its tight-triple outcome gives outcome 4 here, its cycle outcome gives outcome 3, and its reversed-edge outcome can be placed in a consecutive tight triple of `(w,P)`, giving outcome 4.

Now suppose `(P;w)` is right-extended. If `k=0`, then either `Q=(v_0)`, in which case `(v_0,w)` is a tight path properly containing both `P` and `Q`, or `Q` properly contains `P`. Hence assume `k>=1`.

If the common vertices of `P,Q` occur in different relative orders, apply Section 4. Outcomes 2 and 3 there already suffice. If outcome 1 there gives a reversed common edge, choose a consecutive tight triple of `(P,w)` containing that edge. Such a triple exists because `(P,w)` has order at least three. This gives outcome 4 here.

Now assume the common vertices occur in the same order. Since `Q` contains `v_k`, the vertex `v_k` is the last common vertex along `Q`.

If `Q` has a successor `u` immediately after `v_k`, test `(v_{k-1},v_k,u)`. If it is tight, `P` followed by the terminal segment of `Q` beginning at `v_k` is a tight path properly containing `P`; that terminal segment has no other vertex of `P`. If it is not tight, `(u,v_k,v_{k-1})` is tight and gives outcome 4.

It remains that `Q` ends at `v_k`. If `Q=(v_k)`, then `(v_k,w)` properly contains `Q`. Otherwise write the preceding vertex of `Q` as `q`. If `w∉V(Q)`, test `(q,v_k,w)`. If it is tight, `(Q,w)` properly contains `Q`; otherwise `(w,v_k,q)` is tight and gives outcome 4.

Finally suppose `w∈V(Q)`. The paths `(P,w)` and `Q` contain the common vertices `v_k,w` in opposite orders. Apply Section 4 to these two paths. Its tight-triple outcome gives outcome 4 here, its cycle outcome gives outcome 3, and its reversed-edge outcome can be placed in a consecutive tight triple of `(P,w)`, giving outcome 4. ∎



# Maximum-path splicing

This lemma is adapted from the last-out-edge argument in Devine--Milans, Tight paths in fully directed hypergraphs, Lemma noDisjointMaxPaths. The published argument uses the stronger local rule available in triangle-free (3,4)-tournaments. In a boundary tournament that final contradiction is unavailable, but reversal antisymmetry leaves a useful local configuration.

## Lemma

Let H be a boundary tournament, and let A=(a_1,...,a_t) and B=(b_1,...,b_t) be vertex-disjoint tight paths of globally maximum order t.

Then there are distinct vertices p,q,r in V(A) union V(B) for which (r,p,q) and (p,q,r) are both tight.

If two distinct witnesses r,s work for the same ordered pair (p,q), then (r,p,q,s) and (s,p,q,r) are tight four-vertex paths.

## Proof

Call a triple an A-out triple when it has the form (a_j,a_{j+1},b_u) with u in {j,j+1}; define B-out triples symmetrically.

Suppose first that some out triple is tight. Choose a tight out triple whose path-edge index is maximal, and subject to that whose third-vertex index is maximal. Exchange A and B if necessary, so it is (a_j,a_{j+1},b_u), u in {j,j+1}.

If u=t, then j=t-1 and (a_1,...,a_t,b_t) is a tight path of order t+1, impossible. Hence u<t.

The attempted concatenation (a_1,...,a_{j+1},b_u,b_{u+1},...,b_t) has more than t vertices. All consecutive triples are known tight except possibly (a_{j+1},b_u,b_{u+1}), so this triple is non-tight and (b_{u+1},b_u,a_{j+1}) is tight.

The cyclic shift (b_u,b_{u+1},a_{j+1}) is a B-out triple. If it were tight, then when u=j+1 its path-edge index would exceed j, and when u=j its third-vertex index would exceed u. Either contradicts extremality. Hence it is non-tight, and (a_{j+1},b_{u+1},b_u) is tight.

Take p=b_{u+1}, q=b_u, r=a_{j+1}.

Now suppose there is no tight out triple. The alternating word a_t,b_t,a_{t-1},b_{t-1},...,a_1,b_1 has 2t vertices and cannot be tight. Choose a non-tight consecutive triple.

If it is (a_j,b_j,a_{j-1}), then its cyclic shift (a_{j-1},a_j,b_j) is an A-out triple and is also non-tight. Reversing both gives (a_{j-1},b_j,a_j) and (b_j,a_j,a_{j-1}) tight, so take p=b_j, q=a_j, r=a_{j-1}.

The other possible turn, (b_j,a_{j-1},b_{j-1}), is symmetric and yields the same two-sided pattern.

Finally, if distinct r,s both extend the same ordered pair on both sides, the two consecutive triples of (r,p,q,s) are (r,p,q),(p,q,s), and those of (s,p,q,r) are (s,p,q),(p,q,r). ∎

## Relevance to GN3

Ordinary path-order disagreement can yield a reversed edge, reversing triple, or cycle. This maximum-path argument can yield a stronger local configuration: one ordered pair extendable on both sides by the same witness. Repetition of that ordered pair immediately creates two opposite tight four-vertex paths.

This does not itself give a spanning two-cover. Its possible use is to convert repeated order-disagreement data into a form that interacts directly with path ends.

## Metadata

- ID: pathcalc01
- Kind: toolkit
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
