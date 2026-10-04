# Article VII — antipodal geodesics and topological reformulations

---

## Section — Antipodal geometry of permutation space

<!-- section_id: antipodal_permutation_geometry -->

### Permutation simplices and monotone geodesics

Let \(V\) be an \(n\)-element label set. A monotone geodesic from \(\varnothing\) to \(V\) in the \(n\)-cube adds every label exactly once, hence is specified by a permutation
\[
\pi=(v_1,\ldots,v_n),\qquad S_i=\{v_1,\ldots,v_i\}.
\]
The simplex
\[
\Delta_\pi=\operatorname{conv}\{\mathbf 1_{S_0},\ldots,\mathbf 1_{S_n}\}
\]
is one maximal simplex of the standard staircase triangulation of \([0,1]^V\). Its region is
\[
1\ge x_{v_1}\ge \cdots\ge x_{v_n}\ge0.
\]
Thus the maximal simplices are exactly the monotone pole-to-pole geodesics, and adjacent permutation simplices meet along faces obtained by tying coordinate inequalities.

This is the geometric realization of the spanning-order space used throughout the geodesic approach.

### The antipodal link of the long diagonal

Every maximal staircase simplex contains the long diagonal \([\mathbf0,\mathbf1]\). The simplicial link of that diagonal consists of chains of nonempty proper subsets of \(V\), hence is the barycentric subdivision of the boundary of an \((n-1)\)-simplex and therefore an \((n-2)\)-sphere.

Cube complementation \(A(x)=\mathbf1-x\) sends \(\Delta_\pi\) to \(\Delta_{\pi^{\rm rev}}\). On the link it sends a subset chain to its complementary reversed chain and is fixed-point-free. In centered coordinates it is realized by negation on
\[
\mathbf1_S-\frac{|S|}{n}\mathbf1.
\]
So the permutation complex carries the standard antipodal action of the type-\(A\) Coxeter sphere.

This identifies the right topological carrier. Working on the whole cube is too coarse: every odd map has the automatic zero at the cube center, which does not select a distinguished permutation. Any Borsuk-Ulam/Tucker/Sperner-style argument must use the link or an equivalent pole-relative object.

### Triple colors as antipodal local data

Write
\[
h(u,v,w)=
\begin{cases}
1,&(u,v,w)\text{ is tight},\\
0,&(u,v,w)\text{ is non-tight}.
\end{cases}
\]
Boundary reversal is
\[
h(w,v,u)=1-h(u,v,w).
\]
For \(\pi=(v_1,\ldots,v_n)\), the consecutive-triple word is
\[
h(v_1,v_2,v_3),\ldots,h(v_{n-2},v_{n-1},v_n).
\]

The color at a triple of successive directions \(u,v,w\) belongs naturally to the tetrahedral face
\[
S,\quad S\cup\{u\},\quad S\cup\{u,v\},\quad S\cup\{u,v,w\}
\]
of the staircase triangulation and is independent of the base subset \(S\). Complementation reverses the successive directions to \(w,v,u\) and therefore complements the color.

This is the precise common structure with antipodal cube-coloring problems such as the Norine line of ideas: geodesics are permutations, opposite geodesics are reversals, and the local datum flips under the antipode. The important difference is that our color is attached to three consecutive directions, not directly to an ordinary cube edge. Any imported antipodal-path theorem must therefore survive this memory requirement rather than silently forgetting it.

---

## Section — The lifted geodesic graph and one-change orders

<!-- section_id: lifted_geodesic_graph_and_one_change_orders -->

### The memory-lift graph Γ_n

The staircase triangulation identifies spanning orders with cube geodesics, but the color at one step depends on three successive directions. Introduce a graph \(\Gamma_n\) that stores this two-step memory.

Its vertices are poles \(s,t\) and states
\[
(\sigma,S,u,v),
\]
where \(\sigma\in\{0,1\}\), \(u\ne v\), and \(S\subseteq V\setminus\{u,v\}\). Give the state rank \(|S|+1\), with \(r(s)=0\) and \(r(t)=n\). Join \(s\) to every \((\sigma,\varnothing,u,v)\); join
\[
(\sigma,S,u,v)\longrightarrow(\sigma,S\cup\{u\},v,w)
\]
whenever \(w\notin S\cup\{u,v\}\); and join every rank-\(n-1\) state to \(t\).

Color a source edge by \(\sigma\), an internal edge by \(h(u,v,w)\), and a terminal edge by \(1-\sigma\). The underlying graph depends only on \(n\).

### Antipodal involution and cube projection

