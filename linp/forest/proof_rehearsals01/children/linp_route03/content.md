# Route 3 — Rotation-expansion and terminal-pair cycle rank

## Statement

Comprehensive synthesis of the Pósa-style rotation and terminal-pair graph route for forcing special-edge density or bounded cycle complexity.

## Body

# Route 3. Rotation-expansion and terminal-pair cycle rank

## Goal and setup

Let H be a P_ℓ-free linear 3-uniform hypergraph with m edges and n vertices. Write s for the number of special edges. For every nonspecial edge e, let x be its unique entrance and let {u,v} be its terminal pair. Because H is linear, two nonspecial edges cannot have the same terminal pair, so the terminal pairs form a simple graph T.

The route seeks a quantitative theorem saying that T cannot contain too many independent cycles unless the corresponding blocker obligations force endpoint expansion, rank growth, extra entrance support, or special edges.

The starting snake inequality is

2m+s ≤ (2ℓ−3)n.      (1)

Thus any lower bound s≥εm−O(n) gives a strict leading improvement below coefficient 1. More strongly, if the nonspecial complexity is O(n), then (1) reaches the two-thirds scale.

The natural measure of that complexity is the cycle rank

β(T)=|E(T)|−|V(T)|+κ(T),

where κ(T) is the number of connected components.

## 1. Why a terminal cycle carries hypergraph structure

Give each edge uv of T the rank of its parent hyperedge. In every connected component choose a spanning tree F of maximum total edge rank.

Let e be a nonforest edge and let C_e be its fundamental cycle in F+e. If some tree edge f on C_e had smaller rank than e, replacing f by e would increase the total tree rank. Therefore

rank(e) ≤ rank(f)

for every tree edge f of C_e. In particular the two cycle-neighbors of e have rank at least rank(e).

Now let e and f be adjacent on C_e, sharing terminal v. Suppose φ(f)≤φ(e), and take a maximum path P witnessing v as a terminal of e. If f met P only at v, then appending f at v would produce a path longer than φ(f), in fact forcing

φ(f) ≥ φ(e)+1,

a contradiction. Hence f must meet P at a second vertex.

Applied on both sides of e, this proves:

**Fundamental-cycle blocker lemma.** Every nonforest edge e has two canonical blocker obligations, one from each neighboring edge of its fundamental cycle.

Since the number of nonforest edges is exactly β(T), one obtains one canonical two-sided blocker certificate per unit of terminal-pair cycle rank.

This is the first substantive reduction: β(T) is not abstract graph cycle rank. Every one of its units is tied to explicit maximum-path contacts in H.

## 2. Rotation primitives

The blocker contacts are useful because they support length-preserving rotations.

Let

P=(e_1,e_2,…,e_p)

be a linear path and let f be an edge outside P meeting e_p and exactly one earlier edge e_j. If j≤p−2, then

(e_1,…,e_j,f,e_p,e_{p−1},…,e_{j+2})

is again a p-edge linear path, with a new endpoint. If j=p−1 there is the analogous one-step replacement.

For a globally longest path ending in a nonspecial edge, the permitted contact positions are even more restricted. A two-contact competitor cannot have its earlier contact exactly two positions before the end, and a single-blocker rotation likewise excludes that position. These localization facts ensure that a genuine blocker normally creates a distinct endpoint or forces an additional contact.

There is also a rank version. If e and f share terminal v and a maximum terminal witness for e meets f only at v, then the absence of a blocker forces a rank jump of at least two. More generally, if p=φ(e), q=φ(f)≤p, and f occupies r vertices of a p-edge witness for e, then

2≤r≤3
and
p≤r(q−1).      (2)

In particular, if p≥2q−1, then all three vertices of f lie on the witness.

Thus failure of a blocker is not harmless: it produces rank growth. The route is designed around this dichotomy:

- blocker contact  →  rotation and endpoint motion;
- no blocker contact  →  quantitative rank increase.

## 3. The cycle-rank hinge

Suppose one could prove

β(T) ≤ C s + D n      (3)

for fixed constants C,D. Combining the number of forest edges with (1) yields

m ≤ [2(C+1)ℓ−3(C+1)+D+1]/(2C+3) · n.      (4)

Hence the leading coefficient would be

