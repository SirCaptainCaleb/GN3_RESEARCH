# Projective square curvature and the antipodal exchange-disk identity

# Projective square curvature and antipodal exchange disks

Let \(n\ge3\), let \(B_n=\partial[0,1]^n\cong S^{n-1}\), and let \(\tau y=\mathbf1-y\) be central antipodality. Its quotient is \(Y_n=B_n/\tau\cong\mathbb{RP}^{n-1}\). Work with cubical cellular (co)chains over \(\mathbb F_2\). A legal NORI1 edge coloring is a one-cochain \(c\) with
\[
c(\tau e)=1+c(e)\qquad(e\text{ an undirected cube edge}).
\tag{1}
\]
Define its **square curvature** by \(\kappa=\delta c\):
\[
\kappa_{ij}(y)
=c_i(y)+c_j(y\oplus e_i)+c_i(y\oplus e_j)+c_j(y).
\tag{2}
\]
This depends only on the square, not the chosen corner. Since a square has four edges, \(\kappa(\tau F)=\kappa(F)\), so \(\kappa\) descends to a two-cocycle \(\bar\kappa\) on \(Y_n\).

**Theorem 1 (canonical antipodal exchange disk).** Let \(x\) be any cube vertex and \(\pi=(d_1,\ldots,d_n)\) any permutation. Let \(P=P(x,\pi)\) be the full antipodal geodesic, and concatenate it with its antipodal translate \(\tau P\). For \(i<j\), define \(F_{ij}(x,\pi)\) to be the two-face spanned by dimensions \(d_i,d_j\) with one corner
\[
q_{ij}=x\oplus\bigoplus_{k=i}^{j-1}e_{d_k}.
\tag{3}
\]
Then the two-chain
\[
\boxed{\Sigma_P=\sum_{1\le i<j\le n}F_{ij}(x,\pi)}
\tag{4}
\]
satisfies
\[
\boxed{\partial\Sigma_P=P+\tau P,}
\qquad
\boxed{\sum_{i<j}\kappa(F_{ij}(x,\pi))=n\pmod2.}
\tag{5}
\]

*Proof.* The closed walk \(P+\tau P\) has direction word \(d_1\cdots d_nd_1\cdots d_n\). Commute the second \(d_1\) left past \(d_n,\ldots,d_2\), then cancel the resulting consecutive pair \(d_1d_1\). Repeat for \(d_2,\ldots,d_n\). Each adjacent commutation is realized by one cubical square, and the commutation of the second \(d_i\) across \(d_j\) uses the face in (3). Each pair \(i<j\) is used once. The final walk is empty, so the boundary of their sum equals \(P+\tau P\), proving the first identity. Stokes' identity and antipodal oddness give
\[
\sum_{i<j}\kappa(F_{ij})=\langle c,P+\tau P\rangle
=\sum_{e\in P}(c(e)+c(\tau e))=n\pmod2.
\]
\(\square\)

The chain uses \(\binom n2\) squares, one for every unordered pair of dimensions. The identity holds for every dimension and every legal coloring; it was also checked independently on random colorings in dimensions \(3\) through \(7\).

**Theorem 2 (projective curvature class).** Let \(u\in H^1(\mathbb{RP}^{n-1};\mathbb F_2)\) be the standard generator. Then for every legal coloring,
\[
\boxed{[\bar\kappa]=(n\bmod2)u^2
\in H^2(\mathbb{RP}^{n-1};\mathbb F_2).}
\tag{6}
\]
In particular square curvature is an unavoidable nontrivial cohomology class on the antipodal quotient in odd dimension, but is a coboundary on that quotient in even dimension.

*Proof.* The quotient projection \(\pi:B_n\to Y_n\) sends the two copies of \(P\) to the same edge chain. Hence \(\pi_*\Sigma_P\) is a two-cycle. Theorem 1 implies
\[
\langle\bar\kappa,\pi_*\Sigma_P\rangle
=\langle\kappa,\Sigma_P\rangle=n\pmod2.
\]
For odd \(n\) the class is nonzero; the one-dimensional cohomology group \(H^2(\mathbb{RP}^{n-1};\mathbb F_2)\) has generator \(u^2\), proving (6).

