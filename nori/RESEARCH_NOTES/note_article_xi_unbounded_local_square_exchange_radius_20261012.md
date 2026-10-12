# Unbounded local-exchange radius for shortest port cocircuits

- Stable ID: note_article_xi_unbounded_local_square_exchange_radius_20261012
- Author: unspecified; session provenance retained
- Primary home: article:nori_article_xi_matroidal_turn_geometry
- Labels: proved, structural-obstruction, matroid-duality
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6379_4
- Updated session: session_nori_r6379_4
- Disposition: none
- Successor: none

## Related references

- None

## Research note

**Proved all-dimensional obstruction to bounded-radius shortest-port-cocircuit descent.** Let \(n=2m\ge4\). Color each undirected coordinate-\(i\) edge of \(Q_n\) by
\[
c_i(x)=\sum_{j\ne i}x_j\pmod2.
\]
This does not depend on \(x_i\), and global complementation changes its value by \(n-1=1\pmod2\), so the coloring is antipodally odd.

**Theorem.** Any antipodal geodesic rooted at the zero vertex has cyclic turn weight \(n-1\), but the same coloring has a monochromatic antipodal geodesic (cyclic turn weight one). Every path in the marked minimum-port-cocircuit gallery connecting these two types of witnesses, using cyclic rerooting and adjacent coordinate-square swaps, requires at least \((n-2)/2\) swaps. Reaching weight at most three from the zero-rooted geodesic requires at least \((n-4)/2\) swaps.

*Proof.* For a geodesic from zero, the step-\(t\) color is \(t-1\pmod2\), independently of the direction order. These colors alternate, producing \(n-1\) internal changes and no changed antipodal seam, so the cyclic weight is \(n-1\).

Choose a starting vertex with \(m\) zero coordinates and \(m\) one coordinates. Follow directions whose initial coordinate values alternate \(0,1,0,1,\ldots\). The parity of the current vertex at step \(t\) is \(m+t-1\), and the unused coordinate in the chosen direction equals \(t-1\); therefore each traversed edge has color \(m\pmod2\). Hence the full antipodal geodesic is monochromatic and has cyclic weight one.

Cyclic rerooting preserves cyclic turn weight. Swapping consecutive coordinate steps alters only three adjacent turn comparisons, and the weights before and after are positive odd integers; their difference is in \(\{-2,0,2\}\). Thus \(k\) swaps can decrease cyclic turn weight by at most \(2k\). The two distance bounds follow. \(\square\)

**Matroid statement.** Each full geodesic determines a shortest port cocircuit \(Y_C=C\cup\{p\}\), with \(|X_d\cap Y_C|=1+w_d(C)\). Consequently the minimum-cocircuit intersection objective is 2-Lipschitz on adjacent square exchanges, while this family realizes a range \(n-2\). There can be no dimension-independent finite-radius local square-exchange procedure that starts from an arbitrary minimum port cocircuit and always reaches intersection at most four, even when a two-intersection cocircuit already exists.

This is a structural obstruction to greedy or bounded-radius proof strategies, not a counterexample to NORI1. Global methods, topological constraints on the entire exchange complex, and nonlocal exchanges remain viable.

**Sharp fixed-root spectrum and relation to Hollom's layer coloring.** For the same coloring on \(Q_{2m}\), fix a root \(x\) of Hamming weight \(k\). Let \(\pi\) range over all permutations of coordinate directions. The minimum number of *internal* switches among \(x\)-to-\(\bar x\) geodesics satisfies
\[
\boxed{\mu_x=\max\{0,\,2|k-m|-1\}.}\tag{3}
\]
The minimum cyclic turn weight of these geodesics is
\[
\boxed{\min_\pi w_d(C_{x,\pi})=\max\{1,\,2|k-m|-1\}.}\tag{4}
\]
Here the cyclic turn cycle depends on both the root and direction order; root rotation of one cycle need not retain the same root.

*Proof.* If \(a_t=x_{\pi_t}\), the color at step \(t\) is
\[
c_{\pi_t}(x^{\{\pi_1,\dots,\pi_{t-1}\}})
=k+t-1+a_t\pmod2.
\]
Thus a change at the \(t\)-th internal turn occurs if and only if \(a_t=a_{t+1}\). An arrangement of \(k\) ones and \(2m-k\) zeros can have at most \(2\min(k,2m-k)\) adjacent unlike pairs when the two counts differ; its minimum number of equal adjacent pairs is then \(2m-1-2\min(k,2m-k)\). If \(k=m\), alternating all bits gives zero equal adjacent pairs. This proves (3).

For the cyclic turn word, its closing seam changes precisely when \(a_{2m}\ne a_1\), because the final edge color is compared with the complement of the initial one. When \(k\ne m\), arranging the minority bits separately between majority bits gives \(2\min(k,2m-k)\) unlike internal pairs and equal endpoint bits, so cyclic turn weight \(2m-1-2\min(k,2m-k)\). Any arrangement with unlike endpoints loses at least one internal unlike pair and adds one changed closing turn, giving no improvement. At \(k=m\), perfect alternation has no internal color changes and the closing seam contributes one. This gives (4). \(\square\)

The local turn signature has a simple form: at a vertex \(x\), the disagreement between the direction-\(i\) and direction-\(j\) edges is
\[
\boxed{d_{ij}([x])=x_i+x_j\pmod2.}\tag{5}
\]
Thus this signed cocycle is induced by the partition of incident directions according to the current vertex bits.

This example is the antipodally odd even-dimensional version of the **layer coloring** discussed by Lawrence Hollom, *Hypercube geodesics with few colour changes*, arXiv:2605.20184 (2026), Section 3. Hollom notes that layer coloring makes the expected minimum switch count for a uniformly random starting vertex of order \(\sqrt n\). The fixed-root formula above explains the effect more fully and the preceding exchange-distance theorem translates it into an obstruction for pointed-matroid gallery descent. It is not presented as an unrelated newly discovered coloring family.
