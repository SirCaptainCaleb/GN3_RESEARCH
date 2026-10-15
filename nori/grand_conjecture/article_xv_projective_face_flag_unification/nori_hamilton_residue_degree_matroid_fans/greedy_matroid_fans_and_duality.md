# Greedy matroid fans and duality

### Connected matroid greedy fans carry degree one

Fix an \(m\)-element ground set \(E\), \(m\ge2\), and \(W=\{z\in\mathbb R^E:\sum z_i=0\}\). Let \(P_m\subset W\) be the centered permutahedron with vertices indexed by all orders \(\pi\) of \(E\).

**Theorem 1 (matroidal prefix degree).** Let \(M\) be any connected matroid on \(E\). Put \(p_M=|\mathcal B(M)|^{-1}\sum_{B\in\mathcal B(M)}\mathbf1_B\), the barycenter of its basis polytope. Let \(B_M(\pi)\) be the greedy basis obtained by scanning the order \(\pi\) and accepting an element precisely when it increases rank. At each permutahedral vertex define
\[
g_M(\pi)=\mathbf1_{B_M(\pi)}-p_M\in W.
\]
This vertex labeling admits a zero-free piecewise-affine extension to \(\partial P_m\). After radial normalization, its degree is \(\pm1\).

*Proof.* A proper face of \(P_m\) is indexed by an ordered partition with first block \(S\), a nonempty proper subset of \(E\). Every order compatible with that face begins with precisely the elements of \(S\). Greedy selection accepts a basis of \(S\) before any other element, so
\[
\sum_{e\in S}g_M(\pi)_e=r_M(S)-p_M(S).
\tag{1}
\]
Connectivity of \(M\) implies \(r_M(S)+r_M(E\setminus S)>r_M(E)\). Extend a basis of \(E\setminus S\) to a basis of \(M\); this basis meets \(S\) in only \(r_M(E)-r_M(E\setminus S)<r_M(S)\) elements. All bases meet \(S\) in at most \(r_M(S)\) elements. Therefore their average satisfies \(p_M(S)<r_M(S)\), so (1) is strictly positive at all vertices of the face. Affine interpolation on any triangulation of that boundary face stays in this halfspace and avoids zero.

The centered permutahedron vertex \(u_\pi=\sum_{j=1}^m((m+1)/2-j)e_{\pi_j}\) satisfies \(\sum_{e\in S}(u_\pi)_e=|S|(m-|S|)/2>0\) on this face. Consequently the straight-line homotopy from \(g_M\) to \(u_\pi\), extended affinely over boundary simplices, avoids zero throughout. The radial map from the centered permutahedron boundary has degree \(\pm1\). QED.

**Theorem 2 (arbitrary connected matroid selection).** Even if a different connected matroid \(M_\pi\) is selected independently at every permutation \(\pi\), the labels \(g_{M_\pi}(\pi)\) still induce a zero-free boundary map of degree \(\pm1\).

*Proof.* The inequality (1) holds for every connected matroid on the same ground set, with the same positive side of the supporting hyperplane associated with \(S\). Both the zero-avoidance and the homotopy to \(u_\pi\) therefore hold vertexwise on each proper permutahedral face, regardless of the choice of \(M_\pi\). QED.

**Theorem 3 (dual complement and reversal).** Let \(M^*\) be the dual matroid and \(\pi^R\) the reversed total order. Then
\[
B_{M^*}(\pi^R)=E\setminus B_M(\pi),\qquad
p_{M^*}=\mathbf1-p_M,\qquad
\boxed{g_{M^*}(\pi^R)=-g_M(\pi).}
\tag{2}
\]

*Proof.* A basis of \(M^*\) is the complement of a basis of \(M\). A greedy basis is the unique maximum-weight basis for any strictly decreasing order-compatible generic weights; reversing the order is equivalent to negating the weights. Maximizing reversed weights among dual bases is thus equivalent to maximizing the original weights among primal bases and taking complements. Averaging the bijection of bases gives the barycenter identity, and subtracting barycenters gives (2). QED.

**Specialization to the switch-bivector program.** The greedy basis of the uniform matroid \(U_{k,m}\) is the first \(k\) symbols of \(\pi\), with barycenter \((k/m)\mathbf1\). Thus Theorems 1 and 2 generalize the variable-length centered prefix degree theorem. Equation (2) explains why complement reversal of ordered flags acts antipodally on these carrier vectors. This is an intrinsic matroidal degree carrier shared by the dimension-order structures underlying the cube and boundary Hamilton order problems, not a proof of either coloring conjecture; the necessary color-sensitive global extension remains unresolved.
