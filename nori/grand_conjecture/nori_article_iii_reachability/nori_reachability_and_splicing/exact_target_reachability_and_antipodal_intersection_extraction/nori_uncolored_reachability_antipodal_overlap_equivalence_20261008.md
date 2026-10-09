# Uncolored monochromatic reachability regions: antipodal overlap exactly characterizes edge-geodesic closure

# Uncolored reachability is sufficient for the antipodally odd edge case

Let \(Q_n\) carry an undirected binary edge coloring satisfying \(c(\bar e)=1-c(e)\). Define the **uncolored monochromatic-geodesic reachability region**
\[
R(x)=\{z\in Q_n:\text{there exists a monochromatic shortest path from }x\text{ to }z\},
\]
allowing either edge color and the length-zero path. No color index is required in the definition or in a topological labeling representing R.

**Exact equivalence.** The following are equivalent:

(i) A monochromatic full antipodal geodesic exists somewhere in \(Q_n\).

(ii) Some root x has an antipodal pair of vertices in its reachability region: \(R(x)\cap\overline{R(x)}\ne\varnothing\).

(iii) Some antipodal pair of roots \(x,\bar x\) has intersecting regions: \(R(x)\cap R(\bar x)\ne\varnothing\).

Proof. The oddness law maps a monochromatic x-to-z geodesic to a monochromatic \(\bar x\)-to-\(\bar z\) geodesic, of the complementary color. Thus \(R(\bar x)=\overline{R(x)}\), proving (ii)\(\Leftrightarrow\)(iii). If z lies in the intersection in (iii), take a monochromatic geodesic from x to z of color q and one from \(\bar x\) to z of color r. Their direction supports are complementary, so their concatenation (reversing the second path) is a full antipodal geodesic with at most one change. If q=r it is already monochromatic. If q differs from r, let the one-switch path have a q-colored prefix from x to z and an r-colored suffix from z to \(\bar x\). Append the antipodal copy of its q-colored prefix to its r-colored suffix. The appended portion has color \(1-q=r\), and the two direction supports are disjoint, yielding a monochromatic geodesic from z to \(\bar z\). Hence (iii) implies (i). Conversely a monochromatic full antipodal geodesic from x to \(\bar x\) witnesses \(\bar x\in R(x)\) and \(x\in R(x)\), proving (ii). QED.

**Topological research target.** Construct antipodally equivariant, actual-reachability-set labels on the root space and show that one fiber \(R(x)\) contains an antipodal vertex pair. Since \(R(\bar x)=\overline{R(x)}\), this is exactly equivalent to finding a common reachable vertex from antipodal roots, and it avoids unnecessary fixed-color labels. The main unsolved obligation is a genuine forcing theorem: standard equivariance alone does not ensure overlap. This concerns the simpler edge-colored case; an ordered-three-face NORI lift additionally requires correct directed path orientation and seam-window compatibility, because one-switch three-face windows do not automatically rotate into monochromatic ones.
