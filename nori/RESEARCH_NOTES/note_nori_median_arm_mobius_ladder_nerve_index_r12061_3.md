# Median-arm cover, Möbius-ladder nerve, and projective index

- Stable ID: note_nori_median_arm_mobius_ladder_nerve_index_r12061_3
- Author: unspecified; session provenance retained
- Primary home: subsection:central_freudenthal_subdivision_and_the_all_root_geodesic_chamber_sphere
- Labels: NORI1, topology, median, Freudenthal, equivariant-index
- Lifecycle: active
- Epistemic status: proved
- Current version: 3
- Retention: current and at most one previous snapshot
- Created session: session_nori_r12061_3
- Updated session: session_nori_r12118_3
- Disposition: none
- Successor: none

## Related references

- note:note_nori_xvii_median_three_route_telescoping_r12024_2

## Research note

# Median-arm cover, Möbius-ladder nerve, and projective index

Let n>=d>=3, with d odd, and partition [n] into nonempty direction blocks B_1,...,B_d. The antipodal 2d-run cycle C arises by toggling these blocks in order, twice. For each vertex p of C, let I_p,J_p denote its two incident run blocks. Define the cubical face F_p by fixing every bit in I_p union J_p at the bit values of p, leaving all other dimensions free. Then dim F_p=n-|I_p|-|J_p|, and tau(F_p)=F_(tau p).

THEOREM 1 (median-arm cover). The union U of all F_p is the union of the cubical median-to-corner faces of every spanning triangle among the 2d cycle vertices (three cyclic gaps each <d). Indeed a median arm ending at p cannot change either incident run block, so is contained in F_p. In compressed d-bit notation at p=0^d, the triangle {v_0,v_(d-1),v_(d+1)} has median 0 1^(d-2) 0 and its median arm to p equals F_p. Cyclic symmetry completes the proof.

In the compressed d-cube, U is the union of the 2d faces z_j=0,z_(j+1)=1 or z_j=1,z_(j+1)=0 (1<=j<d), together with z_1=z_d=0 or z_1=z_d=1. A compressed vertex z belongs to V(z)+[z_1=z_d] faces, V(z)=sum_(j<d)[z_j != z_(j+1)]. This is always odd by telescoping XORs. An edge changing bit i is absent from the compressed 1-skeleton of U iff all bits before i are constant, all bits after i are constant, and those two constants are opposite when i is not an endpoint. These are precisely the two C-edges of direction i (with analogous end cases). Hence U contains every coarse vertex and every coarse edge except those of C. This 1-skeleton claim concerns the compressed d-cube; it need not hold for all edges in the original n-cube when some blocks have size >1.

THEOREM 2 (nerve). Two distinct faces F_(v_i), F_(v_j) are disjoint iff j-i equals +1,-1,or d modulo 2d. Conflicting assignments on a fixed direction block occur precisely at neighboring or antipodal cycle vertices. Other fixed-bit assignments are compatible. Pairwise compatibility implies compatibility of any family. Therefore the nerve of {F_p} is Ind(M_(2d)), the independence complex of the Möbius ladder made by adding antipodal chords to C_(2d). Every nonempty face intersection is a convex subcube, and the antipodal involution permutes the cover freely. Hence U and Ind(M_(2d)) are equivariantly homotopy equivalent.

THEOREM 3 (index). Agarwal and Basak, The Homotopy Types of the Independence and Perfect Matching Complex of Möbius Ladder Graph, arXiv:2608.30601 (2026), show that for odd d, Ind(M_(2d)) has ordinary homotopy type S^m, m=2 floor((d-1)/4). For d=3, the two contractible components are exchanged by tau, so index=0. For d>=5, the mod-two Cartan-Leray spectral sequence of the free involution has cohomology concentrated in two rows of degrees 0 and m. Its transgression of the degree-m generator must be u^(m+1), since the quotient is finite-dimensional. Thus H^*(U/tau;F2)=F2[u]/(u^(m+1)), giving cohomological antipodal index m.