2(C+1)/(2C+3)<1.

In the particularly important case β(T)=O(n), equation (4) has leading coefficient 2/3.

This gives the route a precise target: a theorem bounding cycle rank by special-edge mass and linear support complexity is enough to improve the Turán coefficient. One need not classify all cycles individually.

## 4. Entrance support and the incidence bridge

There is a reason special edges alone cannot pay for all cycles. Let h be the number of distinct entrance vertices used by nonspecial edges, and let N_ns be the vertex-edge incidence matrix restricted to nonspecial columns. Then

nullity(N_ns) ≤ β(T)+h.      (5)

For the full incidence matrix N,

nullity(N) ≤ β(T)+h+s.      (6)

The proof is elementary in spirit. Choose a spanning forest of T. Along each tree component, once entrance variables are fixed, the nonspecial incidence columns can be eliminated recursively through the terminal pairs. Each nonforest edge contributes at most one new degree of freedom, and each distinct entrance contributes at most one more. Special columns add at most s further dimensions.

Equations (5)–(6) are important even inside this route. They show the correct complexity parameter is not β(T) alone but approximately

β(T)+h.

Repeated reuse of the same entrance may support many terminal cycles without producing special edges. Any expansion theorem that ignores entrance support will therefore be false.

## 5. Why rotations should control β(T)+h

Take the maximum-total-rank forest F and attach to every nonforest edge its two blocker contacts. Consider grouping the resulting certificates by the path witness, entrance, or tree edge on which they are realized.

If the groups are light, then many certificates live on distinct resources. The rotation primitives should then create many distinct reachable endpoints, contradicting the bounded path rank.

If some group is heavy, many fundamental-cycle obligations reuse the same witness or entrance. The rank-transfer lemmas then force one of three phenomena:

1. repeated edges occupy progressively larger portions of the same witness;
2. rank must increase along the reused structure;
3. unique-entrance behavior breaks, producing specialness or additional entrance support.

This is exactly the Pósa-style mechanism the route seeks. The certified local lemmas establish each individual move, but there is not yet a theorem summing those moves over all β(T) fundamental cycles without losing control to reuse.

## 6. Known obstruction: cycles need not create special edges

The most important failed shortcut is

β(T)≤s.

It is false. There are linear triple systems with no special edges at all whose terminal-pair graph is a disjoint union of copies of K_{3,3}. Each such component has positive cycle rank. The same examples show that nonspecial incidence columns need not be linearly independent.

Therefore a terminal cycle is not itself a contradiction, and no proof may charge every nonforest edge directly to a special edge.

Likewise, one legal rotation is not endpoint expansion. A rotation theorem must control how many rotations collapse onto the same endpoint, path witness, or entrance. This repeated-support phenomenon is the genuine obstruction.

## 7. First unsupported implication

The proof reaches the following precise frontier.

**Rotation-expansion target.** Starting from the maximum-total-rank forest F, assign to every nonforest terminal-pair edge its canonical two-sided blocker obligations. Prove that these β(T) obligations force either

β(T)+h ≤ C s + Dn

for fixed C,D, or an equivalent endpoint-expansion inequality strong enough to imply such a bound.

A weaker theorem controlling β(T) alone would suffice for some coefficient improvements, but the K_{3,3} obstruction shows that a robust statement should explicitly pay for entrance/support reuse.

All ingredients before this point are certified: the blocker transfer, rank-jump alternative, rotation primitives, canonical fundamental-cycle selection, cycle-rank hinge, and incidence-nullity bridge. What is missing is the global bounded-reuse/expansion theorem that composes them.

The attempted proof stops here.

## Research handoff

Begin with a maximum-total-rank spanning forest of T and the canonical blocker obligations on its nonforest chords. Organize certificates by shared entrance and shared witness before performing rotations; otherwise endpoint multiplicity is invisible.

Do not retry β(T)≤s, nonspecial-column independence, bare cycle counting, or an argument in which a single rotation is treated as expansion. A new ingredient must control repeated use of the same entrance or witness.

This route interfaces cleanly with two neighboring philosophies. A bound on β(T)+h feeds the incidence-rank route through (5)–(6), while a strong endpoint-expansion theorem can serve as the rank-flow engine in the dense-core route.