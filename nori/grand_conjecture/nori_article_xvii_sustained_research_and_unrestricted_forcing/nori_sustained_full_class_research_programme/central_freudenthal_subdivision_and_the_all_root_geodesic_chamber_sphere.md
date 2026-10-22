# Central Freudenthal subdivision and the all-root geodesic chamber sphere

# Central Freudenthal subdivision and the all-root geodesic chamber sphere

Let \(Q_n=\{0,1\}^n\), \(n\ge2\), be the discrete cube and \(B=[0,2]^n\) its geometric realization with outer vertices \(2x\), \(x\in Q_n\). Put \(\mathbf1=(1,\ldots,1)\). Partition \(B\) into \(2^n\) unit cubes
\[
B_x=\prod_{i=1}^n[x_i,x_i+1]\qquad(x\in Q_n).
\tag{1}
\]
Give each \(B_x\) the Freudenthal triangulation in which each axis points from its outer vertex \(2x\) toward the shared center \(\mathbf1\).

## Full face flags and original-cube geodesics

For \(\pi=(\pi_1,\ldots,\pi_n)\in S_n\), let \(S_k=\{\pi_1,\ldots,\pi_k\}\), \(S_0=\varnothing\), and define
\[
b_k(x,\pi)_i=
\begin{cases}
1,&i\in S_k,\\
2x_i,&i\notin S_k.
\end{cases}
\qquad
\sigma(x,\pi)=\operatorname{conv}\{b_0,\ldots,b_n\}.
\tag{2}
\]
Here \(b_0=2x\), \(b_n=\mathbf1\).

**Theorem 1 (all-root central triangulation).** The simplices \(\sigma(x,\pi)\) and their faces triangulate \(B\), and the resulting triangulation is the barycentric subdivision \(\operatorname{sd}B\) of its cubical face complex. There are \(2^n n!\) maximal simplices, and \(3^n\) subdivision vertices.

*Proof.* Let \(F_k(x,\pi)\) be the face of \(B\) whose free directions are \(S_k\), with all remaining entries fixed to their values in \(2x\). Its barycenter is \(b_k(x,\pi)\), and
\[
F_0(x,\pi)\subsetneq F_1(x,\pi)\subsetneq\cdots\subsetneq F_n(x,\pi)=B.
\]
Every maximal face flag starts at a unique outer vertex \(2x\) and frees the \(n\) directions in a unique order \(\pi\). Hence these are all the barycentric maximal simplices, including the natural induced identifications on adjacent unit cubes. The number of nonempty faces of \(B\), counting \(B\) itself, is \(\sum_{k=0}^n\binom nk2^{n-k}=3^n\). \(\square\)

Encode each flag by the sequence of **original cube vertices**
\[
u_k(x,\pi)=x\oplus\mathbf1_{S_k},\qquad 0\le k\le n.
\tag{3}
\]
It gives the full directed antipodal geodesic
\[
P(x,\pi):u_0=x\to u_1\to\cdots\to u_n=\bar x.
\tag{4}
\]
Every original direction is used once; every such rooted geodesic occurs once. The geometric edges between the face barycenters \(b_k\) are encoding edges of the subdivision. The edges whose colors matter for NORI1 are the original edges \(\{u_{k-1},u_k\}\) of (4).

## Antipodal link sphere and all codimension-one exchanges

Set \(L_n=\operatorname{lk}_{\operatorname{sd}B}(\mathbf1)=\operatorname{sd}(\partial B)\). Then
\[
\operatorname{sd}B=\mathbf1*L_n,\qquad |L_n|\cong S^{n-1}.
\tag{5}
\]
Its \(2^n n!\) maximal \((n-1)\)-simplices (chambers) are indexed by the pairs \((x,\pi)\) above. Central reflection \(\rho(z)=2\mathbf1-z\) acts freely on \(L_n\) and satisfies
\[
\rho\,\sigma(x,\pi)=\sigma(\bar x,\pi).
\tag{6}
\]
The orbit space is a triangulated \(\mathbb RP^{n-1}\).

**Theorem 2 (chamber facet identifications).** Every facet adjacency in \(L_n\) is one of the following:
\[
r_0(x,\pi)=(x\oplus e_{\pi_1},\pi),
\quad
r_k(x,\pi)=(x,s_k\pi),\quad 1\le k<n,
\tag{7}
\]
where \(s_k\) interchanges the entries at positions \(k,k+1\). The first adjacency is a root slide across the first original edge of (4). The second replaces the two successive edges in directions \(\pi_k,\pi_{k+1}\) with the other two-edge route around their cube square, preserving all original edges before and after those two positions.

*Proof.* A chamber of \(L_n\) is \(F_0\subsetneq\cdots\subsetneq F_{n-1}\). Omitting \(F_0\) leaves the first one-dimensional face \(F_1\), whose two possible starting vertices differ by direction \(\pi_1\). Omitting \(F_k\), \(1\le k<n\), leaves a rank-two face interval \(F_{k-1}\subsetneq F_{k+1}\) with two intermediate faces, obtained by the two orders of the freed directions. Reading their original-cube vertex sequences (3) proves all edge-incidence assertions. \(\square\)

## Original edge coloring and the open labeling problem

For an arbitrary binary edge coloring \(c:E(Q_n)\to\mathbb F_2\) with \(c(\bar e)=1-c(e)\), define the chamber color word
\[
w_k(x,\pi)=c(\{u_{k-1}(x,\pi),u_k(x,\pi)\}),\qquad1\le k\le n.
\tag{8}
\]
All appearances of a shared original edge in different chambers receive its single specified color. The geometric involution (6) yields
\[
w(\bar x,\pi)=\mathbf1-w(x,\pi).
\tag{9}
\]
Reversing the dimension order while keeping the original root fixed is a second operation:
\[
w(x,\pi^{\mathrm{rev}})=\mathbf1-\operatorname{rev}w(x,\pi).
\tag{10}
\]
Both identities hold without any restriction on nonlinear dependence of \(c\).

The geometry admits a useful odd labeling of the **dual chamber vertices** under the hypothetical absence of monochromatic full geodesics. Such absence also excludes one-change full geodesics: moving the root to their change point and cyclically shifting their direction order gives a monochromatic geodesic, since the formerly initial run reappears in antipodal edges of the complementary color.

Let \(t_2(x,\pi)\in\{2,\ldots,n-1\}\) denote the position between edges at which the second color change occurs, and put
\[
\lambda(x,\pi)=(-1)^{w_1(x,\pi)}t_2(x,\pi).
\tag{11}
\]

**Proposition 3 (odd dual-edge labeling).** Under the hypothetical absence of monochromatic antipodal geodesics, \(\lambda(\bar x,\pi)=-\lambda(x,\pi)\). No facet-adjacent chambers of \(L_n\) have opposite signed labels of equal magnitude.

*Proof.* Antipodality complements colors and preserves change positions. The \(r_0\) exchange and each \(r_k\), \(k\ge2\), preserve the first original edge, so they preserve the sign. For \(r_1\), original edges in positions \(3,\ldots,n\) coincide. Were the two initial colors opposite and their second change position the same \(t\), their colors at the common edge in position \(t+1\ge3\) would equal their respective initial colors, a contradiction. \(\square\)

The dual cellulation has higher-dimensional cells; the preceding dual-edge condition alone does not extend \(\lambda\) to an antipodally equivariant map to \(S^{n-3}\). A useful completion must resolve the higher-dimensional attaching maps using the same globally consistent original edge colors and legal square/root-slide exchanges. This is an open forcing step. The triangulation and its full geodesic decoding, by contrast, hold for every \(n\ge2\) independently of \(c\).


## Rectified-cube degree-one projection

Let \(X_n\) be the regular dual cellulation of the all-root Freudenthal link sphere. Let \(R_n=\operatorname{conv}\{m(e):e\text{ an original cube edge}\}\), the rectified cube, with boundary another antipodal \((n-1)\)-sphere. Define on dual chamber vertices
\[
\Phi(x,\pi)=m(e_1(x,\pi)).
\]

**Theorem.** This map extends antipodally over \(X_n\) to \(\partial R_n\), with degree \(\pm1\).

*Carrier proof.* Every dual cell is indexed by a nonempty partial face flag. If its smallest prescribed face is a vertex \(x\), all first original edges in its full-flag refinements meet \(x\); their midpoints lie in the simplex facet \(H_x\) of \(R_n\). Otherwise all such first edges lie in the smallest prescribed face \(F\), which is a proper cube face; their midpoints lie in a proper facet of \(R_n\) inherited from a fixed outer-cube bit. Therefore each dual cell's chamber images lie in one convex boundary face. Send its barycenter to the arithmetic mean of its chamber images, and interpolate over chains of nested dual cells. Every subdivision simplex is carried by the convex boundary face of its largest dual cell. This builds the equivariant continuous extension.

*Degree proof.* The top dual cell \(D_x\) at an original cube vertex is the permutohedron \(P_n\). Its image is in \(H_x\cong\Delta^{n-1}\), and its permutation vertex \(\pi\) maps to simplex vertex \(\pi_1\). A facet \(F_A\) of \(P_n\) with the nonempty proper set \(A\) placed ahead of its complement maps into \(\Delta_A\). The map of pairs \(P_n\to\Delta^{n-1}\) has degree \(\pm1\): the case \(n=2\) is a segment mapping endpoints to endpoints; for \(n>2\), take a target simplex facet \(\Delta_A\), \(|A|=n-1\). Only \(F_A\) among the source facets can meet its relative interior, and \(F_A\cong P_{n-1}\) restricts to the same first-entry construction, proving the degree by induction.

Because \(H_x\) is a supporting facet, a generic point in its relative interior can only have preimages among dual simplices supported on first original edges incident at \(x\). These contributing simplices belong to the root dual cell \(D_x\); non-root dual cells supported on one incident edge map to the boundary of \(H_x\). The global degree of \(\Phi\) is consequently the local relative degree \(\pm1\). Hence \(\Phi\) is a homotopy equivalence. \(\square\)

Original antipodally odd edge signs extend by barycentric face averaging to an odd scalar field on \(\partial R_n\). Pulling it back through \(\Phi\) recovers the first-edge color signs at dual chamber vertices and represents the nonzero projective \(w_1\) interface. This degree-one construction imposes no assumption on nonlinear edge-color dependence.


## Intermediate edge positions have no analogous convex boundary-face carrier

The direct extension of the preceding map to edge position \(k\), \(2\le k\le n-1\), fails its essential face-carrier property even on one root permutohedron \(D_x\). Represent the outer vertex \(x\) by its sign vector \(r_x\in\{\pm1\}^n\). The midpoint of the \(k\)-th original edge of a rooted full geodesic has \(k-1\) entries equal to \(-r_x\), one zero entry, and \(n-k\) entries equal to \(r_x\). Averaging uniformly over all \(n!\) direction orders gives
\[
\boxed{\frac1{n!}\sum_{\pi\in S_n}m(e_k(x,\pi))
=\frac{n-2k+1}{n}\,r_x.}
\]
For every intermediate \(k\), all entries have absolute value strictly below one, and the \(\ell_1\)-norm is at most \(n-3<n-1\). By the known rectified-cube formula
\[
R_n=[-1,1]^n\cap\{y:\sum_i|y_i|\le n-1\},
\]
this average lies in its interior.

**Proposition.** For \(2\le k\le n-1\), the set of midpoints of the \(k\)-th original edges of all complete geodesics rooted at \(x\) is contained in no proper face of \(R_n\).

*Proof.* Their arithmetic mean lies in the interior of \(R_n\), whereas the convex hull of a subset of a proper face remains in that face. \(\square\)

Thus the first-edge projection has a special positive carrier property: arbitrary complete refinements of a nonempty partial face flag have initial edges within one proper rectified face. Intermediate original-edge positions violate that same property. This is a method obstruction to a face-convex extension, not a nonexistence statement for arbitrary equivariant continuous maps. It isolates the need for additional color-aware and dimension-support-aware compatibility if a multi-position map is to force the monochromatic geodesic required by NORI1.


## The unique essential color interface and its exchange disks

