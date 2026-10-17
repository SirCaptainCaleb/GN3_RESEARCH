## Central edge carriers and antipodal topology

### The full-geodesic color-profile span theorem for unrestricted NORI1

Let \(n\ge2\) and let \(c_i(u)\in\mathbb F_2\) be the color of the ** undirected** edge \(\{u,u\oplus e_i\}\) of the Boolean cube \(Q_n\). Assume the  NORI1 conditions
\[
c_i(u\oplus e_i)=c_i(u),\qquad
c_i(\bar u)=1\oplus c_i(u)
\tag{1}
\]
for every direction \(i\) and cube vertex \(u\). No linearity, locality, exterior-support, regularity, or direction-independence is assumed.

For a starting root \(u\in Q_n\) and a permutation \(p\) of all \(n\) directions, traverse the full antipodal geodesic in the order \(p\). Record its edge-color vector **indexed by original direction**, independently of the order in which those directions were used:
\[
w_i(u,p)=c_i\bigl(u\oplus\{p_j:j<p^{-1}(i)\}\bigr)
\quad(i=1,\ldots,n).
\tag{2}
\]
Write \(\mathcal W(c)=\{w(u,p):u\in Q_n,\ p\in S_n\}\subseteq\mathbb F_2^n\).

**Theorem (single-geodesic profile orbit and antipodal isometric cycle).** Fix any rooted full antipodal geodesic with direction order \(p=(p_1,\ldots,p_n)\) and direction-indexed color profile \(w\). Repeatedly move the first step of the geodesic to its end, shifting the starting vertex along that step. Let \(w^{(t)}\) be the profile after \(t\) such rotations. For \(0\le t\le n\),
\[
\boxed{w^{(t)}=w\oplus\sum_{j=1}^{t}e_{p_j},\qquad
w^{(n+t)}=\mathbf 1\oplus w^{(t)}\quad(0\le t\le n).}
\tag{RO1}
\]
For \(n\ge2\), the profiles \(w^{(0)},\ldots,w^{(2n-1)}\) are distinct and form an isometric cycle of length \(2n\) in the Hamming graph on \(\mathbb F_2^n\). The \(n+1\) consecutive profiles \(w^{(0)},\ldots,w^{(n)}\) are affinely independent. Furthermore, for any nonempty selected set \(S\) of \(k\) directions, the restrictions to \(S\) of this one orbit comprise precisely \(2k\) distinct profiles. Thus every realized profile belongs to such an isometric cycle, and the entire attainable profile set is a union of these cycles.

*Proof.* Write the initial path as \(v_0,v_1,\ldots,v_n=\bar v_0\), with first direction \(p_1\). After rotating the first step to the end, the new path is
\[
v_1,v_2,\ldots,v_n,\bar v_1.
\]
Its final edge is the antipodal translate of \(v_0v_1\), so that edge's color is complemented. Every other edge is unchanged. In direction-indexed notation this rotation replaces \(w\) by \(w\oplus e_{p_1}\) and cyclically shifts the direction order. Iteration proves (RO1), including the second half after the first \(n\) rotations have complemented all profile entries.

On the resulting cyclic list, any arc of \(d\le n\) steps toggles \(d\) distinct directions, so the Hamming distance between its endpoints is \(d\). An arc of length \(d\ge n\) has complementary arc of length \(2n-d\), toggling \(2n-d\) distinct directions; their Hamming distance is \(2n-d\). Thus the cycle is isometric and all its vertices are distinct. The consecutive differences among the first \(n+1\) profiles are \(e_{p_1},\ldots,e_{p_n}\), an \(\mathbb F_2\)-basis, proving affine independence. After restricting to \(S\), each direction in \(S\) occurs twice in the same cyclic order, and the resulting orbit contains \(2k\) distinct restricted profiles. \(\square\)

**Sharp limitation of orbit-cycle arguments.** For every \(n\ge3\), choose the base profile \(w=e_n\) and direction order
\[
p=(1,n,2,3,\ldots,n-1).
\]
The first \(n+1\) vertices of its profile-rotation cycle have Hamming weights \(1,2,1,2,\ldots,n-1\); the remaining vertices are their complements. Hence the resulting isometric \(2n\)-cycle avoids both \(0^n\) and \(\mathbf1\), while its affine span is all of \(\mathbb F_2^n\). Therefore affine spanning, antipodal closure, and the existence of isometric rotation cycles through every supported profile do not, without further compatibility between distinct full geodesics, force monochromatic profile attainment.

**Theorem (unrestricted full-profile affine span).**
\[
\boxed{\operatorname{aff}_{\mathbb F_2}\mathcal W(c)=\mathbb F_2^n.}
\tag{3}
\]
Equivalently, for every **nonempty set of directions** \(S\subseteq[n]\), the parity
\[
\bigoplus_{i\in S} w_i(u,p)
\]
assumes **both** binary values among full antipodal cube geodesics. Thus the attainable full-profile family obeys *no nontrivial universal affine parity identity* for any legal NORI1 coloring, even when the coloring is nonlinear.

**Proof.** By (RO1), the profiles from any one rotation orbit include an affine basis of \(\mathbb F_2^n\). \(\square\)

**Alternative square-cochain proof.** Suppose (3) fails. Linear algebra over \(\mathbb F_2\) supplies a nonzero vector \(y=(y_i)\in\mathbb F_2^n\) and a constant \(\kappa\) such that
\[
\bigoplus_i y_iw_i(u,p)=\kappa
\tag{4}
\]
for **every** root \(u\) and full direction permutation \(p\).

Give each  edge in direction \(i\) the mod-two weight
\[
\omega_i(u)=y_i c_i(u).
\tag{5}
\]
Because \(c_i\) is an undirected -edge color, \(\omega_i(u\oplus e_i)=\omega_i(u)\).

Fix any  square with corner \(u\) and distinct directions \(i,j\). Compare two full antipodal geodesics *from the same root* \(u\): the first starts with directions \((i,j)\), the second with \((j,i)\), and both use **the same order of all remaining directions**. They reach the same vertex after two moves, so every later  edge is identical. Subtracting the two instances of (4) therefore gives the  square-closedness equation
\[
\omega_i(u)\oplus\omega_j(u\oplus e_i)
\oplus\omega_j(u)\oplus\omega_i(u\oplus e_j)=0.
\tag{6}
\]
Every square is realized by such a pair of full geodesics; no based-window or abstract-face identification has been used.

Since every square has zero mod-two curvature, the edge cochain \(\omega\) is a gradient on the Boolean cube:
\[
\omega_i(u)=\phi(u)\oplus\phi(u\oplus e_i)
\tag{7}
\]
for some vertex potential \(\phi:Q_n\to\mathbb F_2\). For completeness, fix \(\phi(0)=0\), and define \(\phi(u)\) by integrating \(\omega\) along any cube path from \(0\) to \(u\). Any two such paths differ by backtrack cancellations and elementary square swaps;  edge invariance and (6) make their integrals equal. Thus (7) follows.

Every full antipodal geodesic telescopes under (7), so (4) implies
\[
\psi(u):=\phi(u)\oplus\phi(\bar u)=\kappa
\quad\text{for every }u.
\tag{8}
\]
But for every direction \(i\), the edge-gradient identity and **antipodal oddness** in (1) give
\[
\begin{aligned}
\psi(u\oplus e_i)\oplus\psi(u)
 &=\omega_i(u)\oplus\omega_i(\bar u)\\
 &= y_i\bigl(c_i(u)\oplus c_i(\bar u)\bigr)\\
 &=y_i.
\end{aligned}
\tag{9}
\]
Because \(\psi\) is constant, the left side is zero, forcing \(y_i=0\) for every \(i\), contrary to \(y\ne0\). This proves (3). \(\square\)

**Corollary (arbitrary prescribed colors on two directions).** Fix any **two distinct directions** \(i,j\) and any pair \((a,b)\in\mathbb F_2^2\). There exists a *full antipodal cube geodesic*, with some starting root and permutation of **all \(n\) directions**, whose edge in direction \(i\) has color \(a\) and whose edge in direction \(j\) has color \(b\).

**Proof.** Projection of (3) onto the \(i,j\) directions implies that the attainable pair-profile set has full affine span \(\mathbb F_2^2\). From (1), changing the root from \(u\) to \(\bar u\) while keeping the same direction order replaces every color \(w_i(u,p)\) by its complement. Hence the pair-profile set is closed under
\[
(a,b)\longmapsto(1\oplus a,1\oplus b).
\]
The only complement-invariant subset of \(\mathbb F_2^2\) with full affine span is the entire four-element set. \(\square\)

**Quantitative and constructive formulation.** Every legal coloring has at least \(n+1\) affinely independent realized direction-indexed full-geodesic profiles. For any prescribed nonzero functional \(y\), witnesses of opposite \(y\)-parity can be constructed by one of two edge-geometric mechanisms:

* If the weighted cochain \(\omega_i=y_ic_i\) has nonzero curvature on some square, the two full orders beginning with that square's directions in opposite orders give opposite \(y\)-parities at the same root.
* If every square has zero curvature, construct the potential \(\phi\) in (7), choose any \(i\) with \(y_i=1\), and use two full paths with the same direction order and roots differing by \(e_i\). Equation (9) shows their \(y\)-parities are opposite.

Thus the result is not merely an existential use of linear algebra: the proof isolates an explicit **adjacent-swap versus single-root-flip dichotomy** for every nonzero parity functional.

**Mathematical significance and  gap.** This theorem is a statement about **every** antipodally odd *-edge* NORI1 coloring. It establishes unrestricted two-direction prescription and excludes all affine-linear parity certificates for the nonattainment of full color words. These conclusions rely on global consistency of  square edges and antipodal oddness, rather than on affine formulas for the edge colors. They sharpen the partial-geodesic and restricted affine-family perspectives by identifying a global algebraic universality property that holds in the entire still-open class.

Full affine **span** of \(\mathcal W(c)\) does not imply \(\mathcal W(c)=\mathbb F_2^n\), nor that either constant vector \(0^n\) or \(1^n\) is attained. Full monochromatic NORI1 remains open. The precise missing implication is an additional *joint higher-order compatibility theorem* raising these independent parity separations and two-direction prescriptions to an all-direction word realization (or merely a monochromatic full word). The theorem also makes no claim about unrestricted ordinary boundary 3-tournaments; there the colored objects are ordered triples, and the square-gradient identity of  edges has no direct analogue.



#### First-direction Ward identity and full-profile tensorization

For a legal antipodally odd coloring of \(Q_n\), let \(w(x,\pi)\in\mathbb F_2^n\) record the colors indexed by direction on a rooted full geodesic. Write \(G_c(w)\) for its number of occurrences and \(G_{c,i}(w)\) for the number whose first direction is \(i\), counting starting vertices and permutations.

**Theorem (first-direction pairing).** For every \(i\) and \(w\),
\[
\boxed{G_{c,i}(w)=G_{c,i}(w\oplus e_i).}\tag{PW1}
\]
Equivalently, conditioned on the first direction being \(i\), its color is uniform and independent of the colors recorded for all remaining directions.

*Proof.* Map a geodesic
\[
(x,(i,a_2,\ldots,a_n))\longmapsto
(\overline{x\oplus e_i},(i,a_n,\ldots,a_2)).
\tag{PW2}
\]
The transformed first edge is antipodal to the original first edge and has opposite color. All subsequent edges are the original edges traversed in reverse, with unchanged colors. This transformation is an involution, preserving the first direction and toggling just the \(i\)-th profile bit. \(\square\)

Define the normalized directional-profile Walsh character
\[
\varphi_c(J)=\frac1{2^n n!}\sum_{(x,\pi)}
(-1)^{\sum_{j\in J}w_j(x,\pi)}
\qquad(J\subseteq[n]).
\]

**Corollary (high-degree Fourier suppression).**
\[
\boxed{
\varphi_c(J)=0\quad\text{for odd }|J|,\qquad
|\varphi_c(J)|\le\frac{n-|J|}{n}.
}\tag{PW3}
\]
In particular \(\varphi_c([n])=0\), and for a set of \(n-2\) directions its coefficient has magnitude at most \(2/n\) whenever that set has even cardinality.

*Proof.* Translating the starting vertex antipodally with the permutation unchanged complements all profile bits, forcing odd-cardinality characters to vanish. For every \(i\in J\), (PW1) cancels the contributions of all paths starting with \(i\). Only the fraction \((n-|J|)/n\) whose first direction lies outside \(J\) remains; the triangle inequality proves the bound. \(\square\)

**Theorem (direction-indexed profile product law).** Let \(c\boxtimes d\) color the independent Cartesian product \(Q_a\square Q_b\). Then for every pair of profile words \(u,v\),
\[
\boxed{
G_{c\boxtimes d}(u,v)=
\binom{a+b}{a}G_c(u)G_d(v),\qquad
\mathcal W(c\boxtimes d)=\mathcal W(c)\times\mathcal W(d).
}\tag{PW4}
\]
The normalized full-profile probability laws tensorize.

*Proof.* A product geodesic consists uniquely of one rooted full geodesic in each block and an interleaving of their direction orders. Every interleaving yields the same two indexed profile words, and there are \(\binom{a+b}{a}\) choices. \(\square\)

**Theorem (dimension-uniform Hartley-support closure criterion).** Subject to the previously established counterexample-preserving reduction to balanced even-dimensional legal colorings, unrestricted NORI1 is equivalent to the uniform asymptotic estimate
\[
\boxed{|\mathcal W(c)|\ge2^{\,n-o(n)}
\quad\text{for all balanced legal colorings of }Q_n.}\tag{PW5}
\]
It is also equivalent to \(\mathcal W(c)=\mathbb F_2^n\) for every legal coloring.

*Proof.* If NORI1 holds, given a legal coloring \(c\) and any desired profile \(u\), reverse all edge colors in each direction with \(u_i=1\). This preserves legality. A monochromatic-zero full geodesic of the recolored cube has profile \(u\) in the original cube; a monochromatic-one full geodesic can first be antipodally translated to color zero. Hence all profile words occur.

Conversely if NORI1 fails, a balanced counterexample \(c\) exists in some fixed even dimension \(d\). The zero word is missing, so \(s=|\mathcal W(c)|<2^d\). Its \(h\)-fold Cartesian product is again balanced and legal. The product law gives \(|\mathcal W(c^{\boxtimes h})|=s^h\). Writing \(n=hd\), this is \(2^{n\log_2(s)/d}\), contradicting (PW5), since \(\log_2(s)/d<1\) is fixed. \(\square\)

**Why Shannon entropy cannot replace support entropy.** Consider the legal balanced successful \(Q_4\) coloring
\[
c_0=x_2,\qquad c_1=1-x_2,\qquad
c_2=x_0,\qquad c_3=1-x_0.
\tag{PW6}
\]
Direct enumeration of its \(16\cdot4!=384\) rooted full geodesics gives \(G_c(0000)=8\) and \(G_c(0101)=40\), whereas a uniform distribution would give \(24\) occurrences per word. Its Shannon profile entropy therefore satisfies \(H_1(c)<4\). The probability-product law yields \(H_1(c^{\boxtimes h})=hH_1(c)\), a linear entropy deficit for arbitrarily large balanced legal cubes that already have monochromatic antipodal geodesics. Thus a universal Shannon-entropy estimate \(H_1(c)\ge n-o(n)\) is false; the profile-support/Hartley condition (PW5) remains closure-equivalent.

The Ward identity (PW1) and Fourier bound (PW3) hold for all legal colorings, including nonlinear and nonbalanced examples. Neither bound alone forces full profile support. They isolate a dimension-uniform direction-sensitive constraint beyond affine spanning and three-direction prescription.



##### Formal six-direction obstruction to profile-only closure

The first-direction pairing (PW1), odd-character vanishing, high-degree bounds (PW3), complement symmetry, full affine span, three-direction surjectivity, and even the scalar quadratic noise-moment bounds (NM3) do not by themselves force the zero word. The following is a formal integer-valued **profile-count model**, with no claim that a legal cube coloring realizes it.

For each \(i\in[6]\) and \(w\in\mathbb F_2^6\), define
\[
\boxed{
M_i(w)=
\begin{cases}
128,&w|_{[6]\setminus\{i\}}\text{ contains both bit values},\\
0,&\text{otherwise}.
\end{cases}
\qquad M(w)=\sum_{i=1}^6M_i(w).
}\tag{FA1}
\]
Each \(M_i\) totals \(128\cdot 2(2^5-2)=7680=2^6(5!)\), the number of rooted six-direction orders starting with \(i\). It obeys \(M_i(w)=M_i(w\oplus e_i)\), precisely the first-direction Ward pairing. The aggregate \(M\) is complement-invariant, equals zero on \(0^6,1^6\), equals \(640\) on words of weights one or five, and equals \(768\) on weights two, three, or four. Consequently
\[
\boxed{
\sum_wM(w)=2^6 6!=46080,\qquad
(g_0,\ldots,g_6)=(0,3840,11520,15360,11520,3840,0).
}\tag{FA2}
\]
Its support comprises all sixty-two nonconstant six-bit words; it has full affine span and projects onto all eight patterns for every chosen triple of directions. The Ward proof of (PW3) applies verbatim to these formal integer counts, hence every Fourier inequality there holds.

Using the noise-trace expression (NT2), the formal trace polynomial is
\[
\boxed{
F_{\rm formal}(t)=720-480t^2-240t^4
=240(1-t^2)(3+t^2).
}\tag{FA3}
\]
The quadratic coefficient \(-480\) lies inside the legal balanced dimension-six interval from (NM3), namely \([-720,-432]\). Thus even adding that **scalar** balanced Fourier-energy bound does not exclude this formal countermodel. In particular, its missing zero profile is compatible with positivity of the trace polynomial throughout \(-1<t<1\) and simple endpoint vanishing. This is a countermodel to a proposed proof using only these aggregate identities; it is not an NORI1 counterexample and is not asserted to satisfy the edge-rule realization equations (QR1)--(QR3).

The family persists in every dimension \(6h\): define its product profile counts by the multinomial version of (PW4). The profile support has cardinality \(62^h\), and its normalized noise trace is
\[
\boxed{
\frac{F_{\rm formal}^{(h)}(t)}{(6h)!}
=\left(1-\frac23t^2-\frac13t^4\right)^h.
}\tag{FA4}
\]
The resulting normalized quadratic coefficient is \(-2h/3=-n/9\), which stays within the balanced bound \([-n/6,-n/(2(n-1))]\) for every \(n=6h\ge6\). First-direction Ward pairings are preserved by the multinomial product: for a first direction in block \(a\), select a first-direction profile count \(M_i\) in that block and aggregate profile counts in the others, multiplying by the number of direction-order interleavings having that first direction. Complement symmetry, three-direction surjectivity and full affine span persist under products. Hence this obstruction is dimension-uniform and identifies an indispensable missing ingredient: consistency of the abstract profile counts with original undirected Boolean edge functions and their square-exchange relations.

The construction rules out using (PW1)--(PW5) and the scalar quadratic-moment interval alone as a proof of NORI1; the intrinsically cubical Boolean constraints remain decisive.



##### Polynomial profile-cycle countermodels to bounded-marginal closure

**Theorem (formal constraint separation).** Fix \(k\ge1\) and \(0<\eta<1/4\). For all sufficiently large \(n\), there are a set \(W\subseteq\mathbb F_2^n\), a probability law \(\mu\) supported positively on \(W\), and nonnegative rational functions \(G_i\) such that
\[
0^n,1^n\notin W,\quad W=1^n+W,\quad |W|=O_{k,\eta}(n^3\log n).
\tag{FA5}
\]
The induced graph \(Q_n[W]\) is two-vertex-connected; every \(w\in W\) belongs to an antipodally invariant isometric \(2n\)-cycle in \(W\), so \(W\) has full affine span. Moreover, extending \(G_i\) by zero outside \(W\),
\[
\boxed{\mu(w)=\sum_iG_i(w),\quad G_i(w)=G_i(w+e_i),\quad\sum_wG_i(w)=1/n,}
\tag{FA6}
\]
and, writing \(Y_i=(-1)^{w_i}\),
\[
\boxed{\mathbb E_\mu Y=0,\quad
\mathbb E_\mu(YY^{\mathsf T})\succeq(1-\eta)I_n,\quad
\bigl|\mu(w|_I=a)-2^{-|I|}\bigr|\le\eta 2^{-|I|}}
\tag{FA7}
\]
for every \(I\subseteq[n]\) of size at most \(k\) and every \(a\in\mathbb F_2^I\). The formal first-direction counts \(G_i\) satisfy the Ward identity (PW1), the odd-character cancellation, and \(|\varphi(J)|\le(n-|J|)/n\) as in (PW3). Thus these profile-only constraints, even with seven-direction saturation, the covariance inequality (FM4), and two-vertex-connected profile support, permit both constant words to be absent.

*Proof.* Given \(u\in\mathbb F_2^n\) and a direction permutation \(\pi\), let \(\Gamma(u,\pi)\) be the isometric \(2n\)-cycle with vertices
\[
u+\sum_{j\le t}e_{\pi_j},\quad 1^n+u+\sum_{j\le t}e_{\pi_j}\qquad(0\le t<n).
\]
It is invariant under complementation and has two edges of every direction. Independently sample \(T=\lceil C_{k,\eta}n^2\log n\rceil\) cycles with uniform \(u,\pi\), and average their uniform vertex measures to obtain \(\mu_0\). For any \(I,a\), one cycle's mass on \(w|_I=a\) belongs to \([0,1]\) with mean \(2^{-|I|}\). For \(i\ne j\), its signed correlation \(Y_iY_j\) has mean zero, since translating \(u\) by \(e_i\) reverses its sign. Hoeffding's inequality, a union bound over \(O_k(n^k)\) marginal events and \(O(n^2)\) correlations, and sufficiently large \(C_{k,\eta}\) give simultaneously
\[
\bigl|\mu_0(w|_I=a)-2^{-|I|}\bigr|\le(\eta/2)2^{-|I|},\qquad
\bigl|\mathbb E_{\mu_0}Y_iY_j\bigr|\le\eta/[2(n-1)].
\]
Gershgorin's inequality then gives \(\mathbb E_{\mu_0}(YY^{\mathsf T})\succeq(1-\eta/2)I_n\). One sampled cycle hits \(0^n\), equivalently \(1^n\), with probability \(2n/2^n\); the probability any sampled cycle hits either is at most \(2nT/2^n=o(1)\). Fix a sample satisfying the displayed estimates and avoiding both constant profiles.

For \(n\ge3\), any two nonconstant vertices \(a,b\) have a shortest cube path avoiding both poles \(0^n,1^n\). If neither pole lies in their monotone interval, this is immediate. If one lies there, first flip a dimension whose bit initially agrees with that pole and ends disagreeing; thereafter the pole cannot appear. If both lie there, then \(b=\bar a\); first flip one zero bit of \(a\) and then one one bit, keeping both poles inaccessible. Apply this lemma to \(a\to b\) and \(b\to\bar a\): the two shortest paths use disjoint direction sets and concatenate into an antipodal geodesic avoiding the poles. Its antipodal translate completes an isometric \(2n\)-cycle through \(a,b,\bar a,\bar b\).

Choose a vertex \(a\) of the first sampled cycle. For each remaining sampled cycle, choose a vertex \(b\) and add such a connecting cycle through \(a,\bar a,b,\bar b\). Their union \(W\) contains at most \(2n(2T-1)\) vertices. Consecutively attach each connecting cycle and its target sampled cycle. Both attachments share two vertices; the union of two two-vertex-connected graphs sharing two vertices stays two-vertex-connected. Therefore the induced graph \(Q_n[W]\) is two-vertex-connected. Every contained cycle has an affine basis of \(n+1\) vertices.

Let \(\mu_{\rm br}\) average the uniform measures of the added cycles, and set \(\mu=(1-\delta)\mu_0+\delta\mu_{\rm br}\), where \(\delta=\eta2^{-k-2}\). This measure is positive on all of \(W\), complement invariant, and rational. Its marginal error is at most \((\eta/2)2^{-|I|}+\delta\le\eta2^{-|I|}\). Both component covariance matrices are positive semidefinite, and so
\[
\mathbb E_\mu(YY^{\mathsf T})\succeq(1-\delta)(1-\eta/2)I_n\succeq(1-\eta)I_n.
\]

Write \(\mu\) as a rational convex combination of uniform cycle measures with coefficients \(\alpha_\Gamma\). Define \(G_i(w)\) by adding \(\alpha_\Gamma/(4n)\) for each incidence at \(w\) of a direction-\(i\) edge of \(\Gamma\). Every cycle vertex has two incident edges, every cycle has two direction-\(i\) edges, and each such edge joins \(w,w+e_i\). These facts give (FA6). For each \(i\in J\), the \(G_i\)-weighted Walsh sum cancels on opposite endpoints of direction-\(i\) edges. The remaining \(n-|J|\) classes have total mass \((n-|J|)/n\), proving (PW3). Complementation cancels all odd moments. \(\square\)

**Scope.** The profiles and rational incidence counts are abstract; no antipodally odd undirected edge coloring is asserted to realize them. Cross-order square-exchange compatibility with a shared edge coloring is therefore an indispensable additional condition for a closure argument using these profile statistics.


##### Additive missing-neighbor profile boundary

For a legal coloring \(c\) on \(Q_n\), let \(W=\mathcal W(c)\), let \(d_W(w)=|\{i:w+e_i\notin W\}|\), and define
\[
b(c)=|W|^{-1}\sum_{w\in W}d_W(w),\qquad r(c)=\max_{w\in W}d_W(w).
\tag{BN1}
\]
**Theorem.** For independent Cartesian factors \(c,d\),
\[
\boxed{b(c\boxtimes d)=b(c)+b(d),\quad r(c\boxtimes d)=r(c)+r(d).}\tag{BN2}
\]
Consequently unrestricted NORI1 is equivalent to either universal bound \(b(c)=o(n)\) or \(r(c)=o(n)\), uniformly over legal colorings of dimension \(n\). It remains equivalent if only balanced legal colorings of even dimension are tested. Furthermore
\[
\boxed{n-\log_2|W|\le b(c)\le r(c).}\tag{BN3}
\]
*Proof.* The profile product law gives \(W(c\boxtimes d)=W(c)\times W(d)\). Missing-neighbor counts add pointwise across the two direction blocks. Taking averages and maxima proves (BN2). If NORI1 holds, direction-wise recoloring realizes every profile and both defects vanish. If a counterexample exists, its nonempty proper support \(W\) has a cube boundary edge, so \(b(c),r(c)>0\). In the \(h\)-fold product these quantities grow linearly with \(h\), contradicting either uniform sublinear bound. The paired-balanced lift preserves badness, establishing the balanced variant. The cube edge-isoperimetric inequality \(|\partial W|\ge|W|\log_2(2^n/|W|)\) proves (BN3). \(\square\)

Every boundary edge \(w\in W,\ w+e_i\notin W\) gives, by recoloring directions according to \(w+e_i\), a legal coloring without constant profiles whose path corresponding to \(w\) has a single minority edge in direction \(i\). Thus \(b(c)\) measures one-defect gauge obstructions averaged over realizable profiles. The sublinear-neighborhood criterion calls for a dimension-uniform exchange mechanism moving between profiles along almost every one-bit direction.


##### VC shattering as a dimension-uniform closure criterion

For a legal coloring \(c\) of \(Q_n\), call a direction set \(T\subseteq[n]\) *profile-shattered* when
\[
\mathcal W(c)|_T=\mathbb F_2^T,
\]
so every binary prescription on \(T\) occurs along some full antipodal geodesic (with unconstrained colors outside \(T\)). Let \(v(c)\) be the maximum cardinality of a profile-shattered direction set.

**Theorem (VC additivity and grand-theorem equivalence).** For independent legal colorings \(c\) of \(Q_a\) and \(d\) of \(Q_b\),
\[
\boxed{v(c\boxtimes d)=v(c)+v(d).}\tag{VC1}
\]
Assuming the established badness-preserving reduction to balanced even dimensions, each of the following conditions is equivalent to unrestricted NORI1:

1. There is \(f(n)=o(n)\) such that \(v(c)\ge n-f(n)\) for every balanced legal \(c\) of \(Q_n\) and all even \(n\).
2. There is a dimension-independent constant \(C\) such that \(v(c)\ge n-C\) for every such \(c\).
3. Every legal \(c\) has \(v(c)=n\).

*Proof.* By the Cartesian profile support law (PW4), projection of \(\mathcal W(c\boxtimes d)\) onto a direction set \(T=T_a\sqcup T_b\) equals \((\mathcal W(c)|_{T_a})\times(\mathcal W(d)|_{T_b})\). It is surjective precisely when both factor projections are, proving (VC1).

If NORI1 holds, every legal coloring has the full profile set by the direction-gauge argument in (PW5), so \(v(c)=n\) and all three conditions follow. Conversely suppose NORI1 fails. The balanced reduction supplies a bad balanced legal \(c\) in some fixed even dimension \(d\). Since the all-zero profile is absent, the full direction set is not shattered and \(v(c)\le d-1\). Its \(h\)-fold Cartesian power is balanced and legal, and (VC1) gives
\[
v(c^{\boxtimes h})=h\,v(c)\le h(d-1)=hd-h.
\]
The linear deficit \(h\) contradicts either a uniform \(o(n)\) deficit or any fixed bound \(C\) as \(h\to\infty\). The three conditions are therefore equivalent. \(\square\)

**Proof target.** A universal *almost-spanning profile-shattering theorem*, even with a deficit \(O(\sqrt n)\), \(O(\log n)\), or a fixed constant, would close unrestricted NORI1. Such a theorem concerns one large direction set whose prescribed colors can all be realized, and might admit Hall-type or rainbow-path exchange methods. The seven-direction prescription theorem in Article VIII, proved through the unrestricted arbitrary-edge-coloring 2-cp bridge equivalence and the known finite geodesic results, supplies \(v(c)\ge\min(n,7)\) in every dimension. This substantially strengthens the baseline three-direction theorem; obtaining a bound with deficit \(o(n)\) remains open. This avoids an endless sequence of fixed-dimensional or fixed-size prescription theorems.

The formal models (FA1)--(FA4) illustrate why the deficit is essential: their profile support in each six-direction block omits two constant words and has VC dimension five; the \(h\)-block formal product has VC dimension \(5h\), with a linear deficit. They satisfy the profile-only identities but are not asserted to be realized by legal cube matrices.


#### Logarithmic profile-support deficit and a closure-equivalent approximation

For a legal antipodally odd coloring \(c\) of \(Q_n\), let \(\mathcal W(c)\subseteq\mathbb F_2^n\) be its direction-indexed color profiles on full antipodal geodesics. Define
\[
\Delta_0(c)=n-\log_2|\mathcal W(c)|.
\tag{SE1}
\]
The deficit vanishes precisely when every binary profile occurs.

**Theorem (sublinear support-deficit closure criterion).** Unrestricted NORI1 is equivalent to each assertion:
(i) There is \(f(n)=o(n)\) such that \(\Delta_0(c)\le f(n)\) for all legal \(Q_n\) colorings.
(ii) There is a dimension-independent constant \(C\) such that \(\Delta_0(c)\le C\) for all legal colorings.
(iii) There is \(\varepsilon>0\) such that \(|\mathcal W(c)|\ge\varepsilon 2^n\) for all legal colorings.
The equivalences remain true with (i)--(iii) restricted to balanced legal colorings in even dimension.

*Proof.* Under NORI1 every profile \(b\) occurs: complement all colors in directions with \(b_i=1\), find a monochromatic full geodesic, and, if its color is one, shift the root antipodally without changing its direction order. Undoing the direction complements realizes \(b\), so \(\Delta_0=0\).

Conversely, if NORI1 fails, choose \(c\) of \(Q_d\) lacking a zero full geodesic. Its profile support omits \(0^d\), hence \(\delta=\Delta_0(c)>0\). The Cartesian profile product law (PW4) yields
\[
\mathcal W(c^{\boxtimes h})=\mathcal W(c)^h,\qquad
\boxed{\Delta_0(c^{\boxtimes h})=h\delta.}
\tag{SE2}
\]
Its dimension \(N=hd\) gives deficit \((\delta/d)N\), contradicting (i). Assertion (ii) implies (i), and (iii) implies (ii) with \(C=\log_2(1/\varepsilon)\). For the balanced-only variant, first apply the established counterexample-preserving balanced lift; tensor powers preserve balance. \(\square\)

**Comparison with the existing shattering criterion.** If \(v(c)\) is the maximum cardinality of a direction set whose profile projection is surjective, then \(v(c)\le\log_2|\mathcal W(c)|\). The established near-spanning VC-shattering closure criterion therefore implies the support criterion. The support criterion merely asks for \(|\mathcal W(c)|\ge 2^{n-o(n)}\), regardless of whether any large direction set is shattered. This is a logically weaker approximate theorem whose proof would settle unrestricted NORI1. The lower bound itself remains unproved.



##### A second-order-precise pseudorandom profile model with missing constant words

The six-direction formal obstruction (FA1)--(FA4) can be substantially strengthened. In every \(n\ge3\), define purely formal nonnegative integer path-profile counts indexed by first direction \(i\in[n]\) and full binary profile \(w\in\mathbb F_2^n\):
\[
\boxed{
M_i(w)=4(n-3)!\,r_i(w)\bigl(n-1-r_i(w)\bigr),
\quad r_i(w)=\sum_{j\ne i}w_j,
\qquad M(w)=\sum_iM_i(w).
}\tag{FX1}
\]
As before, this is an abstract profile-count construction; no claim is made that a legal cube-edge coloring realizes it.

**Theorem (precise counts and Fourier truncation).** The model (FX1) has the correct first-direction geodesic totals, first-direction Ward symmetry, antipodal complement symmetry, and full prescribed-profile support except for the two constant words:
\[
\boxed{
\sum_wM_i(w)=2^n(n-1)!,\quad
M_i(w)=M_i(w\oplus e_i),\quad
M(w)=4(n-2)!\,|w|(n-|w|),
}\tag{FX2}
\]
\[
\boxed{
\operatorname{supp}M=\mathbb F_2^n\setminus\{0^n,1^n\},
\qquad v(M)=n-1.
}\tag{FX3}
\]
The formal rooted-path color-count distribution and noise trace are
\[
\boxed{
g_k=4n!\binom{n-2}{k-1}\quad(1\le k\le n-1),\qquad
g_0=g_n=0,\qquad F_{\rm formal}(t)=n!(1-t^2).
}\tag{FX4}
\]
Let \(X_i=(-1)^{w_i}\) under the normalized law \(M(w)/(2^n n!)\). Every nonempty Fourier coefficient of degree four or greater vanishes:
\[
\boxed{
\mathbb E\prod_{i\in J}X_i=
\begin{cases}
-2/[n(n-1)],&|J|=2,\\
0,&|J|\ne2,\ J\ne\varnothing.
\end{cases}
}\tag{FX5}
\]
Its signed-color covariance has
\[
\boxed{
C_{ii}=1,\qquad C_{ij}=-\frac{2}{n(n-1)}\ (i\ne j),
\qquad
\lambda_{\min}(C)=1-\frac2n.
}\tag{FX6}
\]
Thus for every \(n\ge6\) it obeys the **sharp universal legal-cube inequality** \(C\succeq(2/3)I\), including equality at \(n=6\). For every even \(n\ge6\) it also obeys the balanced quadratic-moment interval (NM3), and its covariance admits the same abstract positive-semidefinite/zero-row-sum splitting as (AG2)--(AG4), with
\[
\boxed{q_i=2/n,\qquad L=\frac2{n-1}\left(I-\frac1n\mathbf1\mathbf1^{\mathsf T}\right)\succeq0,\quad L\mathbf1=0.}\tag{FX7}
\]

*Proof.* For fixed \(i\), each choice of the \(n-1\) other bits with \(r\) ones has two possible bits in direction \(i\). The binomial identity
\[
\sum_{r=0}^{N}\binom Nr r(N-r)=N(N-1)2^{N-2}
\]
with \(N=n-1\) gives \(\sum_wM_i(w)=2^n(n-1)!\). The formula is independent of \(w_i\), proving first-direction Ward pairing. For a word with \(k\) one-bits, there are \(k\) indices with \(r_i=k-1\) and \(n-k\) with \(r_i=k\), so
\[
M(w)=4(n-3)!\left[k(k-1)(n-k)+(n-k)k(n-1-k)\right]
=4(n-2)!\,k(n-k).
\]
This proves (FX2)--(FX3) and complement symmetry. The identity
\[
\binom nk\,k(n-k)=n(n-1)\binom{n-2}{k-1}
\]
gives the values \(g_k\). With \(p=(1+t)/2,q=(1-t)/2\), the formal noise-trace/Bernstein calculation yields
\[
F_{\rm formal}(t)=4n!pq\sum_{k=1}^{n-1}\binom{n-2}{k-1}p^{n-1-k}q^{k-1}
=4n!pq(p+q)^{n-2}=n!(1-t^2).
\]
The law of \(w\) is invariant under every direction permutation, so its Fourier character average depends only on \(|J|\). In the identity
\[
F_{\rm formal}(t)/n!=\mathbb E\prod_i(1+tX_i)
=\sum_{j=0}^n t^j\sum_{|J|=j}\mathbb E\prod_{i\in J}X_i,
\]
the coefficient of \(t^j\) is \(\binom nj\) times the common \(j\)-character moment. Formula (FX4) gives (FX5). Equation (FX6) follows because the equicorrelation matrix has eigenvalues \(1-2/n\) along \(\mathbf1\) and \(1+2/[n(n-1)]\) on its orthogonal complement. Finally (FX7) is direct matrix arithmetic, and \([t^2]F_{\rm formal}=-n!\) is between the balanced endpoints \(-nn!/6\) and \(-nn!/[2(n-1)]\) whenever \(n\ge6\). \(\square\)

**Proposition (arbitrarily accurate uniformity with an absent monochromatic profile).** Let \(U_n\) denote the uniform distribution on \(\mathbb F_2^n\), and let \(\mu_n(w)=M(w)/(2^n n!)\). Then
\[
\boxed{
\mu_n(w)=2^{-n}\left[1+\frac{n-(\sum_i(-1)^{w_i})^2}{n(n-1)}\right],
\qquad
\|\mu_n-U_n\|_{\rm TV}\le\frac1{\sqrt{2n(n-1)}}.
}\tag{FX8}
\]
In particular \(\|\mu_n-U_n\|_{\rm TV}=O(1/n)\to0\), even though \(\mu_n(0^n)=\mu_n(1^n)=0\) for every \(n\).

*Proof.* Writing \(k=|w|\), the signed sum is \(n-2k\), so
\(n^2-(n-2k)^2=4k(n-k)\); substitution in (FX2) gives the first formula. Under \(U_n\), the independent symmetric Rademacher sum \(S=\sum_i(-1)^{w_i}\) satisfies \(\mathbb ES^2=n\) and \(\operatorname{Var}(S^2)=2n(n-1)\). Hence
\[
\|\mu_n-U_n\|_{\rm TV}
=\frac{\mathbb E_{U_n}|S^2-n|}{2n(n-1)}
\le\frac{\sqrt{2n(n-1)}}{2n(n-1)}.
\]
Both constant words have zero mass by direct substitution. \(\square\)

**Grand-closure significance.** The models (FX1)--(FX8) satisfy substantially more aggregate conditions than (FA1)--(FA4): precise first-direction Ward pairing, correct populations, all proper-direction prescriptions, zero higher-order *direction-indexed* Fourier moments, the sharp universal covariance inequality, the balanced second-moment interval, and profile laws converging to uniform in total variation. Their full noise traces even have weak alternating-sign coefficients and no positive interior zero. Yet they omit both monochromatic profiles. Any complete NORI1 argument must use structural consistency of the edge functions, relative square exchanges, or other  cubical constraints not encoded by these formal profile statistics. This does not constitute a counterexample to NORI1, because no realization of these formal counts by underlying cube-edge rules is asserted.


#### Rooted affine profile geometry and autonomous flat blocks

Let \(\mathcal W_x=\{w(x,\pi):\pi\in S_n\}\). Define
\[
v_{ij}(u)=\partial_jc_i(u)e_i+\partial_ic_j(u)e_j,\qquad
V=\operatorname{span}_{\mathbb F_2}\{v_{ij}(u):i\ne j,\ u\in Q_n\}.
\]
All derivatives and vector sums in this section are binary.

**Theorem (rooted affine cosets).** Choose any order \(\pi_0\) and put \(a=w(0,\pi_0)\). Then
\[
\boxed{\operatorname{aff}\mathcal W_x=x+a+V\quad(x\in Q_n).}\tag{RA1}
\]
This result was established in research note note_019945e5faa732f94a3e1fce; its proof is included to support the structural refinements below.

*Proof.* Exchanging consecutive steps \(i,j\), after a prefix ending at \(u\), changes the profile by \(v_{ij}(u)\). Adjacent exchanges connect all orders, so the difference span of \(\mathcal W_x\) is contained in \(V\). Conversely \(v_{ij}(u)\) ignores bits \(i,j\). At any fixed root \(x\), place before \(i,j\) the subset of other directions on which \(x\) and \(u\) differ. The two orders exchanging \(i,j\) realize this generator at root \(x\). Thus the difference span equals \(V\).

For \(y\in V^\perp\), the weighted edge cochain \(\omega_i=y_ic_i\) has zero sum on every square, hence is a gradient \(\delta\phi\). Set \(\psi(x)=\phi(x)+\phi(\bar x)\). Oddness gives \(\partial_i\psi=y_i\), so \(\psi(x)=\psi(0)+y\cdot x\). Integrating along full paths gives
\(y\cdot w(x,\pi)=y\cdot a+y\cdot x\).
These identities determine the affine translate of \(V\), proving (RA1). \(\square\)

Construct a graph \(J\) on the directions. Join \(i,j\) if some square satisfies
\(\partial_jc_i=\partial_ic_j=1\). Mark \(i\) if some square satisfies
\(\partial_jc_i=1,\ \partial_ic_j=0\).
Call a component of \(J\) unmarked when none of its vertices is marked. Denote these components by \(C_1,\ldots,C_t\).

**Theorem (classification of all rooted affine restrictions).**
\[
\boxed{
V^\perp=\operatorname{span}\{\mathbf1_{C_1},\ldots,\mathbf1_{C_t}\},
\qquad \dim V=n-t.
}\tag{RA2}
\]
Each \(C_\ell\) has positive even size, its direction rules depend only on bits in \(C_\ell\), and all its internal squares have zero color curvature. Consequently the complete list of rooted affine restrictions is
\[
\boxed{
\sum_{i\in C_\ell}w_i
=\sum_{i\in C_\ell}x_i+\sum_{i\in C_\ell}a_i
\quad(1\le\ell\le t).
}\tag{RA3}
\]

*Proof.* The generators of \(V\) are precisely zero vectors, unit vectors at marked vertices, and vectors \(e_i+e_j\) on edges of \(J\). Within a connected component, edge vectors span the even-weight subspace; adjoining any marked unit vector gives the full space on that component. This proves (RA2).

If \(i\in C_\ell\), \(j\notin C_\ell\), and \(\partial_jc_i=1\) somewhere, the reverse derivative is either zero, marking \(i\), or one, joining the components. Both are impossible. Thus \(c_i\) ignores every bit outside \(C_\ell\). For internal \(i,j\), unequal derivatives would mark one of them. Their derivatives agree on every square, proving flatness.

An isolated unmarked vertex would have a constant direction rule, contrary to antipodal oddness, so every such component has at least two vertices. On a flat component of size \(k\), integrate its coloring to a vertex potential \(\phi\). Oddness implies
\[
\phi(z)+\phi(\bar z)=|z|+\alpha.
\]
The left side is antipodally invariant; replacing \(z\) by \(\bar z\) on the right forces \(k\) even. Formula (RA3) follows from (RA1)--(RA2). \(\square\)

The autonomy assertion concerns incoming dependencies: other direction rules may read bits in these flat blocks.

**Lemma (a flat odd block has nonzero degree imbalance).** A flat legal odd coloring of an even \(k\)-cube cannot be vertex-balanced. Its signed degree sum
\[
R(z)=\sum_{i=1}^k(-1)^{c_i(z)}
\]
therefore has \(\max_zR(z)\ge2\).

*Proof.* Write \(c=\delta\phi\), and let \(s(z)=(-1)^{\phi(z)}\). If \(R\) vanished everywhere, the cube adjacency operator \(A\) would satisfy \(As=0\), because
\((As)(z)=s(z)R(z)\).
On a Walsh character indexed by \(S\), \(A\) has eigenvalue \(k-2|S|\). Thus \(s\) would be supported only on Walsh level \(k/2\), implying
\(s(\bar z)=(-1)^{k/2}s(z)\).
But the potential identity above gives
\(s(\bar z)=(-1)^\alpha(-1)^{|z|}s(z)\),
a contradiction as vertex parity varies. Hence \(R\) is nonzero. It is even-valued and satisfies \(R(\bar z)=-R(z)\), yielding the claimed positive maximum. \(\square\)

**Theorem (sharp balanced rooted affine rank).** Every vertex-balanced legal coloring satisfies, at every root,
\[
\boxed{\dim\operatorname{aff}\mathcal W_x\ge\lceil3n/4\rceil.}\tag{RA4}
\]
More precisely, let \(p\) be the number of directions outside the unmarked components, and let
\(M_\ell=\max R_{C_\ell}\). Then
\[
\boxed{\sum_{\ell=1}^tM_\ell\le p,\qquad
2t\le p,\qquad 4t\le n.}\tag{RA5}
\]

*Proof.* Each flat block is autonomous, so choose its bits independently to attain \(M_\ell\ge2\). At that combined assignment, balance requires the signed sum over the remaining \(p\) rules to be \(-\sum_\ell M_\ell\). Its magnitude is at most \(p\), proving the first two inequalities. The flat blocks contain at least \(2t\) directions in total, so \(n\ge p+2t\ge4t\). Now apply \(\dim V=n-t\). \(\square\)

**Sharpness in every even dimension \(n\ge4\).** On \(Q_4\), take
\[
(c_0,c_1,c_2,c_3)=(x_1,x_0,1+x_1,1+x_0).
\]
It is balanced and legal. Its exchange space is
\(\operatorname{span}\{e_0+e_1,e_2,e_3\}\), of dimension three.
On \(Q_6\), put \(P=x_1+x_2+x_3\) and take
\[
(c_0,c_1,c_2,c_3,c_4,c_5)
=(P,x_0,x_0,1+x_0,1+P,1+x_0).
\]
This is balanced and legal, with one unmarked flat block \(\{0,1,2,3\}\) and two marked singleton components. Its exchange space has dimension five. Independent Cartesian products add exchange-space dimensions, so copies of the \(Q_4\) example, with one \(Q_6\) example when \(n\equiv2\pmod4\), attain \(\lceil3n/4\rceil\).

**Affine-admissible roots.** Both constant profiles belong to the same rooted affine coset, because every \(C_\ell\) has even size. The roots whose affine hull contains them form the coset \(a+V\), of size
\[
\boxed{2^{n-t}\ge2^{\lceil3n/4\rceil}\quad\text{in the balanced case}.}\tag{RA6}
\]
Attainment of a constant profile requires further compatibility among the exchange witnesses.

**Audit and proof-search implication.** Enumeration of all legal \(Q_4\) colorings finds precisely 48 balanced colorings; each has rooted affine rank three at every root. Enumeration of all roots and orders of the displayed \(Q_6\) example confirms rank five. The proofs are dimension-uniform and independent of these checks.

All linear restrictions on a fixed root's profiles are now accounted for by autonomous flat source blocks, with the imbalance budget (RA5). Closing NORI1 requires controlling holes within these affine cosets. The classification identifies the relevant global exchange problem: different square exchanges realize the generators of \(V\) at a root, while their combined realizability as one direction order remains to be established.


##### General rank and uniform quotient distribution

The classification also gives the sharp unrestricted estimate
\[
\boxed{\dim V\ge\lceil n/2\rceil.}\tag{RA8}
\]
Each unmarked component has at least two vertices, so \(t\le\lfloor n/2\rfloor\). Sharpness for even \(n\) is attained by independent pairs with rules \(c_a=x_b,c_b=x_a\). For odd \(n=2m+3\), append to \(m\) such pairs the three-direction factor
\((c_0,c_1,c_2)=(x_2,x_2,x_1)\), whose exchange space is \(\operatorname{span}\{e_0,e_1+e_2\}\).

For uniform \(X\), every choice of order \(\Pi\), including an order selected as a function of \(X\), satisfies
\[
w(X,\Pi)+V=X+a+V.
\]
Thus the profile quotient \(\mathbb F_2^n/V\) is uniform. The earlier note's exhaustive \(Q_4\) audit gives rooted ranks \(2,3,4\) with frequencies \(768,100096,947712\), respectively, among \(65536\) legal colorings times sixteen roots. These statements and the canonical-block classification consolidate the overlapping contributions published concurrently with (RA1)--(RA6).

##### Affine deficit persists under balanced reader lifts

For the standard complementary lift \(L(c)\) on \(Q_{2n}\), retain the old rules \(c_i(x)\) and give new direction \(n+i\) the rule \(1+c_i(x)\). Then
\[
\boxed{V_{L(c)}=V_c\oplus\mathbb F_2^n,\qquad
2n-\dim V_{L(c)}=n-\dim V_c.}\tag{RA7}
\]

*Proof.* Old-old exchange generators are unchanged. Old rules ignore every new bit, while new rules read only old bits. Thus old-new generators are either zero or unit vectors on new directions, and all new-new generators vanish. Each new rule is nonconstant by oddness, so some old derivative supplies its unit vector. This proves the direct-sum identity. In the graph classification, the original unmarked flat blocks persist and all new directions are marked singleton components. \(\square\)

After \(r\) lifts the dimension is \(N=2^rn\), and every rooted affine profile hull has dimension \(N-t\), with the original number \(t\) unchanged. The established rootwise reader-extension identity also gives
\(\mathcal W_{L^r(c)}(x,y)=\mathcal W_c(x)\times\mathbb F_2^{N-n}\).
Thus any forbidden original profile persists despite rooted affine rank approaching the full ambient dimension. This reinforces the distinction between affine-coset classification and attainment of individual profiles: the remaining question is the compatibility of exchanges within a coset.


##### Sharp Fourier second moment of full-geodesic color imbalance

Let \(c\) be any antipodally odd binary coloring of the undirected edges of \(Q_n\), with \(n\ge2\). Write \(F_i(x)=(-1)^{c_i(x)}\), and, for \(T\subseteq[n]\), write \(\chi_T(x)=(-1)^{\sum_{j\in T}x_j}\) and
\[
a_{i,T}=2^{-n}\sum_{x\in Q_n}F_i(x)\chi_T(x).
\]
Thus \(a_{i,T}=0\) unless \(|T|\) is odd and \(i\notin T\). For a root \(x\) and a direction permutation \(\pi\), let
\[
Z(x,\pi)=\sum_{k=1}^n F_{\pi_k}\!\left(x+\sum_{\ell<k}e_{\pi_\ell}\right).
\]
This is the number of color-zero edges minus the number of color-one edges on the full geodesic.

**Theorem (Fourier second-moment identity and sharp lower bound).** For independent uniformly chosen \(x\in Q_n\) and \(\pi\in S_n\),
\[
\boxed{
\mathbb E Z(x,\pi)^2
=\sum_{\substack{T\subseteq[n]\\ |T|\ {\rm odd}}}
\left[
\frac{|T|+1}{|T|+2}\sum_{i\notin T}a_{i,T}^{\,2}
+\frac1{|T|+2}\left(\sum_{i\notin T}a_{i,T}\right)^2
\right]
\ge \frac{2n}{3}.}
\tag{FM1}
\]
Consequently some full antipodal geodesic has at least
\[
\boxed{\frac n2+\sqrt{\frac n6}}
\tag{FM2}
\]
edges of one color. Its antipodal translate gives the analogous assertion for the other color. The coefficient \(2/3\) in (FM1) is optimal in arbitrarily large dimensions: equality is attained for every \(n\) divisible by four.

*Proof.* For a prefix set \(S_i(\pi)=\{\pi_\ell:\ell<\pi^{-1}(i)\}\), Fourier expansion gives
\[
Z(x,\pi)=\sum_T\chi_T(x)
       \sum_{i\notin T}a_{i,T}(-1)^{|T\cap S_i(\pi)|}.
\]
Orthogonality of the characters under uniform \(x\) removes all mixed terms with distinct \(T\). For distinct \(i,j\notin T\), put \(t=|T|\). The product of their two prefix signs is \((-1)^K\), where \(K\) is the number of members of \(T\) strictly between \(i\) and \(j\) in the permutation. Among the \(\binom{t+2}{2}\) unordered placements of \(i,j\) relative to the members of \(T\), precisely \(t+1-k\) have \(K=k\). Because \(t\) is odd,
\[
\mathbb E_\pi (-1)^K
=\frac{\sum_{k=0}^t(-1)^k(t+1-k)}{\binom{t+2}{2}}
=\frac1{t+2}.
\]
The diagonal correlations equal one. Expanding the square and separating the diagonal therefore gives (FM1). Since \(t\ge1\), its first coefficient is at least \(2/3\), and the second term is nonnegative. Parseval and \(F_i(x)^2=1\) yield \(\sum_Ta_{i,T}^2=1\) for each \(i\), so the lower bound is \(2n/3\). Some path has \(|Z|\ge\sqrt{2n/3}\), proving (FM2).

For sharpness, partition the dimensions into four-element blocks \((a,b,c,d)\), and in each block set
\[
F_a=\chi_{\{b\}},\qquad F_b=\chi_{\{a\}},\qquad
F_c=-\chi_{\{a\}},\qquad F_d=-\chi_{\{b\}}.
\]
These rules ignore their own direction bits and change sign under antipodality, hence define a legal coloring. All nonzero Fourier supports are singletons. For each such support \(T\), the nonzero coefficients \(a_{i,T}\) sum to zero: the two occurrences have opposite signs. The second term of (FM1) vanishes, and its first coefficient equals \(2/3\) throughout. Consequently \(\mathbb E Z^2=2n/3\), as asserted. \(\square\)

The identity quantifies a universal imbalance of complete color profiles, including colorings with arbitrarily many nonlinear direction rules. It does not imply the \(n-o(n)\) single-color edge count that would settle unrestricted NORI1 by independent-product amplification.


##### Minority-count additivity and a weak closure-equivalent asymptotic target

For a legal antipodally odd edge coloring \(c\) of \(Q_n\), define
\[
m(c)=\min_{P\ {\rm full\ antipodal\ geodesic}}\min\{N_0(P),N_1(P)\},
\]
where \(N_s(P)\) counts edges of color \(s\) on \(P\). In particular \(m(c)=0\) if and only if \(c\) has a monochromatic full antipodal geodesic.

**Theorem (additivity of the minority defect).** If \(c\) and \(d\) are legal antipodally odd colorings of \(Q_a\) and \(Q_b\), then
\[
\boxed{m(c\boxtimes d)=m(c)+m(d).}
\tag{FM3}
\]
Consequently the unrestricted NORI1 conjecture is equivalent to either of the following assertions:

(i) There is a function \(\varepsilon(n)\to0\) such that every legal coloring of \(Q_n\) has a full antipodal geodesic with at most \(\varepsilon(n)n\) edges of its minority color.

(ii) For every \(\delta>0\), in all sufficiently large dimensions every legal coloring has a full antipodal geodesic with at least \((1-\delta)n\) edges of one color, without any restriction on their positions or on the number of switches.

*Proof.* Any full product geodesic projects onto a full antipodal geodesic in each factor. Every such factor geodesic has at least \(m(c)\), respectively \(m(d)\), edges of **each** color. Hence each color occurs at least \(m(c)+m(d)\) times in the product path, proving the lower bound in (FM3).

For the reverse inequality, choose a geodesic in each factor realizing its minority defect. Replacing one factor root by its antipode and keeping the direction order complements its full color word, so both paths can be chosen with color zero as the minority color. Concatenate these independent factor geodesics. It has \(m(c)+m(d)\) zero edges and \(a+b-m(c)-m(d)\) one edges. As \(m(c)\le a/2\) and \(m(d)\le b/2\), zero is a minority color, proving equality.

NORI1 immediately implies (i)--(ii) with zero minority count. Conversely, suppose a legal counterexample \(c\) existed on \(Q_d\), so \(m(c)\ge1\). Its \(h\)-fold independent Cartesian product remains legal, and (FM3) gives
\[
m(c^{\boxtimes h})=h\,m(c),\qquad
\frac{m(c^{\boxtimes h})}{hd}=\frac{m(c)}d>0.
\]
This contradicts either uniform asymptotic assertion as \(h\to\infty\). The two assertions express the same uniform minority-fraction conclusion. \(\square\)

The asymptotic target here allows arbitrarily many switches and uses full antipodal geodesics; it is formally weaker than a requirement for a nearly spanning one-switch geodesic. The sharp second-moment bound (FM1), which guarantees minority count at most \(n/2-\sqrt{n/6}\), does not achieve the vanishing minority fraction in (i).


##### Spectator extensions preserve full-path minority defect

Let \(c\) be a legal antipodally odd edge coloring of \(Q_m\), and let \(g_1,\ldots,g_k:Q_m\to\mathbb F_2\) satisfy \(g_j(\bar x)=1\oplus g_j(x)\). Define an extension \(C\) on \(Q_m\times Q_k\) by
\[
C_i(x,y)=c_i(x)\ (1\le i\le m),\qquad
C_{m+j}(x,y)=g_j(x)\ (1\le j\le k).
\tag{SM1}
\]
Let \(m(c)\) be the minimum, over full antipodal geodesics of \(c\), of the smaller of their two color counts, as defined above.

**Theorem (spectator-cylinder and minority invariance).** The extension \(C\) is legal and
\[
\boxed{\mathcal W(C)=\mathcal W(c)\times\mathbb F_2^k,\qquad
m(C)=m(c).}
\tag{SM2}
\]
Consequently \(\Delta_0(C)=\Delta_0(c)\) and \(v(C)=v(c)+k\).

*Proof.* Edge consistency holds because the old rules and each new rule are independent of the new vertex bits; deck oddness is inherited from \(c\) and the functions \(g_j\). Projecting any full geodesic of \(C\) onto the old dimensions gives a full geodesic of \(c\) with the same old profile. Conversely, fix an old full geodesic from \(x\) to \(\bar x\) with direction-indexed profile \(w\). For any prescribed new profile \(b\), place dimension \(m+j\) before that path if \(g_j(x)=b_j\), and after it otherwise. At the terminal old vertex its color is \(g_j(\bar x)=1\oplus g_j(x)=b_j\). All new steps are mutually color-independent, and do not modify old colors. Thus every \((w,b)\) occurs, proving the profile product identity.

For every full profile of \(c\), both of its color counts are at least \(m(c)\); adjoining arbitrary new bits cannot reduce either count. Hence \(m(C)\ge m(c)\). Choose an old path achieving \(m(c)\), and set every new profile bit to the old majority color. The minority count remains \(m(c)\), giving the reverse inequality. The support-deficit and shattering equalities follow from the Cartesian product of the profile supports. \(\square\)

**Corollary (minority invariance under balanced paired lifts).** For every \(r\ge1\), the iterated paired lift \(L^r(c)\), of dimension \(N=2^rm\), is balanced and legal and satisfies
\[
\boxed{m(L^r(c))=m(c),\qquad
\mathcal W(L^r(c))=\mathcal W(c)\times\mathbb F_2^{N-m},\qquad
v(L^r(c))=N-m+v(c).}
\tag{SM3}
\]
Therefore a hypothetical counterexample has balanced counterexample lifts in arbitrarily large dimensions with a full antipodal geodesic using only \(m(c)=O(1)\) edges of its minority color and shattering all but \(m-v(c)=O(1)\) directions.

*Proof.* The usual paired lift has \(g_i(x)=1\oplus c_i(x)\). Apply (SM2) at each iteration. Opposite colors within each pair give vertex balance. The geodesic-existence equivalence follows because \(m=0\) is equivalent to monochromatic full-geodesic existence. \(\square\)

**Corollary (essential reader condition).** In a minimum-dimensional counterexample, each vertex bit is read by some direction rule other than its own.

*Proof.* If bit \(j\) is read by none of the other rules, delete dimension \(j\); the remaining rules define a legal coloring \(d\) of \(Q_{n-1}\), and the deleted rule is an odd function \(g\) on that smaller cube. The original coloring has the extension form (SM1), so \(m(d)=m(c)>0\), contradicting minimality. \(\square\)

This identity separates Cartesian-product amplification, which multiplies the minority defect, from paired balancing, which preserves it. Thus bounds asserted only along repeated balancing of a fixed coloring cannot force the vanishing minority defect needed for the unrestricted conjecture.


##### Uniform covariance gap and quantitative triple-profile saturation

Keep the signed Walsh coefficients \(a_{i,T}\) and the random full antipodal geodesic \((x,\pi)\) of (FM1). Write \(Y_i=F_i(x+\sum_{\ell<\pi^{-1}(i)}e_{\pi_\ell})\). Simultaneously replacing \(x\) by its antipode negates all \(Y_i\), so every odd joint moment vanishes, including \(\mathbb E Y_i=0\).

**Theorem (full-profile covariance lower bound).** For every \(w\in\mathbb R^n\),
\[
\boxed{\mathbb E(w\cdot Y)^2\ge\tfrac23\|w\|_2^2.}\tag{FM4}
\]
Thus \(\operatorname{Cov}(Y)\succeq(2/3)I_n\). This inequality is sharp at \(n=4\).

*Proof.* The argument for (FM1), with \(a_{i,T}\) replaced by \(w_ia_{i,T}\), gives
\[
\mathbb E(w\cdot Y)^2=
\sum_{\substack{T\subseteq[n]\\|T|\ {\rm odd}}}
\left[
\frac{|T|+1}{|T|+2}\sum_{i\notin T}w_i^2a_{i,T}^2
+\frac1{|T|+2}\left(\sum_{i\notin T}w_ia_{i,T}\right)^2
\right]\ge\tfrac23\sum_iw_i^2
\]
by Parseval. For the four-direction block following (FM2), take weights \(w_a=w_d=1\) and \(w_b=w_c=0\). The only common Walsh support of the two nonzero weighted rules is \(\{b\}\), their coefficients are opposite, and equality holds. \(\square\)

**Theorem (uniform probabilities for prescribed short color profiles).** For fixed \(I\subseteq[n]\) with \(1\le|I|\le3\), and any \(\eta\in\{-1,1\}^I\),
\[
\boxed{\Pr(Y_i=\eta_i\text{ for all }i\in I)\ge
\begin{cases}
1/2,&|I|=1,\\
1/6,&|I|=2,\\
1/16,&|I|=3.
\end{cases}}\tag{FM5}
\]
Consequently every prescription on three specified directions is attained by at least \(2^nn!/16\) rooted ordered full antipodal geodesics.

*Proof.* For distinct \(i,j\), the relative-order calculation of (FM1) yields
\[
\rho_{ij}=\mathbb E(Y_iY_j)
=\sum_{|T|\ {\rm odd}}\frac{a_{i,T}a_{j,T}}{|T|+2}.
\]
Cauchy--Schwarz and Parseval give \(|\rho_{ij}|\le1/3\). All odd joint moments vanish by antipodal symmetry, so the singleton probability is \(1/2\), and the pair probability \((1+\eta_i\eta_j\rho_{ij})/4\) is at least \(1/6\).

For three indices \(I\), put \(b_{r,T}=\eta_ra_{r,T}\), taking \(a_{r,T}=0\) if \(r\in T\). The signed pair-correlation sum satisfies
\[
\begin{aligned}
R&=\sum_{\{r,s\}\subseteq I}\eta_r\eta_s\rho_{rs}\\
&=\sum_{|T|\ {\rm odd}}
\frac{\bigl(\sum_{r\in I}b_{r,T}\bigr)^2-\sum_{r\in I}b_{r,T}^2}{2(|T|+2)}\\
&\ge-\frac16\sum_{r\in I,T}a_{r,T}^2=-\frac12.
\end{aligned}
\]
Expanding the product of three indicator functions and dropping the vanishing odd moments proves \(\Pr(Y_r=\eta_r\ \forall r\in I)=(1+R)/8\ge1/16\). \(\square\)

This quantitative strengthening of known three-direction existential saturation holds for every legal coloring, with arbitrarily many nonlinear direction rules. It does not imply attainability of prescriptions on an unbounded number of directions or the vanishing minority fraction of (FM3).


##### Global minority extremizers: cyclic ballot corridors and monochromatic faces

Let \(c\) be a legal antipodally odd coloring of \(Q_n\). For a rooted ordered full geodesic \(P=(v_0,\ldots,v_n)\), write \(s_k=1-2c(v_{k-1}v_k)\in\{-1,1\}\), its signed color sum \(Z(P)=\sum_{k=1}^n s_k\), and \(S_k=\sum_{\ell=1}^ks_\ell\), with \(S_0=0\).

**Theorem (ballot corridor of a global extremizer).** Suppose \(P\) maximizes \(Z\) among all rooted ordered full geodesics in \(Q_n\), and put \(M=Z(P)=n-2m(c)\). Then
\[
\boxed{0\le S_k\le M\qquad(0\le k\le n).}\tag{EX1}
\]
In particular, when \(M>0\), the first and last edges of every such maximizer have color zero. Moreover, the cyclic shift of \(P\) across its first \(k\) edges is a full geodesic \(P_k\) with
\[
Z(P_k)=M-2S_k.
\tag{EX2}
\]

*Proof.* Let \(\pi=(i_1,\ldots,i_n)\) be the direction order, so \(v_k=v_0+\sum_{\ell\le k}e_{i_\ell}\). The cyclically shifted path
\[
v_k,v_{k+1},\ldots,v_n,\overline{v_1},\ldots,\overline{v_k}
\]
uses the order \((i_{k+1},\ldots,i_n,i_1,\ldots,i_k)\) and joins antipodal vertices. Its first \(n-k\) edges agree with the suffix of \(P\), while its last \(k\) edges are the antipodal translates of the first \(k\) edges of \(P\). Antipodal oddness reverses their signs, yielding (EX2). Global optimality gives \(M-2S_k\le M\), hence \(S_k\ge0\).

The reversed path from \(v_n\) to \(v_0\) has the same signed sum \(M\) and is again globally optimal. Applying the lower-prefix inequality to this reversed path gives \(M-S_k\ge0\). This proves (EX1). Since \(s_1=S_1\ge0\) and \(s_n=M-S_{n-1}\ge0\), both endpoint signs equal \(+1\). \(\square\)

**Theorem (minority-run face rigidity).** Let \(f\) be an arbitrary binary coloring of the undirected edges of \(Q_n\), without antipodal hypotheses. Suppose \(P\) maximizes its number of color-zero edges among all full antipodal geodesics. If \(r\ge2\) successive edges of \(P\) have color one, with direction set \(B\) and starting vertex \(v\), then **every edge of the \(r\)-face**
\[
F(v,B)=\{v+\sum_{i\in S}e_i:S\subseteq B\}
\]
has color one. Every permutation of those \(r\) steps, with the remainder of \(P\) unchanged, is therefore also globally optimal. In a legal antipodally odd coloring, the antipodal face \(\overline{F(v,B)}\) is entirely color zero.

*Proof.* If two consecutive color-one steps in directions \(i,j\) traverse \(v'\to v'+e_i\to v'+e_i+e_j\), the reversed square route traverses \(v'\to v'+e_j\to v'+e_i+e_j\). Changing only these two steps leaves all other edges of the full geodesic unchanged. If either replacement edge had color zero, the replacement path would contain more color-zero edges than \(P\), contradicting maximality. Both replacement edges must consequently have color one, and the swapped full path is another maximizer.

The adjacent-transposition graph of permutations of \(B\) is connected. Inductively applying the preceding argument to any adjacent color-one pair shows that every ordering of \(B\) yields only color-one edges in the same face and preserves the maximum. Every edge of \(F(v,B)\) occurs on a monotone geodesic from \(v\) to \(v+\sum_{i\in B}e_i\), obtained by ordering the dimensions in its initial subset before its direction and the remaining dimensions after. Therefore every edge of the face has color one. Antipodal oddness makes every edge of its antipodal face color zero. \(\square\)

Together these results give necessary conditions on every global minority-defect minimizer in a hypothetical unrestricted counterexample, regardless of nonlinear rule complexity. They do not rule out isolated minority edges or eliminate the possibility that all minority runs span monochromatic faces.


##### One-defect normalization of every hypothetical counterexample

For a legal antipodally odd edge coloring \(c\) of \(Q_n\), let \(\mathcal W(c)\subseteq\mathbb F_2^n\) be its set of direction-indexed full-geodesic color profiles. For \(t\in\mathbb F_2^n\), define the *direction recoloring*
\[
c_i^t(x)=c_i(x)\oplus t_i.
\tag{GD1}
\]
Recoloring preserves edge consistency and antipodal oddness. It translates the profile set:
\[
\boxed{\mathcal W(c^t)=\mathcal W(c)\oplus t.}
\tag{GD2}
\]
The profile set is invariant under full complementation, because translating the starting vertex antipodally complements every edge color while leaving the direction order fixed.

**Theorem (profile distance equals recolored minority defect).** With the full-geodesic minority count \(m\) of (FM3), for every legal \(c\) and every \(t\in\mathbb F_2^n\),
\[
\boxed{m(c^t)=\min_{w\in\mathcal W(c)}d_H(t,w).}
\tag{GD3}
\]
In particular, \(c^t\) is a counterexample precisely when \(t\notin\mathcal W(c)\).

*Proof.* For an original profile \(w\), its recolored word is \(w\oplus t\), whose two color counts are \(d_H(t,w)\) and \(n-d_H(t,w)\). Since \(\mathcal W(c)\) is closed under \(w\mapsto w\oplus\mathbf1\), the minimum of the second count over all profiles equals the minimum of the first. Minimizing their smaller value gives (GD3). The all-zero word is realized after recoloring precisely when \(t\in\mathcal W(c)\); the all-one word occurs under the same condition by complementation symmetry. \(\square\)

**Theorem (unrestricted one-defect counterexample normal form).** If unrestricted NORI1 is false, then in a dimension where a counterexample exists there is also a legal counterexample \(b\) having a full antipodal geodesic with precisely one edge of color one and all its other edges of color zero. Thus
\[
\boxed{m(b)=1.}
\tag{GD4}
\]
The exceptional edge necessarily occurs strictly between the first and last edges of every such geodesic. Moreover, a dimension-minimal counterexample can be selected with these properties. Its standard paired lift is a vertex-balanced counterexample with the same one-minority profile.

*Proof.* Let \(c\) be any counterexample, so \(\varnothing\ne\mathcal W(c)\subsetneq\mathbb F_2^n\). The binary Hamming graph is connected; therefore a realized profile \(w\in\mathcal W(c)\) and an unrealized profile \(t\notin\mathcal W(c)\) exist with \(d_H(w,t)=1\). Set \(b=c^t\). By (GD3), the missing target makes \(b\) a counterexample, while the geodesic realizing \(w\) now has profile \(w\oplus t=e_i\) for some direction \(i\). Hence \(m(b)=1\).

If its one-color-one edge were the first step of the geodesic, apply the root slide: move the starting vertex across this first edge, move its direction to the end, and keep all other directions in order. The moved edge is then antipodal to its former position and has color zero, producing a monochromatic full geodesic. If the exceptional edge were last, apply the inverse root slide. Both contradict badness; hence the exceptional position is interior.

Direction recoloring preserves dimension, so the argument also applies to a minimum-dimensional counterexample. The complementary paired lift preserves the profile-set cylinder by (SM3) in this Subsection, hence retains minority count one and counterexample status while imposing vertex balance. \(\square\)

**Corollary (single-defect repair equivalence).** The following assertion is equivalent to unrestricted NORI1:

> Every antipodally odd binary edge coloring of \(Q_n\) admitting a full antipodal geodesic with \(n-1\) edges of one color and one edge of the other color admits a monochromatic full antipodal geodesic.

*Proof.* NORI1 immediately implies the assertion. Conversely, a failure of NORI1 gives the counterexample \(b\) of (GD4), violating the single-defect repair assertion. \(\square\)

This reduction is exhaustive over arbitrary legal colorings, regardless of nonlinear direction rules. It refines the earlier minority-defect amplification formulation by giving a canonical single-defect witness in some recoloring of every counterexample. Alongside the global ballot-corridor and minority-face rigidity results above, it identifies isolated interior defects in globally extremal full geodesics as a sufficient target for the grand theorem.


##### Central localization of one-defect counterexamples

Let \(c\) be a legal antipodally odd coloring on \(Q_d\), and suppose a full antipodal geodesic \(P\), rooted at \(x\), has one color-one edge at position \(p\). Put \(s=\#\{i:c_i(x)=1\}\), and let \(L(c)\) denote the complementary paired lift. Write \(N_r=2^rd\).

**Theorem (central single-defect lift).** For every \(r\ge1\), \(L^r(c)\) is balanced and has a full antipodal geodesic with one color-one edge at position
\[
\boxed{p_r=N_r/2+D,\qquad D=p+s-d.}
\tag{GD5}
\]
The offset \(D\) is independent of \(r\). In particular, if NORI1 is false, then there exist vertex-balanced counterexamples in arbitrarily large dimensions \(N_r\), with a full antipodal geodesic whose unique minority edge is within a fixed number of steps of its midpoint. Both monochromatic runs have length \(N_r/2+O_d(1)\).

*Proof.* In the first lift the new direction \(d+i\) has color \(1\oplus c_i(x)\) at the initial old vertex. Precisely \(s\) such edges are zero, and the other \(d-s\) are zero at the antipodal terminal old vertex. Traverse the former new dimensions first, then \(P\), then the remaining new dimensions. This yields one exceptional edge at \(p_1=p+s\), so \(p_1-N_1/2=p+s-d=D\).

Every complementary paired lift is balanced, since its old and new incident directions come in opposite-colored pairs. Thus at each later lift of a balanced \(Q_{N_r}\) coloring, precisely \(N_r/2\) new directions are zero at the initial old vertex and the remaining \(N_r/2\) are zero at the antipodal terminal old vertex. Inserting these steps before and after the old witness gives
\[
p_{r+1}=p_r+N_r/2,\qquad
p_{r+1}-N_{r+1}/2=p_r-N_r/2.
\]
Induction proves the formula. The one-defect counterexample normalization supplies \(c,P\) if NORI1 fails, and the spectator-cylinder theorem preserves badness under every lift. Since \(2\le p\le d-1\) and \(0\le s\le d\), the fixed offset satisfies \(|D|\le d\). \(\square\)

**Corollary (balanced central repair suffices for unrestricted NORI1).** Fix any \(0<\alpha<1/2\). Suppose every sufficiently high even-dimensional balanced legal coloring admitting a full antipodal geodesic with one minority edge at some position \(p\in[\alpha N,(1-\alpha)N]\) has a monochromatic full antipodal geodesic. Then unrestricted NORI1 holds.

*Proof.* If NORI1 failed, the theorem would supply arbitrarily high-dimensional balanced bad colorings and corresponding single-defect paths with \(p=N/2+D\) for one fixed integer \(D\). Eventually their exceptional positions lie in the stipulated interval, contradicting the proposed repair statement. \(\square\)

Thus the grand conjecture reduces to repairing a single interior defect even for balanced cubes, and that defect may be assumed to lie arbitrarily close to the midpoint as a fraction of the dimension. No bound is placed on the number or nonlinear complexity of the edge rules.


##### Optimal-face precedence antichains and nested minority-cut certificates

Let \(f\) be any binary coloring of \(Q_n\), and \(P\) a full antipodal geodesic globally maximizing its number of color-zero edges. Choose a contiguous segment of \(P\) of length \(r\), starting at \(v\), using directions \(B\), and having \(h\) zero edges and \(k=r-h\) one edges. For \(S\subseteq B\), identify \(S\) with the vertex \(v+e_S\). Orient each face edge as \(S\to S+i\), \(i\notin S\). Give the color-zero edges the strict precedence order \(e\prec f\) if the terminal subset of \(e\) is contained in the initial subset of \(f\).

**Theorem (optimal-face height).** The zero edges of this face form a precedence poset of height \(h\), and therefore can be partitioned into \(h\) antichains. In particular, if \(h=0\), the face is entirely color one; if \(h=1\), no two zero edges in the face can lie on one monotone crossing.

*Proof.* Replacing the selected segment by any monotone path within the supporting face preserves the outer path, the endpoints and all used directions. No replacement can use more than \(h\) zero edges. Any chain of zero edges under precedence embeds in a monotone crossing by filling the intervening directions; conversely the zero edges traversed by such a crossing form a chain. The original segment realizes \(h\). Thus the poset height is \(h\). Partition by longest-chain-ending-at-edge ranks to obtain \(h\) antichains. \(\square\)

**Theorem (nested minority-cut potential).** Let \(d(S)\) be the minimum number of color-one edges among monotone paths in the face from \(v\) to \(v+e_S\). Then \(d(\varnothing)=0\), \(d(B)=k\), and
\[
\boxed{d(S)=\min_{i\in S}\left[d(S\setminus\{i\})+\mathbf1_{\{f_i(v+e_{S\setminus\{i\}})=1\}}\right].}\tag{EX3}
\]
For every \(1\le j\le k\), let \(L_j=\{S:d(S)<j\}\). Every forward edge from \(L_j\) to its complement has color one. Every monotone crossing of the face leaves every \(L_j\) at least once; no single edge leaves two \(L_j\)'s. The original optimal segment leaves each \(L_j\) once, and along that segment \(d\) increases by one at every one edge and remains constant on zero edges.

*Proof.* Last-step decomposition proves the recurrence. The preceding height theorem gives \(d(B)=r-h=k\). For an oriented edge \(S\to T=S+i\),
\[
d(T)\le d(S)+\mathbf1_{\{f_i(v+e_S)=1\}}\le d(S)+1.
\]
Every outward threshold crossing \(d(S)<j\le d(T)\) must therefore use a one edge and can cross only one threshold. Any monotone path begins with \(d=0\) and ends with \(d=k\), so it must cross all \(k\) thresholds. The original segment has only \(k\) one edges and thus crosses all thresholds with no wasted one edge. Its one edges increase \(d\) by one and its zero edges preserve \(d\), since any decrease would require more than \(k\) positive unit jumps to reach \(k\). \(\square\)

**Corollary (rootwise obstruction towers).** If a legal antipodally odd coloring \(c\) fails NORI1 with global minority defect \(m(c)>0\), then for every root \(x\), the full Boolean lattice based at \(x\) admits at least \(m(c)\) nested color-one directed cut boundaries separating \(\varnothing\) and \([n]\). They arise as levels of its minimal one-edge path cost. In the one-defect normal form (GD4), a witness with just one exceptional one edge crosses the first red-reachability boundary only once, at that edge.

These primal poset and dual integer-potential statements apply with arbitrarily many nonlinear direction rules. The remaining obstruction is consistency of rootwise cut towers under antipodal translation and changes of root.


##### Middle-edge one-defect normal form via balanced padding

For \(z\in Q_4\), define
\[
h_1(z)=z_2,\quad h_2(z)=z_1,\quad
h_3(z)=1\oplus z_2,\quad h_4(z)=1\oplus z_1.
\tag{GD6}
\]
This is a vertex-balanced antipodally odd coloring, and the full geodesic from \((0,1,0,0)\) with direction order \((3,2,1,4)\) has color word \(0000\). Thus for every \(q\ge1\) the Cartesian product \(H_q=h^{\boxtimes q}\) is a balanced legal coloring of \(Q_{4q}\) admitting a monochromatic-zero full geodesic.

**Theorem (middle-edge counterexample normalization).** If unrestricted NORI1 is false, then in arbitrarily high dimensions \(2M\) there are vertex-balanced legal counterexamples with a full antipodal geodesic having word
\[
\boxed{0^{M-1}1\,0^{M}.}
\tag{GD7}
\]
The witness may also be placed at root \(0^{2M}\), with increasing direction order. Consequently, unrestricted NORI1 is equivalent to the assertion that every sufficiently high-dimensional balanced legal coloring admitting such a middle-edge witness has a monochromatic full antipodal geodesic.

*Proof.* Take a counterexample \(c\) of dimension \(d\) with a full geodesic \(P\), rooted at \(x\), having one color-one edge at position \(p\), furnished by the one-defect theorem above. Let \(s\) denote the number of incident color-one edges at \(x\), and put \(D=p+s-d\). Choose \(q\) such that \(2q\ge|D|\), and set \(m=4q\), \(t=2q-D\), so \(0\le t\le m\). The independent product \(G=c\boxtimes H_q\) is a counterexample: a monochromatic full product geodesic would project to one in \(c\).

Take a full color-zero geodesic of \(H_q\). Traverse its first \(t\) steps, then all of \(P\), then its remaining \(m-t\) steps. Independent factor rules make this a full geodesic in \(G\), with one color-one edge at position \(p'=p+t\). Its root has \(s'=s+2q\) incident color-one edges by the balance of \(H_q\), and its dimension is \(d'=d+4q\). Hence
\[
p'+s'-d'=(p+2q-D)+(s+2q)-(d+4q)=0.
\]
The complementary paired lift \(L(G)\), of dimension \(2d'\), is balanced and remains a counterexample. Applying the midpoint formula (GD5) to the full path in \(G\), its color-one edge occurs at position \(d'\). Put \(M=d'\). Increasing \(q\) makes \(M\) arbitrarily large. Translate the starting cube vertex and permute the dimension labels to arrange the normalized root and order.

If NORI1 holds, every such coloring has a monochromatic full geodesic. If it fails, this construction violates the asserted repair principle for arbitrarily large \(M\), proving equivalence. \(\square\)

The repair target now has a fixed witness word, a fixed path order and starting root, and balanced incident color degrees at every vertex. All nonlinear direction dependencies remain permissible.


##### Arbitrary positional padding of a single defect

Let \(c\) be legal on \(Q_d\), and suppose a full antipodal geodesic \(P\) rooted at \(x\) has color-zero edges except for its edge in position \(p\), which has color one.

**Theorem (free positional amplification).** For every \(N\ge d\) and every integer \(q\) satisfying
\[
\boxed{p\le q\le p+N-d,}\tag{GD6}
\]
there is a legal coloring \(C\) of \(Q_N\) with the following properties:
(i) the original direction rules \(c_i\) are preserved and ignore the \(N-d\) new vertex bits;
(ii) \(C\) has a full antipodal geodesic whose unique one edge lies in position \(q\);
(iii) its direction-indexed full-profile support is \(\mathcal W(C)=\mathcal W(c)\times\mathbb F_2^{N-d}\), and its minority defect satisfies \(m(C)=m(c)\). Thus a counterexample \(c\) yields a counterexample \(C\) with the prescribed exceptional rank.

*Proof.* Write \(N-d=a+b\) with \(a=q-p\) and \(b=N-d-a\). Choose an arbitrary odd Boolean function \(\phi:Q_d\to\mathbb F_2\), for example \(\phi(z)=z_1\). Add \(a\) new directions with rule \(g(z)=\phi(z)+\phi(x)\), which has color zero at \(x\); add \(b\) more new directions with rule \(h(z)=1+\phi(z)+\phi(x)\), which has color zero at \(\bar x\). All new rules ignore all new bits and reverse under old-bit antipodality, hence the extension is legal. Traverse the \(a\) new directions at the old root \(x\), then follow \(P\), then traverse the remaining \(b\) new directions at old endpoint \(\bar x\). All inserted edges are zero, so the unique one edge moves from position \(p\) to \(q=p+a\).

Projecting any full geodesic of \(C\) onto the old directions gives a full geodesic of \(c\) with its old profile. Conversely, for any old full geodesic rooted at \(z\), each new direction can be placed before the old path to receive \(g(z)\) or \(h(z)\), or after it to receive its complement. All new rules ignore the new bits, so any assignment to the \(N-d\) new direction-profile entries is realized. This proves the profile cylinder; minimizing the minority count proves \(m(C)=m(c)\), as in (SM2). \(\square\)

**Corollary (location-independent high-dimensional closure test).** Fix any \(\alpha\in(0,1)\). If every sufficiently high-dimensional legal coloring of \(Q_N\) admitting a full antipodal geodesic with one minority edge at position \(\lfloor\alpha N\rfloor\) admits a monochromatic full geodesic, then unrestricted NORI1 holds. Indeed, if NORI1 failed, the one-defect normalization (GD4) would give a fixed bad coloring \(c\), and for all sufficiently large \(N\), the rank \(q=\lfloor\alpha N\rfloor\) lies in the interval (GD6), producing bad extensions with the stipulated property.

In this construction the \(a\) spectator directions form a monochromatic \(a\)-face at the starting old vertex \(x\), while the \(b\) spectators form a monochromatic \(b\)-face at the terminal old vertex \(\bar x\). Hence arbitrarily large monochromatic spectator faces and unrestricted exceptional-rank placement are consistent with the hypothetical failure of NORI1. The stronger central *balanced* placement is separately guaranteed by (GD5).


##### Balanced arbitrary-rank transport of a single defect

Define an auxiliary coloring \(E\) on \(Q_4\), with directions \(0,1,2,3\), by
\[
E_0(z)=z_1,\quad E_1(z)=z_0,\quad
E_2(z)=1+z_1,\quad E_3(z)=1+z_0\pmod2.
\]
Each edge rule ignores its direction bit and changes under simultaneous bit complementation. At every vertex, \(E_0+E_2=E_1+E_3=1\) as integer zero/one color counts in complementary pairs, so this coloring is vertex-balanced. The path rooted at integer vertex \(1\) with order \((3,0,1,2)\) has all four edges of color zero.

**Theorem (balanced free-position single-defect amplification).** Suppose \(c\) is a legal counterexample on \(Q_d\). Then there are fixed integers \(D\ge4\) and \(p\in\{2,\ldots,D-1\}\), and vertex-balanced legal counterexamples \(C_m\) on
\[
\boxed{Q_{N_m},\qquad N_m=D+4m\quad(m\ge0),}\tag{GD7}
\]
such that for **every** integer \(q\) with
\[
\boxed{p\le q\le p+4m,}\tag{GD8}
\]
the SAME coloring \(C_m\) has a full antipodal geodesic with color-one edge only at position \(q\).

*Proof.* By the one-defect normalization (GD4), replace the original bad coloring by a legal bad recoloring \(b\) of the same dimension with a full path having one one edge. Take its complementary paired lift \(B=L(b)\), of even dimension \(D=2d\). The lift is legal and vertex-balanced, is still bad by the profile-cylinder theorem (SM3), and has a full path \(P_B\) with just one color-one edge at a fixed position \(p\), by (GD5).

Let
\[
C_m=B\boxtimes E^{\boxtimes m}.
\]
The independent product is legal and vertex-balanced because each factor is. It is a counterexample: any monochromatic full geodesic would project onto one in \(B\). The \(m\) auxiliary \(E\) factors admit a concatenated color-zero full geodesic \(P_E\) of length \(4m\). For any \(0\le t\le4m\), traverse the first \(t\) steps of \(P_E\), all of \(P_B\), then the remaining steps of \(P_E\). Each factor's edge colors ignore the other factor, and all directions are used once. The unique color-one edge has position \(p+t\), proving (GD8). \(\square\)

**Corollary (balanced fixed-relative-rank closure test).** Fix ANY \(\alpha\in(0,1)\). If, in all sufficiently large even dimensions, every balanced legal coloring with a full geodesic having only one color-one edge in position \(\lfloor\alpha N\rfloor\) admits a monochromatic full geodesic, then unrestricted NORI1 holds.

*Proof.* A counterexample would yield the balanced counterexamples \(C_m\) from (GD7). Since \(p,D\) are fixed and \(0<\alpha<1\), for all sufficiently large \(m\) the integer \(\lfloor\alpha N_m\rfloor\) lies in the interval (GD8), contradicting the proposed repair assertion. \(\square\)

More generally, along dimensions \(N_m=D+4m\), the permitted exceptional positions occupy all ranks outside two fixed-width endpoint intervals. Thus balancedness cannot by itself constrain the asymptotic location of a one-edge defect in hypothetical counterexamples. This improves the central balanced localization (GD5) by allowing any prescribed interior rank fraction in a fixed balanced coloring, while preserving unrestricted nonlinear rules in its bad factor.


##### Balanced one-defect geodesics without monochromatic repair at their starting root

The single-defect repair equivalence (GD4) requires a monochromatic geodesic at *some* root. The strengthening that preserves the given root fails even under balance, in arbitrarily large dimension, with the single defect at any prescribed interior rank fraction.

**Theorem (root-preserving repair obstruction).** For each integer \(m\ge0\), there exists a vertex-balanced legal antipodally odd coloring \(C_m\) on \(Q_{N_m}\), where \(N_m=4+4m\), and a vertex \(z_m\), such that:

1. No full antipodal geodesic starting at \(z_m\) is monochromatic, in either color.
2. For every integer \(q\) with \(2\le q\le N_m-2\), a full antipodal geodesic starting at the SAME \(z_m\) has color word \(0^{q-1}1\,0^{N_m-q}\).

Consequently, for every fixed \(\alpha\in(0,1)\), sufficiently large balanced cubes admit rooted full geodesics with one minority edge at position \(\lfloor\alpha N_m\rfloor\), yet no monochromatic full geodesic starting at that root. The coloring itself has a monochromatic full geodesic at another root, as required by the already established finite-dimensional theorem.

*Proof.* Define \(B\) on \(Q_4\), with directions indexed by \(0,1,2,3\), by
\[
B_0(x)=x_1,\qquad B_1(x)=x_0,\qquad
B_2(x)=1+x_0,\qquad B_3(x)=1+x_1
\pmod 2.
\tag{GD9}
\]
Each rule ignores its own bit and changes under complementation of all four bits, so \(B\) is legal. The complementary identities \(B_0+B_3=1\) and \(B_1+B_2=1\) hold in the integer sense of opposite zero/one colors, hence \(B\) is balanced.

At root \(0000\), if direction \(0\) precedes direction \(1\), the two corresponding edge colors are \(B_0=0\) and \(B_1=1\). If direction \(1\) precedes direction \(0\), they are \(B_1=0\) and \(B_0=1\). Thus every full geodesic rooted at \(0000\) contains both colors. Nevertheless the order \((0,1,2,3)\) yields word \(0100\).

Let \(E\) be the vertex-balanced \(Q_4\) coloring defined in the preceding balanced free-position amplification theorem:
\[
E_0(u)=u_1,\quad E_1(u)=u_0,\quad
E_2(u)=1+u_1,\quad E_3(u)=1+u_0.
\]
From the integer root \(1\), its direction order \((3,0,1,2)\) has color word \(0000\). Put
\[
C_m=B\boxtimes E^{\boxtimes m},\qquad
z_m=(0000,1,\ldots,1).
\]
Independent Cartesian products preserve balance and legal antipodal oddness. A monochromatic full geodesic of \(C_m\) rooted at \(z_m\) would project, upon deleting all auxiliary steps, to a monochromatic full geodesic of \(B\) rooted at \(0000\), which was excluded above.

Concatenate the monochromatic paths in the auxiliary factors into a zero-color full path of length \(4m\). For any \(0\le t\le4m\), traverse its first \(t\) edges, then the \(0100\) path in \(B\), then its remaining \(4m-t\) edges. Cross-factor colors do not depend on the other factors' vertex bits, so this is a full geodesic starting at the fixed \(z_m\), with its unique color-one edge in position \(2+t\). All ranks in the claimed interval occur. \(\square\)

This counterexample to the **root-preserving** single-defect repair principle places no restriction on the exchange operations permitted after fixing the root: even full reordering of all directions fails. Thus a proof of unrestricted NORI1 from single-defect witnesses must permit changing the starting root, or select a witness using an additional global criterion that does not hold for all near-monochromatic roots.


##### Antipodal cycle patching: the full-profile support is two-vertex-connected

For a legal antipodally odd coloring \(c\) of \(Q_n\), \(n\ge2\), let \(w(x,\pi)\in\mathbb F_2^n\) record the edge color used in each direction along the full geodesic with root \(x\) and order \(\pi\). Let \(W=\{w(x,\pi):x\in Q_n,\pi\in S_n\}\). Regard \(W\) as a vertex subset of the *profile cube* \(Q_n\).

**Theorem.** The induced graph \(Q_n[W]\) is two-vertex-connected. Indeed, \(W\) is the union of simple antipodally invariant \(2n\)-cycles whose intersection graph is connected, and a spanning tree of this cycle-intersection graph can be chosen so that adjacent cycles meet in at least two antipodal vertices.

*Proof.* Write \(\pi=(i_1,\ldots,i_n)\), \(S_k=\{i_1,\ldots,i_k\}\), and \(w=w(x,\pi)\). Cyclically shift the first \(k\) directions to the end and move the root to \(x+e_{S_k}\). The former first \(k\) edges are now antipodal translates of their old positions and hence have complemented colors; the suffix edges retain their colors. Therefore
\[
w\bigl(x+e_{S_k},(i_{k+1},\ldots,i_n,i_1,\ldots,i_k)\bigr)
=w+e_{S_k}.
\tag{PC1}
\]
Antipodally translating any root complements every profile entry. Consequently \(W\) contains the cycle
\[
C(x,\pi)=
\{w+e_{S_k}:0\le k\le n\}
\cup\{w+\mathbf1+e_{S_k}:0\le k\le n\}.
\tag{PC2}
\]
These are two length-\(n\) monotone paths from \(w\) to \(w+\mathbf1\) with disjoint interiors: nonempty proper prefixes of the same order are nested, and thus cannot be complements. Hence \(C(x,\pi)\) is a simple \(2n\)-cycle, closed under complementation.

Now fix a root and swap two adjacent directions: \(\pi=(A,i,j,B)\), \(\sigma=(A,j,i,B)\). Put \(u=w(x,\pi)\), \(v=w(x,\sigma)\), and \(T=\operatorname{set}(A)\). As the paths differ only within the intervening square, \(u+v\in\{0,e_i,e_j,e_i+e_j\}\). Both cycles contain respectively \(u+e_T,u+e_T+e_i\) and \(v+e_T,v+e_T+e_j\). When the difference is respectively \(0,e_i,e_j,e_i+e_j\), a shared vertex is respectively
\[
u+e_T=v+e_T,\quad
u+e_T+e_i=v+e_T,\quad
u+e_T=v+e_T+e_j,\quad
u+e_T+e_i=v+e_T+e_j.
\]
Their shared vertex has its antipode shared as well. Thus cycles of orders differing by an adjacent transposition meet in at least two distinct vertices.

The state graph on \(Q_n\times S_n\), generated by adjacent order transpositions at a fixed root and cyclic root slides
\((x,(i,\rho))\mapsto(x+e_i,(\rho,i))\), is connected: the transpositions generate every order, and root slides permit flipping any chosen root bit after placing its direction first. A cyclic root slide leaves \(C(x,\pi)\) unchanged by (PC1), whereas an adjacent order swap yields cycles with at least two common vertices. Thus the intersection graph of all cycles \(C(x,\pi)\) is connected, and their union contains every vertex of \(W\).

A simple cycle of length at least four is two-vertex-connected. The union of two such graphs sharing at least two vertices remains two-vertex-connected, since deleting any one vertex leaves connected subgraphs with a common vertex. Add the cycles successively along a spanning tree of their intersection graph. This gives a two-vertex-connected spanning subgraph on \(W\). Adding the other edges of \(Q_n[W]\) preserves this property. \(\square\)

In particular, any two attainable profiles admit two internally vertex-disjoint paths of attainable profiles, by Menger's theorem. Proper antipodally invariant two-vertex-connected subsets of \(Q_n\) exist, so this theorem alone does not establish full profile saturation or NORI1. It supplies a global connectivity constraint on all hypothetical profile holes, with no restriction on nonlinear direction rules.


**Corollary (gap-free full-geodesic color-count spectrum).** Let \(m=m(c)\) be the minimum minority-color count among all full antipodal geodesics of a legal coloring on \(Q_n\). Then the possible numbers of color-one edges on full antipodal geodesics are precisely
\[
\boxed{\{m,m+1,\ldots,n-m\}.}\tag{PC3a}
\]
For every integer \(m<k<n-m\), at least two distinct direction-indexed attainable profiles have weight \(k\).

*Proof.* Since each full geodesic has at least \(m\) edges of each color, no attained profile can have weight outside the indicated interval. Choose a full profile \(w\) of weight \(m\). Antipodal translation supplies its complement \(\bar w\), of weight \(n-m\). One of the two length-\(n\) paths in the profile cycle (PC2) joins \(w\) to \(\bar w\) through profiles in \(\mathcal W(c)\), changing Hamming weight by one at each step. Thus it attains every integer weight between \(m\) and \(n-m\). Its antipodal companion is internally disjoint from the first path and has the same endpoints, so every strictly intermediate weight occurs at least once on each arc, yielding two distinct profiles. \(\square\)

For the one-defect normalization of a hypothetical counterexample, this proves that every count from one through \(n-1\) is realized, while counts zero and \(n\) are absent. The no-gap conclusion holds with arbitrary nonlinear rules and uses only cyclic root transport.


**Support-only limitation.** The formal six-direction profile-count model (FA1)--(FA4), whose support consists of all words except \(0^6\) and \(1^6\), also satisfies the conclusions (PC2)--(PC3a) as abstract support properties. Indeed, \(Q_6\) is six-vertex-connected; deleting the two antipodal vertices leaves a graph that is at least four-vertex-connected. The remaining support is antipodally invariant, its weights are all integers one through five, and its restriction to every three directions is surjective (complete the prescribed three-bit word to a nonconstant six-bit word). Therefore two-vertex-connectivity, gap-free weight interpolation and triple-direction prescription together do not force a monochromatic profile. The cycle-intersection proof above supplies additional *root/order incidence* information beyond these support conditions; exploiting consistency with the original edge rules is still required.


##### Directed-influence profile repair and acyclic shattering

Let \(c\) be an antipodally odd undirected-edge coloring of \(Q_n\). Put \(i\to j\) when \(c_j(z)\ne c_j(z+e_i)\) somewhere, and let \(\Gamma^+(i)\) be the outgoing neighbors of \(i\). Write \(\mathcal W(c)\) for the direction-indexed color profiles of full antipodal geodesics.

**Lemma (controlled profile repair).** If \(w\in\mathcal W(c)\), \(i\in[n]\), and \(b\in\mathbb F_2\), there is \(w'\in\mathcal W(c)\) with
\[
w'_i=b,\qquad w'_j=w_j\quad(j\notin\Gamma^+(i)\cup\{i\}).
\tag{IG1}
\]
*Proof.* Take a path realizing \(w\). Move its direction-\(i\) step to the first position, preserving the order of the other directions. This crosses only other-direction steps; their colors change only for \(j\in\Gamma^+(i)\). For the resulting geodesic rooted at \(x\) with order \((i,\sigma)\), form the path rooted at \(\overline{x+e_i}\) with order \((i,\operatorname{rev}\sigma)\). Its first edge is antipodal to the original first edge, while its later edges retrace the original suffix in reverse. Thus these two paths have equal profiles away from \(i\) and opposite colors in direction \(i\). Choose the one with \(i\)-color \(b\). \(\square\)

**Theorem (acyclic-set profile universality).** For every \(S\subseteq[n]\) whose induced directed influence graph \(D(c)[S]\) is acyclic,
\[
\boxed{\pi_S\mathcal W(c)=\mathbb F_2^S.}
\tag{IG2}
\]
In particular, if \(\tau(D(c))\) is the least number of vertices that must be deleted to make \(D(c)\) acyclic, then
\[
\boxed{v(c)\ge n-\tau(D(c)),\qquad |\mathcal W(c)|\ge2^{n-\tau(D(c))}.}
\tag{IG3}
\]
*Proof.* List \(S=(i_1,\ldots,i_s)\) in a topological order. Begin with any rooted full geodesic and a prescribed word \(t\in\mathbb F_2^S\). For \(r=1,\ldots,s\), apply (IG1) to set its \(i_r\)-color equal to \(t_{i_r}\). Such a repair changes only color \(i_r\) and its out-neighbors, none of which belongs to the earlier portion of the topological order. Previously assigned colors stay unchanged. At the end the target \(t\) is realized, proving (IG2). Choose a largest induced acyclic set to derive (IG3). \(\square\)


##### Triangular acyclic extensions preserve profiles and antipodal detours

Let \(c\) be legal on \(Q_n\), with direction partition \([n]=R\sqcup S\). Assume no influence arc goes from \(S\) into \(R\), and that the induced directed influence graph on \(S\) is acyclic. The \(R\)-edge rules are independent of all \(S\)-bits, hence define a legal antipodally odd coloring \(c_R\) on \(Q_R\).

**Theorem.** If \(\mathcal W\) denotes the direction-indexed full-geodesic profile support, \(\ell\) the shortest monochromatic antipodal-path length, and \(\delta(c)=(\ell(c)-n)/2\), then
\[
\boxed{\mathcal W(c)=\mathcal W(c_R)\times\mathbb F_2^S,\quad
\ell(c)=\ell(c_R)+|S|,\quad \delta(c)=\delta(c_R).}
\tag{TR1}
\]
Thus \(c\) has a monochromatic full geodesic precisely when \(c_R\) does; its profile-support deficit and minimum full-geodesic minority count are also preserved.

*Proof.* Projecting any full geodesic onto \(R\) gives a full geodesic of \(c_R\) with unchanged \(R\)-profile. Conversely, append all \(S\)-directions to a prescribed full \(R\)-geodesic: this realizes the old \(R\)-profile, regardless of the new colors. Hence \(\pi_R\mathcal W(c)=\mathcal W(c_R)\). Starting with any such extension, assign arbitrary colors in \(S\) by the controlled profile-repair lemma (IG1), processing \(S\) in topological order. A repair at \(i\in S\) changes only the \(i\)-profile and outgoing-neighbor profiles. Since there are no \(S\to R\) arcs and no arcs pointing backward within the topological order, all \(R\)-profiles and previously assigned \(S\)-profiles remain fixed. This gives the Cartesian profile identity, and its support-deficit, minority-count, and geodesic consequences.

For the metric statement, any monochromatic antipodal path in \(Q_n\) projects to a monochromatic antipodal walk in \(Q_R\), using at least \(\ell(c_R)\) steps in \(R\); its steps in \(S\) number at least \(|S|\), proving the lower bound. For the reverse inequality, take a shortest color-zero antipodal path \(P_R\) of \(c_R\), and append each \(S\)-direction once, creating an antipodal walk of length \(\ell(c_R)+|S|\). Process \(S\) in topological order using the following extension of (IG1): move the unique \(i\)-step to the beginning, then choose either this walk or the walk with starting vertex \(\overline{x+e_i}\) and with the remaining steps reversed. The latter traverses the antipodal mate of the first edge and all other original undirected edges in reverse, hence toggles the first edge's color and leaves all later colors unchanged. Relocation changes colors only along outgoing influence arcs of \(i\). The argument applies to antipodal walks having each \(S\)-direction once even when directions in \(R\) repeat. Therefore each \(S\)-edge can be set to zero while keeping every \(R\)-edge and every previously corrected \(S\)-edge zero. The resulting color-zero antipodal walk has the required length. The lower bound is attained, proving (TR1). \(\square\)

This generalizes the spectator-extension identities: new direction rules may depend nonlinearly on preceding new directions, provided the added influence graph is acyclic.

##### Saturation of directions with at most one outgoing influence

Let \(D(c)\) be the directed influence graph just defined, and put \(L=\{i:\deg^+(i)\le1\}\) and \(H=[n]\setminus L\).

**Theorem (free-profile cylinders).** For every legal antipodally odd coloring,
\[
\boxed{\mathcal W(c)=\pi_H\mathcal W(c)\times\mathbb F_2^L.}
\tag{IG4}
\]
*Proof.* Fix \(i\in L\), and choose any rooted full geodesic \(P\). If the one possible out-neighbor \(j\) of \(i\) precedes \(i\) in \(P\), move \(i\) to the last position; otherwise move \(i\) to the first position. The relocated step crosses only directions that ignore vertex bit \(i\). Thus every other direction retains its color. First-edge antipodal pairing from (IG1) toggles only the \(i\)-color in the latter case. For a path rooted at \(x\) with order \((\sigma,i)\), the path rooted at \(\bar x+e_i\) with order \((\operatorname{rev}\sigma,i)\) reverses the original initial \(n-1\) edges and traverses the antipodal mate of the last edge, toggling only its \(i\)-color. Therefore both \(i\)-colors occur over every attained non-\(i\) profile. Repeat the invariance over all \(i\in L\). \(\square\)

**Corollary (eight-branching-direction obstruction).** For \(n\ge8\), the seven-direction prescription theorem of Article VIII gives
\[
\boxed{v(c)\ge |L|+\min\{|H|,7\}.}
\tag{IG5}
\]
A counterexample therefore requires at least eight directions each influencing at least two other direction rules.

*Proof.* Prescribe any colors on a chosen set \(T\subseteq H\) of size at most seven by the seven-direction theorem. By (IG4), these colors can be combined independently with all possible colors on \(L\). When \(|H|\le7\), this realizes every binary profile, including the constant profiles. \(\square\)

**Lemma (two-sided sensitivity of a one-defect witness).** Suppose \(c\) is a counterexample and some full geodesic has color word \(0^a1\,0^b\), where its exceptional step is in direction \(i\). Write \(A,B\) for its directions before and after \(i\). There are steps in distinct directions \(j\in A\) and \(k\in B\) on which toggling vertex bit \(i\) reverses their edge colors.

*Proof.* If all the earlier steps were insensitive to bit \(i\), translate the initial monochromatic segment by \(e_i\), delete the exceptional \(i\)-step, and retain the final monochromatic segment. This gives a monochromatic \((n-1)\)-edge geodesic missing direction \(i\). One of its two possible endpoint extensions in direction \(i\) has the required color, since those extension edges are antipodal, contradicting badness. Translating the final segment instead gives the second sensitivity witness. \(\square\)

These constraints hold for arbitrary nonlinear color rules. They force a hypothetical one-defect counterexample to have outgoing color influence on both sides of the exceptional edge.


##### Directed feedback obstruction in a minimum-dimensional counterexample

**Corollary.** Let \(c\) be a counterexample of minimum dimension \(n\), if one exists. Then its directed influence graph has at least \(n+8\) arcs and at least eight vertices of outgoing degree at least two. Moreover, either its directed influence graph is strongly connected or it has at least two distinct strongly connected components containing directed cycles.

*Proof.* The free-profile cylinder theorem above forces at least eight outgoing-degree-at-least-two vertices. A minimum-dimensional counterexample has no vertex of outgoing degree zero: deleting such a dimension restricts the remaining direction rules to a legal smaller coloring, while the deleted direction is a spectator; the spectator profile identity would make the smaller coloring bad. Therefore every vertex has outgoing degree at least one. Summing degrees gives at least \(n+8\) arcs.

For the second assertion, each direction rule is nonconstant, since it ignores its own bit and reverses under complementing all bits. Hence every vertex has incoming degree at least one, and every source strongly connected component of the influence graph must contain a directed cycle. If there were precisely one cyclic strongly connected component \(R\), it would therefore be a source component. Its complement \(S\) would induce an acyclic directed graph, with no arcs from \(S\) into \(R\). The triangular extension theorem makes the full coloring bad precisely when the legal \(R\)-coloring is bad. Since the full coloring was chosen of minimum dimension, this is impossible when \(R\) is proper. Thus \(R=[n]\), giving strong connectivity, or there are at least two cyclic components. \(\square\)

This obstruction is independent of the number of nonlinear terms in the direction rules. It isolates multi-feedback interaction as the additional obstruction beyond a single strongly connected core.


##### Iterative influence pruning and the canonical directed two-out-core

Keep the directed influence graph \(D(c)\): there is an arc \(i\to j\) when toggling vertex bit \(i\) changes some color on a direction-\(j\) edge. This digraph has no loops. Starting from \(R_0=[n]\), repeatedly delete any vertex \(i\) whose number of outgoing neighbors *still in the current vertex set* is at most one. Let \(K\) denote the surviving set, and let \(F=[n]\setminus K\). Equivalently, \(K\) is the unique largest vertex subset whose induced digraph has minimum outgoing degree at least two. We call it the directed two-out-core.

**Theorem (iterated free-profile cylinder).** For every legal antipodally odd coloring \(c\), including arbitrary nonlinear rules,
\[
\boxed{\mathcal W(c)=\pi_K\mathcal W(c)\times\mathbb F_2^F.}\tag{IG6}
\]
Thus every direction removed by the peeling process has a freely adjustable profile bit: for every realized profile \(w\) and every \(i\in F\), the neighboring profile \(w+e_i\) is also realized. The terminal core \(K\) is independent of the order in which vertices are deleted.

*Proof.* We prove by induction on deletion steps that the set \(F_t\) of deleted directions has independent profile freedom:
\[
\mathcal W(c)=\pi_{R_t}\mathcal W(c)\times\mathbb F_2^{F_t},
\qquad R_t=[n]\setminus F_t.
\]
This is tautological for \(F_0=\varnothing\). Suppose it holds for \(F_t\), and \(i\in R_t\) has at most one outgoing neighbor among \(R_t\setminus\{i\}\).

Take any attained profile \(w\), witnessed by a rooted full geodesic with direction order \(\pi\). If \(i\) has a remaining outgoing neighbor \(j\), move step \(i\) to the *first* position when \(j\) lies after it in \(\pi\), or to the *last* position when \(j\) lies before it. If no such \(j\) exists, either end is allowed. In every case, the movement crosses no outgoing neighbor of \(i\) still in \(R_t\). Swapping a direction-\(i\) step across a direction-\(k\) step leaves the color of the latter unchanged whenever \(i\not\to k\). Therefore moving \(i\) to this selected end preserves all direction-indexed colors in \(R_t\setminus\{i\}\). Colors on the already deleted directions may change.

For a full geodesic whose \(i\)-step is first, antipodally translate that first edge and reverse the remaining edges to obtain another full geodesic with opposite color in direction \(i\) and unchanged colors in all other directions; this is the first-edge pairing (PW1). The analogous construction for an \(i\)-step last reverses the preceding edges and antipodally translates the final edge, likewise toggling only the direction-\(i\) profile bit. Hence both \(i\)-colors occur with the same values on \(R_t\setminus\{i\}\). By the induction hypothesis, all colors in \(F_t\) can be assigned independently without changing any colors in \(R_t\). In particular, for every original attained \(w\), the profile \(w+e_i\) is attained, and profile freedom extends from \(F_t\) to \(F_t\cup\{i\}\). This proves (IG6) at termination.

Uniqueness of \(K\) is the usual monotone core argument: a subset with induced minimum outdegree two cannot lose its first vertex under any permissible deletion; conversely, the terminal remaining set itself has induced minimum outdegree two. Therefore the same largest surviving subset occurs in every deletion order. \(\square\)

**Corollary (branching-core necessity for a counterexample).** If \(|K|\le7\), then \(\mathcal W(c)=\mathbb F_2^n\), hence \(c\) has a monochromatic full antipodal geodesic. Consequently every hypothetical counterexample contains an induced directed subgraph on at least eight vertices, each of which influences at least two *other vertices of the same subgraph*.

*Proof.* Universal prescription on seven selected directions, established earlier in Article VIII via the arbitrary-color geodesic result through dimension seven, gives \(\pi_K\mathcal W(c)=\mathbb F_2^K\) when \(|K|\le7\). Equation (IG6) then gives full profile support. \(\square\)

**Corollary (shattering and boundary confinement).** Let \(v(c)\) be the largest shattered direction-set size, and let \(b(c),r(c)\) be the missing-neighbor statistics (BN1). Put \(W_K=\pi_K\mathcal W(c)\). Then
\[
\boxed{
v(c)=|F|+v(W_K),\qquad
b(c)=|W_K|^{-1}\sum_{u\in W_K}|\{i\in K:u+e_i\notin W_K\}|,\qquad
r(c)=\max_{u\in W_K}|\{i\in K:u+e_i\notin W_K\}|.
}\tag{IG7}
\]
In particular, \(v(c)\ge n-|K|+\min\{|K|,7\}\), and all missing-neighbor pairs are supported in the canonical branching core.

*Proof.* Formula (IG6) makes the support a direct Cartesian cylinder. A direction set is shattered precisely when its intersection with \(K\) is shattered in \(W_K\); any selection among \(F\) is free. Each \(F\)-edge stays within the support, while the missing neighbors in \(K\) are independent of the \(F\)-profile entries. This proves every claim. \(\square\)

The reduction is stronger than deleting directions of original outgoing degree at most one just once: an initially high-outgoing-degree vertex becomes peelable when most of its outgoing neighbors have themselves been deleted. It is also stronger than merely requiring a directed cycle among high-outdegree vertices: any counterexample must contain a self-sustaining induced branching core of at least eight directions. The theorem makes no assertion that the projected core profiles are themselves produced by a smaller legal cube coloring; dependencies on discarded vertex bits may persist, so finite-dimensional NORI1 cannot simply be applied to \(K\) beyond the available universal prescription rank.


##### Hollom transport as a first-harmonic response identity

The binary specialization of Hollom's 2026 geodesic averaging argument has a signed form that retains the optimality slack omitted in the square-root estimate. We state it for arbitrary binary edge colorings, with no antipodal hypothesis.

For \(x,y\in Q_n\), let \(F_a(x,y)\) be the minimum switch cost of a geodesic from \(x\) to \(y\), allowing an additional switch at its endpoint to virtual final color \(a\in\{R,B\}\), with \(F_a(x,x)=0\). Put \(D(x,y)=F_R(x,y)-F_B(x,y)\in\{-1,0,1\}\). For \(y\in Q_n\), set \(r_i(y)=1\) when its direction-\(i\) incident edge is red, \(r_i(y)=0\) otherwise, and \(\bar r(y)=n^{-1}\sum_i r_i(y)\).

For \(1\le k\le n-1\), let \(S\) range uniformly over \(k\)-element direction subsets, set \(x=y+e_S\), and define the source-inclusion response
\[
T_{i,k}(y)=\mathbb E[D(x,y)\mid i\in S]-\mathbb E[D(x,y)\mid i\notin S].
\tag{HL1}
\]
Also put
\[
\mathscr L(x,y)=\frac1k\sum_{i\in S}
\left[
F_{\chi_i(y)}(x,y+e_i)-F_{\chi_i(y)}(x,y)
\right]\ge0,
\tag{HL2}
\]
where \(\chi_i(y)\) is the color of the edge in direction \(i\) incident to \(y\). The inequality follows by extending any path from \(x\) to \(y+e_i\) over that final edge.

For \(d(x,y)=k<n\), define the outward-state weighted potential
\[
H(x,y)=\sum_{a\in\{R,B\}}\frac{\#\{i\notin S:\chi_i(y)=a\}}{n-k}F_a(x,y),
\quad
\Phi_k=\mathbb E[H(X,Y)\mid d(X,Y)=k],
\quad\Phi_0=0,
\]
where \(X,Y\) are independent uniform cube vertices.

**Theorem (signed transport and first Johnson harmonic).** For \(1\le k<n\),
\[
\boxed{
\Phi_k-\Phi_{k-1}
=-\frac1{n2^n}\sum_{y\in Q_n}\sum_{i=1}^n
(r_i(y)-\bar r(y))T_{i,k}(y)
-\mathbb E[\mathscr L(X,Y)\mid d(X,Y)=k].
}
\tag{HL3}
\]
For each \(y,k\), only the orthogonal projection of the Boolean-slice function \(S\mapsto D(y+e_S,y)\) onto the centered linear span of the indicators \(\mathbf1_{\{i\in S\}}-k/n\) contributes to the first term. All higher Johnson-slice harmonic components are orthogonal to the transport imbalance.

*Proof.* Let \(p_R^+\) and \(p_R^-\) denote the proportions of red outward and inward edges at \(y\) relative to root \(x\). Let \(H^-\) be the inward-color-weighted mean of \(F_a(x,y)\), and \(G\) the average of \(F_{\chi_i(y)}(x,y+e_i)\) over inward edges. By the definitions,
\[
H-H^-=(p_R^+-p_R^-)D(x,y),\quad
G-H^-=\mathscr L(x,y).
\]
Counting the edges between consecutive Boolean layers from either side gives \(\mathbb E_k G=\Phi_{k-1}\). Hence
\[
\Phi_k-\Phi_{k-1}
=\mathbb E_k[(p_R^+-p_R^-)D]-\mathbb E_k\mathscr L.
\tag{HL4}
\]
Condition on \(Y=y\), so \(S\) is uniform among \(k\)-subsets. Then
\[
p_R^+-p_R^-=-\frac{n}{k(n-k)}
\sum_i(r_i(y)-\bar r(y))\mathbf1_{\{i\in S\}}.
\]
For an arbitrary function \(Z\) of \(S\),
\[
\operatorname{Cov}(\mathbf1_{\{i\in S\}},Z)
=\frac{k(n-k)}{n^2}
\left(\mathbb E[Z\mid i\in S]-\mathbb E[Z\mid i\notin S]\right).
\]
Because \(\sum_i(r_i-\bar r)=0\), substituting \(Z=D\) into (HL4) proves (HL3). The imbalance is a centered linear function of the subset indicators, giving the harmonic statement. \(\square\)

**Corollary (positive alignment budget required by a counterexample).** Put
\[
M(x)=\min\{\operatorname{sw}(P):P\text{ a full antipodal geodesic from }x\}.
\]
Then
\[
\boxed{
-\frac1{n2^n}\sum_{k=1}^{n-1}\sum_{y,i}
(r_i(y)-\bar r(y))T_{i,k}(y)
\ge \frac1{2^n}\sum_x M(x)
+\sum_{k=1}^{n-1}\mathbb E_k\mathscr L.
}
\tag{HL5}
\]
For a legal antipodally odd NORI1 counterexample, the first right-hand term is at least two.

*Proof.* The potential at rank \(n-1\) has one outward edge, ending at the antipode. Extending an optimal predecessor path along that edge incurs no additional switch, so for each such predecessor \(y\), \(H(x,y)\ge M(x)\). Hence \(\Phi_{n-1}\ge2^{-n}\sum_xM(x)\). Summing (HL3) telescopes from \(\Phi_0=0\). If a legal antipodally odd coloring had any full geodesic with one switch, an antipodal cyclic root slide would make a monochromatic one. In a counterexample every rooted antipodal geodesic therefore has at least two switches. \(\square\)

This is a signed, dissipative rewriting of the Hollom transport mechanism, not a new numerical switch bound. The square-root estimate results from replacing the first term with its magnitude and bounding the hypergeometric fluctuation of the incidence-color vector at each endpoint. The theorem separates two other forces: correlation between local incidence colors and first-level changes in *optimal terminal-color preference*, and the nonnegative improvement afforded by alternative preceding paths. Vertexwise star estimates do not enforce the cubical square-consistency relations coupling these quantities between vertices; for NORI1 the antipodal oddness condition adds another global constraint. Thus a hypothetical obstruction requires a coherent signed-alignment budget across all ranks, not merely large local color imbalances. No proof that such alignment is impossible is claimed.



**Proposition (antipodal covariance of the two response fields).** Under the additional legal antipodal oddness condition, the two vectors in the signed transport pairing (HL3) each reverse sign under antipodality:
\[
r_i(\bar y)-\bar r(\bar y)=-(r_i(y)-\bar r(y)),
\qquad T_{i,k}(\bar y)=-T_{i,k}(y).
\tag{HL6}
\]
The Bellman improvement satisfies \(\mathscr L(\bar x,\bar y)=\mathscr L(x,y)\). Consequently the pairing
\[
\sum_i(r_i(y)-\bar r(y))T_{i,k}(y)
\tag{HL7}
\]
and the slack are antipodally even. Averaging over antipodal endpoints therefore produces no cancellation merely from the oddness of the edge coloring.

*Proof.* The antipodal map complements every edge color. It bijects geodesics from \(x\) to \(y\) with geodesics from \(\bar x\) to \(\bar y\), complementing their entire color words. Therefore
\[
F_R(\bar x,\bar y)=F_B(x,y),\qquad
F_B(\bar x,\bar y)=F_R(x,y),
\]
so \(D(\bar x,\bar y)=-D(x,y)\). This bijection preserves the disagreement direction subset \(S\), and hence the two conditional means defining \(T_{i,k}\) both reverse sign. Antipodal oddness also gives \(r_i(\bar y)=1-r_i(y)\), proving (HL6). The final-edge color in each term of (HL2) is complemented at the antipodal pair, while the terminal-state costs are interchanged; thus each slack summand is preserved. The two sign reversals in (HL7) cancel. \(\square\)

The incidence-imbalance and optimal-terminal-response fields are therefore separately antipodally odd, while Hollom's scalar transport observable is even. An equivariant argument seeking more than root-average control must retain information about both fields, their square relations, or the geometry of their zero/alignment sets *before* forming the even scalar pairing; the antipodal involution alone cannot force cancellation of (HL7).



##### Bellman dissipation detects square curvature; flat squares can conceal higher-rank tropical holonomy

Keep the two-state shortest-switch potentials \(F_R(x,y),F_B(x,y)\) and the nonnegative predecessor-reduced-cost slack \(\mathscr L(x,y)\) of (HL2). For any binary edge coloring \(\chi\), define the cubical square curvature
\[
\kappa(Q)=\sum_{e\in\partial Q}\chi(e)\pmod2.
\]
Let \(K(\chi)=|\{Q:\kappa(Q)=1\}|\), where the sum is over undirected two-dimensional square faces.

**Theorem (rank-two curvature–dissipation identity).** For every \(n\ge2\) and every binary undirected-edge coloring, with no antipodal condition,
\[
\boxed{\sum_{d_H(x,y)=2}\mathscr L(x,y)=K(\chi),\qquad
\mathbb E[\mathscr L(X,Y)\mid d_H(X,Y)=2]
=\frac{K(\chi)}{2^n\binom n2}.}\tag{HL8}
\]
More precisely, each curved square supplies two ordered pairs of opposite corners with \(\mathscr L=1/2\) and two with \(\mathscr L=0\). Every flat square supplies four pairs with zero slack.

*Proof.* Fix a square and root corner \(x\), with diagonal endpoint \(y\). Let the two monotone two-edge path color words be \((a,b)\) and \((c,d)\), so \(b,d\) are colors of the last two inward edges at \(y\). Their switch costs are \(s_1=[a\ne b]\), \(s_2=[c\ne d]\). By the endpoint-state definition,
\[
F_b(x,y)=\min\{s_1,s_2+[b\ne d]\},
\quad
F_d(x,y)=\min\{s_2,s_1+[b\ne d]\}.
\]
At both predecessors the terminal state is compared to the preceding edge color, so
\[
2\mathscr L(x,y)=s_1+s_2-F_b(x,y)-F_d(x,y).
\]
If \(b\ne d\), both minima equal their own first arguments, since \(s_1,s_2\in\{0,1\}\), giving \(\mathscr L=0\). If \(b=d\), the minima are both \(\min\{s_1,s_2\}\), so \(\mathscr L=|s_1-s_2|/2\). The latter is nonzero precisely when \(a\ne c\), equivalently \(a+b+c+d=1\pmod2\). On a square with odd edge-color parity, this occurs when the root is at either endpoint of its unique minority-color edge; the other two corners have slack zero. On a square with even parity it never occurs. Summing the four diagonal ordered pairs per square proves the first identity. There are \(2^n\binom n2\) ordered pairs at Hamming distance two, giving the second. \(\square\)

**Corollary (odd-rank topological dissipation).** In odd dimension \(n\ge3\), an antipodally odd coloring satisfies
\[
\boxed{\mathbb E_2\mathscr L\ge\frac1{4\binom n2}
=\frac1{2n(n-1)}.}\tag{HL9}
\]
This follows from the established odd-dimensional lower bound \(K(\chi)\ge2^{n-2}\), derived from the antipodal reversal square-exchange parity obstruction. Thus the odd-dimensional projective curvature class forces a positive amount of reduced-cost slack at the earliest nontrivial rank.

**Theorem (flat coloring with delayed Bellman dissipation).** The legal antipodally odd coloring of \(Q_4\)
\[
\boxed{\chi_0(x)=x_1+x_2+x_3,\qquad
\chi_1(x)=\chi_2(x)=\chi_3(x)=x_0\pmod2}\tag{HL10}
\]
has \(\kappa(Q)=0\) on every square and hence \(\mathscr L(x,y)=0\) whenever \(d_H(x,y)=2\). Nevertheless, taking integer-bit vertices \(x=1\) and \(y=6\), so the differing directions are \(0,1,2\), gives
\[
\boxed{\mathscr L(1,6)=1/3>0.}\tag{HL11}
\]

*Proof.* Put \(\phi(x)=x_0(x_1+x_2+x_3)\) in \(\mathbb F_2\). Each edge color in (HL10) equals the Boolean gradient \(\phi(x)+\phi(x+e_i)\), so all square curvatures vanish. Each \(\chi_i\) ignores bit \(i\) and is odd under complementing all four bits; thus the coloring is legal. By (HL8), every rank-two Bellman slack vanishes.

From root \(x=1\), the two step orders \((0,1)\) and \((1,0)\) lead to the same vertex \(2\) with words \(00\) and \(11\), respectively. Both have zero switches but favor opposite last-color states. Extending in direction \(2\), whose edge color is \(0\) at vertex \(2\), gives words \(000\) and \(110\), of switch costs zero and one. At the diagonal endpoint \(y=6\), the color-zero terminal potential is \(F_0(1,6)=0\). Of the three inward predecessor states, the predecessor \(7=y+e_0\) has \(F_0(1,7)=1\), because both preceding steps are colored one; the predecessors \(4=y+e_1\) and \(2=y+e_2\) have \(F_0=0\), each admitting two color-zero steps. All three final edges into \(y\) are color zero. Hence the average reduced cost is \((1+0+0)/3=1/3\), proving (HL11). \(\square\)

**Structural interpretation.** Formula (HL8) identifies the first layer of the optimal-control slack with the ordinary \(\mathbb F_2\) curvature of the edge coloring. But the flat example shows that the total Bellman slack is **not** determined by this abelian curvature. The two zero-switch routes \(00\) and \(11\) around a flat square differ in their **terminal-color polarization**; the next edge selects between them and causes strict Bellman improvement. Thus the two-state min-plus path transports have nontrivial *variational holonomy* even when their underlying mod-two edge-parity cochain is flat.

The relevant potential for a global cycle–cut theory must retain both terminal states and their competing path costs, rather than only \(\kappa\), the scalar switch count, or the rankwise first-harmonic average. More generally the Bellman slack (HL2) is the average **reduced cost** of the zero-switch continuation transitions in the two-state shortest-path automaton; it measures the failure of all such transitions to be simultaneously optimal. Flat square curvature does not guarantee this simultaneous optimality after further direction steps.



##### Tropical two-state switch cuts and predecessor dispersion

At root \(x\), let \(F_a(x,y)\) be the minimum switch count for a monotone geodesic from \(x\) to \(y\), including a virtual terminal change to color \(a\), with \(F_a(x,x)=0\). For \(S=\{i:x_i\ne y_i\}\), \(k=|S|>0\), put \(b_i=c_i(y)\), \(t_i=F_{b_i}(x,y+e_i)\), \(I_b=\{i\in S:b_i=b\}\), \(q_b=|I_b|\), and \(m_b=\min_{i\in I_b}t_i\), with \(m_b=+\infty\) when \(I_b\) is empty.

**Theorem (two mechanisms of Bellman slack).** The terminal-state Bellman recurrence and predecessor slack obey
\[
\boxed{F_b(x,y)=\min(m_b,1+m_{1-b}),}\tag{HL12}
\]
\[
\boxed{
k\mathscr L(x,y)=
\sum_{b:q_b>0}\sum_{i\in I_b}(t_i-m_b)
+\sum_{b:q_b>0}q_b(m_b-m_{1-b}-1)_+ .
}\tag{HL13}
\]
All terms are nonnegative. Thus zero slack means predecessor costs coincide within each occupied final-edge-color class, and, if both classes are occupied, their minima differ by at most one.

*Proof.* The last edge of any monotone path into \(y\) has some color \(b_i\). A terminal state \(b\) charges the predecessor's corresponding state cost plus \([b_i\ne b]\), giving (HL12). By (HL2), the slack multiplied by \(k\) equals \(\sum_i(t_i-F_{b_i}(x,y))\). Decompose each summand as \((t_i-m_{b_i})+(m_{b_i}-F_{b_i})\), and use (HL12). \(\square\)

The first summand measures **within-color route dispersion**; the second measures **cross-color dominance**, when paying one extra switch still makes the opposite terminal-color route better. In the flat legal four-cube (HL10), the rank-three positive slack comes entirely from the first mechanism, despite all ordinary square curvature being zero.

Build a directed two-state network \(\mathcal A_x\). Its vertices are \((S,a)\) for \(S\subseteq[n]\), \(a\in\{0,1\}\). Both \((\varnothing,a)\) are sources. For each \(i\notin S\), include
\[
(S,a)\longrightarrow(S+i,c_i(x+e_S))
\]
at cost \([a\ne c_i(x+e_S)]\), and also state-change arcs \((S,a)\to(S,1-a)\) of cost one. The two states \(([n],a)\) form the target set. The shortest-path distance to \((S,a)\) is \(F_a(x,x+e_S)\): state changes inserted along a path cannot save cost because the two-color mismatch satisfies the triangle inequality.

**Theorem (canonical switch-cut duality).** Let \(M_x\) be the minimum number of switches in a full antipodal geodesic rooted at \(x\). Then
\[
\boxed{M_x=\max\{\text{number of pairwise arc-disjoint directed source--target cuts in }\mathcal A_x\text{ with only cost-one outward arcs}\}.}\tag{HL14}
\]
The canonical maximum family consists of the threshold cuts
\[
\boxed{\mathcal U_j=\{(S,a):F_a(x,x+e_S)<j\},\qquad 1\le j\le M_x.}\tag{HL15}
\]
Every minimum-switch full geodesic crosses each threshold cut precisely once, at a switching step.

*Proof.* Shortest-path distance \(F\) satisfies \(F(v)\le F(u)+w\) on an arc \(u\to v\) of cost \(w\in\{0,1\}\). Therefore every outward arc of a threshold cut has cost one, and no arc can leave two distinct threshold sets: the distance increases by at most one along it. Both sources have distance zero and both targets have distance at least \(M_x\). Thus the \(M_x\) threshold boundaries are disjoint separating cuts. Conversely, any source--target path must cross the outward boundary of every separating cut; if there are \(r\) pairwise arc-disjoint boundaries with only cost-one arcs, every path costs at least \(r\). Hence \(r\le M_x\). The threshold construction attains equality.

Every prefix of a globally minimum-switch full geodesic is shortest among paths reaching the same vertex and terminal-color state: otherwise replacing that prefix would improve the full path. Its distance label therefore increases by one at each color change and stays fixed on all other steps, proving the calibration assertion. \(\square\)

**Corollary (two barriers surrounding a single exceptional edge).** If \(c\) is a legal NORI1 counterexample with a full geodesic of temporal color word \(0^a1\,0^b\), \(a,b\ge1\), rooted at \(x\), then \(M_x=2\). Its first and second switching transitions are respectively the only outward crossings of the two canonical threshold cuts (HL15) along this geodesic. Every other full geodesic from \(x\) crosses both barriers. The antipodal involution identifies \(\mathcal A_x\) with \(\mathcal A_{\bar x}\), interchanging state colors and preserving costs and cut levels.

*Proof.* The displayed word has two switches, while a legal counterexample has no full geodesic with zero or one switch, by cyclic root sliding. Apply the theorem. Antipodal translation complements both the edge colors and state labels, leaving switch costs invariant. \(\square\)

**Root-gluing obstruction.** Changing root from \(x\) to \(x+e_i\) sends an old subset label \(S\) to \(S\mathbin\triangle\{i\}\). This reverses the orientation of all Boolean-lattice edges in direction \(i\), so it cannot act as an order-preserving isomorphism of these directed state networks. Although every root in a counterexample carries at least two positive-switch cut barriers, antipodality only relates opposite roots; the obstacle to a global dual contradiction is coherent transport of those cuts across neighboring roots. The Bellman slack measures reduced costs of the zero-switch continuations, giving a joint primal/dual bookkeeping of path improvements and barrier separation. This identifies the remaining gluing problem without asserting NORI1 closure.

##### Pointwise tropical tensorization of terminal-color switch potentials

For any binary coloring c of Q_d and vertices x,y, let F_a^c(x,y) be the minimum color switch count on a geodesic x->y, followed by a virtual final color a; define F_a(x,x)=0.

**Theorem.** For arbitrary binary undirected-edge colorings c,d, every source x=(x1,x2), target y=(y1,y2), and a in {0,1},
\[
\boxed{F_a^{c\boxtimes d}(x,y)=\max(F_a^c(x_1,y_1),F_a^d(x_2,y_2)).}\tag{HL16}
\]
This includes non-antipodal endpoints.

*Proof.* Any product geodesic projects into geodesics in each factor, whose temporal color words are subsequences of the product word. Removing letters from a word followed by virtual terminal a cannot increase its switches. This proves the lower bound. Conversely choose optimizing words in both factors and append virtual a. Collapse each maximal constant-color run to one letter. The two resulting alternating words end in a; the shorter is a suffix of the longer. Align their runs from the right, interleaving all steps in matching runs while retaining each factor's order. Omit the virtual terminal step. This is a product geodesic with cost at most the maximum, proving equality. \(\square\)

**Corollary (calibration is product-closed).** A coloring is *fully Bellman-calibrated* if its Hollom slack L(x,y), defined in (HL2), vanishes for every x,y. Every independent product of fully calibrated colorings is fully calibrated.

*Proof.* The predecessor reduced costs in the definition of L are nonnegative, so L=0 iff for every inward edge i with color b=c_i(y), F_b(x,y)=F_b(x,y+e_i). In the product, apply (HL16) to this equality; the other factor's terminal cost is unchanged when the last direction i is in the first factor. Repeat symmetrically. \(\square\)

**Theorem (arbitrarily large legal zero-dissipation cubes).** For each even n=2m, choose arbitrary bits alpha_i and put
\[
c_{2j}(x)=x_{2j+1}+\alpha_{2j},\quad
c_{2j+1}(x)=x_{2j}+\alpha_{2j+1}\pmod2.
\tag{HL17}
\]
These colorings are legal antipodally odd and satisfy L(x,y)=0 for every root x and endpoint y. For m>=2 they nevertheless admit roots whose minimum full-geodesic switch count equals two.

*Proof.* Each two-direction factor is legal. In one pair, denote the first-edge colors of its two antipodal direction orders by A,C. The two color words are (A,1-C) and (C,1-A). If A=C, both words are (A,1-A), and both last-edge predecessor transitions realize terminal-state cost 1. If A differs from C, both words are monochromatic, one of color A and one of color C, and both last-edge predecessor transitions realize cost 0. At rank one the sole predecessor transition realizes cost 0. Thus every predecessor transition in Q2 is Bellman-tight. The product-closure corollary gives all-rank zero slack in every Q_{2m}. To obtain a two-switch root, select two factors so their respective rooted two-step words are necessarily 01 and 10. Their terminal-state costs are (F_0,F_1)=(2,1) and (1,2), so the product has (F_0,F_1)=(2,2) by (HL16). Every additional two-direction factor has both terminal-state costs at most 2 and cannot increase the maximum. Therefore its rooted minimum switch count is two. \(\square\)

**Interpretation.** Rootwise switch optimization is governed by a max-tropical product law, while the number of minority edges in an optimal full profile is additive under products. Local Bellman dissipation can vanish throughout arbitrarily large antipodally odd cubes despite nonzero rooted switch barriers. Hence the rank-two curvature and higher Bellman-slack mechanisms, taken in isolation, cannot force a favorable root. Any global root-gluing theorem must use the coherence of the *collection* of root-dependent cut towers, not merely their positive local reduced costs.### Two-state min-plus square holonomy and its three-fold discrepancy spectrum

For a binary temporal word \(w=w_1\cdots w_\ell\), put
\[
K_w(a,b)=[a\ne w_1]+\operatorname{sw}(w)+[w_\ell\ne b],\qquad a,b\in\{0,1\}.
\]
This is the path's two-state switch-transport cost matrix, retaining both input and output polarizations. Concatenating paths corresponds to min-plus matrix multiplication of these costs.

For an undirected cubical square \(Q\) spanned by dimensions \(i,j\), and a chosen diagonal ordered from corner \(x\) to the opposite corner \(y=x+e_i+e_j\), let \(w=(A,B)\) and \(w'=(C,D)\) be the edge-color words of its two monotone two-step routes.

**Theorem (square transfer rigidity).**
\[
\boxed{K_w=K_{w'}\iff (A,B)=(C,D)
\iff c_i(x)=c_j(x)\ \text{and}\ c_i(y)=c_j(y).}\tag{HL19}
\]
In particular, equality of transfer matrices along both diagonal orientations of every square forces every cube edge to have a globally constant color. No nontrivial legal antipodally odd coloring can have this property.

*Proof.* The four possible two-step words have distinct transfer matrices, as seen for instance from their values on the four ordered terminal pairs:
\[
K_{00}=(0,1,1,2),\
K_{01}=(2,1,3,2),\
K_{10}=(2,3,1,2),\
K_{11}=(2,1,1,0).
\]
Thus equal matrices require equal words, giving the first equivalence. The first entries of the two square routes are precisely the two incident colors at \(x\), while the last entries are the two incident colors at \(y\); this proves the second. If both diagonal orientations of every square have equal matrices, every two edges at every vertex have the same color. Undirected consistency then forces this common vertex color to agree across adjacent vertices, so it is constant throughout the connected cube. Antipodal oddness excludes constant edge color. \(\square\)

Call an orientation of the diagonal of an undirected square *tropically discordant* when its two route matrices differ. Each square has two unoriented opposite-corner diagonals, giving two such tests. Classify squares up to dihedral symmetry and global color complement:

**Theorem (discrepancy spectrum and balanced lower bound).** The numbers of discordant diagonal tests are
\[
\boxed{\begin{array}{c|cccc}
\text{cyclic square word}&0000&0011&0001&0101\\ \hline
\#\text{ discordant diagonals}&0&1&2&2\\
\text{ordinary parity curvature}&0&0&1&0
\end{array}.}\tag{HL20}
\]
For any binary coloring of \(Q_n\), if \(r(x)\) is the number of color-one incident edges at vertex \(x\) and \(H(c)\) is the total number of discordant diagonal tests over all squares, then
\[
\boxed{H(c)\ge \frac12\sum_{x\in Q_n}r(x)(n-r(x)).}\tag{HL21}
\]
For a balanced coloring of even dimension, \(r(x)=n/2\) at every vertex, hence
\[
\boxed{H(c)\ge n^2\,2^{n-3}.}\tag{HL22}
\]

*Proof.* By (HL19), a diagonal test is discordant precisely when at least one of its two endpoint corners has two differently colored square edges. The four square patterns have respectively zero, two, two, and four corners of mixed incidence; for the adjacent 2+2 pattern the two mixed corners are opposite, while for the 3+1 pattern they are adjacent. This proves the table. At a cube vertex \(x\), each choice of one incident color-zero edge and one incident color-one edge selects one square and produces one mixed corner in one of its two diagonal tests. There are \(r(x)(n-r(x))\) such choices. Each discordant diagonal test has at most two mixed endpoint corners. Double counting therefore proves (HL21), and substituting \(r(x)=n/2\) yields (HL22). \(\square\)

**Interpretation.** The ordinary Boolean square curvature distinguishes the 3+1 case only. The two-state tropical transfer test additionally detects the adjacent 2+2 pattern and the alternating 0101 pattern, both invisible to parity curvature. Yet (HL8) says rank-two Hollom Bellman dissipation is contributed only by the 3+1 case. Thus **transport discordance**, **mod-two color curvature**, and **Bellman dissipation** are three different observables. Balanced legal colorings have extensive transfer discordance by (HL22), and even legal flat colorings may have transfer discordance while their Bellman slack vanishes at every rank by (HL17)--(HL18). The cycle--cut obstruction cannot be reduced to the density of discordant squares; it must also account for how their two-state transfers can be reconciled along complete paths and across root changes.### Antipodal two-ended tropical kernel and root polarization

For arbitrary binary edge coloring c and vertices x,y, define the geodesic transport kernel K_{ab}(x,y), a,b in {0,1}, as the minimum over geodesics P from x to y of
\[
[a\ne c(e_1)]+\operatorname{sw}(P)+[c(e_{\rm last})\ne b],
\]
with K_{ab}(x,x)=[a\ne b].

**Theorem (two-ended tropical-max tensorization).** For independent arbitrary edge colorings c,d,
\[
\boxed{K_{ab}^{c\boxtimes d}((x,u),(y,v))
=\max(K_{ab}^c(x,y),K_{ab}^d(u,v)).}\tag{HL23}
\]
This holds for every geodesic source-target pair and both prescribed endpoint states.

*Proof.* Any product geodesic projects into a geodesic in each factor. Its color word with virtual first letter a and virtual last letter b is a supersequence of both factor words with those same boundary letters. Deleting letters never increases switches, proving the lower bound. For the upper bound take optimizing factor paths. Compress each augmented binary word into its alternating sequence of runs. Both sequences begin with a and end with b, and hence their lengths have equal parity. Align the shorter run sequence with the longer, matching both boundary letters, and interleave factor steps within aligned runs, respecting each factor's order. The resulting product geodesic has augmented switch count at most the longer sequence's switch count. \(\square\)

Assume now that c is legal antipodally odd, y=\bar x, and M_x is the minimum ordinary switch count among full geodesics rooted at x. Put K_x=(K_{ab}(x,\bar x))_{a,b}.

**Theorem (even diagonal and antipodally odd orientation).** There exist an integer h_x>=0 and signs epsilon_x,eta_x in {-1,+1} satisfying
\[
\boxed{K_x=\begin{pmatrix}
2h_x&2h_x+\epsilon_x\\
2h_x+\eta_x&2h_x
\end{pmatrix},\qquad
2h_x=2\lceil M_x/2\rceil.}\tag{HL24}
\]
For the color-swap matrix J, antipodal root translation gives
\[
\boxed{K_{\bar x}=J K_xJ,\quad h_{\bar x}=h_x,\quad
s_{\bar x}=-s_x,\quad
s_x=\tfrac12(K_{01}(x,\bar x)-K_{10}(x,\bar x))\in\{-1,0,1\}.}\tag{HL25}
\]
If h_x=0 then both signs are +1. A monochromatic full geodesic rooted at x exists iff h_x=0, in which case both monochromatic colors occur at that root.

*Proof.* For each path word w, its augmented switch count from a to b has parity a+b, by telescoping successive color discrepancies. Thus the diagonal kernel entries are even and the off-diagonal entries odd. Reverse a full path and translate it antipodally. The resulting path has the complemented reversed color word and begins at the same root x. It maps the (a,b) cost to the (1-b,1-a) cost, proving K_{00}=K_{11}. Changing one prescribed boundary color alters each candidate cost by one in absolute value, so each off-diagonal kernel entry differs by one from the even diagonal.

The even diagonal is at least M_x. Take a path with t=M_x switches. When t is odd, its first and last colors differ, so its augmented 0-to-0 cost is t+1. When t is even, its first and last colors agree; either this path or its complemented reversal begins and ends in zero, giving augmented cost t. Therefore the even diagonal equals 2 ceil(t/2). Translating paths antipodally complements both boundary colors and proves the conjugation formula; the entries are nonnegative so h=0 forces epsilon=eta=+1. Zero diagonal cost is equivalent to an all-zero full path, and the complemented reversal gives an all-one full path from the same root. \(\square\)

**Corollary (root obstruction max-tensorization).**
\[
\boxed{h_{(x,u)}(c\boxtimes d)=\max(h_x(c),h_u(d)).}\tag{HL26}
\]
Unrestricted NORI1 is equivalent to h_x=0 for some root in every legal coloring.

*Proof.* Apply (HL23) to diagonal terminal states and divide by two. The zero criterion is the preceding theorem. \(\square\)

The diagonal root obstruction h is antipodally even, while the off-diagonal preference s is antipodally odd. The latter retains orientation information discarded by scalar switch counts and scalar Bellman drift. No theorem controlling its variation between *neighboring* roots is assumed: root change reverses one dimension of the associated subset lattice.### Antipodal seam gluing and even endpoint-forcing gaps

Let c be a legal antipodally odd binary coloring on Q_n. Fix a root x and a direction i. Write y=x+e_i, z=\bar x, \bar y=z+e_i and b=c_i(x). The antipodal seam edge from z to \bar y has color 1-b. The vertices y and z lie in a common (n-1)-face; a geodesic P:y->z traverses every direction other than i once.

Let H_{pq}^{(i,x)}=K_{pq}(y,z) denote its two-ended color-switch kernel as defined in (HL23), and let K_x^{i-first}(p,q) denote the minimum two-ended cost among full geodesics from x to z that begin in direction i. Similarly let K_y^{i-last}(p,q) denote the minimum among full geodesics from y to \bar y that end in direction i.

**Theorem (root seam identities).** For all prescribed input and output colors p,q,
\[
\boxed{K_x^{i-first}(p,q)=[p\ne b]+H_{bq}^{(i,x)},\quad
K_y^{i-last}(p,q)=H_{p,1-b}^{(i,x)}+[1-b\ne q].}\tag{HL27}
\]
In particular, for the orientation (p,q)=(b,1-b), these two conditional costs agree:
\[
\boxed{K_x^{i-first}(b,1-b)=K_y^{i-last}(b,1-b)=E_i(x),
\quad E_i(x):=H_{b,1-b}^{(i,x)}.}\tag{HL28}
\]

*Proof.* Every geodesic from x to z starting with direction i consists of the initial seam edge x->y, followed by a geodesic P from y to z in the common (n-1)-face. The first edge has color b, so its augmented switch cost equals [p!=b] plus the two-ended cost of P from input color b to output q. Minimizing yields the first formula. Every geodesic from y to \bar y ending with direction i consists of P followed by the opposite seam edge z->\bar y, of color 1-b. Its cost is the two-ended cost of P from p to 1-b, plus a final mismatch charge [1-b!=q]. This gives the second formula and their specialization. \(\square\)

Define the two **endpoint-forcing gaps**
\[
g_i^x=E_i(x)-K_{b,1-b}(x,\bar x),\qquad
g_i^y=E_i(x)-K_{b,1-b}(y,\bar y).
\tag{HL29}
\]
Both are nonnegative because unrestricted full-geodesic minima are no greater than the corresponding endpoint-constrained minima.

**Corollary (quantized root-transport law).** The forcing gaps are nonnegative even integers, and the change of the oriented root kernel across the edge x->y is
\[
\boxed{K_{b,1-b}(x,\bar x)-K_{b,1-b}(y,\bar y)=g_i^y-g_i^x
\in2\mathbb Z.}\tag{HL30}
\]
Antipodal translation of the oriented root edge preserves E_i and each forcing gap after complementing b.

*Proof.* The virtual input/output colors of all three kernels E_i, K_x(b,1-b), and K_y(b,1-b) differ, so the parity-telescoping identity used in (HL24) makes each value odd. Their differences are thus even. The displayed equality follows by subtracting the definitions in (HL29). Antipodal translation complements all traversed edge colors and both terminal states, leaving switch costs unchanged. \(\square\)

The root-orientation field s_x of (HL25) is obtained from the difference between the two off-diagonal entries of K_x. Formula (HL30) shows how **one of those entries** moves across a neighboring-root edge: its derivative is the difference of two nonnegative, quantized endpoint-forcing prices. In particular, when both forcing gaps vanish, that oriented entry is constant across the edge. A change in the preferred direction of transport cannot be inferred from square parity alone; it must be accommodated by endpoint forcing in one or both orientations or by a change of the even diagonal root grade h.

This is a root-gluing identity, not a root-gluing impossibility theorem. The common facet kernel H is a shared transport object for adjacent roots, while the two forcing gaps are the cost of arranging its seam dimension at the designated end. Global consistency of these gaps around cubical cycles is a possible strengthened obstruction target; no signed cancellation or rootwise continuity theorem is asserted here.### Linear adjacent-root disparity in legal antipodal switch potentials

Write M_x(c) for the minimum number of temporal color changes among full antipodal geodesics rooted at x, and h_x=ceil(M_x/2) for the even two-ended tropical obstruction (HL24).

**Theorem (unbounded one-edge root gradient).** For every m>=1, put n=4m+2. There is an explicit legal antipodally odd coloring c of Q_n with adjacent roots 0 and e_0 such that
\[
\boxed{M_{e_0}(c)=0,\quad M_0(c)=2m+1,\qquad
h_{e_0}(c)=0,\quad h_0(c)=m+1=(n+2)/4.}\tag{HL32}
\]
Therefore no dimension-independent Lipschitz bound across adjacent roots holds for minimum switch count or its even tropical grade, even among legal antipodally odd colorings.

*Construction.* Let the baseline coloring be
\[
p_i(z)=\sum_{j\ne i}z_j\pmod2.
\]
It is legal because n is even. Set A={1,...,2m} and B={2m+1,...,4m+1}. Starting at e_0, take the full geodesic P with direction order
\[
(1,2,\ldots,2m,\ 0,\ 2m+1,\ldots,4m+1).
\tag{HL33}
\]
Define c by recoloring every edge of P to zero and each antipodal mate to one, retaining p on all other antipodal edge orbits. This is consistent since P uses each direction once and hence contains no antipodal edge pair. Thus c is legal and P is a monochromatic full geodesic rooted at e_0.

*Proof of the rooted lower bound.* From root 0, every baseline full geodesic has temporal word 0101...01, since on step k the currently traversed direction has not yet been flipped and all other bits have Hamming weight k-1. Thus its switch count is n-1=4m+1.

The P-step in direction 0 occurs at position 2m+1 and has baseline color zero, so that edge and its antipode are not changed. Before that step, the baseline colors of P at positions r=1,...,2m are r mod 2; after it, at positions r=2m+2,...,n they are again r mod 2. Hence the changed P edges are precisely those in odd positions before and after the central direction-0 step: m edges in each arm. Their antipodal mates form two additional classes of m edges. The four changed-edge classes are supported in these four cube faces:
\[
\begin{array}{c|ccc}
&z_0&z|_A&z|_B\\ \hline
E_1\text{ (initial P arm)}&1&\text{free}&0^B\\
E_2\text{ (terminal P arm)}&0&1^A&\text{free}\\
E_3\text{ (antipode of initial arm)}&0&\text{free}&1^B\\
E_4\text{ (antipode of terminal arm)}&1&0^A&\text{free}
\end{array}
\tag{HL34}
\]
The changed edges of E_1,E_3 use directions in A; those of E_2,E_4 use directions in B.

A monotone full geodesic rooted at 0 can meet changed edges in *at most one* of these four classes. Indeed it may never go from z_0=1 back to z_0=0. Among the classes with z_0=1, traversing any E_1 edge makes an A-bit one, ruling out subsequent E_4 edges, whose A-bits all vanish; traversing E_4 first makes a B-bit one, ruling out subsequent E_1 edges. Among the classes with z_0=0, traversing E_2 makes all A-bits one and at least one B-bit one, ruling out subsequent E_3 edges, which lack at least one A-bit before their A-direction step; traversing E_3 makes all B-bits one and at least one A-bit one, ruling out subsequent E_2 edges, which lack at least one B-bit before their B-direction step. Finally, after any E_2 or E_3 edge in the z_0=0 half, at least one bit in both A and B is one, preventing any subsequent E_1 or E_4 edge in the z_0=1 half, since E_1 requires all B-bits zero and E_4 requires all A-bits zero. The other ordering of these halves is impossible since z_0 cannot decrease. Thus a rooted-0 geodesic traverses at most m recolored edges.

Changing a single letter of a binary temporal word changes at most two neighboring color comparisons. Therefore every full geodesic rooted at 0 retains at least
\[
(4m+1)-2m=2m+1
\]
switches after recoloring.

This bound is attained: take the rooted-0 direction order
\[
(0,1,2,\ldots,4m+1).
\]
Its first step has color zero. The following A-steps traverse the changed initial arm of P, so all first 2m+1 steps are color zero. The subsequent B-steps avoid every changed edge class and retain their baseline alternating colors, starting and ending with one. Their appended temporal word contributes precisely 2m+1 changes. Thus M_0=2m+1, completing the theorem. \(\square\)

**Scope and implication.** This family *satisfies* NORI1, since P is monochromatic from e_0. It is not a counterexample to the grand conjecture. Rather, it rules out dimension-uniform continuity of the rooted minimum switch count or its even tropical grade, even across one cube edge. The obstruction is geometric: four mutually incompatible families of edited edges, each small along a root-0 monotone path, suffice to produce a linear root gradient while preserving antipodal oddness. Any successful root-gluing argument must use information beyond scalar regularity of the rooted Bellman obstruction.### Linear neighboring-root switch disparity persists under vertex balance

Let c be the legal coloring of Q_n, n=4m+2, from (HL32), with M_c(0)=2m+1 and a monochromatic color-zero full path from e_0. Define its complementary paired lift L(c) on Q_{2n} with old bits x and new bits z by
\[
C_i(x,z)=c_i(x),\qquad C_{n+i}(x,z)=1+c_i(x)\pmod2,\qquad 0\le i<n.
\tag{HL37}
\]

**Theorem (balanced linear root gradient).** For every m>=1, the lift C is legal antipodally odd and has equal numbers of zero and one incident edges at every vertex. For every new-bit vector z, its adjacent roots (0,z) and (e_0,z) satisfy
\[
\boxed{M_C((0,z))\ge2m+1,\qquad M_C((e_0,z))=0.}\tag{HL38}
\]
For the even rooted tropical grades,
\[
\boxed{|h_C((0,z))-h_C((e_0,z))|\ge m+1=(N+4)/8,
\qquad N=2n=8m+4.}\tag{HL39}
\]

*Proof.* Each old/new direction pair has colors c_i and 1-c_i at every vertex, giving balanced incident degree. Both are independent of their own direction bits, and antipodal oddness is inherited from c, so C is legal.

Consider any full geodesic from (0,z) in the lift. Delete all steps in new directions. The remaining edges project to a full geodesic of c rooted at 0, and their temporal colors are a subsequence of the lift's temporal colors. Deleting symbols cannot increase the number of binary color changes. Thus every full lifted path from (0,z) has at least M_c(0)=2m+1 switches.

Now start from (e_0,z). Follow the old color-zero full geodesic P, but prepend all new directions n+i satisfying c_i(e_0)=1. These new edges are zero at initial old vertex e_0 because C_{n+i}=1+c_i(e_0)=0. After P, the old vertex is \bar e_0. Append every remaining new direction, for which c_i(e_0)=0. Antipodal oddness gives c_i(\bar e_0)=1, hence each appended new edge also has color zero. New rules ignore all new-bit states, so this construction traverses every old and new direction once with color zero. Thus M_C((e_0,z))=0. Equation (HL39) follows from h=ceil(M/2). \(\square\)

Therefore even the class of **perfectly vertex-balanced antipodally odd cubes** admits rooted minimum-switch obstructions with a linear jump across a single cube edge. Consequently local-Lipschitz, discrete harmonic, or root-continuity principles applied only to the scalar rooted switch-grade cannot prove NORI1 in the balanced reduction. Any viable root-selection argument must exploit stronger structure than balance and small root displacement. The constructed colorings themselves satisfy NORI1.
##### Root seam curl and the scalar-holonomy limitation

Let c be legal antipodally odd. Write A_x=K_{01}(x,\bar x), B_x=K_{10}(x,\bar x), t_x=(A_x+B_x)/2, s_x=(A_x-B_x)/2 for the rooted two-ended kernel. The antipodal identities give t_{\bar x}=t_x, s_{\bar x}=-s_x, s_x in {-1,0,1}.

For oriented root edge e=(x,y=x+e_i), write w_e=(-1)^{c_i(x)} and
D_e=K_{c_i(x),1-c_i(x)}(x,\bar x)-K_{c_i(x),1-c_i(x)}(y,\bar y).
The seam identities (HL30) say D_e=g_e^y-g_e^x, with g_e^x,g_e^y nonnegative even integers.

**Theorem (root-seam discrete Leibniz rule).**
\[
\boxed{D_{x\to y}=t_x-t_y+w_e(s_x-s_y)\in2\mathbb Z.}\tag{HL40}
\]
For an oriented cubical square with vertices v_0,v_1,v_2,v_3 and signed edge colors w_r along v_r to v_{r+1} (cyclic indices),
\[
\boxed{\Omega(Q):=\sum_{r=0}^3D_{v_r\to v_{r+1}}
=\sum_{r=0}^3(w_r-w_{r-1})s_{v_r}\in2\mathbb Z.}\tag{HL41}
\]
Only corners with two differently colored incident square edges can contribute. In particular monochromatic squares have zero seam circulation. This shows that ordinary square parity alone does not determine the oriented root-seam circulation.

*Proof.* For edge color b the chosen oriented off-diagonal kernel entry equals t_x+(-1)^b s_x. Subtract its value at y to obtain (HL40). Sum around Q: the t differences telescope and the remaining terms regroup to (HL41). Each coefficient w_r-w_{r-1} is 0 or plus/minus 2 depending on color agreement at that corner. \(\square\)

**Corollary (root-seam curvature is a coboundary).** Antipodal translation preserves this oriented edge assignment:
\[
\boxed{D_{\bar x\to\bar y}=D_{x\to y}.}\tag{HL42}
\]
Consequently D/2 descends to an integer one-cochain on the antipodal quotient root complex, and
\[
\boxed{\Omega/2=\delta(D/2).}\tag{HL43}
\]
Thus the cohomology class of the scalar seam curvature vanishes on the cube and on its antipodal quotient. A nonzero projective obstruction class cannot come from the curl of these scalar endpoint-forcing differences alone.

*Proof.* Antipodal translation swaps each rooted kernel's off-diagonal entries while complementing the color on the connecting edge; hence the selected entry is preserved at both ends. Formula (HL43) is the cellular coboundary definition. \(\square\)

**Corollary (forcing budget).** Summing over cube squares and undirected root edges,
\[
\boxed{\sum_Q|\Omega(Q)|\le(n-1)\sum_e(g_e^x+g_e^y).}\tag{HL44}
\]
Indeed \(|D_e|=|g_e^y-g_e^x|\le g_e^x+g_e^y\), and every cube edge belongs to n-1 squares.

The circulation can be nonzero: for the legal affine Q4 rules
c_0=x_1, c_1=x_0+x_2+x_3, c_2=x_0+x_1+x_3, c_3=x_0+x_1+x_2,
the root square (0,1,3,2) has rooted orientation values s=(-1,1,0,0) and edge-color word 0110, giving \(\Omega=-2\).

**Interpretation.** The scalar seam curvature is a nontrivial local observable supported at mixed-color square corners, but its integral cohomology class always vanishes. Therefore an argument seeking a nontrivial projective holonomy obstruction must retain additional noncommuting terminal-state transfers or path-incidence data, rather than only additive endpoint-forcing differences.### Forced root-gradient cost and a sharp one-sided seam penalty

Continue with the two-ended root kernel (HL24), its even grade h, and the nonnegative, even endpoint-forcing penalties g_e^x,g_e^y for neighboring roots x,y joined by edge e, defined in (HL29).

**Theorem (forcing-weighted local root continuity).**
\[
\boxed{|h_x-h_y|\le1+\frac12(g_e^x+g_e^y).}\tag{HL45}
\]
For any root path \(x=x_0,x_1,\ldots,x_\ell=y\),
\[
\boxed{|h_x-h_y|\le\ell+\frac12\sum_{r=0}^{\ell-1}
(g_{e_r}^{x_r}+g_{e_r}^{x_{r+1}}),\qquad e_r=x_rx_{r+1}.}\tag{HL46}
\]

*Proof.* By (HL24), either off-diagonal root entry has form \(2h+\epsilon\) with \(\epsilon\in\{-1,1\}\). Choose the edge-dependent oriented entry \(K_{b,1-b}\) for the edge color \(b=c(e)\). Hence
\[
2|h_x-h_y|\le |K_{b,1-b}(x,\bar x)-K_{b,1-b}(y,\bar y)|+2.
\]
The seam law (HL30) expresses the kernel difference as \(g_e^y-g_e^x\), whose absolute value is at most \(g_e^x+g_e^y\). Divide by two and sum along the root path. \(\square\)

**Theorem (sharp one-sided price in the linear root-jump family).** For the legal construction of (HL32) in dimension \(n=4m+2\), with x=0, y=e_0 and seam edge color b=0, the rooted kernels and common facet seam cost obey
\[
\boxed{
K_x=\begin{pmatrix}2m+2&2m+1\\2m+3&2m+2\end{pmatrix},\quad
K_y=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\quad E_0(x)=2m+1.
}\tag{HL47}
\]
Consequently
\[
\boxed{g_e^x=0,\qquad g_e^y=2m,\qquad
h_x=m+1,\quad h_y=0.}\tag{HL48}
\]
Equality holds in (HL45).

*Proof.* In the construction of (HL32), the full rooted-x path following directions \(0,1,\ldots,4m+1\) has temporal colors \(0^{2m+1}(10)^m1\). Its switch count is \(2m+1\), and its first and last colors are zero and one. The previous lower bound shows no rooted-x full path has fewer than \(2m+1\) switches. Thus the even diagonal of \(K_x\) equals \(2m+2\), and its 0-to-1 off-diagonal cost equals \(2m+1\). The complemented reversal symmetry of the rooted two-ended kernel gives the opposite off-diagonal entry \(2m+3\): a 1-to-0 cost of \(2m+1\) would require a path with that switch count starting in color one and ending zero. Such a path cannot exist here because every rooted-x path with the minimum switch count has its first edge of color zero and last edge of color one; this follows from the equality case in the path-editing bound in (HL32): the first and last baseline colors are respectively zero and one, and editing the maximum m entries cannot change either endpoint without sacrificing a switch reduction. [For an unconditional proof avoiding this equality-case characterization, the stronger claim about the other off-diagonal entry can be verified by induction on the four exceptional edge families; the weaker K_01 and grade values suffice for (HL48).]

The old root y has a monochromatic-zero full path by construction, so its kernel is \(\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\). The rooted-x path begins with the seam direction 0 and reaches its antipode with input-zero/output-one augmented cost \(2m+1\); hence the common facet conditional seam cost E is at most \(2m+1\). Unrestricted rooted K_01(x,\bar x) is also \(2m+1\), so E equals \(2m+1\). The forcing gap definitions give \(g_e^x=0,\ g_e^y=2m\). The displayed inequality (HL45) becomes \(m+1\le1+m\), giving equality. \(\square\)

**Interpretation.** The failure of unweighted root Lipschitz control is fully paid by an integer-valued dual endpoint-forcing penalty. In the linear-jump family the entire price is incurred at the favorable root's *opposite seam placement*: forcing direction zero to be last rather than allowing its successful monochromatic order costs \(2m\), while forcing it first at the difficult root costs nothing. This phenomenon survives vertex balance via the paired-lift reduction (HL37)--(HL39).

**Equality-case audit completing the other entry of (HL47).** The lower bound proof of (HL32) has a useful rigidity. Every rooted-zero full direction order has baseline color word \(0101\cdots01\), with \(4m+1\) switches. At most \(m\) of its temporal letters are changed by the recoloring. A change of an internal letter can remove at most two switches, while a change of the first or last letter can remove at most one. Therefore attaining the minimum \(2m+1\) switches requires \(m\) altered letters, all internal, and in particular leaves the first and last letters in their baseline colors zero and one. For an augmented root-zero path with virtual initial color one and virtual terminal color zero, a path with the minimum odd number \(2m+1\) of internal switches must consequently incur two additional boundary switches, for total \(2m+3\). A path with \(2m+2\) internal switches has equal first and last colors and necessarily pays one boundary switch for opposite prescribed terminal colors, again totaling at least \(2m+3\). Every path with at least \(2m+3\) internal switches clearly has augmented cost at least \(2m+3\). Thus \(K_{10}(0,\bar0)\ge2m+3\). The universal one-boundary-change estimate (HL24), combined with \(K_{00}=2m+2\), gives the reverse bound, proving the previously displayed full kernel matrix in (HL47) without relying on a finite-dimensional audit.
##### Tropical facet seam minimum is the projective Petrie variation

For a legal antipodally odd coloring c, associate to each undirected cube edge e={x,x+e_i}, of color b, the common oriented-facet seam cost
\[
E(e)=K_{b,1-b}(x+e_i,\bar x),
\]
using the two-ended geodesic kernel on the (n-1)-face with direction i omitted.

**Theorem (seam-cyclic identification).** This cost is independent of the choice of endpoint x of e, is always a positive odd integer, and satisfies
\[
\boxed{\min_{e\in E(Q_n)}E(e)=\mu(c)+1,}\tag{HL49}
\]
where \(\mu(c)\) is the minimum ordinary switch count on any full antipodal geodesic. In particular NORI1 holds for c if and only if some seam edge has E(e)=1. In the hypothetical one-defect normalization, the minimum seam cost would be 3.

*Proof.* Reversing a facet path after antipodal translation sends its temporal word \(w_1,\ldots,w_{n-1}\) to \(1-w_{n-1},\ldots,1-w_1\). Its virtual boundary cost from b to 1-b is preserved:
\[
[b\ne w_1]+\operatorname{sw}(w)+[w_{n-1}\ne1-b]
=[b\ne(1-w_{n-1})]+\operatorname{sw}(w)+[(1-w_1)\ne1-b].
\]
This proves orientation independence. The virtual endpoints b and 1-b are opposite, so the augmented switch count is odd and at least one.

Every full geodesic P begins with some direction i and edge color b. Removing that first edge gives a facet path whose augmented seam cost is
\[
\operatorname{sw}(P)+[\text{last color of P}\ne1-b]
=2\left\lfloor\frac{\operatorname{sw}(P)}2\right\rfloor+1.
\tag{HL50}
\]
Conversely every facet seam path extends to a full geodesic by prepending its corresponding seam edge, with the same relation. Thus \(\min_e E(e)=2\lfloor\mu(c)/2\rfloor+1\). The established antipodal cyclic root-slide theorem makes \(\mu(c)\) even: any full word with an odd number of internal switches has a root slide across one switch reducing their count by one. Hence (HL49). \(\square\)

The quantity in (HL50) is also the number of changed comparisons on the associated projective Petrie cycle, including the comparison from the terminal edge to the antipodal mate of the initial edge. Thus (HL49) is a two-state min-plus expression of the established projective odd-turn-girth identity. It identifies the shared facet seam kernel as a useful interface between the Hollom control formulation and the existing projective-cycle/matroidal formulation; the odd-girth equivalence itself is not claimed as a new proof of NORI1.
##### A noncontractible rainbow cycle of fully calibrated minimum-energy seams

Let c be a legal antipodally odd coloring, \(\mu(c)\) its minimum full-geodesic switch count, and \(E(e)\) the odd shared-facet seam energy (HL49). For any undirected edge e with endpoints x,y and color b, denote by \(g_e^x,g_e^y\) the nonnegative even endpoint-forcing gaps (HL29).

**Theorem (critical calibrated Petrie loop).** Suppose c has **no** monochromatic full antipodal geodesic but does have a rooted full geodesic P whose temporal color word is \(0^a1\,0^b\), \(a,b\ge1\). The projection of P onto the antipodal quotient \(Q_n/(x\sim\bar x)\) is a simple direction-rainbow n-cycle \(\Gamma\), representing the nontrivial antipodal covering monodromy. Every edge orbit on \(\Gamma\) satisfies
\[
\boxed{E(e)=3,\qquad g_e^x=g_e^y=0.}\tag{HL51}
\]
Moreover \(\Gamma\) has precisely three changed-color turns, at three distinct quotient vertices, and at each of those vertices one rooted lift has full two-ended antipodal kernel
\[
\boxed{K_x=\begin{pmatrix}2&3\\3&2\end{pmatrix},\quad h_x=1,\quad s_x=0.}\tag{HL52}
\]
Thus, if unrestricted NORI1 is false, the established direction-gauge one-defect normalization (GD4) produces a legal counterexample containing such a noncontractible, fully calibrated minimum-energy rainbow cycle.

*Proof.* Let the direction order of P be \(i_1,\ldots,i_n\) and its vertices \(v_0,\ldots,v_n=\bar v_0\). No two vertices \(v_r,v_s\), \(0\le r<s<n\), represent the same antipodal quotient vertex: equality would repeat a monotone subset, while antipodal equality would require all n directions between them, possible only for the endpoints \(r=0,s=n\). Hence the projected path is a simple n-cycle using every direction once. It lifts to a path joining antipodal vertices, so its quotient cycle has nontrivial covering monodromy.

Extend P's edge-color word antiperiodically, so its closing comparison is between its last color zero and the antipodal complement of its first color, namely one. Its ordinary two internal switch positions are the boundaries of the exceptional one edge. The closing comparison supplies a third switch. The projective cyclic turn count is therefore three. Each projective cycle edge can be selected as the first seam of a cyclic root rotation. Its full cyclic turn count is three, hence its facet seam energy is at most three by (HL50). Since c is a counterexample, the global minimum seam energy equals \(\mu(c)+1\ge3\) by (HL49), so each cycle edge has E=3.

For any root in a legal counterexample, either oriented off-diagonal entry of its rooted two-ended kernel is an odd integer at least three: if it were one, the witnessing full geodesic would have at most one ordinary switch, and cyclic root sliding would produce a monochromatic one. Therefore each endpoint-root oriented entry appearing in (HL29) is at least three. As its common seam energy equals three, both nonnegative forcing gaps vanish. This proves (HL51).

In the projective cyclic word, a root slide across one of its three changed comparisons removes that changed turn and produces a full word with precisely two ordinary switches. The three selected root positions are distinct quotient vertices by simplicity of the cycle. A legal counterexample admits no full geodesic with fewer than two switches, so at each of these roots the minimum switch count is two and (HL31) gives the displayed kernel (HL52). Finally the direction-gauge normalization (GD4) makes any hypothetical counterexample a new bad coloring possessing an interior one-defect witness; the preceding proof applies. \(\square\)

**Interpretation and limitation.** The three-turn projective rainbow cycle and its homological monodromy are already part of the established Petrie-cycle framework. The added conclusion is that *all n of its seams simultaneously saturate the tropical facet lower bound and have both endpoint-forcing penalties zero*. Hence an obstruction cannot be challenged by assuming that some seam in a critical cycle necessarily has positive local penalty: every seam is already locally calibrated. What remains is the consistency of multiple calibrated square-exchange alternatives to this noncontractible cycle, retaining the direction-rainbow condition and the common edge coloring.

##### Fully calibrated three-turn loop in a successful six-cube

**Theorem (calibration is not a failure certificate).** On Q_6, define the legal antipodally odd coloring
\[
\boxed{c_{2j}(x)=x_{2j+1},\qquad c_{2j+1}(x)=x_{2j},\quad j=0,1,2.}\tag{HL53}
\]
Let P begin at integer vertex 12, with direction order (0,1,2,3,4,5). Its temporal word is 011001, giving a projective Petrie cycle C of grade three. At all six quotient vertices v of C, the rooted two-ended antipodal kernel equals
\[
\boxed{K_v=\begin{pmatrix}2&3\\3&2\end{pmatrix}.}\tag{HL54}
\]
At each of the six edge orbits e=uv of C, the shared facet seam energy and both endpoint forcing gaps satisfy
\[
\boxed{E(e)=3,\qquad g_e^u=g_e^v=0.}\tag{HL55}
\]
Nevertheless the same coloring has a monochromatic zero full geodesic starting at integer vertex 21, with direction order (0,1,2,3,4,5) and temporal word 000000.

*Proof.* In a single paired Q_2 factor with root bits 00, both antipodal direction orders have word 01; with root bits 11, both have word 10; and with root bits 01 or 10, the two orders have monochromatic words 00 and 11. Their respective two-ended matrices are
\[
K^{01}=\begin{pmatrix}2&1\\3&2\end{pmatrix},\quad
K^{10}=\begin{pmatrix}2&3\\1&2\end{pmatrix},\quad
K^{\rm mono}=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
The six rooted vertices along P are 12,13,15,11,3,19. Their factor-type triples are respectively
\[
(01,10,01),\quad
({\rm mono},10,01),\quad
(10,10,01),\quad
(10,{\rm mono},01),\quad
(10,01,01),\quad
(10,01,{\rm mono}).
\]
Each triple contains both a forced 01 and a forced 10 factor. The two-ended tropical product law (HL23) takes the entrywise maximum, giving the claimed critical matrix at every rooted vertex.

The word 011001 has three internal color changes, and its projective closing comparison is unchanged, so C has three projective turns. Choosing any cycle edge as the first seam of a cyclic rotation gives a facet path with augmented cost three, hence E(e)<=3. The selected oriented kernel entries at both endpoint roots are three by the displayed rooted matrices; endpoint forcing cannot improve on them, so E(e)=3 and both gaps vanish. Finally root 21 has first bit one and second bit zero in each paired factor, and following the first direction then second in each factor yields word 00; concatenation gives 000000. \(\square\)

Thus the *entire* tropical calibration certificate derived from a hypothetical counterexample in (HL51)--(HL52) can occur in a successful legal coloring. The example has three internal switches rather than the special single-exception pattern of (GD4), so it does not exclude an exchange argument exploiting that stronger hypothesis. Calibration of one cycle, even at every seam, cannot by itself imply the absence of one-turn cycles elsewhere.



##### Rooted switch kernels survive odd feedforward extensions

For a nonempty full antipodal geodesic with color word \(w\), write
\[
C_{ab}(w)=[a\ne w_1]+\operatorname{sw}(w)+[w_n\ne b],
\qquad K^c_{ab}(x)=\min_{P:x\to\bar x}C_{ab}(w(P)).
\]
The minimum ranges over full geodesics. Add a new direction \(r\), leave all old direction rules independent of its bit, and give its edges color \(g(x)\), where \(g(\bar x)=1-g(x)\).

**Theorem (rootwise feedforward invariance).** For every old root \(x\), new bit \(z\), and virtual colors \(a,b\),
\[
K^{c^+}_{ab}(x,z)=K^c_{ab}(x).
\]
The analogous terminal-only minima and the ordinary minimum switch count \(M(x)\) are also preserved. These conclusions iterate through any sequence of odd feedforward extensions, whose new rules may read earlier added bits.

*Proof.* Every old full geodesic extends to a new full geodesic with the same first color, last color, and collapsed run word. If its word has a switch, insert the new step at a switching vertex. Its color there is one of the two adjacent colors, so it extends the corresponding run. Old edges retain their colors because their rules ignore the new bit. If the old word is monochromatic with color \(\alpha\), oddness of \(g\) makes one of its values at the two antipodal old endpoints equal to \(\alpha\); insert the new step at that endpoint. This proves each upper bound. Conversely, deleting the new step from any extended geodesic gives an old full geodesic. Deleting a letter cannot increase the number of changes, including either or both virtual endpoint colors. This proves each lower bound. Apply the argument successively for feedforward additions. \(\square\)

Only the minima and the existence of a run-preserving extension are asserted; an extended path can have additional runs that disappear on projection.

**Corollary (a square-root root-average obstruction within the balanced class).** There are perfectly balanced legal odd colorings on \(N=2d\) directions, for every positive even \(d\), with
\[
\mathbb E M=\frac{(d+1)\binom d{d/2}}{2^d}-1
=\sqrt{N/\pi}-1+O(N^{-1/2}),
\]
while the fraction of roots admitting a monochromatic full geodesic is
\[
\frac{\binom d{d/2}}{2^d}\sim\frac{2}{\sqrt{\pi N}}.
\]

*Proof.* On the old \(d\)-cube take \(c_i(x)=\bigoplus_{j\ne i}x_j\). This coloring is antipodally odd since \(d-1\) is odd. At a root of weight \(t\), the \(k\)-th edge in order \(\pi\) has color
\[
\left(\bigoplus_jx_j\right)\oplus x_{\pi_k}\oplus(k-1\bmod2).
\]
Two consecutive colors differ precisely when the corresponding initial bits agree. Among words with \(t\) ones and \(d-t\) zeros, the least number of equal adjacent pairs is
\[
M(x)=\max\{0,|d-2t|-1\}.
\]
For even \(d\), this is zero precisely at \(t=d/2\). With \(T\) binomial \((d,1/2)\), the elementary binomial identity
\(\mathbb E|d-2T|=d\binom d{d/2}/2^d\)
gives the stated mean.

For each old direction \(i\), add a companion with rule \(1-c_i(x)\). Each pair has complementary incident colors at every vertex, so the resulting \(2d\)-cube is perfectly balanced. These are odd feedforward additions. The theorem preserves \(M(x)\) for every assignment of the new bits. Stirling's formula gives the asymptotics. \(\square\)

Hollom's general root-average square-root scale is already known to be optimal. The conclusion here is that this obstruction persists pointwise through the complementary balancing construction, within the counterexample-universal paired class. In particular, a uniform constant upper bound for the root-averaged minimum switch count cannot follow from perfect balance. Root selection remains essential.

##### Hollom response as Eulerian circulation

Retain \(T_{i,k}\), \(\Phi_k\), and \(\mathscr L\) from (HL1)--(HL3), and suppose the coloring is perfectly balanced. Give each cube edge the reference orientation from its even endpoint \(u\) to its odd endpoint \(v\). Write \(J(e)=1\) for red and \(J(e)=-1\) for blue, and define the antisymmetric edge form by its reference value
\[
\omega_k(e)=\frac{T_{i,k}(u)+T_{i,k}(v)}2
\quad(e\text{ in direction }i).
\]

**Theorem (response circulation identity).** The signed current \(J\) is divergence-free, and
\[
\Phi_k-\Phi_{k-1}
=-\frac{\langle J,\omega_k\rangle}{n2^n}-\mathbb E_k\mathscr L.
\]
For any decomposition of the canonical Eulerian orientation into directed cycles,
\[
\langle J,\omega_k\rangle=\sum_C\oint_C\omega_k.
\]
The pairing is unchanged on replacing \(\omega_k\) by \(\omega_k+d\psi\).

*Proof.* Perfect balance gives zero signed incidence sum at each vertex, hence zero divergence. For the two endpoints of a direction-\(i\) edge, its incidence color is the same. Since \(\bar r=1/2\),
\[
\sum_{y,i}(r_i(y)-1/2)T_{i,k}(y)
=\sum_{e=uv}\frac{J(e)}2(T_{i,k}(u)+T_{i,k}(v)).
\]
Substitute in (HL3). An Eulerian decomposition partitions the edge current, giving the cycle formula. The gradient contribution vanishes by summation by parts against the divergence-free current. \(\square\)

Suppose further that the directions have a fixed complementary pairing: the two rules of each pair are complementary functions independent of both bits in that pair. Each paired two-face is then a directed square in the canonical orientation. These squares partition the edges, and there are \(n2^{n-3}\) of them. Let \(\overline\Omega_k\) be their mean oriented \(\omega_k\)-circulation. Then
\[
\boxed{\Phi_k-\Phi_{k-1}=-\overline\Omega_k/8-\mathbb E_k\mathscr L.}
\]
Consequently a counterexample in this class must satisfy
\[
-\sum_{k=1}^{n-1}\overline\Omega_k
\ge16+8\sum_{k=1}^{n-1}\mathbb E_k\mathscr L,
\]
by (HL5). At rank one,
\[
T_{i,1}(y)=-\frac{2n}{n-1}(r_i(y)-1/2),
\quad \omega_1(e)=-\frac n{n-1}J(e),
\quad\overline\Omega_1=-\frac{4n}{n-1}.
\]
Indeed \(D(y+e_j,y)\) equals \(-1\) on a red edge and \(1\) on a blue edge; conditioning on inclusion of \(i\) and using balance gives the displayed response.

These circulations concern optimal terminal-color responses. They differ from raw color parity around a square and from the rooted facet seam energies. The preceding balanced family shows that the cumulative response budget, even after subtracting Bellman dissipation, can grow on the square-root scale in successful colorings. A useful closure inequality must therefore retain root selection or additional structure of a hypothetical obstruction, rather than impose a constant bound on this budget for every balanced coloring.

**Finite audit.** Independent subset dynamic programming checked the root-switch formula on the balanced lifts with \(N=4,8\). Rational arithmetic checked the response identity at all three ranks of the \(N=4\) lift: the total currents are \(-128/3,-64/3,-32/3\), the mean slacks are \(0,1/12,1/12\), and the successive potentials are \(2/3,11/12,1\). These checks support the formulas; the dimension-uniform conclusions follow from the proofs above.


#### Sharp order-template complexity for direction-indexed color profiles

For a legal coloring \(c\) and a permutation \(\pi\in S_n\), let
\[
W_\pi(c)=\{w(x,\pi):x\in Q_n\}\subseteq\mathbb F_2^n,
\]
where \(w_i(x,\pi)\) is the color encountered when direction \(i\) is traversed. The global profile set is \(W(c)=\bigcup_\pi W_\pi(c)\). For \(s\in\mathbb F_2^n\), define the direction-gauge recoloring \(c^s_i(x)=c_i(x)\oplus s_i\). This recoloring remains legal and satisfies \(W_\pi(c^s)=W_\pi(c)\oplus s\).

**Theorem (minimum fixed-order image).** For every legal coloring of \(Q_n\), \(n\ge2\), and every permutation \(\pi\),
\[
\boxed{|W_\pi(c)|\ge4.}\tag{OT1}
\]
The bound is sharp simultaneously for every permutation, for every \(n\ge2\).

*Proof.* Write \(F(x)=w(x,\pi)\). Antipodal oddness gives \(F(\bar x)=\mathbf1\oplus F(x)\), so the image consists of complement-pairs. For each \(i\), \(F_i(x)\) ignores the input bit \(x_i\): the prefix preceding direction \(i\) excludes that direction, and \(c_i\) ignores its own bit. Suppose the image had only two members \(a,\bar a\). Then \(F(x)=a\oplus h(x)\mathbf1\) for one Boolean function \(h\). Because every output \(F_i\) ignores \(x_i\), \(h\) ignores every input bit, hence is constant. This contradicts \(F(\bar x)=\mathbf1\oplus F(x)\). The image is nonempty and complement-invariant, so its cardinality is at least four. The coloring below attains four. \(\square\)

**Theorem (sharp exponential obstruction to predetermined orders).** Fix \(n\ge2\). There is a legal affine coloring \(c^\star\) such that
\[
\boxed{\min\{|P|:P\subseteq S_n,\quad\bigcup_{\pi\in P}W_\pi(c^\star)=\mathbb F_2^n\}
=2^{n-2}.}\tag{OT2}
\]
In particular, for every coloring-independent collection \(P\) of fewer than \(2^{n-2}\) direction permutations, there is a legal affine coloring \(d\) for which no order in \(P\) gives a monochromatic full antipodal geodesic, from any starting root and in either color.

*Proof.* Set
\[
c^\star_0(x)=x_1,\qquad c^\star_i(x)=x_0\quad(1\le i<n).
\]
Every rule ignores its own bit and is reversed by antipodal complementation. For a fixed order \(\pi\), let \(S_\pi\subseteq\{1,\ldots,n-1\}\) be its directions occurring after direction zero. Then
\[
w_i(x,\pi)=x_0\oplus\mathbf1_{\{i\in S_\pi\}}
\quad(i\ge1),
\]
and
\[
w_0(x,\pi)=x_1\oplus\mathbf1_{\{1\text{ occurs before }0\}}.
\]
Thus \(W_\pi(c^\star)\) comprises four vectors: the zero-direction bit is arbitrary, while the vector in the other \(n-1\) slots is either \(\mathbf1_{S_\pi}\) or \(\mathbf1_{\bar S_\pi}\). As \(S_\pi\) ranges over all subsets, these four-element sets form a partition of \(\mathbb F_2^n\), indexed by the \(2^{n-2}\) complementary pairs \(\{S,\bar S\}\) of subsets of \(\{1,\ldots,n-1\}\). Every subset \(S\) is realized by putting its complement before direction zero and \(S\) afterward. This proves (OT2).

If \(|P|<2^{n-2}\), its profile union omits some vector \(s\). Direction-gauge recoloring \(d=(c^\star)^s\) makes a full path red precisely when its original profile is \(s\). Hence none of the tested orders admits a red full geodesic. If one of them admitted a blue full geodesic, translating its starting root antipodally while retaining the same order would give a red full geodesic, a contradiction. This proves the last assertion. \(\square\)

**Interpretation and limitation.** The existing rotation-orbit theorem (RO1) and full affine-span theorem establish strong constraints on \(W(c)\) for all legal colorings, but do not control the number of orders needed to cover its attainable profiles. This sharp exponential obstruction already occurs in affine colorings; therefore no fixed family of subexponentially many direction orders can guarantee a monochromatic geodesic for every legal coloring. The theorem concerns coloring-independent order templates: an algorithm choosing orders in response to the coloring is outside its scope. It neither asserts nor refutes the unrestricted NORI1 conjecture.


**Corollary (full derivative data cannot select a small universal order template).** The \(2^n\) legal colorings \(c^{\star,s}_i=c^\star_i\oplus s_i\), \(s\in\mathbb F_2^n\), used in (OT2) have identical nonconstant Boolean derivative data: for every \(i\), every nonempty set \(J\subseteq[n]\), and every \(x\),
\[
\partial_J c^{\star,s}_i(x)=\partial_J c^\star_i(x).
\]
In particular they have the same directed influence graph and the same pattern of noncommuting direction pairs. If a method assigns to each coloring a set of direction orders using only its Boolean derivatives of positive order (or any invariant determined by those derivatives), and promises that some assigned order supports a monochromatic full antipodal geodesic, then that method must assign at least \(2^{n-2}\) orders to this common derivative class.

*Proof.* Every nonempty Boolean derivative annihilates an additive constant \(s_i\), proving identical derivative data. The method must therefore assign the same order family \(P\) to all \(c^{\star,s}\). By (OT2), fewer than \(2^{n-2}\) orders miss a direction-indexed profile \(s\) in the base coloring, so the recoloring \(c^{\star,s}\) has no monochromatic full antipodal geodesic with any order in \(P\). \(\square\)

**Signed-order cancellation obstruction.** For the same star-reader coloring \(c^\star\), in every dimension \(n\ge3\) and at every root \(x\),
\[
\boxed{
\sum_{\substack{\pi\in S_n:\\(x,\pi)\text{ is a red full geodesic}}}
\operatorname{sgn}(\pi)=0.}\tag{OT3}
\]
Indeed red direction steps \(i\ge1\) require \(x_0=0\) before direction zero and \(x_0=1\) afterward. Thus any all-red full word has direction zero first (when \(x_0=1\)) or last (when \(x_0=0\)), with all \(n-1\) remaining directions in an arbitrary order. The direction-zero rule \(c_0=x_1\) determines whether that root permits the corresponding placement but imposes no restrictions on the internal order. For \(n-1\ge2\), the \(S_{n-1}\) alternating signs cancel. Nevertheless this coloring has
\[
N_R(c^\star)=2^{n-1}(n-1)!>0
\]
rooted red full geodesics. Hence nonvanishing of the alternating-signed full-geodesic count at some root is a false strengthening of NORI1 in every dimension \(n\ge3\).


#### Unary-reader betweenness and sharp universal-order systems in dimensions three and four

Let \(n\ge3\), choose a map \(r:[n]\to[n]\) with \(r(i)\ne i\), and constants \(\varepsilon_i\in\mathbb F_2\). Set
\[
c_i(x)=x_{r(i)}\oplus\varepsilon_i.
\tag{UB1}
\]
These are legal antipodally odd edge colors. For a direction permutation \(\pi\), write \(j\prec_\pi i\) when \(j\) is visited before \(i\).

**Theorem (reader-betweenness certificate).** An order \(\pi\) supports a monochromatic full antipodal geodesic, from some starting vertex, if and only if for each \(j\in\operatorname{im}r\), the values
\[
\boxed{\varepsilon_i\oplus\mathbf1_{\{j\prec_\pi i\}},
\qquad i\in r^{-1}(j)}
\tag{UB2}
\]
are all equal. When this holds, for each specified color there are \(2^{n-|\operatorname{im}r|}\) starting roots giving a monochromatic full geodesic in that order. Thus the good order set is the solution set of a family of elementary precedence/betweenness constraints.

*Proof.* At the moment direction \(i\) is traversed, its reader bit \(x_{r(i)}\) has been toggled if and only if \(r(i)\prec_\pi i\). Its edge color is therefore
\[
x_{r(i)}\oplus\varepsilon_i\oplus\mathbf1_{\{r(i)\prec_\pi i\}}.
\]
To make every edge have a prescribed common color \(t\), solve the equation \(x_{r(i)}=t\oplus\varepsilon_i\oplus\mathbf1_{\{r(i)\prec_\pi i\}}\) for each direction. Equations with different reader bits are independent, and those sharing a reader agree precisely under (UB2). Each reader bit is then prescribed, while the \(n-|\operatorname{im}r|\) other starting bits are free. \(\square\)

**Theorem (one successful unoriented order in \(Q_3\) and \(Q_4\)).** For \(n=3\), the affine legal coloring
\[
c_0=1\oplus x_1,\qquad c_1=x_2,\qquad c_2=x_1
\tag{UB3}
\]
admits monochromatic full antipodal geodesics only in orders \((0,1,2)\) and \((2,1,0)\).

For \(n=4\), the coloring
\[
\boxed{c_0=1\oplus x_1,\quad c_1=1\oplus x_2,\quad
c_2=x_1,\quad c_3=x_2}
\tag{UB4}
\]
admits them only in orders \((0,1,2,3)\) and \((3,2,1,0)\). All listed orders admit both colors with suitable roots.

*Proof.* In (UB3), directions zero and two share reader one and have opposite additive constants. Condition (UB2) forces direction one between zero and two, leaving only the two listed orders.

In (UB4), directions zero and two share reader one with opposite constants, forcing direction one between zero and two. Directions one and three share reader two with opposite constants, forcing direction two between one and three. These two betweenness relations force \(0\prec1\prec2\prec3\), or its reversal. By (UB2), each listed order admits \(2^{4-2}=4\) starting roots in each color. The three-dimensional example admits \(2^{3-2}=2\) roots in each color per listed order. \(\square\)

Define a *universal order family* \(P\subseteq S_n\) to be a set of direction orders such that every legal coloring of \(Q_n\) has a monochromatic full antipodal geodesic whose order belongs to \(P\). Let \(u_n\) be its minimum size when such families exist.

**Corollary (minimum universal families at small dimension).**
\[
\boxed{u_3=3,\qquad u_4=12.}\tag{UB5}
\]
In particular, the prior dimension-uniform template lower bound \(2^{n-2}\) is not sharp at \(n=3,4\).

*Proof.* Permuting direction names in either witness (UB3) or (UB4) realizes an arbitrary chosen reversal pair as the only successful order pair. Thus a universal \(P\) must include at least one representative of every reversal pair, requiring \(n!/2\) orders. Conversely, monochromatic full geodesic existence in these dimensions has been verified by enumerating all \(2^6=64\) legal colorings of \(Q_3\) and all \(2^{16}=65536\) legal colorings of \(Q_4\). Every enumerated coloring has at least one successful order. Reversing a monochromatic path preserves its color, so taking one order from each reversal pair then gives a universal family of size \(n!/2\).

For reproducibility, encode a legal coloring by one binary choice on each orbit of undirected edges under antipodal translation. Enumerate orbits by scanning canonical edges \((x,x\oplus e_i)\), \(x<x\oplus e_i\), first in increasing \(x\), then \(i\). For each orbit bit assignment, check all roots and all direction permutations; a permutation is successful if its path-color word is constant for some root. The enumeration found no coloring with an empty successful-order set; its seven different successful-order masks in dimension three are the seven nonempty unions of three reversal pairs. In dimension four it found 1093 distinct successful-order masks, none empty, including every singleton reversal pair. \(\square\)

**Scope.** The formulas give a dimension-uniform certificate for unary-reader colorings and explicit small-dimensional obstructions for fixed-order proof templates. The factorial template lower bound for all dimensions remains unproved. A finite search over all \(1{,}048{,}576\) legal affine colorings of \(Q_5\) found at least two successful reversal pairs in each, so the particular four-direction gadget does not immediately extend to dimension five inside the affine class. The universal NORI1 conjecture is not resolved by these findings.


##### Rootwise affine profile-hull rigidity

For a legal odd coloring \(c\) of \(Q_n\), let \(w(x,\pi)\in\mathbb F_2^n\) record the full geodesic edge colors by direction and set \(\mathcal W_x=\{w(x,\pi):\pi\in S_n\}\).

**Theorem.** There is a root-independent binary subspace \(L(c)\subseteq\mathbb F_2^n\) with a basis of disjoint nonempty even-size support indicators, such that
\[
\boxed{\operatorname{aff}\mathcal W_x=x+\operatorname{aff}\mathcal W_0,\qquad
\dim\operatorname{aff}\mathcal W_x=n-\dim L(c)\ge\lceil n/2\rceil.}
\tag{RHA1}
\]
Both dimension bounds are attained for every \(n\ge2\).

*Proof.* Define \(L_x\) as the annihilator of all differences \(w(x,\pi)+w(x,\sigma)\). By exchanging adjacent directions \(i,j\) after an arbitrary prefix set \(S\) of other directions, \(y\in L_x\) if and only if the weighted edge rule \(\omega_i=y_i c_i\) has zero square curl. Varying \(S\) visits every \(ij\)-square, irrespective of the fixed root, so \(L_x=L(c)\) for all \(x\). The square condition is
\[
y_i\Delta_jc_i(z)+y_j\Delta_ic_j(z)=0
\quad(z\in Q_n,\ i\ne j).
\tag{RHA2}
\]
For each fixed square its solution condition is one of \(y_i=0\), \(y_j=0\), \(y_i=y_j\), or vacuous. All these conditions are preserved under bitwise AND as well as XOR. Thus \(L(c)\) is a Boolean subring of \(\mathbb F_2^n\), whose minimal nonempty support sets are disjoint atoms, and all supports are unions of these atoms.

For \(y\in L(c)\), closedness of \(\omega\) implies \(\omega_i(z)=\phi_y(z)+\phi_y(z+e_i)\) for some vertex potential. Hence every full geodesic has weighted color sum
\[
y\cdot w(x,\pi)=g_y(x):=\phi_y(x)+\phi_y(\bar x).
\]
Oddness gives \(g_y(x+e_i)+g_y(x)=\omega_i(x)+\omega_i(\bar x)=y_i\); thus \(g_y(x)=g_y(0)+y\cdot x\). But \(g_y(\bar x)=g_y(x)\), so \(y\cdot\mathbf1=0\). Each atom therefore has even size, yielding \(\dim L\le\lfloor n/2\rfloor\). Since the affine annihilator is \(L\), all affine hulls are cosets of \(L^\perp\). The relation \(g_y(x)=g_y(0)+y\cdot x\) implies the claimed root-translation law.

For sharpness, use pairs \((a_r,b_r)\) with \(c_{a_r}(z)=z_{b_r}, c_{b_r}(z)=z_{a_r}\). Then \(L\) consists of vectors constant on each pair, with dimension \(\lfloor n/2\rfloor\). For odd \(n\), add a last direction \(k\) with \(c_k(z)=z_0\), forcing \(y_k=0\) but not constraining the pair indicators. \(\square\)

**Limitation.** For the legal odd \(Q_3\) coloring \(c_0=x_1,c_1=x_2,c_2=x_0\), the space \(L\) is zero, so every rooted affine hull equals \(\mathbb F_2^3\). Nevertheless at root zero the six direction orders realize precisely the six nonconstant profiles; neither \(000\) nor \(111\) occurs at that root. Thus full affine-hull dimension does not imply rootwise profile completeness.

**Fixed-order converse.** For any selected permutation \(\pi\), the full profile maps \(F_\pi:x\mapsto w(x,\pi)\) are precisely the antipodally odd maps \(F:Q_n\to Q_n\) whose \(i\)-th output ignores input bit \(i\). Necessity follows from legal edge coloring. For sufficiency, let \(P_i\) be the preceding-direction mask and prescribe \(c_i(z)=F_i(z+P_i)\). Every such map has at least four output patterns for \(n\ge2\), sharply: an image of only \(\{u,\bar u\}\) would require a common odd scalar \(h(x)\) independent of every input bit, impossible; the map \(F_0=x_1,F_i=x_0\ (i\ge1)\) has four outputs.


**Corollary (complete fixed-root two-direction prescription).** For any fixed root \(x\in Q_n\), any two directions \(i\ne j\), and target pair \((a,b)\in\mathbb F_2^2\), there exists a full geodesic from \(x\) whose direction-\(i\) and direction-\(j\) colors are \((a,b)\), unless
\[
c_i(z)=z_j+\alpha,\qquad c_j(z)=z_i+\beta\qquad(z\in Q_n)
\tag{RHA4}
\]
for some constants \(\alpha,\beta\). In the exceptional case the realized pair set at \(x\) consists of precisely two complementary pairs and satisfies
\[
w_i(x,\pi)+w_j(x,\pi)=x_i+x_j+\alpha+\beta+1
\quad\text{for every }\pi.
\tag{RHA5}
\]
The exceptional pairs form a matching of directions, so at most \(\lfloor n/2\rfloor\) direction pairs fail four-pattern prescription at any root.

*Proof.* Reversing any full order while keeping \(x\) fixed complements each direction-indexed color: the predecessor set of direction \(i\) becomes its complement among all other directions, so legality and oddness give \(w(x,\pi^{\rm rev})=\mathbf1+w(x,\pi)\). Thus the projection of \(\mathcal W_x\) to the chosen two bits is complement-invariant. If it does not realize all four bit pairs, it realizes a single complementary pair, so \(w_i+w_j\) is independent of the order. By (RHA2), this is equivalent to the square-closedness of the cochain with nonzero labels only in directions \(i,j\). On each square of directions \(i,k\) for \(k\notin\{i,j\}\), closedness forces \(\Delta_k c_i=0\); similarly \(\Delta_k c_j=0\). Since \(c_i\) ignores bit \(i\) and is antipodally odd, it must then have the form \(c_i=z_j+\alpha\), and likewise \(c_j=z_i+\beta\). Conversely (RHA4) makes all weighted square curls vanish and yields (RHA5) by either relative ordering of \(i,j\). The two complementary pairs both occur by reversing an order. Two exceptional pairs cannot share a direction because an edge rule cannot equal both different input bits up to constants. \(\square\)

**Explicit four-witness decoder.** If (RHA4) fails, the weighted cochain supported on \(\{i,j\}\) has a square of nonzero flux, in some pair of square directions \(p,q\). Choose a prefix of the full direction order so that the square reached from the prescribed root \(x\) is that square; interchange the adjacent directions \(p,q\) and keep the suffix unchanged. This produces two full paths from \(x\) with opposite \((i,j)\)-color parity. Reverse each order, still rooted at \(x\), to complement both profile bits, producing all four prescribed pairs. The construction uses at most four explicit full paths once the nonzero-flux square has been identified.

**Sharp failure for three directions.** On \(Q_n\), \(n\ge3\), put \(c_0=x_1,c_1=x_2,c_2=x_0\), and for \(k\ge3\) put \(c_k=x_0\). These rules are legal and odd. For root zero, restriction of any full path color profile to directions \(0,1,2\) is determined solely by their relative order and consists precisely of the six nonconstant three-bit words; neither \(000\) nor \(111\) can occur on these three directions. Nevertheless every pair of these three directions admits all four patterns. Thus the two-direction prescription theorem cannot be extended to three directions using only legal oddness and a fixed root.


##### Cyclic reader rooted support obstruction

For n>=3 define c_i(z)=z_(i+1 mod n), a legal odd edge coloring. At a root x set b_i=x_(i+1). The full direction-indexed color profiles are all binary words except b and its complement. Proof: desired colors orient the cyclic precedence constraints between i and i+1; a total order exists unless all comparisons orient the cycle consistently. At root zero every nonconstant word occurs, and every proper-subset color prescription occurs, yet neither monochromatic profile does. For a given full profile precisely two antipodal roots fail to realize it. The constructive order comes from topological sorting. This does not contradict NORI1, since every other root realizes both monochromatic profiles. A full generalization and proof for arbitrary unary-reader functional digraphs is preserved in research note note_dcf71a720b27f7b6e3f7521f, version 2.


#### Tournament comparison gauges: uniform profiles and the order constraint

Let \(c_i(x)\) be any legal antipodally odd edge coloring of \(Q_n\), and set \(m=\binom n2\). An arbitrary comparison system \(b\) is a family of bits \(b_i(j)\) for \(i\ne j\) satisfying \(b_i(j)\oplus b_j(i)=1\); if transitive, it encodes a complete direction order with \(b_i(j)=1\) when \(j\) precedes \(i\). Define the relaxed color profile
\[
W_i(x,b)=c_i\left(x\oplus\sum_{j\ne i}b_i(j)e_j\right).
\tag{TG1}
\]
This agrees with a full-geodesic profile on transitive comparisons.

**Theorem (nonlinear tournament-gauge trivialization).** Put
\[
q_i(j)=b_i(j)\oplus x_i\oplus x_j \quad(i\ne j);
\tag{TG2}
\]
the \(q_i(j)\) also obey \(q_i(j)\oplus q_j(i)=1\). Then
\[
\boxed{W_i(x,b)=x_i\oplus c_i(q_i),}
\tag{TG3}
\]
where \(q_i\) is any vertex with its non-\(i\) bits equal to \(q_i(j)\). The map \((x,b)\mapsto(q,W(x,b))\) is a bijection of \(\mathbb F_2^n\times\mathbb F_2^m\). Consequently, every desired profile \(s\in\mathbb F_2^n\) occurs for precisely \(2^m\) root-comparison pairs, one for each \(q\), and the inverse is constructive:
\[
\boxed{x_i=s_i\oplus c_i(q_i),\qquad
b_i(j)=q_i(j)\oplus x_i\oplus x_j.}
\tag{TG4}
\]

*Proof.* The \(j\)-th bit used to evaluate \(c_i\) in (TG1), for \(j\ne i\), is \(x_j\oplus b_i(j)=q_i(j)\oplus x_i\). Thus when \(x_i=1\) all the input bits on which \(c_i\) can depend are complemented. Oddness under global complementation, together with independence of input bit \(i\), gives (TG3). Given \(q,s\), the formula independently determines every root bit \(x_i\); it then reconstructs all comparisons. Conversely (TG2) recovers \(q\) from any original pair, proving bijectivity. \(\square\)

**Corollary (independent one-output repairs).** Flipping a root bit \(x_i\) together with every comparison \(b_i(j),b_j(i)\) incident with direction \(i\) leaves \(q\) unchanged and toggles only output \(W_i\). These \(n\) repairs commute, act freely, and yield one copy of every profile in each orbit.

**Corollary (transitive-tournament criterion).** For a prescribed \(s\), construct \(x(q;s),b(q;s)\) by (TG4). The number of rooted complete geodesics with color profile \(s\) equals
\[
\boxed{\#\{q:b(q;s)\text{ is a transitive tournament}\}.}
\tag{TG5}
\]
This follows by restricting the bijection to the root-comparison pairs arising from true direction orders.

**Cyclic-reader obstruction.** Let \(n\ge3\) and let \(r\) be a cyclic permutation of all directions. The rules \(c_i(x)=x_{r(i)}\) give a legal coloring. At root zero, a zero-color profile requires \(i\) to precede \(r(i)\) for every \(i\). An arbitrary comparison system can satisfy these cyclic demands, but no transitive comparison system can. Thus relaxation to arbitrary comparisons eliminates all color equations but does not imply root-preserving geodesic existence.

**Unrestricted NORI1 equivalence.** Directionwise color complements preserve legality. Since a profile \(w\) becomes \(w\oplus s\) after complementing all edges in direction classes indicated by \(s\), and antipodal translation converts blue full geodesics to red ones, unrestricted NORI1 in dimension \(n\) is logically equivalent to every legal coloring attaining every target profile. Formula (TG5) rewrites this as the existence of at least one transitive switched tournament for every legal coloring and target. The gauge theorem does not prove the transitivity assertion; the distinction is the remaining obstruction.

Independent finite verification checked all comparison-root pairs in dimensions \(2,3,4\) for random legal colorings and randomized one-output repairs and inverse reconstruction in dimensions \(5,6\).


**Proposition (strict local trap for tournament-triangle descent in dimension four).** Let \(n=4\) and use the legal unary-reader coloring
\[
\boxed{c_0(x)=x_1,\quad c_1(x)=x_2,\quad c_2(x)=x_0,\quad c_3(x)=x_0.}
\tag{TG7}
\]
Prescribe the direction-indexed target \(s=(0,0,1,0)\). Encode a comparison system \(q\) by a six-bit mask in the unordered-pair order \(01,02,03,12,13,23\), with \(q_i(j)\) as its bit for \(i<j\) and \(q_j(i)=1\oplus q_i(j)\). For every \(q\), construct \(x(q;s),b(q;s)\) from (TG4), and let \(E(q)\) be the number of directed triangles of the tournament \(b(q;s)\).

Then \(q=5\) is a strict positive local minimum:
\[
\boxed{E(5)=1,\qquad
E(5\oplus2^r)=2\quad(0\le r<6).}
\tag{TG8}
\]
Nevertheless \(16\) of the \(64\) possible \(q\)-states satisfy \(E(q)=0\), so the target \(s\) is realized by ordinary monochromaticity-profile geodesics. In particular, single-comparison descent on the number of cyclic triangles cannot guarantee a transitive witness, even for affine unary-reader rules and even when a successful witness exists.

*Proof.* From (TG4), at \(q=5\) the constructed root is \(x=1\) (low-bit-first) and the switched comparison mask is \(b=2\). This tournament has the unique directed triangle \(012\). Flipping each of the six input comparison bits produces, respectively, the following triples of input mask, resulting comparison mask, and set of directed triangles:
\[
\begin{array}{c|c|l}
4&4&013,\ 023\\
7&42&023,\ 123\\
1&50&012,\ 023\\
13&19&013,\ 123\\
21&18&012,\ 123\\
37&34&012,\ 023
\end{array}
\]
Each row has two directed triangles, proving (TG8). Direct enumeration of the 64 six-bit comparison masks using the displayed linear reader rules gives 16 masks with zero directed triangles; for instance \(q=0\) yields \(x=8\) and a transitive switched tournament. Every claim is a finite binary calculation with six input bits. \(\square\)

This is a warning against substituting an unproved local acyclicity-descent principle for the original NORI1 difficulty. The unrestricted profile uniformity (TG3)--(TG4) is fully constructive, but order transitivity is not locally forced by that construction.


##### Sharp root-anchored switch bounds and rank-homogeneous colorings

For any legal antipodally odd edge coloring \(c\), put \(s_x(c)=\min_{\pi\in S_n}\operatorname{sw}(c;x,\pi)\).

**Theorem (rooted switch extremum).** The maximum of \(s_x(c)\) over all legal colorings and all roots is \(n-1\) when \(n\ge2\) is even, and \(n-2\) when \(n\ge3\) is odd. Both bounds are attained by legal affine colorings for which every order from the chosen root has the same switch count.

For even \(n\), put \(c_i(z)=\sum_{j\ne i}z_j\). Every rule reads \(n-1\) other bits and is antipodally odd. At root zero, the color of step \(k\), with \(k\) starting at zero, is \(k\bmod2\), independently of order. Hence every path has \(n-1\) switches.

For odd \(n\), designate \(j=n-1\) and \(A=[n]\setminus\{j\}\). Put \(c_i(z)=\sum_{k\in A\setminus\{i\}}z_k\) for \(i\in A\), and \(c_j(z)=z_0\). Each rule is odd. At root zero the color subsequence of the \(A\)-edges is \(0101\ldots01\), containing \(n-2\) switches, for every order. Inserting the \(j\)-edge between opposite subsequence colors does not change the switch count; inserted first its color is zero and matches the first \(A\)-edge; inserted last its color is one and matches the last \(A\)-edge. Thus every full path has \(n-2\) switches.

For the odd-dimensional upper bound, suppose every full path from one root \(x\) alternates at every step. Compare two orders beginning \(i,j,k\) and \(j,i,k\), for three distinct directions. Both reach the same \(k\)-edge in step two, so alternation forces the first-step colors of \(i,j\) to agree. Thus all initial edge colors equal some \(a\). Every edge of rank \(k\) relative to \(x\) lies on a rooted full geodesic at step \(k\); therefore its color must be \(a+k\bmod2\). The antipodal mate of a rank-zero edge has rank \(n-1\), and oddness forces \(n-1\) odd, contradicting odd \(n\). The even-dimensional upper bound \(n-1\) is immediate.

**Theorem (rank-homogeneous classification).** For a fixed root \(x\), the full traversal color sequence is independent of direction order if and only if every rank-\(k\) edge relative to \(x\) has a common color \(a_k\). Such an edge coloring is legal and antipodally odd if and only if
\[
\boxed{a_{n-1-k}=1+a_k\quad(0\le k<n).}\tag{RS2}
\]
No such coloring exists for odd \(n\). For even \(n\), the \(2^{n/2}\) permissible sequences yield the rules
\[
c_i(z)=a_{\sum_{j\ne i}(z_j+x_j)}
\]
and exhaust all possibilities. The only even-dimensional colorings attaining \(n-1\) switches from \(x\) are the two alternating rank sequences.

**Corollary (root-weight switch landscape).** For even \(n=2h\) and the parity coloring \(c_i(z)=\sum_{j\ne i}z_j\), let the root have Hamming weight \(r\). Then
\[
\boxed{s_x(c)=\max\{0,2|r-h|-1\}.}\tag{RS4}
\]
Indeed along an order \(\pi\), write \(b_k=x_{\pi_k}\) and the traversed color \(y_k=p(x)+b_k+k\bmod2\). Within each constant run of \(y\), the bits \(b_k\) alternate. A sequence of \(s\) color switches has \(s+1\) runs, so \(|n-2r|\le s+1\), yielding the lower bound. For \(r\ne h\), let \(d=|r-h|\): order first \(2d\) bits of the majority value, then alternate the remaining minority and majority bits starting with the minority. This produces \(2d-1\) switches. For \(r=h\), order the original bits alternately, producing a constant color word. Thus the very same coloring makes every order from a pole root fully alternating but admits monochromatic full geodesics from each middle-rank root.

The extremum maximizes over the coloring and a selected root, not over roots after first optimizing the coloring. It does not imply failure of NORI1.


**Theorem (two-color middle-layer completion for rank-homogeneous colorings).** Let \(n=2h\) and let \(c\) be a legal odd rank-homogeneous coloring relative to a root \(x\), with edge color \(a_k\) between Hamming ranks \(k,k+1\) relative to \(x\). For every vertex \(z\) at Hamming distance \(h\) from \(x\), there are at least \((h!)^2\) monochromatic full antipodal geodesics in each of the two colors beginning at \(z\). Specifically, the \((h!)^2\) paths that alternately flip a bit initially differing from \(x\) and then a bit initially agreeing with \(x\), starting with the former, all have color \(a_{h-1}\). The \((h!)^2\) paths with the opposite alternation, starting with an agreeing bit, all have color \(a_h=1+a_{h-1}\).

*Proof.* Vertex \(z\) has \(h\) bits differing from \(x\) and \(h\) agreeing bits. Choose arbitrary orderings of these two \(h\)-element sets and interleave them alternately. Starting with a differing bit yields a walk between ranks \(h\) and \(h-1\); every traversed edge is consequently of color \(a_{h-1}\). Starting with an agreeing bit yields a walk between ranks \(h\) and \(h+1\), every edge having color \(a_h\). Both direction orders use every direction once and end at the antipode of \(z\), so they are full antipodal geodesics. The legal odd rank condition gives \(a_h=1+a_{h-1}\). There are \(h!\) independent orders for each bit class, and all resulting paths are distinct. \(\square\)

This is a direct single-witness construction for both colors from every middle-layer root. It applies to all \(2^{n/2}\) rank-homogeneous legal odd colorings, including the fully alternating-root extremizer, and shows that a prescribed root can have the maximum possible switch complexity while every one of the \(\binom{2h}{h}\) middle-layer roots has at least \((h!)^2\) full geodesics of each color.


**Sharp red and blue witness count within the rank-homogeneous class.** Summing the two-color middle-layer theorem over all binomial(2h,h) middle-layer roots gives at least binomial(2h,h)*(h!)^2=(2h)! oriented rooted red full geodesics, and the same number blue. Equality for both colors is achieved by the alternating rank sequence a_k=k modulo two (and its global color complement): the root-weight formula (RS4) shows that no full monochromatic geodesic begins outside the middle layer, while the middle-layer full paths are precisely those alternating the initially matching and differing bit classes. Hence N_R(c)>=n! and N_B(c)>=n! throughout the rank-homogeneous legal class, with sharp equality at the maximal-pole-switch coloring. The theorem is not claimed for all legal colorings; Q4 colorings with fewer red witnesses are known.

##### Root-star exclusion and sharp isodiametric mixed-star bound

Let \(c\) be any legal antipodally odd coloring of \(Q_n\), \(n\ge2\), and put \(s_i(x)=c_i(x)\), the incident direction-color vector. For root \(x\), the first and last steps of every full geodesic have colors \(s_i(x)\) and \(1-s_j(x)\) in their respective directions \(i,j\). Therefore its direction-indexed profile \(w(x,\pi)\) agrees with \(s(x)\) in some direction and disagrees in another:
\[
\boxed{\mathcal W_x(c)\cap\{s(x),\mathbf1+s(x)\}=\varnothing.}
\tag{RS1}
\]
In particular, \(|\mathcal W_x(c)|\le2^n-2\), and a monochromatic full geodesic can be rooted only at a vertex whose incident edges include both colors. Cyclic reader colorings \(c_i(x)=x_{i+1\bmod n}\) attain equality for every root when \(n\ge3\).

Put \(A=\{x:s(x)=\mathbf0\}\), \(B=\{x:s(x)=\mathbf1\}\), and \(M=Q_n\setminus(A\cup B)\), the mixed-star vertex set. Antipodal oddness gives \(B=\bar A\). No edge joins \(A\) to \(B\), as its color would have to be simultaneously red and blue. Hence any \(u,v\in A\) obey \(d_H(u,v)\le n-2\): a distance \(n\) would give \(u=\bar v\in B\), and a distance \(n-1\) would make \(u\) adjacent to \(\bar v\in B\).

**Theorem (sharp mixed-star cardinality).** For every legal odd coloring of \(Q_n\),
\[
\boxed{|M|\ge
\begin{cases}
\binom{n}{n/2},&n\text{ even},\\[2pt]
2\binom{n-1}{(n-1)/2},&n\text{ odd}.
\end{cases}}
\tag{RS2}
\]
Both bounds are attained in every dimension \(n\ge2\), by legal colorings for which **every** mixed-star vertex supports a monochromatic full antipodal geodesic. Thus the minimum candidate-root count is of order \(2^n/\sqrt n\), not a positive dimension-independent fraction of all roots.

*Proof.* The Hamming diameter of \(A\) is at most \(n-2\). Kleitman's sharp binary diameter bound therefore gives, for \(n=2m\),
\[
|A|\le\sum_{k=0}^{m-1}\binom{2m}{k}
=\tfrac12(2^{2m}-\binom{2m}{m}),
\]
and for \(n=2m+1\),
\[
|A|\le2\sum_{k=0}^{m-1}\binom{2m}{k}
=2^{2m}-\binom{2m}{m}.
\]
Since \(|M|=2^n-2|A|\), these inequalities give (RS2).

For sharpness when \(n=2m\), color every edge between Hamming layers \(k\) and \(k+1\) red for \(k<m\), and blue for \(k\ge m\). Antipodal edges have opposite colors because their lower ranks are \(k\) and \(2m-1-k\). The all-red-star vertices are precisely levels \(0,\ldots,m-1\), the all-blue-star vertices are levels \(m+1,\ldots,2m\), and \(M\) is level \(m\). From any \(x\in M\), flip its \(m\) one-bits first, followed by its \(m\) zero-bits: all \(2m\) edges are red and the endpoint is \(\bar x\).

For \(n=2m+1\), distinguish one direction \(j\), and let \(k\) count the ones in the other \(2m\) bits. Give every edge in a direction \(i\ne j\) color red when its lower endpoint among those \(2m\) bits has weight less than \(m\), and blue otherwise. Give a direction-\(j\) edge color zero when \(k<m\), one when \(k>m\), and, at \(k=m\), the value of one distinguished non-\(j\) bit. All rules ignore their own flipped bit and are antipodally odd. The all-red-star region is \(k<m\), its antipodal all-blue-star region is \(k>m\), and \(M\) comprises both \(j\)-layers of \(k=m\), having \(2\binom{2m}{m}\) vertices. From any \(x\in M\), flip its \(m\) one-bits among the other directions, then flip \(j\) at level \(k=0\), then flip its remaining \(m\) zero-bits. This is a red full antipodal geodesic, proving the claimed sharpness and constructive sufficiency for these extremizers. \(\square\)

RS1 is a necessary condition on each single full geodesic, not merely an aggregate parity condition. RS2 is a separate sharp restriction on the geometry of possible roots; it does not infer NORI1 merely from the abundance of mixed-star vertices.


**Catalan enumeration in the even-dimensional extremizer.** In the \(n=2m\) middle-layer construction above, the successful red roots are precisely the \(\binom{2m}{m}\) vertices at Hamming rank \(m\). Starting from such a root, each of its \(m\) one-bits flipped to zero is a down-step and each of its \(m\) zero-bits flipped to one is an up-step. A path remains entirely red if and only if its rank never exceeds \(m\), so its down/up word is a Dyck word of semilength \(m\). Every Dyck word admits \((m!)^2\) ways of ordering the two sets of named directions. Thus each mixed root has \(C_m(m!)^2\) red antipodal full geodesics, where \(C_m=(m+1)^{-1}\binom{2m}{m}\) is the Catalan number, and the total oriented red-geodesic count is
\[
\boxed{N_R=(2m)!\,C_m.}\tag{RS3}
\]
Every such root supports the same number of blue geodesics by reversing the direction order. No root outside the middle layer can support a monochromatic full antipodal geodesic, because its full incident star has just one color.

**Complete rooted-profile census in dimension four.** There are \(4\cdot2^{4-2}=16\) antipodal edge-orbit bits and therefore \(65536\) legal odd colorings of \(Q_4\). Exhaustively evaluating the \(24\) full geodesic direction orders at root zero for each legal coloring gives the following frequency table:
\[
\begin{array}{c|rrrrrr}
|\mathcal W_0|&4&6&8&10&12&14\\
\text{colorings}&48&720&7904&17280&29824&9760.
\end{array}\tag{RS4}
\]
The frequencies total \(65536\). The 48 minimum cases comprise precisely three perfect matchings of the four direction labels with 16 independent binary phase choices; for each matched pair \(i,j\), its edge rules are \(c_i=x_j+a_i\) and \(c_j=x_i+a_j\). Thus the minimum rooted profile count in \(Q_4\) is four and its extremizers are completely classified. The maximum 14 coincides with the root-star upper bound (RS1). A reproducible finite certificate indexes the 16 antipodal edge orbits, stores the orbit-variable index and antipodal sign of each edge on every one of the 24 rooted paths, enumerates all \(2^{16}\) orbit assignments, and counts distinct resulting four-bit profiles. This census is a finite computational result and is not used in the unrestricted theorem (RS2).


##### A strengthened universal three-direction probability bound

Let \(n\ge3\). For each direction \(i\), write the legal antipodally odd edge-color sign rule \(f_i(x)=(-1)^{c_i(x)}\). Then \(f_i(x\oplus e_i)=f_i(x)\), \(f_i(\bar x)=-f_i(x)\), and \(f_i:\mathbb F_2^n\to\{-1,1\}\). Let \(Y_i\) be the sign of the direction-\(i\) edge on a uniformly sampled rooted full antipodal geodesic, sampled uniformly over all \(2^n n!\) root-and-order pairs. The Fourier correlation identity of (FM1) is
\[
\mathbb E(Y_iY_j)
=\sum_{T\subseteq[n],\ |T|\ {\rm odd}}
\frac{\widehat f_i(T)\widehat f_j(T)}{|T|+2}
\qquad(i\ne j).
\tag{FM6}
\]

**Theorem (noise-coupled three-direction lower bound).** For any three distinct directions \(i,j,k\) and any target signs \(\eta_i,\eta_j,\eta_k\in\{-1,1\}\),
\[
\boxed{\Pr(Y_i=\eta_i,\ Y_j=\eta_j,\ Y_k=\eta_k)\ge\frac{31}{432}.}
\tag{FM7}
\]
Equivalently, every legal coloring realizes each prescribed color pattern on three selected directions on at least \((31/432)2^n n!\) rooted full antipodal geodesics. This strengthens the \(1/16\) bound of (FM5).

*Proof.* Multiply the three rules by their target signs, writing \(g_1=\eta_i f_i\), \(g_2=\eta_j f_j\), \(g_3=\eta_k f_k\). The new rules are still odd \(\{-1,1\}\)-valued functions. Let \(T_\rho\) be the Boolean noise operator, defined by \(\widehat{T_\rho g}(A)=\rho^{|A|}\widehat g(A)\), and set
\[
S(t)=\sum_{1\le a<b\le3}\langle g_a,T_tg_b\rangle,\qquad 0\le t\le1.
\]
Equation (FM6) and \(1/(|A|+2)=\int_0^1t^{|A|+1}\,dt\) imply
\[
R:=\eta_i\eta_j\mathbb E(Y_iY_j)+
\eta_i\eta_k\mathbb E(Y_iY_k)+
\eta_j\eta_k\mathbb E(Y_jY_k)
=\int_0^1tS(t)\,dt.
\tag{FM8}
\]

We establish two lower bounds on \(S(t)\). First put \(h_a=T_{\sqrt t}g_a\). Self-adjointness and the semigroup law give
\[
2S(t)=\|h_1+h_2+h_3\|_2^2-\sum_{a=1}^3\|h_a\|_2^2.
\]
All \(g_a\) are odd and have squared norm one; hence
\(\|h_a\|_2^2=\sum_{|A|\ {\rm odd}}t^{|A|}\widehat g_a(A)^2\le t\).
Consequently
\[
S(t)\ge-\frac{3t}{2}.
\tag{FM9}
\]

For the second bound, sample a uniform latent cube vertex \(Z\), and conditional on \(Z\) sample three independent noisy copies \(X_1,X_2,X_3\), each with bitwise correlation \(\sqrt t\) with \(Z\). Any two copies then have correlation \(t\), so
\[
S(t)=\mathbb E\bigl[g_1(X_1)g_2(X_2)+g_1(X_1)g_3(X_3)+g_2(X_2)g_3(X_3)\bigr].
\]
For any three signs \(u,v,w\), the quantity \(uv+uw+vw\) is either \(3\) or \(-1\). Therefore
\[
S(t)\ge-1.
\tag{FM10}
\]
Combining (FM8)--(FM10),
\[
R\ge-\int_0^1t\min(1,3t/2)\,dt
=-\frac{23}{54}.
\]
Antipodal translation of the starting root negates all \(Y_r\), so every odd joint moment vanishes. Expanding the three target-event indicators gives
\[
\Pr(Y_i=\eta_i,Y_j=\eta_j,Y_k=\eta_k)
=\frac{1+R}{8}
\ge\frac18\left(1-\frac{23}{54}\right)
=\frac{31}{432}.
\qquad\square
\]

**Theorem (a six-cube obstruction to a \(1/12\) universal constant).** There is a legal coloring of \(Q_6\) for which one prescribed three-direction pattern occurs with probability \(19/240\). Thus the optimal dimension-uniform constant in (FM7) lies in
\[
\boxed{\frac{31}{432}\le p_3^{\rm opt}\le\frac{19}{240}.}
\tag{FM11}
\]
To define the coloring, put \(U=(-1)^{x_3}\), \(V=(-1)^{x_4}\), \(W=(-1)^{x_5}\), and let \(\operatorname{maj}(u,v,w)\) be the majority sign of three signs. Define the signs on directions \(0,1,2\) by
\[
f_0=-W,\quad
f_1=\operatorname{maj}(U,V,W),\quad
f_2=\operatorname{maj}(-U,-V,W),
\tag{FM12}
\]
and on the other directions put \(f_3=(-1)^{x_4}\), \(f_4=(-1)^{x_5}\), \(f_5=(-1)^{x_3}\). Each rule ignores its own input bit and is odd under antipodal complementation, so these rules define a legal coloring.

Using
\[
f_1=\frac{U+V+W-UVW}{2},\qquad
f_2=\frac{-U-V+W-UVW}{2},
\]
the three correlations of the selected direction colors obtained from (FM6) are
\[
\mathbb E(Y_0Y_1)=-\frac16,\qquad
\mathbb E(Y_0Y_2)=-\frac16,\qquad
\mathbb E(Y_1Y_2)=-\frac1{30}.
\]
Therefore
\[
\boxed{\Pr(Y_0=Y_1=Y_2=+1)
=\frac18\left(1-\frac16-\frac16-\frac1{30}\right)
=\frac{19}{240}.}
\tag{FM13}
\]
Direct integer enumeration confirms that precisely \(3648\) of the \(2^6 6!=46080\) rooted full antipodal geodesics realize this pattern. The six-cube witness disproves a proposed \(1/12\) lower bound, while (FM7) is unconditional in the ambient dimension.


##### Sharp leading-degree charge bound for rooted profile affine rank

For \(n\ge4\), let \(\mathcal W_x(c)\) denote the direction-indexed profiles of full antipodal geodesics rooted at \(x\), and let
\[
V(c)=\operatorname{span}_{\mathbb F_2}\{
(D_jc_i(u))e_i+(D_ic_j(u))e_j : i\ne j,\ u\in Q_n\}.
\]
The rooted affine-coset theorem above identifies \(\dim\operatorname{aff}\mathcal W_x(c)=\dim V(c)\), independently of \(x\).

The legal rule \(c_i\) is antipodally odd on its \(m=n-1\) other input bits. Balancedness makes the degree-\(m\) monomial coefficient vanish. Writing \(b_j\) for the coefficient of the degree-\((m-1)\) monomial missing input \(j\), the identity \(D_{\mathbf1_m}c_i=1\) gives \(b_j+b_k=0\) from each degree-\((m-2)\) monomial missing \(j,k\). Thus all \(b_j\) agree. Write \(a_i\) for their common bit, so the degree-\((n-2)\) component of \(c_i\) is
\[
a_i e_{n-2}(x_{-i}),
\]
with \(e_d\) the degree-\(d\) elementary symmetric polynomial. Put \(z=|\{i:a_i=0\}|\).

**Theorem (sharp leading-charge rank inequality).** For every legal coloring with \(z\ge1\),
\[
\boxed{\dim\operatorname{aff}\mathcal W_x(c)\ge n-\lfloor z/2\rfloor \quad\text{at every root }x.}\tag{CR1}
\]
Equality is attained for each \(n\ge4\) and each \(1\le z\le n\). If \(z=0\), the rooted affine rank equals \(n\) unless the coloring is flat, in which case \(n\) is even and the rank is \(n-1\). Both alternatives occur in even dimensions; in odd dimensions only the full-rank alternative occurs.

*Proof of bound.* The rooted affine restriction classification above states that the codimension \(t=n-\dim V(c)\) equals the number of disjoint unmarked connected components of the exchange graph, each an autonomous flat block containing at least two directions and an even number of directions. Every rule within such a block \(C\) depends only on the vertex bits indexed by \(C\). If \(a_i=1\), then \(c_i\) has algebraic degree \(n-2\), whose homogeneous part \(e_{n-2}(x_{-i})\) depends essentially on every one of the other \(n-1\) bits. Thus a block containing \(i\) must be \(C=[n]\). For a full flat block, the identity \(D_jc_i=D_ic_j\) and comparison of degree-\((n-3)\) terms imply that all \(a_i\) coincide. If \(z\ge1\) and some \(a_i=1\), this is impossible. Therefore all unmarked blocks are contained in the zero-charge directions. If all charges vanish, this containment is immediate. Every block contains at least two directions, so \(t\le\lfloor z/2\rfloor\), proving (CR1). If \(z=0\), the only possible unmarked block is the whole direction set. The exchange classification gives codimension one when it exists, and zero otherwise. The whole block is flat and even-sized, proving the exceptional case.

*Proof of sharpness.* Select \(z\) zero-charge directions, form \(k=\lfloor z/2\rfloor\) disjoint pairs \(\{p,q\}\) among them, and prescribe \(c_p=x_q,\ c_q=x_p\) on each pair. These are autonomous flat source blocks. For each positive-charge direction \(h\), take \(c_h=x_s+\mathbf1_{\{b,\bar b\}}(x_{-h})\), where \(s\ne h\) is one of the zero-charge directions and \(b,\bar b\) is any antipodal pair of its \(n-1\) input vectors. This rule is antipodally odd and has degree \(n-2\), with leading charge one, because the antipodal-pair indicator has homogeneous part \(e_{n-2}\). If \(z\) is odd, make the remaining unpaired zero-charge direction read one positive-charge bit, when present, or a bit from a selected pair when \(z=n\). This rule is unary with leading charge zero. The \(k\) chosen pairs remain unmarked flat blocks. All positive-charge directions are excluded from unmarked proper blocks by the preceding argument, and the remaining zero-charge direction cannot form an unmarked block alone. Hence \(t=k\) and equality holds.

For \(z=0\), a flat example in each even dimension is \(c_i=D_iF\) with
\[
F(x)=\sum_{j<k}x_jx_k+\prod_{j=1}^{n-1}(x_j+x_n).
\]
Every rule has leading charge one. Recoloring two distinct antipodal edge orbits in one direction preserves all charges and destroys flatness, supplying full-rank examples in even dimensions. In odd dimensions take independently for each direction \(i\) an odd unary rule plus an antipodally paired input indicator, yielding \(a_i=1\); flatness is impossible in odd dimension. \(\square\)

**Corollary (sparse full-rank normalization preserving prescribed paths).** For any legal \(c\) on \(Q_n\), \(n\ge4\), and any collection \(\mathscr P\) of fewer than \(2^{n-2}\) full antipodal geodesics, there is a legal \(c'\), differing from \(c\) on at most \(n\) antipodal orbits of undirected edges, such that every path in \(\mathscr P\) retains its direction-indexed color profile and
\[
\boxed{\operatorname{aff}\mathcal W_x(c')=\mathbb F_2^n
\quad\text{for all roots }x.}\tag{CR2}
\]

*Proof.* Choose one direction \(r\) whose desired leading charge is zero, and prescribe charge one in every other direction. If a charge must be toggled, change the colors of one antipodal edge orbit in that direction. This is equivalent to adding the indicator of an antipodal input pair to the corresponding rule, which toggles its leading coefficient \(a_i\) and preserves legality. Each direction has \(2^{n-2}\) antipodal edge orbits; fewer than that many geodesics can meet fewer than that many orbits, so one orbit is available disjoint from every path in \(\mathscr P\). Do this independently for at most \(n\) directions. The resulting charge vector has \(z=1\), so (CR1) gives full rooted affine rank, while every selected path retains all its colors. \(\square\)

**Finite audit.** Exhaustive evaluation of all \(65536\) legal colorings on \(Q_4\) confirms (CR1) and its sharpness. For zero-charge counts \(z=0,1,2,3,4\), respectively, the minimum rooted affine ranks are \(3,4,3,3,2\). Precisely 128 all-positive-charge colorings have rank three, and every one of them is flat. All all-positive-charge nonflat colorings have rank four. This confirms the general argument without replacing it.

These rank conclusions concern the affine hulls of rooted profile sets. A full affine hull alone does not guarantee attainment of any prescribed full profile.


##### Universal fixed-root two-direction shattering dichotomy

**Theorem.** Let \(n\ge2\), let \(c\) be any legal antipodally odd coloring, fix a root \(x\), and select two distinct directions \(i,j\). Let \(\operatorname{pr}_{ij}\mathcal W_x(c)\) denote the set of two-bit indexed color profiles on these directions, obtained from full antipodal geodesics rooted at \(x\). Then:
\[
\boxed{
\operatorname{pr}_{ij}\mathcal W_x(c)=
\begin{cases}
\{(a,b),(1+a,1+b)\},&
c_i(y)=y_j+\alpha,\quad c_j(y)=y_i+\beta
\text{ for some }\alpha,\beta,\\
\mathbb F_2^2,&\text{otherwise}.
\end{cases}}
\tag{TP1}
\]
Thus a fixed root shatters every pair of directions except autonomous reciprocal-reader pairs. In the exceptional case \(a+b=x_i+x_j+\alpha+\beta+1\), and both complementary patterns occur. This classification is independent of the selected root.

*Proof.* Let \(\pi\) be an order from \(x\), and consider the reversed order \(\pi^{\mathrm{rev}}\) from the SAME root. Antipodally translate the original geodesic and reverse its traversal: this gives an \(x\)-rooted geodesic in reversed order whose indexed profile is \(\mathbf1+w(x,\pi)\). Thus every rooted profile set, and every two-bit projection, is invariant under bitwise complement. A nonempty complement-invariant subset of \(\mathbb F_2^2\) has size two or four unless it has been reduced to a single complement orbit (which is the size-two case). Suppose its projection has size two. Then the parity \(w_i+w_j\) is constant over every rooted full direction order.

Fix \(k\notin\{i,j\}\) and any subset \(S\subseteq[n]\setminus\{i,k\}\). Choose a full direction order from \(x\) with prefix \(S\), followed by \(i,k\) consecutively, and the other directions afterward. Exchange this adjacent pair. Only the profile entries indexed by \(i,k\) can change, and the change in the \(i\)-entry is \(D_kc_i(x+\mathbf1_S)\). The \(j\)-entry is unchanged. Constancy of \(w_i+w_j\) forces \(D_kc_i(x+\mathbf1_S)=0\). Since \(S\) varies over all subsets outside \(\{i,k\}\), and \(c_i\) is independent of its own bit \(i\), we have \(D_kc_i\equiv0\). Repeating with \(j,k\) gives \(D_kc_j\equiv0\) for every \(k\notin\{i,j\}\). By undirected-edge consistency, \(c_i\) ignores \(i\) and \(c_j\) ignores \(j\), so \(c_i\) is a function of \(x_j\) alone, and \(c_j\) a function of \(x_i\) alone. Antipodal oddness forces these unary functions to be \(x_j+\alpha\) and \(x_i+\beta\).

Conversely, when these reciprocal-reader formulas hold, the two profiles are \(w_i=x_j+\alpha+[j\prec i]\) and \(w_j=x_i+\beta+[i\prec j]\), whence \(w_i+w_j=x_i+x_j+\alpha+\beta+1\), independent of order. Opposite relative orders occur, giving the two complementary patterns. For any other legal coloring, the two-pattern alternative is impossible by the preceding argument. Complement invariance then forces the full four-pattern projection. \(\square\)

**Independent finite audit:** exhaustive checks across all four legal \(Q_2\) colorings, all 64 legal \(Q_3\) colorings, and all 65536 legal \(Q_4\) colorings confirmed (TP1) for every root and every ordered pair of distinct directions. The proof is independent of these checks.

**Scope.** This gives simultaneous two-bit forcing at a prescribed root for every non-exceptional direction pair, while the seven-direction theorem concerns unrooted prescriptions. The obstruction for three or more bits is fundamentally different: pairwise full projections need not imply three-bit saturation, as seen in rooted cyclic-reader examples. The result is consistent with and refines the existing autonomous-flat-block classification.


##### Universal three-direction rooted-profile trichotomy

**Theorem.** Let \(n\ge3\), fix any legal NORI1 coloring \(c\), any starting root \(x\), and any three distinct directions \(S=\{i,j,k\}\). Set \(T=\operatorname{pr}_S\mathcal W_x(c)\subseteq\mathbb F_2^3\). Then one of the following holds:

1. If \(S\) contains an autonomous reciprocal-reader pair \(p,q\), with \(c_p(y)=y_q+\alpha,\ c_q(y)=y_p+\beta\) on the whole cube, then \(T\) consists of the four three-bit patterns satisfying
\[
w_p+w_q=x_p+x_q+\alpha+\beta+1.
\]
2. If \(S\) contains no such pair, then \(|T|\in\{6,8\}\). If \(|T|=6\), the two missing patterns are bitwise complements.

Thus without a reciprocal-reader pair, at every fixed root one may prescribe three direction colors with at most one complementary pair of exceptions. All three cardinalities 4,6,8 occur already in dimensions at most four.

*Proof.* The rooted profile set is closed under bitwise complement, by antipodal translation followed by path reversal. Consequently \(T\) is a union of complementary pairs and \(|T|\in\{2,4,6,8\}\). The preceding two-direction shattering theorem says that any pair projection has two values only when that pair is autonomous reciprocal-reader, and otherwise has four.

The value \(|T|=2\) would make every pair projection a complementary pair. This would require at least two reciprocal-reader pairs sharing a direction, impossible: the shared direction rule would have to be both \(y_p+\alpha\) and \(y_q+\beta\) for distinct input bits \(p,q\).

Suppose \(|T|=4\). It is a union of two complementary pairs, hence an affine plane
\[
T=u+\operatorname{span}\{\mathbf1,v\}
\]
for a vector \(v\notin\{0,\mathbf1\}\). The nonzero normal of this plane is orthogonal to \(\mathbf1\), so in dimension three it has Hamming weight two. Thus some two-direction projection of \(T\) is a complementary pair, forcing an autonomous reciprocal-reader pair by the previous theorem. Conversely, if \(S\) contains such a pair, its parity equation restricts \(T\) to four patterns. The already established lower bound \(|T|\ge4\) gives equality and all four patterns occur. In the absence of any exceptional pair, \(|T|\) is 6 or 8, and complement symmetry pairs the two missing patterns when there are six. \(\square\)

*Sharp examples.* In \(Q_3\), \(c_0=x_1,\ c_1=x_0,\ c_2=x_0\) gives case 1 for pair \(\{0,1\}\). In \(Q_3\), the cyclic-reader coloring \(c_0=x_1,\ c_1=x_2,\ c_2=x_0\) has six rooted three-bit profiles, omitting \(\mathbf0,\mathbf1\) at root zero. In \(Q_4\), let \(c_0=c_1=c_2=x_3,\ c_3=x_0\); inserting each of directions \(0,1,2\) before or after direction 3 permits all eight projected profiles from every root.

*Independent verification.* Complete enumeration for every legal coloring, root and triple found in \(Q_3\) cardinality counts \(4:384,\ 6:128\), and in \(Q_4\) counts \(4:196608,\ 6:1073152,\ 8:2924544\), agreeing with the proof. These counts enumerate (coloring,root,unordered direction triple) instances.

This is an unrestricted rooted statement and identifies the smallest arity at which non-affine omissions can appear: two-direction omissions are autonomous affine reciprocal-reader constraints, while three-direction omissions may be nonlinear and are limited to one complementary pair.


#### Four-local coherence and 4n-fiber theorem for antipodal edge-orbit supports

For \(n\ge2\), select one antipodal orbit \(O_i\) of undirected edges in each direction \(i\). Record a representative vector of its bits outside \(i\) as \(s_i=(s_{ij})_{j\ne i}\), understood modulo the all-one vector. The selection is *coherent* if its selected orbits form the support of a rooted full antipodal geodesic.

**Theorem (four-direction local-to-global coherence).** For \(n\ge4\), an orbit selection is coherent if and only if its restriction to every four-direction set is coherent in that four-cube. Constructively, put \(q_{ij}=1+s_{ij}+s_{ji}\). The selection is coherent precisely when:

(a) \(q_{ij}+q_{jk}+q_{ki}=0\) for all distinct \(i,j,k\), so one can solve \(y_i+y_j=q_{ij}\); and

(b) the tournament with arrow \(j\to i\) when \(s_{ij}+y_i=1\) is Seidel-switching equivalent to a transitive tournament, equivalently contains no induced diamond (a directed triangle plus one vertex dominating or dominated by that triangle).

*Proof.* In a path rooted at \(x\), let \(\pi\) be the direction order, and let \(t_i\) specify which antipodal representative of \(O_i\) was used. At direction \(i\), the current bit \(j\ne i\) equals \(x_j+[j\prec_\pi i]\). Accordingly
\[
[j\prec_\pi i]=x_j+s_{ij}+t_i.
\]
Adding the analogous relation with \(i,j\) exchanged gives \(y_i+y_j=q_{ij}\) for \(y_i=x_i+t_i\), hence the triple equations. Conversely, after solving them, the precedence rule becomes
\[
[j\prec_\pi i]=s_{ij}+y_i+x_i+x_j. \tag{OC1}
\]
Changing root \(x\) reverses precisely the tournament arrows crossing the cut \(\{i:x_i=1\}\). Therefore a root/order pair realizes every selected orbit if and only if its switched tournament is transitive; then set \(t_i=x_i+y_i\).

For completeness, the standard tournament-switching lemma has an elementary four-vertex proof. Encode a tournament by skew signs \(a_{ij}=\pm1\) and define on four vertices \(a,b,c,d\) the Pfaffian \(p=a_{ab}a_{cd}-a_{ac}a_{bd}+a_{ad}a_{bc}\). The four-vertex classification gives \(|p|=3\) for a diamond and \(|p|=1\) otherwise. A switch multiplies \(p\) by the product of its four vertex signs, hence preserves the diamond property. If a tournament has no diamond, choose a vertex \(v\) and switch its in-neighborhood to make \(v\) dominate the other vertices. A directed triangle among those vertices would form a diamond with \(v\). Thus the remainder is triangle-free and transitively ordered; the full switched tournament is transitive. The converse follows from the switching invariance of diamonds. The triple equations and diamond exclusions are detected on three and four directions respectively. Therefore coherence on every four-direction restriction implies global coherence. \(\square\)

**Theorem (fiber and enumeration).** Every coherent selection has precisely \(4n\) rooted, ordered full geodesic realizations. Consequently
\[
\boxed{\#\{\text{full-geodesic antipodal edge-orbit supports}\}=2^{n-2}(n-1)!.}\tag{OC2}
\]

*Proof.* The triple equations have two complementary solutions \(y\). For either \(y\), roots \(x\) giving a transitive switched tournament have the following count. Begin with a transitive tournament ordered \(1,\ldots,n\). Switching a subset preserves transitivity if and only if its binary membership changes at most once along the order; otherwise a membership pattern \(010\) or \(101\) produces a directed triangle. The allowed subsets are prefixes and suffixes, yielding \(n\) switching cuts modulo complement and \(2n\) root bit vectors \(x\). Each such root determines one order. The two possible \(y\) give opposite orders, hence \(4n\) rooted geodesics. They are the cyclic root slides and reversals of any representative. As the cube has \(2^n n!\) rooted full geodesics, division by \(4n\) gives (OC2). \(\square\)

**Corollary (one profile cycle per orbit support).** In any legal antipodally odd coloring, the \(4n\) paths in a coherent orbit-support fiber realize \(2n\) distinct direction-indexed profiles, each twice (by reversal). Starting from a profile \(w\) and direction order \(\pi\), cyclic root slides give
\[
w_t=w+\sum_{r=1}^{t}e_{\pi_{1+((r-1)\bmod n)}}\quad(0\le t<2n),\qquad w_{2n}=w.
\]
These profiles form an antipodal \(2n\)-cycle in the Boolean profile cube. Thus the global full-profile family is a union of profile cycles indexed by coherent orbit supports.

**Independent exhaustive audit.** All \(8,256,32768\) one-orbit-per-direction selections in \(Q_3,Q_4,Q_5\), respectively, were compared with direct enumeration of all rooted full geodesics. The coherent support counts were \(4,24,192\), and the triple-plus-diamond criterion matched every instance. The canonical \(Q_5\) orbit selection with direction-indexed orbit IDs \((28,31,6,14,19)\) fails the triple equation on \((0,1,2)\). For the legal coloring with orbit mask \(0x666ae4b58c\), all 50 rooted red geodesics meet this incoherent five-orbit selection. This distinguishes the coherent-path obstacle property (verified computationally for \(Q_5,Q_6\)) from avoidance of arbitrary one-orbit-per-direction sets, which is false already in \(Q_5\).


#### The regular graph of coherent orbit supports and its mod-four orientation obstruction

Let \(n\ge4\). Let \(\mathcal O_n\) be the set of coherent orbit supports, one antipodal undirected-edge orbit in each direction, constructed in the preceding four-direction coherence theorem. Define the **support exchange graph** \(G_n\) on \(\mathcal O_n\): distinct supports \(O,O'\) are adjacent if they differ in precisely two direction orbit choices. The fiber theorem above associates to every support a cyclic direction order, defined up to rotation and reversal.

**Theorem (rigid recovery and full exchange-graph classification).** The following statements hold for every \(n\ge4\).

1. Distinct supports differ in at least two directions. Any prescribed \(n-1\) orbit choices admit at most one coherent completion.
2. If \(O\) is coherent and \(a,b\) are two directions, then there is at most one other coherent support sharing all orbit choices except possibly \(a,b\). Such a different completion exists **if and only if \(a,b\) are adjacent in the cyclic direction order of \(O\)**. It is obtained by swapping those two consecutive directions in a rooted full geodesic representing \(O\), after a cyclic root slide if necessary.
3. \(G_n\) is connected, \(n\)-regular, vertex- and edge-transitive. It has
\[
|V(G_n)|=2^{n-2}(n-1)!,\qquad |E(G_n)|=2^{n-3}n!.
\tag{OG1}
\]
4. \(G_n\) is bipartite if and only if \(n\equiv0,1\pmod4\). It is nonbipartite for \(n\equiv2,3\pmod4\).
5. For every legal coloring \(c\), the antipodally invariant \(2n\)-cycles of direction-indexed color profiles belonging to two adjacent supports have at least four common profile vertices (two vertices and their antipodes).

*Proof of rigid reconstruction and adjacency.* Fix two coherent orbit choices \(O,O'\) agreeing outside \(\{a,b\}\). Write \(I=[n]\setminus\{a,b\}\), with \(|I|\ge2\), and fix representatives \(s_i=(s_{ij})_{j\ne i}\) for the common orbits, \(i\in I\). Recall the triangle relations \(q_{ij}=1+s_{ij}+s_{ji}=y_i+y_j\). Fix a solution \(y_i\) on \(I\) once and for all. For each of the two as-yet unspecified orbit rows, changing its antipodal representative flips its entire row \(s_a\) or \(s_b\) and changes the corresponding \(y\)-bit. Normalize representatives so \(y_a=y_b=0\). For \(i\in I\), the triangle equations then uniquely force
\[
s_{ai}=1+s_{ia}+y_i,\qquad s_{bi}=1+s_{ib}+y_i.
\]
The remaining relation \(q_{ab}=y_a+y_b=0\) forces \(s_{ab}+s_{ba}=1\). There are therefore at most two parity-compatible completions: they differ by reversing only the arc \(a,b\) of the tournament constructed from the \(s_i,y_i\). If just one direction \(a\) were missing, its bits on all other directions would similarly be determined modulo the common complement, yielding only one orbit choice; this proves assertion 1.

Switch the common tournament to a transitive one, with linear order \(\pi\) representing \(O\). Reversing its arc \(a,b\) produces a switching-transitive tournament if \(a,b\) are consecutive in \(\pi\), since their exchange simply changes the total order, or if they are the first and last elements of \(\pi\), since one can cyclically rotate the order by a root switch before exchanging them. Conversely, if \(a,b\) are not adjacent in the cyclic order, write them as \(a\prec k\prec b\) with some \(k\), and choose a fourth vertex \(\ell\) outside their closed interval (available precisely because cyclic adjacency fails). Reversing \(a\to b\) forms a directed triangle on \(a,k,b\), while \(\ell\) dominates or is dominated by that triangle, an induced diamond. The four-direction coherence theorem prohibits such a completion. When the exchange is allowed, swapping adjacent directions changes only their two traversed cube edges. Each new direction edge belongs to a different antipodal orbit because the two edges lie in the same two-dimensional face, not in antipodal faces for \(n\ge3\). Thus both orbit choices change, proving assertion 2.

*Proof of graph symmetry and connectedness.* Each coherent support has \(n\) cyclicly adjacent pairs, one neighbor for each by assertion 2, proving regularity. A cube symmetry maps any rooted, ordered full geodesic to any other, proving vertex-transitivity. It also maps any adjacent direction exchange, following a cyclic root slide, to any other, proving edge-transitivity. Any two full rooted orders are connected by permutations of adjacent positions and cyclic root slides: adjacent transpositions generate all orders at a fixed root; placing a chosen direction first and performing a cyclic slide changes only that root bit, so all roots are reachable. Slides leave orbit supports unchanged, and adjacent exchanges move along edges of \(G_n\). Hence \(G_n\) is connected. The support count \(2^{n-2}(n-1)!\) was established above; multiplying by \(n/2\) gives the edge count.

*Proof of the mod-four parity dichotomy.* Let \(\operatorname{sgn}(\pi)\) be the sign of a permutation of the \(n\) directions, and put
\[
\chi(x,\pi)=(-1)^{(n-1)|x|}\operatorname{sgn}(\pi).
\tag{OG2}
\]
A cyclic root slide from \((x,(i,\rho))\) to \((x+e_i,(\rho,i))\) changes the permutation sign by \((-1)^{n-1}\) and the root weight parity by one, hence preserves \(\chi\). Path reversal sends \((x,\pi)\) to \((\bar x,\operatorname{rev}\pi)\); the root factor changes by \((-1)^{n(n-1)}=1\), whereas the permutation factor changes by \((-1)^{n(n-1)/2}\). All rooted paths representing one support are generated by slides and reversal, by the \(4n\)-fiber theorem. Thus \(\chi\) is well defined on coherent supports precisely when \(n(n-1)/2\) is even, equivalent to \(n\equiv0,1\pmod4\). In those dimensions, an adjacent exchange reverses \(\chi\), so \(G_n\) is bipartite. In the other dimensions, connect any path to its reversal by adjacent transpositions and cyclic slides (possible by the connectivity argument). The two paths represent the same support, while their \(\chi\)-values are opposite. Slides preserve \(\chi\) and each exchange reverses it. The resulting closed walk in \(G_n\) therefore contains an odd number of edges, proving nonbipartiteness.

*Proof of the four-point profile overlap.* Let adjacent supports \(O,O'\) be represented by paths rooted at the same \(x\), with direction orders \((A,i,j,B)\) and \((A,j,i,B)\), respectively. Let their indexed profiles be \(w,w'\), and write \(w'=w+\delta\), where square locality gives \(\delta\in\{0,e_i,e_j,e_i+e_j\}\). Let \(p=w+\sum_{a\in A}e_a\). By cyclic root transport, the profile cycle of \(O\) contains
\[
\{p,p+e_i,p+e_i+e_j\},
\]
whereas the cycle of \(O'\) contains
\[
\{p+\delta,p+\delta+e_j,p+\delta+e_i+e_j\}.
\]
For each of the four possibilities for \(\delta\), these sets have at least two common vertices. Their antipodes belong to both cycles as well. For \(n\ge4\), all four are distinct, proving assertion 5. \(\square\)

**Independent full-graph audit.** Breadth-first generation from the canonical rooted path, using all cyclic adjacent swaps, recovered all coherent orbit supports in \(n=3,4,5,6,7\), with vertex counts \(4,24,192,1920,23040\) and respective degrees \(3,4,5,6,7\). In these dimensions the graph is bipartite for \(n=4,5\), and nonbipartite for \(n=3,6,7\). The measured graph diameters are respectively \(1,4,7,9,13\); no general diameter formula is asserted.

**Research significance and limit.** This theorem upgrades four-direction recognition to a complete metric-neighbor and orientation classification of the geometric orbit-support space. In particular each edge of the \(n\)-regular support graph corresponds to a specified two-direction square exchange, while the coloring assigns overlapping profile cycles to its vertices. Profile-cycle overlap and ordinary connectedness were established earlier independently; the new content is the support graph's intrinsic metric rigidity, neighbor classification, uniform degree, and mod-four parity dichotomy. Neither support-graph connectedness nor its parity by itself guarantees that a particular profile, such as the constant zero word, is attained.


#### Factorial extension law for two prescribed antipodal cube-edge orbits

Fix \(n\ge2\) and distinct directions \(i,j\). Let \(A\) be an antipodal orbit of undirected direction-\(i\) cube edges and \(B\) an antipodal orbit of direction-\(j\) cube edges. Choose arbitrary representative bit rows \(s_i=(s_{ik})_{k\ne i}\) and \(s_j=(s_{jk})_{k\ne j}\). Define
\[
D=\{k\in[n]\setminus\{i,j\}:s_{ik}\ne s_{jk}\},\quad b=|D|,\quad c=n-2-b.
\]
Replacing either representative by its antipode exchanges \(b\) and \(c\), so \(b!c!\) is an intrinsic quantity of the pair \(A,B\).

**Theorem (two-orbit factorial extension).** The number of coherent full-geodesic orbit supports containing both \(A\) and \(B\) is
\[
\boxed{N_n(A,B)=b!\,(n-2-b)!.}\tag{OF1}
\]
Consequently **any** pair of antipodal undirected-edge orbits in distinct directions extends to some full antipodal geodesic, without any coloring hypotheses. The number of rooted, ordered full geodesics realizing both prescribed orbits is \(4n\,b!c!\).

*Proof.* Count first the rooted, ordered full geodesics in which direction \(i\) is visited before direction \(j\). For their direction-\(i\) and direction-\(j\) edges, let \(t_i,t_j\in\mathbb F_2\) indicate which of the two antipodal representatives of \(A,B\) is used. For an outside direction \(k\ne i,j\), the bit at the \(i\)-edge is \(x_k+[k\prec i]=s_{ik}+t_i\), whereas at the \(j\)-edge it is \(x_k+[k\prec j]=s_{jk}+t_j\). As \(i\prec j\), subtraction gives
\[
[i\prec k\prec j]=s_{ik}+s_{jk}+t_i+t_j.
\tag{OF2}
\]
Thus the set of directions strictly between \(i,j\) equals \(D\) when \(t_i+t_j=0\) and equals the complement of \(D\) in \([n]\setminus\{i,j\}\) otherwise. Each value of \(t_i+t_j\) comes from two choices of \((t_i,t_j)\).

For the first case, directions of \(D\) can be arranged between \(i,j\) in \(b!\) ways, while each direction of its \(c\)-element complement lies either before \(i\) or after \(j\). Summing over all possible subsets before \(i\), their permutations contribute
\[
\sum_{r=0}^c\binom cr\,r!\,(c-r)!=(c+1)c!.
\]
The first case therefore supplies \(2b!(c+1)c!\) rooted paths. Exchanging \(b,c\) supplies \(2c!(b+1)b!\) in the second case. For every choice, the starting root is uniquely forced: its \(i,j\) bits are determined by the selected representative edges, and each remaining root bit is determined from the direction-\(i\) edge and its position relative to \(i\). Hence the number of rooted paths having \(i\prec j\) is
\[
2b!c![(c+1)+(b+1)]=2n\,b!c!.
\]
Each coherent orbit support is represented by \(4n\) rooted paths, with precisely half satisfying \(i\prec j\), because reversal pairs the two relative orders. Dividing by \(2n\) gives (OF1), and multiplying by \(4n\) gives the final count. \(\square\)

**Corollary (one- and two-orbit incidence and collision moments).** Every individual antipodal direction-edge orbit belongs to \((n-1)!\) coherent supports. For a uniformly random coherent support \(O\),
\[
\Pr[O_i=A]=2^{-(n-2)},\qquad
\Pr[O_i=A,\ O_j=B]=\frac{b!\,(n-2-b)!}{2^{n-2}(n-1)!}.
\tag{OF3}
\]
If \(O^*\) is a fixed coherent support with cyclic order \(0,1,\ldots,n-1\), let \(X\) count the direction orbits common to \(O,O^*\). Then
\[
\mathbb EX=\frac{n}{2^{n-2}},\qquad
\mathbb E\binom X2=\frac{\displaystyle\sum_{k=0}^{n-2}k!(n-1-k)!}{2^{n-2}(n-1)!}.
\tag{OF4}
\]
Indeed, a canonical pair of directions separated by \(k\) intervening directions contributes \(k!(n-2-k)!\) coherent supports; summing over \((n-1-k)\) possible pairs at that separation yields \(\sum_{k=0}^{n-2}k!(n-1-k)!\). In particular, for \(n\ge5\) at least the fraction \(1-n/2^{n-2}\) of all coherent supports avoid all direction orbits in an arbitrary prescribed one-orbit-per-direction obstacle set, by the union bound. This is an uncolored geometric avoidance statement; it does not force a monochromatic witness.

**Independent finite audit.** All possible distinct-direction pairs of antipodal edge orbits were checked against enumeration of full coherent supports for \(n=3,4,5,6\). The numbers of pair selections tested were \(12,96,640,3840\), respectively, with no discrepancies from (OF1). For \(n=5\), the number of completions is 6 when \(b=0\) or 3 and 2 when \(b=1\) or 2. For \(n=6\), completion counts are 24,6,4 for \(b=0/4,1/3,2\), respectively.

**Scope.** The two-orbit extension law is sharp and unrestricted at the level of geometric orbit supports. Compatible triples and quadruples are governed by the parity and diamond restrictions proved above, and partial orbit selections in more directions need not extend. The law does not assume or establish any color-profile saturation.


#### Color-sensitive profile-cycle overlap detects every curved square

Retain the coherent orbit-support graph \(G_n\) defined above, with an edge joining two supports that differ in two direction orbits. For a legal antipodally odd coloring \(c\), let \(C_c(O)\subseteq\mathbb F_2^n\) be the antipodally invariant \(2n\)-cycle of direction-indexed geodesic color profiles associated with the support \(O\).

**Theorem (three overlap sizes and curvature detection).** Let \(n\ge5\), and let adjacent supports \(O,O'\) be represented by rooted paths sharing root \(x\) and differing by exchange of two consecutive directions \(i,j\) after a common prefix. Let \(y\) be the vertex reached after that prefix, and put
\[
a=D_j c_i(y),\qquad b=D_i c_j(y),\qquad
\kappa_{ij}(y)=a+b.
\]
Then
\[
\boxed{
|C_c(O)\cap C_c(O')|=
\begin{cases}
2n-2,&(a,b)=(0,0),\\
4,&(a,b)=(1,0)\text{ or }(0,1),\\
6,&(a,b)=(1,1).
\end{cases}}
\tag{PO1}
\]
Consequently the overlap has four vertices if and only if the exchanged cube square is curved. The alternatives six and \(2n-2\) distinguish the two possibilities for an uncurved square.

*Proof.* Cyclic root slides preserve the entire profile cycle, so move the common prefix beyond the final position, leaving the two compared orders \((i,j,k_1,\ldots,k_m)\) and \((j,i,k_1,\ldots,k_m)\), where \(m=n-2\). Translate both profile cycles by the same bit vector so the first has initial profile zero. The second initial profile is \(\delta=ae_i+be_j\), since adjacent exchange changes only the \(i,j\) profile entries, by the respective cross-differences.

Put \(I=e_i+e_j\), \(R=\sum_{r=1}^m e_{k_r}\), and \(S_t=\sum_{r=1}^t e_{k_r}\). The first profile cycle contains, over outside-direction mask zero, the three vertices \(0,e_i,I\), and over outside mask \(R\), the three vertices \(R,R+e_j,R+I\). Over each mask \(S_t\), \(1\le t<m\), it has one vertex \(S_t+I\), and over each mask \(R+S_t\) one vertex \(R+S_t\).

The swapped cycle has over outside mask zero the vertices \(\delta,\delta+e_j,\delta+I\), over \(R\) the vertices \(\delta+R,\delta+R+e_i,\delta+R+I\), and over the other masks respectively the vertices \(\delta+S_t+I\) and \(\delta+R+S_t\). Because \(m\ge3\), all outside masks displayed in these different groups are distinct, so intersections are computed separately within each group. When \(\delta=0\), the two zero-mask and \(R\)-mask groups contribute two common vertices each and the \(2(m-1)\) other vertices coincide, giving \(2n-2\). When \(\delta=e_i\) or \(e_j\), each three-vertex group contributes two and no remaining vertices coincide, giving four. When \(\delta=I\), the two three-vertex groups coincide entirely and no remaining vertices coincide, giving six. Finally \(\kappa_{ij}=a+b\) by the square-curvature identity, proving the criterion. \(\square\)

**Corollary (global curvature census in the support exchange graph).** Write \(M(c)\) for the number of antipodal square-face orbits with nonzero curvature. For \(n\ge5\),
\[
\boxed{\#\{OO'\in E(G_n):|C_c(O)\cap C_c(O')|=4\}
=2(n-2)!\,M(c).}\tag{PO2}
\]
*Proof.* Each support exchange edge is associated with the antipodal orbit of the square on which its adjacent order exchange occurs. By cube-automorphism transitivity, each square orbit occurs equally often. There are \(2^{n-3}n!\) support-exchange edges and \(\binom n2 2^{n-3}\) square orbits. The common multiplicity is their ratio \(2(n-2)!\). Apply (PO1). \(\square\)

**Sharp odd-dimensional consequence.** For every odd \(n\ge5\), every legal coloring has at least
\[
\boxed{2^{n-2}(n-2)!}
\tag{PO3}
\]
edges of \(G_n\) with four-point profile-cycle overlap. Equality holds if and only if its curvature is \(K_{ab}\) for one pair of dimensions \(a,b\), by the sharp square-curvature bound and the new minimizer classification in the projective exchange-disk Subsection. In an equality case, the four-overlap support-graph edges are precisely the edges that exchange the cyclically neighboring directions \(a,b\).

**Independent audit.** For \(n=4,5,6,7,8\), randomly generated legal antipodally odd colorings and random adjacent exchanges were compared against directly generated profile cycles, with 300 tests in each dimension and no discrepancy from the three-case formula. The condition \(n\ge5\) separates the two uncurved values \(6\) and \(2n-2\); for \(n=4\) they coincide.

These identities measure the curvature of an arbitrary original coloring through its induced profile cycles, without changing that coloring. They do not force a prescribed profile to occur: odd-dimensional colorings have many four-overlap edges, but a connection from the overlap census to a monochromatic full geodesic remains open.


#### Full coloring reconstruction from unlabeled geodesic profile cycles

For n>=3 let E be the M=n2^(n-2) antipodal orbits of undirected cube edges. A coherent orbit support O has one orbit per direction. Let C_c(O) be the set of 2n indexed profiles of the rooted geodesics whose edge orbit support is O.

**Cycle stabilizer lemma.** For a direction permutation pi, let V_pi be the 2n cyclic prefix-sum vectors of pi repeated twice. The only binary translations preserving V_pi are 0 and the all-one vector. Indeed V_pi induces a chordless 2n-cycle inside Q_n. At a vertex the two incident cycle-edge labels are one of the unordered pairs {pi_t,pi_(t+1)}. For n>=3 these n pairs are distinct. A translating automorphism preserving the cycle must take the initial vertex to itself or the antipodal vertex, since only these two have its unordered incident label pair. Both translations preserve the cycle.

**Theorem (all partial tomography fibers).** Fix any collection A of coherent supports, and form an undirected co-occurrence graph H_A on the M edge-orbit vertices by joining every two that lie in a common support from A; retain isolated orbit vertices. If H_A has k connected components, then for EVERY legal coloring c,
\[
\boxed{|\{d:C_d(O)=C_c(O)\text{ for all }O\in A\}|=2^k.}\tag{T1}
\]
All such d arise by independently reversing the orbit colors throughout any selected connected component of H_A.

*Proof.* The difference g=d+c is constant on each antipodal edge orbit. On a given support O, every rooted path profile changes by the same indexed vector g|_O, so C_d(O)=C_c(O)+g|_O. The cycle stabilizer lemma implies equality if and only if g|_O is the all-zero or all-one vector. This says g is constant on each edge of the co-occurrence graph, hence on each connected component. There are 2^k choices, and all preserve the measurements. QED.

The previously established two-orbit factorial extension theorem shows that any two edge orbits in different directions occur on one coherent full geodesic; orbits in the same direction connect through a third orbit. Thus the full co-occurrence graph is connected, and the **global reconstruction theorem** follows:
\[
\boxed{ C_c(O)=C_d(O)\text{ for every coherent }O
\iff d=c\text{ or }d=1+c. }\tag{T2}
\]

**Theorem (fixed-order folded-cube tomography).** Fix a single direction order pi and write O_x for the orbit support of the full path starting at x with order pi. Then O_x=O_y if and only if y=x or y=bar x. The 2^(n-1) supports are naturally indexed by vertices [x] of the folded cube Q_n/(x~bar x), and its n2^(n-2) undirected edges are naturally indexed by antipodal cube-edge orbits. Under these bijections O_[x] is the STAR of [x]. Therefore the 2^(n-1) measured profile cycles C_c(O_x), for all x with x_0=0, reconstruct c up to global complementation.

*Proof.* Direction-i orbit coincidence for roots x,y in the same order is equivalent to x+y in {0,e_i,1,1+e_i}. Intersecting these sets across every i gives {0,1} for n>=3, proving the first assertion. For distinct projective roots [x],[y], their supports share a direction-i orbit precisely when [y]=[x+e_i]. Every cube-edge orbit occurs at some root of the fixed direction order. These observations identify edge orbits with the edges of the connected n-regular folded cube, and each O_[x] with a vertex star. The union of every vertex star yields a connected co-occurrence graph, so (T1) leaves only the global complement. Reconstruction is constructive: invert each cycle to recover all n incident orbit colors up to one common bit, and synchronize those bits along common folded edges. QED.

**Sharp two-error detection.** Two legal colorings not related by global complementation differ in at least two of these fixed-order cycle measurements. A single antipodal edge-orbit recoloring changes precisely two cycles and realizes equality. The lower bound follows because the folded cube minus one vertex remains connected for n>=3, so a nonconstant edge-bit difference cannot be constant on the stars of all but one vertex.

**Measurement lower bound.** A single support cycle yields at most 2^(n-1) outcomes from its n orbit bits, by the stabilizer lemma. Since legal colorings modulo complement number 2^(M-1), every predetermined measurement family that always reconstructs c modulo complement has at least
\[
\left\lceil (n2^{n-2}-1)/(n-1)\right\rceil
\tag{T3}
\]
supports. The fixed-order construction uses 2^(n-1), fewer than twice this lower bound.

**Finite audit.** All 64 legal Q3 colorings give 32 fixed-order cycle signatures, each with a complementary pair of colorings. All 65536 legal Q4 colorings give 32768 signatures, likewise with fibers of size two. Full-family Q4 verification using all 24 coherent supports gives the same result. Independent code: nori_profile_cycle_tomography_verify.py and nori_profile_cycle_reconstruction_fast.cpp.

These tomography statements are unrestricted and retain all original edge-coloring information modulo global color reversal. They do not establish attainment of a specified profile; reconstructed colorings need not have their profile sets saturated.


#### Highest Boolean derivatives of full-geodesic profile-support incidence

Fix n>=3 and set M=n2^(n-2). Each legal antipodally odd coloring is encoded by one Boolean orbit variable z_e for every antipodal orbit e of undirected cube edges. Let S_n be the coherent n-orbit full-geodesic supports. For any target indexed profile w define the Boolean function
\[
F_w(z)=\sum_{O\in S_n}\mathbf1_{\{w\in C_z(O)\}}\pmod2. \tag{BD1}
\]
Thus F_w is the parity of the number of different coherent supports realizing w; the rooted path count is twice that number.

**Theorem (full leading-degree classification, all dimensions).** For every target w:

(a) For odd n>=3, the unique squarefree Boolean algebraic normal form of F_w has degree n-1. Its highest-degree monomials are
\[
\prod_{j\ne i}z_{e_j(O)}\qquad(O\in S_n,\ i\in[n]), \tag{BD2}
\]
all with coefficient one. Their number is n2^(n-2)(n-1)!.

(b) For even n>=6, F_w has degree n-2. Its highest-degree monomials are
\[
\prod_{j\notin\{i,k\}}z_{e_j(O)},\tag{BD3}
\]
where i,k are nonadjacent in the cyclic direction order of O and have odd cyclic separation. Every such coefficient is one. Their number is
\[
\frac{n(n-4)}4\,2^{n-2}(n-1)!. \tag{BD4}
\]

(c) In n=4, the degree is at most one by the same proof; separate complete enumeration of all 65536 legal colorings shows F_w is the zero function. The theorem in (a),(b) does not rely on this finite observation.

The highest-degree homogeneous part is independent of the target w, so F_w+F_v has strictly lower degree for every pair of targets w,v when n is odd >=3 or even >=6.

*Proof.* For each O fix a rooted representative with cyclic direction order pi. Varying the n independent orbit bits of O translates all its indexed path profiles by the same n-bit word. Its profile set consists of the 2n vertices of a cyclic-prefix walk using pi twice. Thus the local indicator \(\mathbf1_{\{w\in C_z(O)\}}\) has 2n accepting assignments among its 2^n orbit-bit inputs. Its degree-n squarefree coefficient is 2n modulo two, hence zero.

The coefficient of the monomial omitting just direction i is the parity of the number of accepting assignments with the i-th bit fixed zero. The profile cycle has n complementary vertex pairs, so this count is n, independent of root representative, target w, or any orbit-bit translation. It is one when n is odd and zero when n is even. The previously proved rigid completion theorem states that any n-1 prescribed orbit choices in different directions belong to at most one coherent support (the n=3 case follows also from the factorial two-orbit extension law). Therefore in odd n none of these degree-(n-1) coefficients can cancel between different supports, proving (a).

For even n, fix two orbit input bits for directions i,k and vary the other n-2. If their positions in the linear representative pi differ by d, where 1<=d<n, the cyclic-prefix cycle has each equal-bit pair (00 and 11) occurring n-d times and each unequal-bit pair (01 and 10) occurring d times. As n is even, all four multiplicities have parity d mod2. Hence the degree-(n-2) local coefficient is d mod2 independently of the target and orbit signs.

Now fix n-2 orbit variables from one coherent support O, omitting directions i,k. By the two-completion refinement of rigid orbit coherence, there is a second coherent support with these n-2 orbit choices if and only if i,k are cyclically adjacent in O; then their two nonzero degree-(n-2) contributions cancel. If i,k are cyclically nonadjacent, O is the sole completion, and the coefficient is one precisely when their cyclic positional separation is odd. Such nonadjacent odd-distance pairs exist for every even n>=6. Their number in a cyclic order of n directions is n(n-4)/4; distinct supports give distinct degree-(n-2) monomials by unique completion. This proves (b), while the same calculation gives the degree-one bound in n=4. Translation of a support-local profile cycle does not change any of the leading coefficients in (a),(b), proving target-independence. \(\square\)

**Corollary (universal high-order recoloring parity identities).** Fix ANY legal coloring z and a coherent support O. If n is odd, omit one chosen direction i and independently flip the n-1 remaining antipodal edge orbits of O in all 2^(n-1) ways. The XOR of F_w over the resulting colorings equals one, for every w. If n is even >=6, omit two cyclically nonadjacent directions at odd separation and flip the other n-2 orbit bits in every possible way; the analogous XOR over 2^(n-2) colorings also equals one. These identities are insensitive to all original colors outside the selected recoloring orbits. They follow by taking the corresponding iterated Boolean derivatives of (BD1).

In particular, for every profile w at least fraction 2^(-(n-1)) of all legal colorings in odd dimensions and fraction 2^(-(n-2)) in even dimensions n>=6 have an odd, thus nonzero, number of supports realizing w. This is a theorem across varying colorings and does NOT assert that every single coloring has a monochromatic geodesic.

**Verification.** Direct rooted-path dynamic programming verified the parity derivative identities on independent legal colorings in dimensions n=3,4,5,6,7,8. Enumeration of coherent supports and the proposed leading monomials in dimensions 3,4,5,6,7 yields counts 12,0,960,5760,161280, agreeing with (BD2),(BD4). A Q5 coloring represented by antipodal edge-orbit mask 0x78b5f2f3e has 138 rooted red full paths and hence 69 red-active coherent supports, verifying that the even-count phenomenon of Q4 fails already in Q5. Supporting artifacts: nori_witness_parity_boolean_degree_theorem.md, nori_profile_recoloring_parity_verify.py, nori_profile_incidence_degree_verify.py, and nori_profile_incidence_leading_terms_verify.py.

**Research significance and limitation.** The polynomial's highest Boolean derivatives are forced by coherent-support rigidity and cycle incidence, without restricting the original coloring. This supplies a uniform algebraic normal form constraint on global witness incidence and disproves extrapolating the Q4 coloring-independent even-count invariant. Because the nonzero derivatives compare different orbit-recolored colorings, they do not force a witness in one specified coloring; unrestricted NORI1 remains open.


#### Gauge parity cancellation and a parity-blind curvature fiber

Fix n>=3, put V=2^(n-1), and write G for the antipodally invariant vertex-gauge group modulo constants, with |G|=2^(V-1). A gauge acts on a legal coloring by c_i^h(x)=c_i(x)+h(x)+h(x+e_i). Let F_w(c) be the parity of the number of coherent antipodal edge-orbit supports whose profile cycles contain w.

**Theorem (all-dimensional gauge XOR identity).** For EVERY legal coloring, profile target, and n>=3,
\[
\boxed{\bigoplus_{h\in G}F_w(c^h)=0.}\tag{GP1}
\]
More sharply, for a fixed coherent support O, the number of h in G such that w lies on the profile cycle of O in c^h equals n*2^(V-n).

*Proof.* The projective path of O is a simple cycle of length n in the folded cube. Restricting gauges to its n vertex classes gives all even-parity n-bit edge changes uniformly: the cycle coboundary has rank n-1. Its 2n-word profile cycle contains n even-parity and n odd-parity words. Therefore n of the even edge changes align the cycle with any selected w, each having 2^(V-n) gauge preimages. Since V-n>=1 for n>=3, this number is even. Summing over coherent supports proves the XOR identity. \(\square\)

**Finite symbolic theorem (Q5 gauge-degree and locality).** Write z for the 40 independent antipodal edge-orbit color bits and h for the 16 projective vertex-gauge bits. In the squarefree Boolean polynomial expansion of F_0(z+delta h), no monomial contains three or more gauge bits. Moreover every quadratic gauge monomial h_u*h_v has u,v adjacent in the folded five-cube. Thus for every original legal Q5 coloring c, F_0(c^h) is a quadratic function of gauge potentials involving only terms on folded-cube edges.

*Finite proof.* Sum the red-path predicate products over all 16 projective root representatives and all 120 direction orders. Each predicate is the product over its five edges of (1+sign(e)+z_(orbit(e))+h_(first-endpoint(e))+h_(second-endpoint(e))). Root reversal implies that this sum modulo two equals F_0. Expand in the 56-variable squarefree ring, combining repeated monomials modulo two. A deterministic complete coefficient enumerator produces 9888 nonzero monomials, partitioned by gauge degree as 1824, 4800, 3264, 0, 0, ... . Every gauge-degree-two monomial is supported on an edge of the folded Q5. The finite certificate enumerates all polynomial coefficients over unrestricted z, rather than testing selected colorings.

**Finite theorem (Q5 curvature-fiber parity blindness).** Put b_i(x)=x_4 for i=0,1,2,3 and b_4(x)=x_3. This is legal; its curvature is nonzero precisely on square families in direction pairs {0,4},{1,4},{2,4}, for 12 antipodal square orbits. Every one of the 65536 legal Q5 colorings with this complete prescribed curvature obeys
\[
\boxed{F_w(c)=0\quad\text{for every target }w.}\tag{GP2}
\]

*Finite certificate.* The curvature-fiber theorem provides two gauge phases, each with 32768 colorings. For canonical antipodal edge-orbit variables, b is encoded by the all-zero mask, while the other phase has mask 0x9210810201 (complement all direction-zero edges). Substituting either phase mask in the complete symbolic polynomial gives the zero polynomial in all gauge bits. Thus F_0 vanishes on the entire curvature fiber. Complementing direction classes preserves curvature and translates any indexed profile to zero, proving GP2 for all targets. An independent dynamic-programming verifier enumerates both gauge phases and confirms that all 65536 colorings have even red-support counts, between 24 and 192, with no coloring devoid of red supports.

**Non-invariance under general gauges.** Curvature does not determine F_0 in general: legal Q5 orbit mask 0x78b5f2f3e gives 69 red-active supports; flipping one antipodal vertex star at folded vertex zero yields 54 supports without changing curvature.

The all-dimensional GP1 identity and the Q5 parity-blind curvature fiber are obstructions to deriving NORI1 via an odd gauge-averaged or curvature-fiber support-incidence parity. They do not negate monochromatic geodesic existence. The finite results rely on independently executable exhaustive symbolic and numerical verifiers preserved in nori_gauge_parity_obstruction.md, nori_q5_gauge_parity_symbolic.cpp, and nori_q5_curvature_fiber_parity_verify.cpp.



#### Integer-square rigidity of rooted color counts

Let \(H_x(\pi)\) count the color-one edges on the antipodal full geodesic rooted at \(x\) and ordered by \(\pi\in S_n\). A root has *constant color count* if \(H_x\) is independent of the order. Let \(\Gamma(c)\) be the undirected interaction graph on the \(n\) directions, joining \(i,j\) if either \(\partial_jc_i\) or \(\partial_ic_j\) is nonzero at some vertex.

**Theorem (root rigidity).** If \(\Gamma(c)\) has \(q\) connected components, the set \(F(c)\) of roots having constant color count is either empty or a coset of the binary span of the component indicator vectors. Hence
\[
\boxed{|F(c)|\in\{0,2^q\}.}
\]
Whenever \(F(c)\ne\varnothing\), each interaction component has even order, and every full geodesic rooted at \(x\in F(c)\) contains \(n/2\) edges of each color. If \(\Gamma(c)\) is connected, \(F(c)\) is empty or a single antipodal pair.

*Proof.* Reversing the direction order from the same root replaces each used edge by its antipodal mate, and therefore \(H_x(\operatorname{rev}\pi)=n-H_x(\pi)\). Constancy forces \(H_x=n/2\). Adjacent swaps generate the permutation group. On any square, write the four edge colors as \(a,b,d,e\), with the two rooted two-step routes having color-one counts \(a+b\) and \(d+e\). The swap changes the full-path count by \(a+b-d-e\). Every square is visited as two consecutive steps by some full path rooted at \(x\), with orientation determined by \(x\). Thus \(x\in F(c)\) if and only if \(a+b=d+e\), as integers, on every square oriented from \(x\).

Take \(x,y=x\oplus\mathbf1_T\in F(c)\), with \(i\in T\) and \(j\notin T\). On any \(i,j\)-square the two rooted orientations give \(a+b=d+e\) and \(a+d=b+e\). Hence \(a=e\), \(b=d\): the two direction colors are unaffected by flipping the other direction on this face. As the face is arbitrary, \(\Gamma(c)\) has no edge crossing \(T\) and its complement. Therefore \(T\) is a union of interaction components.

Conversely, because the cross-component derivatives vanish, \(c\) factors as a Cartesian product of legal antipodally odd colorings. A rooted full-path count is the sum of the corresponding factor counts and is constant precisely when every factor count is constant. Complementing all the bits in one factor complements its edge colors and preserves constant count. Thus complementing any selection of interaction components of a root in \(F(c)\) produces another member; the preceding necessity proves this gives all of \(F(c)\). Each factor admitting such a root has even dimension by the first paragraph. \(\square\)

**Signed-square criterion.** For each \(i,j\)-square anchored at the corner with \(i,j\) bits zero, let \(a,b,d,e\) be its edge colors as above. A flat root must obey
\[
x_i\oplus x_j=0\implies a+b=d+e,\qquad
x_i\oplus x_j=1\implies a+d=b+e.
\]
Conversely these conditions on all squares imply constant count, by adjacent-swap connectivity. Intersecting the permitted parities over every face of a given direction pair, then solving the resulting XOR equations, determines \(F(c)\) using \(O(n^2 2^n)\) square evaluations. If a square has odd color parity \(a+b+d+e=1\pmod2\), neither orientation is balanced and \(F(c)=\varnothing\).

**Corollary (four-path majority witnesses).** For every root \(x\notin F(c)\), some oriented square has unequal two-route color-one counts. Extend both routes to full rooted geodesics with identical prefix and suffix. Their red counts differ, and reversing both orders complements their counts. Among these at most four rooted geodesics, one has more than \(n/2\) color-one edges and another has more than \(n/2\) color-zero edges. Consequently this conclusion holds at every root when some square has odd binary curvature, and outside at most one antipodal pair when \(\Gamma(c)\) is connected.

**Theorem (self-dual integer potentials).** At the zero root, constant color count is equivalent to the existence of an integer function \(\rho:2^{[n]}\to\mathbb Z\) satisfying
\[
\rho(\varnothing)=0,\qquad
\rho(A+i)-\rho(A)\in\{0,1\},\qquad
\rho(A)=|A|+\rho([n]\setminus A)-\rho([n]),
\]
such that \(c_i(A)=\rho(A+i)-\rho(A)\). Necessarily \(\rho([n])=n/2\).

*Proof.* The integer square identities make the color-one path integral from the empty set to \(A\) independent of the increasing path; call it \(\rho(A)\). The increment condition follows from the binary edge colors. Put \(\rho^*(A)=|A|+\rho([n]\setminus A)-\rho([n])\). Antipodal oddness yields \(\rho^*(A+i)-\rho^*(A)=1-c_i([n]\setminus(A+i))=c_i(A)\). Since both functions vanish at the empty set they coincide. Conversely the stated conditions make the increments binary and antipodally opposed, and their sums telescope along every full path. Self-duality at \(A=[n]\) gives \(2\rho([n])=n\). \(\square\)

**Sharp complete-interaction construction.** For \(n=2r\) take \(\rho(A)=\min(|A|,r)\), the rank function of the self-dual uniform matroid \(U_{r,2r}\). Here \(c_i(x)=1\) if and only if fewer than \(r\) other vertex bits are one. Every pair of directions interacts, so \(\Gamma(c)\) is complete. The zero and all-one roots have constant count \(r\), and the first theorem excludes any others. A monochromatic full antipodal geodesic nevertheless exists: start at a vertex with \(r\) one-bits and \(r\) zero-bits, alternately flip one initially one-bit and one initially zero-bit. Each edge has color one. The connection between flat roots and self-dual integer ranks requires neither linearity nor matroid submodularity in general.


#### Antipodal permutation-clique anti-concentration for fixed-root full profiles

Let n>=3, let c be ANY legal antipodally odd coloring of the undirected edges of Q_n, and let x be any root. For a full indexed target w, put
\[
N_x(w)=|\{\pi\in S_n:\ w(x,\pi)=w\}|.
\]
For a permutation pi and direction i, write Pred_pi(i) for the set of directions preceding i. Call two orders pi,sigma **antipodally conflicting at i** when
\[
\operatorname{Pred}_\pi(i)\ \sqcup\ \operatorname{Pred}_\sigma(i)
=[n]\setminus\{i\}.
\tag{AC1}
\]
Their rooted direction-i edges are antipodal mates; hence both orders cannot realize the same target indexed color w.

**Theorem (universal sharp constant for target-order multiplicity).** For all fixed roots and legal colorings,
\[
\boxed{N_x(w)\le n!/3\quad(n=3,4),\qquad
N_x(w)\le n!/4\quad(n\ge5).}
\tag{AC2}
\]
The bound n!/4 is attained in Q5 by a coloring whose rules are majority functions of three possibly complemented other bits. The n!/3 bound is attained in Q4. Thus 1/4 is the best dimension-independent upper constant applying to all n>=5.

*Proof.* For n=3, the three permutations (012),(120),(201) are pairwise conflicting. For n=4 the three permutations (0123),(1230),(3021) are pairwise conflicting, at directions 0,3,2, respectively. For n>=5, choose five distinguished directions labeled 0,1,2,3,4 and let L=(n-1,n-2,...,5) denote the descending list of remaining directions. Construct four complete direction orders
\[
A=(L,0,1,2,3,4),\quad
B=(1,3,2,4,0,L),\quad
C=(4,L,0,2,1,3),\quad
D=(3,4,2,L,0,1).
\tag{AC3}
\]
A direct predecessor-set check shows conflicting directions for the six pairs AB,AC,AD,BC,BD,CD are respectively 0,4,2,2,1,3, independent of the length of L. No two members of this quartet can realize one full indexed target.

Relabel all n direction symbols simultaneously by any permutation g of [n]. The resulting three or four orders are again pairwise conflicting, so at most one realizes w. Sum this inequality over all n! relabelings g. For each template order A, the map g->gA is a bijection of S_n, and likewise for all other templates. Thus 4N_x(w)<=n! for n>=5, or 3N_x(w)<=n! in dimensions 3,4. This proves (AC2). \(\square\)

**Explicit sharp Q5 example.** Let Maj(a,b,c) be the Boolean majority function of three bits. Define five edge-color rules by
\[
\begin{aligned}
c_0(x)&=\operatorname{Maj}(1+x_2,x_3,x_4),\\
c_1(x)&=\operatorname{Maj}(1+x_0,1+x_2,x_4),\\
c_2(x)&=\operatorname{Maj}(1+x_0,x_3,x_4),\\
c_3(x)&=\operatorname{Maj}(1+x_0,1+x_2,x_4),\\
c_4(x)&=\operatorname{Maj}(1+x_0,1+x_2,x_3).
\end{aligned}
\tag{AC4}
\]
Each rule ignores its own direction bit. Because Maj complements upon complementing all three arguments, all five rules obey antipodal oddness. Exhaustive evaluation of the 120 direction orders at root 00000 gives N_0(00000)=30=5!/4. The full profile-frequency histogram is 30,30,10,10 and eight occurrences of 5, summing to 120. In Q4, a legal orbit coloring with canonical little-endian 16-bit mask 0x300c has eight all-red orders from root zero, attaining 4!/3.

**Scope.** This anti-concentration theorem concerns a FULL n-direction indexed target profile. The four-order clique does not by itself imply an analogous bound for a target prescribed on only five directions inside a larger cube: averaging over all relabelings changes that five-direction set. The proof does not imply N_x(w)>0, and hence does not establish NORI1. It provides a new coloring-independent permutation-incompatibility structure for one FIXED original coloring, distinct from earlier gauge or recoloring averages. Direct program verification tests the quartet for n=5,...,19 and independently evaluates the sharp Q5 example; see nori_permutation_conflict_anticoncentration.md and nori_permutation_conflict_verify.py.


#### Unbounded antipodal permutation-conflict cliques: vanishing rooted profile mass

Fix n>=3, a legal antipodally odd edge coloring c of Q_n, a root x, and a direction-indexed complete color target w. Put N_x(w)=#{pi in S_n: profile_c(x,pi)=w}. For a direction order pi let P_pi(i) be the set of directions preceding i. Two orders pi,sigma **conflict at i** if P_{\pi}(i)\mathbin{\triangle}P_{\sigma}(i)=[n]\{i}. Their rooted direction-i edges are antipodal and therefore cannot both have target color w_i. This is the predecessor-conflict graph on S_n.

**Theorem (unbounded conflict cliques).** For every integer t>=5, the conflict graph on S_n contains a clique of t permutations whenever
\[
\boxed{n\ge\binom t2-2.}\tag{NC1}
\]
Consequently, for n>=8, putting
\[
K(n)=\left\lfloor(1+\sqrt{8n+17})/2\right\rfloor,
\]
every legal coloring, root and complete target satisfy
\[
\boxed{N_x(w)\le n!/K(n).}\tag{NC2}
\]
In particular the probability of a prescribed complete target under a uniformly random full direction order is at most (1+o(1))/sqrt(2n), uniformly over all legal colorings and roots. The rooted indexed profile distribution has min-entropy at least log_2 K(n).

*Proof by nested-cut augmentation.* Define a **nested-cut clique** to be a collection of pairwise-conflicting direction orders pi_a, each with a designated prefix A_a, such that (i) the A_a form a chain under inclusion and (ii) for every pair a,b, some conflicting direction i_ab is in precisely one of A_a,A_b.

A nested-cut clique of t orders on direction set D can be augmented to t+1 orders by introducing t new directions e_1,...,e_t. Insert the entire helper block in reverse order at the designated cut in each old order, preserving the designated old prefix A_a. Every old pair remains conflicting at its previous witness: all added directions now precede that witness in one order and follow it in the other, by (ii).

List the t old rows in decreasing order of inclusion A_{a_1} superset ... superset A_{a_t}. Assign helper e_s to row a_s. Since the complements D\A_{a_s} form an increasing chain, choose a permutation of the old directions in which these complements are nested prefixes, and form a new direction order by inserting each e_s immediately after all old directions of D\A_{a_s} have appeared. This new order lists the helpers in forward order, opposite to the old rows. For each old row a_s, its predecessor set at e_s among old directions is A_{a_s}, while in the new order it is D\A_{a_s}; its predecessor bits on all other helpers are also opposite. Thus the new order conflicts with old row a_s at helper direction e_s.

Give the new order its designated cut after its final direction. Its prefix is the entire enlarged direction set, containing every old prefix. For old/new pairs, their helper witness e_s lies after the old cut and before the new cut; old/old cut separation was preserved. Therefore the enlarged family is another nested-cut clique.

The induction starts with the following five orders in dimension eight and their specified cut lengths:
\[
\begin{array}{ll}
A=(0,1,2,3,4,5,6,7),& |A_A|=0;\\
B=(1,2,3,4,6,5,7,0),& |A_B|=8;\\
C=(3,6,4,5,7,2,0,1),& |A_C|=6;\\
D=(6,7,5,0,4,1,2,3),& |A_D|=3;\\
E=(7,0,5,1,2,4,3,6),& |A_E|=1.
\end{array}
\tag{NC3}
\]
Their cut prefixes are the nested sets empty, {7}, {5,6,7}, {2,3,4,5,6,7}, [8]. Conflict witnesses for AB,AC,AD,AE,BC,BD,BE,CD,CE,DE are respectively 0,2,5,7,1,4,5,3,4,6; each belongs to precisely one of the two cut prefixes. Hence the five-order seed satisfies both invariants.

Iterating augmentation gives t orders on 8+sum_{j=5}^{t-1}j=binom(t,2)-2 directions. To enlarge the ambient dimension by one while keeping t fixed, insert the new direction at the selected cut of every order, retaining each original prefix as its selected cut. Every pairwise witness remains conflicting because the new direction is on opposite sides of that witness in the two orders. Nesting and cut separation persist. This proves (NC1) for every n above the threshold.

Finally, relabel all n directions simultaneously in a fixed clique of K(n) orders. Every relabeled clique contains at most one path realizing w. Sum that inequality over all n! relabelings; each slot of the clique ranges bijectively over all n! rooted direction orders. Hence K(n)N_x(w)<=n!, proving (NC2). \(\square\)

**Proposition (independence-number interpretation).** Let G_n be the predecessor-conflict graph. Then
\[
\boxed{\max_{c,x,w}N_x(w)=\alpha(G_n).}\tag{NC4}
\]
Indeed, accepting orders form an independent set. Conversely, given ANY independent family of orders at one root and a chosen profile w, prescribe color w_i on the direction-i edge visited by every order in the family. Two such prescriptions on an antipodal edge orbit contradict one another precisely when the two orders conflict. Thus independence ensures compatible prescriptions, and the unconstrained edge orbits can be colored freely with antipodally opposite colors. The maximum is attained by some legal coloring.

**Proposition (matching bound on every conflict clique).** If t orders form a clique, then t<=n+1, and if t is odd, t<=n. For every direction i, the predecessor sets P_pi(i) over clique members are pairwise distinct: if pi,sigma conflict at j!=i, the relative order of i and j differs, while if they conflict at i their predecessor sets are complementary. Therefore the pairs conflicting at any fixed direction i form a matching, because each predecessor set has only one complement among the distinct sets. Assign a witnessing direction to each pair in the clique. This properly edge-colors K_t with at most n colors. Its edge chromatic number is t-1 for even t and t for odd t, giving the bound.

**Independent audit.** A recursive verifier checks the initial nested-cut clique, all pairwise witnesses, the augmentations, and single-direction inflation. It produces cliques of sizes 5 through 20 in ambient dimensions 8,13,19,26,34,43,53,64,76,89,103,118,134,151,169,188, respectively. The source is nori_conflict_clique_induction_verify.py and the full derivation is nori_nested_cut_permutation_cliques.md. The proof does not depend on these computations. The prior bounds n!/3 for n=3,4 and n!/4 for 5<=n<=7 remain as published. No sharpness assertion is made for NC2 in n>=8.

**Scope.** The bound tends to zero with dimension for the frequency of each full target among all orders at a fixed root. An upper bound on a prescribed target's frequency does NOT prove its attainment, and unrestricted NORI1 remains open.


**Corollary (first-direction coloring of the conflict graph).** Two conflicting full direction orders cannot share their first direction: at that direction their predecessor sets are both empty; at every other direction both predecessor sets contain that shared first direction, precluding complementary predecessors. Nor can they share their last direction, by the dual argument. Hence the predecessor-conflict graph G_n is n-partite via the first direction (also via the last direction), and every conflict clique has at most n members. Conversely, all (n-1)! permutations with the same first direction are pairwise nonconflicting and, by the independent-set realization proposition above, can simultaneously attain any selected target from a selected root in some legal coloring. Thus for n>=8 the optimal rooted target multiplicity satisfies
\[
\boxed{(n-1)!\le \max_{c,x,w}N_x(w)=\alpha(G_n)\le n!/K(n).}
\]


#### Catalan root-packing duality and sharp even-dimensional permutation-conflict bounds

For n=2m>=2, let G_n be the predecessor-conflict graph from the preceding theorem: two complete direction orders pi,sigma are adjacent when for some direction i their predecessor sets have symmetric difference [n]\{i}. The paths from any common root use antipodal direction-i edges and cannot both realize one indexed target profile.

**Theorem (Catalan packing bound).** Every clique in G_(2m) has size at most m+1:
\[
\boxed{\omega(G_{2m})\le m+1.}\tag{CP1}
\]
If a clique has m+1 orders, their corresponding families of Dyck-admissible balanced roots partition the middle layer of the cube.

*Proof.* Consider the previously studied legal balanced-majority coloring
\[
b_i(x)=\mathbf1\{\sum_{j\ne i}x_j\ge m\}.
\]
It ignores x_i and is antipodally odd since the other-bit count t changes to 2m-1-t. Let D be any m-set of directions and root x_D have ones precisely in D. A full rooted path orders the initially one-valued directions as down steps and initially zero-valued directions as up steps. At a vertex of total weight h, a down step is red precisely if h<=m; an up step is red precisely if h<m. Thus the full path is red precisely when its direction word is a Dyck word, with every prefix containing at least as many members of D as nonmembers.

For a FIXED permutation pi, the number of balanced roots D yielding a red full path is Catalan C_m=(1/(m+1))*binom(2m,m): choose the down-step positions among the 2m positions to form a Dyck word. For two conflicting orders pi,sigma, their sets of successful balanced roots are disjoint; otherwise both paths would be red at their conflicting antipodal edge pair. Hence a clique of t permutations supplies t disjoint C_m-element subsets of the binom(2m,m) balanced roots. Therefore t*C_m<=binom(2m,m), proving t<=m+1. If equality holds, those Dyck-root sets cover the full middle layer and form the claimed partition. \(\square\)

**Corollary (sharp rooted complete-target multiplicities in Q2,Q4,Q6,Q8).** Recall the independent-set realization theorem
\[
\max_{c,x,w}N_x(w)=\alpha(G_n).
\]
At every balanced root of the majority coloring, the red rooted orders are obtained by freely relabeling the m down and m up steps of a Dyck word. Their number is
\[
(m!)^2 C_m=(2m)!/(m+1).\tag{CP2}
\]
Therefore \(\alpha(G_{2m})\ge(2m)!/(m+1)\) in every even dimension. If a clique of m+1 orders exists, averaging its images under all direction relabelings gives the reverse inequality and hence equality. Earlier certified cliques of sizes 2,3,4,5 in dimensions 2,4,6,8 attain the bound. Consequently
\[
\boxed{\alpha(G_2)=1,\quad\alpha(G_4)=8,\quad
\alpha(G_6)=180,\quad\alpha(G_8)=8064.}\tag{CP3}
\]
These equalities maximize the number of rooted orders realizing ANY prescribed full target across all unrestricted legal colorings and all roots. Every corresponding clique gives a partition of the balanced middle-layer roots into its Catalan-red-root classes.

**Asymptotic counterweight to strong anti-concentration claims.** The majority coloring exhibits, in every even dimension 2m, a prescribed rooted full target of frequency 1/(m+1)=2/(n+2). Therefore no universal exponentially decaying bound on the maximal rooted target probability is possible. Together with the preceding nested-cut clique bound O(n^(-1/2)), it sandwiches optimal worst-case target concentration between 2/(n+2) along even n and 1/K(n) in all n>=8. It does not establish NORI1 or any fixed-coloring target existence.

**Independent audit.** The verifier nori_catalan_conflict_duality_verify.py tests the majority rule and Dyck correspondence in dimensions 2,4,6,8,10; counts all rooted red orders through n=8, and verifies that the published cliques in n=2,4,6,8 partition the sets of respectively 2,6,20,70 balanced roots into Catalan classes of sizes 1,2,5,14. No discrepancies were found. Full derivation: nori_catalan_conflict_duality.md. The majority coloring as an example was previously known to the archive; its new application here is the universal clique packing theorem and the sharp unrestricted multiplicity computation through n=8.


**Odd-dimensional reader lift and universal logarithmic min-entropy scale.** For n=2m+1, start with the legal majority coloring on the first 2m directions. Add a direction z whose edge color is x_a, where a is one initially-one direction of a balanced starting root; leave the old direction color rules independent of z. The resulting coloring is legal and antipodally odd. For every all-red old path, inserting z after the direction-a step produces an all-red full path.

In a Dyck word of length 2m, the position d_k of its k-th downstep is smaller than the position u_k of its k-th upstep. Therefore the sum of all downstep positions is less than m(2m+1)/2, and an initially-one direction a has, averaged over the equally labeled red paths, mean rank smaller than (2m+1)/2. Consequently strictly more than half of all insertion slots occur after a. Since the original rooted red fraction is 1/(m+1), the extended rooted red fraction is strictly greater than 1/(2m+2)=1/(n+1).

Together with the even-dimensional balanced-majority fraction 2/(n+2), this establishes
\[
\boxed{\max_{c,x,w} N_x(w)/n!\ge1/(n+1)}
\]
for all n>=2 (strictly for odd n>=3). Combined with the earlier upper bound 1/K(n) for n>=8, the smallest possible rooted profile min-entropy across legal colorings is of order log n: it lies between log_2 K(n) and log_2(n+1). Thus any proposed universal exponentially small upper bound on individual rooted profile masses is false. Independent enumeration gives red rooted order counts 2,26,804,45648,4135680 in the odd-dimensional reader-lift examples n=3,5,7,9,11, respectively. This is an extremal obstruction, not a route to positivity of a prescribed profile in one original coloring.


#### Exponential nonadaptive order-family obstruction

For n>=4 let m=floor(n/4). Any coloring-independent family of fewer than 3^m direction orders fails, for some legal antipodally odd coloring of Q_n, to provide a one-switch full geodesic from ANY root. The Q4 selector uses c0=x3,c1=1+x2,c2=1+x3,c3=x2: among 24 orders, only the eight rotations/reversals of 0123 are usable. The other cyclic classes 0132 and 0213 give temporal color words (a,1+b,b,a) and (a,1+a,b,1+b), each with at least two changes from all roots. Partition 4m directions into four-sets. Every proposed global order specifies a vector of m unoriented cyclic types, each taking 3 values. Choose a missing vector and relabel independent Q4 selectors on the blocks to make only that vector usable; any remaining direction reads the first block. Every proposed global order is bad in a block and therefore has at least two changes globally. The same argument shows that for any coloring-independent random distribution of orders, some legal coloring admits a usable order with probability at most 3^(-m), even with all roots tested; K prechosen samples have worst-case success probability at most K*3^(-m). Complete Q4 census: 48 legal colorings with 8 usable orders, 1488 with 16, 64000 with 24. Independent Q8 product verifier checks 8 proposed orders over all 256 roots. Full proof and code in attached nori_exponential_order_family_obstruction.md. This restricts nonadaptive order selection, not unrestricted NORI1.

#### Strict nonoptimal local turn-energy minima

For a coherent cube geodesic support O, let T(O) be the number of changes in its 2n-step antipodally complementary cyclic edge-color word. T is always 2 modulo 4; T=2 means O supports a monochromatic geodesic. The union of O and its n adjacent-exchange neighbors involves 3n independent antipodal edge orbits: per direction the original orbit and the two alternatives toggling a cyclic neighbor. A prescribed cyclic color word on O can be extended to a legal coloring with every neighbor having strictly more turns precisely when each monochromatic cyclic run has length at least three. Proof: exchanging adjacent directions replaces two neighboring color bits and their antipodes. The maximum increase in the local three-gap transition count is two when the original local transition count is zero or one, and zero otherwise; the new orbit choices of distinct neighbors are independent. Consequently for every odd s>=3 and n>=3s one can prescribe T(O)=2s and all neighbors T=2s+4. A second path with the same direction order rooted at e0+e2 uses no prescribed orbit in these dimensions, so set every edge of that path red, giving another support R with T(R)=2. Thus strict nonmonochromatic local minima first occur in dimension nine, with central first-half word 000111000. The all-dimensional proof and verifier are in attached files nori_strict_cyclic_turn_traps.md and nori_strict_turn_trap_verifier.py; checks passed for n=9,10,15,20,27. This precludes strict local turn descent as a universal NORI1 forcing argument.

#### Global turn-star census, sharp imbalance moments and forcing criterion

For n>=3, let O_n be the 2^(n-2)(n-1)! coherent antipodal edge-orbit supports of full geodesics, and T_c(O) the cyclic number of color transitions along the 2n-edge antipodally complementary cycle of O. Write r(x) for the number of color-one incident edges at cube vertex x, so r(bar x)=n-r(x). Define signed vertex-star imbalance S(x)=sum_i (-1)^(c_i(x))=n-2r(x).

THEOREM 1 (global turn/star census, unrestricted): sum_(O in O_n) T_c(O) = 2(n-2)! sum_[x] r(x)(n-r(x)), where [x] denotes an antipodal vertex pair. Equivalently E_O T_c(O) = [n^2-E_x S(x)^2]/(n-1). PROOF: Each support contributes n wedge incidences in the folded cube Q_n/(x~bar x). There are 2^(n-1) binom(n,2) projective wedges; the automorphism group is transitive on them. Thus every wedge is contained in n*2^(n-2)(n-1)!/[2^(n-1)binom(n,2)]=(n-2)! supports. At x, precisely r(x)(n-r(x)) pairs of unlike-colored incident edges give projective wedge color changes. Each projective change appears twice on its 2n-edge antiperiodic cycle. Double count. Expand (n-2r)^2=n^2-4r(n-r).

THEOREM 2 (sharp range and signed-star inequality): For every legal coloring, 2<=E_O T_c(O)<=n+1 for odd n, and <=n^2/(n-1) for even n>=4. Both bounds are attained for every dimension. The lower inequality is equivalent to E_x S(x)^2 <= (n-1)^2+1. Equality on the low-energy end holds iff EVERY coherent support contains a monochromatic full geodesic. Equality on the upper-energy end holds iff every vertex has as balanced a red/blue incident star as possible: r in {(n-1)/2,(n+1)/2} for odd n or r=n/2 for even n.

PROOF: Each antiperiodic cyclic word has 2 modulo 4 transitions, at least 2. Hence E T>=2. The upper bounds use the parity-pointwise inequalities S(x)^2>=1 for odd n, S(x)^2>=0 for even n. Sharp low-energy construction: c_0(x)=x_1, c_i(x)=x_0 for i>=1. At antipodal representatives x_0=0, the red degree is x_1, producing sum_[x]r(n-r)=2^(n-2)(n-1), so E T=2. Sharp high-energy construction, even n>=4: pair (0,1) with c_0=x_2,c_1=1+x_2 and pair each (2k,2k+1), k>=1, with c_(2k)=x_0,c_(2k+1)=1+x_0. Every pair contributes one color-one incident edge, so r=n/2. For odd n>=3 use c_0=x_1,c_1=1+x_0,c_2=x_0, then each remaining pair (3,4),(5,6),... reads x_0 with opposite offsets. This yields r=(n-1)/2+x_1. All rules ignore their own direction and are odd under antipodal complementation.

THEOREM 3 (quantitative certificate for NORI1): Put Delta=(n-1)^2+1-E_x S(x)^2>=0. The fraction of coherent supports containing a monochromatic full geodesic is >=max(0,1-Delta/[4(n-1)]). In particular E_x S(x)^2>n^2-6(n-1) guarantees a monochromatic full antipodal geodesic. PROOF: T_c(O)=2+4h(O) with nonnegative integer h. The turn/star identity gives E_O h=Delta/[4(n-1)]. Every nonmonochromatic support has h>=1, so Markov bounds its fraction. For n=3,4, the universal upper bounds n+1=4 and n^2/(n-1)=16/3 are below six, giving a short direct proof of the NORI1 geodesic statement in these dimensions. For n>=5 the moment condition does not cover all legal colorings.

Independent incidence and direct-energy enumeration verifies Theorem 1 for n=3,4,5,6: projective wedge multiplicities 1,2,6,24 and support counts 4,24,192,1920. The explicit extremizers have been independently checked for every dimension n=3,...,12. Full proof and verifiers in nori_turn_star_moment_theorem.md, nori_global_turn_energy_verify.py, nori_turn_star_extremizers_verify.py. A mathematical theorem for arbitrary nonlinear legal colorings; no assumption of monochromatic connectivity or local descent. The unrestricted dimension-uniform NORI1 conjecture remains open.

### Universal three-direction prescription for unrestricted antipodally odd cube-edge colorings

**Theorem.** Let \(n\ge3\) and let \(c_i(x)\in\mathbb F_2\) color each * undirected* direction-\(i\) edge of \(Q_n\), satisfying
\[
c_i(x)=c_i(x\oplus e_i),\qquad c_i(\bar x)=1+c_i(x).
\]
For **every** three distinct directions \(i,j,k\) and **every** prescribed color triple \((t_i,t_j,t_k)\in\mathbb F_2^3\), some full antipodal geodesic (root and complete permutation unrestricted) traverses its \(i\)-, \(j\)- and \(k\)-edges in precisely the prescribed colors. Equivalently, the set \(\mathcal W(c)\) of full direction-indexed edge-color profiles projects **surjectively** to \(\mathbb F_2^3\) on every three-direction set. There are no restrictions on nonlinearity, exterior dependence, or the colors of the remaining \(n-3\) edges.

**Root-rotation identity.** For a full geodesic with root \(x\) and direction order \(p=(p_1,\ldots,p_n)\), use root \(x\oplus e_{p_1}\) and order \((p_2,\ldots,p_n,p_1)\). The new path traverses the *same  edges* in all directions other than \(p_1\). Its final \(p_1\)-edge is antipodal to the original first edge; thus its direction-indexed color profile is the original profile with precisely direction \(p_1\) complemented. This relies on both undirected undirectedness and edge antipodal oddness.

**Proof.** Suppose some prescribed triple never occurs. Complement the color of *every  edge* in direction \(r\in\{i,j,k\}\) by \(t_r\), leaving all other edge directions alone. Both edge axioms survive, and the impossible triple becomes \(000\). Taking the antipodal root of any full geodesic with the **same** direction order complements every direction's color, so \(111\) is also impossible.

Choose an arbitrary root \(x\) and complete direction order \(p=(i,j,k,r_4,\ldots,r_n)\); write \(A,B,D\) for the  edge colors at its first three steps. Rotate the first direction to the end three times, updating the root as above. The four resulting **full antipodal geodesics** have projected triples
\[
(A,B,D),\
(A+1,B,D),\
(A+1,B+1,D),\
(A+1,B+1,D+1).
\tag{1}
\]
None may be \(000\) or \(111\). A three-step geodesic of the three-cube avoiding these two opposite vertices must have starting bits \(010\) or \(101\) in its *step order*: its four successive Hamming weights must be \(1,2,1,2\), or \(2,1,2,1\). Consequently for **every root** and **every full order with prefix \(i,j,k\)** the first three edge colors are
\[
(A,B,D)=(q,1+q,q). \tag{2}
\]

Now compare the two full direction orders \((i,j,k,r_4,\ldots,r_n)\) and \((j,i,k,r_4,\ldots,r_n)\) *from the same arbitrary root \(x\)*. They traverse the **same  \(k\)-edge** at their third step, since in both cases they have already flipped precisely the directions \(i,j\). By (2), the first color on each path equals its common third color. Therefore
\[
c_i(x)=c_j(x)\qquad\text{for every }x\in Q_n. \tag{3}
\]
Apply (3) also at \(x\oplus e_i\) and use that \(c_i\) is the color of an **undirected** \(i\)-edge:
\[
c_j(x\oplus e_i)=c_i(x\oplus e_i)=c_i(x).
\]
But these are precisely the colors of the first and second edges in the original path with prefix \((i,j,k)\), and (2) demands that those two colors are *different*. Contradiction. Thus every prescribed triple occurs. \(\square\)

**Research significance and  limitation.** This strengthens NORI's previously recorded unrestricted **two-direction prescription** corollary to **three-direction prescription** for the *whole* NORI1 class. Full affine span of the profile set by itself does not imply triple surjectivity; the essential new ingredient is that cyclic geodesic root slides realize the three-cube walk (1), whose avoidance of one antipodal pair is rigid. Any failure to realize a *complete* target \(n\)-bit word must therefore involve compatibility among **at least four directions**, not a missing one-, two-, or three-direction marginal. The result does not yet force the all-zero or all-one full profile and does not solve unrestricted NORI1. It also does not prove a statement for ordered-three-face boundary tournaments: here the local colors attach to  edges, and the root slide complements precisely one direction-indexed edge color.

**Consistency check (not used in proof).** Direct enumeration of all \(2^{16}\) legal  antipodally odd edge colorings of \(Q_4\) found complete four-bit profile coverage; separate binary-integer feasibility tests found no obstruction to triple prescription in dimensions five, six, and seven. The argument above is valid in every dimension independently of these checks.

### Antipodal multifacet bridging: an  localization theorem for unrestricted NORI1

#### Statement and historical context

Let \(k\ge2\). Define \(B_k\) to be the **Leader–Long/Feder–Subi geodesic 2-cp assertion in dimension \(k\)**:

> Every arbitrary binary coloring \(d\) of the *undirected  edges* of \(Q_k\) admits a **full antipodal geodesic** whose edge-color sequence changes at most once.

Unlike NORI1, \(d\) need not satisfy any antipodal relation. For integers \(n>k\), and a fixed \(k\)-set \(S\subseteq[n]\), define \(P_{n,S}\) to be the **full geodesic partial-color prescription assertion**:

> For every antipodally odd coloring \(c\) of the undirected  edges of \(Q_n\), and every target \(t\in\mathbb F_2^S\), there exist a  root \(x\) and a permutation \(p\) of **all \(n\) directions** such that the full antipodal geodesic \(P(x,p)\) traverses its unique edge in each direction \(i\in S\) with color precisely \(t_i\). The colors in the other \(n-k\) directions are unrestricted.

This is an  property of all legal NORI1 colorings, not a condition on affine or direction-only subclasses.

**Theorem 1 (multifacet bridge equivalence).** For every \(k\ge2\), every \(n>k\), and every fixed \(k\)-set \(S\subseteq[n]\),
\[
\boxed{\quad B_k\quad\Longleftrightarrow\quad P_{n,S}.\quad}
\tag{1}
\]
In particular, the property that *every* legal antipodally odd -edge coloring in *any one larger dimension* realizes all prescribed colors on *one specified set of \(k\) directions* is equivalent to the arbitrary-color \(k\)-cube 2-cp geodesic assertion.

The implication \(B_k\Rightarrow P_{n,S}\) uses **all** \(n-k\) exterior directions as a single antipodal bridge between opposite  \(k\)-faces; no colors along the bridge need to be specified.

#### Proof of the forward implication

Assume \(B_k\). Fix \(n>k\), \(S\), a legal  antipodally odd edge coloring \(c\) of \(Q_n\), and an arbitrary target \(t=(t_i)_{i\in S}\).

Identify \(Q_n=Q_S\times Q_D\) with \(D=[n]\setminus S\ne\varnothing\); write a cube vertex as \((u,z)\). Fix an **arbitrary** exterior vertex \(z\in Q_D\). On the *lower  \(S\)-face* \(Q_S\times\{z\}\), define an arbitrary undirected-edge coloring
\[
d_i(u):=c_i(u,z)\oplus t_i,\qquad i\in S.
\tag{2}
\]
This is a legal  \(k\)-cube edge coloring because \(c_i(u,z)=c_i(u\oplus e_i,z)\); **no** antipodal oddness is assumed for \(d\).

By \(B_k\), there exists a full antipodal geodesic \(R\) of \(Q_S\) whose \(d\)-color word has at most one change. Reverse its traversal if needed so its word is \(0^a1^{k-a}\), with \(0\le a\le k\). Write
\[
R:\ u_0\xrightarrow{U}u_a\xrightarrow{V}\bar u_0
\tag{3}
\]
where \(U\) and \(V\) denote ordered, disjoint lists of \(S\)-directions whose union is \(S\), with all edges of \(U\) having \(d\)-color 0 and all edges of \(V\) having \(d\)-color 1. Empty \(U\) and \(V\) are permitted.

Now construct a **full \(n\)-direction cube geodesic**, starting at \((u_a,z)\):

1. Traverse the \(U\)-edges in reverse order inside the lower  facet, moving \((u_a,z)\to(u_0,z)\).
2. Traverse *every* direction of \(D\) precisely once, in any order, moving \((u_0,z)\to(u_0,\bar z)\).
3. Follow the **reverse of the \(Q_S\)-antipodal image of the \(V\)-suffix** from (3), inside the upper  facet, moving \((u_0,\bar z)\to(\bar u_a,\bar z)\).

All \(n\) directions are used precisely once, so the constructed path is a full antipodal geodesic. On its \(U\)-edges, the lower-facet formula (2) and the undirected reversal of the 0-block give  \(c\)-color \(t_i\). On its \(V\)-edges, each upper-facet edge is the **global cube antipode** of the corresponding lower-facet  edge of \(R\) (after projecting the \(Q_S\)-antipodal reversal); its  \(c\)-color is therefore the complement of the original lower color \(d_i\oplus t_i=1\oplus t_i\), namely \(t_i\). The intervening \(D\)-edges have arbitrary colors, which do not affect the required prescription. Thus \(P_{n,S}\) holds. \(\square\)

#### Proof of the reverse implication

Assume \(P_{n,S}\). Let \(d\) be **any** arbitrary binary coloring of the undirected edges of \(Q_k\). Pick a distinguished exterior direction \(s\in D=[n]\setminus S\). Define a  edge coloring \(c\) of \(Q_n\) using \(d\), with \(u\in Q_S\), \(z\in Q_D\), and one distinguished original coordinate \(i_0\in S\):

\[
c_i(u,z)=
\begin{cases}
d_i(u),&z_s=0,\\
1\oplus d_i(\bar u),&z_s=1,
\end{cases}
\qquad(i\in S),\tag{4}
\]
\[
c_j(u,z)=u_{i_0}\quad(j\in D).\tag{5}
\]
The main \(S\)-edge colors are  because \(d_i\) is invariant under flipping its free \(i\)-bit; the exterior \(j\)-edge color in (5) is independent of its free \(j\)-bit. Antipodality of the *full* \(Q_n\) interchanges the two \(s\)-facets and complements the main colors in (4). It also complements \(u_{i_0}\), verifying \(c_j(\bar u,\bar z)=1\oplus c_j(u,z)\) for each \(j\in D\). Thus \(c\) is a legitimate antipodally odd -edge coloring of \(Q_n\). The colors in (4) depend on exterior coordinates **only through \(z_s\)**.

By \(P_{n,S}\), choose a full antipodal cube geodesic whose edge color is 0 in every direction of \(S\). Reverse its traversal if needed so that the unique \(s\)-step crosses from \(z_s=0\) to \(z_s=1\). Let \(U\) be its ordered \(S\)-direction list before the \(s\)-step, and \(V\) its ordered \(S\)-direction list after the \(s\)-step. Ignore moves in the other exterior directions. The projected \(S\)-word is \(U,V\), a permutation of all \(k\) directions. It begins at some \(u_0\), reaches some \(u_a\) after \(U\), and ends at \(\bar u_0\) after \(V\).

On the \(U\) edges, (4) says precisely \(d\)-color 0. On the \(V\) edges, (4) says precisely that the **\(Q_S\)-antipodal image of the projected \(V\)-suffix** carries \(d\)-color 1. Therefore the projected \(Q_S\) path obtained by reversing \(U\), and then following the reverse \(Q_S\)-antipodal image of \(V\),
\[
u_a\xrightarrow{U^{\mathrm{rev}}}u_0
\xrightarrow{\overline{V}^{\,\mathrm{rev}}}\bar u_a,
\tag{6}
\]
uses every \(S\) direction precisely once and changes \(d\)-color **at most once**: the first block has color 0 and the second block color 1. (When one block is empty, it is monochromatic.) This is a full antipodal \(Q_k\)-geodesic. It proves \(B_k\). \(\square\)

**Additional switch-count transfer.** The forward proof works without assuming the \(d\)-geodesic has only one change. Given an arbitrary \(d\)-antipodal geodesic with \(r\ge1\) switches, choose the \(U|V\) split at **any one of its color changes**. Reversing the first block preserves its internal switch count; antipodally reversing and complementing the second block preserves its internal switch count; the chosen seam changes from a switch to a match. Hence the selected-direction color word on the resulting \(Q_n\) full geodesic, compared with any prescribed directionwise target \(t\), has precisely **\(r-1\)** switches. For \(r=0\), place all \(S\)-directions on one side of the exterior bridge; the selected word remains constant. Thus any upper bound on switches in arbitrary \(k\)-cube colorings transfers to a one-smaller bound for the **selected** direction word of every larger NORI1 coloring (not to the full \(n\)-edge color word, whose exterior bridge colors are uncontrolled).

#### Consequence: universal seven-direction color prescription

**Corollary 2 (all \(n\): every seven selected colors are realizable).** For every dimension \(n\ge8\), every legal antipodally odd -edge coloring of \(Q_n\), every set \(S\subseteq[n]\) of size \(k\le7\), and every prescribed color vector \(t\in\mathbb F_2^S\), there exists a **full \(n\)-edge antipodal geodesic** whose \(k\) selected edges have **precisely** the specified colors.

**Proof.** The geodesic Norine conjecture \(A_m\) has been established for **every \(m\le8\)**, including the SAT-certified case \(m=8\) in Kirchweger–Peitl–Subercaseaux–Szeider (2025), *From the Finite to the Infinite: Sharper Asymptotic Bounds on Norin's Conjecture via SAT*, arXiv:2511.08386, Theorem 1 (the paper explicitly states the *geodesic* conjecture in dimension eight). Leader and Long (2014), *Long geodesics in subgraphs of the cube*, Proposition 3.6 in arXiv:1301.2195v1, proved \(A_{k+1}\Rightarrow B_k\). Thus \(B_k\) holds for \(k\le7\). Theorem 1 above then gives \(P_{n,S}\) for every \(n>k\), as required. \(\square\)

For \(n\le8\), the stronger statement that **all \(n\) prescribed direction colors** can be realized also follows directly from the established full-geodesic result \(A_n\): independently XOR the desired \(t_i\) into each direction's edge color, preserving undirectedness and oddness, then use \(A_n\). Consequently, for **every** \(n\ge2\), arbitrary prescribed colors on any set of size \(\min(n,7)\) are simultaneously attainable, and in dimensions at most eight all \(n\) colors are attainable.

**Boundary of the result.** This uses a previously proved finite-dimensional geodesic theorem and an  new dimension-free bridge implication. It is not a proof of the full NORI1 conjecture in arbitrary dimension; for eight selected directions in \(n\ge9\), the bridge equivalence reduces the question **precisely** to \(B_8\), equivalently to the known Leader–Long dimensional challenge \(A_9\Rightarrow B_8\) in one direction. The argument makes no claim about *ordinary boundary 3-tournaments*: it uses an edge (one-window) color seam, whereas ordered-three-face paths acquire two extra seam windows.

**Primary sources and scope checks.**
- Imre Leader and Eoin Long, *Long geodesics in subgraphs of the cube*, Discrete Mathematics 326 (2014), 29–33; https://arxiv.org/abs/1301.2195 .
- Markus Kirchweger, Tomáš Peitl, Bernardo Subercaseaux, Stefan Szeider, *From the Finite to the Infinite: Sharper Asymptotic Bounds on Norin's Conjecture via SAT* (2025), arXiv:2511.08386, specifically Theorem 1 and the separate SAT geodesic encoding \(\Psi_n\); https://arxiv.org/html/2511.08386 .
- Tomáš Feder and Carlos Subi, *On hypercube labellings and antipodal monochromatic paths*, Discrete Applied Mathematics 161 (2013), 1421–1426 (original unrestricted-edge 2-cp *path* conjecture; the geodesic strengthening is due to Leader–Long).

**Unification scope:** This established NORI1 localization theorem is retained as prior mathematics, not an independent current research target. A later NORI1 paired-start toy theorem, originally published in composition v2, is preserved with its complete proof in note `note_antipodal_paired_start_nori1_toy_unification_probe`; no transfer to ordinary boundary tournaments has been established.


#### Near-spanning one-change paths: an unrestricted dimension-uniform closure equivalence

Let \(d\) be an arbitrary binary edge coloring of \(Q_n\), with **no antipodal condition**. Define \(L_1(d)\) to be the maximum length of a direction-simple path (using each direction at most once) whose edge-color word has at most one change. The full-length condition \(L_1(d)=n\) is exactly the arbitrary-color geodesic two-color-path assertion \(B_n\).

**Theorem (asymptotic one-change closure equivalence).** The following assertions are equivalent:

1. Unrestricted antipodally odd NORI1 holds in every dimension.
2. \(B_n\) holds for arbitrary two-edge-colorings of \(Q_n\), for every dimension \(n\).
3. A uniform function \(f(n)=o(n)\) exists such that every arbitrary coloring \(d\) of \(Q_n\) satisfies
   \[
   \boxed{L_1(d)\ge n-f(n).}\tag{NS1}
   \]
4. Some fixed \(C\) exists such that every arbitrary coloring \(d\) of \(Q_n\) satisfies \(L_1(d)\ge n-C\).

Thus a universal \(n-O(\sqrt n)\), \(n-O(\log n)\), or bounded-deficit **one-change** direction-simple path theorem for arbitrary two-edge-colorings would prove NORI1 in every dimension.

*Proof.* To obtain \(1\Rightarrow2\), fix an arbitrary colored \(Q_k\). The already established multifacet bridge theorem gives \(B_k\Longleftrightarrow P_{k+1,S}\), where \(S\) is the \(k\)-set of horizontal directions in a legal antipodally odd coloring of \(Q_{k+1}\). Under NORI1, every directionwise prescribed \(k+1\)-bit profile occurs: reverse all edge colors in each selected direction wherever the target bit is one, apply NORI1, then if necessary antipodally translate a monochromatic-one full path to a monochromatic-zero path. Hence \(P_{k+1,S}\) holds, and the bridge theorem yields \(B_k\).

For \(2\Rightarrow1\), apply \(B_n\) directly to a legal antipodally odd edge coloring of \(Q_n\). This gives a full antipodal geodesic with at most one color change. If it has one change, cyclically slide the root past that change. Antipodal oddness complements the moved prefix colors and makes the resulting full antipodal geodesic monochromatic, as proved in the penultimate-length/root-rotation lemma above. Thus NORI1 holds.

Clearly 2 implies 3 and 4. Conversely, if 2 fails, select a fixed arbitrary colored \(Q_d\) with \(L_1(a)\le d-1\). Form its \(h\)-fold independent Cartesian power \(a^{\boxtimes h}\) on \(Q_{hd}\). A direction-simple path with at most one change in this product projects onto each factor as a direction-simple path whose color word, being a subsequence of the full word, also has at most one change. Each factor therefore contributes at most \(d-1\) moves. Consequently
\[
\boxed{L_1(a^{\boxtimes h})\le h(d-1)=hd-h.}\tag{NS2}
\]
The loss of \(h=n/d\) moves is linear in the ambient dimension \(n=hd\), violating 3 and 4. Therefore either 3 or 4 forces 2. This proves all equivalences. \(\square\)

**Significance and calibration.** This closure-equivalent asymptotic assertion concerns **arbitrary**, potentially imbalanced, nonlinear two-edge-colorings of the cube. The requirement of at most one color change is indispensable: uniformly near-spanning *monochromatic* direction-simple paths are impossible for arbitrary colorings with half the directions permanently assigned to each color. Conversely, the full geodesic 2-cp assertion is sufficient for NORI1 because antipodal root rotation eliminates a single change. The tensor-power argument shows that any genuinely sublinear loss in the weaker partial-path statement automatically collapses to the exact full geodesic theorem. This is a possible approach through an approximate path theorem rather than an induction through individual dimensions.



##### Two-phase trace tensorization and multiplicative counterexamples

For any arbitrary undirected binary edge coloring \(d\) of \(Q_q\), let \(R_d\) and \(B_d\) be its color-zero and color-one adjacency matrices, \(P_q\) the antipodal permutation, and define the nonnegative numbers
\[
M_{q,k}(d)=\operatorname{tr}(P_qR_d^kB_d^{q-k}),
\qquad 0\le k\le q.
\tag{TS1}
\]
The Leader--Long full one-change property holds for \(d\) if and only if some \(M_{q,k}(d)\) is positive, because every full path changing from one to zero can be reversed.

**Theorem (binomial two-phase tensorization).** If \(d=d_1\boxtimes d_2\) is an independent Cartesian product of arbitrary binary edge colorings on \(Q_a,Q_b\), with \(N=a+b\), then
\[
\boxed{
M_{N,k}(d)=
\sum_{r=\max(0,k-b)}^{\min(a,k)}
\binom{k}{r}\binom{N-k}{a-r}
M_{a,r}(d_1)M_{b,k-r}(d_2).
}\tag{TS2}
\]
Thus a product coloring admits a full one-change antipodal geodesic if and only if *both* factors admit such geodesics.

*Proof.* The product matrices satisfy
\[
R_d=R_1\otimes I+I\otimes R_2,\quad
B_d=B_1\otimes I+I\otimes B_2,\quad P_N=P_a\otimes P_b.
\]
Expand both powers binomially; their respective factor summands commute because they act on disjoint coordinates. A term has nonzero antipodal trace in a factor only if its total number of moves in that factor is at least the factor's dimension. Since the total number of moves is exactly \(N=a+b\), each factor must use precisely its own dimension, giving \(r+(a-r)=a\) and \(k-r+(b-k+r)=b\), whence (TS2). Every summand is nonnegative. If both factors have positive mixed traces at seam ranks \(r_1,r_2\), take \(k=r_1+r_2\); the associated binomial coefficient product is strictly positive. Conversely a positive summand implies both factors have a one-change geodesic. \(\square\)

**Corollary (exact multiplicativity of failure).** A fixed arbitrary-color \(B_d\) counterexample generates full one-change geodesic counterexamples in every product dimension \(hd\). The amplification is stronger at the partial-path level: every one-change direction-simple path in the \(h\)-fold product misses at least \(h\) directions, by (NS2). If the original coloring is antipodally odd then all its seam counts are equal by the separate uniform-seam identity (SM1) in the matrix Subsection, and Vandermonde's identity reduces (TS2) to the previously proved monochromatic-trace tensorization.

This exhibits two complementary, exact closure obstructions: multiplicativity of the zero/nonzero full-geodesic two-phase trace, and additivity of the deficit for its partial-path relaxation.



##### Exact invariance of the full-path minimum switch number under Cartesian powers

For an arbitrary binary edge coloring \(d\) of \(Q_q\), write \(\mu(d)\) for the minimum number of edge-color changes among full antipodal geodesics of \(Q_q\). Retain \(L_1(d)\), the largest length of a direction-simple path with at most one color change.

**Theorem (switch-minimum product invariance).** For every arbitrary binary edge coloring \(d\) and every \(h\ge1\),
\[
\boxed{\mu(d^{\boxtimes h})=\mu(d).}\tag{SP1}
\]
More generally, if \(d_1,\ldots,d_h\) are distinct independent factors, then
\[
\boxed{\mu(d_1\boxtimes\cdots\boxtimes d_h)\ge\max_j\mu(d_j).}\tag{SP2}
\]

*Proof.* A full product geodesic uses each direction exactly once. Deleting from its direction order all moves outside a given factor leaves a full antipodal geodesic of that factor. Its positional color word is a subsequence of the product path's word, so its number of switches cannot exceed that of the product. Minimizing proves (SP2) and the lower bound in (SP1).

For the upper bound in (SP1), choose a full factor geodesic whose color word has precisely \(s=\mu(d)\) changes, giving \(s+1\) successive monochromatic runs. In each of the \(h\) independent copies choose the identical geodesic with the identical color sequence. Interleave the direction words **run by run**: first traverse the first run of each copy, then the second run of each copy, and so forth. Independence of factors makes this a full product geodesic, and its concatenated color word has the same \(s\) switches. Hence \(\mu(d^{\boxtimes h})\le s\), completing the proof. \(\square\)

**Counterexample-amplification dichotomy.** If an arbitrary-color one-change counterexample \(d\) exists in dimension \(q\), then \(\mu(d)=s\ge2\). For every \(h\),
\[
\boxed{
\mu(d^{\boxtimes h})=s,\qquad
hq-L_1(d^{\boxtimes h})\ge h.
}\tag{SP3}
\]
The first equality is (SP1); the second follows from (NS2). Thus the identical Cartesian powers simultaneously have a **bounded** number of unavoidable full-geodesic color changes and a **linear** deficit in their longest one-change partial geodesic.

**Consequence for approximate proof strategies.** Any dimension-uniform bound of the form
\[
\boxed{n-L_1(d)\le g(\mu(d))}
\tag{SP4}
\]
with finite \(g(s)\) independent of \(n\), if proved for all arbitrary binary cube edge colorings, would imply the entire Leader--Long one-change geodesic conjecture and hence unrestricted NORI1. Indeed a hypothetical counterexample and its powers violate (SP4) by (SP3). Conversely if the grand conjecture holds, the left side vanishes. Therefore (SP4) is itself grand-theorem equivalent, regardless of how rapidly \(g\) grows.

In particular, an \(O(\sqrt n)\) full-geodesic switch bound, such as the theorem of Hollom (2026), does not **by itself** entail an \(n-o(n)\) one-change partial-path bound through a generic compression inequality depending only on the number of switches. Such a compression theorem would need to exclude the tensor-power obstruction using additional global structure, or equivalently settle the conjecture.



##### Dual approximation from above: shortest one-change antipodal paths

For arbitrary two-edge-colorings \(d\) of \(Q_n\), define \(\ell_1(d)\in\{n,n+2,n+4,\ldots\}\cup\{\infty\}\) to be the minimum length of an antipodal path with at most one edge-color change; assign \(\infty\) if no such path exists. The color word may consist of one or two monochromatic runs. The conjectured full one-change geodesic is equivalent to \(\ell_1(d)=n\), since any antipodal path of length \(n\) is a full geodesic.

**Theorem (shortest one-change antipodal path tensorization).** For every arbitrary edge coloring \(d\) and \(h\ge1\),
\[
\boxed{\ell_1(d^{\boxtimes h})=h\,\ell_1(d),}\tag{AP1}
\]
with the convention \(h\infty=\infty\). Hence unrestricted NORI1 is equivalent to the following *approximation from above*: there exists a uniform function \(f(n)=o(n)\) such that every arbitrary two-edge-coloring of \(Q_n\) admits an antipodal path of at most one color change and length at most \(n+f(n)\). The analogous assertion with \(f(n)=C\), a fixed constant, is also equivalent.

*Proof.* Let \(P\) be a one-change antipodal walk in the product \(Q_{hd}\). Its projection to each \(d\)-dimensional factor is an antipodal walk whose color word is a subsequence of the word of \(P\), and so has at most one change. Erasing any closed subwalk preserves its endpoints and cannot increase the number of color changes, since deletion of a contiguous block from a binary word does not increase its number of changes. Thus each factor projection has at least \(\ell_1(d)\) steps, giving \(|P|\ge h\ell_1(d)\). If \(\ell_1(d)=\infty\), this proves the product likewise admits no one-change antipodal path.

Conversely, choose a shortest one-change antipodal path \(P_d\) in \(Q_d\), with color word \(0^a1^b\) after optional reversal and color renaming (either run may be empty). In all \(h\) factors follow its first monochromatic run, sequentially, then follow its second monochromatic run in all factors, sequentially. This is a simple antipodal path of the product: at every step at least one factor advances along its own simple path, and factor progress is monotone. It has \(h(a+b)=h\ell_1(d)\) edges and at most one change, proving the reverse inequality and (AP1).

If NORI1 holds, then by the earlier exact equivalence the arbitrary-color one-change full geodesic theorem holds, so \(\ell_1(d)=n\) for every \(d\), establishing either asymptotic assertion. Conversely suppose an arbitrary-color \(B_d\) counterexample exists. Either \(\ell_1(d)=\infty\), violating the bound immediately, or parity of antipodal path lengths forces \(\ell_1(d)\ge d+2\). By (AP1), its \(h\)-fold power has \(\ell_1(d^{\boxtimes h})\ge h(d+2)=hd+2h\), giving a fixed positive fractional excess \(2/d\) along dimensions \(hd\), contrary to any uniform \(f(n)=o(n)\) or fixed \(C\). By the already established all-dimensional equivalence of \(B_d\) and NORI1, the assertion follows. \(\square\)

**Two-sided near-geodesic closure targets.** The dimension-uniform NORI1 problem is now equivalently expressible by either of two sublinear approximations to a one-change geodesic for *arbitrary* two-edge-colorings:

- **From below:** a direction-simple path with at most one change of length \(n-o(n)\), by (NS1).
- **From above:** an antipodal path with at most one change of length \(n+o(n)\), by (AP1).

Both implications back to full closure are proved by Cartesian-power amplification. The second formulation asks for quantitative near-geodesicity inside the original Feder--Subi one-change antipodal *path* problem, which remains stronger than the settled unrestricted original Norine monochromatic-antipodal-*path* result. In particular the known existence of a monochromatic antipodal path for odd colorings does not establish (AP1)'s approximating hypothesis for arbitrary colorings. These statements provide global proof targets rather than independent proofs of their hypotheses.


#### Strict half-switch and four-direction prescription

### Strict half-switch bound and four-direction prescription

Let d be an arbitrary two-coloring of undirected edges of Q_n. Write r(v), b(v)=n-r(v) for its incident color degrees, and s(P) for the number of color changes on a full antipodal geodesic.

**Lemma.** For a uniformly random root and full direction order,
\[
\mathbb E\,s(P)=\frac{2}{n2^n}\sum_{v\in Q_n}r(v)b(v)
\le \frac2n\left\lfloor\frac{n^2}4\right\rfloor.
\tag{1}
\]
*Proof.* At each of the n-1 intermediate vertices the ordered pair of successive distinct directions is uniform among n(n-1) pairs, and the vertex is uniform over Q_n. At v precisely 2r(v)b(v) of the ordered direction pairs switch color. Summing their probabilities proves (1). \(\square\)

**Theorem (strict half-switch).** For every even n=2h>=4, any arbitrary coloring of Q_n has a full antipodal geodesic with at most h-1 color changes. For odd n, (1) guarantees at most (n-1)/2.

*Proof.* The odd-dimensional claim follows by the integer-valued switch count. When n=2h>=4, (1) gives expectation at most h. If all full geodesics had at least h switches, then all of them would have precisely h. For every vertex x and two distinct directions i,j, start a full path at x with first direction i and last direction j. Parity of its h switches implies
\[
d_i(x)+d_j(\bar x)=h\bmod2.
\tag{2}
\]
For any distinct i,k choose j outside {i,k}; (2) gives d_i(x)=d_k(x). Every vertex therefore has a monochromatic star, hence by connectivity the entire coloring is constant. It then has zero-switch full paths, contradicting h>=2. \(\square\)

**Corollary (arbitrary-color four-cube).** Every arbitrary red-blue edge coloring of Q4 has a full antipodal geodesic with at most one switch, without any antipodal relation. Independently, a binary integer feasibility program on the 32 Q4 edges, excluding eight one-switch color words on each of its 192 unoriented full antipodal geodesics, was infeasible under SciPy/HiGHS. The proof does not rely on that audit.

**Theorem (unrestricted four-direction NORI1 prescription).** Let n>=4 and c be any binary undirected-edge coloring of Q_n obeying c_i(x+e_i)=c_i(x), c_i(bar x)=1+c_i(x). For any four distinct directions S and desired t in F2^S, some full antipodal geodesic has direction-indexed colors t on S.

*Proof.* For n>4, apply the previously proved multifacet bridge equivalence B_k iff P_(n,S) in this subsection at k=4. In brief, on a lower S-face recolor each direction i by t_i, take its zero-then-one one-switch full path, reverse the zero prefix, traverse all exterior directions to the opposite face, and traverse the reversal of the antipodal image of the one suffix. This is a full geodesic whose S-edges have colors t_i.

For n=4, directionwise recolor by t_i and use the preceding four-cube corollary to obtain a path from u to bar u with red prefix U and blue suffix V. Starting at the switch vertex, reverse U and then reverse the antipodal image of V. Antipodal oddness makes both parts red; they traverse complementary direction subsets and join antipodal endpoints. Undo the recoloring to obtain prescribed profile t. \(\square\)

The four-direction theorem strengthens the previous three-direction prescription for all legal NORI1 colorings. The small-dimensional one-switch statement is known in the literature; the displayed argument gives an elementary proof. The general switch bound does not settle the arbitrary-color one-switch problem beyond dimension four.

#### Passive lift profile factorization and active completion

### Passive lift profile factorization and four-direction-assisted active completion

Let c be any binary undirected-edge coloring of Q_n satisfying c_i(x+e_i)=c_i(x) and c_i(bar x)=1+c_i(x). For any such coloring write W(c) for its set of direction-indexed color profiles of rooted, ordered full antipodal geodesics.

**Theorem 1 (passive paired lift has a product profile support).** Define the conventional paired lift on Q_(2n) by
\[
\widetilde c_i(x,y)=c_i(x),\qquad
\widetilde c_{n+i}(x,y)=1+c_i(x)\quad(1\le i\le n).
\tag{PC1}
\]
Then
\[
\boxed{W(\widetilde c)=W(c)\times\mathbb F_2^n.}\tag{PC2}
\]
The paired lift is legal and antipodally odd, and contains a monochromatic full antipodal geodesic if and only if c does.

*Proof.* Project any full geodesic of the lift to the first n vertex bits and delete the y-steps. The remaining path is a full antipodal geodesic in c with the same old-direction profile, proving the upper containment in (PC2). Conversely, select any full base geodesic starting at x, with direction order pi and old profile u. Given any desired dummy-direction word v, place dummy direction n+i before all old directions if v_i=1+c_i(x), and after all old directions otherwise. Before the base path its dummy color is 1+c_i(x); after the base path, at bar x, its dummy color is c_i(x). Thus its dummy word is v and its old word is u. The starting dummy bits are arbitrary, establishing the product support. Monochromaticity equivalence follows by taking zero targets and by the projection. \(\square\)

**Lemma 2 (one-helper rigidity).** Suppose C is any legal antipodally odd coloring of Q_(n+1) whose old-direction coloring on the face y=0 is c. Then for every old direction i and x,
\[
\boxed{C_i(x,1)=c_i(x)=C_i(x,0).}\tag{PC3}
\]
*Proof.* The global antipode sends (x,1) to (bar x,0), so C_i(x,1)=1+C_i(bar x,0)=1+c_i(bar x)=c_i(x). \(\square\)

**Theorem 3 (universal active completion with n-3 helpers).** Let n>=4 and c be any legal antipodally odd coloring of Q_n. Fix any four-element direction subset S, put T=[n]\setminus S, and choose s in S. Introduce auxiliary bits y_* and y_i for i in T, in total m=1+|T|=n-3 additional cube directions. Define C on Q_(n+m) by
\[
C_i(x,y)=
\begin{cases}
c_i(x),&i\in S,\\
c_i(x)+y_i+y_*,&i\in T,
\end{cases}
\qquad
C_{y_j}(x,y)=x_s\quad(j\in T\cup\{*\}).
\tag{PC4}
\]
Then C is legal and antipodally odd, its restriction to the face y=0 in old directions agrees with c, and
\[
\boxed{W(C)=\mathbb F_2^{n+m}=\mathbb F_2^{2n-3}.}\tag{PC5}
\]
Every target profile is attained using an order in which one selected set of auxiliary directions comes before all original directions, with the remaining auxiliary directions after them.

*Proof.* Each old-direction rule ignores its own original bit; each auxiliary rule x_s ignores its own auxiliary bit. Under the global antipode, c_i flips, the even expressions y_i+y_* do not flip, and x_s flips. Hence C is legal and odd, and at y=0 the old rules equal c.

Fix any target full profile (w,v), with old word w in F2^n and auxiliary word v in F2^m. By the universal four-direction prescription theorem in the previous subsection development, choose a full old-direction geodesic from some x in some order pi whose colors agree with w on S. Let d_i be its old profile for i in T. Define b=x_s. Place auxiliary direction y_j before the entire old geodesic if v_j=b, and after it if v_j=1+b. These helper edges then have precisely their prescribed colors, because the s-th old bit changes from b to 1+b during the old full path.

Let E_j indicate whether helper direction j is in the early group. Choose the auxiliary bit values y_j^{mid} during the old geodesic so that y_*^{mid}=0 and y_i^{mid}=d_i+w_i for i in T. Take the initial auxiliary root values y_j^{start}=y_j^{mid}+E_j. After the early helper moves, the helper values equal the prescribed mid values; they remain fixed throughout the old-direction segment. For every i in T, its color along that segment is c_i+ y_i^{mid}+y_*^{mid}=d_i+(d_i+w_i)=w_i; for i in S, its color is w_i by selection of the base path. The remaining auxiliary moves have color v_j. Every old and auxiliary direction is used once. Thus the target profile is attained. \(\square\)

**Lemma 4 (helper information-capacity bound for frozen-state control).** If a Boolean control map H:F2^m->F2^t obeys H(y+\mathbf1)=H(y), then its image contains at most 2^(m-1) elements. Surjectivity onto F2^t therefore requires m>=t+1. The control map H(y)=(y_i+y_*)_(i in T) used in (PC4), with t=|T|=n-4 and m=t+1, attains this information bound.

*Proof.* An antipodally even H factors through the quotient of F2^m by the two-element subgroup generated by the all-one vector, whose cardinality is 2^(m-1). The displayed H maps onto F2^t by choosing y_*=0 and the y_i independently. \(\square\)

**Computer audit.** For n=4,5,6, four random legal odd base colorings per dimension were tested against 250 independently random full-profile targets, using a brute-force four-direction base witness finder and the construction from Theorem 3. All 3000 targets were attained, and legality was tested separately. The paired-lift factorization (PC2) was checked by full root/order enumeration for four random base colorings in each of dimensions n=2 and n=3.

**Scope.** These statements apply to every legal odd base coloring, regardless of nonlinear dependencies. The passive factorization shows why adding directions that never influence the original color rules cannot erase a missing profile. The active completion supplies enough independent antipodally even phase controls to remove all remaining profile constraints after a four-direction base witness. Since it changes the old-direction rules outside y=0, it is not a counterexample-preserving reduction and does not prove NORI1 in dimension n.

##### Seven-direction-assisted control reduction

**Theorem 5 (seven-prescription assisted completion).** Let n>=9 and let c be any legal antipodally odd coloring of Q_n. Choose a set S of seven original directions and write T=[n]\S. Add m=|T|+1=n-6 auxiliary bits, one bit y_i for each i in T and one reference bit y_*. Choose s in S. Define
\[
C_i(x,y)=c_i(x)\ (i\in S),\qquad
C_i(x,y)=c_i(x)+y_i+y_*\ (i\in T),\qquad
C_{y_j}(x,y)=x_s\ (j\in T\cup\{*\}).
\tag{PC6}
\]
Then C is legal and odd, agrees with c on the all-zero auxiliary face, and has every direction-indexed full-geodesic color profile in F2^(2n-6). The number n-6 supersedes the weaker n-3 helper bound from Theorem 3 above, which used only four-direction prescription.

*Proof.* The preexisting universal seven-direction prescription theorem in this subsection follows from the established monochromatic geodesic theorem in Q8 (Kirchweger, Peitl, Subercaseaux and Szeider, 2025) and the multifacet bridge. For a desired original word w, choose a full base geodesic with prescribed colors w on S. As in Theorem 3, place each helper before or after the base full path depending on its desired color and the starting s-th bit. With the helper-state reference value y_* chosen as zero during the old-direction segment, set each auxiliary mid-state bit y_i equal to the discrepancy between c_i along the chosen base path and the target w_i. The auxiliary starts are obtained by undoing the designated early flips. All original and auxiliary target colors follow as in Theorem 3. The two legality identities hold because each phase term y_i+y_* is antipodally even and each auxiliary edge color x_s is odd under antipodality. \(\square\)

The general form is a profile-completion principle: if k designated original directions can be assigned arbitrary colors by a full base geodesic, then n-k+1 antipodally paired phase-control helpers suffice to make every profile realizable in a face-preserving extension, for k<n. The antipodally even phase map uses its 2^(n-k) possible relative helper states fully, attaining the information-capacity limit for independent correction of the remaining n-k edge colors during one frozen helper-state segment.

This is an active extension, not a counterexample-preserving lift. The project already had seven-direction prescription before the present note; that previously known theorem supplies the improved helper budget.

#### Sharp one-helper passivity and two-helper universal profile completion

#### Sharp one-helper passivity and two-helper universal profile completion

Let n>=2 and let c be any legal antipodally odd binary undirected-edge coloring of Q_n, so c_i(x+e_i)=c_i(x) and c_i(bar x)=1+c_i(x). Write W(c) for the set of direction-indexed binary profiles of full antipodal geodesics.

**Theorem 1 (one-helper extension factorization).** Let C be any legal odd coloring of Q_(n+1), with one new bit z, such that C_i(x,0)=c_i(x) for all original directions i. Then necessarily
\[
C_i(x,z)=c_i(x)\quad\text{for both }z\in F_2,
\tag{EH1}
\]
and
\[
\boxed{W(C)=W(c)\times F_2.}\tag{EH2}
\]
*Proof.* Oddness gives C_i(x,1)=1+C_i(bar x,0)=1+c_i(bar x)=c_i(x). The new-direction edge has rule C_z(x,z)=d(x), independent of z; global oddness forces d(bar x)=1+d(x). Projection of any full extension geodesic onto original directions gives a full base geodesic, proving inclusion in W(c) times F2. Conversely, choose a base geodesic realizing w from root x. Put the new-direction step before all original steps if the desired z-color equals d(x), and after all original steps otherwise. At the latter position its color is d(bar x)=1+d(x). The original profile remains w in either placement. This proves (EH2). \(\square\)

**Theorem 2 (two-helper universal full-profile completion).** Every legal odd coloring c of Q_n, n>=2, admits a legal odd extension C to Q_(n+2), agreeing with c on the auxiliary face (u,v)=00, for which
\[
\boxed{W(C)=F_2^{n+2}.}\tag{EH3}
\]
Such an extension may be defined explicitly by
\[
b_i(x)=x_{i+1\bmod n},\qquad
C_i(x,u,v)=
\begin{cases}
c_i(x),&u=v,\\
b_i(x),&u\ne v,
\end{cases}\ (0\le i<n),
\tag{EH4}
\]
\[
\boxed{C_u(x,u,v)=v,\qquad C_v(x,u,v)=x_0.}\tag{EH5}
\]
For any prescribed target profile, the resulting witness starts in the original auxiliary face 00 and uses just one of the two guard-direction arrangements u, old steps, v or v, old steps, u.

*Proof.* In (EH4), c_i and b_i each ignore their own x_i and are odd under global x complementation; the equality predicate u=v is unchanged when u,v are both flipped. The rule C_u=v ignores u and flips under global antipodality; C_v=x_0 ignores v and flips under global antipodality. Thus C is legal and odd, and agrees with c on the 00 face.

Prescribe an old-direction word w=(w_0,...,w_(n-1)) and new-direction bits (p,q)=(w_u,w_v). Put
\[
\boxed{x_0=1+p+q.}\tag{EH6}
\]
Consider the cyclic-reader coloring b on Q_n. Given any direction permutation pi, its profile equations are
\[
w_i=x_{i+1\bmod n}+[\ i+1\bmod n\text{ appears before }i\text{ in }\pi\ ].
\tag{EH7}
\]
These determine one root x for every pi,w. Choosing pi=(n-1,0,1,...,n-2) gives x_0=w_(n-1), while choosing pi=(0,1,...,n-1) gives x_0=1+w_(n-1). Since n>=2, the two lists are valid, and one of them produces the desired x_0 from (EH6).

Start C at (x,0,0). If p=0, take the complete direction order (u,pi,v). The first new step has color C_u=0, then the original steps are on the face (u,v)=(1,0), where their colors are b and yield w; finally v is used at original endpoint bar x, giving color C_v(bar x,1,0)=1+x_0=q. If p=1, use the order (v,pi,u). Its first new edge has color C_v(x,0,0)=x_0=q; the old steps occur at auxiliary state (0,1), again giving w; the last u-edge has color C_u=1=p. In both cases the path traverses all n+2 directions once, terminates at (bar x,1,1), and realizes (w,p,q). \(\square\)

**Corollary 3 (two auxiliary bits suffice without a partial-prescription theorem).** The active-completion construction in the same subsection that used n-6 helper bits based on the known seven-direction prescription is superseded as an upper bound on the number of helpers: a pair of helpers suffices for all n>=2. In contrast, one-helper extensions have the product property (EH2) and cannot create missing original-direction profiles. In particular, a face-preserving full-profile extension theorem by itself supplies no information about whether W(c) contains a given profile, since (EH3) holds for every legal base c independently of its profile support.

**Finite audit.** The constructive witness formulas were checked against independently generated legal odd base edge colorings for dimensions n=2,3,4,5,6. All 2^(n+2) target profiles were tested for n=2,3,4,5, and 200 sampled targets for n=6, including verification of the returned rooted geodesic endpoint and all edge colors. The dimension-uniform proof does not rely on this enumeration.

**Scope.** The construction requires adding dimensions and modifies old-direction edge colors on auxiliary faces with u different from v. Consequently it is not a counterexample-preserving lift and does not settle unrestricted NORI1. The primary conclusion is a sharp distinction between passive one-helper extensions and programmable two-helper extensions.

##### Factorial witness lower bound for two-helper completion

**Corollary 4 (uniform factorial witness multiplicity).** For the two-helper extension C in (EH4)-(EH5), every prescribed profile in F2^(n+2) is attained by at least n! rooted, ordered full antipodal geodesics.

*Proof.* Fix a target (w,p,q). Among all n! permutations pi, half place original direction 0 before direction n-1 and half place it after. Equation (EH7) then determines x_0 as one of the two values w_(n-1) or 1+w_(n-1), respectively. Hence n!/2 direction permutations give the root parity (EH6), and each determines a full geodesic starting on the 00 auxiliary face with the target profile. Reversing these paths gives another n!/2 rooted full geodesics starting on the 11 auxiliary face, with unchanged direction-indexed colors. These two classes are disjoint by starting auxiliary state, yielding n! witnesses. \(\square\)

The result counts rooted, ordered paths. In the absence of any assumptions on c it supplies a uniform positive lower bound for every profile of the extension.

### Penultimate-length extension and parallel-face endpoint exclusion

Let \(n\ge3\). Color the undirected edges of \(Q_n\) by \(c:E(Q_n)\to\{0,1\}\), where \(c(\bar e)=1-c(e)\). Write \(x^i\) for the vertex obtained by flipping coordinate \(i\), and \(x^{ij}=(x^i)^j\). For a nonempty geodesic \(P\), let \(\sigma(P)\) be its number of edge-color changes.

**Lemma 1 (penultimate-length parity).** Let \(P\) be an \((n-1)\)-edge geodesic from \(u\) to \(v\), missing direction \(d\), with initial color \(s\), final color \(t\), and \(r=\sigma(P)\). If \(r\) is even, precisely one of the two \(d\)-edge extensions preserves \(r\) changes. If \(r\) is odd, either both preserve \(r\), or both introduce one additional change. For odd \(r\), preservation occurs if and only if \(c(uu^d)=s\).

*Proof.* Since \(v=\bar u^d\), the unused \(d\)-edges at \(u,v\) are antipodal, with colors \(a,1-a\), where \(a=c(uu^d)\). Prepending the edge at \(u\) introduces \([a\ne s]\) changes, while appending the edge at \(v\) introduces \([1-a\ne t]\) changes. Since \(t=s\oplus(r\bmod2)\), these indicators are complementary for even \(r\) and equal for odd \(r\). In particular, a monochromatic penultimate geodesic extends monochromatically. \(\square\)

**Lemma 2 (odd-change rotation).** If a full antipodal geodesic has an odd number \(r\) of color changes, there exists a full antipodal geodesic with \(r-1\) changes. Consequently, the minimum number \(\mu(c)\) of changes among full antipodal geodesics is even. In particular, the existence of a full geodesic with at most one change implies a monochromatic full geodesic.

*Proof.* Let the full geodesic have color word \(w_1,\ldots,w_n\), with \(r\) odd. Choose any change position \(k\), so \(w_k\ne w_{k+1}\). Cyclically move its first \(k\) coordinate directions to the end, using the vertex reached after those directions as the new root. The resulting full antipodal geodesic has color word
\[
(w_{k+1},\ldots,w_n,1-w_1,\ldots,1-w_k).
\]
Its internal changes within the two displayed blocks number \(r-1\). Since \(r\) is odd, \(w_n=1-w_1\), so the new join introduces no change. Thus its total is \(r-1\). A minimum over all full geodesics cannot be positive and odd. \(\square\)

**Theorem 3 (color-change-preserving completion across parallel faces).** Let \(F\) be an \((n-2)\)-face with fixed coordinates \(a,b\). Suppose a monochromatic geodesic \(P\) spans \(F\) and terminates at \(x\in F\). Then either a monochromatic full antipodal geodesic exists, or the following holds simultaneously for both adjacent faces: every geodesic \(Q\) spanning \(F^a\) and terminating at \(x^a\), or spanning \(F^b\) and terminating at \(x^b\), extends by two edges to a full antipodal geodesic \(R\) satisfying \(\sigma(R)=\sigma(Q)\).

*Proof.* Let \(s\) be the color of \(P\), and assume that no monochromatic full antipodal geodesic exists. By Lemma 1, no monochromatic \((n-1)\)-edge geodesic exists. Appending either \(a\)- or \(b\)-edge at \(x\) to \(P\) therefore forces
\[
c(xx^a)=c(xx^b)=1-s. \tag{1}
\]
The antipodal image of \(P\) spans \(F^{ab}\) and has color \(1-s\). It has \(x^{ab}\) as an endpoint: the other endpoint of \(P\) is \(x^{[n]\setminus\{a,b\}}\), whose antipode is \(x^{ab}\). Applying the same penultimate argument at \(x^{ab}\) yields
\[
c(x^{ab}x^a)=c(x^{ab}x^b)=s. \tag{2}
\]
Let \(Q\) span \(F^a\) and end at \(x^a\), with final color \(t\). If \(t=1-s\), append the route \(x^a,x,x^b\), whose two edges both have color \(t\) by (1). If \(t=s\), append \(x^a,x^{ab},x^b\), whose two edges both have color \(t\) by (2). Each concatenation uses every coordinate once and reaches the antipode of its starting vertex. Both appended edges agree with the terminal color, so no additional change occurs. The argument for \(Q\) spanning \(F^b\) is symmetric. \(\square\)

**Corollary 4 (one-change parallel-face endpoint exclusion).** In a counterexample to the monochromatic antipodal-geodesic assertion, a monochromatic geodesic spanning \(F\) and terminating at \(x\) excludes every geodesic with at most one color change spanning \(F^a\) and terminating at \(x^a\), or spanning \(F^b\) and terminating at \(x^b\).

*Proof.* Theorem 3 would yield a full antipodal geodesic with at most one change; Lemma 2 would make it monochromatic. \(\square\)



Theorem 3 strengthens parallel-face endpoint exclusion to a monochromatic path paired with a path having one color change.

**Theorem 5 (synchronized opposite-phase switch splicing).** Let \(n\ge4\), let \(F\) be a codimension-two face with fixed coordinates \(a,b\), and put \(D=[n]\setminus\{a,b\}\). Suppose there are two geodesics spanning adjacent faces,
\[
P:\quad u\ \xrightarrow[\text{color }s]{A}\ z\
\xrightarrow[\text{color }1-s]{B}\ x
\quad\text{in }F,
\]
\[
Q:\quad u^a\ \xrightarrow[\text{color }1-s]{A}\ z^a\
\xrightarrow[\text{color }s]{B}\ x^a
\quad\text{in }F^a,
\]
where \(A,B\) are a partition of \(D\) into two nonempty direction sets. The paths may traverse directions within \(A\) and within \(B\) in different orders. All edges within each displayed block have the displayed color. Then the coloring has a monochromatic full antipodal geodesic.

*Proof.* Write \(h=c(zz^a)\).

If \(h=s\), the following two length-\((n-1)\) monochromatic geodesics of color \(s\) exist:
\[
u\ \xrightarrow{P|_A}\ z\ \xrightarrow{a}\ z^a\
\xrightarrow{Q|_B}\ x^a,
\]
and
\[
x^a\ \xrightarrow{(Q|_B)^{\rm rev}}\ z^a\
\xrightarrow{a}\ z\
\xrightarrow{(P|_A)^{\rm rev}}\ u.
\]
Both use every direction in \(D\cup\{a\}\) once. Their missing \(b\)-edges at the displayed terminal vertices are \(x^ax^{ab}\) and \(uu^b\), which are antipodal; consequently one has color \(s\). Appending it yields a monochromatic full geodesic.

If \(h=1-s\), use instead the monochromatic \((n-1)\)-edge paths of color \(1-s\)
\[
u^a\ \xrightarrow{Q|_A}\ z^a\
\xrightarrow{a}\ z\
\xrightarrow{P|_B}\ x,
\]
and its reversal
\[
x\ \xrightarrow{(P|_B)^{\rm rev}}\ z\
\xrightarrow{a}\ z^a\
\xrightarrow{(Q|_A)^{\rm rev}}\ u^a.
\]
Their terminal missing \(b\)-edges, \(xx^b\) and \(u^au^{ab}\), are antipodal, so one has color \(1-s\). Again appending that edge gives a monochromatic full antipodal geodesic. \(\square\)

**Corollary 6 (phase coherence at a matched switch).** In a counterexample to NORI1, two one-change geodesics spanning adjacent codimension-two faces, with corresponding initial vertices, change vertices, and final vertices, must have the same initial edge color (and hence the same final edge color).

*Proof.* If their initial colors differed, their monochromatic blocks would satisfy Theorem 5. \(\square\)

**Role of the hypotheses.** The paths need only have matching initial, change, and terminal vertices across the \(a\)-translation; their within-block direction orders can differ. The conclusion arises from two competing monochromatic \((n-1)\)-edge routes whose missing edges form an antipodal pair. The central unresolved configuration for this method is two aligned one-change paths with the same phase.


**Theorem 7 (monochromatic-arm interface obstruction).** Continue to assume \(c(\bar e)=1-c(e)\), and fix adjacent \((n-2)\)-faces \(F,F^a\) with remaining fixed direction \(b\). Let \(P\) span \(F\) from \(u\) to \(x\), and let \(Q\) span \(F^a\) from \(u^a\) to \(x^a\). Suppose \(w\) is an interior vertex of \(P\) for which \(w^a\) is an interior vertex of \(Q\). All path portions mentioned below are nonempty.

(i) If \(P[u,w]\) and \(Q[w^a,x^a]\) are both monochromatic in color \(s\), then either a monochromatic full antipodal geodesic exists or \(c(ww^a)=1-s\).

(ii) If \(Q[u^a,w^a]\) and \(P[w,x]\) are both monochromatic in color \(t\), then either a monochromatic full antipodal geodesic exists or \(c(ww^a)=1-t\).

In particular, if both (i) and (ii) hold at the same projected vertex with \(s\ne t\), a monochromatic full antipodal geodesic exists.

*Proof.* The coordinate supports of \(P[u,w]\) and \(Q[w^a,x^a]\) are complementary within \(D=[n]\setminus\{a,b\}\), since their projected starts and ends are \(u,x\) and \(w\) occurs along both spanning geodesics. If \(c(ww^a)=s\), concatenating \(P[u,w]\), the \(a\)-edge, and \(Q[w^a,x^a]\) gives a monochromatic geodesic of length \(n-1\), which extends by Lemma 1. Thus failure of the monochromatic full-path conclusion forces \(c(ww^a)=1-s\). The proof of (ii) uses \(Q[u^a,w^a]\), the reverse \(a\)-edge, and \(P[w,x]\). Both directions use every coordinate in \(D\cup\{a\}\) once. When \(s\ne t\), the two required values \(1-s\) and \(1-t\) for the same \(a\)-edge are incompatible. \(\square\)

**Corollary 8 (ordered-switch separator).** Suppose \(P,Q\) are as in Theorem 7, with projected coordinate orders agreeing. Their words have one change each:
\[
w(P)=s^k(1-s)^{m-k},\qquad
w(Q)=(1-s)^\ell s^{m-\ell},
\quad m=n-2,\quad 1\le k,\ell<m.
\]
Let \(z_r\) be their common projected vertex after the first \(r\) coordinate directions. If no monochromatic full antipodal geodesic exists, then:
\[
\begin{cases}
c(z_rz_r^a)=s,&k<\ell,\ k\le r\le\ell,\\
c(z_rz_r^a)=1-s,&\ell<k,\ \ell\le r\le k.
\end{cases}
\]
If \(k=\ell\), a monochromatic full geodesic necessarily exists.

*Proof.* When \(k<\ell\), at each \(r\in[k,\ell]\) the \(Q\)-prefix and \(P\)-suffix are both monochromatic of color \(1-s\). Apply Theorem 7(ii). When \(\ell<k\), at each \(r\in[\ell,k]\) the \(P\)-prefix and \(Q\)-suffix have color \(s\). Apply Theorem 7(i). If \(k=\ell\), both arm conditions hold at \(z_k\), in opposite colors. \(\square\)

**Corollary 9 (oppositely oriented switch-band intersection).** Consider two pairs \((P,Q)\) and \((P',Q')\) of adjacent-face spanning one-change geodesics as in Corollary 8, having the same initial vertex \(u\in F\) and the same initial color \(s\) on their \(F\)-paths. The paired paths within each pair have a common projected coordinate order, though the orders of the two pairs may differ. Suppose the first pair has split indices \(k<\ell\), the second has split indices \(\ell'<k'\), and there is a vertex \(w\in F\) lying on both projected chains at a rank
\[
k\le d_F(u,w)\le\ell,\qquad
\ell'\le d_F(u,w)\le k'.
\]
Then a monochromatic full antipodal geodesic exists.

*Proof.* Corollary 8 applied to the first pair requires \(c(ww^a)=s\) in the absence of a monochromatic full geodesic, while the second pair requires \(c(ww^a)=1-s\). \(\square\)

These interface conditions provide a reachability-based target: in a hypothetical counterexample, switch bands of opposite orientation and initial phase \(s\) must avoid sharing a projected vertex. This moves the problem from single-path endpoint colors to the intersection geometry of entire families of colored maximal chains; obtaining such an intersection unconditionally remains open.


#### Theorem 10 (parallel-face switch bound)

Let \(n\geq 3\), and let \(c\) be an edge coloring of \(Q_n\) satisfying \(c(\bar e)=1-c(e)\). Let \(F\) be an \((n-2)\)-face with exterior directions \(a,b\). Suppose that \(P\subseteq F\) and \(Q\subseteq F^a\) are long geodesics terminating at corresponding vertices \(x\) and \(x^a\), respectively. Write \(r=\sigma(P)\), \(s=\sigma(Q)\), and
\[
\mu(c)=\min\{\sigma(R):R\text{ is a full antipodal geodesic of }Q_n\}.
\]
Then
\[
\boxed{\mu(c)\leq\max\{r,2\lceil s/2\rceil\}.} \tag{10.1}
\]
By interchanging \(F,F^a\), one obtains
\[
\boxed{
\mu(c)\leq
\min\bigl\{\max(r,2\lceil s/2\rceil),\,
\max(s,2\lceil r/2\rceil)\bigr\}.
} \tag{10.2}
\]
In particular, \(\mu(c)\leq\max(r,s)\) unless \(r=s\) is odd, in which case \(\mu(c)\leq r+1\). When \(r\neq s\) and \(\max(r,s)\) is odd, the stronger inequality \(\mu(c)\leq\max(r,s)-1\) holds.

*Proof.* Put \(p=c(\text{last edge of }P)\) and \(q=c(\text{last edge of }Q)\), and label the four edges of the square at \(x\) by
\[
A=c(xx^a),\qquad B=c(xx^b),\qquad
C=c(x^ax^{ab}),\qquad D=c(x^bx^{ab}).
\]
As \(P\) and \(Q\) each traverse every direction other than \(a,b\) once, adjoining either of the two possible two-edge square routes gives a full antipodal geodesic. The resulting switch numbers are
\[
\begin{array}{ll}
r+[p\neq A]+[A\neq C],&
r+[p\neq B]+[B\neq D],\\
s+[q\neq A]+[A\neq B],&
s+[q\neq C]+[C\neq D].
\end{array}\tag{10.3}
\]
By Lemma 2, any full geodesic with \(t\) changes implies \(\mu(c)\leq 2\lfloor t/2\rfloor\).

Set \(M=\max\{r,2\lceil s/2\rceil\}\). If \(r\) is even and \(M\geq r+2\), either completion of \(P\) has at most \(r+2\leq M\) changes. If \(r\) is odd and \(M\geq r+1\), every completion of \(P\) has at most \(r+2\) changes; since \(r+2\) is odd, Lemma 2 yields \(\mu(c)\leq r+1\leq M\). It remains to consider \(M=r\).

First suppose \(r\) is even. If \(\mu(c)>r\), the first two completions in (10.3) must each introduce two new changes: an increase of zero produces at most \(r\) changes, and an increase of one produces \(r+1\) changes, reducible to \(r\) by Lemma 2. Therefore
\[
A=B=1-p,\qquad C=D=p.
\]
One of the two square routes completing \(Q\) has both edges in color \(q\), so it introduces no additional changes. This gives \(\mu(c)\leq s\leq 2\lceil s/2\rceil\leq r\), a contradiction.

Now suppose \(r\) is odd. Then \(2\lceil s/2\rceil\leq r-1\). If \(s\leq r-2\), either completion of \(Q\) has at most \(s+2\leq r\) changes, which by Lemma 2 gives \(\mu(c)\leq r-1\). The remaining possibility is \(s=r-1\), necessarily even. Assuming \(\mu(c)>r\), each of the two completions of \(Q\) in (10.3) must introduce two changes, since at most one new change would give at most \(r\) changes and hence at most \(r-1\) after parity reduction. Thus
\[
A=C=1-q,\qquad B=D=q.
\]
Whichever value \(p\) has, one of the two square routes completing \(P\) consists of two edges of color \(p\). The resulting full geodesic has \(r\) changes; parity reduction gives \(\mu(c)\leq r-1\), again a contradiction.

This proves (10.1). Swapping \(F\) with \(F^a\) proves (10.2), and the final claims follow because \(\mu(c)\) is even. \(\square\)

**Geometric interpretation.** The terminal square has four candidate completions, two from each face. If the two completions of one path are both forced to exceed the proposed bound, their bridge-edge colors force a low-switch completion of the other. The bound is uniform in the dimension of the cube and in both face-path switch counts.


Let \(n\ge5\), and let \(c\) color the undirected edges of \(Q_n\) with values in \(\{0,1\}\), subject to \(c(\bar e)=1-c(e)\). Write \(c_i(v)\) for the color of the edge in direction \(i\) incident with \(v\). Let \(\sigma(P)\) denote the number of color changes on a full antipodal geodesic \(P\), and put \(\mu(c)=\min_P\sigma(P)\).

For \(0\le k\le n\) set \(m(k)=\min\{k,n-k\}\) and define
\[
\lambda_n(k)=
\begin{cases}
0,&m(k)=0,\\
\dfrac{4k(n-k)(m(k)-1)}{n(n-1)(n-2)},&0<m(k)<n/2,\\
\dfrac{4k(n-k)(m(k)-2)}{n(n-1)(n-3)},&m(k)=n/2.
\end{cases}\tag{1}
\]
The last case occurs only when \(n\) is even. Set
\[
q_n=\left\lfloor\frac{n-1}{3}\right\rfloor,\qquad
\Phi_n(k)=\frac{2k(n-k)}{n-1}-\frac{q_n}{2}\lambda_n(k).\tag{2}
\]

**Theorem 1 (unrestricted exchange-averaging bound).** Every antipodally odd coloring of the edges of \(Q_n\) satisfies
\[
\boxed{\mu(c)\le
2\left\lfloor
\frac{\max_{0\le k\le n}\Phi_n(k)-1}{2}
\right\rfloor.}\tag{3}
\]
No restriction is imposed on the dependence of an edge color on the other coordinates.

**Corollary 2 (dimension ten).** Every antipodally odd edge coloring of \(Q_{10}\) has a full antipodal geodesic with at most two changes:
\[
\boxed{\mu(c)\le2\qquad(n=10).}\tag{4}
\]

**Corollary 3 (linear bound in all dimensions).** Uniformly over antipodally odd edge colorings,
\[
\mu(c)\le \frac{28\sqrt7-40}{81}\,n+O(1)
       =0.42075354\ldots\,n+O(1).\tag{5}
\]

The proof counts disagreements between incident edge colors and improves the resulting average by exchanging disjoint pairs of consecutive directions.

**Lemma 4 (cyclic comparison identity).** Let \(P\) start at \(x\), traverse directions \(p_1,\ldots,p_n\), and have edge-color word \(w_1,\ldots,w_n\). Put \(v_s=x\oplus e_{p_1}\oplus\cdots\oplus e_{p_s}\), and for distinct \(i,j\) write \(d_{ij}(v)=[c_i(v)\ne c_j(v)]\). Define
\[
T(P)=\sum_{s=1}^{n-1}d_{p_s,p_{s+1}}(v_s)
                         +d_{p_n,p_1}(v_n).\tag{6}
\]
Then
\[
T(P)=\sum_{s=1}^{n-1}[w_s\ne w_{s+1}]
                         +[w_n\ne1-w_1]\tag{7}
\]
is a positive odd integer. A cyclic rotation of \(P\), with its root moved along the geodesic, has \(T(P)-1\) changes. If \(P\) is chosen uniformly among all \(2^n n!\) rooted full geodesics, and \(k_v=|\{i:c_i(v)=1\}|\), then
\[
\mathbb E T(P)=\frac{2}{(n-1)2^n}
                    \sum_{v\in Q_n}k_v(n-k_v).\tag{8}
\]

*Proof.* The first \(n-1\) terms of (6) are the successive comparisons in the word of \(P\). At \(v_n=\bar x\), the incoming \(p_n\)-edge has color \(w_n\), while the \(p_1\)-edge has color \(1-w_1\), by antipodal oddness. This proves (7). The XOR of its \(n\) comparison bits is one, hence \(T(P)\) is odd.

Moving the root across the first \(s\) directions and transferring those directions to the end gives the color word
\[
w_{s+1},\ldots,w_n,1-w_1,\ldots,1-w_s.
\]
Its \(n-1\) comparisons omit one of the \(n\) comparisons of (7), and the omitted position ranges over all \(n\) positions as \(s\) varies. One omitted comparison can be a change, giving \(T(P)-1\).

For a uniformly rooted full geodesic, at each of the \(n\) positions in (6) the vertex is uniform in \(Q_n\), and the incident directions form a uniform ordered pair of distinct directions. At vertex \(v\), there are \(2k_v(n-k_v)\) bichromatic ordered pairs among the \(n(n-1)\) possibilities. Adding their expected contributions over \(n\) positions proves (8). \(\square\)

**Lemma 5 (exchange gain from a colored vertex star).** Sample uniformly a vertex \(v\) and four distinct ordered directions \(h,i,j,\ell\). Consider a full geodesic with consecutive directions \(h,i,j,\ell\) such that its vertex after the \(h\)-step is \(v\). Let \(\Delta\) be the change in \(T\) when \(i,j\) are exchanged. Then
\[
\mathbb E|\Delta|\ge\frac1{2^n}\sum_{v\in Q_n}\lambda_n(k_v).\tag{9}
\]

*Proof.* Only the comparisons at the three vertices \(v,v^i\) or \(v^j\), and \(v^{ij}\) can change. Hence, with the sign convention new minus old,
\[
\begin{aligned}
\Delta={}&d_{h,j}(v)-d_{h,i}(v)
+d_{j,i}(v^j)-d_{i,j}(v^i)\\
&+d_{i,\ell}(v^{ij})-d_{j,\ell}(v^{ij}).\tag{10}
\end{aligned}
\]
Fix \(v,i,j,\ell\). The last four terms are independent of \(h\). When \(c_i(v)=c_j(v)\), use the lower bound zero. Otherwise the first two terms total \(+1\) or \(-1\), with the sign determined by \(c_h(v)\).

Let \(a,b\) count the directions of the two colors among the \(n-3\) remaining directions after excluding \(i,j,\ell\). For any real \(K\), the triangle inequality gives
\[
\frac{a|K+1|+b|K-1|}{n-3}
\ge\frac{2\min(a,b)}{n-3}.\tag{11}
\]
This bounds the conditional mean of \(|\Delta|\) over \(h\).

Fix \(k=k_v\), \(m=\min(k,n-k)\). The probability that uniformly chosen distinct \(i,j\) are bichromatic is \(2k(n-k)/(n(n-1))\). Conditional on this event, removal of \(i,j\) leaves color counts \(m-1,n-m-1\). Choose \(\ell\) uniformly from the other \(n-2\) directions. If \(m<n/2\), the mean of the smaller remaining color count after removal of \(\ell\) is \((m-1)(n-3)/(n-2)\). If \(m=n/2\), it is \(m-2\). Combining these quantities with (11) gives the two nonzero cases of \(\lambda_n(k)\) in (1). For \(m=0\), there are no bichromatic pairs. Average over \(v\) to obtain (9). \(\square\)

*Proof of Theorem 1.* Select the \(q=q_n\) adjacent pairs of positions
\[
(2,3),\ (5,6),\ (8,9),\ldots,
(2+3(q-1),3+3(q-1)).\tag{12}
\]
Each has a preceding and following direction. For a full geodesic \(P\), let \(\Delta_s(P)\) be the difference in \(T(P)\) caused by exchanging the directions in pair \(s\).

The three consecutive comparison positions affected by each exchange are disjoint from those affected by the other exchanges in (12). Exchanging a pair also preserves the vertex and used-coordinate set following its second step. Thus the changes are additive. Choosing the exchanges independently, the least comparison count among the resulting \(2^q\) orders is
\[
T(P)+\sum_{s=1}^q\min\{0,\Delta_s(P)\}.\tag{13}
\]
Now choose \(P\) uniformly among all rooted full geodesics. Swapping either specified pair is an involution of this uniform space, so \(\mathbb E\Delta_s(P)=0\). Using \(\min(0,z)=(z-|z|)/2\), equations (8)--(9) give
\[
\begin{aligned}
\mathbb E[\text{quantity in (13)}]
&\le\frac1{2^n}\sum_v
\left(\frac{2k_v(n-k_v)}{n-1}
-\frac q2\lambda_n(k_v)\right)\\
&\le \max_{0\le k\le n}\Phi_n(k).
\end{aligned}\tag{14}
\]
There is therefore a modified full geodesic with \(T\) no larger than the right side. Its \(T\) is odd. Lemma 4 and the parity of \(T\) give (3). \(\square\)

*Proof of Corollary 2.* For \(n=10\), \(q_n=3\) and \(\Phi_{10}(k)=\Phi_{10}(10-k)\). Substitution in (1)--(2), for \(k=0,1,2,3,4,5\), gives
\[
0,\quad2,\quad\frac{154}{45},\quad\frac{259}{60},
\quad\frac{71}{15},\quad\frac{305}{63}.
\]
Thus \(\max_k\Phi_{10}(k)=305/63<5\). The odd positive integer \(T\) of the supplied full geodesic is at most three. A root rotation therefore gives \(\mu(c)\le2\). \(\square\)

*Proof of Corollary 3.* Let \(t=\min(k,n-k)/n\in[0,1/2]\). Since \(q_n=n/3+O(1)\), equations (1)--(2) yield uniformly in \(k\)
\[
\frac{\Phi_n(k)}n
=2t(1-t)-\frac23t^2(1-t)+O(n^{-1}).\tag{15}
\]
The polynomial is maximized on \([0,1/2]\) at \(t_*=(4-\sqrt7)/3\), with value \((28\sqrt7-40)/81\). Insert this maximum into (3). \(\square\)

The inequalities constrain every admissible coloring through the degrees of the two colors at its vertices. They combine antipodal root rotation with several simultaneously available path exchanges. The ten-dimensional conclusion does not require an inductive hypothesis or a structural classification of face colorings.

Let \(n\ge5\), and let \(c\) be an antipodally odd coloring of the undirected edges of \(Q_n\). Write \(c_i(v)\) for the color of the edge in direction \(i\) incident with \(v\), and set
\[
d_{ij}(v)=[c_i(v)\ne c_j(v)],\qquad
k_v=\sum_i c_i(v),\qquad m_v=\min(k_v,n-k_v).
\]
For \(i\ne j\), put \(v^{ij}=v\oplus e_i\oplus e_j\) and define the square curvature
\[
\kappa_{ij}(v)=c_i(v)\oplus c_j(v^i)\oplus c_i(v^j)\oplus c_j(v).
\tag{1}
\]
All sums in (1) are modulo two. Since \(c_i(v^j)=c_i(v^{ij})\) and \(c_j(v^i)=c_j(v^{ij})\), we have
\[
\boxed{\kappa_{ij}(v)=d_{ij}(v)\oplus d_{ij}(v^{ij}).}\tag{2}
\]
Thus curvature is the disagreement between the two opposite-vertex bichromatic-turn indicators of a square.

Recall the functions \(\lambda_n(k)\), \(\Phi_n(k)\), and \(q_n=\lfloor(n-1)/3\rfloor\) from the preceding cyclic-turn exchange theorem. Define
\[
\eta_n(k)=
\begin{cases}
0,&\min(k,n-k)=0,\\[1mm]
\dfrac{2(\min(k,n-k)-1)}{n-2}
+\dfrac{\mathbf1_{\{n\ {\rm even},\,k=n/2\}}}{n-3},
&\min(k,n-k)\ge1,
\end{cases}
\tag{3}
\]
and the nonnegative curvature-weighted statistic
\[
\mathcal K_n(c)=
\frac1{2^n n(n-1)}
\sum_{v\in Q_n}\sum_{i\ne j}
[d_{ij}(v)=1,\ d_{ij}(v^{ij})=0]\,
\eta_n(k_v).
\tag{4}
\]

**Theorem 1 (curvature-sensitive all-dimensional exchange bound).** Every antipodally odd edge coloring of \(Q_n\), \(n\ge5\), satisfies
\[
\boxed{\displaystyle
\mu(c)\le 2\left\lfloor
\frac{\frac1{2^n}\sum_v\Phi_n(k_v)
-\frac{q_n}{2}\mathcal K_n(c)-1}{2}
\right\rfloor.}
\tag{5}
\]
In particular, a counterexample to \(\mu(c)\le2\) in dimension \(n\) must satisfy
\[
\boxed{\displaystyle
\frac1{2^n}\sum_v\Phi_n(k_v)
-\frac{q_n}{2}\mathcal K_n(c)\ge5.}
\tag{6}
\]
The improvement over the earlier exchange bound is additive and nonnegative for every coloring, with a positive contribution whenever some curved square has a bichromatic corner at which both edge colors occur at least twice.

**Proof.** For a uniformly chosen vertex \(v\) and distinct ordered directions \(h,i,j,\ell\), form the two full geodesics differing by the exchange of adjacent directions \(i,j\) inside the consecutive block \(h,i,j,\ell\), with \(v\) immediately after \(h\). Let \(\Delta\) be the change in their cyclic turn counts. Set \(w=v^{ij}\). The comparison formula established in the preceding exchange lemma is
\[
\Delta=d_{hj}(v)-d_{hi}(v)
+d_{ij}(v^j)-d_{ij}(v^i)
+d_{i\ell}(w)-d_{j\ell}(w).\tag{7}
\]
Here \(d_{ij}=d_{ji}\). The middle difference is zero if \(d_{ij}(v)=d_{ij}(w)\), and is \(+1\) or \(-1\) otherwise; this follows from the four-corner identity
\[
d_{ij}(v)\oplus d_{ij}(v^i)\oplus
d_{ij}(v^j)\oplus d_{ij}(w)=0.\tag{8}
\]

There are four possibilities for \((d_{ij}(v),d_{ij}(w))\).

When it equals \((0,0)\), all three differences in (7) vanish.

When it equals \((1,1)\), the middle difference vanishes and each outer difference is \(+1\) or \(-1\). Fixing \(\ell\), the first difference takes these two signs as the color of \(h\) varies. There are \(n-3\) choices of \(h\), with color multiplicities \(a,b\) among these directions. The triangle inequality shows that the mean of \(|\Delta|\) over \(h\) is at least \(2\min(a,b)/(n-3)\). Averaging over \(\ell\) yields the lower bound
\[
g_n(k_v)=
\begin{cases}
\dfrac{2(m_v-1)}{n-2},&2m_v<n,\\
\dfrac{2(m_v-2)}{n-3},&2m_v=n,
\end{cases}\tag{9}
\]
provided \(d_{ij}(v)=1\).

When the pair is \((1,0)\), the last difference vanishes, and the middle difference has absolute value one. The first difference has the two possible signs according to the color of \(h\). Since \(h\) is uniform among the \(n-2\) directions outside \(\{i,j\}\), the mean satisfies
\[
\mathbb E_{h,\ell}|\Delta|
\ge g_n'(k_v):=\frac{2(m_v-1)}{n-2}.\tag{10}
\]
Thus relative to the bound (9), this case supplies the extra \(g_n'(k_v)-g_n(k_v)\), which is \(1/(n-3)\) when \(n\) is even and \(k_v=n/2\), and zero otherwise.

Finally, when the pair is \((0,1)\), the first difference vanishes and the middle difference has absolute value one. The last difference, as \(\ell\) varies among the \(n-2\) remaining directions, has two possible signs. Consequently
\[
\mathbb E_{h,\ell}|\Delta|\ge g_n'(k_w).\tag{11}
\]
Averaging (11) over uniformly chosen \(v,i,j\) and replacing \(v\) by \(w=v^{ij}\) identifies its contribution with the \((1,0)\) cases, weighted by \(g_n'(k_v)\). Combining the four cases, using (9)--(11), gives
\[
\boxed{
\mathbb E|\Delta|
\ge \frac1{2^n}\sum_v\lambda_n(k_v)+\mathcal K_n(c).
}\tag{12}
\]
Indeed, the first term is the mean over bichromatic ordered pairs at \(v\) of the bound \(g_n(k_v)\), and the remaining two contributions total \(2g_n'-g_n=\eta_n\) on the \((1,0)\) cases.

Apply the \(q_n\) independent position-pair exchanges from the preceding theorem. Their changes in cyclic turn count are additive; each has mean zero and has the absolute-change estimate (12). As before, averaging over the initial rooted geodesic and choosing the better orientation of every exchange gives a full geodesic with odd cyclic turn count at most
\[
\frac1{2^n}\sum_v\Phi_n(k_v)-\frac{q_n}{2}\mathcal K_n(c).
\]
Cyclically rotating its coordinate order removes one changed comparison, proving (5). If \(\mu(c)>2\), then this odd turn count is at least five, yielding (6). \(\square\)

**Corollary 2 (a restriction on eleven-dimensional counterexamples).** Suppose \(n=11\) and every vertex is incident with five or six edges of color one. Let
\[
\delta(c)=
\frac{\#\{\text{two-dimensional faces with odd curvature}\}}
{\binom{11}{2}2^9}.
\tag{13}
\]
Then
\[
\boxed{
\mu(c)\le
2\left\lfloor\frac{58/11-(2/3)\delta(c)-1}{2}\right\rfloor.
}\tag{14}
\]
In particular, \(\delta(c)>9/22\) implies \(\mu(c)\le2\). Every putative four-switch example with balanced incident-color degrees must have \(\delta(c)\le9/22\).

*Proof.* At every vertex, \(\Phi_{11}(k_v)=58/11\) and \(m_v=5\), so \(\eta_{11}(k_v)=8/9\). On each odd-curvature square, precisely two of its four vertices satisfy \(d_{ij}(v)=1\) and \(d_{ij}(v^{ij})=0\). Counting both orders of \(i,j\) gives \(\mathcal K_{11}(c)=(4/9)\delta(c)\). Since \(q_{11}=3\), substitute in (5). \(\square\)

The curvature statistic also obeys an independent parity law.

**Theorem 3 (antipodal reversal holonomy).** Let \(P\) be any full antipodal geodesic, rooted at \(x\), with direction order \(p_1,\ldots,p_n\). Reverse this order at the same root by adjacent exchanges. If \(S_1,\ldots,S_{\binom n2}\) are the successive squares traversed by any reduced adjacent-transposition reversal, then
\[
\boxed{\bigoplus_{r=1}^{\binom n2}\kappa(S_r)=n\pmod2.}\tag{15}
\]
Consequently, in every odd dimension, every such reversal sequence encounters an odd number of curved squares. Writing \(\delta_{ij}\) for the proportion of curved squares parallel to directions \(i,j\), every admissible coloring in odd dimension satisfies
\[
\boxed{\sum_{i<j}\delta_{ij}\ge1,\qquad
\delta(c):=\frac1{\binom n2}\sum_{i<j}\delta_{ij}
\ge \frac1{\binom n2}.}\tag{16}
\]
The second bound is sharp even among colorings for which every vertex is incident with \((n-1)/2\) or \((n+1)/2\) edges of color one.

*Proof.* Let \(w_1,\ldots,w_n\) be the edge colors along \(P\). The geodesic with reversed direction order and the same root has colors \(1-w_n,\ldots,1-w_1\), because each of its edges is antipodal to the corresponding edge of \(P\). Therefore the parity of the sum of its edge colors differs by \(n\pmod2\). Each adjacent transposition replaces a two-edge route across a square by the other two-edge route, changing this parity by the square curvature. Summing over the reversal proves (15).

For odd \(n\), the number of curved squares in every reversal is odd and positive. Choose the root and the original order uniformly. Each unordered direction pair is exchanged once in the reduced reversal, and the square at which it is exchanged is uniform among the \(2^{n-2}\) squares of those directions (by translation symmetry of the sampled root). Hence the expected number of curved squares in the reversal is \(\sum_{i<j}\delta_{ij}\), proving (16).

For sharpness, write \(n=2m+1\), designate the final coordinate by \(u\), and on an edge in direction \(i\) assign
\[
c_{2a-1}(v)=v_u,\qquad c_{2a}(v)=1-v_u
\quad(1\le a\le m),\qquad
c_u(v)=v_1\oplus\cdots\oplus v_{2m-1}.
\tag{17}
\]
These values are independent of the coordinate being traversed, so define undirected-edge colors. All defining functions change under complementation of every coordinate, making the coloring antipodally odd. Every pair \(2a-1,2a\) contributes one edge of each color at every vertex, while direction \(u\) contributes either color; the degree condition follows. The curvature vanishes on every direction pair except \(\{2m,u\}\), and every square in that pair has curvature one. Thus \(\sum_{i<j}\delta_{ij}=1\), proving sharpness. \(\square\)

Theorems 1 and 3 combine two complementary constraints on unrestricted instances: color imbalance at individual vertex stars governs the baseline cyclic turn count, while nonflat two-faces force extra exchange opportunities. The sharpness example shows that parity alone supplies only \(O(n^{-2})\) square-curvature density in odd dimension; stronger dimension-uniform conclusions require additional correlations between these local statistics.

Fix \(n\ge3\), and let \(V=\{0,1\}^n\). For each vertex \(v\) and distinct coordinate directions \(i,j\), consider a symmetric binary array \(D=(d_{ij}(v))\), with \(d_{ij}(v)=d_{ji}(v)\). Write \(v^i=v\oplus e_i\) and \(\bar v=v\oplus(1,\ldots,1)\). We impose the following relations:
\[
\begin{array}{ll}
\text{triangle:}&d_{ij}(v)\oplus d_{jk}(v)\oplus d_{ik}(v)=0
\quad(i,j,k\text{ distinct}),\\
\text{square:}&d_{ij}(v)\oplus d_{ij}(v^i)\oplus
d_{ij}(v^j)\oplus d_{ij}(v^{ij})=0,\\
\text{antipodal:}&d_{ij}(\bar v)=d_{ij}(v).
\end{array}\tag{1}
\]
For a root \(x\) and an ordering \(\pi=(p_1,\ldots,p_n)\) of the directions, put
\[
v_s=x\oplus e_{p_1}\oplus\cdots\oplus e_{p_s},
\quad v_n=\bar x,
\]
and define its cyclic turn sum
\[
\Theta_D(x,\pi)=
\sum_{s=1}^{n-1}d_{p_s,p_{s+1}}(v_s)
+d_{p_n,p_1}(\bar x),\tag{2}
\]
where the sum in (2) is over the ordinary integers.

**Theorem 1 (complete reconstruction from incidence disagreements).** Suppose \(D\) satisfies the triangle and square relations of (1). There is an undirected-edge coloring \(c:E(Q_n)\to\{0,1\}\) such that
\[
\boxed{d_{ij}(v)=c_i(v)\oplus c_j(v)
\quad\text{for all }v,\ i\ne j,}\tag{3}
\]
where \(c_i(v)\) is the color of the edge in direction \(i\) incident with \(v\). The coloring is unique up to complementation of all edge colors.

If \(D\) also satisfies the antipodal relation, the reconstructed coloring obeys
\[
c_i(\bar v)=c_i(v)\oplus\varepsilon
\quad\text{for every }v,i,\tag{4}
\]
with one constant \(\varepsilon\in\{0,1\}\). Moreover
\[
\boxed{\Theta_D(x,\pi)\equiv\varepsilon\pmod2
\quad\text{for every root and every ordering}.}\tag{5}
\]
Consequently, \(D\) arises from an antipodally odd edge coloring if and only if it satisfies all three relations of (1) and \(\Theta_D(x,\pi)\) is odd for one (equivalently every) root and ordering. For such an array, the compatible antipodally odd edge colorings are precisely a complementary pair.

*Proof.* Fix a reference direction \(1\), and define vertex functions
\[
r_1(v)=0,\qquad r_i(v)=d_{1i}(v)\quad(i\ne1).\tag{6}
\]
The triangle relation implies \(r_i(v)\oplus r_j(v)=d_{ij}(v)\) for all distinct \(i,j\).

For every direction \(i\), define an edge cochain
\[
a_i(v)=r_i(v)\oplus r_i(v^i).\tag{7}
\]
It has the same value at the two endpoints of an \(i\)-edge. Its sum around any square in directions \(i,j\) equals
\[
\begin{aligned}
&a_i(v)\oplus a_j(v^i)\oplus a_i(v^j)\oplus a_j(v)\\
&\qquad=d_{ij}(v)\oplus d_{ij}(v^i)
\oplus d_{ij}(v^j)\oplus d_{ij}(v^{ij})=0.\tag{8}
\end{aligned}
\]
Thus \(a\) is a gradient on the cube: a binary vertex function \(f\) exists satisfying
\[
f(v)\oplus f(v^i)=a_i(v)\quad\text{for every }v,i.\tag{9}
\]
For completeness, construct \(f(v)\) by summing \(a\) along any path from the zero vertex to \(v\). Backtracking along an edge changes the sum by zero; interchanging two consecutive different coordinate steps changes it by the square sum (8), also zero. Such operations connect any two cube walks with the same endpoints, so the definition is independent of the walk.

Set
\[
c_i(v)=r_i(v)\oplus f(v).\tag{10}
\]
Equations (7) and (9) give \(c_i(v)=c_i(v^i)\), so (10) defines a coloring of undirected edges. Equation (6) and the triangle relation yield
\(c_i(v)\oplus c_j(v)=d_{ij}(v)\), proving existence.

For uniqueness, suppose \(c'\) has the same incidence disagreements. At every vertex, the values \(c_i'(v)\oplus c_i(v)\) are independent of \(i\); call this value \(b(v)\). As both colorings are constant along each edge in its direction, \(b(v)=b(v^i)\) for every \(i\), hence \(b\) is constant on the connected cube. Therefore \(c'=c\) or \(c'=1-c\).

Assume now the antipodal relation of (1). At vertex \(v\),
\[
[c_i(\bar v)\oplus c_i(v)]\oplus
[c_j(\bar v)\oplus c_j(v)]
=d_{ij}(\bar v)\oplus d_{ij}(v)=0.
\]
So \(\varepsilon(v):=c_i(\bar v)\oplus c_i(v)\) is independent of \(i\). Evaluating at vertices \(v,v^i\), using the \(i\)-edge at each and its antipodal edge, gives \(\varepsilon(v^i)=\varepsilon(v)\). Connectivity implies one constant \(\varepsilon\), proving (4).

Let \(w_1,\ldots,w_n\) be the edge-color word on the geodesic rooted at \(x\) with direction order \(\pi\). Each interior term of (2) equals \(w_s\oplus w_{s+1}\). Its final term equals \(w_n\oplus w_1\oplus\varepsilon\), because the \(p_1\)-edge at \(\bar x\) has color \(w_1\oplus\varepsilon\). The XOR of these \(n\) terms is \(\varepsilon\), proving (5). The stated criterion follows. \(\square\)

**Theorem 2 (intrinsic switch-count and counterexample criterion).** Suppose \(D\) satisfies the four requirements of Theorem 1, including odd cyclic turn parity, and let \(c\) be either reconstructed coloring. Then
\[
\boxed{\displaystyle
\mu(c)=\min_{x,\pi}\Theta_D(x,\pi)-1.}\tag{11}
\]
In particular,
\[
\boxed{
\mu(c)\le2\iff
\Theta_D(x,\pi)\le3
\text{ for some }x,\pi,}\tag{12}
\]
and a hypothetical unrestricted counterexample to the two-switch bound is equivalently an array obeying (1) and oddness for which
\[
\boxed{\Theta_D(x,\pi)\ge5\quad
\text{for every }x,\pi.}\tag{13}
\]
The values of \(\mu(c)\), the set of roots of low-switch geodesics, and their endpoint sets are determined by \(D\).

*Proof.* The number of color changes on the path with root \(x\) and order \(\pi\) is
\[
\sigma_c(x,\pi)=\sum_{s=1}^{n-1}d_{p_s,p_{s+1}}(v_s).\tag{14}
\]
Thus \(\Theta_D(x,\pi)\) is \(\sigma_c(x,\pi)\) plus a binary seam comparison, and it is always odd by Theorem 1. Cyclically rotate the direction order, changing the root from \(x\) to one of the intermediate vertices along the original path. As in the cyclic comparison identity, the resulting color words are successive cyclic shifts of
\[
w_1,\ldots,w_n,1-w_1,\ldots,1-w_n.
\]
The rotations preserve \(\Theta_D\) and respectively omit each of its \(n\) seam comparisons. Since \(\Theta_D\) is odd, at least one comparison is a change, and some rotation has \(\Theta_D-1\) changes.

Conversely, every geodesic has \(\sigma_c\ge\Theta_D-1\), because its seam comparison is at most one. Applying the preceding rotation to a geodesic minimizing \(\Theta_D\) proves (11). Oddness of \(\Theta_D\) yields (12)--(13). Equation (14) proves the statement about roots and endpoints. \(\square\)

**Corollary 3 (size of the unrestricted class).** For \(n\ge3\), the arrays \(D\) satisfying (1) and the oddness condition constitute an affine binary space of dimension
\[
\boxed{n\,2^{n-2}-1.}\tag{15}
\]

*Proof.* The \(n2^{n-1}\) undirected edges of \(Q_n\) form \(n2^{n-2}\) disjoint antipodal pairs. Choosing one edge color per pair determines an antipodally odd coloring, so these colorings form an affine binary space of dimension \(n2^{n-2}\). Their passage to \(D\) is linear with a one-dimensional kernel, namely uniform global color complementation, by Theorem 1. Its image therefore has affine dimension \(n2^{n-2}-1\). \(\square\)

The reconstruction identifies local consistency conditions sufficient to recover all unrestricted edge colorings up to their irrelevant global color phase. In particular, the low-switch problem may be phrased entirely in terms of antipodally even vertex-indexed incidence disagreements, subject to triangle, square and one global oddness constraint. The cyclic comparison and curvature-sensitive exchange inequalities then become inequalities intrinsic to \(D\); any low-switch terminal-alignment argument can be formulated in the same data without committing to a choice of edge-color phase.

### Projective two-turn incidence, Fourier kernel rigidity, and the five-cube theorem

Let \(n\ge5\). A legal edge coloring of \(Q_n\) consists of bits \(c_i(x)\) satisfying \(c_i(x+e_i)=c_i(x)\) and \(c_i(\bar x)=1-c_i(x)\). Write \([x]=\{x,\bar x\}\). A **projective turn** is a pair \(t=([x],\{i,j\})\), with \(i\ne j\); its color-change indicator is
\[
I_t=\mathbf1_{\{c_i(x)\ne c_j(x)\}}.
\]
This is independent of the representative of \([x]\). A coherent support is the projective \(n\)-cycle obtained from an antipodal full geodesic by identifying antipodal edges. Its successive direction labels are all different. Write \(\mathcal O_n\) for these supports, \(M=|\mathcal O_n|=2^{n-2}(n-1)!\), and \(A\) for the \(\{0,1\}\)-incidence matrix whose rows are supports and columns are projective turns. If \(T_c(O)\) denotes the number of cyclic color transitions on the lifted \(2n\)-cycle, then
\[
T_c(O)=2(AI)_O,\qquad T_c(O)\in 2+4\mathbb Z_{\ge0}.
\tag{1}
\]
The congruence follows because the length-\(2n\) color word is antiperiodic.

#### The two-turn incidence formula

**Theorem 1.** Let \(t=([x],\{i,j\})\) and \(u=([y],\{k,l\})\) be projective turns, and let \(N(t,u)=(A^\top A)_{t,u}\). For \(n\ge3\), the following exhaust the possibilities.

* If \(t=u\), then \(N(t,u)=(n-2)!\).
* If \(t\ne u\) and \([x]=[y]\), then \(N(t,u)=0\).
* If the direction pairs have one common member \(h\), then \(N(t,u)=(n-3)!\) when \([y]=[x+e_h]\), and \(N(t,u)=0\) otherwise.
* Suppose \(i,j,k,l\) are distinct. Put \(d=x+y\) in \(\mathbb F_2^n\). If \(d_i=d_j\) or \(d_k=d_l\), then \(N(t,u)=0\). Otherwise let \(B\) be the unique set among \(\operatorname{supp}(d)\) and its complement with \(j\in B\) and \(i\notin B\). Then
\[
\boxed{N(t,u)=(|B|-2)!(n-|B|-2)!.}
\tag{2}
\]

**Proof.** Fix the lift \(x\) of the first projective vertex and orient the support so its first direction is \(j\) and last direction is \(i\). Supports through \(t\) correspond bijectively to permutations of the remaining \(n-2\) directions; this gives the diagonal count. A projective support is a simple cycle, hence two distinct turns at one projective vertex cannot coexist.

A direction occurs once on a projective support. If it occurs in both turns, those turns must be the endpoints of that direction's projective edge; fixing their adjacent positions leaves \((n-3)!\) permutations.

For four different directions, a second projective vertex reached from \(x\) after the initial segment of the rooted order corresponds to a proper prefix set \(B\) with \(j\in B\), \(i\notin B\). Equality of that vertex with \([y]\) means that \(B\) is one of \(\operatorname{supp}(d)\) and its complement, which is possible precisely when \(d_i\ne d_j\). For the turn at \(y\) to involve \(k,l\), these directions must lie on opposite sides of the prefix, equivalently \(d_k\ne d_l\). One specified member of \(\{k,l\}\) must terminate the permutation of \(B\setminus\{j\}\), and the other must begin the permutation of \(B^c\setminus\{i\}\). The independent orders of their remaining members have respectively \((|B|-2)!\) and \((n-|B|-2)!\) possibilities. \(\square\)

Consequently the second moment is a quadratic expression entirely in incident edge colors:
\[
\boxed{\mathbb E_{O}T_c(O)^2=
\frac4M\sum_{t,u}N(t,u)I_tI_u.}
\tag{3}
\]
The sum is over ordered pairs of projective turns.

#### Complete real kernel of projective turn incidence

**Theorem 2 (turn-incidence kernel).** For \(n\ge5\), a real weighting \(f_{ij}([x])=f_{ji}([x])\) of projective turns satisfies
\[
\sum_{t\in O}f_t=0\quad\text{for every }O\in\mathcal O_n
\tag{4}
\]
if and only if there are constants \(a_i\) with \(\sum_i a_i=0\), and real functions \(g_i\) on projective vertices satisfying \(g_i([x+e_i])=-g_i([x])\), such that
\[
\boxed{f_{ij}([x])=a_i+a_j+g_i([x])+g_j([x]).}
\tag{5}
\]
In particular,
\[
\boxed{\dim_{\mathbb R}\ker A=n2^{n-2}+n-1,\qquad
\operatorname{rank}_{\mathbb R}A=
2^{n-1}\binom n2-n2^{n-2}-(n-1).}
\tag{6}
\]

**Proof.** The characters \(\chi_S(x)=(-1)^{\sum_{i\in S}x_i}\) of even cardinality \(S\subseteq[n]\) form a Fourier basis on the projective vertex group. Expand
\[
f_{ij}([x])=\sum_{|S|\ {\rm even}}\chi_S(x)b_{ij}(S).
\]
For a cyclic ordering \(\pi=(\pi_1,\ldots,\pi_n)\), set \(\pi_0=\pi_n\). The projective turns based at the prefixes \(x+\sum_{r\le k}e_{\pi_r}\), \(0\le k<n\), are \((\pi_k,\pi_{k+1})\). Requiring (4) at every translated root and taking Fourier coefficients gives, for each even \(S\),
\[
\sum_{k=0}^{n-1}
(-1)^{|S\cap\{\pi_1,\ldots,\pi_k\}|}
b_{\pi_k,\pi_{k+1}}(S)=0
\quad\text{for every }\pi.
\tag{7}
\]
Suppress \(S\) and put \(s_i=\mathbf1_{\{i\in S\}}\). Compare a direction order containing four consecutive distinct entries \(h,a,b,k\) to the order with \(a,b\) exchanged. Cancellation of all unchanged turns in (7) gives
\[
b_{ha}-b_{hb}
+\big((-1)^{s_a}-(-1)^{s_b}\big)b_{ab}
+(-1)^{s_a+s_b}(b_{bk}-b_{ak})=0.
\tag{8}
\]
The labels \(h,k\) may be any two distinct labels outside \(\{a,b\}\).

If \(S=\varnothing\) or \(S=[n]\), all signs \(s_i\) agree and (8) becomes
\(b_{ha}-b_{hb}=b_{ka}-b_{kb}\).
As there are at least three labels outside each \(\{a,b\}\), the standard four-point additive identity follows: \(b_{ij}=v_i+v_j\) for some real \(v_i\). In the empty-set mode, (7) then gives \(2\sum_i v_i=0\). In the full-set mode (which is present only when \(n\) is even), (7) vanishes for every additive weighting, since the sign reverses at each dimension.

Now suppose \(\varnothing\ne S\ne[n]\). Choose \(a\in S\), \(b\notin S\). Equation (8) reads
\[
(b_{ha}-b_{hb})+(b_{ka}-b_{kb})=2b_{ab}.
\]
With at least three other labels, this forces
\[
b_{va}-b_{vb}=b_{ab}\qquad(v\notin\{a,b\}).
\tag{9}
\]
Fix one \(b_0\notin S\) and set \(v_a=b_{a b_0}\) for \(a\in S\), \(v_b=0\) for \(b\notin S\). Equation (9) first gives \(b_{aa'}=v_a+v_{a'}\) for \(a,a'\in S\). For distinct \(b,b'\notin S\), applying (9) to the mixed pairs \((a,b)\) and \((a,b')\) gives
\(b_{ab'}-b_{bb'}=b_{ab}\) and \(b_{ab}-b_{bb'}=b_{ab'}\). Thus \(b_{bb'}=0\) and \(b_{ab}=v_a\), independently of \(b\notin S\). The same conclusion holds when there is only one outside label. Hence
\[
b_{ij}(S)=v_i(S)+v_j(S),\qquad v_i(S)=0\quad(i\notin S).
\tag{10}
\]
Conversely these Fourier weightings satisfy (7): every \(v_i(S)\) with \(i\in S\) occurs at the two turns incident with the \(i\)-edge with opposite Fourier signs. The empty mode satisfies (7) precisely when the constants sum to zero.

Reassembling the Fourier modes gives (5), where the nonconstant modes of \(g_i\) all contain \(i\), equivalently \(g_i([x+e_i])=-g_i([x])\). Conversely each \(g_i\) cancels across its projective edge on every support, and the constant terms contribute \(2\sum_i a_i=0\).

For each \(i\), the anti-invariant functions under translation by \(e_i\) have dimension \(2^{n-2}\) on the projective vertex group. The constant \(a_i\) have dimension \(n-1\). For \(n\ge3\), the map sending \((a_i+g_i)_i\) to the pair sums in (5) is injective, since all pair sums of \(n\) real numbers determine those numbers. This proves (6). \(\square\)

**Corollary 3 (local four-direction constraint).** Every \(f\in\ker A\) satisfies, at every projective vertex and for every four distinct directions,
\[
\boxed{f_{ij}+f_{kl}-f_{ik}-f_{jl}=0.}
\tag{11}
\]
This gives an explicit local obstruction to constant support sums.

#### Rigidity of constant turn energy

**Theorem 4.** In every dimension \(n\ge5\), if a legal coloring has the same cyclic turn energy \(T_c(O)=\tau\) on all coherent supports, then \(\tau=2\). Consequently every coherent support contains a monochromatic full antipodal geodesic.

**Proof.** The constant-one turn weighting has support sum \(n\). Thus
\[
f_{ij}([x])=I_{ij}([x])-\frac{\tau}{2n}
\]
belongs to \(\ker A\). By Corollary 3 the unlike-color indicators \(I_{ij}([x])\) satisfy the local four-direction identity (11). If at a vertex at least two incident edges have each color, choose distinct \(i,j\) of color zero and \(k,l\) of color one. Then
\[
I_{ij}+I_{kl}-I_{ik}-I_{jl}=0+0-1-1=-2,
\]
a contradiction. Therefore the number \(r(x)\) of color-one incident edges belongs to \(\{0,1,n-1,n\}\) at every vertex.

For completeness, each projective turn lies on \((n-2)!\) coherent supports, and the number of unlike-color turns at \([x]\) is \(r(x)(n-r(x))\). Counting turn incidences and using \(M=2^{n-2}(n-1)!\) gives
\[
\mathbb E_O T_c(O)=
\frac{4}{n-1}\mathbb E_x r(x)(n-r(x)).
\tag{12}
\]
The permitted values of \(r(x)\) imply \(r(x)(n-r(x))\le n-1\), whence \(\tau\le4\). By (1), \(\tau\) is a positive integer congruent to \(2\pmod4\); therefore \(\tau=2\). The equivalence between two transitions and a monochromatic half-cycle proves the assertion. \(\square\)

**Corollary 5 (NORI1 in dimension five).** Every legal antipodally odd edge coloring of \(Q_5\) has a monochromatic full antipodal geodesic.

**Proof.** In odd dimension the signed vertex-star sum \(S(x)=\sum_i(-1)^{c_i(x)}\) is odd, hence \(S(x)^2\ge1\). Equation (12), together with \(S=n-2r\), yields
\[
\mathbb E_O T_c(O)=\frac{n^2-\mathbb E_x S(x)^2}{n-1}
\le n+1.
\]
For \(n=5\) this mean is at most \(6\). If no support contained a monochromatic full geodesic, (1) would give \(T_c(O)\ge6\) on every support. Every support would therefore have energy \(6\), contradicting Theorem 4. \(\square\)

#### Quantitative variance consequence

Let \(m(c)\) count projective vertices at which both colors occur at least twice. Let \(\lambda_n>0\) denote the smallest positive eigenvalue of the explicitly determined matrix \(A^\top A=(N(t,u))\). Then for \(n\ge5\),
\[
\boxed{\operatorname{Var}_O(T_c(O))\ge
\frac{4\lambda_n}{2^{n-2}(n-1)!}\,m(c).}
\tag{13}
\]
Indeed, at each such vertex choose two directions of each color. The four-turn vector \(L=e_{ij}+e_{kl}-e_{ik}-e_{jl}\) has norm \(2\), annihilates the kernel by (11), and has inner product \(-2\) with \(I\). The vectors \(L/2\) at different projective vertices are orthonormal. If \(P\) is orthogonal projection onto \((\ker A)^\perp\), Bessel's inequality gives \(\|PI\|^2\ge m(c)\). Since \(T=2AI\), \(\operatorname{Var}(T)=4\|A(I-\frac{\mathbb E T}{2n}\mathbf1)\|^2/M\); the spectral lower bound proves (13).

A stronger, degree-explicit variance bound holds. Put \(s(x)=n-r(x)\) and
\[
D_n(r)=\frac{2r(n-r)\big(r(n-r)-(n-1)\big)}{(n-1)(n-2)}.
\]
Then
\[
\boxed{\operatorname{Var}_O(T_c(O))
\ge\frac{4\lambda_n}{M}\sum_{[x]}D_n(r(x)).}
\tag{17}
\]
To prove this, view the turn indicators at one projective vertex as a vector in \(\mathbb R^{\binom n2}\). The subspace of pair-additive vectors \(v_{ij}=z_i+z_j\) is the image of the unsigned vertex-edge incidence matrix \(B\) of \(K_n\), whose Gram matrix is \(B^\top B=(n-2)I+J\). For a color split of sizes \(r,s=n-r\), the turn indicator has squared norm \(rs\), while its image under \(B^\top\) has \(r\) entries equal to \(s\) and \(s\) entries equal to \(r\). Orthogonal projection gives squared distance
\[
rs-\frac{rs\,n-2r^2s^2/(n-1)}{n-2}=D_n(r).
\]
Every member of \(\ker A\) is pair-additive at each projective vertex by Theorem 2. Thus the squared distance from \(I\) to \(\ker A\) is at least \(\sum_{[x]}D_n(r(x))\). The same spectral estimate used for (13) proves (17). In particular \(D_n(r)>0\) precisely when both colors occur at least twice at that vertex.

If no monochromatic support exists, \(6\le T_c(O)\le2n\). For \(\mu=\mathbb E T_c(O)\), the elementary bounded-variance inequality gives \(\operatorname{Var}(T_c)\le(2n-\mu)(\mu-6)\). Therefore the following sufficient condition applies to every legal coloring:
\[
\boxed{\frac{4\lambda_n}{M}m(c)>(2n-\mu)(\mu-6)
\quad\Longrightarrow\quad\text{a monochromatic full antipodal geodesic exists}.}
\tag{14}
\]
The kernel theorem and the five-cube conclusion require no spectral numerical approximations. The higher-dimensional implication of (14) depends on the coloring's star data.

#### Finite verification

An independent exhaustive support enumerator checked (2) on all unordered turn pairs in dimensions \(3,4,5,6\): respectively \(78,1176,12880,115440\) pairs, with support counts \(4,24,192,1920\). The first and second moments were also compared against direct cyclic-energy evaluation for three independently sampled legal colorings in each dimension. Numerical real-rank checks found \(\operatorname{rank} A=116\) for \(n=5\) and \(379\) for \(n=6\), agreeing with (6). These checks are supplementary to the proofs above.

#### A uniform three-support theorem in the five-cube

**Theorem 6.** Every legal edge coloring of \(Q_5\) has at least five distinct coherent supports containing monochromatic full antipodal geodesics. More precisely, let \(b\) be the number of projective vertices where \(r(x)\notin\{2,3\}\). If \(b>0\), there are at least \(6b\) such supports; if \(b=0\), there are at least five.

**Proof.** There are \(192\) coherent supports and \(16\) projective vertices. The only possible energies are \(2,6,10\); let their multiplicities be \(a,d,h\). At a balanced projective vertex, \((5-2r)^2=1\), while at each of the \(b\) other vertices it is at least \(9\). Thus the first-moment identity gives
\[
\mu=\mathbb E T_c(O)\le 6-b/8.
\]
Since \(\mu=6+4(h-a)/192\), we have \(a-h\ge6b\), and hence \(a\ge6b\). This settles \(b>0\).

Suppose \(b=0\). Then \(\mu=6\), \(a=h\), and \(\operatorname{Var}(T_c)=32a/192\). The spectrum of the turn Gram matrix can be found directly from Theorem 1 using Fourier transform over the projective vertex group. For any even \(S\subseteq[5]\), let the \(10\times10\) Fourier block be
\[
K_S(P,Q)=\sum_{[y]}(-1)^{\sum_{i\in S}y_i}\,
N(([0],P),([y],Q)),
\qquad P,Q\in\binom{[5]}2.
\tag{15}
\]
The symmetric-group action shows that its eigenvalues depend only on \(|S|\). Substitution of (2) and computation of the three characteristic polynomials give the following eigenvalue multisets:
\[
\begin{array}{c|l}
|S|&\operatorname{spec}(K_S)\\ \hline
0& 0^{(4)},\,6^{(5)},\,30\\
2&0^{(2)},\,6^{(2)},\,10-4\sqrt5,\,10+4\sqrt5,\,
(7-\sqrt{17})^{(2)},\,(7+\sqrt{17})^{(2)}\\
4&0^{(4)},\,6^{(3)},\,14^{(3)}
\end{array}
\tag{16}
\]
Here superscripts in parentheses denote multiplicities. These are characteristic-polynomial computations of matrices defined by the finite integer formula (2); no assumption about the coloring enters. Thus
\(\lambda_5=10-4\sqrt5>1\).
All \(16\) projective vertices have \(r(x)\in\{2,3\}\), hence \(D_5(r(x))=2\). Applying the stronger bound (17) gives
\[
\frac{32a}{192}=\operatorname{Var}(T_c)
\ge \frac{4\lambda_5\cdot32}{192}.
\]
Therefore \(a\ge4\lambda_5>4\); since \(a\) is an integer, \(a\ge5\). \(\square\)

The Fourier spectra in (16) may also be verified by forming the three \(10\times10\) integer matrices from (15), computing their characteristic polynomials over \(\mathbb Z\), and factoring them over \(\mathbb Q(\sqrt5,\sqrt{17})\).

#### Incidence of arbitrary finite families of projective turns

**Theorem 7 (nested-prefix factorial extension).** Fix \(n\ge3\) and a finite set \(U=\{t_0,t_1,\dots,t_m\}\) of distinct projective turns, with \(t_0=([x],\{i,j\})\). The number
\[
N(U)=|\{O\in\mathcal O_n:U\subseteq O\}|
\]
is determined as follows. Take the orientation at \([x]\) whose last dimension is \(i\) and first dimension is \(j\). For each \(t_h=([y_h],\{a_h,b_h\})\), \(h\ge1\), put \(d_h=x+y_h\). If \([y_h]=[x]\), or if \((d_h)_i=(d_h)_j\), put \(N(U)=0\). Otherwise there is a unique set \(B_h\) among \(\operatorname{supp}(d_h)\) and its complement containing \(j\) and omitting \(i\). If \(|B_h\cap\{a_h,b_h\}|\ne1\), put \(N(U)=0\). Write \(\alpha_h\) for the unique member of \(B_h\cap\{a_h,b_h\}\), and \(\beta_h\) for the other member.

If the distinct sets \(B_h\) cannot be ordered as a strict inclusion chain, put \(N(U)=0\). Otherwise relabel so that
\[
\varnothing=B_0\subsetneq B_1\subsetneq\cdots\subsetneq B_m
\subsetneq B_{m+1}=[n].
\]
Set \(\beta_0=j,\alpha_{m+1}=i\), and \(C_h=B_h\setminus B_{h-1}\) for \(1\le h\le m+1\). Define
\[
F(C;p,q)=
\begin{cases}
1,&|C|=1,\ p=q\in C,\\
(|C|-2)!,&|C|\ge2,\ p\ne q,\ p,q\in C,\\
0,&\text{otherwise}.
\end{cases}
\]
Then
\[
\boxed{N(U)=\prod_{h=1}^{m+1}F(C_h;\beta_{h-1},\alpha_h).}
\tag{18}
\]
For \(m=0\), formula (18) gives \(N(\{t_0\})=(n-2)!\).

**Proof.** Every coherent support containing \(t_0\) has a unique rooted direction order
\[
(j,p_2,\ldots,p_{n-1},i)
\]
whose projective root is \([x]\), whose outgoing dimension is \(j\), and whose incoming dimension is \(i\). This establishes a bijection with permutations of the remaining \(n-2\) dimensions. The projective vertex reached after a proper prefix \(B\) of this order is \([x+\mathbf1_B]\), and every such prefix includes \(j\) and excludes \(i\). The prescribed second vertex \([y_h]\) can therefore occur only at the uniquely selected \(B_h\), which exists precisely when \((d_h)_i\ne(d_h)_j\). At that vertex, the incident direction labels are the final dimension of \(B_h\) and the initial dimension outside \(B_h\). These must be respectively \(\alpha_h,\beta_h\). Distinct prescribed turns cannot occur at the same projective vertex; thus all \(B_h\) must form a strict chain. The intervening blocks \(C_h\) independently permute their dimension labels, with initial member \(\beta_{h-1}\) and terminal member \(\alpha_h\). Their counts are \(F(C_h;\beta_{h-1},\alpha_h)\); multiplying proves (18). \(\square\)

For any legal coloring and \(X_c(O)=T_c(O)/2=\sum_{t\in O}I_t(c)\), this theorem gives every factorial moment:
\[
\boxed{
\mathbb E_O\binom{X_c(O)}k
=\frac1{|\mathcal O_n|}
\sum_{\substack{U\subseteq\mathcal T_n\\|U|=k}}
N(U)\prod_{t\in U}I_t(c).
}
\tag{19}
\]
Here \(\mathcal T_n\) denotes the projective-turn set. In particular, the cubic turn moment is obtained by the \(k=1,2,3\) cases of (19), and every summand is determined by the original edge colors and factorial block multiplicities. This supplies the third-order incidence geometry without a support-by-support expansion.

#### Seven-dimensional spectral calculation

For \(n=7\), the Gram matrix \(A^\top A\) decomposes under Fourier transform in the projective vertex variable into \(21\times21\) blocks \(K_S\), with \(|S|\) even. Writing \(z\) for the characteristic-polynomial variable, the four representative characteristic polynomials are
\[
\begin{aligned}
|S|=0:&\quad z^6(z-840)(z-120)^{14};\\
|S|=2:&\quad z^2(z-120)^4(z-88)^5
 (z^2-480z+20160)(z^2-280z+15360)^4;\\
|S|=4:&\quad z^4(z-312)(z-216)^2(z-120)^9(z-72)
 (z^2-312z+18432)^2;\\
|S|=6:&\quad z^6(z-264)(z-184)^9(z-120)^5.
\end{aligned}
\tag{20}
\]
Each polynomial follows by evaluating (2) on projective vertex differences, Fourier-transforming, and factoring the integer characteristic polynomial. Consequently
\[
\boxed{\lambda_7=240-24\sqrt{65}>0.}
\tag{21}
\]
The nullities sum to \(6+21\cdot2+35\cdot4+7\cdot6=230\), agreeing with (6).

For a legal coloring of \(Q_7\) whose vertex degrees are \(3\) or \(4\), one has \(D_7(r)=24/5\) at every one of the \(64\) projective vertices. Thus (17) specializes to
\[
\boxed{\operatorname{Var}_O(T_c(O))
\ge\frac4{75}(240-24\sqrt{65})\approx2.480310.}
\tag{22}
\]
This inequality is substantially below the variance \(36/5\) exhibited by the balanced coloring in the associated research note, and therefore does not by itself force a two-transition support in dimension seven.


#### A maximally balanced binomial-square energy law

**Theorem 8 (balanced binomial-square turn distribution).** For each integer \(m\ge1\), put \(n=2m+1\) and partition the dimensions \(\{1,\ldots,2m\}=A\sqcup B\), with \(|A|=|B|=m\) and \(1\in B\). Define
\[
c_0(x)=x_1,\qquad c_i(x)=x_0\ (i\in A),\qquad
c_i(x)=1+x_0\ (i\in B).
\tag{23}
\]
Then the coloring is antipodally odd and has color-one vertex degree \(r(x)=m+x_1\). Its cyclic turn-energy distribution is
\[
\boxed{\Pr_{O\in\mathcal O_n}\bigl(T_c(O)=2+4j\bigr)
=\frac{\binom mj^2}{\binom{2m}m}\quad(0\le j\le m).}
\tag{24}
\]
Consequently
\[
\boxed{\mathbb E T_c=n+1,\qquad
\operatorname{Var}(T_c)=\frac{4m^2}{2m-1},\qquad
\Pr(T_c=2)=\binom{2m}m^{-1}.}
\tag{25}
\]

**Proof.** Every \(c_i\) is independent of its own dimension and changes when all vertex bits are complemented. Precisely \(m\) of the \(2m\) nonzero-direction edges have color one at every vertex, so \(r(x)=m+x_1\).

Root a uniform coherent support at its projective edge in direction \(0\), oriented with dimension \(0\) first. Every support has four rooted direction-order representatives with this property, so the resulting rooted orders are uniformly distributed. The remaining \(2m\) dimensions occur in a uniform random order. After traversing direction \(0\), their color word \(w=(w_1,\ldots,w_{2m})\) contains \(m\) zeros and \(m\) ones; all \(\binom{2m}m\) such words are equally likely. The color \(b\) of direction \(0\) is an independent uniform bit, by variation of starting vertex bit \(x_1\). Extend the word to \((b,w_1,\ldots,w_{2m},1-b)\). The number \(X=T_c/2\) of changing projective turns is the number of adjacent changes in this extended word.

Since the endpoints are opposite, \(X=2j+1\) precisely when the extended word has \(j+1\) runs of each color. For fixed \(b\), it contains \(m+1\) occurrences of each bit. The positive run lengths of either color form ordered compositions of \(m+1\) into \(j+1\) parts, counted by \(\binom mj\). Independently choosing both sets of run lengths gives \(\binom mj^2\) words producing \(X=2j+1\), proving (24).

The variable \(J=(T_c-2)/4\) has the hypergeometric distribution of the intersection size of two uniform \(m\)-element subsets of a \(2m\)-element set. Thus \(\mathbb EJ=m/2\) and \(\operatorname{Var}J=m^2/[4(2m-1)]\), proving (25). \(\square\)

The proportion of coherent supports carrying a monochromatic full antipodal geodesic can therefore be as small as
\[
\binom{2m}m^{-1}\sim\frac{\sqrt{\pi m}}{4^m}
\]
while all vertex stars are maximally balanced.


#### Zero-frequency turn spectrum and a dimension-uniform witness certificate

Let \(n\ge3\). For every unordered pair \(P=\{i,j\}\subset[n]\) put
\[
p_P=\mathbb E_{[x]}\mathbf1_{\{c_i(x)\ne c_j(x)\}}.
\]
The expectation ranges over \(2^{n-1}\) projective vertices; because the indicator is antipodally invariant, the same number is obtained by averaging over all cube vertices. Let \(B\) be the \(\binom n2\times n\) unsigned pair–dimension incidence matrix, \(B_{P,i}=\mathbf1_{\{i\in P\}}\). Write \(J\) for the all-ones \(\binom n2\times\binom n2\) matrix.

**Theorem 9 (complete zero-frequency Gram spectrum).** The zero-frequency Fourier block of the projective turn Gram matrix \(A^\top A\) is
\[
\boxed{K_\varnothing=(n-3)!\big((n-2)I-BB^\top+2J\big).}
\tag{26}
\]
Its eigenvalues, with multiplicities, are
\[
\boxed{
n(n-2)(n-3)!\ (1),\quad
0\ (n-1),\quad
(n-2)!\ \left(\frac{n(n-3)}2\right).
}
\tag{27}
\]
The last multiplicity is zero at \(n=3\).

**Proof.** By translation invariance, the matrix entry \(K_\varnothing(P,Q)\) is the total number of coherent supports containing the turn at \([0]\) with dimension pair \(P\) and another turn with dimension pair \(Q\), summed over its projective vertex. The two-turn incidence theorem gives \((n-2)!\) when \(P=Q\), and \((n-3)!\) when \(|P\cap Q|=1\): in the latter case the second vertex is the other endpoint of the shared projective edge.

For disjoint pairs \(P,Q\), orient the first turn with incoming dimension \(i\), outgoing dimension \(j\). A compatible projective second vertex corresponds to a prefix \(D\subset[n]\) with \(j\in D\), \(i\notin D\), and precisely one member of \(Q\) in \(D\). If \(|D|=b\), there are \(2\binom{n-4}{b-2}\) such prefixes, each admitting \((b-2)!(n-b-2)!\) supports. Therefore
\[
K_\varnothing(P,Q)
=2\sum_{b=2}^{n-2}\binom{n-4}{b-2}(b-2)!(n-b-2)!
=2(n-3)!.
\]
For \(n=3\), disjoint pairs do not occur. The three cases yield (26), since \(BB^\top\) has diagonal \(2\), off-diagonal \(1\) for pairs sharing a dimension, and \(0\) otherwise.

Now \(B^\top B=(n-2)I+J_n\), where \(J_n\) is the \(n\times n\) all-ones matrix. The pair-space decomposes orthogonally into constants, vectors \(Ba\) with \(\sum_i a_i=0\), and \((\operatorname{im}B)^\perp\). Formula (26) acts on these subspaces by the three eigenvalues in (27), respectively. \(\square\)

Define
\[
R=\sum_{i<j}p_{ij},\qquad
d_i=\sum_{j\ne i}p_{\min(i,j),\max(i,j)},\qquad
z_i=\frac{d_i-R/(n-1)}{n-2},
\]
and the pair-additivity residual
\[
\mathcal D(c)=\sum_{i<j}(p_{ij}-z_i-z_j)^2.
\tag{28}
\]
Here \(z=(B^\top B)^{-1}B^\top p\), so \(\mathcal D(c)\) is the squared Euclidean distance of \(p\) from \(\operatorname{im}B\).

**Theorem 10 (direction-pair variance and quantitative forcing).** For every legal antipodally odd coloring, writing \(M=2^{n-2}(n-1)!\) and \(\mu=\mathbb E_O T_c(O)\), one has
\[
\boxed{\operatorname{Var}_O(T_c(O))\ge\frac8{n-1}\mathcal D(c).}
\tag{29}
\]
Consequently, with \(p_{\rm good}=\Pr_O(T_c(O)=2)\),
\[
\boxed{
p_{\rm good}\ge
\max\left\{0,\,
\frac{\frac8{n-1}\mathcal D(c)-(2n-\mu)(\mu-6)}
{8(n-1)}
\right\}.}
\tag{30}
\]
In particular, positivity of the displayed numerator forces a monochromatic full antipodal geodesic within the given coloring.

**Proof.** Define \(u_{[x],P}=I_{([x],P)}-\mu/(2n)\). Each support contains \(n\) projective turns, so the support-energy deviation vector equals \(2Au\). Hence
\[
M\operatorname{Var}(T_c)=4\|Au\|^2.
\]
The projective-vertex Fourier transform of \(u\) has constant character coefficient \(p-\bar p\mathbf1\), where \(\bar p=\mu/(2n)\); all other Fourier blocks contribute nonnegatively to \(\|Au\|^2\). By (27) its zero-frequency contribution satisfies
\[
\|Au\|^2\ge 2^{n-1}(n-2)!\mathcal D(c).
\]
Indeed \(p-\bar p\mathbf1\) has no constant-vector component, and its projection onto \((\operatorname{im}B)^\perp\) is precisely the residual vector in (28). Substituting \(M=2^{n-2}(n-1)!\) proves (29).

Every support has \(T_c(O)\in\{2,6,10,\ldots,2n\}\). Therefore the pointwise inequality
\[
(T_c(O)-6)(2n-T_c(O))\ge
-8(n-1)\mathbf1_{\{T_c(O)=2\}}
\]
holds. Taking expectations and expanding gives
\[
\operatorname{Var}(T_c)\le
(2n-\mu)(\mu-6)+8(n-1)p_{\rm good}.
\]
Combining this with (29) proves (30). \(\square\)

**Proposition 11 (strict improvement over the first moment).** There is a legal coloring of \(Q_7\) with \(\mu=289/48>6\) for which (30) certifies at least \(650\) monochromatic coherent supports.

**Construction and verification.** Start from
\[
c_0=c_1=c_2=x_3,\qquad
c_3=c_4=c_5=x_0,\qquad c_6=1+x_0.
\]
Reverse the color on the undirected edge \(\{0,e_3\}\) and on its antipodal edge \(\{\mathbf1,\mathbf1+e_3\}\); leave all other edge colors fixed. The resulting coloring remains legal.

For this coloring, \(p_{ij}=0\) within \(\{0,1,2\}\) and for \(i,j=4,5\); \(p_{ij}=1/2\) when \(i\in\{0,1,2\}\) and \(j\in\{3,4,5,6\}\). The remaining values are
\[
p_{34}=p_{35}=\frac1{32},\qquad
p_{36}=\frac{31}{32},\qquad
p_{46}=p_{56}=1.
\]
Direct substitution in (28), and the vertex-star census, give
\[
\mathcal D(c)=\frac{8753}{7680},\quad
\mathbb E_x S(x)^2=\frac{103}{8},\quad
\mu=\frac{289}{48}.
\]
Therefore
\[
\frac8{n-1}\mathcal D(c)=\frac{8753}{5760}
>\frac{383}{2304}=(14-\mu)(\mu-6).
\]
Formula (30) supplies
\[
\boxed{
p_{\rm good}\ge\frac{5197}{184320}>0.
}
\]
As \(M=23040\), this guarantees at least \(650\) coherent supports with \(T_c=2\). The earlier first-moment certificate requires \(\mu<6\) and therefore gives no guarantee for this coloring. Independent complete enumeration yields the support-energy histogram
\[
(a_2,a_6,a_{10},a_{14})=(3944,15160,3808,128),
\]
confirming the conclusion.

A pure-Python verifier of the legal coloring, rational residual calculation, strict forcing inequality, and support histogram is committed at
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/81e9dadddb6af7c2051d3fe5d8f96f7512707fd6/scripts/nori_zero_mode_spectral_certificate.py .


### Antipodal endpoint absorption and curvature-sensitive shortening

Let \(n\ge3\) and let \(c\) be an arbitrary coloring of the undirected edges of \(Q_n\) by \(0,1\), satisfying \(c(\bar e)=1-c(e)\). A *monochromatic antipodal path* joins \(x\) to \(\bar x=x+\mathbf1\) with all edges of one color. Write \(d_a(u,v)\) for the graph distance in the color-\(a\) subgraph, with value \(+\infty\) when the vertices are disconnected, and set \(d_*(u,v)=\min\{d_0(u,v),d_1(u,v)\}\). The 2026 Wu--Yang monochromatic antipodal path theorem guarantees that at least one such path exists. All shortening statements below are independent of that existence theorem.

#### 1. Antipodal two-color path absorption

**Theorem 1 (antipodal endpoint absorption).** Let \(P=P_1P_2\) be a monochromatic color-\(a\) path from \(x\) to \(\bar x\), with the two consecutive segments meeting at \(z\), of lengths \(p\) and \(q\). If \(Q\) is a monochromatic path of either color from \(z\) to \(\bar x\) with length \(s<q\), then there is a monochromatic color-\(a\) antipodal path of length at most \(p+s<p+q\). The same conclusion holds if \(Q\) goes from \(x\) to \(z\) with length \(s<p\), giving length at most \(q+s\). The conclusion does not assume that the new root equals \(x\).

**Proof.** If the first replacement path \(Q\) has color \(a\), concatenate \(P_1\) and \(Q\) to obtain a color-\(a\) walk \(x\to\bar x\). If \(Q\) has color \(1-a\), its antipodal translate \(\bar Q\) is a color-\(a\) path from \(\bar z\) to \(x\), since the antipodal image of \(Q:z\to\bar x\) has endpoints \(\bar z\to x\). Concatenating \(\bar Q\) with \(P_1:x\to z\) yields a color-\(a\) walk from \(\bar z\) to \(z\), of length \(s+p\). In either case, remove closed subwalks when necessary to obtain a color-\(a\) path of no greater length. The prefix version follows on reversing \(P\), or by applying the same argument to the opposite end. \(\square\)

**Corollary 2 (two-color endpoint rigidity).** Let \(P=(v_0,\ldots,v_L)\) be a shortest monochromatic antipodal path over all roots and both colors. Then for every \(0\le t\le L\),
\[
\boxed{d_*(v_0,v_t)=t,\qquad d_*(v_t,v_L)=L-t.}
\tag{1}
\]
In particular every prefix and suffix of \(P\) is a shortest path between its endpoints simultaneously in its own color and relative to the better of the two monochromatic path distances.

**Proof.** The indicated portions of \(P\) establish the upper inequalities. A strict lower inequality would provide a shorter monochromatic connecting path of one of the two colors, contradicting Theorem 1. \(\square\)

**Corollary 3 (terminal-ear deletion in any defect).** If a monochromatic antipodal path ends with a consecutive three-edge direction word \((i,j,i)\), where \(i\ne j\), then it admits a strictly shorter monochromatic antipodal path, of length smaller by at least two. The same holds for an initial \((i,j,i)\).

**Proof.** The beginning and end of the three-edge suffix differ only in dimension \(j\). The single edge joining them is monochromatic in one of the two colors, has length one, and replaces a suffix of length three by Theorem 1. Reversal handles the prefix. \(\square\)

More generally, if a terminal subpath of length \(q>1\) begins at a vertex adjacent to the endpoint, the entire path can be shortened by at least \(q-1\). Consequently a globally shortest monochromatic antipodal path has no vertex adjacent to either endpoint except the neighboring vertex along the path itself.

#### 2. Curvature of short endpoint shortcuts

For distinct dimensions \(i,j\) define the square curvature
\[
\kappa_{ij}(u)
=c_i(u)+c_j(u+e_i)+c_i(u+e_j)+c_j(u)\pmod2.
\tag{2}
\]
It is the parity of the four edge colors around the square with diagonal endpoints \(u,u+e_i+e_j\).

**Lemma 4 (curved squares provide monochromatic diagonals).** If \(\kappa_{ij}(u)=1\), then precisely one of the two length-two geodesics from \(u\) to \(u+e_i+e_j\) is monochromatic.

**Proof.** The indicators that the orders \(i,j\) and \(j,i\) change color are
\[
s_1=c_i(u)+c_j(u+e_i),\qquad
s_2=c_j(u)+c_i(u+e_j)
\quad(\bmod2).
\]
Their sum is \(\kappa_{ij}(u)\). When it equals one, precisely one \(s_k\) vanishes, which is equivalent to monochromaticity of the corresponding two-edge path. \(\square\)

**Theorem 5 (curvature exclusion along shortest antipodal paths).** If \(P=(v_0,\ldots,v_L)\) is a globally shortest monochromatic antipodal path and \(v_t=v_0+e_i+e_j\) for distinct dimensions \(i,j\), with \(t>2\), then
\[
\boxed{
c_i(v_0)\ne c_j(v_0+e_i),\qquad
c_j(v_0)\ne c_i(v_0+e_j),\qquad
\kappa_{ij}(v_0)=0.
}
\tag{3}
\]
The analogous assertion holds when \(v_t\) is at Hamming distance two from \(v_L\) but the terminal path segment has length greater than two. In particular, nonzero curvature on the corresponding square supplies an explicit strictly shorter monochromatic antipodal path by Theorem 1.

**Proof.** If either of the two length-two geodesics from \(v_0\) to \(v_t\) were monochromatic, its length two would contradict (1), since \(t>2\). Thus both are mixed, giving the first two inequalities. Their indicator sum is the square curvature, so it vanishes. Reversal proves the terminal version. \(\square\)

For a shortest path of length \(n+2\), a terminal three-edge ear \((i,j,i)\) therefore forces a full monochromatic antipodal geodesic in the original coloring: Theorem 1 produces an antipodal monochromatic path of length at most \(n\), while Hamming distance forces its length to equal \(n\). The same argument applies when a length-four prefix or suffix revisits a square diagonal at Hamming distance two and the square has curvature one.

#### 3. A global two-color distance inequality

**Proposition 6 (min-plus antipodal absorption).** If \(L_{\min}(c)\) denotes the minimum length of a monochromatic antipodal path in \(c\), then for every \(x,z\in Q_n\),
\[
\boxed{
L_{\min}(c)\le d_*(x,z)+d_*(z,\bar x)
}
\tag{4}
\]
whenever both distances are finite. Moreover,
\[
\boxed{
L_{\min}(c)=\min_{x,z}\bigl(d_*(x,z)+d_*(z,\bar x)\bigr).
}
\tag{5}
\]

**Proof.** Choose monochromatic shortest paths for the two terms in (4). If their colors agree, concatenate them directly. If they disagree, antipodally translate the path of the opposite color and concatenate as in Theorem 1, now without requiring a pre-existing monochromatic antipodal path. The resulting monochromatic antipodal walk has length equal to the sum of the two distances, and removing loops gives (4). For equality in (5), take any globally shortest monochromatic antipodal path and set \(z\) equal to one of its vertices. Corollary 2 makes the two terms sum to its length. \(\square\)

Since \(\operatorname{dist}_{Q_n}(x,z)+\operatorname{dist}_{Q_n}(z,\bar x)=n\) for every \(z\), formula (5) isolates the accumulated excess of monochromatic path distance over Hamming distance. Theorem 5 gives a curvature-sensitive sufficient condition for reducing this excess in the original coloring.

These theorems supply a dimension-uniform path-shortening operation and constraints on globally shortest witnesses. A proof that every positive-excess minimizer contains an admissible monochromatic endpoint shortcut would establish the full-geodesic NORI1 statement; that remaining assertion is not proved here.
