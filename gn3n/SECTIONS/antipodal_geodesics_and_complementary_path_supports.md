# Antipodal geodesics and complementary path supports

**Summary:** The cube analogy becomes an exact geodesic reformulation that retains every vertex exactly once. A direct equivalent target asks for two tight paths overlapping in an oppositely directed end edge and otherwise partitioning the vertices; neither existence assertion is proved here.

## Statement

An explicit graph over the Boolean cube carries a fixed-point-free color-complementing involution. Its distinguished-pole geodesics encode spanning vertex orders, and one-change pole geodesics are exactly one-change spanning orders. Equivalently, such orders are pairs of tight paths with complementary tail supports and opposite terminal or initial directions on their common edge. Existence of these geodesics or complementary supports remains open.

## Body

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


## Metadata

- ID: antipodal_geodesics_and_complementary_path_supports
- Kind: section
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Subsection 1 — HOT, version 1: (untitled)