Let \(n\ge3\). Put \(Y=\partial R_n/\tau\cong\mathbb RP^{n-1}\). Assign the sign \((-1)^{c(e)}\) to each original edge midpoint of \(R_n\); choose a generic odd PL extension \(f_c\) on \(\partial R_n\), linear along its original edges. Its quotient zero hypersurface \(Z=f_c^{-1}(0)/\tau\) represents \(\operatorname{PD}(w_1)\), the Poincaré dual of the covering class.

**Theorem 5 (unique essential interface).** Precisely one connected component \(Z_*\) of \(Z\) has nonzero class in \(H_{n-2}(Y;\mathbb F_2)\). Moreover
\[
[Z_*]=\operatorname{PD}(w_1),\qquad
\langle w_1^{n-2},[Z_*]\rangle=1.
\]
Its antipodal inverse image is connected and has cohomological covering index \(n-2\).

*Proof.* Write \(Z=\bigsqcup C_i\). The sum of their fundamental classes equals the nonzero \(\operatorname{PD}(w_1)\), so an odd number of them represent the nonzero element of \(H_{n-2}(Y;\mathbb F_2)\cong\mathbb F_2\). If two disjoint components both did, their Poincaré duals would both equal \(w_1\), so their cup product would equal \(w_1^2\ne0\) for \(n\ge3\). Disjoint hypersurfaces have zero intersection product, contradiction. Thus precisely one component is essential. Its stated pairing equals \(\langle w_1^{n-1},[Y]\rangle=1\). The restriction of \(w_1\) to \(Z_*\) has nonzero top power, so the corresponding double cover is connected and has index \(n-2\). \(\square\)

A full original-cube geodesic \(P\) with edge sequence \(e_1,\ldots,e_n\) determines an essential length-\(n\) projective rectified cycle \(\gamma_P\), whose lift follows \(m(e_1),\ldots,m(e_n),m(\bar e_1)\). For the original color word \(w_1,\ldots,w_n\) its interface crossing count is
\[
\boxed{m(P)=\sum_{j=1}^{n-1}[w_j\ne w_{j+1}]+[w_n=w_1].}
\]
The count is always odd. It equals one precisely for words with zero or one change; a cyclic root slide converts the one-change case to a monochromatic full geodesic. Every complete \(P\) satisfies
\[
|\gamma_P\cap Z_*|\equiv1\pmod2,\qquad
|\gamma_P\cap C|\equiv0\pmod2\quad(C\ne Z_*),
\]
because each \(\gamma_P\) represents the generator of \(H_1(Y;\mathbb F_2)\).

**Proposition 6 (original-square exchange disk).** If two full geodesics differ by swapping adjacent directions \(i,j\), the changed portions of their projective rectified cycles bound a local 2-chain consisting of one rectified original-square face and two incident original-vertex star triangles.

*Proof.* The four edges of the \(\{i,j\}\)-square between the common cube vertices \(u\) and \(v=u\oplus e_i\oplus e_j\) yield the four vertices of a square 2-face of \(\partial R_n\). The predecessor original edge at \(u\), together with the two competing first square edges, forms a star triangle. The successor edge at \(v\), together with the two competing final square edges, forms another star triangle. These three faces form a disk whose outer boundary consists of the two alternative rectified paths between the predecessor and successor edge midpoints. At the first and final path positions, use the antipodally doubled cyclic edge word to identify the predecessor or successor across the closing seam. Projection gives the stated 2-chain in \(Y\). \(\square\)

Intersecting this exchange disk with the zero locus of the color section gives a mod-two 1-chain whose boundary is the symmetric difference of crossing 0-chains on the two competing arcs. Thus square exchanges give explicit crossing cobordisms preserving componentwise intersection parity. The root-flip chamber generator also admits such a cobordism: cyclically rotate the projective geodesic by one step (leaving its unoriented projected cycle unchanged), then return the displaced first direction from the last position to the first by \(n-1\) successive adjacent exchanges.

**Research status.** The unique \(Z_*\) identifies the mandatory crossing component; all extra crossings occur in pairs in the componentwise mod-two count. Crossing cobordisms may join two crossings on the same path, so they provide no canonical selector and no guaranteed cancellation by a new shortest cycle. The next mathematical obligation is to convert selected mod-two crossing-pair cobordisms into legal, length-preserving square exchanges, retaining the use of each original direction once. The higher-dimensional coherence needed for that conversion remains open.


## One-sided essential color interface and the systolic obstruction

Write \(Y=\partial R_n/\tau\cong\mathbb RP^{n-1}\), \(n\ge3\). Let \(Z\subset Y\) be the transverse zero hypersurface of a generic odd PL sign-field interpolating the original edge colors. By the preceding theorem there is a unique essential connected component \(Z_*\), with \(w_1^{n-2}|_{Z_*}\ne0\).

**Theorem 7 (one-crossing essential continuous loop).** There exists a projectively essential loop \(\gamma\subset Y\) intersecting \(Z\) transversely in one point of \(Z_*\).

*Proof.* The normal bundle of \(Z\) in \(Y\) is the restriction of the antipodal sign line bundle. Since \(w_1|_{Z_*}\ne0\), choose a loop \(\alpha\subset Z_*\) with nontrivial normal-line monodromy. Its narrow normal tube is a Möbius strip. A loop running around its base and moving transversely through the zero section once gives \(\gamma\), with tube chosen disjoint from the other components of \(Z\). Its intersection number with \(Z\) is one, so \(\langle w_1,[\gamma]\rangle=1\). \(\square\)

This is a statement about continuous essential loops. NORI1 demands a *shortest essential cycle of length \(n\)* in the original rectified graph, because those and only those decode to direction-once antipodal cube geodesics. The one-sided-interface theorem supplies no control on the length of the resulting loop.

## Complete local color-change criterion under a square exchange

Two rooted full geodesics related by an adjacent transposition have common predecessor and successor original edges in their doubled antipodal cyclic rectified words. Write their colors as \(a,b\). Let \(p,q\) and \(r,s\) be the two alternative intervening square-route color pairs. The changing portions of the projective interface crossing numbers are
\[
V(a,p,q,b)=(a\oplus p)+(p\oplus q)+(q\oplus b),
\qquad
V(a,r,s,b),
\tag{15}
\]
where the XOR bits are interpreted as integers. The closing edge, when involved, is represented by its antipodal counterpart.

**Proposition 8 (local two-crossing criterion).** The difference of these two numbers belongs to \(\{-2,0,2\}\). If \(a=b\), then \(V=0\) if and only if \(p=q=a\), and otherwise \(V=2\). If \(a\ne b\), then \(V=3\) if and only if \(p=1-a,q=a\), and otherwise \(V=1\).

*Proof.* The parity of the number of changes in a four-bit word is \(a\oplus b\). Equal endpoints permit zero or two changes; zero requires every bit equal. Distinct endpoints permit one or three changes; three requires full alternation. The formulas follow. \(\square\)

**Necessary conditions at a globally minimum-crossing geodesic.** For every adjacent square exchange, (i) when its two unchanged outer colors agree, a nonmonochromatic chosen middle pair cannot have an alternative middle pair both of that outer color; (ii) when its outer colors differ and its chosen four-bit word alternates, the alternative word must also alternate. These square restrictions are valid for arbitrary nonlinear, shared-edge-consistent antipodally odd colorings. The desired dimension-uniform step is to combine such conditions along the entire root-and-permutation exchange complex and rule out a global minimizer with at least three cyclic crossings. That remains unproved.


## Checkerboard rectified squares and a three-sheet topological countermodel

A square face of the rectified cube arises from the four original edges bordering one original 2-face. Its opposite vertices represent disjoint parallel original edges. Suppose the two \(i\)-edges are red and the two \(j\)-edges are blue. Then the rectified-square vertex signs alternate around its boundary.

**Proposition 9 (forced added adjacency).** Any triangulation of this square using only its four existing vertices contains a diagonal joining two vertices of the same color whose original cube edges are disjoint. Thus connectivity of a monochromatic PL vertex region in such a triangulation need not decode to connectivity in the original line graph.

*Proof.* The two possible diagonals join the two vertices corresponding to parallel original edges: either the red \(i\)-edges or the blue \(j\)-edges. Parallel edges of the original square have no common endpoint and are nonadjacent in its line graph. The diagonal introduces the claimed edge. \(\square\)

Under antipodality the corresponding opposite square has complementary vertex colors, so a centrally symmetric triangulation carries this same-color diagonal phenomenon in the complementary color there. A singular checkerboard interpolation, locally modeled by \(f(s,t)=st\), instead leaves both positive quadrants and both negative quadrants separated, with two zero branches meeting in a node. Regularizing the node reconnects one color region through the new corridor.

**Proposition 10 (three essential sheets are compatible with the odd covering class).** In every \(\mathbb RP^{n-1}\), \(n\ge3\), choose three distinct projective hyperplanes \(H_1,H_2,H_3\), obtained as zeros of linearly independent real linear forms \(\ell_1,\ell_2,\ell_3\) when \(n\ge3\) (for \(n=3\), three distinct projective lines). The odd scalar field
\[
f(u)=\ell_1(u)\ell_2(u)\ell_3(u),\qquad u\in S^{n-1},
\]
has projective zero locus \(H_1\cup H_2\cup H_3\), whose mod-two fundamental class is \(\operatorname{PD}(w_1)\). Yet every projectively essential loop transverse to the three hyperplanes and avoiding their mutual intersections meets each \(H_i\) an odd positive number of times, so it has at least three total zero crossings.

*Proof.* Each \(H_i\) represents \(\operatorname{PD}(w_1)\); their mod-two sum represents \(3w_1=w_1\). Every essential loop evaluates \(w_1\) to one and therefore has an odd intersection number with every \(H_i\). Avoiding their mutual intersections makes the intersections distinct, giving at least three. \(\square\)

This model is an unrestricted odd scalar field on the projective sphere; it is not claimed to arise from a NORI1 cube-edge coloring. It demonstrates why the nonzero projective class and connectedness of a singular interface alone do not yield an essential shortest loop with one crossing. A generic smoothing can create corridors through which continuous loops reduce the intersection count, but these corridors need not follow original line-graph edges. The NORI-specific forcing obligation must use the shared original cube-edge assignments, legal two-direction square exchanges, and full-direction path decoding to prevent such multi-sheet obstruction on the discrete systolic gallery.


## A dimension-uniform trapped plateau for cyclic crossing descent

For even \(n\ge6\) use the legal flat coloring \(c_i^*(x)=\sum_{k\ne i}x_k\pmod2\). Choose distinct directions \(i,j\), and reverse its colors on the single original edge \(e=\{e_j,e_j+e_i\}\) and its antipodal mate, yielding another legal coloring \(c\). For any full geodesic let \(M(P)\) count changes on its doubled antipodal cyclic edge word in one projective period.

**Theorem (neutral plateau with an uphill boundary).** The set
\[
\mathcal C_{ij}=\{P(0,\pi):\pi_{n-1}=i,\ \pi_n=j\}
\]
is a connected component of the full Coxeter chamber sublevel graph \(M\le n-3\). It consists of \((n-2)!\) chambers, all of crossing count \(n-3\); every chamber neighbor outside the set has count \(n-1\). Nevertheless \(c\) has a monochromatic full antipodal geodesic elsewhere.

*Proof.* For the flat coloring, every zero-root complete path has word \(0101\cdots01\), hence \(M=n-1\). In \(\mathcal C_{ij}\), the direction-\(i\) edge in position \(n-1\) is \(\bar e\). Flipping its bit changes the terminal triple \(101\) into \(111\), removing two crossings, hence \(M=n-3\). Swaps among the first \(n-2\) directions preserve this changed edge and connect the \((n-2)!\) chambers. Swapping positions \(n-2,n-1\) moves \(i\) to position \(n-2\), where its edge has \(n-3\) other bits set. Swapping positions \(n-1,n\) moves \(i\) to last, where it has \(n-1\) other bits set. Neither edge is \(e\) or \(\bar e\), which have respectively \(1,n-2\) other bits set. Both neighboring paths therefore retain the alternating flat word and have \(M=n-1\).

The remaining root-flip chamber generator changes the root from \(0\) to \(e_{\pi_1}\), with \(\pi_1\notin\{i,j\}\). It avoids both changed edges, because the direction-\(i\) edge is encountered with \(n-3\) other bits set. Its flat word begins \(00101\cdots0\), with \(n-2\) internal switches plus the closing switch, giving \(M=n-1\). These exhaust the chamber adjacencies and prove the trapped-component assertion.

