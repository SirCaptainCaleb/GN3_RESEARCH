# Nonbacktracking color components and the first antipodal chain equation

# Nonbacktracking color components and the first antipodal chain equation

Let \(c:E(Q_n)\to\mathbb F_2\) be any binary edge coloring, \(n\ge2\). For \(a\in\{0,1\}\), let \(H_a\) be the spanning subgraph consisting of all edges of color \(a\). Let \(P_a(c)\) be the directed monochromatic geodesic endpoint poset of Article XIV and \(K_a=\Delta P_a(c)\).

For any graph \(H\subseteq Q_n\), define the **nonbacktracking arc graph** \(N(H)\) as the ordinary undirected graph whose vertices are ordered arcs \((u,v)\) for every edge \(uv\in H\), and whose adjacency is
\[
\boxed{(u,v)\sim(v,w)\quad\text{if }uv,vw\in H,\ u\ne w.}
\tag{1}
\]
The condition \(u\ne w\) means that the consecutive edges have different cube directions, so their concatenation is a dimension-simple geodesic of length two.

**Lemma 1 (generation by arc turns and equal-endpoint identifications).** Every vertex \(p=(u,v)\) of \(K_a\) is connected within \(K_a\) to all the directed arcs of every monochromatic geodesic from \(u\) to \(v\). Each edge of \(N(H_a)\) is realized by a two-step monochromatic interval vertex of \(K_a\). Thus the connected components of \(K_a\) are obtained from those of \(N(H_a)\) by identifying directed arc components whenever they occur among the directed arcs of two or more monochromatic geodesics between the same endpoint pair.

*Proof.* A directed arc \((x,y)\) along a monochromatic dimension-simple geodesic from \(u\) to \(v\) is a directed subinterval of \((u,v)\); the prefix and suffix of that geodesic certify its comparison to \((u,v)\) in \(P_a(c)\). Hence an edge of the one-skeleton of \(K_a\) joins their poset vertices. In particular every monochromatic interval is attached to the arc graph, and distinct monochromatic witnesses of the same interval attach through that common vertex. An adjacency (1) consists of consecutive arcs of a red or blue two-step geodesic and is realized by their comparisons to its ordered endpoint pair. Conversely, for each poset comparison, the monochromatic extension certificates can be joined with an interior monochromatic path to realize both comparable intervals in one path, so all their directed arcs lie in a common component after the indicated equal-endpoint identifications. This proves the statement. \(\square\)

**Theorem 2 (component classification).** Let \(H\) be a connected component of \(H_a\) containing at least one edge. Its contribution to \(K_a\) has precisely the following connected-component count:

- **Branching case:** if some vertex of \(H\) has degree at least three, its entire endpoint-poset complex is connected.
- **Path case:** if \(H\) is a nontrivial path, it contributes precisely two components, representing the two orientations along the path.
- **Cycle case:** if \(H\) is a cycle of length \(2k\), it contributes one component if there exist opposite vertices \(u,v\) on that cycle with cube distance \(d_{Q_n}(u,v)=k\), and otherwise it contributes precisely two components.

In the cycle case, the condition says that the two complementary length-\(k\) half-cycles are both cube geodesics; such a pair of geodesics merges the two directed nonbacktracking components.

*Proof.* At a vertex \(v\) of degree \(d\) in \(H\), the local incidence graph in \(N(H)\) between the \(d\) incoming and \(d\) outgoing directed arcs is \(K_{d,d}\) with the \(d\) immediate-reversal pairs removed. If \(d\ge3\), this graph is connected, so both orientations of every incident edge belong to one component. For a neighboring vertex \(w\), both orientations of \(vw\) being in one component propagates this fact to each further incident edge: at degree two its two nonbacktracking continuations connect both orientations of the next edge, and at degree at least three the local graph is connected. Induction along paths in \(H\) shows that all arcs of a connected component containing a branching vertex lie in one component of \(N(H)\), hence of \(K_a\).

If every degree is at most two, \(H\) is a path or a cycle. Its nonbacktracking arc graph has precisely two components corresponding to the forward and reverse cyclic or linear orientations. In a path there is a unique directed simple path between two endpoints; thus no monochromatic interval can merge these components.

