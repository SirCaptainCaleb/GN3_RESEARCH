# Hereditary reversal-cover switch sets and deletion-critical paths

# Hereditary reversal-cover switch sets and deletion-critical paths

Let \(G\to H=G/\tau\) be a two-sheeted graph cover with free involution and class \(\alpha\in H^1(H;\mathbb F_2)\). A binary state coloring \(b\) is reversal-odd if \(b(\tau v)=b(v)+1\). Its switch bit on edge \(vw\) is \(b(v)+b(w)\); the quotient switch cochains are precisely the affine cut coset \(\alpha+B^1(H;\mathbb F_2)\), as proved in the preceding local-cycle-integration subsection.

The two intended covers are (i) the line graph \(L(Q_n)\) of undirected cube edges under antipodality and (ii) the overlap graph of injective ordered triples under reversal. Restrict complete paths respectively to dimension-simple antipodal cube geodesics and Hamilton tight triple paths. Put \(\ell=[\mathbf1_{E(H)}]\), the graph-length parity class, and \(\beta=\alpha+\ell\). Define the realizable support family \(\mathfrak A_\alpha=\{\operatorname{supp}s:[s]=\alpha\}\) and its deletion closure
\[
\boxed{\mathfrak H_\alpha=\{D\subseteq S:S\in\mathfrak A_\alpha\}.}
\tag{1}
\]

**Theorem 1 (intrinsic hereditary characterization).** For every \(D\subseteq E(H)\),
\[
\boxed{D\in\mathfrak H_\alpha\iff \beta|_{H[D]}=0
\iff \forall C\subseteq H[D]\text{ cycles},\
|C|\equiv\langle\alpha,[C]\rangle\pmod2.}
\tag{2}
\]
This also means that on \(H[D]\), the reversal double cover is isomorphic to the canonical length-parity bipartite double cover.

*Proof.* Fix a representative \(s_0\) of \(\alpha\). A legal switch cochain equal to one on D has the form \(s_0+\delta f\), requiring \(\delta f(e)=1+s_0(e)\) for every \(e\in D\). These prescribed edge differences admit a vertex potential f if and only if their sum on each cycle of \(H[D]\) vanishes. That sum is \(|C|+\langle\alpha,[C]\rangle\), proving all equivalences. \(\square\)

**Theorem 2 (deletion closure preserves the path conjecture).** Given a family \(\mathscr P\) of admissible complete paths and an integer \(t\ge0\), the condition
\[
\forall S\in\mathfrak A_\alpha\ \exists P\in\mathscr P:
|S\cap E(P)|\le t
\]
is equivalent to
\[
\boxed{\forall D\in\mathfrak H_\alpha\ \exists P\in\mathscr P:
|D\cap E(P)|\le t.}
\tag{3}
\]
At \(t=1\), this is the boundary 3-tournament one-switch conjecture. For cubes it is equivalent to NORI1 by the established antipodal root-rotation lemma.

*Proof.* By (1), each hereditary set D is contained in a realizable S. Any path with at most t hits of S also has at most t hits of D. Conversely every realizable S is itself hereditary. The cube equivalence uses the odd total switch parity on a covering-odd rainbow projective cycle: a one-switch geodesic's projective closure has only one switch, which can be omitted by choosing another starting point. \(\square\)

**Theorem 3 (two-switch criticality).** If (3) at \(t=1\) fails and D is an inclusion-minimal hereditary counterexample, then
\[
\boxed{\forall e\in D\quad\exists P_e\in\mathscr P:
e\in E(P_e),\quad |D\cap E(P_e)|=2.}
\tag{4}
\]

*Proof.* Deleting e preserves the hereditary constraint and permits a complete path with at most one remaining hit. The original D hits every complete path at least twice. Thus the selected path uses e, with total count two. \(\square\)

**Proposition 4 (sharp size of legal coloring changes).** For \(n\ge3\), two distinct legal antipodally odd cube-edge switch sets differ on at least \(2(n-1)\) antipodal unoriented-turn orbits. For \(n\ge5\), the corresponding bound for reversal-odd ordered triple colorings is \(2(n-3)\) reversal-turn orbits. Both are sharp.

