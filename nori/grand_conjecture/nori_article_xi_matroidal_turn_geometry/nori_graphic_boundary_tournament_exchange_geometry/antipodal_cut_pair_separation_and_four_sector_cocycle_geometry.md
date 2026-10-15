# Antipodal cut-pair separation and four-sector cocycle geometry

# Antipodal cut-pair separation and four-sector cocycle geometry

The component-contact minor records the intersections of monochromatic components with their deck images. Here we recover additional information lost under zero-turn contraction: the *boundaries of a monochromatic component and its deck image are disjoint graphic-matroid cocycles*. This yields a canonical four-sector quotient with prescribed boundary colors, and a matroid-intersection characterization of which vertex sets can occur as monochromatic components under a deck-odd coloring.

Let \(G\) be a finite connected graph with a fixed-point-free involution \(\tau\) that acts freely on edges, and let \(c:E(G)\to\mathbb F_2\) obey \(c(\tau e)=1+c(e)\). The antipodal cube \(Q_n\), \(n\ge3\), is the principal example. The graph cuts \(\delta_G(S)\) form the cocycle space of the graphic matroid \(M(G)\).

## 1. Disjoint antipodal cut cocycles

**Theorem 1 (component-cut disjointness).** Let \(R\subseteq V(G)\) be the vertex set of one connected color-zero component, excluding isolated zero-degree vertices. Then
\[
\boxed{\delta_G(R)\subseteq c^{-1}(1),\qquad
\delta_G(\tau R)=\tau\delta_G(R)\subseteq c^{-1}(0),}
\tag{1}
\]
and therefore
\[
\boxed{\delta_G(R)\cap\delta_G(\tau R)=\varnothing.}
\tag{2}
\]

*Proof.* An edge leaving a full color-zero connected component cannot itself have color zero, since its exterior endpoint would belong to the same component. Thus \(\delta_G(R)\) is blue. Applying \(\tau\) converts those edges to red and gives the boundary of \(\tau R\), proving (1) and (2). \(\square\)

**Corollary 2 (antipodal cocycle pair).** The two graphic-matroid cocycles \(\delta_G(R)\) and \(\delta_G(\tau R)\) have disjoint supports, are exchanged by \(\tau\), and have the same cardinality. Their union is the cocycle
\[
\boxed{
\delta_G(R)\sqcup\delta_G(\tau R)
=\delta_G(R\mathbin{\triangle}\tau R).
}
\tag{3}
\]
If \(R\) contains an antipodal pair, then \(R\cap\tau R\ne\varnothing\), and this pair of separated cuts coexists with a port-parallel loop in the pointed component-contact minor.

*Proof.* Binary cut addition obeys \(\delta(A)\triangle\delta(B)=\delta(A\triangle B)\). The supports are disjoint by (2), and \(\tau\) exchanges them. \(\square\)

## 2. Canonical four-sector geometry

Define a partition of \(V(G)\):
\[
\boxed{
I=R\cap\tau R,\quad
A=R\setminus\tau R,\quad
B=\tau R\setminus R=\tau A,\quad
O=V(G)\setminus(R\cup\tau R).
}
\tag{4}
\]
The sectors \(I,O\) are \(\tau\)-invariant; \(\tau\) exchanges \(A\) and \(B\).

**Theorem 3 (four-sector forbidden diagonals and forced colors).** No edge joins \(I\) to \(O\), and no edge joins \(A\) to \(B\):
\[
\boxed{E_G(I,O)=E_G(A,B)=\varnothing.}
\tag{5}
\]
Every edge between distinct sectors belongs to one of the four other cross-sector classes. Its color is forced:
\[
\boxed{
c(E_G(I,A))=0,\quad
c(E_G(B,O))=0,\quad
c(E_G(I,B))=1,\quad
c(E_G(A,O))=1.
}
\tag{6}
\]
Edges contained within an individual sector are not assigned a color by (5)–(6).

*Proof.* An edge between \(I\) and \(O\) crosses both boundaries \(\delta(R)\) and \(\delta(\tau R)\); so does an edge between \(A\) and \(B\). Theorem 1 forbids such edges. An \(I\)-to-\(A\) edge crosses \(\delta(\tau R)\), hence is red. An \(I\)-to-\(B\) edge crosses \(\delta(R)\), hence is blue. The other two cases are symmetric and give (6). \(\square\)

Equivalently, the sector label defines a \(\tau\)-equivariant graph map to a four-cycle with cyclic sectors \(I,A,O,B\), allowing stationary steps, and with the two opposite diagonals forbidden. Red and blue boundary edges alternate around this four-cycle. The quotient is a global compatibility constraint between the color-zero component \(R\), the color-one component \(\tau R\), and their interface \(I\), not merely a statement about one component in isolation.

## 3. Which sets can be monochromatic components?

Let \(G\) be any finite connected graph with a fixed-point-free involution acting freely on edges, as at the start of this Subsection. A deck edge orbit is the two-element pair \(\{e,\tau e\}\). For a vertex set \(R\), let \(G_R=G[R]\) be its induced graph. The edge orbits partition \(E(G_R)\) into classes of size one or two. Let \(P_\tau(R)\) be the partition matroid on \(E(G_R)\) permitting at most one selected edge from each antipodal orbit. Let \(M(G_R)\) be the graphic cycle matroid of the induced graph.

