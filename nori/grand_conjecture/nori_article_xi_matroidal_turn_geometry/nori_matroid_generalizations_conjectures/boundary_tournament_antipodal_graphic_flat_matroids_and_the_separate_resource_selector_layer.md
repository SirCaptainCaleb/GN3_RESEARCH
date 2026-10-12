# Boundary-tournament antipodal graphic-flat matroids and the separate resource-selector layer

# Boundary tournaments, antipodal graphic-flat matroids, and resource-basis packing

We verify that *every* ordinary reversal-odd boundary 3-tournament produces the antipodal graphic-flat and edge-orbit partition-matroid structure of Article XI. We also establish a distinction between the **basis-exchange quotient** and its covering graph, and reduce the spanning one-turn conjecture to the existence of a two-arm basis of the **separate** original-vertex graphic matroid.

## 1. Cover and matroid construction

For \(n\ge4\), define \(\mathscr S_n\) to have vertices \((a,b)\), \(a\ne b\), and undirected edges
\[
\boxed{\{(a,b),(b,c)\}\quad(a,b,c\text{ distinct}).}
\tag{1}
\]
Each covering edge is indexed by its ordered triple \((a,b,c)\). Reversal \(\tau(a,b)=(b,a)\) exchanges the edges of \((a,b,c)\) and \((c,b,a)\). Thus
\[
\boxed{\mathscr S_n/\tau\cong L(K_n)=\Gamma(U_{2,n}),}
\tag{2}
\]
with a connected regular two-cover \(\mathscr S_n\to L(K_n)\). The cover is \(2(n-2)\)-regular, has \(N=n(n-1)\) vertices, and has \(N(n-2)\) edges.

Write \(\mathsf G_n=M(\mathscr S_n)\) for its graphic cycle matroid. Let \(\mathsf P_n\) be the partition matroid on covering edges with one two-element part \(\{e,\tau e\}\) per triple reversal-orbit, each of capacity one. Its rank is \(N(n-2)/2\).

**Theorem 1 (unrestricted boundary representation).** Reversal-odd boundary 3-tournaments are in bijection with the bases \(B\) of \(\mathsf P_n\): their zero-colored covering edges. For any such \(B\), let \(\Pi_B\) be the partition into connected components of \((V(\mathscr S_n),B)\) and let \(F_B=\operatorname{cl}_{\mathsf G_n}(B)\). Then
\[
\boxed{
F_B\cup\tau F_B=E(\mathscr S_n),\qquad
r_{\mathsf G_n}(B)=N-|\Pi_B|,
}
\tag{3}
\]
and
\[
\boxed{
|B|-r_{\mathsf G_n}(B)
=\frac{n(n-1)(n-4)}2+|\Pi_B|.
}
\tag{4}
\]
Conversely, a partition \(\Pi\) is the full zero-colored component partition of some reversal-odd boundary coloring if and only if its graphic flat \(F_\Pi\) covers \(E(\mathscr S_n)\) together with \(\tau F_\Pi\), and \(F_\Pi\) contains an orbit-rainbow spanning forest. By the graphic–partition matroid intersection theorem, the latter is equivalent to the refinement-partition cut inequalities already proved in the global flat-cover Subsection.

*Proof.* Each reversal-odd coloring selects one edge from every reversal-orbit as zero-colored; that is a basis of the orbit partition matroid, and every such basis gives a coloring. Every zero edge lies in its connected component, and the reversal of any one-colored edge is a zero edge, which proves the flat covering. The graphic rank is \(N\) minus the number of connected components, giving (3) and (4). The converse is the all-cover flat and rainbow-forest characterization from the preceding Subsection, applied to \(\mathscr S_n\). \(\square\)

It follows that **all** the shared antipodal cut, Eulerian contact-graph, global even-edge and graphic-flat results of Article XI apply to every boundary coloring. The pointed binary matroid from the induced cover of the turn graph \(L(L(K_n))\) is a second, compatible construction. No special coloring subclass is needed.

## 2. The covering graph itself is not generally a basis graph

**Theorem 2 (basis-graph obstruction in unbounded orders).** The graph \(\mathscr S_n\) is not the basis-exchange graph of any matroid when \(n=4\) or \(n\ge8\).

*Proof.* Choose distinct original symbols \(a,b,c\) and vertices \(u=(a,b)\), \(v=(a,c)\) in \(\mathscr S_n\). They are not adjacent, and their common neighbors are
\[
\boxed{N(u)\cap N(v)=\{(x,a):x\notin\{a,b,c\}\}.}
\tag{5}
\]
Thus these two vertices are at distance two and possess \(n-3\) common neighbors. In every matroid basis graph, two vertices at distance two correspond to bases differing by two elements in each direction. All common neighbors exchange one of two elements for one of two others, giving at most four possibilities. Symmetric basis exchange supplies at least two distinct common neighbors. The number \(n-3\) violates the lower bound for \(n=4\) and the upper bound for \(n\ge8\). \(\square\)

