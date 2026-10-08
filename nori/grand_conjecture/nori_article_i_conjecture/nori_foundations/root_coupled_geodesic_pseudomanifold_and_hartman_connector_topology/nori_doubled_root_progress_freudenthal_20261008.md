# Root–progress 2n-cube: simultaneous Freudenthal charts, 6D face carriers, and root-slide squares

# The doubled root–progress cube: a universal Freudenthal geometry

Let \(C=[0,1]^n_r\times[0,1]^n_s\). Its Boolean vertices are pairs \((r,S)\), where \(r\in\{0,1\}^n\) is a starting root and \(S\subseteq[n]\) is the set of already traversed directions. Define the physical-vertex map on Boolean vertices by
\[
q(r,S)=r\oplus 1_S.
\]
It has the continuous, coordinatewise bilinear extension
\[
\Psi_i(r,s)=r_i+s_i-2r_i s_i. \tag{1}
\]

**Theorem 1 (a single common Freudenthal realization).** The standard Freudenthal triangulation of the \(2n\)-cube restricts on every vertical \(n\)-face \(C_r=\{r\}\times[0,1]^n_s\), with \(r\in\{0,1\}^n\), to the usual Freudenthal triangulation of the progress cube. Its top simplices are exactly the maximal chains
\[
(r,\varnothing),(r,\{p_1\}),\ldots,(r,[n])
\]
indexed by \(p\in S_n\). Applying \(q\) to the ordered vertices yields the actual full antipodal geodesic
\[
r,\ r\oplus\{p_1\},\ldots,r\oplus[n]
\]
in \(Q_n\). Hence all \(2^n\) rooted geodesic chart systems occupy separate coordinate faces of ONE common triangulated \(2n\)-cube, without incompatible crossing diagonals.

*Proof.* A Freudenthal simplex is a chain of Boolean vertices under the product coordinate order. Fixing all \(r\)-coordinates to a Boolean vertex restricts these to chains of the \(s\)-coordinates. Every maximal such chain is obtained by turning on the \(n\) progress bits once, in a unique permutation order. The XOR formula then flips the physical coordinates in precisely that order. \(\square\)

**Theorem 2 (actual ordered-face labels lift to six-dimensional carriers).** Fix a vertical chamber \((r,p)\) and window index \(i\). Its free progress triple is \(W_i=\{p_i,p_{i+1},p_{i+2}\}\). The actual ordered physical face has exterior values
\[
q_j=r_j\oplus 1_{\{j\in S_{i-1}\}},\qquad j\notin W_i.
\]
The color depends only on the exterior values and the ordered free triple, so changing any of the three root bits indexed by \(W_i\) preserves the label. Thus the eight root-slice progress three-faces with root \(r\oplus T\), \(T\subseteq W_i\), lie in a common 6-dimensional coordinate face of \(C\) on which their assigned ordered-face labels agree. (Both root and progress coordinates in \(W_i\) are free in this carrier.) Two adjacent window labels jointly remain invariant under root toggles in the common two-element free-direction intersection \(W_i\cap W_{i+1}\); their change bit descends to a 4-dimensional root–progress coordinate carrier.

*Proof.* The physical face forgets the root/progress coordinates corresponding to its three free directions. For adjacent windows, precisely the two common free coordinates can be toggled in the root while leaving both face labels unchanged. \(\square\)

**Theorem 3 (root slides are explicit diagonal-square corridors).** Let \(p=(a,p_2,\ldots,p_n)\), \(r'=r\oplus\{a\}\), \(p'=(p_2,\ldots,p_n,a)\). For \(0\le k\le n-1\) define
\[
S_{k+1}=\{a,p_2,\ldots,p_{k+1}\},\qquad
T_k=\{p_2,\ldots,p_{k+1}\}.
\]
Then \(q(r,S_{k+1})=q(r',T_k)\), and the two vertices \((r,S_{k+1})\) and \((r',T_k)\) are opposite corners of the elementary square obtained by varying the two coordinates \((r_a,s_a)\). Consequently a root slide between full geodesics appears as an \(n\)-square corridor in the doubled cube, with \(n\) identical physical vertices; it preserves the first \(n-3\) overlapping ordered window objects and adds one new final window. This geometrically realizes the exact word transport
\[
(w_1,\ldots,w_{n-2})\longmapsto(w_2,\ldots,w_{n-2},b).
\]

**Antipodal reversal.** The global fiber reflection \(J:(r,s)\mapsto(r,\mathbf1-s)\) takes each vertical Freudenthal chain to its reversed-permutation chain (after reversing vertex order), and
\[
\Psi(r,\mathbf1-s)=\mathbf1-\Psi(r,s).
\]
Thus the NORI involution and complementary-reversed window word are represented exactly within root slices. The standard full \(2n\)-dimensional Freudenthal triangulation is *not* generally \(J\)-simplicial on mixed root/progress simplices: reflection of progress coordinates reverses the diagonals of mixed root/progress squares. A \(J\)-invariant common polyhedral refinement (and its barycentric subdivision) supplies an equivariant triangulation, refining but retaining the original vertical Freudenthal chambers as geometric carriers.

**Topological guardrail.** The fixed-point set of \(J\) is the whole root midsection
\[
\operatorname{Fix}(J)=[0,1]^n_r\times\{(1/2,\ldots,1/2)\}_s.
\]
Any continuous \(J\)-odd map \(f:C\to\mathbb R^d\) vanishes identically along this midsection. Removing it leaves a free \(J\)-space equivariantly homotopy equivalent to \([0,1]^n\times S^{n-1}\), in turn equivariantly homotopy equivalent to \(S^{n-1}\) with antipodal action, by contracting the fixed root factor. Hence a direct Borsuk–Ulam argument on the untouched doubled cube adds no equivariant index beyond that of a fixed-root progress sphere. A proof of NORI must exploit the nontrivial colored root/incidence carriers or impose a relative boundary condition, not merely apply odd-map zero existence.

**Mixed-simplex warning.** The vertex map \(q(r,S)=r\oplus S\) does not define a simplicial map from the entire \(2n\)-Freudenthal triangulation to the all-root geodesic pseudomanifold \(K_n\). For \(n=2\), a monotone doubled-cube chamber flipping root bits \(r_1,r_2\) and then progress bits \(s_1,s_2\) maps to physical vertices \(00,10,11,01,00\), containing all four cube vertices; all four do not span a face of \(K_2\). Such mixed 2n-chambers project to closed walks using each physical coordinate twice, not necessarily to antipodal geodesics. Extracting one vertical chamber is a substantive proof obligation.

**Research frontier.** Use the 6-dimensional ordered-window carriers, 4-dimensional seam carriers, and diagonal-square root-slide corridors as the legal cells of a reversible one-switch repair complex. For Hartman least-unreachable labels, targets must encode *jointly realizable* terminal supports; coordinatewise reachability alone does not suffice. Prove a Sperner/KKM boundary condition and a terminal-extraction theorem compatible with the carrier geometry.
