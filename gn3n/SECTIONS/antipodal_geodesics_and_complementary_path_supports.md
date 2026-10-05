# Antipodal geodesics and complementary path supports

**Summary:** Adding one vertex makes the red-then-blue geodesic target exactly equivalent to the original two-cover conjecture. Every successful order automatically locates its change beside the added vertex; each cover gives exactly two reverse orders. The earlier one-change target on the original vertices may be stronger.

## Statement

Spanning one-change orders admit exact descriptions by antipodal pole geodesics and by two tight paths with a common terminal or initial vertex. After adjoining r with every (u,v,r) tight, red-then-blue spanning orders are in a two-to-one correspondence with two-covers of the original tournament, independently of the local tournament at r. Their subset generating polynomial is (1+F_H)^2. The resulting single-copy geodesic existence assertion is equivalent to the grand two-cover conjecture; existence remains unproved.

## Cold composition

### The staircase triangulation and its antipodal link

Let \(V\) be a set of \(n\geq3\) labels, and identify the vertices of the cube \([0,1]^V\) with subsets of \(V\). A monotone geodesic from \(\varnothing\) to \(V\) adds every label exactly once. Thus it is specified by a permutation
\[
\pi=(v_1,\ldots,v_n),\qquad S_i=\{v_1,\ldots,v_i\}\quad(0\leq i\leq n).
\]
The convex hull
\[
\Delta_\pi=\operatorname{conv}\{\mathbf1_{S_0},\ldots,\mathbf1_{S_n}\}
\]
is an \(n\)-simplex.

These simplices triangulate the cube. Indeed, the region belonging to \(\Delta_\pi\) is
\[
1\geq x_{v_1}\geq \cdots\geq x_{v_n}\geq0.
\]
Every point of the cube has such a coordinate ordering. Its barycentric coefficients are
\[
1-x_{v_1},\quad x_{v_1}-x_{v_2},\quad\ldots,\quad
x_{v_{n-1}}-x_{v_n},\quad x_{v_n}.
\]
They are nonnegative, sum to one, and express the point in the displayed prefix vertices. Ties in coordinate order give the common faces of the corresponding simplices.

The cube antipode \(A(x)=\mathbf1-x\) sends \(\Delta_\pi\) to \(\Delta_{\pi^{\rm rev}}\). Every maximal simplex contains the diagonal edge \([\mathbf0,\mathbf1]\). Its simplicial link consists of chains of nonempty proper subsets of \(V\), hence is the barycentric subdivision of the boundary of the \((n-1)\)-simplex. In particular it is an \((n-2)\)-sphere. Complementation reverses subset chains and gives the usual antipodal action on this type-\(A\) Coxeter sphere; it is realized by negation on the centered subset vectors
\[
\mathbf1_S-\frac{|S|}{n}\mathbf1.
\]

This identifies the permutation space in the boundary-tournament problem directly with the cube's monotone geodesics. It also locates the relevant sphere: the common diagonal is removed when taking the link. An odd map on the entire cube has an automatic zero at the center, which by itself supplies no distinguished permutation.

### The color is attached to three successive directions

Fix a boundary \(3\)-tournament \(H\), and write
\[
h(u,v,w)=
\begin{cases}
1,&(u,v,w)\text{ is tight},\\
0,&(u,v,w)\text{ is non-tight}.
\end{cases}
\]
Thus
\[
h(w,v,u)=1-h(u,v,w)
\]
for distinct \(u,v,w\).

On the monotone cube geodesic specified by \(\pi\), the required word is
\[
h(v_1,v_2,v_3),\ldots,h(v_{n-2},v_{n-1},v_n).
\]
A color depends on three successive directions. In the staircase triangulation it belongs to the tetrahedron with vertices
\[
S,\quad S\cup\{u\},\quad S\cup\{u,v\},\quad S\cup\{u,v,w\}.
\]
Its color is independent of the base subset \(S\). Complementation sends this tetrahedron, written again in increasing-subset order, to one with successive directions \(w,v,u\), so it complements the color.

Consequently this is an antipodal coloring of specified three-dimensional faces of the triangulation. It is not automatically an ordinary coloring of the cube edges. The following graph retains the adjacent directions and makes the colors genuine edge colors.