Define
\[
A(s)=t,\qquad A(t)=s,
\]
and
\[
A(\sigma,S,u,v)=
(\sigma,V\setminus(S\cup\{u,v\}),v,u).
\]
This is a fixed-point-free graph involution. For an internal edge carrying the triple \(u,v,w\), the antipodal edge, read in increasing-rank direction, carries \(w,v,u\); hence its color is complementary by boundary reversal. Source and terminal edges are likewise paired with complementary colors.

There is also an antipodal graph map to the cube,
\[
p(s)=\varnothing,\qquad p(t)=V,\qquad
p(\sigma,S,u,v)=S\cup\{u\}.
\]
Every \(\Gamma_n\) edge projects to a cube edge and \(p(Ax)=V\setminus p(x)\). Thus \(\Gamma_n\) is a finite memory lift of the cube rather than an unrelated auxiliary graph.

### Pole geodesics are spanning orders

Every edge changes rank by one, so \(d(s,t)\ge n\). For every permutation \(\pi=(v_1,\ldots,v_n)\) and each \(\sigma\), there is a length-\(n\) path
\[
s,\quad
(\sigma,S_i,v_{i+1},v_{i+2})\quad(0\le i\le n-2),\quad
t.
\]
Conversely, every \(s\)-\(t\) geodesic must increase rank at every step, so it chooses each label exactly once and hence determines a unique permutation and copy index.

Therefore the pole geodesics are in bijection with pairs \((\sigma,\pi)\), and their color words are
\[
\sigma,\quad h(v_1,v_2,v_3),\ldots,
h(v_{n-2},v_{n-1},v_n),\quad1-\sigma.
\]

It follows immediately that \(H\) has a spanning order whose consecutive-triple statuses change at most once if and only if \(\Gamma_n\) has a pole geodesic with at most one edge-color change. Deleting the two artificial endpoint colors gives one direction; choosing \(\sigma\) to match the first run gives the other.

### Why geodesicity is essential

For any \(s\)-\(t\) walk \(W\), let \(m_v\) be the number of times its projection uses cube coordinate \(v\). Since the projection joins antipodal cube vertices, every \(m_v\) is odd and
\[
|W|=\sum_{v\in V}m_v
=n+2\sum_{v\in V}\frac{m_v-1}{2}.
\]
Thus the geodesics are exactly the walks with \(m_v=1\) for every \(v\).

This is the key constraint behind the analogy with antipodal path theorems. A theorem producing some one-change antipodal walk is insufficient if it allows repeated coordinates; repetition means repeated original vertices. Likewise, an antipodal theorem whose endpoint pair is allowed to vary is insufficient unless its output can be normalized to the distinguished poles \(s,t\). The desired topology must preserve both pole location and zero detour.

---

## Section — Complementary path supports and endpoint involutions

<!-- section_id: complementary_path_supports_and_endpoint_involutions -->

### Opposite terminal edges and complementary supports

For an ordered pair \(u,v\), let \(\mathcal F_{uv}\) consist of the sets \(X\subseteq V\setminus\{u,v\}\) for which some ordering of \(X\), followed by \(u,v\), is a tight path.

A spanning order with status word \(1^a0^b\) exists if and only if for some \(u\ne v\) there are
\[
X\in\mathcal F_{uv},\qquad Y\in\mathcal F_{vu}
\]
that partition \(V\setminus\{u,v\}\). Indeed, the tight prefix ends with \(u,v\), while reversing the non-tight suffix turns it into a tight path ending with \(v,u\). Conversely, two such paths splice into a spanning order whose first block is tight and second block non-tight.

Thus a one-change order is the same object as two tight paths sharing exactly one ordinary edge, traversed in opposite terminal directions, with complementary remaining supports. The \(0^a1^b\) case is the corresponding initial-edge formulation.

### The common-terminal formulation

Equivalently, on a vertex set \(W\), a spanning order with word \(1^a0^b\) exists if and only if there are two tight paths whose union is \(W\), whose intersection is one vertex \(v\), and which both end at \(v\). Either path may be the singleton \(v\).

From paths
\[
P=(p_1,\ldots,p_\ell,v),\qquad
Q=(q_1,\ldots,q_m,v)
\]
one obtains
\[
(p_1,\ldots,p_\ell,v,q_m,\ldots,q_1).
\]
All triples on the first side are tight and all triples on the reversed second side are non-tight; the single central triple may have either status without creating a second change. Conversely, split a one-change order at the change point and reverse its non-tight side.

This common-terminal picture removes the shared edge from the notation and is better adapted to endpoint transport.

### The endpoint-moving involution

