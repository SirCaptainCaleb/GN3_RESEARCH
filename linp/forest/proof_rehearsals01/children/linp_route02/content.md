# Route 2 — Dense-core all-special / ascending-edge rank flow

## Statement

Comprehensive synthesis of the two-thirds upper-bound program based on dense-core normalization, elimination of nonspecial ascending edges by rank layers, and all-special closure.

## Body

# Route 2. Dense-core all-specialness and ascending-edge rank flow

## Goal and setup

This route seeks the two-thirds upper coefficient. Let H be an n-vertex P_ℓ-free linear 3-uniform hypergraph with m edges. For a vertex v let φ(v) be the maximum length of a linear path ending at v, and for an edge e let φ(e) be the maximum length of a linear path ending in e. A nonspecial edge e has a unique entrance x; it is ascending when φ(x)=φ(e)−1, the remaining two vertices being terminals.

The route begins with the standard density-core reduction. If an extremal inequality m≤dn is hereditary, then a counterexample contains an induced subhypergraph of density at least d and minimum degree greater than d. Thus, for a two-thirds theorem, it is enough to work in a dense core with minimum degree just above 2ℓ/3.

The ideal conclusion is that every edge of such a core is special. That conclusion is stronger than necessary. The actual quantitative target is to show that the number of ascending nonspecial edges is lower order, or equivalently that each high-rank vertex supports only a sublinear number of ascending terminal incidences.

## 1. The global defect is exactly the ascending mass

Let A denote the number of ascending nonspecial edges. The basic snake-incidence count gives

3m − A ≤ Σ_v (2φ(v)−1) ≤ (2ℓ−3)n.      (1)

The reason for the single defect A is exact: for an incident pair (v,e), one always has φ(e)≤φ(v)+1, and equality occurs precisely when e is nonspecial ascending and v is its unique entrance. Thus every incidence behaves as in the all-special count except the unique entrance incidence of an ascending edge.

Consequently

m ≤ ((2ℓ−3)/3)n + A/3.      (2)

Hence the leading two-thirds coefficient follows as soon as

A=o(ℓ n).      (3)

A convenient sufficient local statement is the following. Let c(v) be the number of ascending nonspecial edges for which v is a terminal. If c(v)≤g(φ(v)) for every v, then, because each ascending edge has two terminals,

A ≤ (1/2)Σ_v c(v) ≤ (n/2)g(ℓ−1),

and therefore

m ≤ ((2ℓ−3)/3 + g(ℓ−1)/6)n.      (4)

In particular, any uniform bound g(p)=o(p) proves the two-thirds leading coefficient. A square-root bound already suffices with only a lower-order loss. Thus the route does not require literal all-specialness; it requires summable control of the ascending defect.

## 2. Rank superlevels turn ascending edges into flow

For t≥1 define the vertex-rank superlevel

V_t={v:φ(v)≥t}.

Among hyperedges of rank at least t, the edges crossing the cut V_t are exactly the rank-t ascending nonspecial edges: their unique entrance lies outside V_t and their two terminals lie inside V_t. Thus every ascending edge is a boundary-crossing object at exactly one rank.

There are two equivalent ways to encode this flow.

First, orient every ascending edge from its entrance x toward each terminal. Along any directed path in this orientation, vertex rank rises strictly; a directed path of length r therefore yields rank increase at least r and, in particular, a hypergraph path of length at least r.

Second, fix a threshold t and form the graph R_t on terminal vertices by joining the two terminals of every ascending nonspecial edge whose entrance has rank below t and whose terminals have rank at least t. Color the terminal pair by its entrance. Linearity makes this coloring proper. Moreover R_t contains no rainbow t-edge path: such a path would lift through its distinct entrance colors to a hypergraph path of length t whose endpoint ranks contradict the definition of the threshold.

Thus an ascending edge cannot wander arbitrarily through rank space. It either crosses a superlevel, participates in a proper-colored rainbow-free terminal graph, or lies on a strictly rank-increasing directed chain.

