# An odd cycle of nearly complementary supports in uncolored R(x) forces antipodal monochromatic closure

# COLOR-FREE reachability odd-cycle obstruction and the middle Kneser graph

Let c be an antipodally odd binary UNDIRECTED edge coloring of Q_n. For root x write
\[
\mathcal R_x=\{S\subseteq[n]:x\oplus S\in R(x)\},
\]
where R(x) is the color-FREE set of endpoints of monochromatic geodesics starting at x, of EITHER color. Define a graph \(\Gamma_x\) on \(\mathcal R_x\) by joining distinct supports S,T exactly when
\[
S\cap T=\varnothing,\qquad S\cup T=[n]\setminus\{i\}
\]
for some i. Thus two adjacent supports are disjoint and cover n-1 of the n coordinate directions.

**Theorem (odd-cycle reachability certificate).** If \(\Gamma_x\) is nonbipartite for any root x, then c has a MONOCHROMATIC FULL ANTIPODAL GEODESIC. Equivalently, in every hypothetical counterexample, \(\Gamma_x\) is bipartite for EVERY x. This condition is expressed entirely in the uncolored reachability set R(x); it requires no colors in the definition or the topological labeling.

**Proof.** Let S--T be an edge of \(\Gamma_x\). Any two actual monochromatic geodesics from x to x⊕S and x⊕T with the SAME color concatenate in reverse/forward order to a monochromatic (n-1)-edge geodesic, omitting the sole direction i. Its two possible endpoint-extension edges are antipodes and therefore have opposite colors; one has the path color and produces a full monochromatic antipodal geodesic. Consequently, under the hypothesis of NO full monochromatic antipodal geodesic, two reachable supports joined by an edge must have OPPOSITE witness colors. Furthermore, a support incident to any edge must admit a UNIQUE possible monochromatic witness color, since availability of both colors would allow a same-color match with its neighbor. These unique witness colors give a proper binary vertex coloring of all nonisolated vertices of \(\Gamma_x\). Isolated vertices can be colored arbitrarily. Hence \(\Gamma_x\) is bipartite. Contraposition proves the theorem. \(\square\)

**Odd dimensions and the Kneser graph.** For n=2k+1, restrict \(\Gamma_x\) to reachable supports of size k. Two k-subsets are joined exactly when they are disjoint, so this is the subgraph of the Kneser graph KG(2k+1,k) induced by the reachable middle-layer supports. The full KG(2k+1,k) contains an explicit (2k+1)-cycle. For any order p_1,...,p_n, set S_0={p_2,p_4,...,p_{2k}} and iteratively
\[
S_t=S_{t-1}\mathbin{\triangle}([n]\setminus\{p_t\}),\quad 1\le t\le n.
\]
Because p_t has bit 0 in S_{t-1}, S_{t-1} and S_t are disjoint k-subsets whose union omits exactly p_t. Each step toggles 2k bits, preserving cardinality k. The n steps return to S_0 because each coordinate is toggled n-1 times, an even number. The S_t for 0<=t<n are distinct (any shorter nonempty consecutive product of distinct toggle masks is nonzero). Hence they form an odd n-cycle. If ALL these S_t lie in \(\mathcal R_x\), closure follows.

**Quantitative obstruction.** For every hypothetical counterexample, at least one vertex of each such middle-layer n-cycle is absent from \(\mathcal R_x\). Averaging the n cyclic supports over uniformly random permutations p, each position is uniformly distributed among k-subsets. Therefore every root x has at least
\[
\frac1n\binom nk
\]
unreachable k-subsets. For n=3, k=1, all singletons are reachable from every root, contradicting this condition, giving an immediate proof of the edge-geodesic conjecture in n=3.

**Parity limitation.** For even n, every edge of \(\Gamma_x\) joins a set of even size to a set of odd size, because |S|+|T|=n-1 is odd. Thus \(\Gamma_x\) is automatically bipartite in even dimension; the odd-cycle criterion provides information only for odd n (or after a further higher-order construction).

**Research direction.** The theorem changes topological extraction from a single 'balanced ridge is good' assertion to a global statement: seek topological / Kneser / Tucker forcing of a nonbipartite near-complementary-support graph \(\Gamma_x\) for SOME root x. This is a precise COLOR-FREE reachability-label coincidence: the desired odd-cycle vertices are actual reachable supports, and the edge-color witness consistency is derived only in the extraction proof. The existence of such a root for all odd-colorings remains an unsolved forcing obligation; the theorem itself is an exact sufficient condition.
