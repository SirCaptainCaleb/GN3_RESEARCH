# Linear adjacent-root instability of antipodal-geodesic switch minima

- Stable ID: note_article_xi_unbounded_neighbor_root_instability_20261012
- Author: unspecified; session provenance retained
- Primary home: article:nori_article_xi_matroidal_turn_geometry
- Labels: proved, all-dimensional, matroidal-geometry, root-reachability-obstruction
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6379_4
- Updated session: session_nori_r6379_4
- Disposition: none
- Successor: none

## Related references

- None

## Research note

# Linear adjacent-root instability for antipodally odd cube colorings

**Status: proved all-dimensional obstruction.** This construction disproves any dimension-independent bounded-cost rule transporting good antipodal geodesics from one root to a neighboring root. It is a counterexample to a proposed induction mechanism, not to the universal existence conjectures.

**Theorem.** For every even \(n=2m\ge4\), there exists an antipodally odd undirected two-edge coloring \(c\) of \(Q_n\) and adjacent vertices \(x,y\) such that
\[
\boxed{\mu_y(c)=0,\qquad \mu_x(c)\ge m-2.}\tag{1}
\]
Here \(\mu_z(c)\) is the minimum number of internal switches among full antipodal geodesics rooted at \(z\).

*Construction.* Fix \(x=0^n\), \(y=e_0\), and partition the other \(n-1\) coordinate directions into \(A,B\) of sizes \(a=m-1\) and \(b=m\). Begin with the layer-parity coloring
\[
r_i(v)=\sum_{j\ne i}v_j\pmod2.
\tag{2}
\]
Let \(P\) be the full antipodal geodesic rooted at \(y\), with direction order consisting of all directions of \(A\), then direction \(0\), then all directions of \(B\). Give every edge of \(P\) color zero, and every antipodal mate of those edges color one; leave every other edge colored as in (2). Because a full geodesic traverses each coordinate direction once, it cannot contain any edge and its antipodal mate. The assignment is therefore consistent, defines an undirected coloring, and is antipodally odd. By construction \(P\) is monochromatic, giving \(\mu_y=0\).

*Proof of the lower bound.* View any \(x\)-rooted full geodesic as a maximal monotone chain in the Boolean lattice of coordinate subsets, increasing Hamming weight one at every step. Its edge colors outside the modified edge set alternate with the rank parity, so any uninterrupted run of \(L\) unmodified steps forces \(L-1\) switches.

The modified edges are contained in four monotone chains plus two special direction-zero edges. Using notation where coordinates in a named set are either all zero or all one, the four chains are:
\[
\begin{array}{c|c|c|c}
\text{chain}&v_0&A&B\\
P_A&1&\text{prefix increases}&0\\
P_B&0&1&\text{prefix increases}\\
(\tau P_A)^{\rm rev}&0&\text{suffix increases}&1\\
(\tau P_B)^{\rm rev}&1&0&\text{suffix increases}.
\end{array}
\tag{3}
\]
Their rank-interval lengths are \(a,b,a,b\), respectively. The special direction-zero edges join \((v_0,A,B)=(1,1,0)\) to \((0,1,0)\), and \((0,0,1)\) to \((1,0,1)\).

An increasing Boolean-lattice chain can meet at most one of the four nonempty modified chains. Within either \(v_0\)-facet, meeting one chain requires filling a coordinate class that the other chain requires empty; since filled coordinates never become empty, both cannot be used. Crossing the \(v_0\)-coordinate after meeting a lower-facet modified chain precludes meeting either upper-facet chain by the same monotonicity. Likewise, the special direction-zero edges cannot be used together with any modified chain: each requires completing one coordinate class and leaving the other empty at the crossing, eliminating all modified-chain steps before and after it. Thus every increasing chain's modified edges lie either in a single rank interval of length at most \(m\), or consist of one direction-zero edge.

In the first case, at least \(n-m=m\) of its \(n\) steps lie outside one consecutive rank interval of length at most \(m\). These unmodified steps form at most two runs and alternate in color within each run, forcing at least \(m-2\) switches. In the second case, at least \(n-1\) unmodified steps form at most two runs, forcing at least \(n-3\ge m-2\) switches. This proves (1). \(\square\)

**Connection to the pointed matroid.** A rooted full geodesic is a marked shortest port cocircuit, with color-switch count determined by its intersection against the admissible port-containing binary cycle. Theorem (1) shows that the minimum intersection achievable *within a prescribed root fiber* can differ by \(\Omega(n)\) between neighboring fibers, even though the global minimum port-cocircuit intersection is two. The difficulty cannot be repaired by any dimension-independent root-local Lipschitz estimate. Any proof via root-indexed coboundary or gallery exchange must exploit nonlocal information.

**Computational cross-check.** Using subset DP over all direction-simple paths, the stated explicit construction with \(A=\{1,\dots,m-1\}\), \(B=\{m,\dots,2m-1\}\) has the following rooted switch minima:
\[
\begin{array}{c|cccc}
n&6&8&10&12\\ \hline
\mu_{0^n}&3&3&5&5\\
\mu_{e_0}&0&0&0&0
\end{array}
\]
The finite check is supplementary; the proof holds for every even \(n\).

**Relation to earlier notes and literature.** This construction strengthens the adjacent-square-exchange-radius obstruction established earlier in Article XI. The underlying layer coloring was discussed in Lawrence Hollom, *Hypercube geodesics with few colour changes*, arXiv:2605.20184 (2026), as an example of large average rooted geodesic-switch cost. The new feature recorded here is the surgical forcing of a monochromatic geodesic at one root while retaining a linear switch lower bound at its immediate neighbor.
