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

## 5. A pulled-back original-resource matroid on covering transitions

Fix the initial ordered pair \((u,v)\). For each covering edge
\[
e_{abc}=\{(a,b),(b,c)\}\in E(\mathscr S_n),
\]
label its original resource by \(\lambda(e_{abc})=\{b,c\}\in E(K_n)\). This is well-defined because an undirected covering edge has a unique ordered-triple index. Define the parallel-extension pullback matroid
\[
\boxed{\mathsf N_{uv}=\lambda^*(M(K_n)/\{u,v\})}
\tag{10}
\]
on the same covering-transition ground set as \(\mathsf G_n=M(\mathscr S_n)\). Thus \(A\subseteq E(\mathscr S_n)\) is independent in \(\mathsf N_{uv}\) if the resource labels \(\lambda(A)\) are distinct and
\[
\{\{u,v\}\}\cup\lambda(A)\in\mathcal I(M(K_n)).
\tag{11}
\]

**Theorem 4 (resource independence of coherent forward words).** A coherent forward covering-state path starting at \((u,v)\) with no repeated covering edge decodes to an injective original-vertex word if and only if its edge set is independent in \(\mathsf N_{uv}\). When these conditions hold, its edge set is also independent in the covering graphic matroid \(\mathsf G_n\).

*Proof.* The initial original edge \(\{u,v\}\) followed by the labels of the successive forward covering edges is the entire original edge sequence of the decoded word. An injective word traces a graph path with pairwise distinct original resource labels, so (11) holds. Conversely, revisiting an original vertex yields a closed nonbacktracking segment, because consecutive triples use three distinct original vertices. That segment either repeats a resource edge or contains a graph cycle, contradicting the label distinctness or original graphic independence in (11). For an injective word, its oriented-pair covering states are distinct, so the covering edges form a graph path and are independent in \(\mathsf G_n\). \(\square\)

**Proposition 5 (plain matroid intersection does not enforce coherent paths).** On five original vertices there exists a reversal-odd boundary coloring whose red covering edge set contains a common independent set of size \(n-2=3\) in \(\mathsf G_5\) and \(\mathsf N_{01}\), yet no red or blue spanning tight path exists.

*Proof.* Use the representative bit mask \(\mathrm{0x3ed25058}\), with representatives ordered by increasing middle vertex followed by increasing outer pair \(a<c\). The full \(5!=120\) word enumeration in the five-cycle sharpness Subsection establishes that all spanning words have at least one turn, so no monochromatic spanning word exists. Nevertheless, the three covering edges indexed by
\[
\boxed{(0,1,3),\ (0,1,4),\ (0,2,3)}
\tag{12}
\]
are red. They form a covering graph forest (two share only state \((0,1)\), and the third is disjoint). Their original resource labels are \(\{1,3\},\{1,4\},\{2,3\}\). Adding the initial resource \(\{0,1\}\) gives a spanning tree of \(K_5\). Hence the three covering edges are independent in both matroids, attaining resource rank \(3\), but they are not a single forward coherent state path. \(\square\)

This yields two graphic-derived matroids on the same boundary covering-edge set, plus the antipodal orbit partition matroid that parametrizes all reversal-odd colorings. Theorem 4 proves resource independence is an ordinary matroid constraint on directed forward paths. Proposition 5 shows a common independent set of full resource rank need not be a forward path: its **directed adjacency and route connectedness** must be retained as a separate admissibility condition. Thus a matroid-based spanning one-turn proof needs an exchange principle compatible with the coherent directed path language, not plain matroid intersection alone.

## 6. Near-complete resource support in every boundary coloring

There is a strong universal abundance theorem for the original-resource labels of a **fixed** color, independent of any randomization or exchange choices.

Fix one color \(\varepsilon\), and let \(B_\varepsilon\) consist of covering edges of that color. Using the resource labeling \(\lambda(e_{abc})=\{b,c\}\), put
\[
\boxed{
\Lambda_\varepsilon=\lambda(B_\varepsilon)
\subseteq E(K_n).
}
\tag{13}
\]

