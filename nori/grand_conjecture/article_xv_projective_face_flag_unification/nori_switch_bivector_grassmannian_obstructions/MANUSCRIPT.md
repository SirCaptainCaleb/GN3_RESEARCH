## Switch Bivectors and Grassmannian Obstructions

##### Endpoint-symmetric affine chambers and toroidal loss of antipodal index

The root-gluing obstruction from earlier in this Article suggests adjoining the exchange that changes a cube geodesic's starting vertex across its *last* dimension, in addition to the usual first-dimension root exchange. This gives a reflection-compatible chamber complex. The resulting topology can be computed: it is a torus, and its free path-reversal cover has vanishing Bockstein. Thus this natural repair eliminates the projective obstruction used in the spherical approach.

Fix \(n\ge3\). Let a cube complete-path chamber be \(g=(x;\pi_1,\ldots,\pi_n)\), with root \(x\in\mathbb F_2^n\) and a permutation \(\pi\) of the dimensions. Write
\[
r_0(x;\pi)=(x+e_{\pi_1};\pi),\qquad
r_n(x;\pi)=(x+e_{\pi_n};\pi),
\]
and, for \(1\le i<n\), let \(r_i\) exchange \(\pi_i\) and \(\pi_{i+1}\) without moving the root. The generators \(r_0,\ldots,r_{n-1}\) are the ordinary type-B chamber exchanges. The additional generator \(r_n\) changes the root across the last dimension. Every chamber still represents a full, dimension-simple antipodal cube geodesic.

**Theorem 1 (the endpoint-symmetric torus).** These \(n+1\) exchanges are the facet adjacencies of a finite regular cell decomposition of the \(n\)-torus
\[
\boxed{\mathbb T_n=(\mathbb R/2\mathbb Z)^n}\tag{1}
\]
into \(2^n n!\) full-dimensional simplicial chambers indexed by \((x;\pi)\). Their rank-two exchange relations are those of the affine Coxeter diagram \(\widetilde C_n\): orders four at the two terminal adjacent pairs, orders three at the internal adjacent pairs, and commuting relations for nonadjacent pairs. In particular the chamber graph is a finite quotient of an affine Coxeter chamber graph.

*Proof.* Represent a generic point of (1) by \(t_i\in(-1,1)\) with \(0<|t_i|<1\) and pairwise distinct absolute values. Record its signs by \(x_i=0\) for \(t_i>0\) and \(x_i=1\) for \(t_i<0\), and sort the magnitudes as
\[
0<|t_{\pi_1}|<|t_{\pi_2}|<\cdots<|t_{\pi_n}|<1.
\tag{2}
\]
For every \((x;\pi)\), the closure of the corresponding region is the image of the standard closed simplex \(0\le s_1\le\cdots\le s_n\le1\), under \(t_{\pi_j}=(-1)^{x_{\pi_j}}s_j\pmod2\). Distinct interior regions are disjoint, and their closures cover the torus, yielding a regular simplicial-cell decomposition. The interiors number \(2^n n!\).

Crossing \(s_1=0\) changes the sign of the smallest-magnitude entry, and hence gives \(r_0\). Crossing \(s_j=s_{j+1}\), \(1\le j<n\), exchanges the adjacent sorted entries and gives \(r_j\). Crossing \(s_n=1\) passes through the identified representatives \(+1\equiv-1\pmod2\), changing the sign of the largest-magnitude entry and giving \(r_n\). These are all the chamber facets.

At a codimension-two intersection of consecutive interior magnitude walls, six chambers meet, giving the braid relation of order three. At either end, a sign wall meets an adjacent magnitude wall with eight surrounding chambers, giving order four. Nonadjacent walls commute. These are the relations of the affine \(\widetilde C_n\) string diagram. \(\square\)

**Theorem 2 (reversal becomes geometric).** Define on the chamber set
\[
A(x;\pi)=(\bar x;\pi),\qquad
R(x;\pi)=(x;\pi^{\mathrm{rev}}),\qquad
J=AR.
\tag{3}
\]
On the torus (1), these are induced by
\[
\boxed{
A(t)=-t,\qquad R(t)=\mathbf1-t,\qquad
J(t)=t+\mathbf1\pmod{2\mathbb Z^n}.}\tag{4}
\]
Consequently \(R\) is a cellular involution, exchanges \(r_0\) with \(r_n\), and conjugates \(r_i\) with \(r_{n-i}\). It has \(2^n\) fixed points on \(\mathbb T_n\). The involution \(J\), which reverses each original full cube geodesic as an undirected path, is free on the entire torus.

*Proof.* Negation flips each sign and preserves the ordering of absolute values, giving \(A\). For \(t_i\in(0,1)\), \(1-t_i\in(0,1)\); for \(t_i\in(-1,0)\), the representative of \(1-t_i\pmod2\) belongs to \((-1,0)\). In both cases its magnitude is \(1-|t_i|\), so the sign remains unchanged and the magnitude order reverses. This gives \(R\). The product is translation by \(-\mathbf1\equiv\mathbf1\pmod2\), giving \(J\).

The conjugation laws follow from the exchanges of the smallest and largest magnitude walls under \(s\mapsto1-s\). The equation \(t=\mathbf1-t\pmod2\) has solutions \(t_i\in\{1/2,3/2\}\) independently, hence \(2^n\) fixed points. Translation by \(\mathbf1\) has no fixed point modulo \(2\mathbb Z^n\), because \(\mathbf1\notin2\mathbb Z^n\). Finally, reversing a full cube geodesic changes its root to its antipode and reverses its dimension order, which is precisely \(J\). \(\square\)

The field transformation is significant. For any antipodally odd undirected cube-edge coloring \(c\), writing \(w(g)\) for its full edge-color word, the identities established earlier in this Article give
\[
w(Ag)=\mathbf1+w(g),\qquad
w(Rg)=\mathbf1+\operatorname{rev}w(g),\qquad
\boxed{w(Jg)=\operatorname{rev}w(g).}\tag{5}
\]
Thus the reflection \(R\), which complements and reverses the word, acquires fixed points in this enlarged source; the free geometric involution \(J\) merely reverses the undirected-edge word.

**Theorem 3 (vanishing primary cover obstruction).** The quotient of the endpoint-symmetric torus by its free involution \(J\) is another \(n\)-torus. Its double-cover class \(\alpha\in H^1(\mathbb T_n/J;\mathbb F_2)\) is the reduction of an integral class, so
\[
\boxed{\beta(\alpha)=0,\qquad \alpha^2=0.}\tag{6}
\]
More generally, \(\alpha^k=0\) for every \(k\ge2\). Hence the Bockstein and cup-power obstructions that force failures of equivariant fillings on the spherical type-B carrier do not force such failures on this free toroidal carrier.

*Proof.* Write \(\Lambda=2\mathbb Z^n+\mathbb Z\mathbf1\). Translation by \(\mathbf1\) defines the quotient
\[
\mathbb T_n/J\cong\mathbb R^n/\Lambda,
\]
which is a torus because \(\Lambda\) is a full-rank lattice. The vectors \(\mathbf1,2e_2,\ldots,2e_n\) form a basis of \(\Lambda\): indeed \(2e_1=2\mathbf1-\sum_{j=2}^n2e_j\). The double cover corresponds to the index-two sublattice \(2\mathbb Z^n\subset\Lambda\). Its covering homomorphism sends the \(\mathbf1\) basis vector to one in \(\mathbb F_2\) and all \(2e_j\) basis vectors to zero. It is the reduction modulo two of the integral homomorphism recording the integer coefficient of \(\mathbf1\). Hence \(\alpha\) lifts to \(H^1(\mathbb T_n/J;\mathbb Z)\), and the integral Bockstein vanishes. The mod-two cohomology ring of a torus is the exterior algebra on degree-one generators, in which every degree-one element squares to zero; this proves the remaining assertions. \(\square\)

**Consequence for a dimension-simple Wu--Yang argument.** Adjoining both endpoint root exchanges resolves the incompatibility of reversal with the ordinary type-B chamber adjacency while keeping every chamber a full dimension-simple geodesic. The natural completion replaces the sphere by a torus. The color-complementing reflection has fixed points, whereas the free path-reversal translation has a covering class with vanishing Bockstein and cup powers. Therefore the spherical equivariant obstruction cannot be transplanted unchanged to this endpoint-symmetric affine complex. A successful common proof requires additional color-sensitive incidence information or a different global source with a nonvanishing index.

##### Resolving affine reversal fixed points into type-A antipodal boundary spheres

The endpoint-symmetric affine chamber torus constructed in the preceding Subsection realizes the cube's color-complementing, order-reversing flag involution \(R(x;\pi)=(x;\pi^{\mathrm{rev}})\) geometrically, but \(R\) has isolated fixed points. Resolving these points yields a **free involution with the full projective cohomological index restored**. The new boundary spheres carry precisely the type-A dimension-order chambers arising at fixed cube roots. This offers an equivariant source in which both root changes and rooted type-A opposition are visible.

Fix \(n\ge3\) and write \(\mathbb T_n=(\mathbb R/2\mathbb Z)^n\), with its endpoint-symmetric affine chamber decomposition. As above, \(R(t)=\mathbf1-t\) and chambers are labeled by root signs \(x\in\mathbb F_2^n\) and magnitude permutations \(\pi\in S_n\).

**Theorem 1 (fixed points and their Coxeter links).** The involution \(R\) has precisely \(2^n\) fixed points, naturally indexed by cube roots \(x\):
\[
\boxed{p_x=\bigl((-1)^{x_i}/2\bigr)_{i=1}^n\pmod{2\mathbb Z^n}.}\tag{1}
\]
Near \(p_x\), let \(u_i=(-1)^{x_i}(t_i-(p_x)_i)\). The local chamber walls are
\[
\boxed{u_i=u_j\qquad(1\le i<j\le n),}\tag{2}
\]
the braid arrangement. The induced decomposition of a sufficiently small linking sphere \(S^{n-1}\) is the suspension of the type-\(A_{n-1}\) Coxeter sphere
\[
\boxed{S\bigl(\{u:\sum_i u_i=0\}\bigr)\cong S^{n-2}.}\tag{3}
\]
The involution acts as \(u\mapsto-u\) on this link, and as permutation reversal on its \(n!\) equatorial Coxeter chambers.

*Proof.* The fixed point equation \(t=\mathbf1-t\pmod2\) is \(2t_i=1\pmod2\) in each component, yielding the representatives \(t_i=\pm1/2\) and hence (1). Each lies away from the sign walls \(|t_i|=0,1\). For \(t\) close to \(p_x\), one has \(|t_i|=1/2+u_i\), so the only chamber walls through \(p_x\) are the equalities (2). The common intersection of these hyperplanes is the diagonal line \(\mathbb R\mathbf1\); in the perpendicular hyperplane \(W=\{u:\sum_i u_i=0\}\), they form the essential type-A braid arrangement. The unit link \(S^{n-1}=S(\mathbb R\mathbf1\oplus W)\) is the suspension of \(S(W)\), and its arrangement decomposition is the suspension of the braid-arrangement sphere. Finally \(R(p_x+\delta)=p_x-\delta\), so its derivative is negation. A chamber labeled by increasing \(u_{\pi_1}<\cdots<u_{\pi_n}\) is carried to the reversed-order chamber. \(\square\)

**Theorem 2 (a free reversal carrier).** Choose disjoint sufficiently small open Euclidean balls \(B_x\) around the points \(p_x\), invariant under \(R\). Define
\[
\boxed{M_n=\mathbb T_n\setminus\bigcup_{x\in\mathbb F_2^n}B_x.}\tag{4}
\]
Then \(M_n\) is a connected compact \(n\)-manifold with \(2^n\) spherical boundary components. The involution \(R\) is free on \(M_n\), acts antipodally on each boundary sphere, and preserves the truncated full-path chamber decomposition. Its quotient \(N_n=M_n/R\) is a compact \(n\)-manifold whose \(2^n\) boundary components are
\[
\boxed{\partial_xN_n\cong\mathbb RP^{n-1}.}\tag{5}
\]
Each \(\partial_xM_n\) contains an invariant type-A Coxeter equator \(S^{n-2}\) with the usual antipodal action and dimension-order chamber labels.

*Proof.* The fixed point set is the finite set (1). Small balls in the flat torus can be chosen disjoint and invariant under the point-reflection \(R\), since it acts as \(-I\) in their centered local charts. All fixed points are removed by (4), making the action free. Every boundary is a small unit sphere on which \(R\) is antipodal; its quotient is \(\mathbb RP^{n-1}\). Removing finitely many disjoint open balls from a connected \(n\)-torus leaves it connected for \(n\ge2\). The chamber walls are linear near the removed centers by (2), so truncating their cells yields a compatible chamber decomposition whose maximal regions retain their original labels \((x;\pi)\). The equator and its opposition are supplied by Theorem 1. \(\square\)

Let \(\alpha\in H^1(N_n;\mathbb F_2)\) classify the connected double cover \(M_n\to N_n\).

**Theorem 3 (full restoration of projective index).** For every \(0\le k\le n-1\),
\[
\boxed{\alpha^k\ne0\ \text{in }H^k(N_n;\mathbb F_2),\qquad
\alpha^n=0.}\tag{6}
\]
Moreover the integral Bockstein is nonzero:
\[
\boxed{\beta(\alpha)\ne0\ \text{in }H^2(N_n;\mathbb Z).}\tag{7}
\]
Consequently there is no \(R\)-equivariant continuous map
\[
\boxed{M_n\longrightarrow S^{n-2}}\tag{8}
\]
with the antipodal action on the target. The highest nonzero power of the covering class is \(n-1\), matching the projective index of a free antipodal \((n-1)\)-sphere.

*Proof.* Restrict the double cover to any boundary component \(\partial_xN_n\cong\mathbb RP^{n-1}\). By Theorem 2, it is the standard antipodal cover \(S^{n-1}\to\mathbb RP^{n-1}\). Thus \(\alpha\) restricts to the canonical generator \(a\in H^1(\mathbb RP^{n-1};\mathbb F_2)\). The ring \(H^*(\mathbb RP^{n-1};\mathbb F_2)=\mathbb F_2[a]/(a^n)\) has \(a^k\ne0\) for \(0\le k\le n-1\). Therefore \(\alpha^k\) is nonzero on \(N_n\) in each of these degrees. Since \(N_n\) is connected, compact, and has nonempty boundary, its absolute top mod-two cohomology vanishes, so \(\alpha^n=0\).

For \(n\ge3\), the Bockstein of \(a\) for \(0\to\mathbb Z\xrightarrow{\times2}\mathbb Z\to\mathbb F_2\to0\) is the nonzero element of \(H^2(\mathbb RP^{n-1};\mathbb Z)\). Naturality of the Bockstein gives \(\beta(\alpha)|_{\partial_xN_n}=\beta(a)\ne0\), establishing (7).