To obtain a monochromatic path, take a root \(x\) with \(|x|=n/2\) and \(x_i=0\), then order dimensions starting with \(i\) so the root bits follow \(0101\cdots01\). The flat word is constant, by \(w_r=|x|+x_{\pi_r}+(r-1)\). Its only direction-\(i\) edge is first, with \(n/2\) other bits set, and hence avoids \(e,\bar e\). All other directions are unmodified. This remains monochromatic in \(c\). \(\square\)

Thus a nonincreasing path of individual chamber exchanges cannot necessarily escape an elevated neutral plateau, even for a legal coloring differing from a flat coloring on just one antipodal edge orbit. Any proof via descent must use nonmonotone moves or global information connecting distinct sublevel components.


## Fork coherence reduces to curvature on a three-face

The root-directed two-fork data contain more information than curvature on one square, but their proposed scalar degree-three Bockstein defect introduces no independent cubical data. For a three-face with varying directions \(i,j,k\) and lower corner \(x\), write \(\kappa_{ij}(x)\) for the square curvature at the lower \(ij\)-face. Then
\[
\boxed{\Theta_{ijk}(x)=\kappa_{ij}(x)+\kappa_{ik}(x)+\kappa_{jk}(x).}
\]
Expanding gives the parity of the six original middle-layer edges of the three-face:
\[
\Theta_{ijk}(x)=c_i(x^j)+c_i(x^k)+c_j(x^i)+c_j(x^k)+c_k(x^i)+c_k(x^j).
\]
Indeed the three lower square boundaries contain each edge incident to the lower cube vertex twice and each middle-layer edge once. The upper three faces give the same sum since \(d\kappa=0\). The resulting antipodally invariant scalar three-cochain is closed: in any four-face, each relevant edge between relative Hamming levels one and two, or two and three, appears in two of its three-face middle hexagons. Hence \(\delta\Theta=0\).

The familiar local-coefficient connecting homomorphism identifies its projective class as \([\Theta]=w_1\smile[\bar\kappa]\), yielding \(w_1^3\) for odd \(n\ge5\), and zero for even \(n\). In particular, when curvature vanishes pointwise, so does the middle-hexagon defect. It does not detect the previously established rank-three zero-switch-prefix obstruction on flat cubes. A higher-order NORI1 proof requires root- and path-order-sensitive fork data beyond this scalar curvature Bockstein.


## Two checkerboard faces give nonzero second-switch winding on a dual square

Consider a dual Coxeter square generated by commuting swaps of path positions \(1,2\) and \(3,4\), with the rooted initial vertex and all other direction positions fixed. Suppose the corresponding two original cube squares are checkerboard squares, so their alternative two-edge routes have color pairs \((a,1-a)\), \((1-a,a)\) and \((b,1-b)\), \((1-b,b)\), respectively.

**Theorem (dual-square winding).** At its four vertices the first four original edge colors are
\[
(a,1-a,b,1-b),\qquad a,b\in\mathbb F_2.
\]
The second switch is at position 2 if \(a=b\), and at position 3 otherwise. The four signed-second-switch labels are
\[
(0,0)\mapsto+e_2,\quad
(0,1)\mapsto+e_3,\quad
(1,0)\mapsto-e_3,\quad
(1,1)\mapsto-e_2.
\]
In the cyclic order of the commuting-swap dual square, these labels wind once around the signed-basis diamond \(\partial\operatorname{conv}\{\pm e_2,\pm e_3\}\). For \(n=4\), this is an attaching degree of \(\pm1\), so the second-switch boundary labeling cannot extend over this individual dual 2-cell with target \(S^1\).

*Proof.* Each two-edge route is mixed, producing unavoidable switches at positions 1 and 3. The middle transition occurs precisely when \(a=b\), giving the asserted second-switch positions and labels. The commuting swaps change either \(a\) or \(b\), so the four labels traverse the four successive vertices of the target diamond. In higher dimensions the same circle lies in \(S^{n-3}\), where its loop is contractible for \(n\ge5\). \(\square\)

**Flat, legally odd realization in dimension four.** Let each subscript of \(c\) name its edge direction. Set
\[
c_1(x)=1+x_2,\qquad c_2(x)=1+x_1,\qquad
c_3(x)=x_4,\qquad c_4(x)=x_3.
\tag{20}
\]
Each function ignores its edge direction bit and changes under cube antipodality. All two-face curvatures vanish, since the cross-differences occur in symmetric pairs.

At root \(0000\), hold fixed the first two direction set \(\{1,3\}\) and the last two set \(\{2,4\}\). The resulting dual square has:
\[
\begin{array}{c|c|c}
\text{order}&\text{four-edge color word}&\text{signed second-switch label}\\\hline
1324&1001&-e_3\\
1342&1010&-e_2\\
3142&0110&+e_3\\
3124&0101&+e_2
\end{array}
\]
The indicated boundary order has degree \(\pm1\), while the four signed color-word vectors average to zero.

Every full root-\(0000\) geodesic has at least two switches: its ordered color subsequence in directions \(\{1,2\}\) is always \(1,0\), and its ordered subsequence in directions \(\{3,4\}\) is always \(0,1\), regardless of interleaving. No binary word with at most one switch contains both patterns as ordered subsequences. Nonetheless the full path with root bits \(x=(0,1,1,0)\) and direction order \(1234\) has color word \(0000\), so the full unrestricted conjecture holds for this coloring.

This demonstrates a nonzero *local* attaching obstruction in a legal coloring which has a monochromatic full path elsewhere. Therefore a proof cannot fill each exceptional dual cell using only its internal original-edge assignments: the forced global compatibility must connect such local winding to chambers at other roots. This phenomenon is not detected by ordinary square curvature, which is zero in this example.


## A Borsuk-Ulam fractional profile certificate on one dual cell

For a rooted complete geodesic \(P\), let \(s(P)\in\{\pm1\}^n\) be its signed color word, \(s_k(P)=(-1)^{c(e_k(P))}\). Cube antipodality gives \(s(\tau P)=-s(P)\). Put
\[
W=\{z\in\mathbb R^n:\sum_{k=1}^nz_k=0\},\qquad
\operatorname{pr}(z)=z-\frac1n(\sum_k z_k)\mathbf1.
\]

**Theorem (fractional common-position color balance).** For every legal antipodally odd edge coloring of \(Q_n\), \(n\ge2\), there exists a nonempty dual cell \(D\) of the all-root Freudenthal chamber sphere and a probability distribution on at most \(n\) chamber vertices \(P\in V(D)\) such that
\[
\boxed{\sum_P\lambda_Ps_k(P)=t\quad\text{for every }k\in[n]}
\tag{21}
\]
for one scalar \(t\in[-1,1]\). In other words, the randomized complete geodesic has the same edge-color probability at all step positions. All paths in the support refine the same partial flag of proper original cube faces.

*Proof.* On each vertex \(P\) of the dual sphere \(X_n\cong S^{n-1}\) put the vector \(\operatorname{pr}s(P)\in W\). For each nonempty dual cell \(D\), assign to its barycenter the arithmetic mean of these vectors over its chamber vertices. Extend affinely over the barycentric subdivision of \(X_n\). This makes a continuous odd map \(F:X_n\to W\cong\mathbb R^{n-1}\), since the antipode complements each entire color word and permutes the dual cells. Borsuk-Ulam guarantees a zero \(z\in X_n\).

Choose a barycentric-subdivision simplex containing \(z\), corresponding to a chain of nested dual cells. Its largest cell \(D\) contains all chamber vertices used in the barycentric averages of that simplex. Consequently \(0=F(z)\) belongs to the convex hull of \(\{\operatorname{pr}s(P):P\in V(D)\}\). Caratheodory's theorem in \(W\) selects at most \(n\) of these vectors with convex weights yielding zero. Their unprojected signed profile average lies in the kernel of \(\operatorname{pr}\), which is the constant-vector line; this proves (21). \(\square\)

Under a hypothetical NORI1 counterexample, \(t\) must lie strictly between \(-1\) and \(1\); otherwise every positive-weight path has a constant monochromatic signed color word. Thus the support of any fractional certificate in such a counterexample must exhibit both colors at every step position. The theorem strengthens the ordinary all-position variation obstruction to a common *equal-marginal* mixture, while the required path-decoding step remains open.

The preceding legal flat \(Q_4\) checkerboard example shows the limitation already inside one root-fixed dual square. Its four complete words \(1001,1010,0110,0101\) have no fewer than two switches, yet their signed profile vectors average to zero. Indeed two opposite vertices of that dual square already have complementary full color profiles. Fractional balance, even among paths refining one fixed partial flag and all having multiple switches, does not imply a monochromatic full geodesic from their common root.


## Classification of exceptional commuting-square second-switch winding in rank four

Let \(D\) be a dual Coxeter 2-cell of \(Q_4\) generated by \(s_1,s_3\). It has four complete geodesic chamber vertices, formed by independently choosing either route through a first original square \(F\) (directions in path positions 1,2) and either route through a second original square \(G\) (positions 3,4). Assume each of the four resulting full color words has at least two changes, so the signed-second-switch labeling on the boundary is defined.

For an original square \(E\), put \(\alpha(E)=1\) if its four edge colors alternate around the square, and \(0\) otherwise.

**Theorem (complete local winding classification).** The mod-two winding of the signed-second-switch labels on \(\partial D\to S^1\) is
\[
\boxed{o(D)=\alpha(F)\alpha(G).}
\tag{22}
\]
In particular it is nonzero if and only if *both* separated original squares are checkerboard squares. This classification requires no restriction to affine or flat colorings.

*Proof.* Write the two ordered two-edge color pairs of \(F\) as \(A_0,A_1\), and those of \(G\) as \(B_0,B_1\). The four full words are \(A_rB_s\). Each signed second-switch label is one of \(\pm e_2,\pm e_3\).

As \(s\) changes with \(r\) held fixed, the sign of the label is fixed, since the first word bit depends only on \(A_r\). To wind nontrivially around the four-vertex target diamond, on each such side of the source square the label magnitude must change between \(e_2\) and \(e_3\), and the two sides must have opposite signs.

If either \(A_r\) is monochromatic, its first switch occurs at position 2 or later, so two switches in a four-bit word require switches at both positions 2 and 3. Its second-switch position is then always 3, independent of \(s\). Hence both first-square routes must be mixed. Opposite label signs mean their initial bits are opposite, which forces \(A_0=(a,1-a)\) and \(A_1=(1-a,a)\). Thus \(\alpha(F)=1\).

Now the first switch always occurs at position 1. For a fixed \(A_r=(a,1-a)\), the second switch occurs at position 2 when the initial bit of \(B_s\) equals \(a\), and at position 3 otherwise, provided the latter route has a second internal switch. Therefore magnitude variation with \(s\) forces the two \(B\)-routes to begin with opposite colors. In the case when no switch occurs at position 2, the requirement of at least two total switches forces the \(B\)-route to be mixed. Since both values of the first color \(a\) arise from the two first-square routes, both \(B\)-routes must be mixed. Hence \(\alpha(G)=1\).

Conversely, two checkerboard squares give the four words \((a,1-a,b,1-b)\), \(a,b\in\mathbb F_2\), with second switch at 2 when \(a=b\) and at 3 otherwise. Their signed labels traverse the target diamond once, as in the preceding theorem. \(\square\)

This gives a precise local product rule for one exceptional primary obstruction cell. It does not extend immediately to a dimension-uniform primary-obstruction formula: for \(n\ge5\) the same signed-basis circle embeds into the simply connected target \(S^{n-3}\), and local dual squares are fillable. The open higher-rank requirement is a coherent, root-sensitive assembly of these checkerboard products with the other exceptional dual cells, especially those involving the root-flip generator \(s_0\).


## Face-saturated fractional Borsuk-Ulam certificates and a dimension-uniform rounding obstruction