Common-terminal pairs on a fixed support carry a fixed-point-free involution. Suppose
\[
P=(A,u,v),\qquad Q=(B,w,v).
\]
Exactly one of \((u,v,w)\) and \((w,v,u)\) is tight. If the first is tight, move \(w\) across the common endpoint:
\[
(A,u,v,w),\qquad(B,w).
\]
The new pair has common terminal vertex \(w\), and applying the same rule there returns to \(v\). The other orientation is symmetric. If one member is the singleton \(v\), the move truncates the other path at its final edge and creates the two-vertex path \((v,u)\); this is again inverted by the same rule.

The two paired common-terminal states are precisely the two truncations of one pair of tight paths that share an oppositely directed terminal edge and are otherwise disjoint. Hence endpoint motion by itself produces matched pairs rather than a longer orbit. Any augmentation argument needs an additional operation beyond this involution.

### Positive support enumeration

In the square-zero algebra
\[
\mathcal A=\mathbb Q[x_v:v\in V]/(x_v^2:v\in V),
\]
define
\[
F_{uv}=\sum_{P\text{ tight ending }u,v}
x_{V(P)\setminus\{u,v\}}.
\]
Then
\[
Z_{\rm end}(H)=\sum_{u<v}x_ux_vF_{uv}F_{vu}
\]
has nonnegative coefficients, and \([x_V]Z_{\rm end}(H)>0\) exactly when there is a spanning order of type \(1^a0^b\). Intersecting tails vanish because of the square-zero variables; complementary tails survive positively. An analogous polynomial \(Z_{\rm start}\) records the \(0^a1^b\) case.

This formulation isolates the unresolved combinatorics as a disjointness problem between opposite endpoint-support families. It is the support-theoretic shadow of the one-change geodesic problem.

---

## Section — Auxiliary-vertex exactification

<!-- section_id: auxiliary_vertex_exactification -->

### The exact one-change extension

Let \(H\) have nonempty vertex set \(V\). Adjoin \(r\), retain all triples of \(H\), and impose
\[
h(u,v,r)=1,\qquad h(r,v,u)=0
\]
for distinct \(u,v\in V\). The values \(h(u,r,v)\) may be chosen arbitrarily subject only to boundary reversal.

Every spanning order of the extension is uniquely
\[
(L,r,R).
\]
If its status word has the directed form \(1^a0^b\), then \(L\) is a tight path: whenever \(|L|\ge2\), its last two vertices followed by \(r\) form a tight triple, so every earlier triple lies in the initial tight run. Likewise \(R^{\rm rev}\) is a tight path because a triple beginning at \(r\) is non-tight, forcing the entire right side into the non-tight run. Deleting \(r\) therefore produces the two-cover
\[
L\mid R^{\rm rev}.
\]

Conversely, from a two-cover \(P\mid Q\), the orders
\[
(P,r,Q^{\rm rev})\qquad\text{and}\qquad(Q,r,P^{\rm rev})
\]
both have status word \(1^a0^b\). The possible triple with \(r\) in the middle can have either status without destroying the one-change form. These two orders are reverses, and no other cover maps to either order.

Hence directed one-change spanning orders of \(H^+\) map two-to-one onto two-covers of \(H\), independently of the local tournament at \(r\).

### The switch and common endpoint normalize to r

The extension does more than create a correspondence: it normalizes the geometry.

For nonempty \(P,Q\), let \(p=|P|\) and
\[
\epsilon=h(\operatorname{last}(P),r,\operatorname{last}(Q)).
\]
In the order \((P,r,Q^{\rm rev})\), the number of initial tight triple positions is
\[
a=p-1+\epsilon.
\]
Thus the ordinary edge straddling the change contains \(r\). The switch location is forced by the extension.

Likewise, every tight path containing \(r\) has at most one vertex after \(r\), because any triple beginning at \(r\) is non-tight. Therefore any pair of tight paths sharing an oppositely directed terminal edge and covering \(V\cup\{r\}\) must share an edge containing \(r\). Under the endpoint-moving involution, exactly one of its two common-terminal states ends at \(r\). Removing \(r\) from that normalized state gives a two-cover of \(H\).

So neither the switch position nor the common endpoint needs to be found by a separate search once the extension is made.

### Exact positive factorization

Let
\[
F_H=\sum_{P\text{ nonempty tight in }H}x_{V(P)}
\]
in the square-zero algebra, with path orders counted separately. For \(S\subseteq V\), let \(m_r(S)\) be the number of orders of \(S\cup\{r\}\) having directed one-change word \(1^a0^b\). Applying the exact extension to every induced subtournament yields
\[
\boxed{\sum_{S\subseteq V}m_r(S)x_S=(1+F_H)^2.}
\]
The constant term is the singleton order \(r\); \(2F_H\) corresponds to a single path placed on either side of \(r\); and \(F_H^2\) corresponds to two disjoint nonempty paths on opposite sides. There is no cancellation.