An equivariant map in (8) would induce a quotient map \(N_n\to\mathbb RP^{n-2}\) pulling back the latter's universal degree-one class to \(\alpha\). But the \((n-1)\)-st power of that class vanishes in \(\mathbb RP^{n-2}\), contradicting \(\alpha^{n-1}\ne0\). \(\square\)

**Comparison with the unmodified endpoint torus.** The free translation \(J(t)=t+\mathbf1\), which reverses an original undirected full cube path, has a torus quotient and zero Bockstein, as shown in the preceding Subsection. The color-complementing reversal \(R(t)=\mathbf1-t\), after removing its isolated fixed points, instead has the full nonzero projective index of Theorem 3. These are distinct involutions and their covering classes behave differently.

**Theorem 4 (an explicit odd reference map).** Let \(s(t)=\min_{k\in\mathbb Z}|t-2k|\in[0,1]\) for \(t\in\mathbb R/2\mathbb Z\), and define
\[
\Omega(t)=\bigl(s(t_1)-\tfrac12,\ldots,s(t_n)-\tfrac12\bigr)\in\mathbb R^n.
\]
Then \(\Omega(Rt)=-\Omega(t)\), and its zero set consists precisely of the \(2^n\) fixed points (1). Thus
\[
\boxed{\Phi(t)=\frac{\Omega(t)}{\|\Omega(t)\|}:M_n\longrightarrow S^{n-1}}\tag{9}
\]
is a continuous odd map. On each newly introduced boundary sphere it has degree \(\pm1\), and its restriction to the canonical type-A equator is, after choosing the local signed tangent variables, the identity of \(S^{n-2}\). In particular the obstruction in Theorem 3 is sharp with respect to target sphere dimension: an odd map to \(S^{n-1}\) exists, while one to \(S^{n-2}\) does not.

*Proof.* For every circle component \(s(1-t)=1-s(t)\), hence \(\Omega(Rt)=-\Omega(t)\). The simultaneous equations \(s(t_i)=1/2\) have the points (1) as their solutions. Therefore \(\Omega\) is nonzero on \(M_n\), and its normalization is odd. In local variables near \(p_x\), \(s(t_i)-1/2=u_i\). Its normalized restriction to a centered boundary sphere is consequently the identity in the \(u\)-chart, or a diagonal sign change in the original flat chart; it has degree \(\pm1\). The braid equator \(\sum_i u_i=0\) is preserved by normalization, which acts as the identity there. \(\square\)

**Corollary 5 (signed root-degree cancellation).** Orient each small linking sphere by the outward orientation of its removed ball, using the standard orientation of the flat torus. The reference map \(\Phi\) of Theorem 4 has
\[
\deg\bigl(\Phi|_{\partial B_x}\bigr)=(-1)^{\sum_i x_i},
\qquad
\boxed{\sum_{x\in\mathbb F_2^n}\deg\bigl(\Phi|_{\partial B_x}\bigr)=0.}\tag{10}
\]
*Proof.* In flat variables \(\delta_i=t_i-(p_x)_i\), the differential of \(\Omega\) near \(p_x\) is diagonal with entries \((-1)^{x_i}\). Its determinant sign is \((-1)^{\sum_i x_i}\), which gives the local sphere degree. Summing over roots yields \((1-1)^n=0\). \(\square\)

This cancellation is compatible with the nonzero mod-two covering index of Theorem 3: each individual projective boundary detects the covering class, while the signed degrees of all root-boundary maps sum to zero. A global degree-counting argument must therefore use color-sensitive information beyond the reference map.

**Proof-search consequence and limitations.** The carrier \(M_n\) makes the full collection of cube roots into \(2^n\) type-A equatorial boundary spheres, while all endpoint root exchanges remain represented in its interior chamber geometry. The type-A equators have the same chamber opposition as the spherical carrier for Hamilton orders in ordinary boundary tournaments; the ambient free reversal realizes the complemented-reversal law for chiral cube turns from earlier in this Article. Thus a common dimension-simple chain construction can be sought on an explicit high-index equivariant space that includes the root-gluing exchanges.

Theorem 3 is topological and holds independently of any coloring. To deduce NORI1 or the unrestricted boundary-tournament conjecture, one still needs to construct a color-sensitive equivariant map into a low-dimensional target under the assumption that every complete path has excessive switches. The new equatorial boundary spheres provide a precise place for local rank-exchange data and for the required obstruction to meet; they do not supply that map or prove a one-switch path.

##### Reversal-odd quadratic switch bivectors and switch rank

The two original existence questions admit a common algebraic zero-detection formula in the type-A reflection space. The construction applies uniformly to centered complete-path color words, with the center offset specifying the intrinsic observational radius. It produces an **odd exterior two-form** that vanishes precisely on paths with at most one color switch, and whose rank measures the number of switches.

Let \(n\ge3\), \(s\ge0\), and \(m=n-2s\ge2\). Fix an ordered list \(\pi=(\pi_1,\ldots,\pi_n)\) of distinct symbols, and an associated binary observation word \(w=(w_1,\ldots,w_m)\), centered at positions \(s+1,\ldots,n-s\). Set
\[
W=\{z\in\mathbb R^n:\sum_i z_i=0\},\qquad
Z_r(\pi)=\sum_{h=1}^r e_{\pi_h}-\frac rn\mathbf1
\quad(1\le r<n),
\tag{1}
\]
and \(\delta_j=w_j\oplus w_{j+1}\in\{0,1\}\) for \(1\le j<m\).

**Definition (quadratic switch bivector).** Put
\[
\boxed{\mathcal B_s(\pi,w)=
\sum_{1\le j<k<m}\delta_j\delta_k\,
Z_{j+s}(\pi)\wedge Z_{k+s}(\pi)
\quad\in\Lambda^2W.}\tag{2}
\]

**Theorem 1 (zero and rank detection).** The bivector \(\mathcal B_s\) vanishes if and only if the observation word has at most one switch. If the word has \(r\) switches, the skew-symmetric linear form defined by \(\mathcal B_s\) has rank
\[
\boxed{\operatorname{rank}\mathcal B_s=2\left\lfloor\frac r2\right\rfloor.}\tag{3}
\]
In particular a two-switch word gives a nonzero decomposable bivector, while at least four switches give a form of rank at least four.

*Proof.* The vectors \(Z_1(\pi),\ldots,Z_{n-1}(\pi)\) form a basis of \(W\): pairing with successive simple roots gives
\[
(e_{\pi_i}-e_{\pi_{i+1}})\cdot Z_j=\mathbf1_{\{i=j\}}.
\tag{4}
\]
Consequently the wedge products \(Z_a\wedge Z_b\), \(a<b\), form a basis of \(\Lambda^2W\). The coefficients of (2) are \(\delta_j\delta_k\); all vanish precisely when at most one \(\delta_j\) equals one. This proves the zero condition.

Restrict to the \(r\) basis vectors indexed by switch positions. In that basis the alternating form has matrix \(A_r\) with entries \((A_r)_{ij}=1\) for \(i<j\), \(-1\) for \(i>j\), and zero for \(i=j\). If \(A_rv=0\), successive row differences give \(v_{i+1}=-v_i\). Hence every null vector must have alternating entries \((a,-a,a,-a,\ldots)\). The first row equation forces \(a=0\) when \(r\) is even, while for odd \(r\) it is satisfied by every such alternating vector. Therefore \(\operatorname{rank}A_r=r\) when \(r\) is even and \(r-1\) when \(r\) is odd, proving (3). \(\square\)

**Theorem 2 (reversal oddness).** Suppose a complete-path system has an involution \(R\) sending
\[
(\pi,w)\longmapsto
\bigl(\pi^{\mathrm{rev}},\mathbf1+\operatorname{rev}w\bigr).
\tag{5}
\]
Then
\[
\boxed{\mathcal B_s(R(\pi,w))=-\mathcal B_s(\pi,w).}\tag{6}
\]

*Proof.* A switch at index \(j\) becomes one at index \(m-j\) after reversal. Since \(m=n-2s\), its centered prefix rank \(j+s\) changes to \((m-j)+s=n-(j+s)\). The first \(n-(j+s)\) symbols of \(\pi^{\mathrm{rev}}\) are the complement of the first \(j+s\) symbols of \(\pi\). Consequently
\[
Z_{n-(j+s)}(\pi^{\mathrm{rev}})=-Z_{j+s}(\pi).
\tag{7}
\]
Under reversal, a pair of switch indices \(j<k\) becomes \(m-k<m-j\). Substitution into (2), followed by interchange of the wedge factors, gives
\[
(-Z_{k+s})\wedge(-Z_{j+s})
=-Z_{j+s}\wedge Z_{k+s}.
\]
Every pair contributes its negative, proving (6). \(\square\)

**Corollary 3 (both original problems have the same bivector zero target).**

1. For an antipodally odd edge coloring of \(Q_n\), take a complete geodesic flag \((x;\pi)\), its true length-\(n\) edge-color word \(w\), and \(s=0\). The cube reversal \(R(x;\pi)=(x;\pi^{\mathrm{rev}})\) has word law (5), as proved earlier in this Article. There exists a complete flag with \(\mathcal B_0=0\) if and only if NORI1 holds for that coloring. Indeed \(\mathcal B_0=0\) gives at most one internal switch, and the antipodal root-slide orbit criterion converts any such flag into a monochromatic full geodesic.
2. For an unrestricted reversal-odd boundary 3-tournament on \(n\) vertices, take a Hamilton order \(\pi\), its length-\(n-2\) consecutive triple-color word, and \(s=1\). Reversing the Hamilton order obeys (5). There exists a full flag with \(\mathcal B_1=0\) if and only if the boundary tournament has a Hamilton tight path with at most one switch.

Thus the same formula (2), the same reversal representation (6), and the same zero criterion describe both full unrestricted existence problems. The observation offset is determined by the centered window: one edge-dimension position in the cube, versus a triple centered at its middle vertex for the boundary tournament.

**Theorem 4 (universal rational bivector contraction).** Fix \(n\ge3\), let \(\vartheta=2^{1/n}\), and set
\[
u_i=\vartheta^{i-1}-\frac1n\sum_{h=1}^n\vartheta^{h-1}
\quad(1\le i\le n),\qquad u\in W.
\tag{8}
\]
Using the standard inner product to contract bivectors, the map \(\mathcal I_u:\Lambda^2W\to W\), \(\Xi\mapsto\iota_u\Xi\), obeys
\[
\boxed{\mathcal I_u(\Xi)\ne0
\quad\text{for every nonzero }\Xi\in\Lambda^2(W\cap\mathbb Q^n).}\tag{9}
\]
Consequently, for the switch bivector \(\mathcal B_s\),
\[
\boxed{\mathcal V_s=\iota_u\mathcal B_s\in W
\quad\text{vanishes precisely on words with at most one switch},}
\tag{10}
\]
and under the reversal law (5) it satisfies \(\mathcal V_s(Rg)=-\mathcal V_s(g)\).

*Proof.* Represent a rational bivector \(\Xi\) by a skew-symmetric matrix \(A\) with rational entries. Since both of its wedge factors lie in \(W\), one has \(A\mathbf1=0\). Therefore \(Au=A(1,\vartheta,\ldots,\vartheta^{n-1})^{\mathsf T}\). The polynomial \(X^n-2\) is irreducible over \(\mathbb Q\) by Eisenstein's criterion at the prime two. Hence \(1,\vartheta,\ldots,\vartheta^{n-1}\) are linearly independent over \(\mathbb Q\). If \(Au=0\), every row of \(A\) gives a rational relation among these numbers and must vanish. Thus \(A=0\), proving (9), with the harmless convention of the sign of interior contraction. The vectors \(Z_j\) have rational entries, so \(\mathcal B_s\) is rational. Theorem 1 now gives (10), and Theorem 2 gives its reversal law. \(\square\)

Theorem 4 provides a **single fixed real \((n-1)\)-dimensional target** for odd switch detection on all complete paths, for every coloring, without losing the bivector zero criterion. For the free punctured-torus reflection carrier of the preceding Subsection, \(W\setminus\{0\}\simeq S^{n-2}\) is precisely the forbidden equivariant target dimension. The unresolved work is the extension of these odd vectors from complete-path chambers over root-changing and rank-two cells. Their nonvanishing on a discrete chamber set supplies no continuity or filling by itself.

**Scope and obstruction.** All four theorems are unconditional algebraic statements for any centered reversal word system. Their zero-detection property does not force a zero: reversal-odd words on unrelated complete flags can all have many switches. Theorem 4 removes the ambient target-dimension barrier **at the finite set of complete-path chambers**. It supplies no continuous extension on the source chamber complex. For the punctured affine cube carrier, a nowhere-zero equivariant extension into \(W\) would contradict the nonzero covering index from the preceding Subsection and thereby prove NORI1. For the boundary type-A sphere, one must additionally reduce the target by one real dimension to obtain an analogous contradiction; generic projections retain nonvanishing on finite chamber sets, yet compatible higher-cell fillings are unproved. The central open step for both problems is coherent color-sensitive continuation across all local exchanges, respecting the original projective incidence descent and complete-path support.

##### Antiparallel switch-wedge exchanges and the endpoint dichotomy

The quadratic switch-bivector from the preceding Subsection can be replaced by a decomposable extreme-switch wedge. Its comparison under adjacent rank exchanges has a sharp algebraic classification. This yields an unconditional one-skeleton compatibility theorem for arbitrary reversal-odd boundary triple colorings and all but two cube exchange ranks. Importantly, the cube's root-changing rank exchange is compatible even when its cyclic variation jump is large.

###### Extreme-switch wedge and opposition

Let \(n\ge3\), \(s\in\{0,1\}\), \(m=n-2s\ge3\), and let \(\pi\) be an order of \(n\) distinct symbols. Put \(W=\{z\in\mathbb R^n:\sum_i z_i=0\}\) and
\[
Z_0(\pi)=Z_n(\pi)=0,\quad
Z_j(\pi)=\sum_{h=1}^j e_{\pi_h}-\frac jn\mathbf1
\quad(1\le j<n).
\]
For a binary word \(w\) of length \(m\), let \(a(w)\) and \(b(w)\) be the first and last switch positions when at least two switches occur. Define
\[
\boxed{E_s(\pi,w)=
Z_{a(w)+s}(\pi)\wedge Z_{b(w)+s}(\pi)\in\Lambda^2W,}
\tag{1}
\]
and set \(E_s=0\) when the word has at most one switch. The prefix vectors \(Z_1,\ldots,Z_{n-1}\) form a basis of \(W\), so
\[
\boxed{E_s=0\iff\operatorname{sw}(w)\le1.}\tag{2}
\]
If reversal sends \((\pi,w)\) to \((\pi^{\rm rev},\mathbf1+\operatorname{rev}w)\), then
\[
\boxed{E_s(Rg)=-E_s(g).}\tag{3}
\]
Indeed the switch interval endpoints exchange under reversal, the centered prefix \(Z_j\) becomes \(-Z_{n-j}\), and wedge factor order reverses.