The earlier projected signed-color-profile argument can be localized to one *complete face carrier*, rather than an arbitrary family of chamber flags. Let \(L_n=\operatorname{sd}(\partial Q_n)\), \(X_n\) its dual cellulation, and \(D_F\) the top dual cell corresponding to the barycenter of a nonempty proper cube face \(F\) of dimension \(d\), \(0\le d\le n-1\). A chamber in \(D_F\) corresponds to a rooted antipodal geodesic whose first \(d\) directions are the free directions of \(F\), beginning at some vertex of \(F\); all its remaining directions are the directions outside \(F\). Thus the chambers through \(F\) form a parabolic coset with stabilizer \(B_d\times S_{n-d}\), and
\[
D_F\cong P(B_d)\times P(A_{n-d-1}),
\tag{23}
\]
a product of generalized permutohedra of total dimension \(n-1\). The first factor is a point when \(d=0\); the second is a point when \(n-d=1\).

For each rooted complete path \(P\), let \(s(P)\in\{\pm1\}^n\) be its **position-indexed** signed color profile and let
\[
p(s)=s-\frac1n\Bigl(\sum_{k=1}^ns_k\Bigr)\mathbf1
\in W=\mathbf1^\perp\cong\mathbb R^{n-1}.
\]
Antipodal translation sends \(s(P)\) to \(-s(P)\). Give every dual chamber vertex the value \(p(s(P))\); map each barycenter of a dual cell to the average of its chamber-vertex values, and interpolate affinely over barycentric chains of nested dual cells. The resulting map \(G:X_n\to W\) is continuous and antipodally odd. The image of each dual cell lies inside the convex hull of its chamber-vertex values.

**Theorem (one-face fractional color equality).** Every legal antipodally odd coloring admits one proper original cube face \(F\), at most \(n\) rooted complete paths \(P_1,\ldots,P_q\) passing through \(F\) at step \(d=\dim F\), and positive weights \(\lambda_1,\ldots,\lambda_q\) summing to one, such that
\[
\boxed{\sum_{\nu=1}^q\lambda_\nu s_k(P_\nu)=t
\quad(1\le k\le n)}
\tag{24}
\]
for one real \(t\in[-1,1]\).

*Proof.* By Borsuk-Ulam the odd map \(G:S^{n-1}\to\mathbb R^{n-1}\) has a zero \(z\). The top dual cells \(D_F\) cover \(X_n\), so \(z\in D_F\) for at least one proper original face \(F\). Convexity of the barycentric-chain interpolation gives \(0=G(z)\in\operatorname{conv}\{p(s(P)):P\in V(D_F)\}\). Caratheodory's theorem in the \((n-1)\)-dimensional space \(W\) gives a combination of at most \(n\) such projected profiles equal to zero. Its unprojected weighted profile is in \(\ker p=\mathbb R\mathbf1\), proving (24). The chamber description of \(D_F\) gives the common-face condition. \(\square\)

This face localization does not imply a monochromatic path. Indeed even restriction to one fixed original root, and requiring the full \(\mathbb R^n\) signed profile average to vanish, cannot force one.

**Theorem (flat paired-block rounding countermodel).** For every \(n=4h\ge4\), there is a legal globally flat antipodally odd coloring with these properties:

1. Every complete antipodal geodesic beginning at \(0^n\) has at least two changes in its edge-color word.
2. The uniform random distribution on all \(n!\) complete direction orders beginning at \(0^n\) satisfies
\[
\boxed{\mathbb E_\pi s_k(0,\pi)=0\qquad(1\le k\le n),}
\tag{25}
\]
so the unprojected signed-profile convex hull of this single root contains the origin.
3. The same coloring has monochromatic full geodesics beginning at other roots.

*Proof.* Partition the directions into \(m=n/2=2h\) disjoint ordered pairs \((i_r,j_r)\), and choose bits \(b_r\), with \(h\) zero bits and \(h\) one bits. Set
\[
\boxed{c_{i_r}(x)=b_r+x_{j_r},\qquad
c_{j_r}(x)=b_r+x_{i_r}\pmod2.}
\tag{26}
\]
Each label is independent of its own direction bit and is complemented by translating every bit of \(x\). All square curvatures vanish: each pair has the two symmetric cross-differences equal to one, and different pairs have no cross-differences.

For a complete path starting at zero, the first member of pair \(r\) traversed has color \(b_r\), and the second has color \(1-b_r\), independent of interleaving or which of the two directions is visited first. Because both values of \(b_r\) occur, every complete word contains an ordered \(0,1\) subsequence and an ordered \(1,0\) subsequence. A word with at most one switch cannot contain both, proving (1).

Under a uniform random direction permutation, conditioned on step position \(k\) belonging to pair \(r\), the partner direction has already appeared with probability \((k-1)/(n-1)\). Therefore its expected signed color is
\[
(-1)^{b_r}\Bigl(1-\frac{2(k-1)}{n-1}\Bigr).
\]
Each pair supplies two of the \(n\) directions, so the pair index is uniform. The sum of \((-1)^{b_r}\) is zero, giving (25).

Finally choose a root satisfying \(x_{i_r}=1+b_r,\ x_{j_r}=b_r\) for every pair, and traverse each \(i_r\) immediately before its \(j_r\), in arbitrary order across pairs. Both edges of each pair then have color zero; all pairs are independent. This gives the monochromatic full geodesic required in (3). \(\square\)

The model demonstrates that a fully balanced *integral-dimensional* average of signed color profiles from one root can coexist with a universal two-switch obstruction at that root; neither the fractional BU condition nor stronger coordinatewise balancing suffices to round to one monochromatic path. A dimension-uniform proof must exploit higher-order path compatibility, not just first moments in position.

**Computational investigation, not a theorem.** A distinct strengthening was tested: does *every* legal coloring have some root supporting **two** complete paths whose full position-indexed color words are complementary? Exhaustive enumeration verified this for all legal colorings of \(Q_2,Q_3,Q_4\) (respectively \(4,64,65{,}536\) antipodal edge-orbit assignments), and randomly sampled colorings in dimensions five and six also satisfied it. A general proof or counterexample is not known from this investigation. Such a two-path result would sharpen (24) by forcing an unprojected zero average of just two paths from one root. It must not be inferred from the fractional BU theorem, since antipodal convex balancing does not generally reduce to two vertices.


## Fixed-root reversal symmetry and a sharper open two-path selection problem

The full position-indexed signed profile has a useful symmetry beyond global antipodality. Fix an original cube root \(x\), and let \(\operatorname{rev}\pi\) reverse the permutation of the directions. For every legal coloring,
\[
\boxed{s(x,\operatorname{rev}\pi)
=-\operatorname{rev}s(x,\pi).}
\tag{27}
\]
The underlying original edge in position \(n+1-k\) of the reversed direction order is the antipodal mate of the original edge in position \(k\), so both the reversal of order and the complement of every bit follow without any affine coloring assumptions.

Let \(\mathcal S_x=\{s(x,\pi):\pi\in S_n\}\), and put \(p(s)=s-(\sum s_i/n)\mathbf1\).

**Proposition (full balancing from a projected fixed-root certificate).** For every fixed root \(x\),
\[
\boxed{0\in\operatorname{conv}p(\mathcal S_x)
\quad\Longleftrightarrow\quad
0\in\operatorname{conv}\mathcal S_x.}
\tag{28}
\]

*Proof.* The reverse implication is immediate. If a convex combination of profiles has projected average zero, its unprojected average equals \(t\mathbf1\). Reverse every supporting direction permutation with the same weights. By (27), the reversed combination has mean \(-t\mathbf1\). Averaging the two distributions produces a convex combination on the *same root* with mean zero in every position. \(\square\)

The formal implication from full balancing to a *two-point* complementary profile pair is false for arbitrary profile sets having only reversal symmetry. In rank four the five-word family
\[
\mathcal V=\{0011,0100,1000,1101,1110\}
\tag{29}
\]
is invariant under \(w\mapsto\mathbf1-\operatorname{rev}w\), its signed convex hull contains zero (with weights \(1/3,1/6,1/6,1/6,1/6\) in the listed order), and no two words in \(\mathcal V\) are complementary. Thus a two-path selection theorem, if true for legal cube colorings, must exploit the Boolean-lattice square-incidence rules beyond path reversal alone.

**Open root-pair question.** Does every legal coloring have some root \(x\) and two permutations \(\pi,\sigma\) with
\[
s(x,\pi)=-s(x,\sigma)?
\tag{30}
\]
Exhaustive enumeration for dimensions two through four and randomized experiments for dimensions five and six support this, but neither the face-localized Borsuk-Ulam theorem nor Proposition (28) proves it. A positive answer would yield a much sharper two-path certificate; a counterexample would expose the limitations of pairwise balancing.


## Equatorial hypersimplex reduction and balanced half-prefix forcing

A new way to express the full-geodesic target uses the middle Hamming layer of the original cube, which is a hypersimplex and has an intrinsic antipodal involution. For even \(n=2m\), fix a root \(x\) and put
\[
\Delta_x(m,2m)=\operatorname{conv}\{x+\mathbf1_S:|S|=m\},
\]
where vertex arithmetic is interpreted in Boolean subset differences from \(x\). Combinatorially this is the middle hypersimplex \(\Delta(m,2m)\); its vertex involution sends \(S\mapsto S^c\).

Let
\[
A_x^a=\{S\in\binom{[n]}m:\text{there is a color-}a
\text{ geodesic prefix of length }m\text{ from }x
\text{ with direction set }S\},
\]
and write \(U_x=A_x^0\cup A_x^1\), forgetting the color on the endpoint.

**Theorem (color-blind equatorial criterion).** For every legal odd coloring of \(Q_{2m}\),
\[
\boxed{\text{a monochromatic full antipodal geodesic exists }
\iff
\exists x,\ S:\ S,S^c\in U_x.}
\tag{31}
\]

*Proof.* Let two monochromatic half-prefixes from \(x\) end at \(u=x^S\) and \(v=x^{S^c}=\bar u\). Their direction sets are complementary. If their colors agree, reverse the first and concatenate it with the second, obtaining a monochromatic full direction-simple path from \(u\) to \(v=\bar u\). If their colors differ, concatenate the first path \(x\to u\) with the antipodal translate of the second path traversed backward: this second part starts at \(\bar v=u\), ends at \(\bar x\), uses the complementary directions, and has the color of the first path. Conversely, split a monochromatic full path at its middle vertex \(x\) and reverse its two halves; both are monochromatic length-\(m\) prefixes from \(x\) to the original antipodal endpoints, whose support sets complement one another. \(\square\)

**Theorem (balanced half-prefix existence).** Suppose the original coloring is vertex-balanced: each vertex of \(Q_{2m}\) has precisely \(m\) incident edges of each color. For every original root \(x\), and each \(a=0,1\), there exists a color-\(a\) direction-simple geodesic prefix of length \(m\). More strongly, every color-\(a\) prefix of length \(k<m\) extends to one of length \(m\).

*Proof.* At the endpoint of a prefix of length \(k\), at most \(k\) incident edges have directions already used. Since \(m\) incident edges have color \(a\), at least \(m-k\ge1\) color-\(a\) incident edges lie in unused directions. Choose one and continue inductively until \(m\) directions have been used. \(\square\)

Thus, in a hypothetical balanced even-dimensional NORI1 counterexample, every root has nonempty red and blue middle-layer reachability sets, but
\[
\boxed{U_x\cap\{S^c:S\in U_x\}=\varnothing
\quad\text{for every }x.}
\tag{32}
\]
In particular \(|U_x|\le\tfrac12\binom{2m}m\), and these antipodal-free supports must be compatible across all original roots under the color-selective cone-transport relations of Article XIV. This does not follow from mere greedoid accessibility of individual rooted families; the antipodal square-edge identities are the missing forcing input.

**Palindromic halfway refinement.** If the two complementary-support half-prefixes from a root have position-indexed color words \(a_1\ldots a_m\) and \((1-a_1)\ldots(1-a_m)\), the antipodally reversed completion above gives a pair of full antipodal geodesics with complementary **palindromic** full words
\[
a_1\ldots a_m a_m\ldots a_1,
\qquad
(1-a_1)\ldots(1-a_m)(1-a_m)\ldots(1-a_1).
\]
Conversely every palindromic full color word in an even-dimensional cube splits into such complementary half-prefixes. This is weaker than a monochromatic full path, but identifies a more structured possible intermediate selection theorem.

