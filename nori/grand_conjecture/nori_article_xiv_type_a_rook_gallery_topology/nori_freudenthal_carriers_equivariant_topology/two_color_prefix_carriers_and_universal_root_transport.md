# Two-color prefix carriers and universal root transport

The union of the red and blue prefix complexes at a root is a cone. Its intersection with its antipodal image characterizes a full one-switch geodesic. Every colored edge admits a contractible bridge between these cones and their lower-dimensional antipodal complements. Higher square coherence remains open.

Let \(c:E(Q_n)\to\mathbb F_2\) be an arbitrary antipodally odd undirected edge coloring, \(n\ge3\). For each root \(x\), write \(K_x^a\) for the monochromatic color-\(a\) geodesic-prefix Freudenthal subcomplex of Article XIV. Define
\[
\boxed{C_x=K_x^0\cup K_x^1.}
\]
Both constituents are simplicial cones with apex \(x\), so \(C_x\) is a cone. Every simplex uses disjoint sets of cube dimensions between its consecutive support sets. Every edge incident to \(x\) lies in \(C_x\), regardless of color. Antipodal oddness yields \(AC_x=C_{\bar x}\).

**Theorem 1 (color-blind antipodal intersection).** For each root \(x\),
\[
\boxed{C_x\cap C_{\bar x}\ne\varnothing
\iff\text{a full geodesic beginning at }x\text{ has at most one switch}.}
\]

*Proof.* These two cones are subcomplexes of the same antipodally invariant rooted Freudenthal triangulation. If they intersect, they share a vertex \(y\). There are monochromatic geodesics \(x\to y\) of some color \(a\), and \(\bar x\to y\) of some color \(b\). Their dimension supports are complementary, so concatenating the first with the reversal of the second gives a full geodesic whose word is a run of \(a\) followed by a run of \(b\). Conversely, split any at-most-one-switch full geodesic from \(x\) at its change, or at any intermediate vertex if it is monochromatic. The two segments, one read backward from \(\bar x\), are monochromatic paths meeting at a vertex in both cones. \(\square\)

**Corollary 2 (single sphere target per root).** If no monochromatic full antipodal geodesic exists anywhere, then all \(C_x\) are disjoint from their antipodes and are contained in the cube boundary \(S^{n-1}\). The complements
\[
Z_x=S^{n-1}\setminus(C_x\cup AC_x)
\]
have the equivariant homotopy type of the antipodal sphere \(S^{n-2}\).

*Proof.* By root-slide rotation, one-switch full geodesics are equivalent to monochromatic full geodesics over freely varying roots. Theorem 1 gives disjointness. No monochromatic prefix of either color can use all \(n\) dimensions, so every generating simplex lies in a proper cubical face. The cone \(C_x\) is collapsible. The equivariant Alexander-dual dimension-drop theorem proved earlier applies. \(\square\)

**Theorem 3 (universal colored-edge bridge for the single target family).** If \(xy\) is a cube edge of color \(a\), with varying dimension \(i\), let
\[
B_{xy}^a=(K_x^a\cap H_{i,x_i})\cup[x,y]\cup
(K_y^a\cap H_{i,y_i}).
\]
This contractible bridge is contained in \(K_x^a\cap K_y^a\), and therefore in \(C_x\cap C_y\). Under the same hypothetical NORI1 counterexample, the inclusions
\[
\boxed{
Z_x\hookrightarrow Z_{xy}\hookleftarrow Z_y,\qquad
Z_{xy}=S^{n-1}\setminus(B_{xy}^a\cup AB_{xy}^a),
}
\]
are equivariant homotopy equivalences. This holds for **every** cube edge, regardless of its color, using a single target \(Z_x\) at each root.

*Proof.* The earlier red-edge cone-extension theorem applies to an edge of color \(a\) with that color in place of red. Every prefix being coned uses dimensions other than \(i\), so the added \(i\)-edge preserves independence. The bridge is collapsible, as proved in the canonical bridge lemma. Under Corollary 2, it is disjoint from its antipode and lies in each endpoint cone \(C_x,C_y\). Alexander duality makes both complement inclusions integral homology equivalences, since each inclusion of a bridge together with its antipode into a larger pair of cones identifies the two contractible components. By the equivariant dimension-drop theorem and equivariant Whitehead, these homology equivalences are equivariant homotopy equivalences. \(\square\)

