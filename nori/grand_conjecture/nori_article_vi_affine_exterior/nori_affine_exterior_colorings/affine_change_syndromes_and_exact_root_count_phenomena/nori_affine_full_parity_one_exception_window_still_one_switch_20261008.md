# One affine-exterior coefficient exception cannot destroy full NORI one-switch closure

# One exceptional window does not destroy affine NORI grand closure near the full-parity family

Let n>=4, choose a fixed exterior-parity coefficient vector a∈F2^n with at most THREE zero coordinates. Fix a direction permutation pi such that those zero-coordinate directions occupy distinct residue classes modulo3 in positions of pi (possible for any n>=max(4,#zeros)). Let h be ANY ordered-triple intercept function and let the baseline physical ordered-three-face coloring have affine exterior slope a restricted to the exterior of every ordered triple, i.e.
 c_0(F,(i,j,k))=h(i,j,k)+Σ_(t outside{i,j,k}) a_t z_t.
By the three-chain affine-exterior theorem, the full root-to-switch-change map for pi has linear part M_0 of full row rank m=n−3.

Now let c be ANY other physical ordered-three-face coloring AFFINE IN exterior bits, and suppose that for all but at most k of the n−2 consecutive ordered triples in the chosen permutation pi, c has the SAME exterior-bit COEFFICIENT VECTOR as the baseline c_0 (intercept bits may differ freely at every triple). For the k exceptional triples the full exterior slope may change arbitrarily. The c coloring may additionally satisfy the active antipodal-reversal-odd NORI axiom; it is not needed for this lemma.

**Theorem (rank loss ≤ exceptional windows).** For the chosen direction order pi,
 rank_F2(M_c) >= (n−3)−k,
and therefore there is an antipodal pi-geodesic with at most k ordered-three-face color changes. In particular for k=1, the FULL NORI grand one-switch conclusion HOLDS, and this is stronger than requiring the perturbation to preserve the color values near any one root.

**Proof.** Let L_0 and L_c be the (n−2)×n coefficient matrices whose rows are the linear parts of consecutive window colors as functions of the original cube-root bits. The root-progress flips only alter intercepts, never coefficients. Thus L_c=L_0+E where E has at most k nonzero rows. The respective change matrices are M_0=∂L_0 and M_c=∂L_c=M_0+∂E, where ∂ is the (n−3)×(n−2) binary consecutive-difference matrix. Since rank(∂E)≤rank(E)≤k, Sylvester's rank inequality gives
 rank M_c≥rank M_0−rank(∂E)≥m−k.
Apply the already proved affine syndrome theorem: for any affine map b+M x∈F2^m some output has weight at most m−rank M. This yields a full antipodal pi-geodesic with at most k switches. QED.

**More general statement.** Given ANY baseline affine ordered-face coloring and a chosen order pi for which its change matrix has codimension c_0, changing exterior slopes on at most k window triples guarantees a full antipodal pi-geodesic with at most c_0+k changes. This is a **linear-algebraic stability theorem** under local changes of physical ordered-face dependence. It does NOT require the intercepts of the windows to be close.

**Actual NORI construction.** Because the order pi uses distinct directions, none of its chosen consecutive increasing ordered triples is the reverse of another. One may prescribe arbitrary changes to an exceptional ordered triple's exterior coefficients and to all the consecutive intercepts, then extend these assignments to reversed triples using the NORI antipodal-reversal rule; this is consistent. Hence the one-exception closure statement genuinely applies to nontrivial, antipodally-reversal-odd face-dependent colorings that are not of the single-fixed-a form.

**Scope.** This is a dimension-independent broad perturbation-stable subclass, not the unrestricted NORI conjecture. With two arbitrary exceptional slope windows, the same method guarantees at most TWO switches, so a further exchange or local topological argument would be needed to reach the desired one switch.