**Theorem 4 (graphic–partition matroid component characterization).** For a nonempty \(R\subseteq V(G)\), there exists a deck-odd edge coloring of the full covering graph for which \(R\) is precisely one connected red component if and only if
\[
\boxed{
\delta_G(R)\cap\tau\delta_G(R)=\varnothing
}
\tag{7}
\]
and
\[
\boxed{
\max\{|T|:T\in\mathcal I(M(G_R))\cap\mathcal I(P_\tau(R))\}
=|R|-1.
}
\tag{8}
\]
The second condition says that \(G_R\) has a spanning tree containing no antipodal pair of edges.

*Proof.* For necessity, let \(R\) be a red component of a deck-odd coloring. Condition (7) is Theorem 1. Choose a red spanning tree of \(R\). It is independent in \(M(G_R)\), has \(|R|-1\) edges, and cannot contain both members of an antipodal edge pair because they have complementary colors. Thus (8) holds.

For sufficiency, choose a spanning tree \(T\subseteq E(G_R)\) meeting each edge orbit at most once. For each orbit that meets \(\delta(R)\), color its unique boundary member blue and its antipode red; this prescription is consistent because (7) forbids both orbit members from lying in \(\delta(R)\). On every still-uncolored edge orbit meeting \(T\), declare its member in \(T\) red and its antipode blue; there is no conflict because the orbit contains at most one tree edge, and any tree edge whose antipode was a boundary edge has already been colored red. Color the remaining orbits arbitrarily with complementary bits. All boundary edges of \(R\) are blue, so no red path exits \(R\); every edge of \(T\) is red, so \(R\) is red connected. Hence \(R\) is one full red component. \(\square\)

**Corollary 5 (intrinsic partition-cut test).** Condition (8) holds if and only if for every partition
\(\mathcal P=\{R_1,\ldots,R_k\}\) of the vertex set \(R\) into \(k\ge2\) nonempty parts,
\[
\boxed{
\#\left\{\text{antipodal edge orbits containing an edge of }
G_R\text{ crossing }\mathcal P\right\}\ge k-1.
}
\tag{9}
\]
Thus (7) together with (9) gives a criterion expressed entirely by **disjoint antipodal graphic cocycles and edge-orbit matroid rank**, without quantification over edge colorings.

*Proof.* Apply the matroid-intersection min–max theorem to \(M(G_R)\) and \(P_\tau(R)\). For any edge subset \(F\subseteq E(G_R)\), the graphic rank is \(|R|-\kappa(F)\), where \(\kappa(F)\) is the number of connected components of \((R,F)\). The partition rank on \(E(G_R)\setminus F\) is the number of antipodal edge orbits represented there. Therefore the intersection has a common independent set of size \(|R|-1\) precisely when, for all \(F\),
\[
\#\{\text{orbits represented in }E(G_R)\setminus F\}
\ge\kappa(F)-1.
\]
The crossing edges of the component partition of \(F\) lie outside \(F\), so (9) implies the inequalities. Conversely, for an arbitrary partition \(\mathcal P\), take \(F\) to contain all edges internal to its parts. The remaining edges are its crossing edges and \(\kappa(F)\ge k\), proving (9). \(\square\)

## 4. Consequences for the spanning-geodesic selector

For a cube coloring \(c\), take a red component \(R\) containing an antipodal pair. The component is subject simultaneously to (i) the graphic-rank amplification bound from the preceding Subsection, (ii) the antipodal cocycle separation (7), and (iii) the orbit-rainbow connectivity condition (8). The induced four-sector partition constrains every edge leaving \(R\) and every edge leaving its antipodal blue mate \(\tau R\).

These conditions provide an intrinsic matroidal class of admissible **monochromatic component supports**, not merely of signed turn graphs. Nevertheless, they characterize which supports are possible under *some* deck-odd coloring, not which edges inside such a support are red under a previously fixed coloring. A vertex-simple antipodal geodesic lying in \(Q_n[R]\) need not be red. Therefore the characterization alone does not establish NORI1.

The next closure problem is to combine the two-cut sector geometry with resource-simple fundamental-circuit exchange. It would suffice to prove that in every admissible fixed coloring, some self-antipodal red component contains a **red** shortest antipodal path. Disjoint graphic cocycle pairs and the partition-cut criterion are additional constraints that any purported counterexample must satisfy; in isolation they do not imply the desired distance equality.

## 5. Shared specialization to both canonical systems

**Corollary 6 (common component-support structure).** Theorems 1–4 and Corollary 5 apply to both canonical Article XI graph coverings:

(i) the \(n\)-regular antipodal cube cover \(Q_n\to Q_n/\tau\), whose covering edges are cube edges; and

(ii) the \(2(n-2)\)-regular ordered-pair cover \(S(K_n)\to L(K_n)\) used for ordinary reversal-odd boundary 3-tournaments, whose covering edges are ordered triples \((a,b,c)\), with deck reversal \((c,b,a)\).

For both systems, every monochromatic component \(R\) and its opposite-colored deck image \(\tau R\) determine disjoint antipodal cut cocycles and the same four-sector constraints. A candidate monochromatic component support is realizable by a deck-odd coloring if and only if its antipodal cut pair is disjoint and its induced graph has an edge-orbit-rainbow spanning tree, equivalently the partition-cut inequalities (9).

*Proof.* In either cover, the deck involution acts freely on vertices and edges and complements edge-state colors. The proofs above use only those conditions and the graphic–partition matroid intersection theorem. \(\square\)

In the boundary model, the vertices of \(S(K_n)\) are ordered pairs of original vertices. Thus red connectivity of an ordered-pair component does not ensure a forward vertex-simple tight path. The shared cocycle and component-realizability structures are independent of, but compatible with, the additional original-resource matroid required for the spanning one-turn conjecture.