A stronger certified form is useful when the entrance-to-terminal rank gap is positive. If an edge e has entrance potential a(e) and the smaller terminal potential p(e)>a(e), then the positive-gap threshold graphs imply the global harmonic estimate

Σ_e (1/a(e) − 1/p(e)) = O(n log ℓ),      (5)

with an explicit certified constant. This already controls edges that make a substantial multiplicative rank jump. Therefore the genuine leading-order difficulty is concentrated where the entrance and terminal ranks are close.

## 3. Local packing near a terminal

Fix a vertex v with p=φ(v). Assign every ascending nonspecial edge e={x,v,u} to a terminal of minimum terminal rank; then φ(u)≥p. Such an assigned edge will be called charged at v.

Every maximum p-edge path ending at v contains x or u, and for distinct charged edges the pairs {x,u} are disjoint. If C_Q(v) denotes the charged edges of rank at most Q, where

⌈(p+2)/2⌉ ≤ Q ≤ p,

then the central-window packing theorem gives

|C_Q(v)| ≤ 4Q−2p−1.      (6)

Equivalently, if the charged ranks are q_1≤⋯≤q_k, then

q_i ≥ ⌈(2p+i+1)/4⌉.      (7)

This already rules out a large low-rank packet at one terminal. A sharper spacing theorem applies to clean entrance-only contacts on a chosen maximum path: if their rank deficit is at least D, then only

O(p/(D+1)+1)

such edges can occur. Hence all but a lower-order part of any large charged family lies in a narrow near-top rank band.

There is an important conditional benchmark here. A suitable four-edge convex spacing inequality for four charged edges at one terminal would imply

c(v)≤3+⌈log_2 p⌉

and hence, by (4),

m ≤ ((2ℓ+⌈log_2(ℓ−1)⌉)/3)n.

So a logarithmic terminal-degree theorem is already enough for the two-thirds leading coefficient. However the required spacing statement is not presently proved, and several tempting stronger variants are false even for clean strict-rise families. The spacing program therefore identifies a sufficient mechanism, not an established closure.

## 4. Rotation reduction of the remaining defect

The rank-flow picture can be combined with longest-path rotations to isolate the surviving obstruction more sharply.

For every nonspecial nonascending edge f with unique entrance x, define

r(f)=⌈φ(x)/(φ(f)−1)⌉−2,

and put R=Σ_f r(f). Then

3m−A+R ≤ Σ_v(2φ(v)−1) ≤ (2ℓ−3)n.      (8)

Thus nonascending nonspeciality already pays an explicit positive correction. The hard mass is ascending.

Now fix for each v a maximum p=φ(v) path P_v ending at v and assign every ascending edge to a minimum-rank terminal v. Apart from at most one last edge per vertex, every assigned edge falls into one of three path-relative types:

- D: both the entrance x and opposite terminal u lie on P_v;
- X: x lies on P_v and u lies off P_v;
- U: u lies on P_v and x lies off P_v.

Let B be the double-blocker compensation, and let S_X,S_U be the total numbers of X- and U-edges. Then

A ≤ B+S_X+S_U+n,      (9)

and, writing N=(2ℓ−3)n,

5m+s+R ≤ 2N+S_X+S_U+n,      (10)

where s is the number of special edges.

For every fixed ε>0, the X-edges with

φ(e) ≤ (1−ε)φ(v)

contribute only O_ε(n). Thus the X-obstruction is again forced into the near-top rank band.

The U-edges have a different structure. A terminal-only U-edge gives a length-preserving Pósa rotation of P_v. For a fixed charged pair (P_v,v), the resulting canonical rotated endpoints have potential at least p, and each endpoint is produced by at most two U-edges. Consequently

|U(P_v,v)| ≤ 2|W(P_v,v)|+1,      (11)

where W(P_v,v) is the set of resulting high-potential endpoints.

