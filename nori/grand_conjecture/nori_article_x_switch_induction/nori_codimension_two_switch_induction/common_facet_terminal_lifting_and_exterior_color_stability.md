# Common-facet terminal lifting and exterior color stability

# Common-facet terminal lifting and exterior color stability

Let \(d,e:E(Q_m)\to\{0,1\}\) be arbitrary undirected-edge colorings. For a face \(H\) of \(Q_m\), write \(E_r^H(d)\) for the vertices of \(H\) that terminate a geodesic spanning \(H\) with at most \(r\) changes in its \(d\)-edge-color word. The set \(E_r(d)\) denotes the corresponding terminals of geodesics spanning the whole cube. If \(S\subseteq[m]\), write \(x^S\) for the vertex obtained by flipping each coordinate of \(S\).

**Lemma 1 (common-subface lifting).** Let \(H\) be a codimension-\(r\) face of \(Q_m\), with fixed-coordinate set \(S\), and let \(a,b\ge0\). Then
\[
\boxed{\bigl(E_a^H(d)\cap E_b^H(e)\bigr)^S
 \subseteq E_{a+r}(d)\cap E_{b+r}(e).}\tag{1}
\]
No conditions are imposed on any edge outside \(H\). The same assertion holds simultaneously for any number of edge colorings, with separately specified switch budgets.

*Proof.* Fix \(x\in E_a^H(d)\cap E_b^H(e)\). Choose spanning geodesics \(P_d,P_e\subseteq H\) ending at \(x\) with at most \(a,b\) changes, respectively. From \(x\), traverse the directions of \(S\) in an arbitrary common order, producing a path \(R\) with \(r\) edges from \(x\) to \(x^S\). Concatenating \(P_dR\) and \(P_eR\) yields two geodesics of \(Q_m\): the paths inside \(H\) traverse every direction outside \(S\) once, and the appended paths traverse precisely the remaining directions. Their final vertex is the same \(x^S\). Appending \(r\) edges introduces at most \(r\) additional adjacent color comparisons, independently for each coloring. This proves (1). For \(r=0\), the inclusion is the identity. The argument is identical for further colorings. \(\square\)

**Theorem 2 (one common block-radial facet).** Suppose \(m\ge2\) and there exist a direction \(p\in[m]\) and a bit \(\eta\in\{0,1\}\) such that, under identification of the facet \(H=\{x:x_p=\eta\}\) with \(Q_{m-1}\), both restrictions \(d|_H,e|_H\) are shifted block-radial edge colorings. Explicitly, for each coloring independently, partition \(D=[m]\setminus\{p\}\) into blocks, choose a shift \(t\in\{0,1\}^D\), and assign an arbitrary binary function \(h_B\) on \(\{0,\ldots,|B|-1\}\) to every block. Its edge colors within \(H\) have the form
\[
d_i(x)=h_{B(i)}\left(\sum_{j\in B(i)\setminus\{i\}}(x_j\oplus t_j)\right)
\qquad(i\in D,\ x\in H),\tag{2}
\]
and analogously for \(e\), with independent data. Then
\[
\boxed{E_2(d)\cap E_2(e)\ne\varnothing.}\tag{3}
\]
The coloring of **every** edge outside \(H\), including all edges in the opposite facet and all edges in direction \(p\), may be prescribed independently and arbitrarily for \(d\) and \(e\).

*Proof.* The simultaneous one-switch terminal theorem for two shifted block-radial colorings, proved above in this Article, applies to the restrictions on \(H\). It yields
\[
E_1^H(d)\cap E_1^H(e)\ne\varnothing.
\]
Apply Lemma 1 with \(S=\{p\}\) and \(a=b=1\). The proof consults the colors outside \(H\) only to count at most one extra change on the appended edge. \(\square\)

**Corollary 3 (several unrestricted exterior coordinates).** Let \(S\subseteq[m]\) have cardinality \(r\) and let \(H\) be any corresponding codimension-\(r\) face with \(m-r\ge1\). If \(d|_H\) and \(e|_H\) are independently shifted block-radial, then
\[
\boxed{E_{r+1}(d)\cap E_{r+1}(e)\ne\varnothing.}\tag{4}
\]
Consequently, for \(r=1\) the common-terminal two-switch assertion survives arbitrary and independent recoloring of all edges outside one common facet, a class wider than perturbations confined to one edge direction.

*Proof.* Apply the simultaneous one-switch theorem on \(H\) and then Lemma 1 with \(a=b=1\). \(\square\)

**Corollary 4 (NORI1 completion from matched codimension-three subfaces).** Let \(n=m+2\ge4\), and let \(c\) color the undirected edges of \(Q_n\) subject to \(c(\bar f)=1-c(f)\) for every edge \(f\). Fix adjacent parallel codimension-two faces \(F,F^a\) with common free directions \(D\) of size \(m\). Suppose that for some \(p\in D\), the restrictions of \(c\) to the two corresponding codimension-three faces obtained by fixing \(p=\eta\) in \(F\) and \(F^a\) are shifted block-radial under their common free-coordinate identification. Then
\[
\boxed{\mu(c)\le2.}\tag{5}
\]

*Proof.* Identify \(F,F^a\) with \(Q_m\), giving unrestricted colorings \(d,e\). Theorem 2 supplies geodesics spanning \(F,F^a\), each with at most two changes and terminating at corresponding vertices. The parallel-face switch bound of Article VIII yields \(\mu(c)\le2\). The antipodal relation on \(c\) is used in the final gluing theorem; no antipodal condition is required in the two subfaces. \(\square\)

The statements are conditional on one common face of controlled structure. In particular, no claim that an arbitrary pair \(d,e\) has such a face is needed.
