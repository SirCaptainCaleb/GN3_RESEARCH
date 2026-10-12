# Folded-cube line graphs and local generation of binary dependencies

# Direction-deleted graphic restrictions and a binary contraction normal form

Let \(n\ge3\), and let \(G_n=Q_n/\langle\tau\rangle\) be the folded cube under antipodal complementation. Put \(H_n=L(G_n)\), with \(V_i\subseteq V(H_n)\) the vertices corresponding to cube-edge pairs of direction \(i\). Let \(M_n\) be the binary matroid on \(E(H_n)\) represented by the vertex-edge incidence matrix \(B\) of \(H_n\), augmented by a row \(a\) recording the monodromy of the cover \(L(Q_n)\to H_n\). In particular, the cycles of \(M_n\) are the even-degree subgraphs of \(H_n\) having zero covering monodromy.

Fix a direction \(s\), set \(U_s=V(H_n)\setminus V_s\), and write \(m=2^{n-2}=|V_s|\).

**Theorem 1 (direction-deleted graphic flat).** There is a canonical isomorphism, after choosing the coordinate-\(s\) zero layer,
\[
H_n[U_s]\cong L(Q_{n-1}).
\tag{1}
\]
The restriction of \(M_n\) to \(E(H_n[U_s])\) is the graphic cycle matroid of \(L(Q_{n-1})\), of rank
\[
(n-1)2^{n-2}-1.
\tag{2}
\]
Moreover, \(E(H_n[U_s])\) is a flat of \(M_n\). Its complement consists of \(2(n-1)m\) turns, partitioned into \(2m\) families of \(n-1\) turns according to the two endpoints of each direction-\(s\) edge of \(G_n\).

*Proof.* Every antipodal vertex pair of \(Q_n\) has a unique representative with coordinate \(s\) equal to zero. Deleting the direction-\(s\) edges from \(G_n\) identifies its remaining graph with \(Q_{n-1}\) on those representatives. Taking line graphs gives (1).

Every closed walk in this direction-deleted graph lifts to a closed walk in the layer \(x_s=0\) of \(Q_n\). Its covering monodromy is zero. Thus the extra row \(a\) of a matrix representing \(M_n\), restricted to \(E(H_n[U_s])\), lies in the cut space of the connected graph \(H_n[U_s]\). The matroid restriction is graphic, with rank \(|U_s|-1=(n-1)2^{n-2}-1\). Every turn outside this restriction has one endpoint in \(V_s\), so its incidence column has a nonzero entry in the corresponding \(V_s\)-row; all columns of the restriction vanish on that row. Such an outside column lies outside their span, proving flatness.

Each vertex \(v\in V_s\) represents an edge \(e_v\) of \(G_n\) in direction \(s\). At each endpoint of \(e_v\), there are \(n-1\) other incident edges, producing \(n-1\) distinct turns incident with \(v\). Since the direction-\(s\) edges of \(G_n\) form a matching, these are all turns outside the restriction. \(\square\)

**Theorem 2 (paired-column contraction).** Let \(T\) be any spanning tree of \(H_n[U_s]\). Contract \(T\) in \(M_n\) and delete the loops arising from \(E(H_n[U_s])\setminus T\). The remaining matroid has rank \(m+1\) and admits over \(\mathbb F_2\) the representation
\[
\boxed{\quad
\{\,e_v^{\,n-1},\ (e_v+z)^{\,n-1}:v\in V_s\,\}
\subseteq\mathbb F_2^{\,V_s}\oplus\mathbb F_2 z .
\quad}
\tag{3}
\]
Here \(e_v^{\,n-1}\) means \(n-1\) parallel copies of the standard vector \(e_v\). The first family represents turns at the endpoint of a selected cube-edge lift with \(s\)-coordinate zero; the second represents turns at its endpoint with \(s\)-coordinate one.

*Proof.* Choose a representative of each antipodal cube-edge pair: for any direction other than \(s\), take its unique edge lying in \(x_s=0\); for every direction-\(s\) pair, choose either one of its two cube edges. Define the reference coloring \(c_0\) to be zero on all selected representatives and one on their antipodes, and let \(a\) be its induced turn cochain on \(H_n\).

A turn between two directions other than \(s\) occurs in the layer \(x_s=0\), giving \(a=0\). A turn involving a direction-\(s\) edge has \(a=0\) when the two incident edges meet at the selected direction-\(s\) representative's endpoint in \(x_s=0\), and \(a=1\) at its endpoint in \(x_s=1\). Indeed, every non-\(s\) edge in the latter layer is antipodal to its selected representative. For the quotient turn, choosing the antipodal lift of both edges leaves their color difference unchanged.

Hence the matrix \(\left(\begin{smallmatrix}B\\a\end{smallmatrix}\right)\) has zero last entry on every edge of \(H_n[U_s]\). Contracting \(T\) identifies all its vertices into one incidence vertex. Deleting the redundant incidence row leaves the \(m\) rows indexed by \(V_s\), together with the monodromy row \(z\). A turn incident with \(v\in V_s\) has incidence vector \(e_v\), with monodromy entry zero or one according to the endpoint family. This gives (3). Every other edge of \(H_n[U_s]\) becomes a loop, since its incidence column belongs to the span of the tree columns and its monodromy entry is zero.

The \(m\) columns \(e_v\), together with any column \(e_v+z\), span \(\mathbb F_2^{m+1}\), proving the rank assertion. \(\square\)

**Corollary 3 (independence and four-element circuits).** Delete parallel copies in (3), and put \(P_v=\{e_v,e_v+z\}\) for every \(v\in V_s\). A set of columns is independent if and only if it contains both members of at most one \(P_v\). For distinct \(v,w\), the four columns of \(P_v\cup P_w\) form a circuit. Consequently \(M_n\) has, for each direction \(s\), a rank-\((2^{n-2}+1)\) minor on \(2^{n-1}\) elements represented by
\[
\begin{pmatrix}
I_m&I_m\\
0&\mathbf1^T
\end{pmatrix}.
\tag{4}
\]

*Proof.* In a linear relation among the columns in (3), the \(e_v\)-coordinate forces the two coefficients from each \(P_v\) to be equal. The \(z\)-coordinate then forces the number of fully selected pairs to be even. A nonzero relation therefore exists if and only if at least two complete pairs occur; any two complete pairs form a minimal relation. Deleting duplicate columns gives (4). \(\square\)

The contraction exhibits the covering monodromy as one shared binary degree of freedom across all direction-\(s\) pairs. The normal form holds for every antipodally odd edge coloring because \(M_n\) is independent of the coloring within its prescribed switching class. Direction-rainbow witnesses and integer turn weights remain additional data in applications to switch minimization.