Equations (8)–(11) reduce the leading-order problem to two related phenomena:

1. near-top clean entrance chords whose rank deficit is too small for the harmonic and spacing bounds to dispose of them; and
2. large families of high-potential Pósa endpoints whose overlap across different centers has not been controlled.

This is the current strongest certified compression of the route.

## 5. The dense-core stability branch

There is a second organization of the same obstruction. Along a longest path, let U_v be the available terminal capacity at a vertex v and S_v the actually occupied terminal incidence. The exact local identity

U_v−S_v = 2(L−d_H(v))

shows that in a dense minimum-degree core the amount of unused terminal capacity is small whenever d_H(v) is close to the longest-path length L.

This creates a natural dichotomy.

If many vertices have substantial unused capacity, the resulting open blocker defects should support rotations and endpoint expansion. If very few defects remain, the local incidence structure is forced toward a near-saturated, punctured-Steiner-type configuration in which almost every allowable pair is already occupied. The latter regime is highly rigid and is the natural home of the zero-slack and blocker-matching normal forms developed elsewhere in LINP.

This dichotomy is presently a strategy rather than a theorem closing the route. Its value is that it explains why the same two enemies keep reappearing: either rotations must expand, or near-saturation must become globally impossible.

## 6. Known obstructions

Several apparently simpler arguments are already ruled out.

The minimum-degree hypothesis is essential: sparse star-type examples defeat unrestricted all-specialness. The full ascending terminal graph need not be rainbow-P4-free, even inside one equal-potential level, so one cannot apply an ordinary rainbow-path theorem globally. Nor is the ascending terminal graph necessarily a forest or pseudoforest.

The old idea that every proper rank superlevel contributes a free positive boundary defect is false; the correct induced-core identity contains an explicit correction term. A universal tiny common-terminal degree is also false: one vertex can support several ascending terminal edges. Likewise, nonspeciality does not automatically propagate toward the maximum-rank terminal.

Finally, naive four-edge spacing is too strong. There are clean strict-rise charged families violating simple spacing inequalities. Any successful spacing theorem must use the precise charged geometry or an additional certificate, not only the ordered edge ranks.

These fences eliminate the most tempting shortcuts but leave the rank-flow philosophy intact.

## 7. First unsupported implication

The proof reaches the following exact frontier.

**Cross-rank progress target.** In a P_ℓ-free dense core of minimum degree above the two-thirds threshold, prove that every macroscopic family of ascending nonspecial edges must satisfy at least one of the following:

1. it creates a positive proportion of special edges;
2. it pays a summable rank or blocker defect, enough to make A=o(ℓ n);
3. its members move monotonically through rank bands into fresh high-potential endpoints or stricter terminal configurations, with bounded global reuse.

Equivalently, it is enough to prove a uniform sublinear terminal bound

c(v)=o(φ(v))

or any theorem implying A=o(ℓ n).

The certified harmonic estimate handles genuine positive gaps, the central-window theorem handles substantial rank deficit, and the rotation reduction turns terminal-only mass into high-potential endpoints. What is not proved is the global termination or bounded-overlap statement for the narrow near-top band. The argument stops there.

## Research handoff

The strongest next target is a theorem controlling overlap of the near-top clean chords and Pósa endpoint packets across centers, or a monotone rank-band transfer theorem showing that repeated failure to become special consumes fresh global resources. A full all-special theorem would close the route, but it is stronger than necessary.

Do not retry unrestricted all-specialness, global rainbow-P4-freeness, free superlevel-defect summation, or generic four-edge spacing. The rank-flow machinery has already isolated the useful part of those ideas. The remaining issue is theorem-wide progress and reuse, not another local constant improvement.

Status note: the global defect identity, threshold graphs, positive-gap harmonic estimate, central packing, and rotation localization used above are certified. The dense-core defect-stability dichotomy and the strongest four-edge spacing formulation remain proposal-level ingredients and have been marked as such.