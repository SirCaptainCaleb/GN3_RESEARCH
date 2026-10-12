# Antipodal facet-exchange chains through simultaneous square defects

### Simultaneous square defects and antipodal facet exchanges

Let \(n\ge5\) be odd. Color the undirected edges of \(Q_n=\{0,1\}^n\) by bits \(c_i(x)\), where \(c_i(x)\) denotes the edge incident with \(x\) in direction \(i\), and assume
\[
c_i(x^i)=c_i(x),\qquad c_i(\bar x)=1+c_i(x).
\tag{1}
\]
Arithmetic of colors is in \(\mathbb F_2\). For \(i\ne j\), put
\[
d_{ij}(x)=c_i(x)+c_i(x^j).
\tag{2}
\]
This depends only on the \((i,j)\)-square containing \(x\).

Triangulate each facet of the geometric cube \([0,1]^n\) by its Freudenthal (monotone-chain) simplices, consistently on intersecting facets. The resulting complex \(\mathcal T\) triangulates \(\partial[0,1]^n\cong S^{n-1}\). Its maximal simplices have as vertices the \(n\) successive corners of a geodesic traversing every free direction of one coordinate facet, starting with all its free bits zero. Call these *facet chains*. Two facet chains are adjacent if their maximal simplices share a codimension-one simplex, equivalently if their sets of \(n\) vertices share \(n-1\) vertices. Cube complementation sends each facet chain, with its order reversed, to another facet chain.

For a nonempty \(I\subseteq[n]\), call a facet chain \(P=(v_0,\ldots,v_{n-1})\) **\(I\)-defect-complete** when, for every \(i\in I\), there is a step \(v_t\to v_{t+1}=v_t^j\) with \(j\ne i\) and
\[
d_{ij}(v_t)=0.
\tag{3}
\]
Let \(\Gamma_I\) be the graph induced by these chains under the preceding adjacency.

**Theorem 1 (simultaneous defect carriers).** For every nonempty \(I\subseteq[n]\) with \(|I|\le n-1\), the graph \(\Gamma_I\) has a vertex. If
\[
1\le |I|\le n-2,
\tag{4}
\]
then \(\Gamma_I\) has a connected component preserved by cube complementation. In particular, there is a sequence
\[
P_0,P_1,\ldots,P_s=\bar P_0
\tag{5}
\]
of \(I\)-defect-complete facet chains such that successive chains share \(n-1\) vertices. All conclusions hold for arbitrary colorings satisfying (1).

*Proof.* For \(i\in[n]\) define at each cube vertex
\[
a_i(x)=(-1)^{\,c_i(x)+\sum_{h\ne i}x_h}.
\tag{6}
\]
Since \(n-1\) is even, (1) gives \(a_i(\bar x)=-a_i(x)\). Moreover, \(a_i(x^i)=a_i(x)\), whereas for \(j\ne i\),
\[
a_i(x^j)=-a_i(x)\quad\Longleftrightarrow\quad d_{ij}(x)=0.
\tag{7}
\]
For \(I=\{i_1,\ldots,i_r\}\), assign the vector
\(a_I(x)=(a_{i_1}(x),\ldots,a_{i_r}(x))\in\{-1,1\}^r\)
to the vertices of \(\mathcal T\), and extend affinely over every simplex. This defines a continuous map
\[
A_I:|\mathcal T|\longrightarrow\mathbb R^r,\qquad
A_I(\bar z)=-A_I(z),
\tag{8}
\]
because the Freudenthal triangulation of the cubical boundary is preserved by complementation.

When \(r\le n-1\), Borsuk–Ulam applied to
\(|\mathcal T|\cong S^{n-1}\) gives \(z\) with \(A_I(z)=0\). Choose a maximal simplex \(\sigma\) containing \(z\), and let \(P\) be its facet chain. The zero vector is a convex combination of the vectors \(a_I(v)\) at vertices of \(P\). For each \(i\in I\), both signs therefore occur among the \(a_i\)-values along \(P\). Some consecutive vertices of \(P\) have opposite \(a_i\)-values; equation (7) shows that this step has direction \(j\ne i\) and satisfies (3). Thus \(P\) belongs to \(\Gamma_I\).