For even \(n\), the legal coloring
\[
c_i^*(y)=\sum_{j\ne i}y_j
=\delta f(\{y,y\oplus e_i\}),\qquad
f(y)=\sum_{i<j}y_i y_j\pmod2
\tag{7}
\]
has zero square curvature. For any other legal coloring \(c\), the difference \(d=c+c^*\) is invariant under \(\tau\) and descends to a one-cochain \(\bar d\) on \(Y_n\). Therefore \(\bar\kappa=\delta\bar d\), proving the even case. \(\square\)

**Corollary 3 (classification of flat legal colorings).** A legal coloring satisfying \(\kappa=0\) exists **if and only if** \(n\) is even. For necessity, on the full contractible cube \(\kappa=0\) implies \(c=\delta f\). Put \(h(y)=f(y)+f(\tau y)\). Antipodal oddness yields \(h(y\oplus e_i)=h(y)+1\), so \(h(y)=h(0)+|y|\pmod2\). But \(h(\tau y)=h(y)\), requiring \(n\) even. Sufficiency is (7). Thus odd-dimensional antipodal colorings necessarily have curved squares, while even-dimensional legal flat colorings exist.

**Theorem 4 (red-blue monochromatic defect decomposition).** On a square, write the successive edge bits of its two increasing two-step routes as \((A,B)\) and \((C,D)\). Define the color-\(t\) exchange defect to be the parity of the number of routes that are monochromatic of color \(t\):
\[
\Omega_t=\mathbf1_{\{A=B=t\}}+\mathbf1_{\{C=D=t\}}\pmod2.
\]
Then
\[
\boxed{\Omega_0+\Omega_1=A+B+C+D=\kappa(F).}
\tag{8}
\]

*Proof.* Writing bits in \(\mathbb F_2\) gives \(\Omega_1=AB+CD\) and \(\Omega_0=(1+A)(1+B)+(1+C)(1+D)\). Their sum is \(A+B+C+D\). \(\square\)

By Theorem 1, every canonical antipodal exchange disk satisfies
\[
\boxed{\sum_{F\in\Sigma_P}(\Omega_0(F)+\Omega_1(F))=n\pmod2.}
\tag{9}
\]
For odd \(n\), this forces an odd number of squares where the two color-specific defects disagree. For even \(n\), the flat coloring (7) can nevertheless have \(\Omega_0=\Omega_1=1\) on individual squares, even though \(\kappa=0\): choose \(y_i\ne y_j\) and a suitable parity of the exterior bits. Thus ordinary square curvature and the path-order obstruction studied in Article XIV, Subsection 21, are independent phenomena.

**Corollary 5 (cup-product relation to the second-switch obstruction).** For odd \(n\ge5\), identify \(Y_n\) with the antipodal type-\(B_n\) Coxeter sphere quotient via radial projection. The primary obstruction to the signed-second-switch map, proved in Article XIV, Subsection 25, is \([o]=u^{n-2}\). Hence
\[
\boxed{[o]=u^{n-4}\smile[\bar\kappa].}
\tag{10}
\]
This is a cohomology identity, not a pointwise formula for the degrees of individual Coxeter residues. For even \(n\), \([\bar\kappa]=0\) while \([o]=u^{n-2}\ne0\), so no such factorization through ordinary square curvature is possible.

**Implications for Wu–Yang's dimension-simple chain repair.** Color-sensitive square defects cannot be dismissed as accidental errors: in odd dimensions their sum carries the forced class \(u^2\), and its cup power reproduces the high-rank second-switch obstruction. Simply demanding that all square defects vanish would exclude every odd-dimensional coloring. Conversely the flat even-dimensional example shows that correcting ordinary cubical curvature alone does not correct order-holonomy. A viable chain construction must account for both the projective curvature and the additional path-order information without losing the dimension-simple path geometry. Neither theorem proves NORI1, but they give a uniform cohomological constraint on any attempted correction.

## Theorem 6 (sharp square-curvature systole in every odd dimension)

For every odd \(n\ge3\), and every unrestricted antipodally odd binary coloring of the undirected cube edges, the number of two-dimensional cube faces with nonzero curvature satisfies
\[
\boxed{|\operatorname{supp}(\kappa)|\ge2^{n-2}.}
\tag{11}
\]
The bound is **attained** for every such \(n\). One extremal coloring has curvature supported entirely on the \(2^{n-2}\) squares spanned by any one chosen pair of dimensions.

