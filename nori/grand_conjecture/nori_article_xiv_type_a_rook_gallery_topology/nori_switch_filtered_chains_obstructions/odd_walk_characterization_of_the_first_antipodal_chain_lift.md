# Odd-walk characterization of the first antipodal chain lift

# Odd-walk characterization of the first antipodal chain lift

Let \(c:E(Q_n)\to\mathbb F_2\) be an antipodally odd coloring. Let \(K_0,K_1\) be the directed monochromatic endpoint-poset complexes, let \(K=K_0\cup K_1\), and put \(I=K_0\cap K_1\). There are two commuting involutions on directed endpoint pairs,
\[
\boxed{A(u,v)=(\bar u,\bar v),\qquad J(u,v)=(v,u),\qquad R=AJ.}
\tag{1}
\]
Antipodality \(A\) exchanges \(K_0,K_1\), while reversal \(J\) preserves each of them. The map \(R\) therefore exchanges colors and acts as the involution in the NORI1 chain-tower construction.

Write \(\mathscr C\) for the finite set of connected components of \(K_0\). Reversal \(J\) acts as an involution on \(\mathscr C\). For a bi-monochromatic directed endpoint pair \(p\in I\), let \(C(p)\in\mathscr C\) denote the red component containing \(p\), and define a (possibly looped, undirected) graph
\[
\boxed{
G_c:\quad
V(G_c)=\mathscr C,\qquad
C(p)\sim C(Ap)\quad(p\in I).
}
\tag{2}
\]
This adjacency is symmetric because \(Ap\in I\) and \(A^2p=p\). Multiple intervals producing the same adjacency may be identified. The graph is preserved by \(J\) because \(Jp\in I\), and the corresponding adjacency is \(JC(p)\sim JC(Ap)\).

**Theorem 1 (two-color incidence as a bipartite double cover).** Let \(\Gamma_c\) be the bipartite incidence graph whose two vertex classes are the connected components of \(K_0\) and \(K_1\), with one edge for every nonempty intersection of a red and a blue component. Under the identification of a blue component \(A(C)\) with \(C\in\mathscr C\), one has an isomorphism
\[
\boxed{
\Gamma_c\cong G_c\times_{\rm bip}K_2,
}
\tag{3}
\]
where the right side is the bipartite double cover with vertices \((C,\epsilon)\), \(\epsilon\in\mathbb F_2\), and an edge \((C,0)\sim(D,1)\) for each graph edge \(C\sim D\). Under this isomorphism the antipodal reversal acts by
\[
\boxed{R(C,\epsilon)=(JC,1-\epsilon).}
\tag{4}
\]

*Proof.* An interval \(p\in I\) belongs to the red component \(C(p)\), and belongs to a blue component \(B(p)\). Since \(A\) maps the blue complex onto the red complex, \(AB(p)=C(Ap)\). Thus \(p\) gives an edge from \((C(p),0)\) to \((C(Ap),1)\) in the double cover. Applying \(A\) to \(p\) gives the reverse sheet edge. Every incidence edge arises from some bi-monochromatic interval, proving (3). Finally \(A\) exchanges sheets, while \(J\) preserves the sheets and sends component \(C\) to \(JC\); they commute, proving (4). \(\square\)

**Theorem 2 (odd-walk criterion).** The first antipodal chain equations
\[
\boxed{
\varepsilon z_0=1,\qquad
\partial z_1=(1+R)z_0
}
\tag{5}
\]
admit a solution in \(C_0(K;\mathbb F_2)\) and \(C_1(K;\mathbb F_2)\) if and only if
\[
\boxed{\text{there is an odd-length walk in }G_c
\text{ from some }C\text{ to }JC.}
\tag{6}
\]

*Proof.* By the first chain-equation theorem in the preceding Subsection, (5) is solvable if and only if \(\Gamma_c\) has a connected component preserved by \(R\), equivalently if some vertex \(v\) is connected to \(Rv\). Choose \(v=(C,0)\) in the double-cover model (3). Its image is \(Rv=(JC,1)\). A walk in \(G_c\) from \(C\) to \(JC\) lifts from \((C,0)\) to \((JC,1)\) precisely when it has odd length, since every edge toggles the sheet. Thus the two conditions are equivalent. \(\square\)

**Corollary 3 (finite parity classification).** The first chain equations (5) are solvable if and only if some connected component \(W\) of \(G_c\) is preserved by \(J\) and satisfies at least one of the following:
\[
\boxed{
\begin{array}{ll}
\text{(a)}&W\text{ is nonbipartite};\\
\text{(b)}&W\text{ is bipartite and }J\text{ exchanges its two bipartition classes}.
\end{array}}
\tag{7}
\]
Loops count as odd cycles in (a).

*Proof.* In a connected nonbipartite graph, any two vertices are joined by walks of either parity, obtained by inserting an odd closed walk. In a connected bipartite graph, the parity of a walk between two vertices is odd precisely when they belong to opposite bipartition classes. An automorphism preserving the connected component either preserves its two bipartition classes individually or swaps them. Apply Theorem 2. \(\square\)

**Connection to color-component classification.** The vertices of \(G_c\) can be determined from the ordinary red edge graph by the preceding nonbacktracking component theorem: every red connected edge subgraph with a branching vertex yields one reversal-fixed node; a red path yields two nodes exchanged by \(J\); and a red cycle yields one node if it has an opposed pair of cube-geodesic half-cycles, otherwise two nodes exchanged by \(J\). Consequently the first equivariant chain equation is governed by an ordinary finite graph with a graph involution, rather than by a higher-dimensional extension problem.

**Limitations and proof direction.** Theorem 2 does not guarantee an odd walk for every legal coloring; that would be a new substantive connectivity assertion. It supplies a lower-complexity necessary and sufficient condition for the first stage. If such an odd walk exists, one can select a first tower chain \(z_1\), but extending the tower requires filling the homology class of \((1+R)z_1\). The forest-collapse theorem shows this higher class may encounter nontrivial directed-turn homology even in acyclic monochromatic edge components.