COROLLARY (relative class). The inclusion U/tau into the projective boundary sphere RP^(n-1) has nonzero restriction of u^m and zero restriction of u^(m+1). Consequently u^(m+1) lifts to a class in H^(m+1)(RP^(n-1),U/tau;F2), whose product with u^(n-m-2) maps to nonzero u^(n-1). Since the full n-cube is contractible, H_(m+1)(Q_n,U;Z) is Z for d>=5. This is a projective relative obstruction attached to a minimum-defect run cycle.

The construction uses original cubical faces and their common bit constraints, but is color-independent once C is selected. Large simplices in the nerve may involve four or more face anchors at one common point and need not give a three-arm partition of [n]. Producing a color-sensitive chain map that converts the relative obstruction into a lower-switch antipodal geodesic remains open.

## Canonical seam-majority poles and the mixed-family suspension (session session_nori_r12118_3)

Fix any legally antipodally odd edge coloring and a full geodesic P of twisted defect \(d=2r+1\ge3\). On its antipodally doubled cycle write \(z_j\), \(j\in\mathbb Z/d\), for the red-to-blue seam vertices. Denote the blue run from \(z_j\) toward the next seam by \(B_j\subset[n]\) (its original direction support), and the subsequent red run by \(R_j\). The \(d\) nonempty blocks \(B_j\) partition \([n]\). Antipodal translation shifts the \(2d\)-run sequence by \(d=2r+1\) runs and preserves direction supports while interchanging blue and red. Therefore
\[
R_{j+r}=B_j,\qquad R_j=B_{j-r}.
\tag{MP1}
\]

Let \(m\) be the unique coordinatewise majority of the \(z_j\), equivalently the canonical seam-majority selector from the first-Walsh theorem. The path beginning at \(z_j\) and ending at \(\bar z_j\) traverses the red blocks \(R_j,\ldots,R_{j+r-1}\) and the blue blocks \(B_j,\ldots,B_{j+r}\). Its direction-i color word gives \(m_i=(z_j)_i\) on blue directions and \(m_i=1-(z_j)_i\) on red directions. In particular
\[
\boxed{D(m,z_j)=
B_{j-r}\sqcup B_{j-r+1}\sqcup\cdots\sqcup B_{j-1}.}
\tag{MP2}
\]
These are r cyclically consecutive blocks. This provides a block-level explanation of the support-interval lemma and the disjoint support pairs used in the newly established d-route telescoping law.

Recall the cubical face \(F_p\) at a run-boundary vertex \(p\): it fixes the two run blocks incident at p, leaving all other original directions free. At \(z_j\) its fixed blocks are the outgoing \(B_j\) and the incoming \(R_{j-1}=B_{j+r}\), both blue in the full path rooted at \(z_j\). They therefore agree with m on these fixed blocks. Every \(B_k\) is fixed in at least one of these faces. This proves:

**Theorem (opposed face poles).**
\[
\boxed{\bigcap_{j\in\mathbb Z/d}F_{z_j}=\{m\},
\qquad
\bigcap_{j\in\mathbb Z/d}F_{\bar z_j}=\{\bar m\}.}
\tag{MP3}
\]
Let \(U_+=\bigcup_j F_{z_j}\), \(U_-=\bigcup_jF_{\bar z_j}\), and \(W=U_+\cap U_-\). Then \(U_+\) is star-shaped about m, \(U_-\) is star-shaped about \(\bar m\), and cube antipodality exchanges them. Both are contractible cubical subcomplexes. The full median-arm face cover of the earlier theorem is \(U=U_+\cup U_-\).

**Theorem (equivariant mixed-overlap suspension).** The cubical cover U is equivariantly homotopy equivalent to the unreduced suspension \(\Sigma W\), with involution
\[
(w,t)\longmapsto(\tau w,-t)
\tag{MP4}
\]
on its suspension model; for \(W=\varnothing\), interpret this as the antipodal two-point sphere.