### An antipodal graph with the required geodesics

Define a fixed graph \(\Gamma_n\) with two distinguished vertices \(s,t\). Its other vertices are
\[
(\sigma,S,u,v),
\]
where \(\sigma\in\{0,1\}\), \(u\ne v\), and \(S\subseteq V\setminus\{u,v\}\). There are two copies indexed by \(\sigma\). Give the vertices ranks
\[
r(s)=0,\qquad r(\sigma,S,u,v)=|S|+1,\qquad r(t)=n.
\]

Its edges are as follows.

1. Join \(s\) to every \((\sigma,\varnothing,u,v)\).
2. For \(w\notin S\cup\{u,v\}\), join
\[
(\sigma,S,u,v)\quad\text{to}\quad(\sigma,S\cup\{u\},v,w).
\]
3. Join every \((\sigma,V\setminus\{u,v\},u,v)\) to \(t\).

Every edge joins consecutive ranks. The underlying graph depends only on \(n\); \(H\) enters only through its coloring. Color the first kind of edge \(\sigma\), the third kind \(1-\sigma\), and the internal edge in item 2 by \(h(u,v,w)\).

**Proposition 1.** The map
\[
A(s)=t,\quad A(t)=s,\quad
A(\sigma,S,u,v)=
(\sigma,V\setminus(S\cup\{u,v\}),v,u)
\]
is a fixed-point-free graph involution that complements every edge color.

**Proof.** Applying the formula twice returns the original state. An internal vertex is never fixed because its ordered pair is reversed. Source edges are paired with terminal edges in the same \(\sigma\)-copy, and their colors are complementary.

For an internal edge with successive directions \(u,v,w\), put
\[
T=V\setminus(S\cup\{u,v,w\}).
\]
The antipodal edge, written in increasing-rank direction, is
\[
(\sigma,T,w,v)\longrightarrow
(\sigma,T\cup\{w\},v,u).
\]
Its color is \(h(w,v,u)=1-h(u,v,w)\). Thus \(A\) preserves adjacency and complements colors. \(\square\)

There is an antipodal graph map to the ordinary cube:
\[
p(s)=\varnothing,\quad p(t)=V,\quad
p(\sigma,S,u,v)=S\cup\{u\}.
\]
Each edge maps to an edge of the cube, and \(p(Ax)=V\setminus p(x)\). In a state over a cube vertex \(U\), the ordered pair records the label \(u\) just added and the label \(v\) to be added next.

**Proposition 2.** The distance from \(s\) to \(t\) is \(n\). Its geodesics are in bijection with pairs \((\sigma,\pi)\), where \(\pi\) is a permutation of \(V\). Their color words are
\[
\sigma,\ h(v_1,v_2,v_3),\ldots,
h(v_{n-2},v_{n-1},v_n),\ 1-\sigma.
\]

**Proof.** Any path from rank zero to rank \(n\) has length at least \(n\), because an edge changes rank by one. Each permutation gives a path of length \(n\):
\[
s,\quad
(\sigma,S_i,v_{i+1},v_{i+2})\ (0\leq i\leq n-2),\quad t.
\]
Thus the distance is \(n\).

Every geodesic must increase rank at every step. Its first state fixes \(v_1,v_2\). Each successive internal edge selects a new label outside the current prefix and ordered pair, so the remaining labels are appended without repetition. Reaching rank \(n-1\) uses all labels. The copy index remains fixed until the terminal vertex. This proves the bijection and the displayed color word. \(\square\)

The projection \(p\) maps each such geodesic to the corresponding monotone cube geodesic. Each cube geodesic has exactly two lifts, one for each \(\sigma\).

**Theorem 3.** The following statements are equivalent.

1. \(H\) has a spanning vertex order whose consecutive-triple colors change at most once.
2. The antipodally edge-colored graph \(\Gamma_n\) has an \(s\)-to-\(t\) geodesic with at most one color change.