*Proof.* A legal change is a graph cut by the cohomology-class characterization. The relevant quotient incidence graphs are simple and vertex-transitive, with regular degrees \(2(n-1)\) and \(2(n-3)\). By Mader's edge-connectivity theorem a nonempty cut has size at least its degree. Recoloring one deck-paired state vertex produces a star cut, attaining the lower bound. For the alternate oriented-cube-arc state convention, one undirected turn has two directed traversals, and the cube bound doubles to \(4(n-1)\) directed-turn orbits. \(\square\)

**Cycle restrictions.** A triangle formed by three cube edges incident to one vertex has trivial cover monodromy and odd length, so it cannot lie entirely in a hereditary switch set. The same holds for a closed-lift tight pentagon of ordered triples. Averaging the latter condition over cyclic five-tuples shows that at least one fifth of ordered distinct quadruples have equal colors on overlapping ordered triples, and hence at any fixed tight-switch position at least \(n!/5\) Hamilton orders avoid that switch.

These results supply a signed-graph deletion-stable alternative to working directly in the nonhereditary affine coset of odd switch colorings. The hereditary family is not asserted to be a matroid independence system. Excluding its two-switch-critical configurations remains open.

Reference: Mader's edge-connectivity theorem for connected vertex-transitive graphs, as discussed in M. DeVos, *Sumsets and Connectivity of Symmetric Graphs*, Theorem 10.2.

## Uniform Hamilton incidence and a hereditary tournament density barrier

The same double-counting principle used for rainbow projective cube cycles applies to the second original geometry, now with Hamilton permutations rather than rainbow cycles.

Let \(n\ge5\). Let \(H_n^\triangle=O_n/R\) be the reversal quotient of the tight-overlap graph of distinct ordered triples, with \(R(abc)=cba\). Its quotient edge-orbits are reversal pairs of tight transitions \(abc\to bcd\). Put \(N=n(n-1)(n-2)/2\). Then
\[
\boxed{|V(H_n^\triangle)|=N,\qquad
|E(H_n^\triangle)|=N(n-3).}
\tag{8}
\]

**Theorem 5 (Hamilton turn incidence).** Every quotient turn edge of \(H_n^\triangle\) occurs in
\[
\boxed{2(n-3)!}
\tag{9}
\]
of the \(n!\) Hamilton vertex orderings, counted with their full ordered tight-transition lists. Consequently for every switch subset D,
\[
\boxed{
\mathbb E_{\pi\in S_n}|D\cap\operatorname{turns}(\pi)|
=(n-3)\frac{|D|}{|E(H_n^\triangle)|}.}
\tag{10}
\]

*Proof.* An oriented tight transition is specified by four distinct consecutive symbols \(a,b,c,d\). Treating this block as one item, the number of Hamilton orders containing it consecutively is \((n-3)!\). Its reversal \(d,c,b,a\) represents the same quotient transition and occurs in another \((n-3)!\) Hamilton orders. Summing gives (9). The n! Hamilton orderings each have n−3 tight transitions, so counting incidences yields (10). \(\square\)

**Theorem 6 (necessary density for hereditary one-switch counterexamples).** If \(D\in\mathfrak H_\alpha\) meets every Hamilton tight path in at least two marked turns, then
\[
\boxed{
|D|\ge n(n-1)(n-2),\qquad
\frac{|D|}{|E(H_n^\triangle)|}\ge\frac2{n-3}.}
\tag{11}
\]
Conversely, every hereditary D has
\[
\boxed{\frac{|D|}{|E(H_n^\triangle)|}\le\frac45}
\tag{12}
\]
because no such D may contain all five edges of a closed-lift tight pentagon.

*Proof.* By Theorem 5, the mean marked-turn count over Hamilton orders is \((n-3)|D|/|E|\). If each count is at least two, its mean is also at least two, proving (11). For (12), choose the family of closed-lift pentagons defined by cyclic lists of five distinct symbols. Each pentagon has trivial \(\alpha\)-monodromy but odd length; hence the hereditary cycle criterion forbids D from containing all five of its edges, bounding its D-hit count by four. The full symbol-permutation group is transitive on quotient turn edges and preserves this pentagon family, so every turn edge occurs in the same number of pentagons. Double-counting pentagon-edge incidences yields \(5|D|/|E|\le4\), proving (12). \(\square\)