In particular,
\[
m_r(V)=2[x_V]\left(F_H+\frac12F_H^2\right).
\]
The left side is positive exactly when \(H\) has a one- or two-path cover. The factorization therefore identifies the count exactly, although it does not itself prove positivity.

### The exact geodesic form of the grand conjecture

Apply the \(\Gamma\)-construction to \(H^+\) and keep only the copy \(\sigma=1\). Its pole geodesics have color words
\[
1,\ h(w_1,w_2,w_3),\ldots,h(w_{n-1},w_n,w_{n+1}),\ 0.
\]
Such a word changes color exactly once if and only if its internal word has directed form \(1^a0^b\).

Therefore the grand two-cover conjecture is equivalent to the following single-copy antipodal-geodesic statement:

> For every boundary tournament \(H\), after adjoining \(r\) with \(h(u,v,r)=1\), the \(\sigma=1\) memory-lift graph of \(H^+\) contains a one-change geodesic from its distinguished source pole to its distinguished target pole.

The local tournament at \(r\) may be chosen arbitrarily, for example transitively. This is the key exactification: topology is no longer being asked to prove the potentially stronger one-change assertion on \(H\) itself.

---

## Section — Cyclic strengthenings and balanced-cut obstructions

<!-- section_id: cyclic_strengthenings_and_balanced_cut_obstructions -->

### Why the two-component cycle target fails

A natural first attempt at importing antipodal path ideas was to seek a spanning cycle whose cyclic transition-color word has at most two monochromatic components. This would be sufficient for a two-cover, but it is not necessary.

There is an infinite family of edge-orderable boundary tournaments \(H_s\) on \(4s\) vertices with
\[
\operatorname{pc}(H_s)=2,
\qquad
\min_C \rho_{H_s}(C)=4,
\]
where \(\rho_H(C)\) is the cyclic monochromatic-component count. The same \(H_s\) nevertheless admits a spanning linear order whose triple-status word changes exactly once.

The construction partitions the vertices into four equal classes \(A,B,C,D\) and orders ordinary edges by four levels: within-class; \(AB,CD\); \(AC,BD\); \(AD,BC\). Suitable within-level orders make two alternating level-three paths tight and give a two-cover.

### Balanced cuts force four components

In an edge-ordered model, a Hamilton cycle with at most two transition-color components has a unimodal cyclic sequence of edge ranks: from its unique minimum the ranks increase to the unique maximum and then decrease. Hence for every rank threshold, the cycle edges above that threshold form one cyclic interval.

Now let a Hamilton cycle meet a balanced partition \(U\mid W\). If all crossing edges form one cyclic interval, degree counting gives the same number of internal cycle edges on the two sides. But the complementary interval of internal edges, if nonempty, lies entirely in one side, a contradiction. Therefore every cycle edge must cross the partition.

Applying this first to \(A\cup B\mid C\cup D\) forces all edges to have level at least two. Applying it next to \(A\cup C\mid B\cup D\) forces all edges to have level three. The level-three graph is the disjoint union of the complete bipartite graphs on \(A,D\) and on \(B,C\), so it has no Hamilton cycle. Thus no spanning cycle has two transition-color components.

This obstruction is structural, not a small-order accident; it occurs for every \(s\ge1\).

### The exact cyclic defect-graph formulation

For an oriented Hamilton cycle \(Z=(v_1,\ldots,v_n,v_1)\), let \(e_i=\{v_i,v_{i+1}\}\). Define the blue-transition defect graph \(D_Z\) on the cycle-edge positions \(e_i\) by adding \(\{e_{i-1},e_i\}\) exactly when \((v_{i-1},v_i,v_{i+1})\) is non-tight.

Cutting a nonempty set \(S\) of cycle edges leaves \(|S|\) inherited path components. Every resulting component is tight exactly when \(S\) meets every edge of \(D_Z\), i.e. exactly when \(S\) is a vertex cover of \(D_Z\). Hence
\[
\operatorname{pc}(H)
=
\min_Z \max\{1,\tau(D_Z)\}.
\]
In particular,
\[
\operatorname{pc}(H)\le2
\iff
\text{some cyclic order }Z\text{ has }\tau(D_Z)\le2.
\]