###### Algebraic classification of adjacent exchanges

Let \(\pi'=\pi s_i\) exchange consecutive entries in positions \(i,i+1\). All centered prefixes except the \(i\)-th remain unchanged, and
\[
\boxed{Z_i(\pi')=Z_{i-1}(\pi)+Z_{i+1}(\pi)-Z_i(\pi).}\tag{4}
\]

**Theorem 1 (only terminal pairs can be antiparallel).** Choose arbitrary index pairs \(1\le a<b<n\), \(1\le a'<b'<n\), and write
\[
U=Z_a(\pi)\wedge Z_b(\pi),\quad
U'=Z_{a'}(\pi')\wedge Z_{b'}(\pi').
\]
Then \(U'\) is a negative real multiple of \(U\) if and only if one of these situations holds:
\[
\boxed{
\begin{array}{c|c|c}
i&(a,b)&(a',b')\\ \hline
1&(1,2)&(1,2)\\
n-1&(n-2,n-1)&(n-2,n-1).
\end{array}}
\tag{5}
\]
In both situations \(U'=-U\). For every \(2\le i\le n-2\), antiparallelity is impossible for all choices of the two index pairs.

*Proof.* Work in the exterior basis \(Z_j(\pi)\wedge Z_k(\pi)\), \(j<k\). The first bivector \(U\) is a single positive basis vector. If neither of \(a',b'\) equals \(i\), the second is also a positive basis vector and hence cannot be a negative multiple of \(U\).

Suppose the second pair contains \(i\). By (4), its wedge expression is the sum of up to three basis terms coming from \(Z_{i-1},Z_{i+1},-Z_i\). If \(2\le i\le n-2\), the first and second neighboring prefix vectors are nonzero and distinct. Wedging with an index other than \(i\) gives at least two nonzero distinct exterior basis terms, including when the other index is \(i-1\) or \(i+1\). Thus it cannot be collinear with \(U\). For \(i=1\), the only possibility of a single negative basis term is the pair \((a',b')=(1,2)\), giving \((Z_2-Z_1)\wedge Z_2=-Z_1\wedge Z_2\). For \(i=n-1\), the symmetric possibility is \((a',b')=(n-2,n-1)\), giving \(Z_{n-2}\wedge(Z_{n-2}-Z_{n-1})=-Z_{n-2}\wedge Z_{n-1}\). Matching with the first positive basis vector forces the index pairs in (5). \(\square\)

**Corollary 2 (boundary-tournament exchange compatibility).** For \(n\ge5\), let \(b\) be an arbitrary reversal-odd boundary 3-tournament on \(n\) vertices. Suppose two Hamilton orders \(g,g'\) differ by an adjacent transposition and both have at least two triple-word switches. Their extreme-switch bivectors \(E_1(g),E_1(g')\) are never antiparallel.

*Proof.* The triple-color word has length \(n-2\), so the switch prefix indices \(a+1,b+1\) always lie in \(\{2,\ldots,n-2\}\). Neither terminal possibility (5) can arise. No property beyond the existence of those full words is required. \(\square\)

**Corollary 3 (cube root exchanges are compatible).** For an arbitrary antipodally odd cube-edge coloring, two full geodesic flags related by the root-changing type-B exchange \(r_0(x;\pi)=(x+e_{\pi_1};\pi)\), and having at least two internal switches each, have non-antiparallel extreme-switch bivectors \(E_0\). The same holds for the added last-dimension root exchange \(r_n(x;\pi)=(x+e_{\pi_n};\pi)\) in the endpoint-symmetric affine chamber geometry. For neighboring dimension orders, antiparallelity is possible only at rank \(i=1\) or \(i=n-1\), and then only with consecutive switches at the corresponding pair of endpoint positions.

*Proof.* Either root exchange leaves \(\pi\) unchanged. Both wedges are positive elements of the same exterior basis, so they cannot be antiparallel. For exchanges changing the dimension order, apply Theorem 1 with \(s=0\). \(\square\)

**Proposition 4 (terminal exceptions occur with legal flat-square colorings).** For every \(n\ge3\), a legal antipodally odd cube-edge coloring realizes antiparallel wedges across an adjacent exchange of the first two dimensions. Take the full orders \(\pi=(1,2,3,\ldots,n)\) and \(\pi'=(2,1,3,\ldots,n)\), both rooted at zero. Prescribe color words
\[
w(0;\pi)=w(0;\pi')=(0,1,0,\ldots,0).
\]
These prescriptions agree on the common suffix and assign the first square's two routes the same successive colors \(0,1\). All prescribed edges lie in distinct antipodal edge orbits, except where the two paths share an edge with identical prescribed color, so the prescriptions extend to a legal antipodally odd coloring. Both have switches at positions \(1,2\), and (4) gives
\[
E_0(0;\pi')=-E_0(0;\pi).
\]
The initial square's four edge colors are \(0,1,1,0\) in cyclic order, whose square curvature is zero. Thus even square flatness cannot exclude this seam. The final-two-dimension exception follows by the symmetric construction at the terminal square.

###### A universally chosen lower-dimensional edge extension

**Theorem 5 (generic projection and equivariant one-skeleton map).** Fix \(n\ge5\). There is a linear map
\[
L:\Lambda^2W\longrightarrow\mathbb R^{n-2}
\tag{6}
\]
chosen independently of the boundary-tournament coloring, such that for *every* reversal-odd tournament in which each Hamilton order has at least two switches, the normalized labels
\[
\boxed{g\longmapsto \frac{L(E_1(g))}{\|L(E_1(g))\|}\in S^{n-3}}
\tag{7}
\]
extend by normalized straight-line interpolation over all adjacent-transposition edges in the dual type-A Coxeter complex, equivariantly under order reversal.

*Proof.* As \(\pi\) varies and \(a<b\) vary over the allowed prefix indices, the set \(\mathcal S=\{Z_{a+1}(\pi)\wedge Z_{b+1}(\pi)\}\) is finite. Choose a linear map \(L\) that takes every member of \(\mathcal S\) to a nonzero vector and takes every linearly independent pair of members to linearly independent vectors. Such maps form a nonempty Zariski-open subset: for each specified nonzero vector or independent pair, the unwanted rank-drop is a proper algebraic condition on linear maps to a real vector space of dimension at least two, and there are finitely many conditions. By Corollary 2, labels of adjacent flags are never on negative rays in \(\Lambda^2W\). Under the chosen projection their images also are never on negative rays, since noncollinear labels remain noncollinear and positive proportional labels remain positive proportional. Their straight-line segments avoid the origin. Normalize these segments and apply (3); reversal maps edges to edges and negates their endpoint labels, so the extension is equivariant. \(\square\)

**Status and obstruction.** Theorem 5 proves one-skeleton compatibility in the complete unrestricted boundary class under the hypothetical no-good-path assumption, while Corollary 3 resolves the cube's root-changing exchanges at this linear level. Higher-dimensional face fillings are still open. The examples in Proposition 4 demonstrate that normalized *straight-line* interpolation across all cube rank exchanges fails without endpoint corrections. Since the target sphere \(S^{n-3}\) is path-connected, the endpoint defects may be bypassed on edges; coherently filling rank-two and higher residues while preserving coloring remains the substantive equivariant obstruction.

##### Sharp convex carriers for centered switch wedges

Let \(n\ge2s+3\), \(s\ge0\), and \(W=\{z\in\mathbb R^n:\sum_i z_i=0\}\). For an ordering \(\pi\) of \([n]\), set
\[
Z_j(\pi)=\sum_{h=1}^j e_{\pi_h}-\frac jn\mathbf1.
\]
The permissible prefix ranks for the switches of a centered word of length \(n-2s\) form \(I_s=\{s+1,\ldots,n-s-1\}\).

An ordered partition \(\mathcal P=B_1|\cdots|B_k\), \(k\ge2\), specifies a flag residue whose orders refine the block order. Define its universal extreme-switch carrier
\[
\mathscr E_s(\mathcal P)=
\{Z_p(\pi)\wedge Z_q(\pi):\pi\text{ refines }\mathcal P,\quad
p<q,\ p,q\in I_s\}.
\tag{1}
\]

**Theorem 1 (sharp endpoint-block criterion).**
\[
\boxed{0\notin\operatorname{conv}\mathscr E_s(\mathcal P)
\iff |B_1|\le s+1\text{ and }|B_k|\le s+1.}
\tag{2}
\]
In the positive case a single real linear functional separates all wedges from zero. In the negative case a uniform average of wedges from the residue equals zero.

*Proof.* Suppose the two endpoint blocks have at most \(s+1\) elements, and choose \(a\in B_1\), \(c\in B_k\). For every permissible \(p<q\), all of \(B_1\) belongs to both prefixes and none of \(B_k\) belongs to either prefix. The \((a,c)\)-skew entry of the wedge is
\[
\boxed{(Z_p)_a(Z_q)_c-(Z_p)_c(Z_q)_a=(p-q)/n<0.}
\tag{3}
\]
Thus every wedge in the carrier lies in the same strict open halfspace.

Now suppose \(t=|B_1|\ge s+2\). Set \(p=s+1\), \(q=s+2\), both no greater than \(t\), and fix the orders of all later blocks. Average \(Z_p\wedge Z_q\) over all permutations of the first block \(A=B_1\). Write \(u_A=\sum_{a\in A}e_a\) and \(Z_A=u_A-(t/n)\mathbf1\). For \(r\le t\), define
\[
U_r=\sum_{h=1}^r e_{\pi_h}-\frac rt u_A,\qquad
Z_r=\frac rt Z_A+U_r.
\]
The mean of \(U_r\) over all permutations of \(A\) is zero. Hence the mean wedge is \(\mathbb E(U_p\wedge U_q)\). For every two distinct labels \(a,b\in A\), their transposition reverses the \((a,b)\)-skew entry of this latter wedge and preserves the uniform distribution. Every skew entry therefore has mean zero. Consequently
\[
\boxed{\frac1{t!}\sum_{\pi|_A\in S_A}Z_p(\pi)\wedge Z_q(\pi)=0,}
\tag{4}
\]
placing zero in the convex hull. If the final block has size at least \(s+2\), reverse all orders and replace \((p,q)\) with \((n-q,n-p)\). Since \(I_s\) is reversal-stable and \(Z_j(\pi^{\rm rev})=-Z_{n-j}(\pi)\), the same zero average applies. This proves (2). \(\square\)

**Corollary 2 (canonical high-dimensional fillings).** Suppose every complete path in a rank-exchange residue has at least two switches, and assign each flag the decomposable bivector determined by its first and last switch ranks, as in the preceding Subsection. Whenever the endpoint block sizes satisfy (2), all these flag labels belong to a common open halfspace. Affine interpolation over any common simplicial refinement of the dual cell therefore produces a nowhere-zero map, canonically and consistently over shared faces. The resulting filling is independent of any additional color compatibility assumptions.

**Corollary 3 (rank-two specializations).** For cube edge words \(s=0\), this convex filling applies to residues with singleton first and last dimension blocks. For unrestricted reversal-odd boundary triple words \(s=1\), it applies to residues with first and last vertex blocks of size at most two. Hence *every* commuting-square residue of boundary Hamilton orders admits such a filling, and every braid-hexagon residue does except those permuting the first three or last three vertices.

*Proof.* Dual two-cells of the type-A flag sphere come from either a three-symbol block or two disjoint two-symbol blocks, with the remaining blocks singleton. Apply (2). \(\square\)

**Limitations.** The zero-average half of Theorem 1 is an obstruction to a *universal* convex carrier containing all possible switch pairs. A particular legal coloring may disallow the simultaneous switch-pair choices used in (4). The positive half is unconditional for every legal coloring and every selection of switch pairs. Thus (2) localizes the remaining convex-filling question to residues with more than \(s+1\) freely permutable endpoint symbols. The argument preserves full Hamilton and dimension-simple witnesses and makes no general one-switch claim.

##### Boundary reversal oddness fills every rank-two switch-wedge residue

Let \(n\ge5\) and let \(b\) be an arbitrary reversal-odd binary coloring of ordered distinct triples. For a Hamilton order \(\pi\) with first and last switch positions \(j<k\), put \(E(\pi)=Z_{j+1}(\pi)\wedge Z_{k+1}(\pi)\).

**Theorem 1 (rank-two convex fillings).** Let \(D\) be any dual type-A Coxeter rank-two cell (commuting square or braid hexagon). If every Hamilton order at its vertices has at least two switches, then
\[
\boxed{0\notin\operatorname{conv}\{E(\pi):\pi\in V(D)\}.}
\tag{1}
\]

*Proof.* The sharp universal carrier theorem handles every commuting square and every braid hexagon other than permutations of the first or last three symbols. Global reversal negates the wedges, so consider the six orders obtained by permuting \(a,b,c\) before a fixed suffix \(d,e,\ldots,z\).

Let \(A=\{a,b,c\}\). On exterior matrices define \(\ell(U)=\sum_{t\in A}U_{t,z}\). For every permitted switch-prefix pair \(2\le p<q\le n-2\),
\[
\boxed{\ell(Z_p\wedge Z_q)=
\frac{p\min(q,3)-q\min(p,3)}n\le0,}
\tag{2}
\]
with equality only for \(p=2,q=3\). Suppose zero belongs to the convex hull in (1). In any zero convex combination, positive weights can occur only on flags with switch-prefix pair \((2,3)\). Their words have the form \((C,1-C,C,C,\ldots,C)\). The associated wedges depend only on the third entry of the first three symbols. Write them \(U_a,U_b,U_c\). They satisfy \(U_a+U_b+U_c=0\) and are pairwise noncollinear. Therefore a zero convex combination needs at least one flag with each third entry.

For \(n\ge6\), the fourth and subsequent color bits are common to all six flags, so the three selected words share a tail color \(C\). Their first triples all have color \(C\). Reversal oddness forbids selecting a triple together with its reverse. The three selected permutations must consequently form one of the two directed three-cycles \((a,b,c),(b,c,a),(c,a,b)\), or its reverse cycle. The other three permutations have first triple color \(1-C\). Since the selected permutations have all three possible third entries, every third and subsequent bit in all six flags is \(C\). Each of the three remaining words therefore has form \((1-C,t,C,C,\ldots,C)\) and hence just one switch, a contradiction.

For \(n=5\), every word has length three. If all six flags had two switches, their words would alternate. Writing \(C_t=b(t,d,e)\), this would force \(b(x,y,t)=C_t\) for every permutation \((x,y,t)\) of \(a,b,c\). Reversal oddness then forces \(C_a+C_b=C_b+C_c=C_c+C_a=1\) in \(\mathbb F_2\), impossible. Thus the final terminal-hexagon case is vacuous. \(\square\)

**Corollary 2 (full equivariant two-skeleton extension).** Suppose \(n\ge6\) and every Hamilton order has at least two switches. On the dual type-A Coxeter sphere \(X\), the labels \(E(\pi)\) extend to an antipodally equivariant continuous map
\[
\boxed{X^{(2)}\longrightarrow\Lambda^2W\setminus\{0\}.}
\tag{3}
\]
Indeed, assign each cell barycenter the arithmetic mean of its flag-vertex labels and interpolate affinely on a common barycentric triangulation of the two-skeleton. Theorem 1 ensures that the entire convex hull of every two-cell misses zero. Opposite flags have negative labels and opposite faces have corresponding averages, yielding equivariance.

**Scope.** The result handles every two-dimensional rank-exchange residue for the unrestricted boundary class under the hypothetical no-good-path condition. It preserves complete Hamilton orders. Higher-dimensional extensions and compression to a target of sufficiently small dimension remain open.

##### Oriented switch-plane charts and the Grassmannian index obstruction

Let \(W=\{z\in\mathbb R^n:\sum z_i=0\}\), \(n\ge5\), and let \(\mathcal G=\widetilde{\mathrm{Gr}}_2(W)\) be the space of oriented two-planes, with its free orientation-reversing involution \(J\). A full centered color word with first and last switch-prefix ranks \(p<q\) determines the oriented plane \(\Psi=(\mathrm{span}\{Z_p,Z_q\}, Z_p\wedge Z_q)\). This is defined whenever there are two switches. Under the complemented-reversal law for either original problem, \(\Psi(Rg)=J\Psi(g)\).

**Lemma 1 (decomposable separating charts).** For independent covectors \(u,v\in W^*\), the subset of oriented planes \(\Pi\) with positive Pluecker evaluation \((u\wedge v)(\Pi)>0\) is contractible, homeomorphic to \(\mathbb R^{2(n-3)}\). The negative subset is also contractible.

*Proof.* Split \(W=H\oplus\ker(u,v)\), with \(H\) two-dimensional and the covectors independent on \(H\). Each such plane is the graph of a unique linear map \(H\to\ker(u,v)\), with the orientation determined by its projection to \(H\). This is a vector-space chart. \(\square\)

**Theorem 2 (boundary rank-two Grassmannian charts).** For every unrestricted reversal-odd boundary triple coloring, every rank-two dual type-A Coxeter cell whose Hamilton flags all have at least two switches has its flag planes \(\Psi\) contained in one contractible chart from Lemma 1.

*Proof.* For each commuting square or braid residue whose first and last ordered blocks have size at most two, the previous universal convex-carrier theorem gives a negative decomposable separator \(e_a^*\wedge e_c^*\), with \(a\) in the first block and \(c\) in the last.

A terminal braid residue with a variable first three-symbol set \(A=\{a,b,c\}\) needs a weighted separator. Fix the final symbol \(z\), choose positive weights \(\lambda_t\) on \(A\) summing to one, and put \(u=\sum_{t\in A}\lambda_t e_t^*\). If the first and last switch-prefix ranks are \(p<q\), then \((u\wedge e_z^*)(Z_p\wedge Z_q)=(p-q)/n<0\) when \(p\ge3\). When \(p=2\), write \(t\) for the third symbol of the first three, and calculate
\[
\boxed{(u\wedge e_z^*)(Z_2\wedge Z_q)
=\frac{q\lambda_t-(q-2)}n.}\tag{1}
\]
For \(q=3\), negativity requires \(\lambda_t<1/3\); for \(q\ge4\), it suffices that \(\lambda_t<1/2\). The terminal-braid theorem from the preceding Subsection proves that, if all six flags have at least two switches, the pair \((p,q)=(2,3)\) cannot occur with each of the three possible third symbols. Thus at most two weights must be below \(1/3\), while the others need only be below \(1/2\). These strict bounds admit positive weights totaling one because their upper bounds sum to at least \(1/3+1/3+1/2>1\). Equation (1) then makes \(u\wedge e_z^*\) negative on all six planes. Reversing all Hamilton orders handles a final-three-symbol braid residue. For \(n=5\), the bad-hexagon hypothesis is already impossible by the previous theorem. \(\square\)

**Corollary 3 (equivariant two-skeleton realization).** Under the hypothetical absence of a one-switch Hamilton order for a reversal-odd boundary coloring on \(n\ge6\) vertices, the flag-plane assignment \(\Psi\) extends equivariantly over the full two-skeleton of the dual type-A Coxeter sphere with target \(\mathcal G\).

*Proof.* The oriented two-plane Grassmannian is simply connected for \(\dim W\ge4\), as follows from the standard fibration \(SO(2)\times SO(n-3)\to SO(n-1)\to\mathcal G\). Choose paths on involutive pairs of dual edges and use simple connectivity to fill each two-cell, choosing fillings in opposite pairs. Theorem 2 strengthens this abstract extension by providing a contractible color-sensitive chart for the vertices of every two-cell. \(\square\)

**Theorem 4 (an infinite Grassmannian cohomological obstruction).** Suppose \(m=2^r\ge4\). On the unoriented Grassmannian \(\operatorname{Gr}_2(\mathbb R^m)\), the orientation-cover class \(\omega=w_1(\gamma_2)\) satisfies
\[
\boxed{\omega^{m-1}=0.}\tag{2}
\]
Consequently, for \(n=m+1\), no antipodally equivariant map exists from the type-A Coxeter sphere \(S^{n-2}\) into \(\widetilde{\operatorname{Gr}}_2(\mathbb R^{n-1})\). Likewise, no equivariant map exists from the free punctured affine reversal carrier \(M_n\) constructed earlier in this Article into that oriented Grassmannian.

*Proof.* Set \(x=w_1(\gamma_2)\), \(y=w_2(\gamma_2)\), and expand the formal inverse \((1+xt+yt^2)^{-1}=\sum_{j\ge0}h_jt^j\). The orthogonal complement of the tautological bundle has rank \(m-2\), so the Whitney sum relation gives \(h_{m-1}=0\). Over \(\mathbb F_2\),
\[
h_j=\sum_{k=0}^{\lfloor j/2\rfloor}
\binom{j-k}{k}x^{j-2k}y^k.
\]
For \(j=m-1=2^r-1\), all terms with \(k\ge1\) vanish modulo two. Indeed the binary digits of \(j-k\) and \(k\) are complementary, so Lucas's criterion makes \(\binom{j-k}{k}\) even. Therefore \(h_{m-1}=x^{m-1}\), proving (2).

The type-A sphere quotient is \(\mathbb RP^{m-1}\), whose covering class \(\alpha\) has \(\alpha^{m-1}\ne0\). A hypothetical equivariant map would induce a quotient map pulling \(\omega\) back to \(\alpha\), contradicting (2). The quotient of \(M_n\) contains projective boundary components \(\mathbb RP^m\) on which its covering class has nonzero \((m-1)\)-st power, giving the same contradiction. \(\square\)

The Grassmannian cohomology presentation is classical; see https://link.springer.com/article/10.1007/s00209-024-03556-y.

**Research consequence.** The oriented switch-plane target is common to both original full-path questions. At dimensions \(n=2^r+1\), its covering class has insufficient index for an equivariant map from either source. For unrestricted boundary tournaments, the no-good-path assumption already supplies an equivariant map on the entire two-skeleton. The next obstruction lies in extending over three-dimensional cells, where \(\pi_2(\mathcal G)\) can carry nonzero classes. For cubes, the terminal braid counterexample still prevents a purely local universal chart. The global extensions, and the original existence conjectures, remain open.

##### Rank-three convex obstruction for unrestricted boundary tournaments

**Theorem.** For every integer n>=6, there is a reversal-odd binary coloring b of all ordered distinct triples, and a three-dimensional dual type-A Coxeter cell D, such that every Hamilton order in D has at least two triple-color switches, yet the convex hull of their first/last-switch bivectors contains zero. Two nonzero labels are negatives.

*Construction and proof.* For n=6 take D to be the 24 permutations (a,b,c,d,4,5), with (a,b,c,d) ranging over the four-element set {0,1,2,3}. This is the rank-three residue corresponding to the ordered partition {0,1,2,3}|{4}|{5}. Specify b(a,h,c) with a<c using these rows, indexed by h; the ten entries in each row follow lexicographic order on pairs {a,c} excluding h:
[
egin{array}{c|c}
h&	ext{ten bits}\hline
0&1000000000\
1&0010010100\
2&0000100000\
3&0110110100\
4&0001000010\
5&0000000000
end{array}
]
Define b(c,h,a)=1-b(a,h,c). The full four-bit words of these 24 complete Hamilton paths are:
[
egin{array}{c|c@{quad}c|c@{quad}c|c@{quad}c|c}
abcd&w&abcd&w&abcd&w&abcd&w\hline
0123&0110&0132&0101&0213&0010&0231&0010\
0312&0101&0321&1010&1023&1010&1032&0101\
1203&1010&1230&1001&1302&1101&1320&1101\
2013&0010&2031&0010&2103&1010&2130&0101\
2301&0110&2310&0101&3012&1001&3021&1010\
3102&1101&3120&1101&3201&1010&3210&0101
end{array}
]
Every word is among {0010,0101,0110,1001,1010,1101}, all having two or three switches. The orders pi=(0,1,2,3,4,5) and pi'=(2,3,0,1,4,5) both have word 0110; their first/last switch positions are 1 and 3. Define centered prefixes Z_j(pi)=sum_{h<=j}e_{pi_h}-(j/n)1. Their extreme-switch bivectors are E(pi)=Z_2(pi) wedge Z_4(pi) and E(pi')=Z_2(pi') wedge Z_4(pi'). As the first four symbols agree as a set, and the first two symbols are complementary within that set, Z_4(pi')=Z_4(pi) and Z_2(pi')=Z_4(pi)-Z_2(pi). Therefore
[
oxed{E(pi')=-E(pi)
e0,quad (E(pi)+E(pi'))/2=0.}
]
The bivectors are nonzero because centered prefix vectors of distinct ranks are linearly independent.

For n>6 append the fixed suffix 6,7,...,n-1. Keep the six-symbol coloring above, set b(j,j+1,j+2)=0 for all j>=4, and extend remaining triples arbitrarily under reversal oddness. Every four-bit word acquires a zero tail, so it retains at least its existing two switches. The two special words are 011 followed by n-5 zeros, retaining switches at 1 and 3 and the same centered-prefix wedge identity. This proves the theorem for all n>=6.

**Consequences.** The theorem shows that convex hull avoidance on every rank-two residue, established previously for unrestricted reversal-odd boundary tournaments, cannot be extended to rank-three residues using only reversal oddness and the absence of a favorable flag. Barycentric affine filling of the switch-wedge labels fails on D. The construction concerns only one residue; favorable full Hamilton orders can exist elsewhere. It does not refute the original conjecture. It does not rule out a nonconvex continuous filling: the target of nonzero bivectors has the homotopy type of S^{binomial(n-1,2)-1}, whose second homotopy group is zero for n>=6.

##### Tetrahedral parity and a sharp rank-three convex obstruction

**Theorem 1 (tetrahedral rank-three obstruction).** For every \(n\ge6\) there is an unrestricted reversal-odd boundary triple coloring and a rank-three dual type-A cell \(D\) with 24 Hamilton-order flags such that every flag has at least two switches, every flag has first and last switch-prefix ranks \((2,4)\), and
\[
\boxed{\sum_{\pi\in V(D)}Z_2(\pi)\wedge Z_4(\pi)=0.}\tag{1}
\]
In particular the nonzero flag wedges have zero in their convex hull, so the color-sensitive rank-two convex-filling theorem cannot be extended to all rank-three cells.

*Proof.* Select a four-element set \(A=\{a,b,c,d\}\), fix a suffix \(e,f,\ldots\) of the remaining \(n-4\) symbols, and let \(D\) consist of the 24 orders \((v_1,v_2,v_3,v_4,e,f,\ldots)\) as the first four symbols are permuted.

Fix an orientation of \(A\). For every ordered triple \((x,y,z)\) drawn from \(A\), let \(t\) be the omitted fourth symbol and set
\[
\boxed{b(x,y,z)=\operatorname{parity}(x,y,z,t).}\tag{2}
\]
Reversal of the triple swaps its outer entries and complements the bit. Moreover if \(t=b(v_1,v_2,v_3)\), then \(b(v_2,v_3,v_4)=1-t\), because rotating the four-symbol permutation by one place is odd.

Set \(b(v_3,v_4,e)=1\) for every two distinct \(v_3,v_4\in A\), and set \(b(v_4,e,f)=0\) for every \(v_4\in A\). Give all later consecutive triples of the fixed suffix color zero. Each prescription concerns an independent reversal orbit, apart from the deliberately linked inside-\(A\) triples (2). Hence it extends to a legal reversal-odd coloring of all distinct triples. Every flag of \(D\) has color word
\[
\boxed{(t,1-t,1,0,0,\ldots,0).}\tag{3}
\]
For \(t=0\), the switches are at positions \(1,3\); for \(t=1\), at \(1,2,3\). Thus every flag is bad and its extreme switch-prefix ranks are \(2,4\).

The prefix \(Z_4=\sum_{x\in A}e_x-(4/n)\mathbf1\) is fixed across the 24 orders. For every two-element subset \(S\subset A\), the complementary pair satisfies \(Z_2(A\setminus S)=Z_4-Z_2(S)\). Consequently
\[
\boxed{Z_2(A\setminus S)\wedge Z_4
=-Z_2(S)\wedge Z_4.}\tag{4}
\]
Each subset occurs as the first two symbols of four orders. The contributions of complementary subsets therefore cancel in the sum (1), and every wedge is nonzero by linear independence of prefix vectors. \(\square\)

**Proposition 2 (Grassmannian distinction).** Although the 24 bivectors surround zero, all 24 associated oriented planes contain the fixed line \(\mathbb R Z_4\). The space of oriented two-planes containing this line is \(S^{n-3}\). For \(n\ge6\), \(\pi_2(S^{n-3})=0\), so any three-cell boundary map that remains inside this common-factor sphere can be filled there.

*Proof.* Fix the orientation of \(\mathbb RZ_4\). An oriented plane containing it is specified by a unit transverse vector in \(W\cap Z_4^\perp\), which has dimension \(n-2\). Its unit sphere is \(S^{n-3}\), and this sphere is 2-connected when \(n\ge6\). \(\square\)

**Scope.** The local convex-carrier method is sharp through rank two for unrestricted boundary colorings. A three-cell can have all-bad flags and antipodal extreme-switch wedges. This example does not by itself produce a nontrivial obstruction to extending a map into the oriented Grassmannian. Coherence between adjacent cells, and the nonzero second homotopy of the full Grassmannian, remain the next proof targets.

##### Critical-dimensional rational contraction for switch bivectors

The extreme-switch bivectors in this Article are rational two-vectors in the type-A reflection space. There is an explicit fixed contraction which preserves their zero sets and pairwise ray relations and takes values in a real vector space of dimension n-2. This corrects the previous target-dimension count: contraction by u of any skew tensor lies in u-perp.

Let n>=4 and W={z in R^n: sum_i z_i=0}. Represent every bivector Xi in Lambda^2W by its associated skew-symmetric matrix A_Xi, which annihilates the all-ones vector. Choose an integer M>2*3^{n-1}, put theta=2^{1/M}, and define
[
v=(	heta^{3^0},	heta^{3^1},ldots,	heta^{3^{n-1}}),qquad
u=v-rac1nleft(sum_{i=1}^n v_iight)mathbf1.
	ag{1}
]
The polynomial X^M-2 is irreducible over Q by Eisenstein at two. Put
[
H_u=Wcap u^perp,qquad
oxed{mathcal C_u(Xi)=A_Xi uin H_u.}
	ag{2}
]
Skew-symmetry gives u dot A_Xi u=0 and A_Xi1=0 gives membership in W. Thus dim H_u=n-2.

**Lemma 1 (linear dependence rigidity).** For two real skew-symmetric matrices A,B, if Av and Bv are linearly dependent for every real vector v and A is nonzero, then B=lambda A for some real scalar lambda.

*Proof.* The nonzero skew matrix A has rank at least two, so choose x,y with Ax and Ay independent. For each z with Az nonzero write Bz=lambda(z)Az. Applying the dependence assumption to x+y shows lambda(x)=lambda(y). For arbitrary z with Az nonzero, select one of x,y with A-image independent of Az; applying dependence to their sum gives the same scalar. For k in ker A, applying dependence to x+k and y+k shows Bk belongs to both span(Ax) and span(Ay), whence Bk=0. Therefore B=lambda A. QED.

**Theorem 2 (universal projective faithfulness).** For every rational bivector Xi in Lambda^2(W intersect Q^n),
[
oxed{Xi
e0impliesmathcal C_u(Xi)
e0.}
	ag{3}
]
For any two real-linearly independent rational bivectors Xi,Psi,
[
oxed{mathcal C_u(Xi),mathcal C_u(Psi)
	ext{ are real-linearly independent.}}
	ag{4}
]
Thus the map preserves positive rays, negative rays, and noncollinearity of pairs of nonzero rational bivectors.

*Proof.* Write A,B for the rational skew matrices representing Xi,Psi. Since A1=B1=0, we may replace u by v when evaluating Au or Bu. Each entry of Av is the value at theta of a polynomial sum_i a_i X^{3^{i-1}} with rational entries. Such a polynomial is nonzero for any nonzero matrix row and has degree at most 3^{n-1}<M. Hence Av is nonzero by the irreducibility of X^M-2. This proves (3).

If A and B are nonproportional, Lemma 1 says the columns Av and Bv are independent for some real vector v. Hence some two-by-two minor of the variable matrix [Az,Bz] is a nonzero homogeneous quadratic polynomial in the n entries of z. Substituting z_i=X^{3^{i-1}} maps distinct monomials of degree two to distinct powers of X: the base-three expansions of 3^{i-1}+3^{j-1}, including i=j, are different. Thus this minor becomes a nonzero rational polynomial of degree at most 2*3^{n-1}<M. It cannot vanish at theta. Its value at theta is a nonzero minor of [Au,Bu], proving (4). For real proportional rational tensors the scalar is rational and contraction preserves its sign. QED.

**Corollary 3 (one-skeleton map in the critical dimension).** Let an unrestricted boundary 3-tournament on n>=5 vertices have at least two switches on every full Hamilton order. At each complete flag pi define
[
F(pi)=mathcal C_uigl(Z_{a+1}(pi)wedge Z_{b+1}(pi)igr)in H_usetminus{0},
	ag{5}
]
with a<b the first and last switch positions. Then F(pi-reversed)=-F(pi). The previously established adjacent-exchange theorem shows that neighboring extreme-switch bivectors are never antiparallel. By Theorem 2 neither are their F-images. Radial normalization of straight-line edges therefore gives an antipodally equivariant map on the dual type-A one-skeleton into
[
oxed{S(H_u)cong S^{n-3}.}
	ag{6}
]
The contraction is fixed independently of the coloring. For NORI1 cube geodesics the same property holds across root-changing exchanges; only the two exceptional terminal dimension-order exchanges require nonlinear edge paths.

**Scope.** This algebraic result supplies the critical-dimensional odd vertex labels and their boundary one-skeleton interpolation. It does not produce a continuous map on the entire flag sphere; Borsuk--Ulam forbids such a map under the no-good-path hypothesis. In particular rank-three convex cancellations remain possible, as the preceding Subsection proves. The unfinished mathematical step is a coherent color-sensitive extension over the remaining rank-exchange cells while retaining the original full-path incidence constraints.

##### Total positivity and the safe cone of cut directions

Fix an order \(\pi=(\pi_1,\ldots,\pi_n)\), \(n\ge4\), and the type-A reflection space \(W=\{x\in\mathbb R^n:\sum_i x_i=0\}\). Its centered prefix vectors are
\[
Z_j=\sum_{h=1}^j e_{\pi_h}-\frac jn\mathbf1,\qquad 1\le j<n.
\]
Their Gram kernel is \(G(i,j)=\langle Z_i,Z_j\rangle=\min(i,j)-ij/n\).

**Theorem 1 (strict total positivity of order two).** For all \(1\le i<j<n\) and \(1\le p<q<n\),
\[
\boxed{D(i,j;p,q):=G(i,p)G(j,q)-G(i,q)G(j,p)\ge0.}\tag{1}
\]
Equality holds precisely when the open real intervals \((i,j)\) and \((p,q)\) are disjoint; otherwise \(D(i,j;p,q)>0\).

*Proof.* Since \(G(i,p)>0\) for all interior ranks, fix \(i<j\) and consider
\[
R(t)=G(i,t)/G(j,t)
=\begin{cases}
(n-i)/(n-j),&t\le i,\\
i(n-t)/[t(n-j)],&i\le t\le j,\\
i/j,&t\ge j.
\end{cases}
\]
This is nonincreasing in \(t\), strictly decreasing precisely on \((i,j)\). Multiplying the inequality \(R(p)\ge R(q)\) by \(G(j,p)G(j,q)>0\) gives (1). Strictness occurs precisely if \((p,q)\) intersects \((i,j)\) in a nonempty open interval. QED.

**Theorem 2 (positive cone of safe contractions).** Let \(S\subseteq\{1,\ldots,n-1\}\) contain at least two ranks, with \(p=\min S<q=\max S\). Give every pair \(r<s\) in \(S\) a nonnegative weight \(w_{rs}\), with \(w_{pq}>0\), and set
\[
\mathcal B=\sum_{r<s,\ r,s\in S}w_{rs}\,Z_r\wedge Z_s.
\]
Then:
1. \(\langle \mathcal B,Z_i\wedge Z_j\rangle\ge0\) for every \(i<j\), strictly if some positive-weight interval \((r,s)\) overlaps \((i,j)\).
2. For every nonzero choice of coefficients \(\lambda_t\ge0\) over \(p\le t\le q\), the vector
\[
T=\sum_{t=p}^q\lambda_tZ_t
\quad\text{satisfies}\quad
\boxed{\iota_T\mathcal B\ne0.}\tag{2}
\]
Consequently every continuous interpolation of cut vectors within this positive cone produces a nonvanishing contracted switch-vector.

*Proof.* The bivector inner product identity
\[
\langle Z_r\wedge Z_s,Z_i\wedge Z_j\rangle=D(i,j;r,s)
\]
proves (1) by Theorem 1 and nonnegative weights. If some \(\lambda_t>0\) for \(t<q\), then
\[
\langle \mathcal B,T\wedge Z_q\rangle
=\sum_{t=p}^{q-1}\lambda_t\langle \mathcal B,Z_t\wedge Z_q\rangle>0,
\]
because the \((p,q)\)-summand has a strictly positive determinant whenever \(p\le t<q\). A zero contraction by \(T\) would make this scalar zero, a contradiction. If the only positive coefficient occurs at \(q\), use instead \(\langle\mathcal B,Z_p\wedge T\rangle>0\). QED.

**Corollary 3 (reversal-odd plane carrier of the full quadratic switch tensor).** Let a full Hamilton order carry at least two switches, at ranks \(S\), and let \(\mathcal B\) be its full unweighted quadratic switch bivector. Put
\[
T(\pi)=\sum_{t=p}^{q}Z_t(\pi),\qquad H(\pi)=\iota_{T(\pi)}\mathcal B(\pi).
\]
Then \(H(\pi)\ne0\) and \(H(\pi)\perp T(\pi)\). Hence the oriented plane
\[
\boxed{\Phi(\pi)=\bigl(\operatorname{span}\{T(\pi),H(\pi)\},\,T(\pi)\wedge H(\pi)\bigr)\in\widetilde{\mathrm{Gr}}_2(W)}
\tag{3}
\]
is well defined. Under complemented reversal of the order and color word,
\[
T(\pi^R)=-T(\pi),\quad \mathcal B(\pi^R)=-\mathcal B(\pi),\quad
H(\pi^R)=H(\pi),\quad \boxed{\Phi(\pi^R)=J\Phi(\pi),}
\]
where \(J\) reverses the plane orientation.

*Proof.* Reversal sends \(Z_{n-j}(\pi^R)=-Z_j(\pi)\) and the switch set \(S\) to \(n-S\); the first two identities follow by reindexing, and the other assertions by contraction and wedge orientation. Nonvanishing comes from (2) with all \(\lambda_t=1\). QED.

**Corollary 4 (safe adjacent-cut slides).** If two neighboring rank cuts \(a,a+1\) satisfy \(p\le a<a+1\le q\), every interpolated cut \(T(t)=(1-t)Z_a+tZ_{a+1}\), \(0\le t\le1\), contracts \(\mathcal B\) nontrivially. Thus local motion of the cut between consecutive ranks inside the first/last switch interval has a canonical zero-free homotopy, without discarding the intermediate switch contributions.

**Interpretation and limitation.** This identifies a substantial contractible family of admissible cut directions and a reversal-equivariant oriented-plane assignment depending on the *complete* switch bivector rather than solely the extreme two switches. It is valid in both the cube-edge and boundary-triple settings at the flag level, because only reversal of the centered prefix vectors and positivity of the switch-pair weights are used. It does not yet extend the map continuously across Coxeter flag exchanges: after a swap the centered-prefix configuration and the switch set may both change. Such cross-flag compatibility is the next color-sensitive question.

### Cylindrical counterexample padding and sparse Grassmannian closure reduction

This subsection connects the odd-dimensional reversal-index strengthening of Article XIV with the special-dimensional oriented-Grassmannian obstruction of Article XV. The key is a dimension-preserving projection of monochromatic full geodesics under a cylindrical extension of an arbitrary antipodally odd cube-edge coloring.

**Theorem 1 (counterexample padding).** Let \(n\ge2\) and \(k\ge1\). Every antipodally odd edge coloring \(c:E(Q_n)\to\mathbb F_2\) admits an antipodally odd extension
\[
\widetilde c:E(Q_{n+k})\to\mathbb F_2
\]
such that **every** monochromatic full antipodal geodesic of \(\widetilde c\) projects to a monochromatic full antipodal geodesic of \(c\). Consequently, if \(c\) is a counterexample to NORI1 in dimension \(n\), then \(\widetilde c\) is a counterexample in dimension \(n+k\).

*Proof.* Identify \(Q_{n+k}=Q_n\times Q_k\), with vertices \((x,y)\), \(x\in\{0,1\}^n\), \(y\in\{0,1\}^k\). For an edge in one of the first \(n\) directions, put
\[
\widetilde c(\{(x,y),(x\oplus e_i,y)\})
=c(\{x,x\oplus e_i\}).
\tag{1}
\]
This is independent of \(y\): every parallel \(Q_n\) face inherits the original coloring. For an edge in a new direction \(n+j\), put
\[
\widetilde c(\{(x,y),(x,y\oplus e_j)\})=x_1.
\tag{2}
\]
This is well-defined on undirected edges, since \(x\) remains fixed on a new-direction edge. Under global cube antipodality, an old-direction edge maps to the antipodal old-direction edge in \(Q_n\), so its color flips by the hypothesis on \(c\). A new-direction edge at \(x\) maps to a new-direction edge at \(\bar x\), and \((\bar x)_1=1-x_1\); thus its color also flips. Hence \(\widetilde c\) is legal.

Suppose a monochromatic full antipodal geodesic \(\widetilde P\) traverses every one of the \(n+k\) directions once. Delete from \(\widetilde P\) the \(k\) edges in new directions and project all remaining vertices onto \(Q_n\). The result is a path using the original \(n\) dimensions once each; deleting a new-direction edge does not change its \(Q_n\) projection. It therefore joins some \(x\) to \(\bar x\), is dimension-simple, and every one of its edge colors equals that of the corresponding edge of \(\widetilde P\) by (1). It is monochromatic. The contrapositive proves counterexample padding. \(\square\)

**Corollary 2 (unbounded-dimension reduction).** Let \(\mathcal D\subseteq\{2,3,\ldots\}\) be any unbounded set of dimensions. If NORI1 is proved in every dimension \(N\in\mathcal D\), then NORI1 holds in every dimension \(n\ge2\).

*Proof.* If a counterexample existed at \(n\), Theorem 1 would lift it to every \(N\ge n\), contradicting its absence at any \(N\in\mathcal D\) greater than \(n\). \(\square\)

In particular, it suffices to prove NORI1 on the exponentially sparse sequence
\[
\boxed{\mathcal D=\{2^r+1:r\ge2\}=\{5,9,17,33,\ldots\}.}
\tag{3}
\]

**Theorem 3 (sparse Grassmannian closure criterion).** For \(r\ge2\), set \(N=2^r+1\), \(m=N-1=2^r\), and let \(\Sigma_N\cong S^{N-2}=S^{m-1}\) be the type-\(A_{N-1}\) Coxeter flag sphere, with proper-subset complementation as its free involution. Let
\[
\mathcal G_m=\widetilde{\operatorname{Gr}}_2(\mathbb R^m)
\]
be the oriented two-plane Grassmannian, with involution reversing plane orientation.

Assume the following construction statement can be proved for every \(r\ge2\):

> For every antipodally odd coloring of \(Q_N\) having no monochromatic full antipodal geodesic, there exists a continuous equivariant map \(\Sigma_N\to\mathcal G_m\).

Then NORI1 holds in every dimension \(n\ge2\).

*Proof.* The Grassmannian covering-class computation proved earlier in Article XV gives
\[
\omega^{m-1}=0\quad\text{in }H^{m-1}(\operatorname{Gr}_2(\mathbb R^m);\mathbb F_2)
\tag{4}
\]
when \(m=2^r\), where \(\omega=w_1(\gamma_2)\) classifies the orientation double cover. By contrast, the class \(\alpha\) of \(\Sigma_N\to\Sigma_N/\mathbb Z_2\cong\mathbb RP^{m-1}\) has \(\alpha^{m-1}\ne0\). An equivariant map as stated would pull \(\omega\) back to \(\alpha\), contradicting (4). Thus no counterexample coloring exists at any \(N=2^r+1\). Corollary 2 then excludes counterexamples in every dimension. \(\square\)

**Corollary 4 (sparse half-dimensional chain-tower criterion).** With \(N=2^r+1\ge9\), suppose that for every legal coloring of \(Q_N\) lacking a monochromatic full antipodal geodesic one can construct an antipodal norm-boundary tower in its two-color endpoint complex through height
\[
\boxed{q_r=(N-3)/2=2^{r-1}-1.}
\tag{5}
\]
Then NORI1 holds in every dimension \(n\ge2\).

*Proof.* The odd-dimensional top-cohomology cancellation theorem of Article XIV shows that a hypothetical counterexample at \(N\ge7\) has \(\alpha_K^{q_r}=0\). The Smith-transfer equivalence shows that the asserted height-\(q_r\) tower would force \(\alpha_K^{q_r}\ne0\), a contradiction. Thus no counterexample exists at any \(N\ge9\) in the unbounded family, and Corollary 2 applies. \(\square\)

**Scope and warning.** Theorem 1 preserves the cube's original dimension-simple paths under projection, but says nothing about increasing or decreasing the switch count for arbitrary nonmonochromatic paths. Theorem 3 is a *conditional proof program*, not a proof that the color-sensitive equivariant Grassmannian map can be extended beyond the low-dimensional cells established in Article XV. Theorem 4 likewise assumes, rather than constructs, the missing chains. The reduction is specific to NORI1; no analogous inheritance theorem for unrestricted ordinary boundary 3-tournaments has been established here.

**Research significance.** All-dimensional NORI1 would follow from coherent Grassmannian extensions in the sparse odd dimensions \(2^r+1\), precisely where the strongest known orientation-cover obstruction is available. It is unnecessary to prove the Grassmannian extension separately for dimensions outside this sequence. Alternatively, only a half-dimensional antipodal chain tower through height \(2^{r-1}-1\) is needed in each of those sparse dimensions.

##### Three-block Pluecker monotonicity and switch-confinement criterion

Let \(V=A\sqcup B\sqcup C\) be an ordered partition with positive block sizes \(a,b,c\), \(n=a+b+c\). Let \(\pi\) be any complete order refining \(A|B|C\). Put \(Z_p(\pi)=\sum_{i\le p}e_{\pi_i}-(p/n)\mathbf1\) for \(1\le p<n\), and \(\lambda_{A,C}=\mathbf1_A^*\wedge\mathbf1_C^*\) on \(W=\{\sum z_i=0\}\).

**Theorem 1 (universal Pluecker sign).** For every \(1\le p<q<n\),
\[
D_{p,q}:=\lambda_{A,C}(Z_p\wedge Z_q)\le0,
\]
independently of the internal block orders. Furthermore,
\[
\boxed{D_{p,q}=0\iff q\le a\ \text{or}\ p\ge a+b.}\tag{1}
\]

*Proof.* Let \(X_p=\mathbf1_A\cdot Z_p=\min(p,a)-ap/n\) and \(Y_p=\mathbf1_C\cdot Z_p=\max(0,p-a-b)-cp/n\). Then \(D_{p,q}=X_pY_q-X_qY_p\). The planar path \((X_p,Y_p)\) has three linear segments:
\[
p\le a:\ ((b+c)p/n,-cp/n);\quad
a\le p\le a+b:\ (a(n-p)/n,-cp/n);\quad
a+b\le p:\ (a(n-p)/n,-(a+b)(n-p)/n).
\]
The determinant for ranks in the six segment pairs \(AA,AB,AC,BB,BC,CC\) is respectively
\[
0,\quad cp(a-q)/n,\quad-bp(n-q)/n,\quad
-ac(q-p)/n,\quad a(n-q)(p-a-b)/n,\quad0.
\]
All mixed entries are negative away from the stated degenerate rank regions. This proves (1). QED.

**Theorem 2 (complete switch-bivector characterization).** Let \(S(\pi)\subseteq\{1,\ldots,n-1\}\) contain at least two switch-prefix ranks, and put
\[
\mathcal B(\pi)=\sum_{p<q,\ p,q\in S(\pi)}Z_p\wedge Z_q,\qquad
E(\pi)=Z_{\min S(\pi)}\wedge Z_{\max S(\pi)}.
\]
Then \(\lambda_{A,C}(\mathcal B)\le0\), and
\[
\boxed{\lambda_{A,C}(\mathcal B)<0
\iff S(\pi)\not\subseteq[1,a]\ \text{and}\
S(\pi)\not\subseteq[a+b,n-1].}\tag{2}
\]
The same condition characterizes strict negativity of \(\lambda_{A,C}(E)\).

*Proof.* Every switch-pair summand is nonpositive by Theorem 1. If all selected ranks lie in either extremal interval, each pair vanishes. Otherwise the smallest and largest ranks form a pair outside both intervals, so its determinant is strictly negative. No other term can cancel it. QED.

**Corollary 3 (coherent parabolic carriers).** Suppose every Hamilton flag in the three-block Coxeter residue \(A|B|C\) has at least two switches, with no flag having all switch ranks contained in either extremal interval of (2). Then all full quadratic bivectors belong to the common strict convex halfspace \(\lambda_{A,C}<0\), so their piecewise-affine interpolation is zero-free on the cell. All extreme-switch oriented planes belong to one contractible Pluecker chart. When a coherent triangulation of the whole Coxeter complex is used, the affine fillings agree on shared faces.

**Corollary 4 (monochromatic-tail localization).** For boundary 3-tournaments the legal switch ranks are \(2,\ldots,n-2\). A flag can prevent this strict three-block chart only if \(a\ge3\) and all its switches are in \(\{2,\ldots,a\}\), or if \(c\ge3\) and all its switches are in \(\{a+b,\ldots,n-2\}\). The former gives a long monochromatic suffix of the triple-color word, and the latter a long monochromatic prefix. The same theorem applies to cube-edge words with their full switch-rank range.

This strengthens the prior universal endpoint-block convex-carrier criterion by allowing arbitrarily large endpoint blocks whenever coloring constraints exclude the two explicitly characterized kinds of switch confinement. It does not show that such exceptional flags are impossible for unrestricted colorings.

##### Rank-two convex carriers for the complete quadratic switch tensor

Let \(n\ge6\) and let \(b(x,y,z)\in\mathbb F_2\) be an unrestricted reversal-odd coloring of ordered distinct triples: \(b(z,y,x)=1-b(x,y,z)\). A Hamilton permutation \(\pi\) has color word \(b(\pi_1,\pi_2,\pi_3),\ldots,b(\pi_{n-2},\pi_{n-1},\pi_n)\). Let \(S_\pi\subseteq\{2,\ldots,n-2\}\) denote the prefix ranks at its switches. When \(|S_\pi|\ge2\), define the complete quadratic bivector
\[
\mathcal B(\pi)=\sum_{p<q,\ p,q\in S_\pi}Z_p(\pi)\wedge Z_q(\pi).
\]

**Theorem 1 (color-sensitive rank-two convex filling).** Let \(D\) be any rank-two dual type-A Coxeter cell (commuting square or braid hexagon), and suppose every Hamilton flag in \(D\) has at least two switches. Then there exists a decomposable covector \(\omega=u\wedge v\in\Lambda^2W^*\) such that
\[
\boxed{\omega(\mathcal B(\pi))<0\quad\text{for every flag }\pi\in D.}\tag{1}
\]
Consequently the convex hull of the *full quadratic* bivectors on \(D\) avoids zero, and their normalized positive affine combinations give a continuous filling over \(D\). This strengthens the rank-two convex-carrier result previously proved for first/last switch wedges.

*Proof.* A rank-two Coxeter cell corresponds to an ordered partition of the symbols with either one block of size three (a braid hexagon) or two blocks of size two (a commuting square).

If both terminal blocks have sizes at most two, put \(u\) equal to the average of the entry-extracting covectors on the first block and \(v\) equal to the average on the last block. Every permitted switch prefix rank \(p\) is at least two and at most \(n-2\). Hence each prefix contains the entire first block and none of the last block, and a direct two-by-two determinant gives
\[
(u\wedge v)(Z_p\wedge Z_q)=-\frac{q-p}{n}<0
\quad(p<q).
\tag{2}
\]
Every \(\mathcal B(\pi)\) is a nonempty positive sum of these wedges, so the same separator works for all flags.

The only remaining cases are a braid cell with three symbols in its first block or three symbols in its last block. Reversal reduces to the first case. Write the first block as \(\{a,b,c\}\), with six orders \((x,y,t,d_4,\ldots,d_n)\), where \(t\) is the third of the three variable symbols. Set \(z=d_n\), and choose \(u=\lambda_a e_a^*+\lambda_b e_b^*+\lambda_c e_c^*\), \(v=e_z^*\), with all \(\lambda_t>0\) and \(\sum\lambda_t=1\). For any prefix pair \(2\le p<q\le n-2\),
\[
n(u\wedge v)(Z_p\wedge Z_q)=
\begin{cases}
q\lambda_t-(q-2),&p=2,\\
-(q-p),&p\ge3.
\end{cases}
\tag{3}
\]
When \(2\notin S_\pi\), formula (3) makes \(\omega(\mathcal B(\pi))<0\). Otherwise put \(R_\pi=S_\pi\setminus\{2\}\), which is nonempty. Then
\[
n\omega(\mathcal B(\pi))
=\lambda_t A_\pi-D_\pi,
\quad
A_\pi=\sum_{q\in R_\pi}q,\quad
D_\pi=\sum_{q\in R_\pi}(q-2)+
\sum_{p<q,\ p,q\in R_\pi}(q-p).
\tag{4}
\]
Every ratio \(\theta_\pi=D_\pi/A_\pi\) is at least \(1/3\), and equality occurs only when \(S_\pi=\{2,3\}\); this follows from \((q-2)/q\ge1/3\) for \(q\ge3\), with strictness for \(q>3\), and from positivity of the second sum. Thus it suffices to choose positive \(\lambda_t\) summing to one with
\[
\lambda_t<\theta_t:=\min_{\pi:\,\pi_3=t,\ 2\in S_\pi}\theta_\pi,
\tag{5}
\]
where an empty minimum means \(+\infty\).

We claim at least one of the three \(\theta_t\) is strictly greater than \(1/3\). Suppose not. For each last first-block symbol \(t\), one of the two orders ending in \(t\) has \(S_\pi=\{2,3\}\). In such an order all color comparisons after its third triple window are equalities. The third window has color \(b(t,d_4,d_5)\), whereas the fourth is the common suffix color \(b(d_4,d_5,d_6)=c_0\). Therefore \(b(t,d_4,d_5)=c_0\) for that choice of \(t\), and it has this value for both initial orders ending in \(t\). The other initial order ending in the same \(t\) has no switches after rank three, by the same suffix calculation; since it is also bad, it must switch at both ranks two and three. Hence its first triple has color \(c_0\), just as in the selected order. Repeating for each \(t\in\{a,b,c\}\) shows that all six permutations of the three-symbol initial block have color \(c_0\), contradicting reversal oddness. This proves the claim.

After replacing infinite \(\theta_t\) by the finite upper bound one, the three positive bounds sum to more than one. One can therefore choose positive \(\lambda_t\) with sum one and each strictly below \(\theta_t\). Equations (4)-(5) prove (1) on all six flags. The final-terminal braid follows by reversing all orders. QED.

**Corollary 2 (full-bivector two-skeleton map).** If an unrestricted reversal-odd boundary coloring had no Hamilton order with at most one switch, its complete quadratic switch-bivector labels would extend, by positive affine interpolation, equivariantly over every rank-two cell of the dual type-A Coxeter sphere into the unit sphere of \(\Lambda^2W\). On each cell a color-sensitive decomposable covector strictly separates the entire interpolated image from zero. Opposite cells are filled by the reversed negative images.

**Sharpness with respect to cell dimension.** The tetrahedral parity rank-three construction published earlier in this Article has all 24 flags bad, but two flags with ordered initial pairs complementary within the first four symbols and the same parity bit zero. Both have switch set \(\{2,4\}\), so the *full quadratic* bivectors at those flags equal the extreme bivectors \(Z_2\wedge Z_4\) and its negative. Therefore zero lies in the convex hull already on a rank-three cell. No corresponding universal convex filling assertion holds in rank three.

**Scope.** The positive rank-two result uses the unrestricted reversal-odd triple constraint only in the terminal braid case and keeps all intermediate switch-pair terms. It does not extend convex fillings over rank-three residues, nor does it resolve the one-switch conjecture.

##### Positive-prefix Stiefel charts and the first substantive cell dimension

Let \(W=\{z\in\mathbb R^n:\sum z_i=0\}\), \(n\ge5\). Fix a nonzero vector \(T\in W\) and write \(\mathcal G=\widetilde{\mathrm{Gr}}_2(W)\) for the manifold of oriented two-planes. Define the open transversal plane set
\[
\mathcal U_T=\{\Pi\in\mathcal G:\operatorname{proj}_{\Pi}T\ne0\}.
\]

**Theorem 1 (explicit sphere deformation retract).** There is a natural deformation retraction
\[
\boxed{\mathcal U_T\simeq S(T^\perp)\cong S^{n-3},}\tag{1}
\]
where \(S(T^\perp)\) is identified with the oriented planes containing \(T\). More precisely, each plane \(\Pi\in\mathcal U_T\) has its unique positively oriented orthonormal frame \((e_1,e_2)\) for which
\[
e_1=\frac{\operatorname{proj}_\Pi T}{\|\operatorname{proj}_\Pi T\|},\qquad
e_2\perp T.
\]
The assignment \(\Pi\mapsto e_2\) has contractible fibers, and the frame deformation
\[
e_1(t)=\frac{(1-t)e_1+tT/\|T\|}{\|(1-t)e_1+tT/\|T\|\|},\qquad e_2(t)=e_2,
\]
retracts \(\mathcal U_T\) onto the containing-\(T\) sphere.

*Proof.* The positive \(T\)-projection determines \(e_1\) uniquely, and the orientation then determines \(e_2\). Since \(T\) has no component along \(e_2\), necessarily \(e_2\in T^\perp\). Conversely, given a unit \(e_2\in T^\perp\), every unit \(e_1\in e_2^\perp\) with \(\langle e_1,T\rangle>0\) yields such a plane and frame; the possible \(e_1\) form an open hemisphere. The displayed formula stays inside this hemisphere and keeps \(e_1(t)\perp e_2\), and at \(t=1\) the plane contains \(T\). QED.

**Theorem 2 (every parabolic residue has a positive-prefix transversal).** Let \(\mathcal P=B_1|\cdots|B_k\) be any ordered partition into at least two nonempty blocks, with \(a=|B_1|\). Put
\[
T_{\mathcal P}=\mathbf1_{B_1}-\frac an\mathbf1.
\]
For every full ordering \(\pi\) refining \(\mathcal P\) and every nontrivial centered prefix \(Z_p(\pi)\),
\[
\boxed{\langle T_{\mathcal P},Z_p(\pi)\rangle
=\min(p,a)-ap/n>0.}\tag{2}
\]
Consequently every extreme-switch oriented plane \(\mathrm{span}^{+}(Z_p,Z_q)\), for \(p<q\), belongs to the SAME open set \(\mathcal U_{T_{\mathcal P}}\), regardless of unrestricted coloring or chosen switch ranks.

*Proof.* Every refining full order places precisely the \(a\) members of \(B_1\) first. The dot product is the centered number of them in the first \(p\) positions, giving (2). Since \(a<n\) and \(0<p<n\), the value is positive. A plane containing \(Z_p\) with positive pairing against \(T_{\mathcal P}\) cannot be perpendicular to \(T_{\mathcal P}\). QED.

**Corollary 3 (local Grassmannian obstruction threshold).** For \(n\ge6\), \(\mathcal U_{T_{\mathcal P}}\simeq S^{n-3}\) is \((n-4)\)-connected. Thus any boundary map of a parabolic cell \(D\) of dimension \(k\le n-3\), provided its entire boundary image stays in this fixed \(\mathcal U_{T_{\mathcal P}}\), extends continuously over \(D\) inside \(\mathcal U_{T_{\mathcal P}}\). In particular any rank-three parabolic cell boundary map inside its natural positive-prefix transversal is nullhomotopic when \(n\ge6\).

*Proof.* Its boundary sphere has dimension \(k-1\le n-4\), while \(\pi_j(S^{n-3})=0\) for \(j<n-3\). QED.

**Theorem 4 (why the top-cell straddling obstruction survives).** In dimension \(d=n-2\), the sphere \(\mathcal U_T\simeq S^{n-3}\) itself has nontrivial group \(\pi_{n-3}(\mathcal U_T)\cong\mathbb Z\). The variable-rank two-block switch-plane boundary constructed in the earlier Stiefel obstruction subsection takes values in \(\mathcal U_T\) and has degree \(\pm1\) under the retraction (1). Under inclusion into the full oriented Grassmannian, this integer reduces modulo \(\chi(S^{n-2})\). Thus its image is the nonzero generator of \(\mathbb Z\) when \(n\) is odd, or \(\mathbb Z/2\) when \(n\) is even.

*Proof.* On the relevant top cell the first vector \(x=Z_k\) stays strictly positive against the block vector \(T\), even under the affine boundary interpolation of the two vectors. The retraction identifies its plane boundary class with the unit contraction \(\iota_T(x\wedge y)\), of degree \(\pm1\) by the permutahedral product theorem. The standard Stiefel fibration \(S^{n-3}\to V_2(\mathbb R^{n-1})\to S^{n-2}\) sends its generator to the quotient by the tangent-sphere Euler number, \(\chi(S^{n-2})\), and the frame-to-Grassmannian bundle does not change \(\pi_{n-3}\) for \(n\ge6\). QED.

**Proof-search implication.** The flag planes in ANY individual nontrivial parabolic residue lie in a common natural transversal to a fixed block vector. Therefore a lower-cell Grassmannian obstruction cannot be inferred merely from its vertex labels: any such obstruction must involve how previously chosen boundary fillings leave or wind between these transversal charts. This isolates the global face-gluing problem more precisely. It does not give compatible chart-preserving fillings across all cells simultaneously, nor resolve the two target conjectures.

### Affine antipodal cube colorings obstruct canonical straddling top-cell fillings

This construction shows that the nonzero top-cell switch-plane degree from Article XV is realizable by **legal cube-edge colorings**, not only by boundary 3-tournament colorings. It occurs in every ambient cube dimension \(n\ge6\), including the sparse dimensions \(n=2^r+1\) relevant to the Grassmannian reduction.

Fix a partition \([n]=A\sqcup B\) with \(a=|A|\ge2\), \(b=|B|\ge2\), and choose fixed-point-free permutations \(\sigma_A\in S_A\), \(\sigma_B\in S_B\). Let \(\sigma=\sigma_A\sigma_B\). Define the affine edge coloring
\[
\boxed{c(\{x,x\oplus e_i\})=x_{\sigma(i)},\qquad i\in[n].}
\tag{1}
\]
The right-hand side is independent of the choice of endpoint because \(\sigma(i)\ne i\). Under global antipodality \(x\mapsto\bar x\), its bit is complemented, so (1) is antipodally odd.

Consider all \(a!b!\) complete cube geodesics rooted at \(0^n\) whose dimension orders list all members of \(A\) before all members of \(B\). Their permutations are the vertices of the top two-block dual Coxeter cell
\[
D(A|B)=P_a\times P_b,\qquad \dim D=n-2.
\]

**Theorem 1 (three compulsory switches in every two-block flag).** Every such geodesic has at least one color switch at a rank strictly between \(1\) and \(a-1\), a switch at rank \(a\), and at least one switch at a rank strictly between \(a+1\) and \(n-1\). In particular every cell vertex has at least three switches, with first switch rank \(p<a\) and final switch rank \(q>a\).

*Proof.* For every direction \(i\), its edge color is the value of the \(\sigma(i)\)-th bit immediately before direction \(i\) is toggled. Since the geodesic begins at \(0^n\) and uses each dimension once, this bit equals one if \(\sigma(i)\) has already appeared in the dimension order and zero otherwise. Because \(\sigma\) preserves each of \(A,B\), the first direction encountered in either block has color zero; its successor under \(\sigma\) belongs to the same block and has not yet been used. The last direction encountered in either block has color one, since its distinct \(\sigma\)-successor belongs to the same block and must already have been used. Thus each block's color subword begins with zero and ends with one, forcing an internal switch. At their common boundary the last \(A\)-edge has color one while the first \(B\)-edge has color zero, forcing a further switch. The first and final switch ranks lie strictly inside \(A,B\), respectively. \(\square\)

When \(a=b=3\) and both permutations are three-cycles, each three-letter block has precisely one internal switch, hence **all 36 rooted six-dimensional geodesics in \(D(A|B)\) have precisely three switches**, with their full color words of the form \(0,0,1,0,0,1\), \(0,1,1,0,1,1\), or the analogous combinations of the two block patterns.

**Theorem 2 (an explicit nonfillable Grassmannian boundary class).** Let \(n\ge6\) and use coloring (1). For each \(\pi\in D(A|B)^{(0)}\), let \(S_\pi\) denote its switch-prefix ranks. Let
\[
Z_j(\pi)=\sum_{h\le j}e_{\pi_h}-\frac jn\mathbf1,\quad
T=\mathbf1_A-\frac an\mathbf1,
\quad
\mathcal B(\pi)=\sum_{\substack{p<q\\p,q\in S_\pi}}Z_p(\pi)\wedge Z_q(\pi).
\]
The piecewise-affine boundary interpolation of
\[
\boxed{H(\pi)=\iota_T\mathcal B(\pi)\in T^\perp\cap W}
\tag{2}
\]
is nowhere zero and represents a map \(\partial D\to S(T^\perp\cap W)\cong S^{n-3}\) of degree \(\pm1\). Hence its oriented-plane lift
\[
\boxed{x\longmapsto
\bigl(\operatorname{span}^{+}\{T,H(x)\}\bigr)}
\tag{3}
\]
defines a nonextendible boundary map into \(\widetilde{\operatorname{Gr}}_2(W)\). Its obstruction is the nonzero generator of \(\mathbb Z\) for odd \(n\), and of \(\mathbb Z/2\) for even \(n\).

*Proof.* Theorem 1 supplies, at each vertex, a switch rank \(p<a\) and another \(q>a\). The universal full-quadratic switch-bivector degree theorem in the Hamilton-residue section of Article XV applies to any such family of nonempty switch sets. It proves that affine interpolation of (2) avoids zero on the entire boundary and has degree \(\pm1\). For the plane (3), the fixed vector \(T\) is independent of the coloring and \(H(x)\perp T\). Therefore its image lies in the \(T\)-containing plane sphere, identified with \(S^{n-3}\) by the positive-prefix Stiefel retraction of Article XV. The inclusion of this sphere into the oriented two-plane Grassmannian sends a degree-one generator to the generator of
\[
\pi_{n-3}(\widetilde{\operatorname{Gr}}_2(\mathbb R^{n-1}))
\cong\mathbb Z/\chi(S^{n-2})\mathbb Z.
\]
For \(n\ge6\), this is \(\mathbb Z\) when \(n\) is odd and \(\mathbb Z/2\) when \(n\) is even. Hence the boundary plane map cannot extend over the top ball \(D\). \(\square\)

**Corollary 3 (the sparse power-of-two-plus-one obstruction is realized by legal cube colorings).** For every \(r\ge3\), the dimension \(n=2^r+1\) admits a legal affine coloring (1) and a two-block Coxeter top cell whose canonical full-quadratic switch-plane boundary map represents a nonzero **integral** Grassmannian homotopy class. One may take \(|A|=3\), \(|B|=n-3\), and cyclic derangements on both blocks.

**Scope and distinction.** These are **local** cell nonextension examples. The affine coloring (1) is not asserted to lack a monochromatic full antipodal geodesic globally; for example, in the \(3+3\) case it has one from an appropriately chosen nonzero root. Thus the result does not refute the conditional global Grassmannian criterion for NORI1. It does refute any strategy claiming that legal antipodal oddness and the absence of a good **flag inside a chosen top cell**, by themselves, make the canonical switch-plane boundary nullhomotopic. A global proof must exploit compatibility across multiple cells, alter lower-cell fillings coherently, or use some feature peculiar to a global counterexample that the present local colorings do not possess.

#### Signed straddling degree as a product of root-zonotope carriers

Write \(D=P_A\times P_B\) for the two-block permutahedral cell, with \(|A|=a\ge2\), \(|B|=b\ge2\), and orient it by \(W_A\oplus W_B\). For any connected graph \(G\) on a block \(E\), write
\[
z_G(\pi)=\tfrac12\sum_{\{i,j\}\in E(G),\,i<j}
\epsilon_{ij}(\pi)(e_i-e_j)
\]
for its oriented graphical-zonotope label. For any nonempty proper first subset \(S\subset E\), all refining permutations satisfy
\[
\boxed{\sum_{i\in S}z_G(\pi)_i=|\partial_G S|/2>0.}
\tag{4}
\]

**Theorem 3 (straddling-degree homotopy).** Let \(H(\pi_A,\pi_B)\in W_A\oplus W_B\) be the contracted *full quadratic switch bivector* in the preceding Article XV theorem, assuming every two-block flag has switch ranks strictly inside both \(A\) and \(B\). For **any connected graphs** \(G_A,G_B\) on the blocks, put
\[
\boxed{\mathcal R(\pi_A,\pi_B)=
-z_{G_A}(\pi_A)\oplus z_{G_B}(\pi_B).}
\tag{5}
\]
The piecewise-affine boundary maps \(H,\mathcal R:\partial D\to W_A\oplus W_B\setminus\{0\}\) are joined by a zero-free straight-line homotopy. Their radial maps have the same signed Brouwer degree; with the product orientation this degree is
\[
\boxed{\deg(H/\|H\|)=(-1)^{a-1}.}
\tag{6}
\]

*Proof.* The full-quadratic switch sign-cone theorem gives \(\sum_{i\in S}H_i<0\) on every facet \(F_S\times P_B\), and \(\sum_{i\in U}H_i>0\) on every facet \(P_A\times F_U\). The cut identity (4) gives the same strict signs for \(\mathcal R\), using its negative \(A\)-component. Therefore on each boundary facet both families of labels and their straight-line interpolations remain in one common strict halfspace. All piecewise-affine boundary maps in this homotopy avoid zero.

Deform each connected graph label to the complete-graph permutahedral label:
\[
z_{G,t}=z_G+t z_{K_E\setminus G},\qquad 0\le t\le1.
\]
Every nonempty proper cut continues to satisfy the strict positive cut inequality, so the corresponding product boundary maps remain nonzero. At \(t=1\), the product map is the linear reflection \((u_A,u_B)\mapsto(-u_A,u_B)\) of the original product permutahedron. Its determinant sign, and thus its boundary degree, is \((-1)^{\dim W_A}=(-1)^{a-1}\). Homotopy invariance proves (6). \(\square\)

**Corollary 4 (block-cycle affine colors).** For the legal affine colorings of the preceding two-block obstruction theorem, choose a single permutation cycle on each block (each of length at least three). The monochromatic root selector of Article XIV, followed by the linear incidence transformation of each cycle, gives \(z_{C_A}\) and \(z_{C_B}\). The local switch-plane obstruction is therefore homotopic, after its standard contraction, to the product of two degree-one root transports, with the \(A\)-factor sign reversed.

**Scope.** Once every flag straddles the cut, the signed local degree depends only on the block size \(a\), not on the switch positions or the coloring. Even colorings with many monochromatic full paths exhibit this local obstruction. Global closure must therefore constrain how the blockwise degree carriers fit together under exchanges and root mobility; isolated top-cell nonextendibility cannot by itself establish NORI1.

### Universal positive-prefix collisions and global odd parity

Let \(n\ge3\), \(d=n-2\), and let \(P_n\) be the centered permutahedron in \(W=\{z\in\mathbb R^n:\sum z_i=0\}\), with antipodal boundary involution \(R\) reversing complete orders. For each order \(\pi\), suppose we choose two distinct proper prefix ranks
\[
1\le p(\pi)<q(\pi)\le n-1,\qquad
p(\pi^R)=n-q(\pi),\quad q(\pi^R)=n-p(\pi).
\tag{1}
\]
These include the first and last color-switch prefix ranks of reversal-complementary binary color words with at least two switches. This covers both fixed-root NORI1 geodesic words in a hypothetical counterexample and the reversal-odd boundary triple words in a hypothetical one-switch counterexample.

Define \(Z_j(\pi)=\sum_{h\le j}e_{\pi_h}-(j/n)\mathbf1\) and vertex labels \(X_\pi=Z_{p(\pi)}(\pi)\), \(Y_\pi=Z_{q(\pi)}(\pi)\). Interpolate affinely on a centrally symmetric triangulation of \(\partial P_n\), for instance by assigning each face barycenter the average of its vertex labels. Write the resulting continuous maps as \(X,Y:\partial P_n\to W\).

**Theorem 1 (positive-prefix symmetry and degree).** Let \(S=X+Y\), \(D=X-Y\). They satisfy
\[
\boxed{S(Rz)=-S(z),\qquad D(Rz)=D(z),\qquad S(z)\ne0.}
\tag{2}
\]
The normalized antipodal sphere map \(S/\|S\|:\partial P_n\to S(W)\) has integer degree \(+1\), with the usual orientation induced by the permutahedron. Moreover \(X(z)\) and \(Y(z)\) can never be negatively proportional.

*Proof.* For a proper nonempty first-block subset \(A\subset[n]\), the centered block vector \(T_A=\mathbf1_A-(|A|/n)\mathbf1\) satisfies, at every order refining its facet,
\[
\langle T_A,Z_j(\pi)\rangle
=\min(j,|A|)-j|A|/n>0
\quad(1\le j<n).
\tag{3}
\]
Positive affine interpolation retains this inequality throughout the facet. Every boundary point belongs to a facet, so X,Y,S are nowhere zero and X,Y are not negatively proportional. Prefix reversal gives \(Z_{n-j}(\pi^R)=-Z_j(\pi)\), which yields \(X(Rz)=-Y(z)\), \(Y(Rz)=-X(z)\), and (2). On every facet, both X and the source permutahedral position vector lie in the common strict open halfspace (3). Straight-line interpolation therefore homotopes normalized X to the identity radial map. The homotopy \(X+tY\) likewise never vanishes. Thus normalized S has degree \(+1\). \(\square\)

**Theorem 2 (odd parity of positive collinearity orbits).** The two interpolated prefix maps have a point where \(X\) and \(Y\) are *positively proportional*. After a small generic equivariant perturbation maintaining the strict facet inequalities, their positive-collinearity set is finite and contains an odd number of antipodal pairs:
\[
\boxed{\#\{[z]\in\partial P_n/R:X(z)\parallel Y(z)\}
\equiv1\pmod2.}
\tag{4}
\]

*Proof.* Put \(Q=\partial P_n/R\cong\mathbb RP^d\). The odd nonzero map S defines a real line subbundle \(L\subset Q\times W\), with \(w_1(L)=\alpha\), the generator of \(H^1(Q;\mathbb F_2)\). Its orthogonal complement \(E=L^\perp\) has rank d. Since \(L\oplus E\) is trivial,
\[
w(E)=(1+\alpha)^{-1}
=1+\alpha+\cdots+\alpha^d,\qquad
\boxed{w_d(E)=\alpha^d\ne0.}
\tag{5}
\]
The even vector D projects orthogonally to the section
\[
s([z])=D(z)-\frac{\langle D(z),S(z)\rangle}{\|S(z)\|^2}S(z)\in E_{[z]}.
\tag{6}
\]
The formula is unchanged under R. A zero means D and S are linearly dependent, which, since S is nonzero, is equivalent to X and Y being linearly dependent. By Theorem 1 this dependence is positive. The top Stiefel–Whitney class forces a zero; for a transverse section it counts zero points modulo two. Its Stiefel–Whitney number on \(Q\) equals \(\langle\alpha^d,[Q]\rangle=1\), proving (4). \(\square\)

**Theorem 3 (sum of local two-block contraction indices).** Let \(F_A\) be the top permutahedral facet of full orders whose first block is a nonempty proper \(A\subset[n]\). On it set
\[
H_A=\iota_{T_A}(X\wedge Y)
=\langle T_A,X\rangle Y-\langle T_A,Y\rangle X
\in T_A^\perp\cap W.
\tag{7}
\]
This vanishes if and only if X and Y are positively proportional. After generic equivariant perturbation avoiding zeros on the proper facet boundaries, define the local mod-two degree
\[
\delta_A=\deg_2(H_A/\|H_A\|:\partial F_A\to S^{d-1}).
\]
Then \(\delta_{A^c}=\delta_A\) and
\[
\boxed{\sum_{\{A,A^c\}}\delta_A=1\pmod2.}
\tag{8}
\]
The sum runs over antipodal pairs of proper nonempty block cuts.

*Proof.* Both scalar products in (7) are positive on F_A, and a linear dependence of X and Y implies H_A=0; conversely, H_A=0 forces their dependence since the coefficients are nonzero. A generic perturbation of the section in Theorem 2 is transverse and has no zeros on the union of boundaries of top facets, a codimension-one subset. On each top ball the mod-two zero count equals its boundary degree. R pairs facets F_A and F_{A^c}, and each zero orbit has one representative per paired facet; sum the local parities over one representative from each pair. Theorem 2 gives (8). \(\square\)

**Conditional odd-dimensional terminal leakage.** If n is odd and every nonterminal two-block facet (both block sizes at least two) has switches straddling the block boundary at every vertex order, the earlier variable-prefix top-cell degree theorem gives \(\delta_A=1\) on those facets. Their number of antipodal pairs is \(2^{n-1}-n-1\), which is even for odd n. Equation (8) therefore forces
\[
\sum_{\{A,A^c\}:\min(|A|,|A^c|)=1}\delta_A=1\pmod2.
\tag{9}
\]
This is conditional, and for ordinary boundary triple colorings the straddling requirement cannot hold for all two-element first blocks because their first switch rank is at least two. It must not be invoked as an unconditional terminal-cell statement.

**Relation to the recent positive-carrier transport theorem.** The new Article XV result on homotopy-constant prefix carriers shows that, while preserving positive-carrier fillings, a homotopy modification in a three-block cell can toggle the two neighboring top-facet obstruction degrees. The graph of antipodal top-facet pairs under these incidences is connected. Consequently these allowable changes generate all even-parity degree changes, whereas (8) fixes the total parity to one. The position of the odd local degrees is therefore not itself a positive-carrier invariant; only their total parity is. A coloring-specific contradiction must use conditions stronger than prefix positivity, rank reversal, and the associated carrier homotopy type.

**Scope.** Theorems 1–3 hold for every rank assignment satisfying (1), whether or not it comes from a coloring. They do not turn a positive-collinearity point of *averaged prefix vectors* into one monochromatic geodesic, and they do not settle NORI1 or the boundary 3-tournament one-switch conjecture. Their role is to identify the universal parity that any color-sensitive obstruction must strengthen.

#### Integral Euler refinement and the dimension-parity dichotomy

The odd collision parity can be sharpened to an integral zero-count in even cube dimension. Retain the notation \(d=n-2\), \(Q=\mathbb RP^d\), the sign line bundle \(L\) and rank-\(d\) orthogonal complement \(E=L^\perp\) from Theorem 2. Let \(\mathbb Z_\alpha\) denote the integral local system with monodromy \(-1\) around the nontrivial loop in \(Q\).

**Theorem 4 (Euler class of the positive-prefix collision bundle).** The Euler class with its orientation local system satisfies
\[
e(E)\in H^d(Q;\mathbb Z_\alpha),\qquad
\boxed{
H^d(Q;\mathbb Z_\alpha)\cong
\begin{cases}
\mathbb Z,&d\text{ even},\\
\mathbb Z/2,&d\text{ odd}.
\end{cases}}
\tag{10}
\]
For even \(d\), \(e(E)\) is a generator of the integer group and its signed evaluation on the twisted fundamental class is \(+1\) with the orientation induced by the degree-\(+1\) sum map of Theorem 1. For odd \(d\), \(e(E)\) is the unique nonzero element of \(\mathbb Z/2\). In both cases its mod-two reduction is the class \(\alpha^d\).

*Proof.* The bundle E has \(w_1(E)=\alpha\), because \(L\oplus E\) is trivial and \(w_1(L)=\alpha\). Its orientation local system is therefore \(\mathbb Z_\alpha\). By Poincare duality with local systems,
\[
H^d(Q;\mathbb Z_\alpha)
\cong H_0(Q;\mathbb Z_\alpha\otimes\mathcal O_Q).
\]
The orientation system of \(Q=\mathbb RP^d\) is the sign system when d is even and trivial when d is odd. The right-hand side is therefore \(\mathbb Z\) for even d and the sign coinvariants \(\mathbb Z/2\) for odd d, proving (10).

Let \(\rho:S^d\to Q\) be the antipodal two-sheeted covering and \(f=S/\|S\|:S^d\to S(W)\cong S^d\) the odd degree-\(+1\) map from Theorem 1. The lifted bundle \(\rho^*E\) is the orthogonal complement of the line spanned by \(f(z)\) in W, and hence
\[
\boxed{\rho^*E\cong f^*(TS^d).}
\tag{11}
\]
When d is even, \(e(TS^d)\) evaluates to \(\chi(S^d)=2\); the degree-one map f therefore gives \(\langle\rho^*e(E),[S^d]\rangle=2\). Pullback of a generator of \(H^d(Q;\mathbb Z_\alpha)\cong\mathbb Z\) to the sphere multiplies its top pairing by two, because \(\rho\) has twisted covering degree two. Thus \(e(E)\) evaluates to \(+1\) with compatible orientations.

When d is odd, the mod-two reduction of the twisted Euler class equals \(w_d(E)=\alpha^d\ne0\). The reduction map from \(H^d(Q;\mathbb Z_\alpha)\cong\mathbb Z/2\) onto top mod-two cohomology is an isomorphism in this degree, so \(e(E)\) is its unique nontrivial element. \(\square\)

**Corollary 5 (signed positive-collision index in even cube dimensions).** For even \(n\ge4\), a transverse equivariant perturbation of the positive-prefix difference section has finitely many antipodal collision orbits, carrying coherent local *integer* indices. The signed sum is
\[
\boxed{\sum_{\text{collision orbits}}\operatorname{ind}([z])=+1.}
\tag{12}
\]
For odd n, the corresponding signed local indices have orientation monodromy, and the canonical global total is their odd parity rather than an integer.

*Proof.* When n is even, \(d=n-2\) is even, and the orientation systems of E and the base Q agree. Therefore every transverse section zero carries an index in a globally consistent orientation convention, and the sum evaluates \(e(E)\) on the twisted fundamental class. Theorem 4 gives +1. When n is odd, the Euler group is \(\mathbb Z/2\); its nonzero class yields the odd parity in Theorem 2. \(\square\)

**Corollary 6 (contrast with the local oriented Grassmannian obstruction).** In dimensions \(n\ge6\), the top-cell homotopy obstruction in the *oriented two-plane Grassmannian* obeys
\[
\pi_{n-3}(\widetilde{\operatorname{Gr}}_2(\mathbb R^{n-1}))
\cong \mathbb Z/\chi(S^{n-2})\mathbb Z
=
\begin{cases}
\mathbb Z/2,&n\text{ even},\\
\mathbb Z,&n\text{ odd}.
\end{cases}
\]
This has the opposite dimension-parity pattern from (10). Thus the integer signed collision number in even dimensions is finer than the mod-two class retained by the local Grassmannian projection; preserving it requires a suitable framed or orthogonal-section lift. Conversely, in odd dimensions, local integer cell degrees can be moved by three-block carrier surgery, while the global collision obstruction records only their total parity.

**Scope.** This is an integral strengthening of the universal topological obstruction, not yet a coloring-specific contradiction. The signed count is determined already by the odd prefix-sum map and is therefore compatible with colorings that possess many monochromatic antipodal paths. Any intended use in NORI1 needs a new theorem tying the local indices to constraints imposed by edge colors and their root changes.

#### Sharpness benchmark: every top facet can have degree one without coloring

The universal hypotheses (1) contain a distinguished *color-independent* rank selection,
\[
\boxed{p(\pi)=1,\qquad q(\pi)=n-1\quad\text{for every full order }\pi.}
\tag{13}
\]
It obeys the reversal rule for all \(n\ge3\). This model realizes the parity obstruction on every top two-block facet simultaneously.

**Theorem 7 (universal facet-barycenter coincidences).** For the ranks (13), every top permutahedral facet \(F_A\), indexed by a nonempty proper \(A\subset[n]\), has a positive-prefix collision at its barycenter \(b_A\). More precisely, with \(a=|A|\), \(b=n-a\) and \(T_A=\mathbf1_A-(a/n)\mathbf1\),
\[
\boxed{X(b_A)=\frac1aT_A,\qquad
Y(b_A)=\frac1bT_A.}
\tag{14}
\]
Moreover, every local two-block contraction degree satisfies
\[
\boxed{\delta_A=1\pmod2.}
\tag{15}
\]
Hence the collision parity from Theorem 3 is already witnessed by the odd count of top-facet pairs
\[
\boxed{\#\{F_A,F_{A^c}\}=2^{n-1}-1\equiv1\pmod2.}
\tag{16}
\]

*Proof.* On F_A, the first member of an ordering is uniformly distributed among the a members of A, while the final member is uniformly distributed among the b members of its complement B. Because \(Z_1(\pi)=e_{\pi_1}-(1/n)\mathbf1\) and \(Z_{n-1}(\pi)=(1/n)\mathbf1-e_{\pi_n}\), averaging the vertex labels gives
\[
X(b_A)=\frac1a\mathbf1_A-\frac1n\mathbf1
=\frac1aT_A,
\]
\[
Y(b_A)=\frac1n\mathbf1-\frac1b\mathbf1_B
=\frac1bT_A.
\]
This proves (14).

If \(2\le a,b\), the selected ranks satisfy \(1<a<n-1\). The established variable-prefix two-block product degree theorem therefore gives \(\delta_A=1\). If a=1, the first-prefix vector X is constant on F_A, equal to T_A, and the contracted map H_A is a positive multiple of the B-part of \(Y=Z_{n-1}\), the centered last-prefix vector on the permutahedron \(P_B\). Its normalized boundary map has degree \(\pm1\) by the standard permutahedral prefix degree theorem. If b=1, the symmetric argument uses the A-part of \(X=Z_1\), again obtaining degree \(\pm1\). Thus every cut has degree one modulo two. There are \(2^n-2\) proper nonempty subset-indexed facets, paired without fixed facets by complementation, giving (16). \(\square\)

**Consequences for proof strategy.** The universal odd collision count, even accompanied by a nonzero local obstruction on *every* top cell, cannot force a monochromatic geodesic without additional coloring identities: model (13) provides all these topological features without reference to edge or triple colors. For ordinary boundary triple colorings, first/last switch ranks must lie in \(\{2,\ldots,n-2\}\), so this illustrative selection is excluded by the switch window; additional restrictions like these, adjacent-exchange coloring constraints, and coherent root changes must be central in any closure argument.