For \(n=5\) the two inequalities are incompatible, recovering the one-switch Hamilton theorem in that dimension by a counting proof. For higher n the interval between the two bounds is nonempty, so a contradiction requires additional constraints on how selected turns distribute among intersecting Hamilton paths. The local pentagon restriction and global Hamilton incidence are the tournament analogues of the bipartite cube-corner bound and rainbow-cycle census, while the quantitative densities differ between the two geometries.

## A relative integrability test for tight three-hit witnesses

A three-hit rainbow cycle of a hereditary switch set is not automatically realizable with only those three switches by a legal coloring. The obstruction is a component-overlap holonomy, parallel to the red-blue seam incidence obstruction in Article XIV.

Let \(H\) be either reversal-cover quotient comparison graph, fix a representative one-cochain a of its covering class \(\alpha\), and let \(D\in\mathfrak H_\alpha\). Write \(U=(V(H),D)\) for the spanning marked-edge subgraph. Let C be a covering-odd cycle with \(|D\cap C|\) odd (in particular, a three-hit rainbow projective cycle). Put \(F=U\cup C\). Define a prescribed switch cochain \(\rho\) on F by
\[
\boxed{\rho(e)=1\ (e\in D),\qquad
\rho(e)=0\ (e\in E(C)\setminus D).}
\tag{9}
\]

**Theorem 7 (tight-witness extension criterion).** There exists a legal reversal-odd state coloring whose switch set contains D and whose switches on C are precisely \(D\cap C\) if and only if
\[
\boxed{[\rho]=\alpha|_F\ \text{in }H^1(F;\mathbb F_2).}
\tag{10}
\]
The condition already holds on U and on C separately. Its only possible failure is on cycles of F mixing marked-subgraph paths with unmarked arcs of C.

*Proof.* A legal quotient switch cochain has the form \(a+\delta f\). To equal \(\rho\) on F requires \(\delta f=\rho+a\) there. A vertex potential f exists precisely when this edge cochain has zero sum on every cycle of F, proving (10); extend f arbitrarily to all vertices of H. On U, this condition is \((\alpha+\ell)|_U=0\), which is the defining hereditary property. On C its sum is \(\alpha(C)+|D\cap C|=1+1=0\), by the hypotheses. Only mixed cycles can obstruct. \(\square\)

**Theorem 8 (overlap-multigraph holonomy).** Choose potentials \(f_U\) solving \(\delta f_U=\rho+a\) on U, and \(f_C\) solving the same equation on C. Let \(\Gamma(U,C)\) be the bipartite multigraph whose vertices are the connected components of U and the one connected component C, and whose edges are the connected components of \(U\cap C\). Label such an edge I by the constant bit
\[
\boxed{k_I=f_U(v)+f_C(v)\quad(v\in I).}
\tag{11}
\]
Then the extension criterion (10) holds if and only if the sum of these labels around every cycle of \(\Gamma(U,C)\) is zero. In particular, it always holds if every connected component of U meets C in at most one connected component.

*Proof.* The difference \(f_U+f_C\) is constant on every connected overlap component because both potentials have the same edge differences there. The potentials may be changed by a constant independently on each component of U and on C. They can be made to agree on overlaps precisely when the edge labels \(k_I\) are a coboundary on the overlap multigraph. This is equivalent to vanishing around its graph cycles. If each U component has at most one connected intersection piece with C, the overlap graph is a star forest and has no cycles. \(\square\)

**Research consequence.** A three-hit witness promised by inclusion-criticality carries a *relative integrability obstruction* invisible to its total three-hit parity. A potential proof that modifies an odd coloring around such witnesses must either control the overlap holonomy or work directly with the hereditary switch sets, where deleting a marked turn is always legal. This is a necessary bookkeeping step for converting cycle-criticality into a coloring-sensitive exchange argument.
