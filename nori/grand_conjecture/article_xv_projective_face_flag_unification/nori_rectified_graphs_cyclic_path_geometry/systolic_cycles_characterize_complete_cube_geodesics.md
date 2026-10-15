# Systolic cycles characterize complete cube geodesics

# Systolic cycles characterize complete cube geodesics

Let \(n\ge3\), \(H=L(Q_n)\) be the line graph of the cube, and \(\tau\) the induced antipodal involution on its vertices (original cube edges). The quotient \(Y=H/\tau\) is the one-skeleton of the antipodal quotient of the rectified cube. A closed walk of \(Y\) is essential when its lift to \(H\) starts at an edge \(e\) and ends at \(\tau e\).

**Theorem 1 (distance and equality characterization).** For every cube edge \(e\),
\[
\boxed{\operatorname{dist}_H(e,\tau e)=n.}
\]
Every shortest path in \(H\) from \(e\) to \(\tau e\) is the sequence of \(n\) undirected edges of a full antipodal geodesic of \(Q_n\), followed by the antipodal initial edge.

*Proof.* Let \(e\) have dimension \(i\). Two endpoints of \(e\) and \(\tau e\) have cube distance at least \(n-1\); equality holds when the endpoints agree in dimension \(i\). For any line-graph path \(e=e_0,e_1,\ldots,e_k=\tau e\), let \(v_j=e_{j-1}\cap e_j\) be its consecutive shared cube vertices. Each pair \(v_j,v_{j+1}\) either coincides or is connected by the cube edge \(e_j\). Thus the sequence \(v_1,\ldots,v_k\) contains a cube vertex walk of length at most \(k-1\) between an endpoint of \(e\) and an endpoint of \(\tau e\). Hence \(k\ge n\). A complete geodesic followed by the antipodal first edge gives length \(n\), so equality holds.

If \(k=n\), the intermediate shared vertices must move along an \((n-1)\)-edge shortest cube vertex path; none can coincide. This path uses every dimension other than \(i\) once. Its first vertex is one endpoint of \(e\), and its last vertex is the antipodal mate of the other endpoint of \(e\). Prepending \(e\) from that other endpoint therefore gives an \(n\)-edge full antipodal cube geodesic, and \(e_k=\tau e\) closes its line-graph path. \(\square\)

**Theorem 2 (systolic cycles).** The shortest essential closed walks in \(Y\) have length \(n\). Every such walk is a simple cycle and is the image of a full antipodal cube geodesic; conversely every full antipodal cube geodesic gives an essential cycle of length \(n\).

*Proof.* Every essential loop lifts to a line-graph path from \(e\) to \(\tau e\), so the preceding theorem bounds its length by \(n\). Equality gives a full geodesic. The first \(n\) cube edges use different dimensions, so their images in the quotient line graph are distinct and the projected walk is a simple cycle. \(\square\)

**Corollary 3 (the intrinsic one-crossing conjecture).** An antipodally odd NORI1 edge coloring corresponds, modulo global color complement, to a cellular one-cocycle \(a\) representing the nonzero class of the double cover \(\partial R(Q_n)\to\partial R(Q_n)/\tau\cong\mathbb RP^{n-1}\). The NORI1 conjecture is equivalent to:

> Every representative \(a\) of the nonzero covering class has a **shortest essential cycle** in the rectified quotient graph on which \(a\) is nonzero on only one edge.

*Proof.* The earlier line-graph representation identifies such cocycles with all antipodally odd cube-edge colorings. Their values on the essential cycle are consecutive original edge-color changes, together with one antipodally twisted closing comparison. The unique cochain crossing can be placed at the closing comparison by a root slide precisely when the corresponding full geodesic is monochromatic. \(\square\)

This description captures dimension-simplicity through intrinsic metric systolicity, rather than a separate matroid hypothesis. It does not yet transfer to the boundary-tournament Hamilton galleries: their paths in the Johnson graph of the rectified simplex are not generally shortest. The missing common structure may therefore involve a flag-sensitive notion of essential systolicity, not the ordinary graph metric alone.