**Theorem 6 (missing resources form a matching).** For every ordinary reversal-odd boundary 3-tournament on \(n\ge3\) vertices, and for each \(\varepsilon\in\{0,1\}\),
\[
\boxed{
E(K_n)\setminus\Lambda_\varepsilon
\text{ is a matching}.
}
\tag{14}
\]
In particular,
\[
\boxed{
|\Lambda_\varepsilon|\ge\binom n2-\left\lfloor\frac n2\right\rfloor,
\qquad r_{M(K_n)}(\Lambda_\varepsilon)=n-1.
}
\tag{15}
\]
Thus every fixed color appears on a collection of forward covering transitions whose **original-resource labels already span the full graphic resource matroid**.

*Proof.* For each middle vertex \(b\), restrict the boundary coloring to the ordered triples \((a,b,c)\) with \(a,c\ne b\). Reversal oddness makes the color-\(\varepsilon\) triples into the arcs of a tournament \(T_b^\varepsilon\) on \(V\setminus\{b\}\), oriented \(a\to c\) when \(b(a,b,c)=\varepsilon\). The resource edge \(\{b,c\}\) occurs as \(\lambda(e_{abc})\) for some color-\(\varepsilon\) triple with middle \(b\) if and only if \(c\) has positive indegree in \(T_b^\varepsilon\).

Suppose two missing resource edges \(\{b,c\}\) and \(\{b,d\}\) share the same vertex \(b\). Their absence implies both \(c\) and \(d\) have indegree zero in \(T_b^\varepsilon\). But a tournament has at most one vertex of indegree zero, because the edge between any two proposed sources must enter one of them. This is impossible. Hence the missing-edge graph has maximum degree at most one, proving (14). The stated cardinality bound follows. The complement of a matching in \(K_n\) is connected for \(n\ge3\); its graphic rank is \(n-1\). \(\square\)

**Corollary 7 (two forced outgoing fans).** If a resource edge \(\{b,c\}\) is absent from \(\Lambda_\varepsilon\), then for every \(a\notin\{b,c\}\),
\[
\boxed{
b(c,b,a)=\varepsilon,\qquad b(b,c,a)=\varepsilon.
}
\tag{16}
\]
Equivalently, both ordered-pair states \((c,b)\) and \((b,c)\) have all \(n-2\) possible **outgoing forward transitions** of color \(\varepsilon\).

*Proof.* Absence of resource \(\{b,c\}\) means each triple \((a,b,c)\) and \((a,c,b)\) has the opposite color \(1-\varepsilon\). Reverse both triples and apply reversal oddness. \(\square\)

The matching bound is attainable: the missing resource sets for the five-vertex mask \(\mathrm{0x3ed25058}\) in Proposition 5 are the two disjoint edges \(\{1,2\}\) and \(\{3,4\}\). More generally the independent local tournament choices at each middle vertex permit any prescribed matching as the missing color-\(\varepsilon\) resource support for \(n\ge4\): make the designated partner a zero-indegree source at each matched vertex, and choose source-free local tournaments at unmatched vertices.

This theorem clarifies why ordinary graphic rank arguments on \(\mathsf R_n\) alone cannot settle the spanning conjecture. Every color already has an almost-complete **resource support graph**, and therefore abundant spanning trees. The obstruction must occur in the directed overlap constraints coupling **successive** resource edges, not in the ability to select independent resources individually. The forced outgoing fans (16) may supply useful local rerouting operations for an eventual rank-preserving opposite-terminal exchange theorem.

## 7. Missing resource edges are forced color-change gates

The outgoing-fan phenomenon in Corollary 7 has a dual incoming constraint. Let \(e=\{b,c\}\) be an original resource edge absent from the color-\(\varepsilon\) support \(\Lambda_\varepsilon\).

**Theorem 8 (forced phase gate at a missing resource).** For every \(a\notin\{b,c\}\),
\[
\boxed{
\begin{aligned}
b(a,b,c)&=1-\varepsilon,&
b(b,c,a)&=\varepsilon,\\
b(a,c,b)&=1-\varepsilon,&
b(c,b,a)&=\varepsilon.
\end{aligned}}
\tag{17}
\]
Consequently **every** coherent forward tight path that passes through either ordered-pair state \((b,c)\) or \((c,b)\) as an interior state makes a color change from \(1-\varepsilon\) to \(\varepsilon\) at that state. All incoming transitions to either state have color \(1-\varepsilon\), and all outgoing transitions have color \(\varepsilon\).

