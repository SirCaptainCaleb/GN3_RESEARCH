# Spectral rigidity for partition matroids

Let \(M\) be a finite matroid obtained as a direct sum of nontrivial uniform matroids
\[
M=\bigoplus_{j=1}^{t}U_{r_j,m_j},\qquad 1\le r_j<m_j,
\]
and let \(G=\Gamma(M)\) be its basis-exchange graph. Thus
\[
G=\mathop{\square}_{j=1}^{t}J(m_j,r_j),\qquad
d=\deg(G)=\sum_{j=1}^{t}r_j(m_j-r_j).
\]
Let \(A_G\) be its adjacency matrix, \(P_2\) the orthogonal projection onto the eigenspace \(W_2\) of its second largest distinct adjacency eigenvalue, and \(N_{\rm sp}(G)\) the linear matroid on graph edges \(uv\) represented by \(P_2({\bf e}_u-{\bf e}_v)\).

**Theorem (spectral-star rigidity).** The following are equivalent:

(i) The edge vectors in every vertex star of \(G\) are independent in \(N_{\rm sp}(G)\).

(ii) There is an integer \(q\ge2\) such that every summand has \(m_j=q\) and \(r_j\in\{1,q-1\}\).

(iii) \(G\cong H(t,q)=K_q^{\square t}\) for some \(q\ge2\).

Under these conditions,
\[
\dim W_2=d=t(q-1),\qquad
\operatorname{rk}N_{\rm sp}(G)=d;
\]
each vertex star is a basis of \(N_{\rm sp}(G)\), and \(N_{\rm sp}(G)\) has minimum possible rank among matroids on \(E(G)\) in which all vertex stars are independent.

*Proof.* The adjacency spectrum of a Johnson graph \(J(m,r)\), for \(1\le r<m\), consists of the distinct eigenvalues
\[
\theta_\ell=(r-\ell)(m-r-\ell)-\ell,\qquad 0\le\ell\le\min(r,m-r),
\]
with the second one \(\theta_1=r(m-r)-m\) of multiplicity \(m-1\). Thus its spectral gap between the largest and second-largest adjacency eigenvalues is \(m\).

The adjacency operator of a Cartesian product is the sum of the lifted factor adjacency operators. Put \(m_*=\min_jm_j\). The second-largest eigenvalue of \(G\) is therefore \(d-m_*\), and its multiplicity is
\[
D=\dim W_2=\sum_{\{j:m_j=m_*\}}(m_j-1).\tag{1}
\]
For every \(j\),
\[
r_j(m_j-r_j)\ge m_j-1,\tag{2}
\]
with equality if and only if \(r_j=1\) or \(r_j=m_j-1\). As each summand is nontrivial, (1)--(2) give \(d\ge D\), and equality holds if and only if all \(m_j=m_*\) and each rank is \(1\) or \(m_*-1\). Since the \(d\) incident edge vectors at a vertex lie in the \(D\)-dimensional space \(W_2\), condition (i) requires \(d\le D\). Hence (i) implies (ii).

Under (ii), every Johnson factor is \(J(q,1)\cong J(q,q-1)\cong K_q\), proving (iii). Conversely, every Johnson graph \(J(m,r)\), \(1\le r<m\), has triangle-connected edge set (the graph whose vertices are its edges and whose adjacencies join two edges belonging to one triangle is connected), unless it consists of a single edge. Indeed, two exchanges at the same basis are joined by a sequence of triangle moves that alternately hold the entering or departing element fixed; the line graph of the complete bipartite fundamental exchange graph \(K_{r,m-r}\) is connected. Connectedness of \(J(m,r)\) then joins the triangle chains across bases. In a Cartesian product, the edges of every triangle lie in one factor, so a triangle-connected Johnson factor cannot split across distinct Cartesian factors. Therefore if (iii) holds, each Johnson factor is one complete factor \(K_q\), and hence \(r_j\in\{1,m_j-1\}\) and \(m_j=q\).

To prove (iii) implies (i), identify the second eigenspace of \(H(t,q)\) with \(\bigoplus_{j=1}^t{\bf1}^{\perp}\subseteq(\mathbb R^q)^t\). The projected difference vector for an edge changing symbol \(a\) to \(b\) in factor \(j\) is, up to a common nonzero scalar, \({\bf e}_b-{\bf e}_a\) in the \(j\)-th summand and zero elsewhere. At any vertex, the \(q-1\) incident vectors in factor \(j\) form a basis of that summand. All incident vectors are therefore a basis of \(W_2\). Connectedness ensures that the projected differences of graph edges span all of \(W_2\), because edge differences span the coordinate hyperplane perpendicular to the all-ones vector, which contains \(W_2\). Hence the edge-column matroid has rank \(d\).

Finally, any matroid on \(E(G)\) with an independent vertex star has rank at least \(d\). The spectral resource matroid attains this lower bound. \(\square\)

**Corollary (intrinsic minimal resource geometry of the canonical roots).** For \(Q_n=H(n,2)\), the minimal-rank spectral resource matroid is the partition matroid on coordinate-direction edge classes, of rank \(n\). For \(K_n=H(1,n)\), it is the graphic matroid \(M(K_n)\), of rank \(n-1\). In both cases, every vertex star is a resource basis. These are two specializations of the same automorphism-invariant spectral projection, with the resource rank equal to the graph degree.

**Scope.** The theorem classifies the spectral-star condition *within partition-matroid basis graphs*. It does not classify all matroid basis graphs satisfying that condition. Its two extremal cases are the root graphs naturally associated with the NORI1 cube and the boundary 3-tournament Johnson basis graph, respectively: the boundary root is \(K_n\), recovered as the line-graph root of \(J(n,2)\) for \(n\ge4\). It provides a structural class and a minimum-rank resource representation but does not force full-rank positively oriented paths.

**Corollary (functorial polarization threshold).** Let \(X=V(H(t,q))\) with the natural action of \(\operatorname{Aut}(H(t,q))=S_q\wr S_t\). If \(q\ge3\), every equivariant self-map \(X\to X\) is the identity. If \(q=2\), the equivariant self-maps are the identity and simultaneous coordinate complementation.

*Proof.* The automorphism group acts transitively. An equivariant map is determined by the image of the all-zero vertex, which must be fixed by its stabilizer. For \(q\ge3\), the stabilizer contains an independent \(S_{q-1}\) permutation group on the unused alphabet symbols in every factor, and therefore fixes only the all-zero vertex. For \(q=2\), the stabilizer permutes the \(t\) factors and fixes the two constant binary words; the two resulting equivariant maps are identity and complementation. \(\square\)

Thus the canonical fixed-point-free antipode of \(Q_t\) disappears immediately upon passing to the next homogeneous Hamming interpolation \(H(t,3)\). Any formulation encompassing arbitrary complete-graph roots must locate its reversal structure on oriented exchange flags or another derived carrier.