**Proof.** A color word with at most one change has the form \(\sigma^a(1-\sigma)^b\) for some \(\sigma\) and nonnegative \(a,b\). If it is constant, either suitable boundary placement is allowed. Prepending \(\sigma\) and appending \(1-\sigma\) gives a word with exactly one change. Proposition 2 therefore proves \(1\Rightarrow2\). Conversely, deleting the first and last entries from a word with at most one change cannot increase its number of changes. Proposition 2 gives \(2\Rightarrow1\). \(\square\)

For completeness, statement 1 implies a two-cover. If the first color run has \(a\) triple positions, cut the vertex order after position \(a+1\). Each resulting block has a monochromatic internal triple word. Reverse a block whose internal word is blue; its boundary-flipped triples are all tight. Empty internal words impose no condition. If the entire word is monochromatic, the whole order in the appropriate orientation is already a tight Hamilton path.

The graph \(\Gamma_n\) is not the ordinary cube. Its additional states distinguish the different incoming and outgoing directions at a subset. A cube-edge theorem therefore needs an argument accommodating these states before it applies here. Theorem 3 is an exact reformulation, not an assertion that a general antipodal-graph theorem is available.

### What geodesicity contributes

Every walk from \(s\) to \(t\) projects to a cube walk from \(\varnothing\) to \(V\). Each coordinate is consequently used an odd number of times. If \(m_v\) is the number of uses of coordinate \(v\), then
\[
\operatorname{length}(W)
=\sum_{v\in V}m_v
=n+2\sum_{v\in V}\frac{m_v-1}{2}.
\]
The geodesics are precisely the walks for which every \(m_v=1\).

Thus the requirement that every original vertex occur once is exactly the zero-detour condition in this graph over the cube. An antipodal or fixed-point argument producing a one-change walk of unrestricted length would leave a separate mathematical task: eliminating coordinate repetitions while preserving the color condition.

The distinguished endpoints also matter. An antipodal-path theorem that permits its endpoint pair to vary does not automatically give a geodesic between the particular poles \(s,t\). A successful application must establish the required conclusion for these poles or prove that its output can be converted into one.

### Opposite terminal edges give a direct path-support formulation

There is a complementary formulation that retains the original tight paths.

For an ordered pair \(u,v\), let \(\mathcal F_{uv}\) be the family of sets \(X\subseteq V\setminus\{u,v\}\) for which some ordering of \(X\), followed by \(u,v\), is a tight path. The empty set belongs to every \(\mathcal F_{uv}\).

**Proposition 4.** A spanning order with color word \(1^a0^b\), \(a+b=n-2\), exists if and only if, for some \(u\ne v\), there are
\[
X\in\mathcal F_{uv},\qquad Y\in\mathcal F_{vu}
\]
such that \(X,Y\) partition \(V\setminus\{u,v\}\).

**Proof.** Suppose the order is \((v_1,\ldots,v_n)\), and put
\[
u=v_{a+1},\qquad v=v_{a+2}.
\]
The prefix \((v_1,\ldots,v_{a+2})\) is tight. The reversed suffix \((v_n,\ldots,v_{a+1})\) is tight, since its forward triples are exactly the blue block. These two tight paths share precisely the ordinary edge \(\{u,v\}\), traversed in opposite terminal directions. Their other vertices partition the remainder.

Conversely, take witnessing tight paths
\[
(x_1,\ldots,x_a,u,v),\qquad
(y_1,\ldots,y_b,v,u).
\]
The spanning order
\[
(x_1,\ldots,x_a,u,v,y_b,\ldots,y_1)
\]
has \(a\) tight triples followed by \(b\) non-tight triples. The latter are exactly the boundary flips of the second path's tight triples. \(\square\)

A word \(0^a1^b\) has the corresponding description using two tight paths sharing opposite initial directions of one ordinary edge. Both types must be retained when the target permits either direction of color change. Reversing the whole vertex order reverses and complements the word; it does not in general exchange the two types.

In particular, a one-change spanning order forces a tight path on at least
\[
\left\lceil\frac{n+2}{2}\right\rceil
=\left\lceil\frac n2\right\rceil+1
\]
vertices: the two overlapping tight paths have a total of \(n+2\) vertices counted with multiplicity. This records the strength of the sufficient target beyond an arbitrary two-cover.