*Proof.* The first and third displayed triples have resource label \(\{b,c\}\) in the color-\(\varepsilon\) resource map. Since this label is absent, both triples have color \(1-\varepsilon\). The second and fourth triples are their reversal pairs, so reversal oddness forces color \(\varepsilon\). The incoming and outgoing transition description follows from the ordered-pair covering graph. \(\square\)

**Corollary 9 (forced-gate packing restriction).** Let \(F_\varepsilon=E(K_n)\setminus\Lambda_\varepsilon\), a matching by Theorem 6. In any spanning tight word with at most one internal color change, there is at most one consecutive original pair from \(F_\varepsilon\) occurring as an interior ordered-pair state; if such a pair occurs, the unique change is from \(1-\varepsilon\) to \(\varepsilon\) at that pair. A monochromatic spanning tight word cannot contain any missing-resource pair as an interior state. The endpoints of the word may contain such a pair without triggering an internal comparison.

Theorem 8 converts a missing resource into a **deterministic two-color switching interface**. In particular, instead of treating missing labels solely as rank defects, a proposed spanning one-turn proof may use one as its intended seam and seek two independent monochromatic arms attaching on opposite sides. The missing edges themselves form a matching, so there can be no overlapping gate constraints based at the same original vertex. This is a structural lead, not a completed spanning one-turn theorem.

## 8. A common full-rank resource-cocircuit axiom for cube and boundary models

The resource-support theorem has a direct counterpart in NORI1 and therefore supplies another **intrinsic hypothesis shared by the two canonical models**.

Let \(\mathsf R\) denote the original-resource matroid of a polarized exchange-gallery system and \(\Lambda_\varepsilon\) the set of resource labels occurring on primitive states or forward transitions of color \(\varepsilon\). Consider the matroid property
\[
\boxed{
r_{\mathsf R}(\Lambda_0)
=r_{\mathsf R}(\Lambda_1)
=r(\mathsf R).
}
\tag{18}
\]
Equivalently, **each color support meets every cocircuit of the original-resource matroid**. This equivalence is standard: a set spans a matroid if and only if it intersects every cocircuit.

**Theorem 10 (common cocircuit-hitting resource supports).** Both canonical Article XI models satisfy (18) for every permitted reversal-odd coloring, with the following refinements.

(a) For the antipodal \(n\)-cube, \(\mathsf R\) is the free matroid on the \(n\) coordinate directions. Each color occurs on precisely \(2^{n-2}\) edges of each coordinate direction, for \(n\ge2\). In particular, \(\Lambda_0=\Lambda_1=[n]\), and each color meets every singleton cocircuit.

(b) For the ordinary boundary 3-tournament, \(\mathsf R=M(K_n)\), and for every nonempty proper \(S\subset[n]\),
\[
\boxed{
|\Lambda_\varepsilon\cap\delta_{K_n}(S)|
\ge |S|(n-|S|)-\min(|S|,n-|S|).
}
\tag{19}
\]
Consequently the resource-support graph \(([n],\Lambda_\varepsilon)\) is \((n-2)\)-edge-connected for every \(n\ge3\), and it contains a Hamilton cycle whenever \(n\ge4\).

*Proof.* For (a), the \(2^{n-1}\) cube edges of any coordinate direction split into \(2^{n-2}\) antipodal edge pairs, and reversal oddness selects one edge of each color in each pair. For (b), Theorem 6 says the missing resource-edge graph is a matching. At most \(\min(|S|,n-|S|)\) edges of that matching cross a cut \(\delta(S)\), proving (19). Its minimum over nontrivial \(S\) is at least \(n-2\) for \(n\ge3\), giving the edge-connectivity bound. Since the support graph has minimum degree at least \(n-2\ge n/2\) for \(n\ge4\), Dirac's Hamilton-cycle theorem applies. \(\square\)

The common full-rank cocircuit-hitting condition (18) is a natural addition to the proposed abstract class of **polarized resource-exchange matroids**. It is an all-color, all-dimensional restriction stronger than merely saying that the uncolored gallery system admits every resource permutation. But it is still not a path selector: the five-vertex counterexample in Proposition 5 has almost-complete full-rank red resource support and even a Hamilton resource cycle, without any coherent monochromatic spanning tight path. A closure proof must exploit **how** these abundant resource labels are realized by adjacent colored covering transitions.

