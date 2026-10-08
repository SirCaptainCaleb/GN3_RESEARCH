# Color-free root–support holonomy with exposed-edge blockers: odd cycles force geodesic closure

# Augmenting the color-free 2n-bit reachability holonomy graph by exposed-edge blockers

Let c be an antipodally odd binary UNDIRECTED edge coloring of Q_n. Start from the color-free reachable state graph H_R with vertices (x,S), S nonempty, x⊕S∈R(x), and signed edges: (A) root antipode sign 1; (B) endpoint swap sign 0; (C) same-root disjoint supports covering n-1 directions sign 1. Add the following signed edges, defined solely by the uncolored reachability states and the cube geometry:

(D) **Exposed-coordinate blockers**, sign 1: whenever (x,S) is reachable with |S|=n-2, and i∉S, connect
\[
(x,S)\longleftrightarrow(x,\{i\}),\qquad
(x,S)\longleftrightarrow(x\oplus S,\{i\}).
\]
The singleton states are always reachable.

**Theorem (augmented holonomy extraction).** If this augmented signed graph H'_R contains a closed walk with odd sign sum AND a (C) or (D) edge, then a monochromatic full antipodal geodesic exists. In any counterexample each connected component containing a (C) or (D) edge admits a consistent binary vertex potential with differences exactly given by the signs.

**Proof.** For a reachable state v=(x,S), let C(v)⊆{0,1} be the colors in which a monochromatic x-to-(x⊕S) geodesic exists. For (A), its image is 1-C(v); for (B), its image is C(v). For (C), the earlier near-complementary two-arm completion theorem shows that if C(v)∩C(w) is nonempty, closure follows. Under no closure, the sets at the two ends of every (C) edge are complementary singletons.

For a (D) edge, a witness q-path from x to x⊕S has n-2 edges, with i an unused direction. If either exposed i-edge at x or x⊕S had color q, prepending/appending that edge would give a monochromatic (n-1)-geodesic. Its two possible final edges are antipodal and of opposite colors, so it would extend to a full monochromatic antipodal geodesic. Therefore, in a counterexample BOTH exposed i-edges have color 1-q. In particular C(x,S) must be a singleton, and the singleton-state endpoint of (D) has precisely its complementary color. Unique witness colors propagate throughout any component containing (C) or (D), satisfying all signed edge conditions. An odd-signed closed walk is impossible. QED.

**Explicit seven-edge frustrated cycle (aligned two-facet lemma).** Fix a,b distinct and U=[n]\{a,b}. Suppose the states (x,U) and (x⊕e_a,U) are both reachable: there are monochromatic U-spanning geodesics in two adjacent parallel U-facets with exactly aligned projected endpoints. Write z=x⊕U and y=x⊕e_a. Then H'_R contains the seven-edge cycle
\[
(x,U)\xrightarrow{D}(x,\{a\})
\xrightarrow{B}(y,\{a\})
\xrightarrow{D}(y,U)
\xrightarrow{D}(y,\{b\})
\xrightarrow{A}(\bar y,\{b\})
\xrightarrow{B}(z,\{b\})
\xrightarrow{D}(x,U).
\]
All states are reachable. The signs are 1,0,1,1,1,0,1, totaling five (odd). Hence full closure. Note that bar y=z⊕e_b, so the fifth-to-sixth transition is indeed an endpoint swap in direction b.

**Geometric significance.** This graph is explicitly built on the user's 2n-bit root–support coordinates. It supports *uncolored* reachability labels and has two analytically justified sources of parity transport: nearly complementary common-root branches (C) and monochromatic n-2 branches blocked in unused directions (D). It subsumes the odd-middle-layer Kneser cycle and the adjacent matched-facet synchronization lemma. A topological proof could aim to FORCE nontrivial signed holonomy through these reachability-dependent edges; pure antipodal equivariance on the underlying 2n-bit torus has index one and alone cannot do so. The existence of such a cycle in all colorings is still unproved.