*Proof.* The two inclusions \(W\hookrightarrow U_\pm\) are cubical subcomplex cofibrations. Thus their ordinary union is their homotopy pushout. Contract \(U_+\) toward m and \(U_-\) toward \(\bar m\) using straight segments inside their constituent faces, choosing the two contractions as antipodal translates. Replacing the two contractible terms of this equivariant homotopy-pushout diagram by its two poles yields the homotopy pushout of \( * \leftarrow W \rightarrow *\), namely \(\Sigma W\), with the indicated free involution. \(\square\)

Together with the previously established homotopy computation \(U\simeq S^h\), where \(h=2\lfloor(d-1)/4\rfloor\) for odd d, this implies that for \(d\ge5\) the mixed overlap W has reduced integral homology \(\mathbb Z\) in degree \(h-1\) and zero in all other degrees. For d=3, the two opposing families are disjoint and W is empty.

**Relation to original-color forcing.** For each j, the entire median-to-seam interval \([m,z_j]\) lies in \(F_{z_j}\). Hence every arm \(H_j:m\to z_j\) of the d-route telescoping theorem lies in the contractible positive family \(U_+\); its antipodal image lies in \(U_-\). The nontrivial equivariant topology of the full face cover is assembled at the mixed overlap W, where faces from both families meet. The geometric poles and their suspension are established; the missing color-sensitive operation is to transport information across W so that the odd-cycle arm-energy inequality fails for a hypothetical globally minimum bad path. The topology of U alone supplies no arm switch-cost estimate.


## Faithful vertex-level decoding through the mixed overlap (session session_nori_r12118_3)

Keep the opposed-star construction above. Every original cube vertex \(x\in V(W)\) belongs to some \(F_{z_j}\cap F_{\bar z_k}\). The intervals \(I(m,x)\) and \(I(x,\bar m)\) lie wholly in those respective cubical faces, since a cubical face contains the interval between any two of its vertices. Their original direction sets are \(D(m,x)\) and \(D(x,\bar m)=[n]\setminus D(m,x)\).

**Proposition (legal mixed-overlap assembly).** For every \(x\in V(W)\), every original-cube geodesic \(P_+:m\to x\) and every original-cube geodesic \(P_-:x\to\bar m\) concatenate to a full direction-simple antipodal geodesic. The two paths can be chosen independently among the paths contained in their corresponding faces. If their ordinary internal switch numbers are \(s_+,s_-\), first colors are \(\alpha_+,\alpha_-\), and final colors are \(\beta_+,\beta_-\), then
\[
D(P_+*P_-)=s_++s_-+
[\beta_+\ne\alpha_-]+[\beta_-=\alpha_+].
\tag{MP5}
\]
In particular, if the two arms are individually monochromatic (with either relationship between their colors), the concatenation has twisted defect one, and a root slide produces a monochromatic full antipodal geodesic.

*Proof.* The two direction supports partition [n], so the concatenation uses every original direction once. Every candidate arm is a path in the original shared-edge-colored cube; face containment follows from interval convexity. Count its two color joins, treating the twisted closing seam as [last color equals first color]. If both arms are monochromatic, equal colors give a monochromatic path, while opposite colors give a one-change path. Both have twisted defect one. \(\square\)

For a hypothetical globally minimum bad coloring with minimal defect d>=3, (MP5) must be >=d for EVERY mixed-overlap vertex and EVERY choice of both arms. This is a compatible two-ended obstruction indexed by the cubical vertices of a space whose essential topology is the mixed-overlap equator W. The face geometry supplies the legal integral path assembly automatically; the missing assertion is that global topology forces a low-defect pair of arm witnesses at one common **original vertex** of W. Existing fractional-zero counterexamples preclude replacing this assertion with arbitrary convex averaging of individual path profiles.