## 9. Matroid base-packing abundance for each color

The cocircuit-hitting theorem also yields a quantitative **spanning-basis packing** result for the color-specific resource supports. This survives in arbitrarily large order and can be useful for future exchange arguments that must avoid a bounded set of resource labels.

**Theorem 11 (boundary spanning-tree packing).** For an ordinary reversal-odd boundary 3-tournament on \(n\ge4\) vertices, let \(B_\varepsilon\) be the colored covering edges and let \(\Lambda_\varepsilon=\lambda(B_\varepsilon)\). Then \(\Lambda_\varepsilon\) contains at least
\[
\boxed{k_n=\left\lfloor\frac{n-2}{2}\right\rfloor}
\tag{20}
\]
pairwise edge-disjoint spanning trees of \(K_n\). Equivalently, the pullback resource matroid
\[
\lambda^*M(K_n)
\]
on the covering-transition ground set contains \(k_n\) pairwise disjoint bases comprised entirely of color-\(\varepsilon\) transitions.

*Proof.* By Theorem 10(b), the resource-support graph \(([n],\Lambda_\varepsilon)\) is \((n-2)\)-edge-connected, hence \(2k_n\)-edge-connected. For every partition of its vertex set into \(t\ge2\) nonempty parts, each part has at least \(2k_n\) crossing incidences. Counting edges crossing between parts twice gives at least \(k_n t\ge k_n(t-1)\) such edges. The Nash-Williams–Tutte spanning-tree packing criterion therefore supplies \(k_n\) edge-disjoint spanning trees. For each tree edge choose one color-\(\varepsilon\) covering transition with that resource label. Since the trees have disjoint resource-edge sets, these choices give disjoint bases of the parallel-extension pullback matroid. \(\square\)

**Proposition 12 (cube analogue).** For the antipodally odd \(n\)-cube, \(n\ge2\), let \(\lambda\) label each colored cube edge by its coordinate direction and let \(\mathsf R\) be the free matroid on \([n]\). For either fixed color, the parallel-extension pullback \(\lambda^*\mathsf R\) on the cube-edge set contains
\[
\boxed{2^{n-2}}
\tag{21}
\]
pairwise disjoint full-rank bases, and no larger number is possible.

*Proof.* In each direction there are precisely \(2^{n-2}\) edges of each color, by Theorem 10(a). A basis of the parallel-extension free matroid chooses one edge in every direction. Pair the direction-\(i\) edges arbitrarily with the indices \(1,\ldots,2^{n-2}\); selecting the edges with the same index across all directions gives \(2^{n-2}\) disjoint bases. Conversely every such basis consumes one colored edge of each direction, and only \(2^{n-2}\) are available. \(\square\)

Hence **both canonical models have many single-color full-rank resource bases**, in addition to the covering graphic-flat and pointed binary matroid structure. The quantitative base-packing property is still weaker than the spanning-path conjectures, because independent resource representatives chosen from different covering states need not be geometrically adjacent or coherently directed. The challenge is to turn this substantial matroid-rank redundancy into a **coherent basis-path selector** using covering monodromy and the antipodal path language.

## 10. Common two-color resource bases and the rarity of forced gates

The preceding full-rank and base-packing statements concern each color separately. The two colors also share a substantial **common** graphic resource support, even in worst-case tournaments.

Let \(F_\varepsilon=E(K_n)\setminus\Lambda_\varepsilon\) denote the color-\(\varepsilon\) missing-resource matching, and define
\[
\boxed{
H_b=([n],\Lambda_0\cap\Lambda_1)
=K_n-(F_0\cup F_1).
}
\tag{22}
\]

**Theorem 13 (simultaneous full rank and Hamiltonian common support).** For every ordinary reversal-odd boundary tournament:
\[
\boxed{
F_0\cap F_1=\varnothing,\quad
\Delta(F_0\cup F_1)\le2,\quad
\delta(H_b)\ge n-3.
}
\tag{23}
\]
Consequently, for \(n\ge5\),
\[
\boxed{r_{M(K_n)}(\Lambda_0\cap\Lambda_1)=n-1;}
\tag{24}
\]
for \(n\ge6\), \(H_b\) has a Hamiltonian cycle; and for \(n\ge7\), \(H_b\) is Hamilton-connected.

