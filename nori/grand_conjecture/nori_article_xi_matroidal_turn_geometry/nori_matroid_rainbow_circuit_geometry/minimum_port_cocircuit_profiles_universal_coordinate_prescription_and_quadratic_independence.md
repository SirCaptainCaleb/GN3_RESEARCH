# Minimum port-cocircuit profiles, universal coordinate prescription, and quadratic independence

# Minimum port-cocircuit profiles and universal coordinate prescription

Let \(n\ge3\). Retain the pointed binary matroid \((D_n,p)\) with ground set \(E(H_n)\cup\{p\}\), where \(H_n=L(Q_n)/\langle\tau\rangle\), and write
\[
\mathcal Y_n=\{Y\in\mathcal C^*(D_n):p\in Y,\ |Y|=n+1\}.
\]
A minimum port cocircuit \(Y\) corresponds to the cyclic turn sequence \(C=Y\setminus\{p\}\) of a full antipodal cube geodesic, with all \(n\) directions occurring once. For a port-containing binary cycle \(X\) of \(D_n\), set \(d(t)=\mathbf1_{\{t\in X\}}\) for turns \(t\).

Choose an orientation of \(C\) and mark a seam following direction \(i_n\). Write \(i_1,\ldots,i_n\) for the successive directions, and \(t_r\) for the turn joining \(i_r\) to \(i_{r+1}\), cyclically. Define the compatible profiles of this marked cocircuit to be the solutions \(w\in\mathbb F_2^n\) of
\[
w_{i_r}+w_{i_{r+1}}=d(t_r)\quad(r<n),\qquad
w_{i_n}+w_{i_1}+1=d(t_n).
\tag{1}
\]
Since \(d(C)=1\), the system has two solutions, related by global complementation. Define \(\mathscr W(X)\) as the union of solutions from all \(Y\in\mathcal Y_n\), orientations and seams.

**Lemma (profile decoding).** The family \(\mathscr W(X)\) equals the family of direction-indexed full-geodesic edge-color vectors for either antipodally odd coloring reconstructed from \(X\). Moving the marked seam across its first direction \(i\) sends a profile \(w\) to \(w+e_i\). The deck involution sends \(w\) to \(w+\mathbf1\).

*Proof.* Lift the ordered turn cycle to cube edges \(e_1,\ldots,e_n,e_{n+1}=\tau e_1\). The first \(n-1\) equations in (1) assert that each incident-edge disagreement equals the turn label. At the closing turn the final edge is compared with the antipode of the initial edge, giving the additional one. The two solutions correspond to the antipodal choices of lifted root, and every geodesic has a marked turn cycle of this form. Rotating the initial direction to the end preserves the other edges and replaces the moved edge by its antipode, changing that profile coordinate by one. \(\square\)

Let \(B_k\) be the assertion that every arbitrary binary coloring of the undirected edges of \(Q_k\) has a spanning antipodal geodesic with at most one change. For \(n>k\) and a fixed set \(S\subseteq[n]\) of \(k\) directions, let \(P_{n,S}\) be
\[
\forall X\in Z(D_n),\ p\in X,\qquad
\{w|_S:w\in\mathscr W(X)\}=\mathbb F_2^S.
\tag{2}
\]

**Theorem (pointed-matroid multifacet bridge).** For every \(k\ge2\), \(n>k\), and \(S\subset[n]\) with \(|S|=k\),
\[
\boxed{B_k\Longleftrightarrow P_{n,S}.}
\tag{3}
\]

*Proof.* Suppose \(B_k\). Reconstruct from any \(X\) an antipodally odd cube coloring \(c\), and fix a desired vector \(t\in\mathbb F_2^S\). Write \(Q_n=Q_S\times Q_D\), with \(D=[n]\setminus S\ne\varnothing\), and fix an exterior vector \(z\). Define the edge coloring of the lower \(S\)-face by \(h_i(u)=c_i(u,z)+t_i\). By \(B_k\), choose an antipodal geodesic in this face with at most one change; reverse it if necessary so its color word is a zero block \(U\) followed by a one block \(V\). If it runs
\[
u_0\xrightarrow{U}u_a\xrightarrow{V}\bar u_0,
\]
begin a full \(Q_n\) geodesic at \((u_a,z)\), traverse \(U\) backwards to \((u_0,z)\), traverse all directions of \(D\), then traverse the reverse of the \(Q_S\)-antipodal image of \(V\) in the upper exterior face. The \(U\) edges have color \(t_i\); the \(V\) edges are global antipodes of the lower one-block edges and likewise have color \(t_i\). This full geodesic gives a profile in \(\mathscr W(X)\) restricting to \(t\).

Conversely suppose \(P_{n,S}\), and let \(h\) be any edge coloring of \(Q_S\). Choose exterior direction \(s\in D\) and a coordinate \(i_0\in S\). Define an antipodally odd coloring of \(Q_n\), using vertices \((u,z)\), by
\[
c_i(u,z)=
\begin{cases}h_i(u),&z_s=0,\\1+h_i(\bar u),&z_s=1,\end{cases}
\ (i\in S);\qquad c_j(u,z)=u_{i_0}\ (j\in D).
\tag{4}
\]
These formulas are invariant under flipping the coordinate of their traversed edge and are complemented by global antipodality. Obtain the associated port cycle \(X\). By \(P_{n,S}\), there is a full geodesic whose \(S\)-edges all have color zero. Reverse it so its unique \(s\)-step runs from \(z_s=0\) to \(z_s=1\). Let \(U,V\) be its \(S\)-direction subsequences before and after the \(s\)-step, ignoring all other exterior steps. The projected \(U\)-edges have \(h\)-color zero, while the \(Q_S\)-antipodal images of the projected \(V\)-edges have \(h\)-color one. Reversing \(U\) and following the reversal of the antipodal image of \(V\) gives a spanning \(Q_S\) geodesic with word \(0^{|U|}1^{|V|}\). Thus \(B_k\) holds. \(\square\)