### Positive enumeration and the remaining disjointness question

In the finite algebra
\[
\mathcal A=\mathbb Q[x_v:v\in V]/(x_v^2:v\in V),
\]
define
\[
F_{uv}=\sum_{P\text{ tight, ending }u,v}
x_{V(P)\setminus\{u,v\}}.
\]
Path orders are counted separately. Fix any total order of the vertex labels solely to sum once over each ordinary edge, and put
\[
Z_{\rm end}(H)=\sum_{u<v}x_ux_v F_{uv}F_{vu}.
\]
The square-zero variables make intersecting tail supports vanish. Therefore the coefficient of \(x_V\) counts unordered pairs of tight paths with complementary tail supports and opposite terminal directions on their shared edge. Proposition 4 shows that
\[
[x_V]Z_{\rm end}(H)>0
\]
is equivalent to existence of a spanning order with word \(1^a0^b\). Defining \(Z_{\rm start}\) with initial-edge path polynomials gives the other type, so the complete one-change target is
\[
[x_V]\bigl(Z_{\rm end}(H)+Z_{\rm start}(H)\bigr)>0.
\]
Every coefficient here is nonnegative; no cancellation or formal walk count is being used to assert positivity.

For fixed \(u,v\) and sizes \(a+b=n-2\), failure of the first target means that every \(a\)-element member of \(\mathcal F_{uv}\) intersects every \(b\)-element member of \(\mathcal F_{vu}\). This includes the possibility that a family is empty. The analogous statement holds for initial-edge families when the second target fails.

The two descriptions locate the same unresolved issue. In \(\Gamma_n\), it is existence of a one-change geodesic between the distinguished poles. In the original path families, it is existence of complementary disjoint tails at opposite directions of some edge. Antipodal connectivity alone supplies neither condition. This route seeks a topological or combinatorial argument that preserves the full prefix sets or, equivalently, the complementary supports, rather than only the positions of extreme color changes.

### Two paths with a common terminal vertex

In this subsection a pair of paths is unordered. Its members are individually ordered tight paths.

**Lemma 5.** Let \(W\) be a vertex set with \(|W|\ge2\). The induced tournament on \(W\) has a spanning order with word \(1^a0^b\) if and only if there are two tight paths whose union is \(W\), whose intersection is one vertex \(v\), and which both end at \(v\). Either path may consist solely of \(v\).

**Proof.** Write the two paths as
\[
P=(p_1,\ldots,p_\ell,v),\qquad
Q=(q_1,\ldots,q_m,v).
\]
The order
\[
(p_1,\ldots,p_\ell,v,q_m,\ldots,q_1)
\]
has tight triples on the \(P\)-side and non-tight triples on the reversed \(Q\)-side. If both tails are nonempty, its only remaining triple is \((p_\ell,v,q_m)\). Either status for this triple gives a word of the form \(1^a0^b\). If a tail is empty, the word is monochromatic.

Conversely, in an order \((w_1,\ldots,w_N)\) with word \(1^a0^b\), take
\[
P=(w_1,\ldots,w_{a+1}),\qquad
Q=(w_N,\ldots,w_{a+1}).
\]
The internal triples of the first path are tight, and those of the second are boundary flips of non-tight triples. Their only common vertex is their terminal vertex \(w_{a+1}\). \(\square\)

The corresponding statement for \(0^a1^b\) uses a common initial vertex.

The elementary movement of the common terminal vertex has particularly rigid behavior.

**Lemma 6.** On a fixed support \(W\) of size at least two, pairs from Lemma 5 have a fixed-point-free involution. Its two paired objects correspond to a single pair of tight paths sharing an oppositely directed terminal edge and otherwise disjoint.

**Proof.** Suppose both paths have a predecessor of the common terminal vertex \(v\), and write
\[
P=(A,u,v),\qquad Q=(B,w,v).
\]
Exactly one of \((u,v,w)\) and \((w,v,u)\) is tight.