**Theorem 4 (flat integral transport and ordinary homotopy-class coherence).** Under the hypotheses of Corollary 2, choose an orientation of the boundary sphere \(S^{n-1}\). For each cube root \(x\), let
\[
o_x\in\widetilde H_{n-2}(Z_x;\mathbb Z)\cong\mathbb Z
\]
be the class corresponding under integral Alexander duality to the characteristic function of the component \(C_x\) in
\(\widetilde H^0(C_x\sqcup AC_x;\mathbb Z)\). Then:

(i) For every cube edge \(xy\), the canonical bridge zigzag of Theorem 3 carries \(o_x\) to \(o_y\).

(ii) Given any two cube-edge walks \(\gamma,\gamma'\) with the same starting and terminal roots, the induced homotopy equivalences \(Z_x\to Z_y\), defined by composing the bridge zigzags and choosing homotopy inverses, are homotopic as ordinary maps. In particular, every cubical square is coherent in the unfiltered homotopy category.

(iii) Antipodal inversion satisfies
\[
\boxed{A_*o_x=(-1)^n o_{\bar x},\qquad o_{\bar x}=-o_x.}
\tag{8}
\]
Since \(o_{\bar x}=-o_x\) in the identical space \(Z_{\bar x}=Z_x\), the intrinsic degree of \(A:Z_x\to Z_x\) is \((-1)^{n+1}=(-1)^{n-1}\), as required for the antipodal sphere \(S^{n-2}\). The transport between antipodal roots instead has intrinsic degree \(-1\). These two maps have different homotopy classes precisely when \(n\) is odd.

*Proof.* Put \(m=n-1\). Integral Alexander duality in the oriented sphere gives natural isomorphisms
\[
\widetilde H_{m-1}(S^m\setminus (D\sqcup AD);\mathbb Z)
\cong \widetilde H^0(D\sqcup AD;\mathbb Z)
\tag{9}
\]
whenever \(D\) and \(AD\) are disjoint nonempty contractible compact polyhedra. The characteristic function of \(D\), considered modulo constant functions on the two components, is a generator of the group on the right.

For an edge \(xy\) of color \(a\), use \(D=B_{xy}^a\) in (9). The bridge and its antipode are disjoint contractible subpolyhedra, and \(B_{xy}^a\subseteq C_x\cap C_y\). Restriction of locally constant functions sends the characteristic functions of \(C_x\) and \(C_y\) to the characteristic function of \(B_{xy}^a\). Naturality of (9) therefore shows that both inclusions \(Z_x,Z_y\hookrightarrow Z_{xy}\) carry their distinguished homology generators to the same generator. This proves (i).

Theorem 3 makes both inclusions homotopy equivalences. Their homotopy inverse classes are unique, so an edge zigzag defines a homotopy class of equivalences \(Z_x\to Z_y\), and every composite along a walk takes \(o_x\) to \(o_y\). Since \(Z_x\) and \(Z_y\) have the homotopy type of \(S^{n-2}\), where \(n-2\ge1\), homotopy classes of maps \(Z_x\to Z_y\) are determined by their integer degree. Thus all root-walk composites with the same endpoints are homotopic. This proves (ii).

Finally, antipodal inversion has degree \((-1)^n\) on the ambient sphere \(S^{n-1}\), and interchanges the two components of \(C_x\sqcup AC_x\). The latter interchange negates the generator of reduced integral zeroth cohomology. Naturality of Alexander duality, including the ambient orientation degree, gives
\[
A_*o_x=(-1)^n o_{\bar x}.
\]
proving (iii). \(\square\)

**Theorem 5 (equivariant flatness).** Under the hypotheses of Theorem 4, any two bridge transports between the same roots are homotopic **through antipode-equivariant maps**. Thus all root squares commute in the equivariant homotopy category of unfiltered complements.

*Proof.* We first establish the equivariant Hopf-degree lemma: two antipode-equivariant maps \(f,g:S^k\to S^k\), \(k\ge1\), with equal integer degrees are equivariantly homotopic. For \(k=1\), the induced maps on the quotient circle have the same odd degree; a homotopy of quotient maps lifts with the prescribed initial lift.

For \(k\ge2\), the quotient maps \(\bar f,\bar g:\mathbb RP^k\to\mathbb RP^k\) both induce the identity on \(\pi_1\). As the universal covering sphere is \((k-1)\)-connected, their sole homotopy obstruction (with the action on \(\pi_1\) fixed) lies in
\[
H^k(\mathbb RP^k;\pi_k(S^k)_{\rm sign})
=H^k(\mathbb RP^k;\mathbb Z_{\rm or})\cong\mathbb Z.
\]
The deck action on \(\pi_k(S^k)\) is multiplication by \((-1)^{k+1}\), the orientation local system. Pullback to the double cover \(S^k\) sends this obstruction to \(\deg(f)-\deg(g)\). Pullback of the top twisted cohomology generator is twice the generator of \(H^k(S^k;\mathbb Z)\), and is injective. Therefore equal degrees annihilate the obstruction. The quotient homotopy lifts to an equivariant homotopy.

By Corollary 2, every \(Z_x\) is equivariantly homotopy equivalent to \(S^{n-2}\). Hence the lemma applies after such identifications. Theorem 4(i) proves that every bridge-walk composite sends the distinguished generator \(o_x\) to \(o_y\), so all composites with the same endpoints have degree \(+1\) under these identifications and are equivariantly homotopic. \(\square\)

**Remaining limitation.** Homotopy-category flatness does not select coherent higher homotopies or preserve the sets of dimensions used by witnesses and their switch filtrations. These remain the missing chain-level ingredients in a dimension-simple Wu--Yang modification.

**Filtration distinction.** The theorem supplies homotopy classes of transport maps and homotopy commutativity of their squares after forgetting dimension-support certificates. It does not construct specified square homotopies, compatible higher homotopies, or filtered chain maps. In particular, these ordinary homotopy classes cannot detect whether an edge prepended to a prefix repeats a dimension. The unresolved Wu–Yang adaptation lies in precisely that stronger coherent, dimension-simple lifting problem.

**The remaining task.** All monochromatic prefix witnesses remain dimension-simple. The construction gives an antipodally symmetric family of contractible carriers and root-changing sphere correspondences over the *entire cube graph*. Passing just to top homology loses dimension support, returning to the connected-component problem in Wu–Yang. A useful chain-map construction must retain the support filtration: a dimension \(i\) may be inserted into a prefix only when it is absent already. Compatible fillings of the mixed-color square exchange defects and higher cubical faces are unproved. This is the new central proof obligation, rather than another specialized coloring class.

**Theorem 6 (degree obstruction on compact models; noncompact fixed-point barrier).** Under the hypothetical absence of an at-most-one-switch full geodesic, let \(\gamma\) be any root walk from \(x\) to \(\bar x\), and let \(T_\gamma:Z_x\to Z_{\bar x}=Z_x\) be a representative of its equivariant bridge-transport class. Then
\[
\boxed{\deg T_\gamma=-1,\qquad \deg(A^{-1}T_\gamma)=(-1)^n.}
\tag{10}
\]
Transport \(f=A^{-1}T_\gamma\) through any equivariant homotopy equivalence \(Z_x\simeq_{\mathbb Z_2}S^{n-2}\) to a self-map \(\widetilde f:S^{n-2}\to S^{n-2}\). This compact-model map has
\[
\boxed{L(\widetilde f)=2.}
\tag{11}
\]
Thus \(\widetilde f\) has an antipodal pair of fixed points; after a generic equivariant perturbation the signed sum of fixed-point indices over antipodal pairs is \(1\).

*Proof.* From Theorem 4(i), \(T_{\gamma*}o_x=o_{\bar x}=-o_x\), proving the first degree. The intrinsic degree of \(A\) is \((-1)^{n-1}\) by corrected Theorem 4(iii), proving the second degree. Let \(k=n-2\). Equivariant homotopy equivalence preserves degree, so \(\deg\widetilde f=(-1)^n=(-1)^k\), and the compact sphere has Lefschetz number
\[
L(\widetilde f)=1+(-1)^k\deg\widetilde f=2.
\]
The Lefschetz fixed point theorem applies to the compact sphere. Equivariance pairs the fixed points; local indices in an antipodal pair agree by conjugation. A generic perturbation yields isolated nondegenerate fixed points, whose pairwise signed sum is therefore \(L/2=1\). \(\square\)

**Proposition 7 (sharp failure of the complement-level coincidence inference).** The degree and symmetry data in Theorem 6 do **not** force \(T_\gamma(z)=Az\) for a point \(z\) in the original open complement \(Z_x\). In fact there is an antipode-equivariant, fixed-point-free homotopy equivalence of the noncompact free antipodal space \(S^1\times\mathbb R\) with Lefschetz number \(2\).

*Proof.* Define the free involution \(A(s,t)=(-s,-t)\) on \(S^1\times\mathbb R\), where \(s=(s_1,s_2)\in S^1\), and let \(R(s_1,s_2)=(s_1,-s_2)\) be reflection. Define
\[
f(s,t)=(Rs,\ t+s_1).
\tag{12}
\]
Then \(fA=Af\), and \(f\) is a homeomorphism with inverse \(f^{-1}(s,t)=(Rs,t-s_1)\). It induces degree \(-1\) on \(H_1(S^1\times\mathbb R;\mathbb Z)\), so its alternating homology trace is \(L(f)=1-(-1)=2\). A fixed point would satisfy \(Rs=s\), which forces \(s=(1,0)\) or \((-1,0)\), and also \(t+s_1=t\), which requires \(s_1=0\). These conditions are incompatible. Finally \(T=Af\) is equivariant with degree \(-1\), while \(T(s,t)=A(s,t)\) would require \(f(s,t)=(s,t)\), which never occurs. \(\square\)

**Research consequence.** The degree and signed parity are valid invariants on compact equivariant sphere models, but moving a forced compact-model fixed point back to the original complement requires geometric control beyond a homotopy equivalence. This exposes a further necessary feature of a Wu--Yang adaptation: a compact, support-preserving carrier construction (or an alternative compactness/properness argument) is required before interpreting topological coincidences as dimension-simple geodesics.

**Proposition 8 (a color-independent countermodel for unfiltered transport).** For every \(n\ge3\), independently of any edge coloring, let
\[
S_x=\bigcup_{i=1}^n[x,x\oplus e_i]\subseteq\partial[0,1]^n
\]
be the cubical one-skeleton star at root \(x\). Then:

(i) Each \(S_x\) is a contractible cone, \(AS_x=S_{\bar x}\), and \(S_x\cap AS_x=\varnothing\).

(ii) For every cube edge \(xy\), the bridge \([x,y]\) lies in \(S_x\cap S_y\); the complement zigzag
\[
\partial I^n\setminus(S_x\cup AS_x)
\ \longrightarrow\
\partial I^n\setminus([x,y]\cup A[x,y])
\ \longleftarrow\
\partial I^n\setminus(S_y\cup AS_y)
\tag{13}
\]
consists of equivariant homotopy equivalences.

(iii) The integral generator transports, path-independence up to equivariant homotopy, and the antipodal signs in Theorems 4--5 hold for these stars, unchanged. Nevertheless the construction carries no edge-color information and has no monochromatic full-path certificate.

*Proof.* A star is a geometric tree with center \(x\), hence collapsible. Every vertex in the star has graph distance at most one from \(x\). Stars centered at antipodes have no common vertex for \(n\ge3\), since antipodal roots have distance \(n>2\); distinct cube edges meet geometrically only at common endpoints. Central inversion carries each incident edge to its antipodal image. For adjacent \(xy\), the common edge belongs to both stars. The two stars and the bridge, together with their antipodal images, are pairs of disjoint compact contractible polyhedra. Integral Alexander duality, as in Theorem 4, makes both complement inclusions in (13) integral homology equivalences. Each complement has the equivariant homotopy type of an antipodal \(S^{n-2}\), by the dimension-drop argument for collapsible carriers, so these maps are equivariant homotopy equivalences. The orientation and degree calculations of Theorems 4--5 require only these properties, proving (iii). No star contains a two-dimensional prefix simplex; the construction is independent of the coloring. \(\square\)

**Corollary 9 (the first color-sensitive distinction occurs at rank two).** For the star model, the union of corner carriers over any square \(F\) meets \(F\) in \(\partial F\) for every square coloring. In the monochromatic-prefix model, the same union fills \(F\) for patterns \(0000\) and \(0011\), and has nontrivial \(H_1\) for patterns \(0001\) and \(0101\), as proved in the rank-two square-carrier subsection of Article XIV. Thus the unfiltered transport axioms of Theorems 3--5 alone cannot imply NORI1 or any switch bound. A successful chain argument must use color-sensitive higher-incidence information absent from the star countermodel.

*Proof.* The union of stars at the four square corners consists of its four boundary edges. The prefix-carrier classification follows from the cited rank-two theorem. The same unfiltered axioms hold in both settings by Proposition 8; therefore those axioms alone cannot constrain the color words of complete paths. \(\square\)
