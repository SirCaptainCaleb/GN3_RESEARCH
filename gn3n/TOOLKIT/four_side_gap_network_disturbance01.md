# Four-label gap networks force a mixed four-set, an outer-edge reversal, or a spaced middle configuration

**Summary:** A complete four-label gap network either gives a mixed Hamiltonian four-set, reverses an outer edge of the four-path, or has gap order g0<=g2-3<g2<g1=g2+1<g3 with g3>=g1+3 and doubled reversal across the middle edge; in the last case the host path has order at least 11.

## Statement

Let H be a minimum counterexample and let X=(x_0,x_1,x_2,x_3) be a Hamiltonian four-path in a spanning three-cover X|P|Q, where P=(p_1,...,p_m), m>=7, and M=(p_2,...,p_{m-1}). Suppose each x_i has a distinct second-type failed-insertion obstruction gap g_i in M and the complete gap-network connectors of four_side_endpoint_lock_gap_network01 are present. Then at least one of the following holds. (1) H contains a proper Hamiltonian four-set meeting both X and V(M), whose complement is non-Hamiltonian with path-cover number two. (2) A tight triple reverses one of the two outer displayed edges x_0x_1 or x_2x_3 of X. (3) For some gap index t, g_2=t, g_1=t+1, g_0<=t-3, and g_3>=t+4; if z is the unique M-vertex in the connector from x_2 to x_1, then both (z,x_2,x_1) and (x_2,x_1,z) are tight. In (3), m>=11. Consequently every hard gap-network configuration on a host path of order at most ten gives (1) or (2).

## Body

Write the four assigned obstruction gaps as
\[
g_i=g(x_i),\qquad 0\le i\le3.
\]
The complete gap-network hypothesis gives, for every pair of labels, either the adjacent-gap cross triple or the tight interval connector through the displayed subinterval of \(M\).

We first record the path-intersection consequence. Suppose \(i<j\) and
\[
g_j<g_i.
\]
Let \(C\) be the gap-network connector from \(x_j\) to \(x_i\), and let
\[
A=(x_i,\ldots,x_j)
\]
be the displayed \(X\)-subpath. Their only common vertices are \(x_i,x_j\), and these occur in opposite relative orders. The reversed-common-vertices lemma from the path-intersection calculus therefore gives either a tight triple reversing a boundary edge of \(A\), or a vertex-simple tight cycle on \(V(A)\cup V(C)\).

The cycle alternative yields conclusion (1). Indeed the cycle meets both \(X\) and \(M\). If it has at least four vertices, four consecutive vertices across a junction between its \(X\)-portion and its \(M\)-portion form a mixed Hamiltonian four-set. If it has three vertices, then \(A\) is a single displayed edge of \(X\). The cyclic triples place the unique \(M\)-vertex on both sides of that ordered edge, and one of the two displayed neighbors of the edge in the four-path \(X\) extends one of these triples to a mixed Hamiltonian four-path. In either case the resulting four-set is proper; minimum-counterexample calculus gives a non-Hamiltonian path-cover-two complement.

Thus, unless (1) holds, every inversion \(g_j<g_i\) forces a tight triple reversing one of the two boundary edges of the displayed subpath \(A\).

Assume henceforth that neither (1) nor (2) holds. Then
\[
g_0<g_1
\]
because an inversion of the adjacent pair \(x_0,x_1\) would reverse the outer edge \(x_0x_1\). Similarly
\[
g_2<g_3.
\]
The four gaps cannot occur in increasing order. To see this, suppose
\[
g_0<g_1<g_2<g_3.
\]
The second-type prefix for \(x_1\) contains
\[
(b_{g_1-1},b_{g_1},x_1).
\]
If \((b_{g_1},x_1,x_2)\) were tight, these vertices would contain a mixed Hamiltonian four-path; otherwise boundary reversal gives
\[
(x_2,x_1,b_{g_1})
\]
tight. Symmetrically, using the second-type suffix for \(x_2\), absence of a mixed Hamiltonian four-path gives
\[
(b_{g_2+1},x_2,x_1)
\]
tight. The latter two triples concatenate to a mixed Hamiltonian four-path, a contradiction. Hence
\[
g_1>g_2.
\]

Consider the connector
\[
C=(x_2,c_1,\ldots,c_k,x_1)
\]
supplied by the gap network. We claim that \(k=1\). The two junction triples with the displayed middle edge of \(X\) are
\[
(x_1,x_2,c_1),\qquad (c_k,x_1,x_2).
\]
If \(k\ge2\) and the first junction is tight, then
\[
(x_1,x_2,c_1,c_2)
\]
is a mixed Hamiltonian four-path. If the second junction is tight, then
\[
(c_{k-1},c_k,x_1,x_2)
\]
is such a path. If both junctions are non-tight, boundary reversal gives
\[
(c_1,x_2,x_1),\qquad(x_2,x_1,c_k)
\]
tight, and since \(c_1\ne c_k\),
\[
(c_1,x_2,x_1,c_k)
\]
is a mixed Hamiltonian four-path. All three possibilities contradict the exclusion of (1). Therefore \(k=1\).

Write the unique internal connector vertex as \(z\). If
\[
(x_1,x_2,z)
\]
were tight, then \((x_0,x_1,x_2,z)\) would be a mixed Hamiltonian four-path. Hence
\[
(z,x_2,x_1)
\]
is tight. Similarly, tightness of \((z,x_1,x_2)\) would make
\[
(z,x_1,x_2,x_3)
\]
a mixed Hamiltonian four-path, so
\[
(x_2,x_1,z)
\]
is tight. Thus the middle edge has reverse triples on both sides through the same vertex \(z\).

By the connector dichotomy in the gap-network theorem, a connector with exactly one internal vertex corresponds to adjacent obstruction gaps. Hence, for some integer \(t\),
\[
g_2=t,\qquad g_1=t+1.
\]
Since \(g_0<g_1\), distinctness of the gaps implies \(g_0<g_2\). Since \(g_2<g_3\), distinctness likewise implies \(g_1<g_3\).

Now apply the short-gap reversal theorem to the displayed tight triple
\[
(x_0,x_1,x_2).
\]
Because \(g_0<g_2\), its two endpoint gaps differ by at least three:
\[
g_2-g_0\ge3.
\]
Apply the same theorem to
\[
(x_1,x_2,x_3).
\]
Because \(g_1<g_3\),
\[
g_3-g_1\ge3.
\]
Consequently
\[
g_0\le t-3,qquad
g_2=t,qquad
g_1=t+1,qquad
g_3\ge t+4.
\]
This is conclusion (3).

Finally the displayed gaps of \(M=(p_2,\ldots,p_{m-1})\) are indexed by
\[
1,\ldots,m-3.
\]
Conclusion (3) gives \(g_3-g_0\ge7\), hence \(g_3\ge8\) and therefore
\[
m-3\ge8,
\qquad
m\ge11.
\]
Thus for \(m\le10\), only conclusions (1) and (2) are possible.

## Metadata

- ID: four_side_gap_network_disturbance01
- Kind: toolkit
- Version: 3
- Math version: 3
- Audit: unaudited
- Refutation: unrefuted
- Toolkit status: Limbo
