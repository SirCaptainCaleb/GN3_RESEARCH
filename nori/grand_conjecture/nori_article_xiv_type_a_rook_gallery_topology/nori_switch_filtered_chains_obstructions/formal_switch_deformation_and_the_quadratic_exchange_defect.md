# Formal switch deformation and the quadratic exchange defect

# Formal switch deformation and its local quadratic exchange law

Wu–Yang's Freudenthal chain is the sum of all maximal monotone simplices of a cubical face. Every such simplex represents a dimension-simple path. We deform its coefficient to retain the number of color switches, and obtain an all-rank local expression for the failure of adjacent-exchange cancellation.

Let \(F\) be a cubical face of dimension \(d\ge4\), rooted at a corner \(x\). For every order \(\pi\) of the varying dimensions, let \(\sigma_\pi\) be the corresponding Freudenthal simplex, \(w(\pi)\) its ordered edge-color word, and \(S(\pi)\) the integer count of switches. Define the chain over \(\mathbb F_2[u]\)
\[
\boxed{\mathfrak F_u(F,x)=\sum_{\pi}(1+u)^{S(\pi)}\sigma_\pi.}
\tag{1}
\]
At \(u=0\) this recovers the ordinary Freudenthal chain of Wu and Yang.

Let \(\pi'=s_j\pi\) exchange two successive dimensions, and let \(\tau_{\pi,j}\) be the common internal facet of their two simplices. Its coefficient in \(\partial\mathfrak F_u\) is
\[
E_{\pi,j}(u)=(1+u)^{S(\pi)}+(1+u)^{S(\pi')}.
\tag{2}
\]

**Theorem 1 (switch-deformation factorization).** For every adjacent exchange of complete rooted dimension orders, \(|S(\pi)-S(\pi')|\le2\). Writing \(h=\min(S(\pi),S(\pi'))\), one has
\[
\boxed{
E_{\pi,j}(u)=
\begin{cases}
0,&S(\pi)=S(\pi'),\\
u(1+u)^h,&|S(\pi)-S(\pi')|=1,\\
u^2(1+u)^h,&|S(\pi)-S(\pi')|=2.
\end{cases}}
\tag{3}
\]
For interior exchanges \(2\le j\le d-2\), the first and last edge colors remain fixed, so \(S(\pi)-S(\pi')\) is even. Consequently *all interior Freudenthal facets cancel modulo \(u^2\)*; only the two endpoint exchanges \(j=1,d-1\) may have nonzero first-order defects.

*Proof.* Adjacent exchange alters only the two edge colors in the exchanged positions. For an interior exchange, its affected three neighboring comparisons all share the same flanking bits and hence have the same parity of switch count on the two routes. Their difference is \(0\) or \(\pm2\), since each count lies between zero and three. At an endpoint exchange, at most two comparisons are affected, so the switch difference has absolute value at most two. The factorization is immediate from
\((1+u)^{h+k}+(1+u)^h=(1+u)^h((1+u)^k+1)\) for \(k=0,1,2\), together with \((1+u)^2+1=u^2\) in characteristic two. \(\square\)

**Theorem 2 (quadratic six-bit defect).** For an interior exchange write the affected word segments as
\[
(A,p,q,B)\quad\text{and}\quad(A,r,s,B).
\]
Then
\[
\boxed{
[u^2]E_{\pi,j}(u)
=A(p\oplus r)\oplus B(q\oplus s)
\oplus(p\oplus q\oplus r\oplus s)
\oplus pq\oplus rs.
}
\tag{4}
\]
This depends only on the colors of the four square edges and the two flanking edges, not on any earlier or later colors. It equals one precisely when the interior exchange changes the switch count by two.

*Proof.* Write \(k\) for the number of changes among the three comparisons in \((A,p,q,B)\), and \(k'\) for the alternative segment; both have parity \(A\oplus B\). If \(C\) denotes the number of unaffected switches, the coefficient of \(u^2\) in (2) is
\[
\binom{C+k}{2}+\binom{C+k'}{2}
=\binom k2+\binom{k'}2\pmod2,
\]
because the terms involving \(C\) cancel. With \(\delta_0=A\oplus p\), \(\delta_1=p\oplus q\), \(\delta_2=q\oplus B\), one has
\[
\binom{k}{2}\equiv\delta_0\delta_1+\delta_0\delta_2+\delta_1\delta_2
=AB\oplus Ap\oplus Bq\oplus p\oplus q\oplus pq.
\]
Add the analogous formula with \(r,s\) to obtain (4). The final assertion follows from (3). \(\square\)

**Corollary 3 (flat-square defects survive).** Put \(A=B=p=q=0\), \(r=s=1\). The two four-letter words are \(0000\) and \(0110\), with zero and two switches. The ordinary four-edge square curvature is \(p\oplus q\oplus r\oplus s=0\), but (4) equals one and
\[
E_{\pi,j}(u)=u^2.
\]
Thus the quadratic defect contains coloring information beyond the ordinary cubical square curvature.

**Theorem 4 (interior exchange integrability).** Fix a root and the first and last dimensions of a full monotone path, and consider the graph of permutations of the remaining dimensions, joined by interior adjacent exchanges. The second-order defect function on its edges is a coboundary:
\[
\boxed{\omega(\pi,\pi')=H(\pi)\oplus H(\pi'),\qquad
H(\pi)=\binom{S(\pi)}2\bmod2.}
\tag{5}
\]
Hence its sum along any commuting-square, braid-hexagon, or other closed exchange walk is zero.

*Proof.* The coefficient of \(u^2\) in (2) is precisely \(H(\pi)+H(\pi')\), and the sum telescopes around any closed walk. \(\square\)

**Scope.** These results prove local algebraic compatibility and show that the first nontrivial interior defects arise at *second order*, while endpoint exchanges may obstruct at first order. They do not show that the formal chain (1) is a chain map: the endpoint facets and the external facets of cubical faces still need correction, and higher equivariant root changes must preserve the used-dimension supports. In particular the coboundary identity (5) is an integrability condition on an exchange graph, not a globally constructed Wu–Yang chain homotopy.
