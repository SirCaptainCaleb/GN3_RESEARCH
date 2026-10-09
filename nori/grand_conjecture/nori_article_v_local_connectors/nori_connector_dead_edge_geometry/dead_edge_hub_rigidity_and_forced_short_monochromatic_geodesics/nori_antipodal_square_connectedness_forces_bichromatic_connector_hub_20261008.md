# Every NORI coloring has a vertex with monochromatic four-edge connectors of both colors

# A discrete equivariant connector lemma forces both monochromatic colors at one physical center

Let \(n\ge5\), and let \(c\) be an active NORI ordered-three-face coloring: \(c(\bar F,\operatorname{rev}\pi)=1\oplus c(F,\pi)\). For a physical cube vertex \(z\), define the **centered monochromatic-connector color set**
\[
\mathcal C(z)=\{q\in\{0,1\}:\ \exists\text{ a genuine centered four-edge geodesic }P_z(a,b,c,d)
\text{ whose two ordered-three-face window colors both equal }q\}.
\tag{1}
\]
The color set is **nonempty at every vertex** by the centered five-direction odd-pentagon theorem. A connector with middle pair \(\{b,c\}\) certifies the same two ordered physical window faces with center at any of the four vertices of the square \(Q(z;b,c)\); hence its color \(q\) belongs to \(\mathcal C\) at all four vertices.

**Theorem (unavoidable bichromatic connector hub).** In every active NORI coloring of \(Q_n\), \(n\ge5\), there exists a physical cube vertex \(z\) such that
\[
\boxed{\mathcal C(z)=\{0,1\}.}
\tag{2}
\]
In other words, **two genuine monochromatic four-edge geodesics of opposite colors have the very same center vertex**, although their free direction orders need not be compatible. In fact \(\bar z\) is also such a hub; thus the set of bichromatic hubs is nonempty and antipodally invariant, and contains at least two vertices.

**Proof.** The proved connected-certified-square theorem, Item \`nori_certified_square_complex_connected_antipodal_one_class_20261008\`, states that the graph \(G_c\) whose edges belong to genuinely certified monochromatic center squares is connected. Every edge \(z\leftrightarrow z'\) of \(G_c\) lies in a certified square and therefore has **one physical monochromatic connector certificate** of some color \(q\) at **both** endpoints. Thus
\[
\mathcal C(z)\cap\mathcal C(z')\ne\varnothing
\quad\text{for every }zz'\in E(G_c).
\tag{3}
\]
Suppose no vertex had both colors. Since all sets \(\mathcal C(z)\) are nonempty, each would be a singleton \(\{q_z\}\). Relation (3) would imply \(q_z=q_{z'}\) along every certified edge. Connectedness would force \(q_z=q\) constant throughout the cube.

On the other hand antipodal reversal maps any monochromatic centered four-edge path with center \(z\) and color \(q\) to a genuine centered monochromatic path with center \(\bar z\) and color \(1\oplus q\). Thus
\[
\mathcal C(\bar z)=\{1\oplus q:q\in\mathcal C(z)\}.
\tag{4}
\]
A globally constant singleton label cannot satisfy (4), contradiction. Hence some \(z\) has \(\mathcal C(z)=\{0,1\}\). By (4) the antipode \(\bar z\) also has both colors. \(\square\)

**General discrete fixed-point principle behind the proof.** If a **connected** finite graph carries a free involution \(\tau\), and every vertex \(v\) carries a nonempty subset \(S(v)\subseteq\{0,1\}\) with \(S(\tau v)=1-S(v)\) and \(S(v)\cap S(w)\ne\varnothing\) on every graph edge, then some vertex has the full label set \(\{0,1\}\). Otherwise the singleton labels define a continuous equivariant map from the connected graph to the disconnected space \(S^0\), impossible. This is the one-dimensional set-valued topological coincidence principle made concrete by genuine NORI witness sheets.

**Exact scope.** The theorem forces a *single physical center* shared by opposite-color monochromatic **four-edge connectors**, an all-dimensional and physically witnessed form of color-free topological overlap. It is **not yet** an antipodal full-geodesic theorem: the two connector direction supports can overlap arbitrarily, their roots may differ, and their terminal memories need not form complementary reversed-tail supports. A successful higher-dimensional Tucker/Sperner/Hex theorem must strengthen this color coincidence to a compatible **coordinate-support** coincidence within the exact reachability families \(R_J(x)\), or yield a nonbipartite four-facet cap-memory graph. Nevertheless the result shows the certified square complex carries an actionable **set-valued** antipodal intersection principle, not merely an abstract nonzero cohomology class.