The equatorial criterion isolates the desired nonlinear topological mechanism: show that the family of color-blind, rooted middle hypersimplex supports \(U_x\) cannot remain antipodal-free at **every** original cube root while respecting the real original-edge cone transport and balanced half-prefix extendibility. This is the same unrestricted NORI1 conclusion in a new carrier geometry, not a proof of it.


## Balanced middle-layer reachability can be exponentially sparse

For n=4k, k>=2, define two antipodally odd balanced four-direction blocks over F_2:
\[
A=(1+x_4,1+x_3,x_4,x_3),\qquad
B=(x_2,1+x_3,1+x_2,x_3).
\]
Each entry gives the color of the original edge in its indexed direction. It ignores that direction's bit. Both blocks have two edges of each color at every vertex and complement their edge colors under antipodality.

At root zero, the full lists of attainable monochromatic two-direction supports are:
\[
\begin{array}{c|cc}
&0&1\\\hline
A&23,14&12\\
B&14&12,34
\end{array}
\]
Direct substitution shows every monochromatic rooted prefix in either block has length at most two. Take the product of r blocks A and s blocks B, with r,s>=1 and r+s=k. The resulting coloring of Q_{4k} is balanced and antipodally odd.

**Theorem.** Its color-blind middle-layer reachability family U_0 from root zero has cardinality \(2^r+2^s\), contains no complementary pair, is independent in the Johnson graph \(J(4k,2k)\), and is contained in a strict open linear halfspace whose boundary passes through the hypersimplex center.

*Proof.* A global monochromatic prefix of length 2k restricts to a monochromatic rooted path of at most two directions in each of the k blocks, so it uses two directions in every block. Conversely all same-color choices of the listed length-two prefixes combine in the product. The color-zero family has size \(2^r\), and the color-one family has size \(2^s\); they are disjoint. Complements of the A color-one support 12 and B color-zero support 14 are respectively the unavailable supports 34 and 23. Thus no complement remains within either global color family. Nor can the complement of any zero-color support become a one-color support, since in an A block the complements of 23 and 14 are not 12.

Two distinct supports of the same color differ in a block by exchanging disjoint two-element supports, so their symmetric difference has size at least four. Opposite-color supports have local symmetric difference two in every block, giving global difference 2k>=4. They are therefore nonadjacent in J(4k,2k).

On each A block put \(h_A(T)=1_T(1)+1_T(2)-1_T(3)-1_T(4)\); on each B block put \(h_B(T)=1_T(1)+1_T(4)-1_T(2)-1_T(3)\). Summing the block functionals yields a linear form H with value 2s on every attainable zero-color middle support, value 2r on every attainable one-color support, and value zero at the center \((1/2,\ldots,1/2)\). Hence all attainable middle supports lie strictly on one side. \(\square\)

When r and s are close to k/2, U_0 has size O(2^{k/2}) versus a middle layer with \(\binom{4k}{2k}\) vertices. For k=2,r=s=1, U_0 consists of 1256,2358,1458,1278 (directions numbered one through eight). This is a dimension-uniform counterexample to rooted middle-layer density, Johnson connectivity and convex-center forcing, **not** a counterexample to NORI1. Any positive mechanism must couple different roots through the original edge structure.


## A linear-radius forbidden midpoint ball

In the preceding balanced product coloring of Q_{4k}, with r A blocks and s B blocks, r,s>=1, call a root a *good midpoint* if it admits two monochromatic length-2k prefixes whose direction sets are complementary. The equatorial criterion identifies good midpoints with centers of some monochromatic full antipodal geodesic.

**Theorem (root-transport radius barrier).** Every good midpoint x satisfies
\[
\boxed{d_H(x,0^{4k})\ge \min(r,s).}
\]
Consequently for r and s nearly k/2, the Hamming ball of radius \(\min(r,s)-1=\Omega(n)\) around the zero root contains no midpoint of any monochromatic full antipodal geodesic, even though the product coloring is balanced and legal.

*Proof.* Any root x with a four-bit A block and a four-bit B block both still equal to zero cannot be good. Suppose there are two monochromatic prefixes from x with complementary global direction supports and respective colors a,b. Restrict each prefix to one of those untouched blocks. From block root 0000 no monochromatic prefix uses more than two directions; since the pair of global supports is complementary, their restrictions together use all four block directions. Therefore both restrictions have length two and are among the supports displayed in the preceding block table.

In block A, the only complementary pair among the listed color-specific supports is \(23,14\), both color zero. Hence a=b=0. In block B, the only complementary pair is \(12,34\), both color one. Hence a=b=1. Contradiction.

Thus any good midpoint must have no untouched A block, or no untouched B block. Changing every block of either type requires at least r or at least s bit flips from zero, yielding the lower bound. This reasoning uses the global shared-edge product coloring and allows arbitrary direction interleavings; it does not assume the paths use the same color or each intermediate block has balanced local endpoint distribution. \(\square\)

For r=s=k/2 with even k, the exclusion radius is k/2-1=n/8-1. Therefore a hypothetical topological argument that seeks a full geodesic through bounded-radius root transport cannot hold for arbitrary initial roots, even in vertex-balanced legal colorings known to have successful full geodesics elsewhere. Global topological degree or long-range root transitions remain possible.


## Balanced same-color root transport on the equatorial geodesic window graph

Let \(n=2m\ge4\), and let \(c\) be any legally antipodally odd, vertex-balanced original cube-edge coloring. Every cube vertex is incident with m edges of each color.