**Corollary (seven-coordinate marginal universality).** Every port-containing binary cycle \(X\) of \(D_n\) satisfies
\[
\boxed{\{w|_S:w\in\mathscr W(X)\}=\mathbb F_2^S
\qquad\bigl(|S|\le\min(7,n)\bigr).}
\tag{5}
\]
For \(n\le8\), every vector of \(\mathbb F_2^n\) occurs as a profile.

*Proof.* The established geodesic Norin theorem through dimension eight, combined with the Leader–Long implication, gives \(B_k\) for every \(k\le7\). Apply (3). For \(n\le8\), independently toggle the cube-edge color of each coordinate direction according to a prescribed full profile; this preserves antipodal oddness. Apply the proved monochromatic geodesic theorem in that dimension, then undo the direction toggles. The remaining claims follow by projection. \(\square\)

The next theorem controls polynomial relations involving arbitrarily many directions. Its conclusion is independent of the bounded-coordinate marginal property (5).

**Theorem (quadratic independence).** For every port-containing cycle \(X\) and every multilinear polynomial
\[
q(w)=a_0+\sum_i b_iw_i+\sum_{i<j}a_{ij}w_iw_j
\quad\text{over }\mathbb F_2,
\tag{6}
\]
the identity \(q(w)=0\) for all \(w\in\mathscr W(X)\) forces every coefficient to vanish. Equivalently,
\[
\boxed{
\operatorname{span}_{\mathbb F_2}\{(1,(w_i)_i,(w_iw_j)_{i<j}):w\in\mathscr W(X)\}
=\mathbb F_2^{1+n+\binom n2}.}
\tag{7}
\]

*Proof.* Recover a cube-edge coloring \(c\) from \(X\), and suppose \(q\) vanishes. Extend \(a_{ij}=a_{ji}\) and put \(a_{ii}=0\). The root rotation in the profile lemma, applied to a geodesic whose first direction is \(i\), yields
\[
b_i+\sum_{j\ne i}a_{ij}w_j=0.
\tag{8}
\]
Fix either facet perpendicular to direction \(i\). Prepending an \(i\)-edge to any antipodal geodesic of that facet shows that the edge cochain \(\omega_j(x)=a_{ij}c_j(x)\), \(j\ne i\), has constant total sum \(b_i\) on all facet-spanning geodesics.

We use an elementary closed-integral lemma. If an undirected edge weighting of a cube has constant sum on all full antipodal geodesics, every square has weight sum zero, and antipodal edges within that cube have equal weights. Indeed, exchange two successive directions at the start of a geodesic to obtain square closure. Integrating a square-closed weighting gives a vertex potential \(\phi\). Its antipodal difference \(\phi(x)+\phi(\bar x)\) equals the constant geodesic integral. Taking derivatives along edges yields antipodal equality.

Complementing the root of the full geodesic in (8) complements every \(w_j\), so
\[
\sum_{j\ne i}a_{ij}=0.
\tag{9}
\]
Within an \(i\)-facet, its antipode is \(x\mapsto\bar x^i\). The closed-integral lemma and \(c_j(\bar x^i)=1+c_j(x^i)\) imply
\[
a_{ij}=1\ \Longrightarrow\ c_j(x)+c_j(x^i)=1.
\tag{10}
\]
Square closure of the same facet cochain gives, for distinct \(i,j,k\),
\[
a_{ij}\bigl(c_j(x)+c_j(x^k)\bigr)
=a_{ik}\bigl(c_k(x)+c_k(x^j)\bigr).
\tag{11}
\]

Form the graph on \([n]\) with edge \(ij\) when \(a_{ij}=1\). If \(ij,jk\) are edges, (10)--(11) force \(ik\) to be an edge. Its connected components are therefore cliques. Equation (9) implies every clique has odd order. Suppose some component \(B\) has an edge, choose \(j\in B\), and use (10) for \(k\in B\setminus\{j\}\) and (11) for \(k\notin B\). Together with undirectedness in direction \(j\), these coordinate derivatives give
\[
c_j(x)=\gamma_j+\sum_{k\in B\setminus\{j\}}x_k.
\tag{12}
\]
Since \(|B|\) is odd, the sum has an even number of coordinates and is invariant under global complementation, contradicting antipodal oddness of \(c_j\). Hence all \(a_{ij}=0\). Equation (8) forces every \(b_i=0\), and evaluation anywhere forces \(a_0=0\). This proves (7). \(\square\)

**Corollary (profile diversity).** Every port-containing cycle \(X\) satisfies
\[
\boxed{|\mathscr W(X)|\ge
\max\left\{2^{\min(n,7)},\
2\left\lceil\frac{1+n+\binom n2}{2}\right\rceil\right\}.}
\tag{13}
\]
For \(n\le8\) equality \(|\mathscr W(X)|=2^n\) holds.

*Proof.* The first bound follows from (5), and the second from the spanning vectors (7), noting that \(\mathscr W(X)\) is closed under complementation and therefore has even cardinality. The small-dimensional equality follows from the complete-profile conclusion of (5). \(\square\)

All profile information here is recovered from a binary port cycle paired with a *marked* minimum port cocircuit; the seam and antipodal choice retain the endpoint memory lost by taking an unmarked intersection size. The two theorems forbid, respectively, missing low-dimensional coordinate marginals and nonzero quadratic annihilators of the full marked-cocircuit family.
