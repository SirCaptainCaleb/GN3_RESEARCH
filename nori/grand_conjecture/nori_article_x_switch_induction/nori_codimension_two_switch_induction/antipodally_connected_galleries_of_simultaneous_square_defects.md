# Antipodally connected galleries of simultaneous square defects

### Antipodally connected galleries of simultaneous square defects

Let \(n\ge3\) be odd, and let \(c\) be a binary coloring of the undirected edges of \(Q_n\) satisfying \(c(\bar e)=1-c(e)\). Write \(c_i(x)\) for the color of the direction-\(i\) edge at \(x\), so that
\[
c_i(x^i)=c_i(x),\qquad c_i(\bar x)=1-c_i(x).
\]
For distinct \(i,j\), put \(d_{ij}(x)=c_i(x)+c_i(x^j)\) in \(\mathbb F_2\). This derivative depends only on the \((i,j)\)-square containing \(x\).

Let \(T\) be the restriction to \(\partial[0,1]^n\) of the Freudenthal triangulation of the cube. Its vertices are those of \(Q_n\); its maximal simplices are the chains in coordinate facets, each encoding a geodesic traversing the \(n-1\) free directions of that facet. Complementation \(\tau(x)=\bar x\) is a simplicial involution of \(T\).

Define vertex signs
\[
g_i(x)=(-1)^{\,c_i(x)+\sum_{j\ne i}x_j},\qquad i\in[n]. \tag{1}
\]
Since \(n-1\) is even,
\[
g_i(\bar x)=-g_i(x),\qquad g_i(x^i)=g_i(x),\qquad
g_i(x^j)=-g_i(x)\ \Longleftrightarrow\ d_{ij}(x)=0
\quad(j\ne i). \tag{2}
\]
Fix a nonempty \(I\subseteq[n]\). Call a simplex of \(T\) *\(I\)-mixed* when, for each \(i\in I\), both signs of \(g_i\) occur among its vertices. Define a graph \(\mathcal G_I\) whose vertices are the maximal \(I\)-mixed simplices of \(T\), with two joined when they share an \(I\)-mixed codimension-one face. The involution \(\tau\) acts on this graph.

**Theorem 1 (connected antipodal square-defect gallery).** For every \(I\subseteq[n]\) with \(1\le |I|\le n-2\), the graph \(\mathcal G_I\) has a connected component invariant under \(\tau\). Every simplex represented by a vertex of \(\mathcal G_I\) encodes a geodesic \(P\) in a coordinate facet such that for each \(i\in I\) some step of \(P\), in a direction \(j\ne i\), lies on an \((i,j)\)-square satisfying
\[
d_{ij}=0. \tag{3}
\]
The threshold \(n-2\) cannot be replaced by \(n-1\) for arbitrary antipodally odd edge colorings.

We first record the connectivity principle underlying the theorem.

**Lemma 2 (connected zero component).** Let \(S^d\) have a finite antipodally invariant triangulation, and let \(F:S^d\to\mathbb R^k\) be an odd piecewise-linear map, where \(1\le k\le d-1\). Then \(F^{-1}(0)\) has a connected component invariant under the antipodal involution.

*Proof.* Borsuk–Ulam makes \(Z=F^{-1}(0)\) nonempty. As the zero set of a map affine on finitely many simplices, \(Z\) is a finite polyhedron and has finitely many connected components. Suppose the involution exchanges the components in disjoint pairs. Assign the constants \(+1\) and \(-1\) to the two components in each pair. This defines a continuous odd map \(h:Z\to\{-1,1\}\). Extend \(h\) to a continuous real function \(h_0\) on \(S^d\), and replace the extension with \((h_0(x)-h_0(-x))/2\). The resulting function \(H\) is odd and agrees with \(h\) on \(Z\). The map
\[
x\longmapsto(F(x),H(x))\in\mathbb R^{k+1}
\]
is odd and nowhere zero: \(F\ne0\) off \(Z\), while \(H=\pm1\) on \(Z\). Since \(k+1\le d\), this contradicts Borsuk–Ulam. Thus some component of \(Z\) is invariant. \(\square\)

*Proof of Theorem 1.* Extend the vertex functions \(g_i\), \(i\in I\), affinely across the simplices of \(T\), obtaining \(F_I:|T|\to\mathbb R^{|I|}\). Equation (2) and antipodal invariance of \(T\) make \(F_I\) continuous and odd. Since \(|T|\cong S^{n-1}\) and \(|I|\le n-2\), Lemma 2 gives a connected \(\tau\)-invariant component \(Z_0\) of \(F_I^{-1}(0)\).