Therefore the relevant **basis graph** is the quotient \(\Gamma(U_{2,n})=L(K_n)\); the covering graph has its own *graphic matroid*. Identifying these two layers would lead to an invalid universal basis-exchange argument.

## 3. A second graphic matroid supplies the Hamilton resource constraint

The original-vertex resource matroid is
\[
\boxed{\mathsf R_n=M(K_n),}
\tag{6}
\]
distinct from \(\mathsf G_n=M(\mathscr S_n)\). A forward tight word \(P=(v_1,\ldots,v_k)\) is a directed-overlap path \((v_1,v_2)\to(v_2,v_3)\to\cdots\) in the covering graph, with resource edges
\[
E(P)=\{\{v_i,v_{i+1}\}:1\le i<k\}.
\tag{7}
\]
Starting from one original edge, requiring each appended resource edge to increase graphic rank in \(\mathsf R_n\) forces every appended original vertex to be new. An undirected same-color path in \(\mathscr S_n\) need not be a legal forward tight path because it may switch the overlap direction and revisit original vertices. Thus covering-graph connectivity, even between reversal-related oriented pairs, does not alone produce the desired tournament path.

**Theorem 3 (opposite-terminal basis packing).** Let \(P,Q\) be vertex-simple \(\varepsilon\)-monochromatic forward tight paths for the same color, ending in ordered pairs \((u,v)\) and \((v,u)\) respectively. A two-vertex arm is allowed. Then
\[
\boxed{
E(P)\cup E(Q)\in\mathcal I(\mathsf R_n)
\iff
V(P)\cap V(Q)=\{u,v\}.
}
\tag{8}
\]
Consequently,
\[
\boxed{
\text{A spanning one-turn boundary tight path exists}
\iff
\exists\,u,v,\varepsilon,P,Q:
E(P)\cup E(Q)\in\mathcal B(\mathsf R_n).
}
\tag{9}
\]
In this formulation, graphic independence automatically enforces disjoint interiors and the Hamilton path degree bound.

*Proof.* Delete the shared last edge \(\{u,v\}\). The remaining edges of \(P\) form one path attached to \(u\), and those of \(Q\) another path attached to \(v\). If the paths have no common additional vertex, their union with \(\{u,v\}\) is a simple path, hence graphic-independent. If they meet at some other original vertex, choose the first common meeting point from the two rooted ends. The two initial subpaths from \(u\) and \(v\), together with \(\{u,v\}\), form a graph cycle; hence their union is graphic-dependent. This proves (8). If the independent union is a graphic basis, its simple path contains all \(n\) original vertices. Reverse \(Q\), which reverses all its triple colors under boundary oddness, and splice it to \(P\) at the terminal pair to obtain a spanning path with at most one color change. Conversely, split a spanning one-turn path at its switch, reverse its second arm and use the two same-colored arms. When the path is monochromatic, use a vacuous two-vertex arm and the full reversed path. \(\square\)

The criterion (9) is the natural **integral matroid basis-packing target**. The difficult part is finding the two forward, color-compatible arms; their families do not satisfy ordinary greedoid augmentation in general, as shown by earlier Article XI research-note counterexamples. Generic matroid intersection on the covering graph \(\mathsf G_n\) is therefore insufficient without the directed resource-language constraint.

## 4. Why a cube-specific port-loop axiom must be excluded

The cube's pointed contact graph always has a port-parallel loop by the known existence of a monochromatic antipodal path. The corresponding loop property fails for boundary tournaments: on four original vertices, the reversal-odd coloring with representative mask \(\mathrm{0x555}\), indexed by increasing middle symbol and then lexicographic outer pair \(a<c\), has a red covering graph consisting of four disjoint oriented three-cycles, one on each three-element original-vertex subset. No component contains both \((a,b)\) and \((b,a)\). The contact graph is \(K_4\) with four parallel copies of every edge. It is Eulerian, nonbipartite, even-sized, and loop-free. Hence its shortest unrestricted port intersection is four, rather than two. This example and an exhaustive enumeration of the 4096 order-four colorings are retained as a research note.

The **shared** matroid class is therefore the antipodal graph-cover, graphic-flat, orbit-partition, and pointed-binary construction. The **distinct admissible selectors** are (i) a displacement-minimal lifted fundamental circuit for the cube and (ii) an opposite-terminal union that is a basis of \(\mathsf R_n=M(K_n)\) for boundary tournaments. A unification theorem must preserve this second level of independent resources rather than replacing it by port parallelism.