*Proof of the bound.* There are \(2^n n!\) full rooted antipodal geodesic flags and \(N_2=\binom n2 2^{n-2}\) two-faces. For every flag \(P\), the exchange-disk theorem supplies a chain \(\Sigma_P\) containing precisely \(\binom n2\) distinct two-faces and satisfying \(\sum_{F\in\Sigma_P}\kappa(F)=1\) because \(n\) is odd. Thus every \(\Sigma_P\) meets \(\operatorname{supp}(\kappa)\).

The hyperoctahedral group acts transitively on cube two-faces and permutes the full geodesic flags and their exchange disks equivariantly. Each two-face therefore belongs to the same number \(r\) of exchange disks. Counting flag–face incidences gives
\[
r=\frac{(2^n n!)\binom n2}{\binom n2\,2^{n-2}}=4n!.
\]
Let \(M=|\operatorname{supp}(\kappa)|\). Double counting incidences between geodesic disks and curved faces yields
\[
2^n n!\le 4n!\,M,
\]
hence \(M\ge2^{n-2}\).

*Proof of attainment.* Choose two different dimensions \(a,b\in[n]\), and define the following edge coloring, with \(y\in\mathbb F_2^n\) denoting either endpoint of the specified edge:
\[
\boxed{
c_a(y)=\sum_{k\notin\{a,b\}}y_k\pmod2,\qquad
c_i(y)=y_a\quad (i\ne a).
}
\tag{12}
\]
Each \(c_i\) ignores the bit \(y_i\), so it defines an undirected-edge coloring. For \(i\ne a\), the antipode flips \(y_a\). For \(i=a\), the defining sum has \(n-2\) terms, an odd number, so antipodality also flips this color.

For a square in dimensions \(i,j\), its curvature is the sum of the cross-differences
\[
\kappa_{ij}=\Delta_j c_i+\Delta_i c_j.
\]
If neither dimension equals \(a\), both cross-differences vanish. If \(i=a\) and \(j\ne a\), then \(\Delta_a c_j=1\), whereas \(\Delta_j c_a=1\) for \(j\ne b\) and zero for \(j=b\). Consequently
\[
\boxed{\kappa_{ij}(y)=\mathbf1_{\{\{i,j\}=\{a,b\}\}}}
\quad\text{for every two-face.}
\tag{13}
\]
There are precisely \(2^{n-2}\) squares with free dimensions \(\{a,b\}\), so the construction attains (11). \(\square\)

**Corollary 7 (projective support minimum).** The projective two-cocycle \(\bar\kappa\) representing \(u^2\in H^2(\mathbb{RP}^{n-1};\mathbb F_2)\) has at least \(2^{n-3}\) nonzero antipodal two-face orbits, and this bound is attained by (12). Thus the cohomological square-curvature obstruction has an explicit minimal-support representative in the quotient cubical cellulation.

**Proof-search implication.** Odd-dimensional antipodal oddness forces many curved squares in absolute count, yet it is compatible with all those squares lying in one pair of dimensions. A proposed Wu–Yang correction that assumes curvature is distributed among many different dimension pairs cannot apply to the full NORI1 class. The all-dimensional lower bound and its concentrated extremizer are constraints on the incidence-based chain-map mechanism, not separate conjectures for a specialized coloring family.

## Theorem 8 (every antipodal exchange disk generates projective two-homology)

For **every** \(n\ge3\), including even dimensions, the projected canonical exchange disk
\[
Z_P=\pi_*\Sigma_P\in Z_2(Y_n;\mathbb F_2)
\]
represents the nonzero element of
\[
\boxed{H_2(\mathbb{RP}^{n-1};\mathbb F_2)\cong\mathbb F_2.}
\tag{16}
\]

Fix an unordered pair \(\{a,b\}\) of dimensions. Define a two-cochain \(K_{ab}\) on the cubical boundary \(B_n\) by setting \(K_{ab}(F)=1\) if \(F\) has free dimensions \(\{a,b\}\), and \(K_{ab}(F)=0\) otherwise. It is antipodally invariant and descends to \(\bar K_{ab}\in C^2(Y_n;\mathbb F_2)\). Then
\[
\boxed{\delta\bar K_{ab}=0,\qquad
[\bar K_{ab}]=u^2,\qquad
\langle\bar K_{ab},Z_P\rangle=1}
\tag{17}
\]
for every complete antipodal geodesic \(P\).