If \(z\in Z_0\) and \(\rho\) is the smallest simplex containing \(z\), then \(0=F_I(z)\) is a convex combination of the vectors \((g_i(v))_{i\in I}\) at vertices \(v\) of \(\rho\). Because each coordinate of each vertex vector is \(\pm1\), both signs occur on \(\rho\) for every \(i\in I\). Thus \(\rho\) and all its containing simplices are \(I\)-mixed.

Consider the maximal simplices meeting \(Z_0\). The finite closed cover of the connected space \(Z_0\) by their intersections with \(Z_0\) has connected intersection graph. Whenever two of these maximal simplices share a point \(z\in Z_0\), their common face contains the smallest simplex \(\rho\) containing \(z\). The maximal simplices containing \(\rho\) form a ridge-connected gallery in the triangulated sphere. Each intermediate ridge contains \(\rho\), hence is \(I\)-mixed. Therefore the maximal simplices meeting \(Z_0\) belong to one connected component of \(\mathcal G_I\). Their collection is invariant under \(\tau\), so that component is invariant as well.

For the path assertion, write the vertices of a maximal simplex as a chain \(v_0,\ldots,v_{n-1}\) with successive cube edges in the free directions of its facet. For each \(i\in I\), the signs \(g_i(v_s)\) cannot be constant. At some successive pair they differ. The traversed direction \(j\) differs from \(i\), since \(g_i\) is unchanged across direction-\(i\) edges. Equation (2) then gives \(d_{ij}=0\) on the square through that step. This proves (3).

To see sharpness, for \(1\le i<n\) define
\[
c_i(x)=x_{i+1}+\sum_{j\ne i}x_j\pmod2,
\]
and put \(c_n(x)=x_1\). Each function is independent of its own direction bit and is antipodally odd because \(n\) is odd. For \(I=[n-1]\), equation (1) yields \(g_i(x)=(-1)^{x_{i+1}}\). A maximal boundary simplex is \(I\)-mixed precisely when it lies in one of the two facets \(x_1=0\) or \(x_1=1\): in these facets its vertex chain traverses every direction \(2,\ldots,n\), whereas any other facet fixes some \(x_{i+1}\). The two families have no adjacency in \(\mathcal G_I\), and complementation exchanges them. Hence no connected component is invariant. \(\square\)

**Proposition 4 (one simultaneous facet chain at the next threshold).** For any \(I\subseteq[n]\) with \(|I|=n-1\), there exists a geodesic spanning a coordinate facet such that, for every \(i\in I\), one of its steps lies in a direction \(j\ne i\) on a square with \(d_{ij}=0\).

*Proof.* The vertex signs \(g_i\) of (1), for \(i\in I\), extend to the odd piecewise-linear map \(F_I:S^{n-1}\to\mathbb R^{n-1}\) used above. Borsuk–Ulam supplies a zero in some maximal simplex of \(T\). On the vertex chain of that simplex, each \(g_i\) takes both signs, so (2) provides the required step. The sharpness construction in Theorem 1 shows why existence here cannot be strengthened to a connected antipodally invariant mixed-ridge gallery. \(\square\)

**Corollary 3 (connected terminal-hole galleries under a four-switch obstruction).** Suppose \(n\ge5\) is odd and \(\mu(c)\ge4\). For \(i<j\), let \(H_{ij}\subseteq Q_{n-2}\) be the complement of the union of the projected terminal sets of spanning geodesics having at most two switches in the four codimension-two faces perpendicular to \(i,j\). For every \(I\subseteq[n]\) with \(|I|\le n-2\), there is a connected, antipodally invariant gallery of coordinate-facet geodesics such that every geodesic in the gallery, for each \(i\in I\), crosses some edge in direction \(j\ne i\) whose associated \((i,j)\)-square projects to a point of \(H_{ij}\).

*Proof.* Under \(\mu(c)\ge4\), every square with \(d_{ij}=0\) projects into \(H_{ij}\). Indeed, if its projection were the terminal of a spanning face geodesic with at most two switches, appending the exterior directions \(i,j\) in either order would produce a full geodesic with at most four switches. The evenness of \(\mu(c)\) forces the face path to have two switches and both full completions to have four, which in turn forces both derivatives of the terminal square to equal one, a contradiction. Apply Theorem 1. \(\square\)

The corollary supplies a connected antipodal carrier of simultaneously witnessed square defects. The witnesses are facet geodesics along which zero derivatives occur; their edge-color words may have arbitrarily many switches. An endpoint-coincidence conclusion would additionally require a theorem relating the connected defect gallery to the terminal sets of low-switch paths. Neither connectedness nor the zero-set theorem supplies that extraction.

#### Even-character simultaneous square witnesses

The preceding gallery construction extends to arbitrary even coordinate masks and to either parity of the cube dimension. Let \(n\ge3\), and let \(c_i(v)\) be the colors of an antipodally odd undirected-edge coloring of \(Q_n\). For \(i\ne j\), write \(d_{ij}(v)=c_i(v)+c_i(v^j)\) in \(\mathbb F_2\).