This is the correct cyclic reformulation. It allows several separated blue runs provided two cut positions hit them all, which is exactly the information lost by counting monochromatic components alone.

---

## Section — Antipodal reachability and the topological frontier

<!-- section_id: antipodal_reachability_and_topological_frontier -->

### The antipodal self-intersection criterion

Work in the \(\sigma=1\) copy of the memory-lift graph for the auxiliary-vertex extension, and orient every graph edge from lower rank to higher rank. Let \(R\) be the set of states reachable from \(s\) by an increasing path using only red edges.

Because the antipodal involution reverses rank and complements color, \(A(R)\) is exactly the set of states \(x\) from which there is an increasing blue path from \(x\) to \(t\). Indeed, a red increasing path from \(s\) to \(y\) maps under \(A\) to a blue decreasing path from \(t\) to \(A(y)\); reversing it gives a blue increasing path from \(A(y)\) to \(t\), and conversely.

Therefore
\[
\boxed{\text{a red-then-blue pole geodesic exists}
\iff R\cap A(R)\ne\varnothing.}
\]
If \(x\in R\cap A(R)\), concatenate a red increasing path from \(s\) to \(x\) with a blue increasing path from \(x\) to \(t\). Rank increases at every step, so the resulting path has length equal to the pole distance and is automatically geodesic. The converse is immediate from the switch state of any such geodesic.

By the auxiliary-vertex exactification, the grand two-cover conjecture is equivalent to this antipodal self-intersection statement.

### The neutral corridor forced by a counterexample

Assume for contradiction that \(R\cap A(R)=\varnothing\). Put
\[
N=V(\Gamma)\setminus(R\cup A(R)).
\]
Then \(A(N)=N\), so \(N\) is antipodally invariant.

Moreover there is no edge, in increasing-rank direction, directly from \(R\) to \(A(R)\). Such an edge cannot be red, because its upper endpoint would then lie in \(R\); and it cannot be blue, because its lower endpoint would then have a blue increasing route through the upper endpoint to \(t\), placing it in \(A(R)\). Since the underlying ranked graph connects the poles, every pole-to-pole path must therefore pass through \(N\). In particular \(N\ne\varnothing\).

The colors on the two interfaces are forced. Any increasing edge from \(R\) to \(N\) is blue, while any increasing edge from \(N\) to \(A(R)\) is red. The antipode exchanges these two frontiers. Thus a counterexample produces an antipodally symmetric separating corridor with opposite prescribed colors on its lower and upper boundary.

This is substantially more rigid than the bare failure of one chosen geodesic. It turns the conjecture into a separation problem in a fixed antipodal ranked complex.

### What a topological proof must actually show

The current topology program is therefore not “find any antipodal path.” It is to rule out the antipodally invariant corridor \(N\) in the ranked memory lift arising from a boundary tournament extension.

Three constraints must be preserved simultaneously:

1. **Distinguished poles.** The output must connect the prescribed source and target, not an arbitrary antipodal pair.
2. **Geodesicity.** Rank must increase at every step, equivalently every original coordinate/vertex is used exactly once.
3. **Memory compatibility.** Edge color in the lift represents a triple of successive cube directions, so a theorem on ordinary cube-edge colorings cannot be applied without carrying the two-step state.

The staircase link supplies an antipodal \((n-2)\)-sphere of permutations, while the reachability criterion supplies an antipodal separation \(R\mid N\mid A(R)\). A plausible closure route is to convert this separation into an antipodal labeling or continuous odd map on the link and then show that Tucker/Borsuk-Ulam/Sperner-type parity forces a forbidden self-intersection or a simplex encoding a red-blue geodesic switch.

What remains unproved is precisely that last implication. The corridor formulation is intended to make the needed topological statement sharp enough to attack directly.

### Relation to the Norine geodesic analogy

The conceptual analogy with antipodal cube-coloring problems remains useful but should be stated at the right level. In both settings, the desired object is an antipodal geodesic constrained to use each coordinate exactly once, and the staircase triangulation turns the family of such geodesics into a simplicial decomposition indexed by permutations.

The strengthened Norine-style intuition—seek an antipodal path whose coordinate directions are all used exactly once—matches exactly the role of geodesicity here. What is special in the present problem is that the coloring is induced by consecutive triples of directions and therefore naturally lives on the memory lift rather than on the bare cube.

The strongest transferable idea is thus not a literal theorem statement but the topological architecture: antipodal symmetry, a sphere of geodesic order types, and a parity/fixed-point mechanism that should prevent an antipodal separation compatible with all local labels. The reachability corridor identifies the concrete separation that such a mechanism would need to forbid.