*Proof.* A resource edge \(\{u,v\}\) cannot be absent from both color supports, since each ordered triple entering the state \((u,v)\) has one of the two colors and would represent that same resource edge. Thus \(F_0\cap F_1=\varnothing\). By Theorem 6 each \(F_\varepsilon\) is a matching, so their union has maximum degree at most two, proving (23). For \(n\ge5\), each component of \(H_b\) contains at least \(\delta(H_b)+1\ge n-2\) vertices. Two components would require at least \(2(n-2)>n\) vertices, impossible; thus \(H_b\) is connected and its original graphic resource rank is \(n-1\). For \(n\ge6\), \(\delta(H_b)\ge n-3\ge n/2\), so Dirac's theorem gives a Hamiltonian cycle. For \(n\ge7\), every pair of nonadjacent vertices has degree sum at least \(2(n-3)\ge n+1\); Ore's Hamilton-connectedness theorem gives a Hamilton path between any prescribed pair of vertices. \(\square\)

The common-support graph omits a graph of maximum degree two whose components are isolated vertices, alternating paths, and even alternating cycles (the two omitted matchings alternate in any nontrivial cycle). In particular, **the same original resource basis can be represented by transitions of either color**, though the two representations need not be coherently adjacent or have compatible roots.

**Corollary 14 (any designated gate can occupy the unique unsupported position).** Let \(n\ge7\), and let \(e=\{u,v\}\in F_0\cup F_1\) be any missing-resource edge. There exists a Hamiltonian vertex order \(w\) containing \(u,v\) consecutively in an *interior* position, such that
\[
\boxed{
E(w)\setminus\{e\}\subseteq\Lambda_0\cap\Lambda_1.
}
\tag{25}
\]

*Proof.* By Theorem 13, the common-support graph \(H_b\) has a Hamiltonian path with prescribed endpoints \(u,v\). Adding the missing edge \(e=uv\) closes this path into a Hamiltonian cycle in which \(e\) is the sole edge outside \(H_b\). Delete a cycle edge not incident with \(e\) to obtain a spanning Hamiltonian path in which \(e\) is an interior resource edge and all other resource edges belong to both color supports. \(\square\)

This is a **resource-geometric**, not a colored-forward-path, statement: the color-\(\varepsilon\) representative of each common resource edge may occur at a completely different ordered-pair state. The theorem shows that the *placement* of a forced switching gate is never obstructed by ordinary graphic basis availability in orders \(n\ge7\). Forward path coherence remains the difficulty.

**Proposition 15 (forced gates are exponentially rare under random coloring).** Under the uniform probability measure on reversal-odd boundary 3-tournaments,
\[
\boxed{
\mathbb E|F_\varepsilon|
=\binom n2\,2^{-2(n-2)},\qquad
\Pr(F_0\cup F_1\ne\varnothing)
\le n(n-1)\,2^{-2(n-2)}.
}
\tag{26}
\]
In particular, with probability \(1-O(n^2 4^{-n})\), the **two** resource supports both equal the entire edge set \(E(K_n)\); no forced switching gate exists.

*Proof.* For a given edge \(\{u,v\}\), its absence from \(\Lambda_\varepsilon\) requires that all \(n-2\) ordered triples entering \((u,v)\) have color \(1-\varepsilon\), and likewise all \(n-2\) triples entering \((v,u)\). These are \(2(n-2)\) distinct reversal-pair bits: the first group has middle vertex \(u\), the second middle vertex \(v\), and no pair is the reversal of another in the same group or across groups. They are independent fair bits, so the absence event has probability \(2^{-2(n-2)}\). Sum over the \(\binom n2\) possible edges and use Markov's inequality and a union bound over both colors to obtain (26). \(\square\)

**Research limitation and next target.** The missing-resource matching and its phase gates are valuable *conditional* rerouting devices, but Proposition 15 rules out any universal proof that requires at least one missing resource: nearly all colorings have none. The stronger shared full-rank property (24) remains available even then. The natural missing theorem is therefore a **coherent basis-path synchronization principle**, converting the two full-color representatives of a common resource basis into oppositely rooted monochromatic arms whose union is independent, with at most one phase seam. Neither ordinary graphic matroid intersection nor uncolored Hamiltonicity implies that synchronization, as the preceding finite obstructions demonstrate.
