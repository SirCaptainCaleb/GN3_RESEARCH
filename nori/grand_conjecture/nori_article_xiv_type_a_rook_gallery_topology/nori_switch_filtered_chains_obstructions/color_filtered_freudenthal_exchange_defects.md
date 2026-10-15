# Color-filtered Freudenthal exchange defects

# Color-filtered Freudenthal chains and exchange defects

Wu and Yang's unrestricted Freudenthal subdivision sums all maximal monotone simplices of a cubical face, so each internal facet cancels in a pair of adjacent permutations. Keeping only those simplices whose complete ordered edge path is monochromatic preserves dimension-simplicity, but introduces a computable obstruction to this cancellation.

Let \(F\) be a \(d\)-dimensional cubical face rooted at a corner \(x\). For each dimension order \(\pi\), let
\[
\sigma_\pi=[v_0=x,v_1,\ldots,v_d],\quad
v_k=x\oplus e_{\pi_1}\oplus\cdots\oplus e_{\pi_k}.
\]
For a bit \(a\), let \(\chi_a(e)=1\) if the undirected cube edge \(e\) has color \(a\), and \(0\) otherwise. Put
\[
r_a(\pi)=\prod_{k=1}^{d}\chi_a(v_{k-1},v_k),\qquad
M_a(F,x)=\sum_{\pi}r_a(\pi)\sigma_\pi
\]
over \(\mathbb F_2\). Every simplex with nonzero coefficient corresponds to a monochromatic geodesic using each of the face's dimensions once.

**Theorem (all-rank exchange-defect identity).** Let \(s_j\pi\) exchange positions \(j,j+1\), \(1\le j<d\), and let \(\tau_{\pi,j}\) be the internal facet shared by \(\sigma_\pi\) and \(\sigma_{s_j\pi}\). Then the internal part of the boundary is
\[
\boxed{
D_a(F,x)=\sum_{j=1}^{d-1}\sum_{\{\pi,s_j\pi\}}
(r_a(\pi)+r_a(s_j\pi))\,\tau_{\pi,j}.
}
\]
If the two exchanged dimensions are \(i,h\), the paths agree up to a vertex \(u\), traverse opposite sides of the dimension-\(\{i,h\}\) square, rejoin at \(u^{ih}=u\oplus e_i\oplus e_h\), and agree thereafter. Let \(A_\pi,B_\pi\) be the products of the red-edge indicators on the shared prefix and suffix. Then
\[
\boxed{
r_a(\pi)+r_a(s_j\pi)=A_\pi B_\pi
\left[
\chi_a(u,u^i)\chi_a(u^i,u^{ih})
+\chi_a(u,u^h)\chi_a(u^h,u^{ih})
\right].
}
\]

*Proof.* Every internal Freudenthal facet is shared by the two maximal simplices obtained by the relevant adjacent exchange, giving the first formula. The two corresponding complete paths have identical outside edges, so their selectors factor through the two alternative length-two square routes, giving the second formula. \(\square\)

**Antipodal covariance.** If \(c(\bar e)=1-c(e)\), the antipode \(A\) gives
\[
A_\#M_a(F,x)=M_{1-a}(\bar F,\bar x),
\quad
A_\#D_a(F,x)=D_{1-a}(\bar F,\bar x).
\]
This follows because antipodal translation preserves dimension order and complements each traversed bit.

**Failure of the naive filtered chain map.** Already on a square, one two-edge route may be entirely red while the other contains a blue edge; then the shared internal diagonal occurs once rather than twice in the boundary. Such local assignments can be extended antipodally in \(Q_n\) for \(n\ge3\).

Therefore the unfiltered Freudenthal cancellation from Wu and Yang does not persist when retaining only dimension-simple monochromatic certificates. Its failure is completely localized to the local square expression above, multiplied by the admissibility of the shared prefix and suffix. A proof must construct correction chains cancelling these interior defects *coherently on higher-dimensional faces*, while also treating the color-dependent exterior facets. The formula and its antipodal covariance are proved; a complete equivariant correction is not.
