# The color-preserving involution conjecture

The problem originates in **NORI1** and **reversal-odd boundary 3-tournaments**. We seek the weakest natural graph-theoretic hypotheses that encompass both classes and guarantee long rainbow paths with few binary-label switches. In particular, the binary labeling must remain unrestricted beyond the required involutive reversal; no additional relations between overlapping boundary triples may be assumed.

Let \(G=(V,E)\) be a finite connected simple graph with an ordinary edge coloring \(\lambda:E\to\mathcal C\), a binary edge labeling \(\chi:E\to\{0,1\}\), and an involutive vertex automorphism \(\tau\) satisfying \(\chi(\tau e)=1-\chi(e)\). Put \(k=\hat\delta(G,\lambda)=\min_{v\in V}|\{\lambda(e):e\ni v\}|\). The initial one-switch target asks for a vertex-simple rainbow path of at least \(k\) edges and at most one change in its \(\chi\)-sequence; the counterexamples below refute stronger special cases. Researchers should seek **minimal structural strengthenings applicable to both motivating classes**, and may examine weaker quantitative targets, especially linear-length paths with logarithmically many switches. Conditions must arise from their graph/resource geometry, not extra assumptions on their freely chosen binary labels.

**Theorem XIII.1 (eight-vertex counterexample).** A connected simple graph on eight vertices admits a proper three-edge-coloring \(\lambda\), a fixed-point-free involution \(\tau\) preserving \(\lambda\), and an edge labeling \(\chi\) reversed by \(\tau\), such that every rainbow path of length three has \(\chi\)-word \(010\) or \(101\). Thus \(\hat\delta(G,\lambda)=3\), but the longest rainbow path with at most one \(\chi\)-change has length two.

**Proof.** Take \(V=\{(i,s):i\in\{0,1,2,3\},\,s\in\mathbb F_2\}\). Define \(\varepsilon_{01}=1\) and \(\varepsilon_{ij}=0\) for the other five pairs \(i<j\), and put
\[
E=\{(i,s)(j,s+\varepsilon_{ij}):i<j,\ s\in\mathbb F_2\}.
\]
All sums involving sheet indices or edge labels are in \(\mathbb F_2\). Color the edges over \(01,23\) by \(A\), those over \(02,13\) by \(B\), and those over \(03,12\) by \(C\). Each vertex has one edge of each color. Each of the two sheets induces \(K_4-01\), and the two edges over \(01\) connect the sheets, so \(G\) is connected.

Set \(\gamma_{02}=\gamma_{03}=1\), with \(\gamma_{ij}=0\) for the other four pairs, and define
\[
\chi((i,s)(j,s+\varepsilon_{ij}))=s+\gamma_{ij}\quad(i<j),
\qquad \tau(i,s)=(i,s+1).
\]
The description of an edge with \(i<j\) is unique. Therefore \(\tau\) is a fixed-point-free automorphism preserving \(\lambda\) and complementing \(\chi\).

Project any rainbow three-edge path onto the base \(K_4\). The projected walk does not repeat an edge, as this would repeat a color. If it visits all four base vertices, its first and third edges are disjoint and have the same color in the specified one-factorization. Therefore its projection is a triangle. A base triangle avoiding \(01\) lifts to closed triangles, which cannot be vertex-simple three-edge paths. The remaining base triangles are \(012\) and \(013\). Their lifts are six-cycles because each traverses the single cross-sheet edge \(01\). For \(t\in\{2,3\}\), the three-edge segment
\[
(0,s),(1,s+1),(t,s+1),(0,s+1)
\]
has \(\chi\)-word \((s,s+1,s)\). Extending this segment around its six-cycle yields alternating edge labels throughout. Every rainbow three-edge path consequently has two \(\chi\)-changes.

Only three colors occur, so a rainbow path has at most three edges. Every two-edge path is rainbow and has at most one \(\chi\)-change. Hence the maximum allowable length is two. \(\square\)
