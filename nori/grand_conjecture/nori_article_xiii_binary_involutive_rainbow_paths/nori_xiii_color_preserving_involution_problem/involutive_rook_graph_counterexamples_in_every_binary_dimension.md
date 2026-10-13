# Involutive rook-graph counterexamples in every binary dimension

### A transfer from properly edge-colored complete graphs

**Theorem (rainbow-path deficiency transfer).** Let \(r\geq4\), and let \(\kappa\) be a proper edge coloring of \(K_r\). Write \(L\) for the maximum length of a \(\kappa\)-rainbow simple path. There is a connected simple graph \(G\) on \(r(r+1)\) vertices, a proper edge coloring \(\lambda\), a binary edge labeling \(\chi\), and a fixed-point-free involutive automorphism \(\tau\) such that
\[
\lambda(\tau e)=\lambda(e),\qquad \chi(\tau e)=1-\chi(e),\qquad
\hat\delta(G,\lambda)=2r-2,
\]
and every rainbow simple path with at most one \(\chi\)-change has at most \(2L\) edges. Moreover, there is no rainbow simple cycle of length \(2r-2\) having at most one \(\chi\)-change in any linear indexing of its edges.

**Proof.** Let \(I\) have \(r+1\) elements. Take the graph with vertex set
\[
V(G)=\{(i,j)\in I^2:i\neq j\},
\]
where two distinct vertices are adjacent precisely when their first coordinates agree or their second coordinates agree. Its rows \(R_i=\{(i,j):j\neq i\}\) and columns \(C_i=\{(j,i):j\neq i\}\) are copies of \(K_r\). This graph is connected: given vertices \((i,j)\) and \((a,b)\), choose \(s\in I\setminus\{i,j,a,b\}\), and join them through \((i,s)\) and \((a,s)\), omitting repeated vertices if \(i=a\).

For each \(i\), choose a bijection \(f_i:I\setminus\{i\}\to V(K_r)\). Color the row edges and the corresponding column edges by
\[
\begin{aligned}
\lambda((i,j)(i,j'))&=(i,\kappa(f_i(j)f_i(j'))),\\
\lambda((j,i)(j',i))&=(i,\kappa(f_i(j)f_i(j'))),
\end{aligned}
\qquad (j\neq j',\ i\notin\{j,j'\}),
\]
and give the row edges label \(\chi=0\) and the column edges label \(\chi=1\). The automorphism \(\tau(i,j)=(j,i)\) preserves \(\lambda\) and complements \(\chi\).

At \((i,j)\) the \(r-1\) row-edge colors have first coordinate \(i\), while the \(r-1\) column-edge colors have first coordinate \(j\). Each set consists of distinct colors by properness of \(\kappa\), and the two sets are disjoint because \(i\neq j\). Thus \(\lambda\) is proper and \(\hat\delta(G,\lambda)=2r-2\).

A path with \(\chi\)-word \(0\cdots01\cdots1\), or its reversal, consists of one path inside a row followed by one inside a column. Each rainbow segment has length at most \(L\), proving the path bound.

For cycles, a single-label cycle lies in a \(K_r\) and has length at most \(r<2r-2\). A cycle involving both labels must have an even number of changes when read cyclically. It cannot have two: its row segment and column segment would have two distinct common endpoints, whereas a row and column meet in at most one vertex. Thus a mixed-label cycle has at least four cyclic changes, and every linear indexing has at least three changes. \(\square\)

**Corollary (unbounded minimum color degree).** For every \(d\geq2\), there is such a graph with
\[
\hat\delta(G,\lambda)=2^{d+1}-2,
\qquad
L_{\leq1}(G,\lambda,\chi)\leq 2^{d+1}-4
=\hat\delta(G,\lambda)-2.
\]
The same graph refutes the alternative permitting rainbow paths **or cycles** of length at least the minimum color degree with at most one binary-label change.

**Proof.** Set \(r=2^d\), identify \(V(K_r)\) with \(H=\mathbb F_2^d\), and color an edge \(xy\) by \(\kappa(xy)=x+y\), a nonzero element of \(H\). This is a proper coloring with \(r-1\) colors. A rainbow path of length \(r-1\) would use every nonzero group element as an edge color. Summing its edge colors gives both the sum of its nonzero group elements, which is zero for \(d\geq2\), and the sum of its endpoint coordinates, which is nonzero because the endpoints differ. Hence \(L\leq r-2\), and the transfer theorem applies. \(\square\)

**Example (sharp bound at color degree six).** Take \(r=4\), \(I=\{0,1,2,3,4\}\), and \(H=\mathbb F_2^2=\{0,1,2,3\}\) with XOR addition. For each \(i\), let \(f_i\) map the increasing enumeration of \(I\setminus\{i\}\) onto \(0,1,2,3\). The rainbow path
\[
(0,1),(0,2),(0,3),(1,3),(2,3)
\]
has four edges and \(\chi\)-word \(0011\). It attains the one-switch upper bound \(4\), whereas the minimum color degree is \(6\). The longer path
\[
(0,1),(0,2),(0,3),(1,3),(2,3),(2,0),(2,1)
\]
has six pairwise distinct edge colors
\[
(0,1),(0,3),(3,1),(3,3),(2,2),(2,1)
\]
and \(\chi\)-word \(001100\). Thus this graph contains a rainbow path of length equal to its minimum color degree; the obstruction is its need for two binary-label changes.
