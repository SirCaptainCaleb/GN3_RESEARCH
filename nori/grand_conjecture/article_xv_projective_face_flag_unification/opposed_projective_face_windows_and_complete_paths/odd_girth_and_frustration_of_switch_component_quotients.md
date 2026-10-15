# Odd girth and frustration of switch component quotients

### Systolic and maximum-cut constraints on switch-component graphs

Let \(p:T\to H\) be a connected free double cover of a connected comparison graph, and let a legal odd coloring yield a quotient switch cocycle \(\eta\) with support \(S\). Let \(Z=(V(H),E(H)\setminus S)\). Contract every connected component of \(Z\) to obtain the connected multigraph \(F\), retaining all switches as edges, including possible loops. These objects are the cographic deletion normal form of the preceding gauge-criticality Subsection.

**Theorem 1 (short odd cycle survives all nonswitch contractions).** Suppose \(H\) contains a closed walk \(C\) of length at most \(L\) whose lift under the double cover joins a state to its involutive mate. Then \(F\) contains an odd circuit of length at most \(L\), with loops counted as odd circuits of length one.

*Proof.* Every legal switch cochain represents the covering class, so \(\sum_{e\in C}\eta(e)=1\pmod2\). Contracting nonswitch edges maps \(C\) to a closed walk in \(F\); the walk traverses precisely the switched edges of \(C\), counted with multiplicity, and has odd length at most \(L\). Every odd closed walk in a multigraph decomposes into circuits, at least one of which has odd length no greater than the walk. QED.

**Corollary 2 (uniform odd-girth bounds in the two unrestricted models).** For any antipodally odd edge coloring of \(Q_n\), the component multigraph \(F\) has odd girth at most \(n\), attained as an upper bound by following a full projective dimension-simple Petrie loop of length \(n\). For any reversal-odd ordered-triple coloring on \(n\ge5\) symbols, \(F\) has odd girth at most six, using the six-step reversal-monodromy walk in the preceding local-cycle Subsection.

**Theorem 3 (quantitative persistent frustration).** Let \(m=|S|=|E(F)|\). Then
\[
\boxed{m-\operatorname{MaxCut}(F)\ \ge\
\begin{cases}
(n-1)2^{n-2},& H=L(Q_n)/J,\quad n\ge3,\\[2pt]
\dfrac{n-4}{4(n-3)}\,|E(H)|,&H=O_n/R,\quad n\ge6.
\end{cases}}
\tag{1}
\]
Consequently, if \(m\) exceeds the respective lower bound by fewer than \(\lambda(F)\) edges, then the zero-switch graph \(Z\) must be connected.

*Proof.* By the cographic deletion theorem, deleting a maximum cut of \(F\) is legal and removes \(\operatorname{MaxCut}(F)\) switches without adding others. The resulting odd coloring has \(m-\operatorname{MaxCut}(F)\) switched comparisons. Every legal cube comparison cochain has at least \((n-1)2^{n-2}\) switches, by the sharp Petrie-averaging cosystole calculation. Every legal reversal-odd triple comparison cochain has at least \(((n-4)/(4(n-3)))|E(H)|\) switches, by the complementary signed-spectral bound in the matroid generalizations section. This proves (1). If \(Z\) is disconnected, \(F\) has at least two vertices and therefore admits a nonempty cut of size at least \(\lambda(F)\). The maximum cut is at least that large, so (1) implies \(m\) is at least the lower bound plus \(\lambda(F)\). Contraposition proves the connectivity criterion. QED.

**Corollary 4 (frustration survives every legal monotone reduction).** The maximum-cut residual graph is still forced to contain an odd circuit of length at most the monodromy length bound from Corollary 2, and its remaining number of switched comparisons obeys (1). Thus no sequence of legal switch deletions can collapse the odd class to a bipartite component quotient; its frustrated core carries both a short odd-cycle certificate and a globally extensive support constraint.

**Interpretation.** The inherited short odd cycle is a *local witness of nonzero covering monodromy*, whereas the maximum-cut deficit measures the global complexity of maintaining that monodromy across all comparisons. The boundary model differs sharply from the cube: its residual signed switch support is a positive fraction of all turns asymptotically, while the cube can reach fraction \(1/n\). Neither statement by itself forces a spanning Hamilton path with one switch or a dimension-simple monochromatic cube geodesic. Their combined constraints provide quantitative tests for proposed switch-critical counterexamples and legal deletion strategies.