If \((u,v,w)\) is tight, replace the pair by
\[
P'=(A,u,v,w),\qquad Q'=(B,w).
\]
These paths have common terminal vertex \(w\) and the same union. The shared-edge pair is
\[
(A,u,v,w),\qquad(B,w,v).
\]
If \(Q'\) has a predecessor \(z\) of \(w\), tightness of the original \(Q\) gives \((z,w,v)\) tight. Hence the same rule at \(w\) moves the terminal vertex back to \(v\). If \(Q'\) is the singleton \(w\), the singleton rule below has the same effect. The other orientation is symmetric.

If one path is the singleton \(v\), write the other as \((A,u,v)\). Replace the pair by
\[
(A,u),\qquad(v,u).
\]
Both are tight. When \(A\) is nonempty, its final vertex \(z\) satisfies \((z,u,v)\) tight, so the preceding rule moves back to \(v\). If \(A\) is empty, the singleton rule moves back directly.

The common terminal vertex changes, so the involution has no fixed point. Conversely, from a pair ending along \(uv\) and \(vu\), truncating one path's final vertex gives a common-terminal pair at \(u\), and truncating the other gives its mate at \(v\). \(\square\)

Thus this particular movement produces matched pairs of states, not a longer sequence of new path orders. Further augmentation needs an additional operation.

### Adjoining one vertex makes the directed one-change target exact

The auxiliary-vertex construction in the direct-enumeration Brainstorm gives a prescribed-switch formulation of the two-cover conjecture. The following stronger statement removes the switch-location condition and identifies every successful order.

Let \(H\) have nonempty vertex set \(V\). Adjoin a vertex \(r\), and define a boundary tournament \(H^+\) by retaining \(H\) and setting
\[
h(u,v,r)=1,\qquad h(r,v,u)=0
\]
for all distinct \(u,v\in V\). Choose the remaining values \(h(u,r,v)\) arbitrarily subject to
\[
h(u,r,v)+h(v,r,u)=1.
\]
Equivalently, the local tournament at \(r\) is arbitrary.

**Theorem 7 (exact one-change extension).** There is a two-to-one map from spanning orders of \(H^+\) with color word \(1^a0^b\) to two-covers of \(H\). Each path in a cover is ordered, and the collection of paths is unordered. The two orders over each cover are reverses of one another.

In particular, the following are equivalent:
\[
\operatorname{pc}(H)\le2;
\]
\[
H^+\text{ has a spanning order with word }1^a0^b.
\]
The entire set of successful orders, not only its cardinality, is independent of the choice of local tournament at \(r\).

**Proof.** Write any spanning order uniquely as
\[
\pi=(L,r,R),
\]
where either displayed side may be empty.

Suppose its word is \(1^a0^b\). If \(L\) has at least two vertices, its last two vertices followed by \(r\) form a tight triple. Every earlier triple must therefore be tight. Thus \(L\) is a tight path. The conclusion is vacuous when \(|L|\le1\).

If \(R\) has at least two vertices, \(r\) followed by its first two vertices is non-tight. Every later triple is therefore non-tight. Consequently \(R^{\rm rev}\) is a tight path, again with the short cases vacuous. Deleting \(r\) and discarding an empty side gives the two-cover
\[
L\mid R^{\rm rev}.
\]

Conversely, let \(P\mid Q\) be a two-cover. If both paths are nonempty, then
\[
(P,r,Q^{\rm rev})
\]
has tight triples through the left side, including the junction ending at \(r\), and non-tight triples through the right side, including the junction beginning at \(r\). The sole possible remaining triple has \(r\) in the middle. Either of its two statuses preserves the form \(1^a0^b\). The order \((Q,r,P^{\rm rev})\) is its reverse.

For a one-path cover \(P\), the two orders are \((P,r)\) and \((r,P^{\rm rev})\). They are monochromatic in opposite colors.

The construction recovers both side orders from \(\pi\), so no other cover maps to it. Conversely, a given cover permits exactly the two displayed side placements. All conclusions depend only on the forced endpoint triples at \(r\); the central triple is unrestricted. \(\square\)

The distinction between \(1^a0^b\) and \(0^a1^b\) is essential in this theorem. Reversing an order preserves the first type, since reversal also complements all triple colors.

