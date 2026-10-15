# Lipschitz variation under exchanges and an unbounded root seam

# Lipschitz variation under exchanges and an unbounded root seam

The twisted cyclic-variation invariant \(D\) of the preceding subsection depends only on the canonical flag-rotation orbit, not on the root selected within the orbit. Its behavior under individual Coxeter rank exchanges makes the key distinction between the two motivating geometries precise: exchanges preserving the starting cube root are local in \(D\), but the exchange changing that root can alter \(D\) by an amount linear in dimension.

For an antipodally odd cube-edge coloring, set
\[
D(x,\pi)=\sum_{j=1}^{n-1}\mathbf1_{\{w_j\ne w_{j+1}\}}
+\mathbf1_{\{w_n=w_1\}},
\tag{1}
\]
where \(w\) is the full-geodesic edge-color word. The last summand is the comparison of \(w_n\) with the complement of \(w_1\). The total \(D\) is odd and unchanged by the flag rotation \(T\).

For an ordinary boundary tournament and a cyclic ordering \(\pi=(v_0,\ldots,v_{n-1})\), put \(a_j=b(v_j,v_{j+1},v_{j+2})\) with cyclic indices and
\[
D_{\rm bdry}(\pi)=\sum_{j\in\mathbb Z/n\mathbb Z}
\mathbf1_{\{a_j\ne a_{j+1}\}}.
\tag{2}
\]
It is even and invariant under cyclic rotation and reversal of the vertex order.

**Theorem 1 (local rank-exchange bounds).**
(a) Exchanging two consecutive dimensions in a cube geodesic while retaining its root changes the cyclic invariant (1) by at most two:
\[
\boxed{|D(x,\pi)-D(x,\pi\circ s_i)|\le2,\qquad 1\le i<n.}
\tag{3}
\]
(b) Exchanging two consecutive vertices of a boundary cyclic order changes (2) by at most four:
\[
\boxed{|D_{\rm bdry}(\pi)-D_{\rm bdry}(\pi\circ s_i)|\le4.}
\tag{4}
\]

*Proof.* For (a), a transposition of adjacent dimensions affects only the corresponding two consecutive original cube edges: the root and all earlier edges agree, and after both exchanged steps the paths arrive at the same cube vertex and follow the same suffix. Thus the two binary \(n\)-words differ in at most two consecutive positions. Only the three comparisons meeting this pair can change, counting the antipodal closing comparison as cyclic. Since both total comparison counts are odd, their difference is even, so it has magnitude at most two.

For (b), switching two adjacent elements of a cyclic vertex order changes only those cyclic triples containing either exchanged element. There are four possible starting positions, consecutive around the cyclic index set. Only the five comparisons incident with these four entries can change. Both cyclic variation counts are even, so their difference is even and hence has magnitude at most four. \(\square\)

**Theorem 2 (sharp linear obstruction at the cube root flip).** For every \(n\ge3\) there is an antipodally odd undirected-edge coloring of \(Q_n\) and two *adjacent type-B Coxeter chambers*
\[
g=(0;1,2,\ldots,n),\qquad
h=(e_1;1,2,\ldots,n)
\tag{5}
\]
whose root-slide orbits have cyclic variation values
\[
\boxed{
D(g)=1,\qquad
D(h)=
\begin{cases}
n,&n\text{ odd},\\
n-1,&n\text{ even}.
\end{cases}}
\tag{6}
\]
The difference is \(n-1\) for odd \(n\) and \(n-2\) for even \(n\), the largest difference compatible with odd cyclic-variation parity. In particular, no dimension-independent Lipschitz bound on \(D\) holds over all adjacent type-B chamber pairs.

*Proof.* Let \(A\) be the complete geodesic from \(0\) using dimensions \(1,2,\ldots,n\), and let \(B\) be the complete geodesic from \(e_1\) using the same dimension order. The initial undirected edge of both is \(\{0,e_1\}\). For each \(j\ge2\), the dimension-\(j\) edge of \(A\) lies in the face \(x_1=1\), while that of \(B\) lies in \(x_1=0\), so the two edges differ. Neither is the antipodal image of the other: since \(n\ge3\), choose a dimension \(k\notin\{1,j\}\). At their \(j\)-th edges, paths \(A\) and \(B\) have the same bit \(x_k\), whereas antipodal edges must have opposite bits \(x_k\). The pairs of paths therefore have no common antipodal edge orbit except their shared initial edge. Distinct positions also have different edge dimensions, so no additional antipodal orbit coincidences arise.

We may consequently prescribe the colors of all edges of \(A\) to be zero and prescribe the colors of the \(j\)-th edges of \(B\) to be \(j-1\bmod2\). The prescriptions agree on the common initial edge and have no conflicts with antipodal oddness. Extend the coloring arbitrarily to the remaining antipodal edge orbits. Then
\[
w(A)=0^n,\qquad
w(B)=(0,1,0,1,\ldots).
\]
The antiperiodic cyclic comparison count of \(0^n\) is one. The alternating word has a change at every internal comparison. Its twisted closing comparison is one for odd \(n\) and zero for even \(n\), yielding (6). Since the chambers differ only by the type-B rank-zero flip across their shared initial edge, they are adjacent. \(\square\)

**Consequences for a common proof.** The exchange bounds (3)–(4) suggest minimizing \(D\) on the graph of rotation orbits rather than on all rooted flags. But Theorem 2 isolates an obstruction specific to gluing the cube's fixed-root type-A fibers: the single rank-zero exchange can leap from an orbit with a monochromatic geodesic to an orbit whose every root-slide has nearly the largest possible switch count. Therefore a proof that treats every adjacent flag exchange as a bounded local energy perturbation cannot work. The missing mechanism must correlate the many root-changing exchanges globally, or use a topological chain construction whose cancellations do not rely on local variation monotonicity.