*Proof.* The canonical exchange chain \(\Sigma_P\) contains one face for each unordered pair of dimensions. Its projection is a cycle by Theorem 1. Every three-dimensional cubical face contains either no squares with free dimensions \(\{a,b\}\), or two opposite such squares. Thus \(\delta K_{ab}=0\), and the same holds after descent to the quotient. Since \(\Sigma_P\) contains one \(\{a,b\}\)-square,
\[
\langle\bar K_{ab},Z_P\rangle
=\langle K_{ab},\Sigma_P\rangle=1.
\]
Both \([\bar K_{ab}]\) and \([Z_P]\) are therefore nonzero. Their projective homology and cohomology groups have dimension one, with \(u^2\) generating cohomology. \(\square\)

**Corollary 9 (sharp projective two-cosystole).** For \(n\ge3\), every two-cocycle \(\eta\) representing \(u^2\) on the antipodal cubical quotient has at least
\[
\boxed{2^{n-3}}
\tag{18}
\]
antipodal two-face orbits in its support. The bound is attained by every \(\bar K_{ab}\). Equivalently, its invariant lift has at least \(2^{n-2}\) two-faces in its support upstairs.

*Proof.* Since \(Z_P\) generates homology, \(\langle\eta,Z_P\rangle=1\) for every full geodesic flag \(P\). Hence every canonical exchange disk contains an odd, and therefore positive, number of faces in the support of the lifted cocycle. There are \(2^n n!\) rooted full geodesic flags. By transitivity of the cube automorphism group, each two-face lies in \(4n!\) exchange disks: this follows by counting the \(\binom n2\) faces per flag among \(\binom n2 2^{n-2}\) two-faces. Double counting forces at least \(2^{n-2}\) supported faces, or \(2^{n-3}\) antipodal orbits. The cochain \(\bar K_{ab}\) has just those \(2^{n-3}\) orbits of \(\{a,b\}\)-squares. \(\square\)

**Corollary 10 (projective factorization in both parities).** For all \(n\ge5\), the universal primary obstruction \([o]=u^{n-2}\) of the signed-second-switch map from Subsection 25 satisfies
\[
\boxed{[o]=u^{n-4}\smile[\bar K_{ab}]}
\quad\text{for every dimension pair }\{a,b\}.
\tag{19}
\]
For odd \(n\), the color-curvature class \([\bar\kappa]\) also represents \(u^2\); for even \(n\), it is zero. Thus the projective generator can be realized by a single fixed-dimension-pair incidence cocycle regardless of parity, while the two color-specific square defects behave differently in odd and even dimension. These are cohomology identities and do not identify the individual residual Coxeter-cell degrees.

Theorem 8 provides a canonical all-dimensional homological interpretation of the antipodal exchange disks themselves, independent of coloring: each is a projective two-homology generator. This gives a fundamental family of two-cycles on which proposed rank-sensitive Wu–Yang correction chains can be tested before attempting high-dimensional fillings.

**Corollary 11 (exchange-disk rigidity at the sharp bound).** Let \(n\ge3\) and let \(\eta\) be a representative of \(u^2\) on the antipodal cubical quotient. If the invariant lifted support has the minimum size \(2^{n-2}\), then **every** complete antipodal geodesic's canonical exchange disk contains precisely one supported square:
\[
\boxed{
\left|\operatorname{supp}(\pi^*\eta)\cap
\{F_{ij}(x,\pi):1\le i<j\le n\}\right|=1
\quad\text{for all }x,\pi.
}
\tag{21}
\]
Conversely, this one-square-per-disk property implies the support has size \(2^{n-2}\).

*Proof.* Every projected disk is a two-homology generator, so its evaluation against \(\eta\) is one. Therefore it meets the lifted support in an odd positive number of faces. By transitivity, every cube two-face belongs to \(4n!\) of the \(2^n n!\) canonical exchange disks. With minimum support \(2^{n-2}\), the total number of support–disk incidences is
\[
(4n!)\,2^{n-2}=2^n n!,
\]
which is the number of disks. Each disk contributes at least one incidence, so each contributes precisely one. Conversely, double counting a family with one supported face per disk gives the asserted support size. \(\square\)

For odd-dimensional color curvature, this means every coloring attaining Theorem 6's lower bound has a perfect transversal property across the **entire collection of dimension-simple antipodal exchange disks**. The extremal coloring (12) realizes it by concentrating all curvature on one dimension pair. This rigidity is not a classification of all extremizers; showing whether other dimension-pair arrangements attain the same bound is a separate question and is not needed for the present theorem.