In a cycle there are precisely two simple paths between distinct vertices. They have equal length and are both cube geodesics precisely when the vertices separate the cycle into two length-\(k\) arcs and their Hamming distance is \(k\). In that case their shared ordered endpoint pair is a vertex of \(K_a\) incident with arcs of both cyclic orientations, merging the two components. If no such pair exists, every directed geodesic interval is supported in a unique cyclic orientation, and no identification is possible. Apply Lemma 1. \(\square\)

Now assume antipodal oddness, and put \(K=K_0\cup K_1\), \(I=K_0\cap K_1\), with \(R(u,v)=(\bar v,\bar u)\). Define a finite **color-component incidence graph** \(\Gamma_c\) as follows. Its vertices are the connected components of \(K_0\) and of \(K_1\), regarded as two distinct parts. For each directed endpoint pair \(p\) supporting both colors, join the component of \(K_0\) containing \(p\) to the component of \(K_1\) containing \(p\). Multiple such pairs may yield the same graph edge. The involution \(R\) swaps the two parts and acts on the graph.

**Theorem 3 (first antipodal tower criterion).** The connected components of \(K\) are naturally in bijection with the connected components of \(\Gamma_c\), compatibly with \(R\). Furthermore, the following are equivalent:

(i) There are chains \(z_0\in C_0(K;\mathbb F_2)\), \(z_1\in C_1(K;\mathbb F_2)\) satisfying
\[
\boxed{\varepsilon z_0=1,\qquad
\partial z_1=(1+R)z_0.}
\tag{2}
\]

(ii) \(K\) has a connected component preserved setwise by \(R\).

(iii) \(\Gamma_c\) has a connected component preserved setwise by its induced involution.

*Proof.* A connected component of the union of two simplicial complexes is determined by the incidence of their connected components through nonempty intersections. This is precisely \(\Gamma_c\), proving the first assertion and (ii) equivalent to (iii).

If (ii) holds, choose any vertex \(p\) of an \(R\)-preserved component. There is a one-skeleton path from \(p\) to \(Rp\); taking \(z_0=p\) and its mod-two edge chain as \(z_1\) proves (i).

Conversely, assume (i). For a component \(C\) of \(K\), the total parity of vertices in the boundary of a one-chain vanishes. Thus
\[
0=\varepsilon_C\partial z_1
=\varepsilon_C z_0+\varepsilon_{RC}z_0.
\]
If every component came in a distinct \(R\)-pair, this equation would make the total augmentation \(\varepsilon z_0\) even, contradicting its value one. Hence some component is preserved by \(R\). \(\square\)

**Corollary 4 (homological barrier after connectivity).** If \(n\ge5\) and no monochromatic full antipodal geodesic exists, then either the incidence graph \(\Gamma_c\) has no \(R\)-preserved component, or each such component of \(K\) has nontrivial mod-two homology in some positive degree at most \(\lfloor(n-1)/2\rfloor-1\). This follows from Theorem 3 and the antipodal chain-tower theorem of Article XIV.

In dimensions five and six, where the required tower height is two, the condition sharpens: whenever \(p,Rp\) lie in the same component and \(\gamma\) is any one-chain with \(\partial\gamma=p+Rp\), the cycle
\[
\boxed{(1+R)\gamma\in Z_1(K;\mathbb F_2)}
\]
must represent a nonzero homology class under a hypothetical NORI1 failure. Indeed otherwise a two-chain filling it would provide the forbidden tower of height two.

**Scope.** This is a connectivity classification, not a proof that a preserved component exists in every coloring. A monochromatic four-cycle provides a crucial exception to the naive nonbacktracking-component rule: its two orientations are joined by the rank-two monochromatic endpoint pair at its opposite corners. More generally, the cycle-geodesic clause of Theorem 2 cannot be discarded. The incidence graph describes the first chain equation entirely in finite graph-theoretic terms; the remaining higher homology is still sensitive to dimension-simple path compatibility.