Assume next that \(r\le n-2\), and let \(Z=A_I^{-1}(0)\). It is a nonempty finite polyhedron with finitely many connected components, preserved as a collection by complementation. We show that some component \(W\) satisfies \(\bar W=W\). Otherwise, the components can be divided into two disjoint closed unions \(Z_+\), \(Z_-\) interchanged by complementation. With distance measured in the ambient Euclidean space, define
\[
g(z)=\operatorname{dist}(z,Z_-)-\operatorname{dist}(z,Z_+)
\quad(z\in|\mathcal T|).
\tag{9}
\]
Then \(g\) is continuous and odd, and \(g\ne0\) on \(Z\). The map \((A_I,g):S^{n-1}\to\mathbb R^{r+1}\) is consequently odd and nowhere zero, contrary to Borsuk–Ulam because \(r+1\le n-1\). This proves the existence of \(W\).

Let \(\mathcal D\) be the graph of maximal simplices meeting \(Z\), joined across codimension-one faces. All such simplices give \(I\)-defect-complete chains by the first part of the proof. The maximal simplices containing any one point \(z\in Z\) are ridge-connected: they constitute the maximal simplices of the star of the minimal face supporting \(z\), whose link in the triangulated sphere is connected in its facet-adjacency graph. Consequently two components of \(\mathcal D\) cannot have closed unions meeting at a point of \(Z\). The connected set \(W\) therefore meets maximal simplices in a single component \(D\) of \(\mathcal D\). Since \(\bar W=W\), this component is preserved by complementation. It lies in \(\Gamma_I\); the component of \(\Gamma_I\) containing \(D\) is also preserved by complementation. Choosing any chain in it and connecting it by graph edges to its complement proves (5). \(\square\)

For each \(i<j\), project the four codimension-two faces with fixed directions \(i,j\) onto the common \(Q_{n-2}\), and let \(H_{ij}\) be the complement of the union of the projected terminals of their spanning geodesics with at most two color changes.

**Corollary 2 (simultaneous terminal-hole exchanges).** Suppose \(\mu(c)\ge4\). For any \(I\subseteq[n]\), \(|I|\le n-1\), there exists a facet chain \(P\) such that for every \(i\in I\), one of its steps in a direction \(j\ne i\) lies on an \((i,j)\)-square whose projection belongs to \(H_{\min(i,j),\max(i,j)}\). For \(1\le |I|\le n-2\), the graph of facet chains with this property has a complementation-invariant connected component, and consequently contains an antipodal exchange sequence as in (5).

*Proof.* The terminal-hole theorem for odd-dimensional cubes gives
\[
d_{ij}(x)=0\quad\Longrightarrow\quad
x|_{[n]\setminus\{i,j\}}\in H_{\min(i,j),\max(i,j)}
\tag{10}
\]
under \(\mu(c)\ge4\): a square with \(d_{ij}=0\) cannot have both cross-derivatives equal to one. Each step certified by (3) therefore certifies the required terminal hole. The asserted graph contains \(\Gamma_I\), is preserved by complementation, and consequently has an invariant connected component whenever \(\Gamma_I\) does. \(\square\)

The conclusion couples terminal holes for as many as \(n-1\) selected directions along one facet chain, and for \(n-2\) directions along an antipodally connected exchange family. A terminal-hole certificate specifies an excluded endpoint of a short face geodesic; it does not provide a short geodesic through that point. In particular, the theorem supplies a global connectivity constraint on the holes of a hypothetical four-switch coloring, while the corresponding-low-switch-terminal intersection required for the Article X induction remains open.