For nonempty \(P,Q\), put \(p=|P|\) and let
\[
\epsilon=h(\operatorname{last}(P),r,\operatorname{last}(Q)).
\]
In the order \((P,r,Q^{\rm rev})\), the number of initial tight triples is
\[
a=p-1+\epsilon.
\]
Hence the two vertices at the change specified in Proposition 4 include \(r\). The switch location is forced by the extension itself.

### Normalization of the common terminal vertex

**Corollary 8.** In \(H^+\), every pair of tight paths sharing an opposite terminal edge and otherwise disjoint, with union \(V\cup\{r\}\), shares an edge containing \(r\). Under the involution of Lemma 6, exactly one associated common-terminal pair ends at \(r\). Removing \(r\) from those two paths gives a two-cover of \(H\).

**Proof.** A tight path containing \(r\) has at most one vertex after \(r\): a triple beginning at \(r\) would be non-tight. Thus \(r\) is one of the last two vertices of every tight path containing it.

In an opposite-terminal-edge pair covering \(r\), at least one path contains \(r\), so its terminal edge contains \(r\). That edge is shared by both paths. The two common-terminal pairs associated by Lemma 6 have the two distinct endpoints of this edge as their common terminal vertices; precisely one ends at \(r\). Deleting that common last vertex leaves disjoint tight paths spanning \(V\), with an empty path discarded. \(\square\)

Equivalently, if a common-terminal pair in \(H^+\) ends at \(v\ne r\), the involution moves its common terminal vertex to \(r\) in one step. Endpoint normalization requires no repeated search in this extension.

### An exact positive factorization

Let
\[
\mathcal A=\mathbb Q[x_v:v\in V]/(x_v^2:v\in V),
\qquad
F_H=\sum_{P\text{ nonempty tight in }H}x_{V(P)},
\]
where different path orders are counted separately.

For each \(S\subseteq V\), let \(m_r(S)\) be the number of orders of \(S\cup\{r\}\) whose triple word is \(1^a0^b\). In particular \(m_r(\varnothing)=1\). Then Theorem 7, applied to every induced subtournament, gives
\[
\boxed{\quad
\sum_{S\subseteq V}m_r(S)x_S=(1+F_H)^2.
\quad}
\]

Indeed, the constant term records the order \((r)\). The term \(2F_H\) records orders arising from a single path on either side of \(r\), and \(F_H^2\) records two ordered, disjoint nonempty paths placed on the two sides. Intersecting supports vanish in \(\mathcal A\). This is a positive enumeration identity, with no cancellation.

For nonempty \(V\),
\[
m_r(V)=2\,[x_V]\left(F_H+\frac12F_H^2\right).
\]
Thus proving positivity on the left is exactly the original two-cover problem. The factorization identifies the count; it does not by itself prove that its spanning coefficient is nonzero.

### The remaining geodesic statement

The case \(|V|=1\) is immediate, so assume \(|V|\ge2\). Apply the graph construction of Proposition 2 to \(H^+\), using only the copy \(\sigma=1\). Its pole geodesics have words
\[
1,\ h(w_1,w_2,w_3),\ldots,
h(w_{n-1},w_n,w_{n+1}),\ 0.
\]
Such a word changes color once exactly when the internal word has the form \(1^a0^b\). Therefore the grand two-cover conjecture is equivalent to the following restricted geodesic assertion:

> For every boundary tournament extended by a vertex \(r\) with \(h(u,v,r)=1\), the \(\sigma=1\) copy of its graph has a one-change geodesic between the poles.

The local tournament at \(r\) may be chosen freely, for example transitive. The output need not specify a switch location or common terminal vertex: Theorem 7 and Corollary 8 supply both. The unresolved requirement is existence of that geodesic. This formulation retains every original vertex once and has exactly the strength of the two-cover conjecture, whereas the one-change target on the original vertex set remains a potentially stronger sufficient condition.


## Metadata

- ID: antipodal_geodesics_and_complementary_path_supports
- Kind: section
- Version: 3
- Math version: 2
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — (untitled)](../SUBSECTIONS/antipodal_geodesics_and_complementary_path_supports_subsection_a.md) (\`antipodal_geodesics_and_complementary_path_supports_subsection_a\`; development v2; composition vNone; stale=True)