Fix an indexed family \(\mathcal A=((i_\alpha,S_\alpha))_{\alpha=1}^r\), where \(i_\alpha\in[n]\) and \(S_\alpha\subseteq[n]\setminus\{i_\alpha\}\) has even cardinality. Repeated directions are permitted. Call a facet chain \(P=(v_0,\ldots,v_{n-1})\) a witness for \(\mathcal A\) if, for each \(\alpha\), some step \(v_t\to v_{t+1}=v_t^{j}\), with \(j\ne i_\alpha\), satisfies
\[
d_{i_\alpha j}(v_t)\ne \mathbf1_{\{j\in S_\alpha\}}. \tag{4}
\]

**Theorem 5 (simultaneous even-character galleries).** If \(r\le n-1\), some facet chain witnesses \(\mathcal A\). If \(r\le n-2\), the graph of witnessing facet chains, adjacent when their simplices share a codimension-one face in the Freudenthal triangulation of \(\partial[0,1]^n\), contains a connected component invariant under complementation. The bound \(r\le n-2\) for invariant connectivity is sharp, in every dimension \(n\ge3\).

*Proof.* For each \(\alpha\), assign the sign
\[
g_\alpha(v)=(-1)^{\,c_{i_\alpha}(v)+
                       \sum_{j\in S_\alpha}v_j}. \tag{5}
\]
The exponent is modulo two. Since \(c_{i_\alpha}(\bar v)=1+c_{i_\alpha}(v)\) and \(|S_\alpha|\) is even, \(g_\alpha(\bar v)=-g_\alpha(v)\). Because \(i_\alpha\notin S_\alpha\), the sign is constant along direction-\(i_\alpha\) edges. Along a direction-\(j\) edge, its sign changes precisely when
\[
d_{i_\alpha j}(v)+\mathbf1_{\{j\in S_\alpha\}}=1, \tag{6}
\]
equivalently when (4) holds.

Affinely extend the \(r\) vertex signs to a map \(G:|\mathcal T|\to\mathbb R^r\) on the antipodally invariant Freudenthal triangulation \(\mathcal T\) of the cubical boundary. The map is continuous and odd. When \(r\le n-1\), Borsuk--Ulam gives \(z\in G^{-1}(0)\). Each coordinate of the vertex images is a sign. Thus every maximal simplex containing \(z\) has both signs in each coordinate. Its ordered vertex chain has a sign-changing step for each \(\alpha\), which witnesses (4) by (6).

When \(r\le n-2\), Lemma 2 (connected zero component) above gives an antipodally invariant connected component of \(G^{-1}(0)\). The star-and-ridge argument in the proof of Theorem 1 carries this component into a single connected component of witnessing maximal simplices, preserved by complementation. This proves the first two assertions.

For sharpness, set \(c_i(v)=v_{i+1}\) for \(i<n\), and \(c_n(v)=v_1\). This coloring is undirected-edge well defined and antipodally odd. Choose \(r=n-1\) and \((i_\alpha,S_\alpha)=(\alpha,\varnothing)\), \(\alpha=1,\ldots,n-1\). For every \(i<n\), the sole direction \(j\) in which \(d_{ij}=1\) is \(j=i+1\). A witnessing facet chain must therefore traverse every direction \(2,\ldots,n\), forcing its fixed direction to be \(1\). Witnessing chains occur in the two opposite facets \(v_1=0\) and \(v_1=1\). These facets are disjoint, so no adjacency component contains chains from both; complementation exchanges the two collections. Hence no component is invariant. \(\square\)

**Corollary 6 (simultaneous derivatives of both values).** Let \(n\ge5\) be odd and \(I\subseteq[n]\) satisfy \(2|I|\le n-2\). There is an antipodally invariant connected gallery of facet-spanning geodesics in which every geodesic, for each \(i\in I\), crosses both (possibly distinct) squares with
\[
d_{ij}=0\quad\text{and}\quad d_{ik}=1,
\qquad j,k\ne i. \tag{7}
\]
The two derivative witnesses may use different directions and positions.

*Proof.* For each \(i\in I\), insert the two constraints \((i,\varnothing)\) and \((i,[n]\setminus\{i\})\) into \(\mathcal A\). Both masks have even size because \(n\) is odd. Equation (4) for the empty mask forces derivative one, while (4) for the full exterior mask forces derivative zero. Apply Theorem 5 with \(r=2|I|\). \(\square\)

These simultaneous witnesses hold without restrictions on the dependence of individual edge colors. They refine the square-defect carrier theorem by including both derivative signs and repeated coordinate constraints. The gallery certifies square crossings; a low-switch geodesic still requires an additional extraction argument.