For \(a\in\mathbb F_2\), define a directed graph \(\mathcal T_m^a\). Its vertices are oriented monochromatic color-a cube geodesics of length m:
\[
P=(v_0,\ldots,v_m),\qquad d_t=v_{t-1}\oplus v_t\in\{e_1,\ldots,e_n\},
\]
with the m direction labels pairwise distinct. Draw an arc \(P\to P'\) if
\[
P'=(v_1,\ldots,v_m,v_m\oplus e_j)
\]
has all m direction labels distinct and the appended edge has color a. The appended direction \(j\) may equal the discarded direction \(d_1\).

**Theorem (nonempty in/out transport and antipodal path criterion).** For every a, every state of \(\mathcal T_m^a\) has at least one incoming arc and at least one outgoing arc. Consequently this finite graph contains a directed cycle, and every state admits an infinite forward monochromatic walk in which every m consecutive edges use distinct directions. Moreover,
\[
\boxed{
\text{NORI1 for }c\quad\Longleftrightarrow\quad
\exists\,a,\ \text{a directed walk of m arcs in }\mathcal T_m^a
\text{ with disjoint supports at its first and last states}.}
\tag{37}
\]

*Proof.* At the terminal vertex \(v_m\), there are m outgoing undirected incident edges of color a. Only m-1 direction labels occur in the retained suffix \(d_2,\ldots,d_m\). Hence at least one color-a edge has a direction outside that suffix, and appending it produces an outgoing arc. At the initial vertex \(v_0\), the same degree argument applied to the retained prefix \(d_1,\ldots,d_{m-1}\) permits a color-a edge in an unused direction to be prepended, proving positive indegree. Finite directed graphs of positive outdegree contain directed cycles, and the extension can be iterated indefinitely.

After m window shifts, the initial and terminal state direction supports are those of two consecutive length-m blocks in a common monochromatic length-2m walk. Each block uses m distinct directions. The supports are disjoint if and only if their union uses every one of the 2m cube directions, making this length-2m walk a monochromatic full antipodal geodesic. Conversely every monochromatic full geodesic gives m consecutive legal window shifts with disjoint initial and final supports. \(\square\)

**Johnson support transport.** If a state starts at x, has initial direction i and support \(S\in\binom{[n]}m\), the transported state starts at \(x\oplus e_i\) and has support
\[
S'=(S\setminus\{i\})\cup\{j\},\qquad
j\notin S\setminus\{i\}.
\tag{38}
\]
Thus each legal shift either preserves S (when j=i) or traverses one edge of the Johnson graph \(J(2m,m)\). This is a necessary **cross-root incidence relation** between middle-layer reachability families, absent from arbitrary antipodal-free subsets of a hypersimplex.

Under a hypothetical NORI1 counterexample, both color-specific transport graphs retain recurrent monochromatic window walks, but on **every** directed walk of m transport arcs the first and last direction supports must intersect. This is a dimension-uniform dynamical obstruction statement on a locally nonempty transport digraph. It supplies a candidate space for equivariant chain or spectral arguments and cleanly identifies the permissible repeated-direction degeneracy that prevents a sliding-window walk from automatically being a full geodesic.

The time-reversal operation on an oriented monochromatic m-geodesic reverses every transport arc, while cube antipodality exchanges the two color-specific transport graphs. Hence the coupled two-color shift system has both reversible path symmetry and an antipodally odd color interchange, retaining the original shared-edge constraints.


**Topological limitation of color-preserving transport.** Let \(\mathcal T_m=\mathcal T_m^0\sqcup\mathcal T_m^1\), and let antipodality translate every path, exchanging the two colors. The locally finite realization of this directed transport graph has an equivariant continuous map to the antipodal zero-sphere:
\[
\mathcal T_m\longrightarrow S^0,\qquad P\longmapsto(-1)^{\operatorname{color}(P)}.
\]
Therefore its ordinary \(\mathbb Z_2\)-cohomological index is zero, despite both color-specific graphs having directed recurrence. No Borsuk-Ulam contradiction can be extracted from this disconnected, color-preserving transport space alone. A topological forcing argument must include the original shared-edge bichromatic exchange incidence, or treat the two color-specific windows as a relative pair inside the full type-B Freudenthal sphere. This separates the positive balanced transport theorem from the still missing global index mechanism.


## Cyclic-pair obstruction to center separation

For \(n=2m\), \(m\ge3\), let \(a_r,b_r\) be direction pairs indexed by \(r\in\mathbb Z/m\), and color original edges by \(c_{a_r}(x)=x_{a_{r+1}}\), \(c_{b_r}(x)=1+x_{a_{r+1}}\). This is antipodally odd and balanced at every vertex.

**Theorem.** At root zero the color-zero middle-distance supports are precisely the \(S=A_a\cup B_b\) with
\[
A\subsetneq[m],\quad B\subseteq\{r:r+1\in A\},\quad |A|+|B|=m.
\]
The only color-one support is all \(b_r\). The union \(U_0\) has \(T_m=[z^m](1+z+z^2)^m\) members, and contains an antipodal pair if and only if \(m\) is even.

*Proof.* Initially the \(a_r\) are zero-color, and traversing \(a_{r+1}\) exchanges the colors of \(a_r,b_r\). A zero-color use of \(b_r\) requires earlier use of \(a_{r+1}\). Among selected first directions, \(a_r\) must precede \(a_{r+1}\), so not all first directions can be selected. Conversely these precedence constraints can be ordered whenever \(A\) is proper, after which the requested \(b_r\) can all be traversed. One-color paths can only use the \(b_r\). In the paired bits \((\mathbf1_{a_{r+1}},\mathbf1_{b_r})\), red states are \(00,10,11\). All middle-weight ternary strings are attainable except the all-\(10\) string, hence \(T_m-1\) zero-color supports plus one blue support. If two zero-color supports are complementary then \(B=\operatorname{pred}(A)\), yielding \(m=2|A|\). Conversely this condition gives complementary supports whenever \(m\) is even. The unique blue support cannot be complemented. \(\square\)

**Theorem (interior centering for odd \(m\)).** If \(m\ge3\) is odd, \(U_0\) is antipodal-free yet its convex hull contains the hypersimplex center \(\mathbf1/2\) in the interior relative to \(\sum z_i=m\).

*Proof.* Uniformly sample a zero-color support. Cyclic symmetry makes the mean first-direction marginal \(p=\mathbb E|A|/m>1/2\) and mean second-direction marginal \(1-p\). Mix this law with the all-second support using weights \(1/(2p)\) and \(1-1/(2p)\). This assigns positive weight to every point of \(U_0\) and gives marginal \(1/2\) in every direction.

To check full affine dimension for odd \(m\ge5\), write paired indicator bits \(z_r=\mathbf1_{a_r}\), \(w_r=\mathbf1_{b_{r-1}}\), and suppose \(L=\sum(\alpha_r z_r+\beta_r w_r)\) is constant on all red middle supports. For distinct \(i,j\), compare state pairs \((11,00)\) and \((10,10)\), filling remaining states with one \(00\), one \(11\), and \(m-4\) copies of \(10\). Both full strings are admissible, and equality of \(L\) gives \(\beta_i=\alpha_j\). Hence all coefficients agree, leaving only the middle-weight affine relation. For \(m=3\), the six red supports have affine dimension four, and the blue support lies outside their first-direction-count hyperplane; together they span the five-dimensional middle layer. A convex combination with strictly positive weight on every point of a full-dimensional finite set lies in its convex hull's interior. \(\square\)

The size fraction satisfies
\[
T_m/\binom{2m}m\sim(\sqrt3/2)(3/4)^m.
\]
An explicit monochromatic full geodesic exists elsewhere: from the root with bit \(a_0=1\) and every other bit zero, traverse \(b_{m-1},a_0,a_1,b_0,a_2,b_1,\ldots,a_{m-1},b_{m-2}\); every edge is color zero.

**A sharp fractional-selection threshold.** If zero lies in the convex hull of at most three sign vectors, two of them are complementary. For positive weights on three vectors, the plus-sign weights in every entry must total one-half, so one vector has weight one-half and the two others agree entrywise with its opposite. Four are necessary and sufficient to evade that implication: in the six-dimensional instance the four noncomplementary middle supports \(123,345,246,156\) average to the center with equal weights.

This infinite family disproves independent affine center-separation of color-blind, antipodal-free half-geodesic reachable sets even under the full balanced, antipodally odd cube-edge conditions.


## Sharp cubic separation degree for the centered equatorial family

Continue with the cyclic-pair balanced coloring (EF1) in even dimension \(n=2m\), where \(m=2h+1\ge3\) is odd. At root zero, write \(U_0\) for the color-blind monochromatic length-\(m\) endpoint supports, and let \(p_r(S)=\mathbf1_{\{a_r\in S\}}\). Define the centered first-direction count
\[
t(S)=\sum_{r=0}^{m-1}p_r(S)-\frac m2.
\]
Under middle-layer complementation \(S\mapsto S^c\), \(t(S^c)=-t(S)\).

**Theorem (minimum-degree odd polynomial separation).** The polynomial
\[
\boxed{Q(S)=t(S)\bigl(h^2-t(S)^2\bigr)}
\tag{EF5}
\]
has degree three in the Boolean endpoint bits, is odd under antipodality, and obeys
\[
Q(S)>0\quad(S\in U_0),\qquad Q(S)<0\quad(S\in \overline{U_0}).
\]
There is no real polynomial of degree at most two with this strict sign separation, whether or not oddness is assumed. Hence the least separating polynomial degree is precisely three.

*Proof.* Every zero-color middle support has \(|A|\in\{h+1,\ldots,2h\}\), so \(t(S)\in\{\frac12,\frac32,\ldots,h-\frac12\}\); thus \(0<t(S)<h\) and \(Q(S)>0\). The unique one-color support has \(|A|=0\), hence \(t(S)=-(h+\frac12)\), and both factors in \(Q(S)\) are negative, again giving \(Q(S)>0\). Oddness gives strict negativity on the antipodal image.

For the lower bound, suppose \(P\) of degree at most two strictly separates \(U_0\) from \(\overline{U_0}\). Antisymmetrize to \(H(S)=(P(S)-P(S^c))/2\). It retains the strict signs and has degree at most two. Expressed in centered variables \(y_i=2\mathbf1_{\{i\in S\}}-1\), antipodality sends every \(y_i\) to \(-y_i\). Every odd polynomial of total degree at most two is linear in these variables. Hence \(H(S)=\ell(\mathbf1_S-\frac12\mathbf1)\) for some linear functional \(\ell\). But the previous theorem placed \(\frac12\mathbf1\) inside the convex hull of \(U_0\), precluding a linear functional strictly positive on every member. Contradiction. \(\square\)

This is an all-dimensional sharp obstruction to linear equatorial separators but not to nonlinear ones. It identifies degree three as the first effective algebraic level for this family, and suggests retaining nonlinear path-sensitive or higher-order endpoint data in proposed equivariant carriers rather than only first moments of middle-layer reachability.


## Four-point tetrahedral balance theorem

Let \(n=2m\). Suppose \(S_1,S_2,S_3,S_4\subset[n]\) have size \(m\), no complementary pair, and admit positive weights \(\lambda_j\) summing to one with
\[
\sum_j\lambda_j\mathbf1_{S_j}=\frac12\mathbf1.
\]
Then \(\lambda_j=1/4\) for all \(j\); every direction appears in two supports; and the counts of directions whose membership pair is \(12,34,13,24,14,23\), respectively, equal
\[
\boxed{(a,a,b,b,c,c),\quad a,b,c\ge1,\quad a+b+c=m.}
\]

*Proof.* Every direction's positive sign rows have weights summing to \(1/2\). A singleton of weight \(1/2\) would force a complementary row pair. Thus positive rows are paired. If only one or two pair partitions occur across the directions, two rows are complementary. All three partitions must occur, so every pair of weights has sum \(1/2\), forcing \(\lambda_j=1/4\). Each direction therefore lies in two supports. Because each support has \(m\) directions, its signed row sum is zero. The three independent sign patterns \((1,1,-1,-1),(1,-1,1,-1),(1,-1,-1,1)\) show that paired opposite multiplicities agree. Positivity of all three partition types gives \(a,b,c\ge1\). \(\square\)

At \(n=6\), the sole possible incidence pattern (up to relabeling) has all six unordered pairs once, identifying the incidence of the complete graph on four vertices. The prior legal six-dimensional balanced cyclic coloring realizes this minimal centered, antipodal-free fractional certificate; further forcing must use monochromatic path witnesses, not just their middle supports.


## A sharp spectral obstruction to flatness in vertex-balanced antipodally odd colorings

Let \(n=2m\). For an undirected-edge binary coloring \(c\), write
\[
D_c(x)=\sum_{i=1}^n(-1)^{c_i(x)}=n-2\deg_1(x).
\]
The coloring is vertex-balanced iff \(D_c\equiv0\), and is flat iff its square coboundary vanishes on every original cube square.

**Theorem 1 (universal nonflatness under balance).** A legal antipodally odd coloring of \(Q_{2m}\) which is vertex-balanced cannot be flat.

**Theorem 2 (sharp mean-square obstruction for every flat legal coloring).** More strongly, every *flat* antipodally odd coloring \(c\) of \(Q_{2m}\) satisfies
\[
\boxed{\frac1{2^n}\sum_{x\in Q_n}D_c(x)^2\ge 2.}
\tag{SP1}
\]
The bound is attained in every even dimension, including \(n=2\). Equivalently,
\[
\frac1{2^n}\sum_x(\deg_1(x)-m)^2\ge\frac12.
\]

*Proof.* Flatness on all squares makes \(c=d\phi\) for a Boolean vertex potential \(\phi\). Put \(g(x)=(-1)^{\phi(x)}\), \(A g(x)=\sum_{i=1}^ng(x^i)\), and \(\chi(x)=(-1)^{|x|}\). Then
\[
D_c(x)=g(x)(Ag)(x),\qquad \|D_c\|_{L^2}^2=\|Ag\|_{L^2}^2.
\tag{SP2}
\]
Antipodal oddness gives \(g(\bar x)g(\overline{x^i})=-g(x)g(x^i)\); hence the sign \(g(\bar x)/g(x)\) changes across every cube edge. Connectedness gives
\[
\boxed{g(\bar x)=\varepsilon\chi(x)g(x)}
\tag{SP3}
\]
for one fixed \(\varepsilon\in\{\pm1\}\).

Let \(g_e=g\,\mathbf1_{|x|\text{ even}}\) and \(g_o=g\,\mathbf1_{|x|\text{ odd}}\). Each has normalized squared \(L^2\)-norm \(1/2\). Because \(n\) is even, antipodality preserves the two parity classes. Equation (SP3) shows that \(g_e,g_o\) have opposite eigenvalues \(\varepsilon,-\varepsilon\) under the antipodal operator. On a Walsh character \(\chi_S\), antipodality has eigenvalue \((-1)^{|S|}\), while adjacency has eigenvalue \(n-2|S|\). Consequently one of \(g_e,g_o\) has Fourier support on levels \(|S|\) whose parity differs from \(m\). For every such level, \(|n-2|S||\ge2\), so its adjacency energy has squared norm at least \(4(1/2)=2\). The two parity pieces have orthogonal images under adjacency (they lie on opposite vertex parity classes), yielding \(\|Ag\|_{L^2}^2\ge2\). This proves (SP1). In particular \(D_c\) cannot vanish identically, proving Theorem 1. \(\square\)

**Sharpness in every even dimension.** Fix any \(S,T\subseteq[n]\) with \(|S|=m\), \(|T|=m+1\), and set
\[
g(x)=\begin{cases}
(-1)^{\sum_{i\in S}x_i},&|x|\text{ even},\\
(-1)^{\sum_{i\in T}x_i},&|x|\text{ odd}.
\end{cases}
\tag{SP4}
\]
This is a Boolean sign function, so define \(\phi\) from \(g=(-1)^\phi\) and put \(c_i=d_i\phi\). It is flat by construction and antipodally odd because the two vertex parity classes have opposite translation signs:
\(g(\bar x)=(-1)^m\chi(x)g(x)\).
A direct adjacency calculation gives
\[
(Ag)(x)=\begin{cases}-2\chi_T(x),&|x|\text{ even},\\0,&|x|\text{ odd}.\end{cases}
\]
Therefore \(D_c=0\) on half the cube vertices and \(D_c=\pm2\) on the other half, establishing equality in (SP1).

**Magnetic-adjacency reformulation.** For any legal coloring let \(M_c\) be the signed adjacency operator \((M_ch)(x)=\sum_i(-1)^{c_i(x)}h(x^i)\). Antipodal oddness imposes \(\tau M_c\tau^{-1}=-M_c\), and balance imposes \(M_c\mathbf1=0\). Flatness would make \(M_c\) gauge-conjugate to the ordinary cube adjacency \(A\). Theorems 1-2 show that these requirements are incompatible, with a sharp spectral energy gap. Thus in the even-dimensional balanced reduction, ordinary projective curvature may be cohomologically zero but cannot vanish pointwise. The theorem does not yield the monochromatic full geodesic; it identifies a necessary nontrivial curvature input for any topological decoding of balanced-star zeros.


## Canonical Fourier-exchange potential of the balanced vertex-star field

Let \(n=2m\ge4\), and let \(c\) be any antipodally odd, vertex-balanced coloring of the original undirected cube edges. Write \(s_i(x)=(-1)^{c_i(x)}\), and expand
\[
s_i(x)=\sum_{S\subseteq[n]}a_{i,S}\chi_S(x),\qquad
a_{i,S}=2^{-n}\sum_{x\in Q_n}s_i(x)\chi_S(x).
\]
Undirectedness, antipodal oddness, and vertex balance imply, respectively,
\[
\boxed{a_{i,S}=0\ (i\in S),\qquad
a_{i,S}=0\ (|S|\text{ even}),\qquad
\sum_{i\notin S}a_{i,S}=0.}
\tag{FP1}
\]
For \(|S|=n-1\), only one direction lies outside \(S\), and the last equation annihilates the coefficient. Therefore every signed-star component has Fourier degree at most \(n-3\). At every nonzero Fourier frequency at least three direction labels remain outside its support.

Let \(F\) be the multilinear extension of the signed star to the real cube, obtained by replacing \(\chi_S(x)\) by \(\chi_S(t)=\prod_{j\in S}(1-2t_j)\).

**Theorem (canonical exchange potential).** For \(i\ne j\), define
\[
\boxed{H_{ij}(t)=
\sum_{\substack{|S|\text{ odd}\\i,j\notin S}}
\frac{a_{i,S}-a_{j,S}}{n-|S|}\chi_S(t).}
\tag{FP2}
\]
Then \(H_{ji}=-H_{ij}\), \(\partial_iH_{ij}=\partial_jH_{ij}=0\), \(H_{ij}(\mathbf1-t)=-H_{ij}(t)\), and
\[
\boxed{F_i(t)=\sum_{j\ne i}H_{ij}(t).}
\tag{FP3}
\]
For each individual Walsh frequency \(S\), the coefficients \((a_{i,S}-a_{j,S})/(n-|S|)\) are the unique minimum-squared-energy antisymmetric flows on the complete graph of directions \([n]\setminus S\) with divergence vector \((a_{i,S})_{i\notin S}\). Hence this construction is canonical and commutes with renaming cube directions.

*Proof.* Put \(T=[n]\setminus S\), \(k=|T|\), and \(v_i=a_{i,S}\). The vector \(v\) has sum zero by (FP1). For each \(i\in T\),
\[
\sum_{j\in T\setminus\{i\}}\frac{v_i-v_j}{k}
=\frac{(k-1)v_i+\ v_i}{k}=v_i.
\]
Summing over frequencies gives (FP3). The antisymmetry, derivative constraints, and oddness follow term by term. Orthogonal projection of the affine space of antisymmetric flows with divergence \(v\) onto the gradient-flow subspace of the complete graph gives this unique minimal-energy solution. \(\square\)

Equivalently, define a real differential 2-form
\[
\Omega(t)=\sum_{i<j}H_{ij}(t)\,dt_i\wedge dt_j,\qquad N=\sum_i\partial_{t_i}.
\]
Then
\[
\boxed{\iota_N\Omega=-\sum_iF_i(t)\,dt_i.}
\tag{FP4}
\]
The signed vertex-star field is thus the contraction of a globally defined, antipodally odd, pair-exchange 2-form, whose \(ij\) entry is independent of the two participating direction variables.

**Pfaffian carrier of Borsuk-Ulam zeros.** Let \(H(t)\) be the skew \(n\times n\) matrix with entries (FP2). Equation (FP3) says \(F(t)=H(t)\mathbf1\). Therefore
\[
\boxed{F(t)=0\Longrightarrow H(t)\mathbf1=0
\Longrightarrow \operatorname{Pf}H(t)=0,\quad\dim\ker H(t)\ge2.}
\tag{FP5}
\]
The second implication uses the even order of the skew matrix, whose nullity is even. The Pfaffian is not universally zero: in \(Q_6\), for the balanced legal coloring
\(c_1=x_3,c_2=1+x_3,c_3=x_5,c_4=1+x_5,c_5=x_1,c_6=1+x_1\)
(using one-indexed directions), direct substitution gives \(\operatorname{Pf}H(0)=-1/25\).
Under geometric antipodality \(H(\mathbf1-t)=-H(t)\), so the Pfaffian transforms by \((-1)^m\). When \(m\) is odd, its boundary restriction is a section of the nontrivial real line bundle over \(\mathbb RP^{n-1}\), with first Stiefel-Whitney class \(u\), giving a canonical projective Pfaffian-degeneracy carrier. This carrier contains all boundary zeros of \(F\), but membership alone does not imply a monochromatic full geodesic.

**Rank-three threshold for the square tetrahedral obstruction.** On an original square with free directions \(p,q\), the mixed second derivative of \(F\) is
\[
\boxed{\partial_p\partial_qF_k
=4\sum_{\substack{S\supseteq\{p,q\}\\|S|\text{ odd}}}
a_{k,S}\chi_{S\setminus\{p,q\}}.}
\tag{FP6}
\]
Every contributing frequency has odd degree at least three. Hence a nonzero quadratic term \(Czw\) in the previously derived balanced-star zero-square normal form requires Walsh interactions of degree at least three. In dimension four, (FP1) forces the full field to have only degree-one Fourier modes, so no zero square can carry a nonzero tetrahedral \(C\)-term. In dimension six the first degree-three modes are permitted, and the previously published legal balanced six-dimensional zero-square example realizes a nonzero \(C\)-term. This gives an intrinsic Fourier explanation of the rank-three local decoding obstruction.

**Precise limitation.** The entries \(H_{ij}\) are real fractional exchange weights, not original edge colors; their skew decomposition does not preserve ordered monochromatic path certificates by itself. A proof of unrestricted NORI1 requires an integrality/transport theorem converting the global Pfaffian and zero-set geometry back into direction-simple colored geodesics. The theorem supplies a dimension-uniform structural target, not that missing theorem.


## Unfiltered twisted filling monodromy is trivializable

Let C_k^- denote integral antipodally anti-invariant cube-boundary chains and Z_1^- their degree-one cycles. As H_1(RP^{n-1};Z_sign)=0, the boundary C_2^- -> Z_1^- is onto. As Z_1^- is free abelian, it has an integral linear section L. For any balanced legal colorings c,d, signed edge cycles z_c,z_d differ by twice a cycle. Thus odd-coefficient anti-invariant square fillings transport by Sigma -> Sigma+2L((z_d-z_c)/2), with composition strictly path-independent. This preserves the two filling classes, so their unfiltered torsor does not compel nontrivial monodromy. A geometric or color-certified filtration is indispensable.


## Odd seam-star incidence and two-red median connectors

Let P be a full original-cube antipodal geodesic of twisted defect d=2r+1>=3, doubled antipodally to a 2n-cycle. Let z_0,...,z_(d-1) be its red-to-blue seam vertices cyclically, and A_j the forward z_j-to-z_(j+1) arc of length L_j.

**Theorem (odd seam-star incidence).** Every L_j<n. Each original direction occurs once in each of two distinct arcs A_a,A_b, where b-a equals r or r+1 modulo d. Hence the n original directions label, with multiplicity, the edges {j,j+r} of the odd star polygon on Z_d, which is one d-cycle. Writing N_j for the multiplicity of {j,j+r},
\[
L_j=N_j+N_{j-r},\qquad \sum_jN_j=n,\qquad
2N_j=\sum_{k=0}^{d-1}(-1)^k L_{j-kr}.
\]
*Proof.* An arc between successive red-to-blue seams contains one blue-to-red seam. An n-edge interval of the antiperiodic word has d>=3 changes, so no such arc reaches length n. Direction i occurs twice at antipodal, n-separated steps, hence in distinct arcs. The first-Walsh seam identity (S1), in note_nori_xvii_projective_turn_flat_cut_reconstruction_r12094_2, says that the i-th seam bits have r+1 occurrences of their majority value and r of their minority value. They switch only across the two direction-i occurrence arcs, and hence form contiguous cyclic blocks of these lengths. Thus the arcs are separated by r or r+1 seam-index steps. Counting incident directions proves the L_j identities, and alternating substitution around the odd orbit of addition by r gives the inversion formula. QED.

Let m=med(z_0,...,z_(d-1)) be their unique majority vertex, and for a modulo d put
\[
T_a=(z_a,z_{a+1},z_{a+r+1}),\qquad m_a=med(T_a).
\]

**Theorem (canonical spanning median triangles).** Every T_a spans all n directions, so its three median-arm supports partition [n]. Moreover,
\[
\boxed{\sum_{a=0}^{d-1}d_H(m_a,m)=(r-1)n.}
\]
For each direction i, the indices a where (m_a)_i differs from m_i form a consecutive cyclic block of size r-1. At d=5, the five sets D(m,m_a) partition [n].

*Proof.* The cyclic index gaps in T_a are 1,r,r. They prevent all three indices from lying in either of the two constant-bit seam intervals of lengths r and r+1, so the triple spans Q_n. Its median differs from m at direction i iff two of its indices lie in that direction's minority block of length r. Only the adjacent pair {a,a+1} can fit; each r-block contains precisely r-1 consecutive such pairs. Sum over i. QED.

**Two original monochromatic connectors.** If p,q are red-to-blue seams separated by s<=r seam-index steps, the short backward path p to bar(q) uses each of its original directions once, begins and ends red, and has d-2s monochromatic runs. Thus for T_a the backward original-cube paths
\[
z_{a+1}\longrightarrow\bar z_{a+r+1},\qquad
z_{a+r+1}\longrightarrow\bar z_a
\]
are both entirely red (s=r). Their direction supports equal respectively D(m_a,z_a) and D(m_a,z_(a+1)): for any spanning triple (p,q,z), D(p,bar(q))=D(med(p,q,z),z) bit by bit. These red paths occupy possibly translated parallel faces and therefore cannot automatically serve as red median arms in an arbitrary nonlinear edge coloring.

**Remaining forcing obligation.** On a globally minimum-defect P, applying the previously proved median three-route identity to any T_a gives a strict improvement when its genuine median arms have total internal switches S and first-edge disagreement Delta in {0,2} satisfying S+Delta/2<d. The new canonical triangles always have two red parallel corridors; no dimension-uniform color-preserving transfer to sufficiently cheap median arms has been proved. These results are a structural incidence theorem and a conditional descent framework, not NORI1 closure.


### Run-block coordinates for the seam-star family

The star incidence has a canonical realization by the red-run supports themselves. Let E_j subset [n] be the direction support of the maximal red run ending at red-to-blue seam z_j on the doubled path. Antipodal complementation makes every original direction red once and blue once over this 2n-edge circuit; therefore [n] is the disjoint union of E_0,...,E_(d-1). Regarding E_j as its indicator vector in F_2^n and retaining the canonical majority m, one has the **block-window identities**
\[
\boxed{z_j=m\oplus\bigoplus_{k=1}^{r}\mathbf1_{E_{j+k}},\qquad
m_a=m\oplus\bigoplus_{k=2}^{r}\mathbf1_{E_{a+k}}.}
\]
Here r=(d-1)/2, indices are cyclic, and the second sum is empty when r=1. In particular,
\[
\boxed{D(m_a,z_a)=E_{a+1},\qquad D(m_a,z_{a+1})=E_{a+r+1}.}
\]
These are the supports of the two red short-backward connectors already identified above. At defect d=5 this specializes to z_j=m xor E_(j+1) xor E_(j+2), m_j=m xor E_(j+2), so the five median displacements partition [n].

*Proof.* Along the oriented doubled path, red edges move toward m and blue edges move away, by the established seam-majority gradient interpretation. Each direction i belongs to one red-run support E_b. Immediately after its red run ends at z_b, its bit agrees with m_i; it becomes opposite to m_i only when the antipodal blue occurrence of direction i is traversed, and remains opposite for r consecutive red-to-blue seam vertices. Consequently its minority seam interval is z_(b-r),...,z_(b-1). Equivalently, the bit of z_j differs from m_i iff i belongs to one of E_(j+1),...,E_(j+r). This proves the seam identity. The majority of z_a,z_(a+1),z_(a+r+1) differs from the global majority precisely in direction blocks E_(a+2),...,E_(a+r), by the preceding canonical-triangle calculation, proving the median identity. Taking symmetric differences yields the two support equalities. QED.

**Interpretation.** The seam configuration factors through a d-block cube with disjoint (possibly unequal) original-direction supports E_j. Its geometry is fixed by cyclic windows; its color-dependent internal geodesic orders and parallel-face square derivatives remain unrestricted. A proof using the compressed geometry must lift every block move to a path on its own original direction support and control colors under transverse transport. No blockwise color-invariance assumption is justified.


### Projective selector distance as a minimum run-window mass

For a full antipodal geodesic P with twisted defect d=2r+1 and projective rainbow cycle C, use its red-to-blue seam vertices z_j and red-run direction supports E_j as above. Write e_j=|E_j| and let Q(C) be the projective canonical majority/seam selector. Then
\[
\boxed{d_G(Q(C),V(C))=\min_{j\in\mathbb Z_d}\sum_{k=1}^r e_{j+k},}
\]
where the empty sum is zero at d=1, and d_G([u],[v])=min(d_H(u,v),n-d_H(u,v)) on the folded cube. In particular,
\[
r\le d_G(Q(C),V(C))\le rn/(2r+1) \quad(d\ge3).
\]

*Proof.* Along the antiperiodically doubled directed path, every red edge decreases the ordinary Hamming-distance height h(u)=d_H(u,m), where m is the global seam majority, and every blue edge increases it, by the established red/blue gradient interpretation of m. Hence its global height minima occur at red-to-blue seam vertices. The maximum heights are the antipodal images of these minima and project to the same minima of min(h,n-h). Thus the projective minimum distance to [m]=Q(C) is attained at one of the z_j. The earlier block-window identity yields h(z_j)=sum_(k=1)^r e_(j+k). Each e_j>=1, giving the lower bound; the average of the d consecutive r-block sums is rn/d, giving the upper bound. QED.

Combining with the previously proved selector-minority equivalence gives the cross-cycle identity
\[
\boxed{\delta(c)=\min_C\min_j \sum_{k=1}^{(d(C)-1)/2}|E_{j+k}(C)|,}
\]
where delta(c) is the minimum minority-color count among all full geodesics. Thus the existing tensor-amplification criterion can be phrased as a uniform o(n) bound for some cyclic half-window of red-run block masses on some complete projective rainbow cycle. Such a bound remains UNPROVED.

### Realization of arbitrary odd seam-star block sizes, and the actual forcing frontier

**Theorem (full seam-star realizability).** Let d=2r+1 be any odd integer with 3<=d<=n, and let [n]=E_0 sqcup ... sqcup E_(d-1) be ANY partition into nonempty sets, with an arbitrary internal order prescribed for each E_j. There exists an antipodally odd original-cube edge coloring c and a full antipodal geodesic P whose doubled color cycle has red-run direction supports E_0,...,E_(d-1), in this cyclic order and with the prescribed internal run orders. In particular, every vector of positive red-run block sizes (e_0,...,e_(d-1)) summing to n occurs; odd polygonal overlaps alone impose no other restriction on these masses.

*Construction and proof.* Build a 2n-step cyclic direction word by concatenating, for j=0,...,d-1 in cyclic order, a BLUE block traversing E_(j+r+1) in its prescribed internal order followed by a RED block traversing E_(j+1) in its prescribed internal order. The sequence has 2d nonempty monochromatic runs, with each direction appearing twice. The red E_j run occupies run slot 2j-1 and its blue mate E_j occupies run slot 2(j+r) modulo 2d; the slots differ by d, and the two runs have identical ordered direction words. Therefore shifting by n edge positions sends every run to its mate and preserves the direction list while complementing its colors: the direction sequence is n-periodic, the binary color sequence antiperiodic. Select any n consecutive steps, which contain each original direction once, and realize them as a rooted full cube geodesic P. Give its n original edges their prescribed edge colors and assign complementary colors to their n antipodal mate edges. Those 2n edges are distinct (the doubled direction-simple cycle); thus these assignments are consistent. Color every remaining original antipodal edge orbit arbitrarily with complementary colors. This produces a legal coloring realizing the prescribed full seam-star data. QED.

This theorem is deliberately about the existence of a *specified geodesic* with prescribed seam-star pattern. The resulting coloring may have other monochromatic full geodesics; it is not a counterexample to NORI1. Its proof shows why parity, Hamming majority, odd-star incidence and run-length inequalities attached solely to one geodesic cannot force descent. A viable argument must use cross-geodesic incidence or shared-edge information outside the doubled P cycle.

**Two-corridor corner interpretation.** For a canonical spanning seam triangle T_a, write O=m_a, A=E_(a+1), B=E_(a+r+1), and let C=[n] without (A union B). Its three seam vertices are O xor A, O xor B, O xor C. The red run on A is an original monochromatic path from O xor A xor B to O xor B. The antipodal mate of the red run on B supplies an original BLUE path from O xor A to O xor A xor B. These are adjoining sides of an A-by-B block square, each with a witnessed internal direction order. The unseen sides from O to O xor A and from O to O xor B, and the complementary C-arm, are where transport must obtain its new information. The common red run E_j participates in two such overlapping canonical triangles. Their odd cyclic overlap is real, but the realization theorem shows that it forces no contradiction until square transport uses the additional original-cube edges.


### Coupled transverse-derivative words from two shared red runs

For a canonical spanning triangle T_a, write O=m_a, A=E_(a+1), B=E_(a+r+1), C=[n] minus (A union B). Its seam vertices are O xor A, O xor B and O xor C. Let R_A=R_(a+1) and R_B=R_(a+r+1) be the known red monochromatic maximal runs in the doubled P cycle, retaining their ORIGINAL ordered sequences of directed edges. The preceding block-corner identities give R_A as an oriented path O xor A xor B -> O xor B and R_B as an oriented path O xor B xor C -> O xor C. Thus the reversed B-translate of R_A is a valid median arm Q_A:O->O xor A; the A-translate of the antipodal R_B is a valid median arm Q_B:O->O xor B.

For any original i-edge e and disjoint transverse direction set S with i not in S, define D_S c(e)=c(e xor 1_S)+c(e) in F_2. This derivative is invariant under antipodal translation: D_S c(bar e)=D_S c(e), by antipodal oddness of c. Define U_a to be the ordered binary word of D_B c(e) along red R_A and V_a the ordered binary word of D_A c(e) along red R_B. Since R_A and R_B were entirely red, the actual color words of Q_A and Q_B are exactly reverse(U_a) and 1+V_a respectively. They are shared-edge-consistent REAL paths in the original cube, for every nonlinear coloring.

Write Var(w) for the ordinary number of changes of a binary word. Consequently Q_A has Var(U_a) changes and initial color alpha_A=last(U_a); Q_B has Var(V_a) changes and initial color alpha_B=1+first(V_a). Let Q_C be ANY full direction-simple geodesic from O to O xor C, with ordinary switch count s_C and initial color alpha_C. Define Delta_a=[alpha_A!=alpha_B]+[alpha_B!=alpha_C]+[alpha_C!=alpha_A], which lies in {0,2}. Then the proved median three-route telescoping identity, with no interior-cut penalty because all three triangle vertices are red-to-blue seams, gives:

**Theorem (simultaneous transverse derivative barrier).** If P globally minimizes its odd twisted defect d over all roots and direction permutations, then for EVERY a and EVERY choice of Q_C,
\[
\boxed{\operatorname{Var}(U_a)+\operatorname{Var}(V_a)+s_C+\tfrac12\Delta_a\ge d.}
\]
Conversely, a violation constructs, via the established three-route recombination, an ORIGINAL direction-once full antipodal geodesic with strictly smaller twisted defect.

*Proof.* The given translations and reversals keep each direction support intact and preserve its internal direction simplicity. Antipodal oddness yields the displayed exact color words and phases. Their supports A,B,C partition [n], so the median three-route formula applies. For a globally minimal P it asserts sum of the three arm switch counts plus Delta_a/2 is at least d. Substitute the exact derivative-word expressions. QED.

**Cross-triangle coupling.** Each original red run R_j participates in TWO canonical triangles, the one indexed a=j-1 (as its A-run) and the one indexed a=j-r-1 (as its B-run). Thus the collection of 2d derivative words U_a,V_a is formed from only d physical red paths, each sampled under two different block translations: E_(j+r) and E_(j-r), respectively. The translations commute as finite differences of genuine edge-color functions, but there is presently no dimension-uniform estimate making the simultaneous family of inequalities impossible. Ordinary F_2 Stokes/derivative integrability supplies consistency identities, not the required INTEGER switch-variation bound. This distinction is the missing global forcing obligation and prevents treating an odd overlap cycle alone as a contradiction.


### Canonical seam annulus and Möbius carrier

Put d=2r+1>=3 and partition [n]=E_0 sqcup ... sqcup E_(d-1) into the red-run direction supports of a full geodesic P. The block vertex v_S=m xor 1_(union_(j in S)E_j) embeds a diagonal Q_d in the geometric original cube. Its macroedges are diagonals across E_j-faces, resolvable into original direction-simple paths.

Define
\[
z_a=v_{\{a+1,\ldots,a+r\}},\quad
b_a=v_{\{a+1,\ldots,a+r+1\}}=\bar z_{a+r+1},\quad
m_a=v_{\{a+2,\ldots,a+r\}}.
\]
The four vertices (m_a,z_a,b_a,z_(a+1)) bound a macro-square Sigma_a in directions A=E_(a+1), B=E_(a+r+1). The upper route z_a->b_a->z_(a+1) is the original BLUE B-run followed by RED A-run; the lower alternative z_a->m_a->z_(a+1) uses A then B.

**Theorem (antipodal seam surface).** Set U_d=union_a(Sigma_a union tau Sigma_a), where tau is antipodality. For d=3, U_3=boundary Q_3=S^2 and U_3/tau=RP^2. For odd d>=5, U_d is a connected annulus, with boundary cycles
\[
L=z_0,m_0,z_1,m_1,\ldots,z_{d-1},m_{d-1},z_0,\quad \tau L.
\]
Antipodality interchanges the two components and U_d/tau is a Möbius band. The 2d-edge doubled full geodesic P is the central essential cycle. Each original direction appears twice around L, in the two appearances of its red-run block as short median-arm support.

*Proof.* The three vertex classes m_a,z_a,b_a have block weights r-1,r,r+1, and tau m_a has weight r+2. For d>=5 the d vertices in each class are distinct. The two core edges of Sigma_a have antipodal mates among the core edges of Sigma_(a+r) and Sigma_(a-r) respectively; every core edge consequently meets two faces in U_d. All other square edges are lower boundary edges m_a--z_a, m_a--z_(a+1) or their antipodes, and each occurs once. They form the two disjoint cycles L,tau L. Links at every vertex are intervals or circles, giving a compact surface. Its faces are connected along the core since gcd(r,d)=1. Counting gives V=4d,E=6d,F=2d and Euler characteristic zero. It has two boundary circles, hence is an annulus. Its free quotient has one boundary circle and Euler characteristic zero, hence is a Möbius band. When d=3 all m_a=m and the six squares are precisely the six faces of Q_3. The two appearances of block E_j along L follow from the previously proved identities D(m_a,z_a)=E_(a+1) and D(m_a,z_(a+1))=E_(a+r+1). QED.

**Original-cube gallery resolution.** Retain the internal direction orders of the actual blue B-run and red A-run on each upper path. Form the lower path by transversely translating these two segments to the A-then-B order; the lower colors are the derivative words U_a,V_a of the preceding theorem. The two paths have the same endpoints and each uses every original direction in A union B once. They bound an explicit |A| by |B| grid of genuine original ij-squares, obtained by commuting the two ordered blocks. Antipodal squares resolve tau Sigma_a. Across shared core sides, all disks use the identical original edges and colors. This gives an antipodally equivariant abstract annular square-exchange complex mapping to the original 2-skeleton; images of distinct squares may intersect.

**Open forcing operation.** At defect three this carrier already gives projective RP^2. At higher defects it yields a Möbius band with median boundary L. Capping that boundary topologically is easy, while obtaining a coloring-compatible cap whose chains constrain the integer switch variation or force a direction-simple lower-defect geodesic remains open. No color-sensitive cap or NORI1 closure is asserted.


### The canonical relative projective square on the median Möbius carrier

Let d>=5 be odd, and let M=U_d/tau be the canonical seam Möbius band, with boundary the projective image of the median loop L. The antipodal annulus U_d->M defines a nonzero covering class omega in H^1(M;F_2), the generator. Its restriction to the boundary vanishes because the preimage of the unique boundary circle is the TWO disjoint circles L and tau L. The long exact cohomology sequence of (M,boundary M) gives an isomorphism
\[
H^1(M,\partial M;\mathbb F_2)\longrightarrow H^1(M;\mathbb F_2),
\]
as the boundary circle winds twice around the core and H^0(M)->H^0(boundary M) is an isomorphism. Denote the unique relative preimage of omega by omega_rel.

**Theorem (nonzero relative square).**
\[
\boxed{\langle\omega\smile\omega_{\mathrm{rel}},[M,\partial M]\rangle=1.}
\]
At d=3 the same statement is the absolute relation <omega^2,[RP^2]>=1 on the closed seam carrier.

*Proof.* Poincare-Lefschetz duality with F_2 coefficients sends omega_rel to a nonzero class in H_1(M;F_2), hence to the core-circle generator. Evaluating omega on that generator gives one, so cap/cup compatibility yields the displayed pairing. Equivalently, attaching a disk to the median boundary makes RP^2 and converts this relative square into its usual top Stiefel-Whitney square. QED.

**What the class does and does not force.** This is an explicit relative projective obstruction supported on original-direction block-square exchange galleries. It exists for EVERY odd-defect full geodesic and every legal coloring, and alone implies no monochromatic original path. A proposed NORI1 topological decoder must obtain, under the *hypothetical absence* of a low-defect path, a boundary trivialization or extension condition extracted from the SAME coloring's median-arm derivative words which forces the relative square to vanish. The exact simultaneous derivative inequality established above is a possible integer-valued input, but no construction is known which turns it into such a cohomological cancellation. An ordinary uncolored cap cannot meet this obligation.
