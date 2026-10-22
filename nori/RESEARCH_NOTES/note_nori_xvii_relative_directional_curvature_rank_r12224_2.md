# Sharp relative directional-curvature rank on the monochromatic cubical carrier

- Stable ID: note_nori_xvii_relative_directional_curvature_rank_r12224_2
- Author: session_nori_r12224_2
- Primary home: subsection:central_freudenthal_subdivision_and_the_all_root_geodesic_chamber_sphere
- Labels: NORI1, combinatorial-topology, relative-curvature, monochromatic-filling, mixed-faces, unrestricted
- Lifecycle: active
- Epistemic status: proved
- Current version: 3
- Retention: current and at most one previous snapshot
- Created session: session_nori_r12224_2
- Updated session: session_nori_r12224_2
- Disposition: none
- Successor: none

## Related references

- note:note_nori_xi_monochromatic_cubical_index_annihilator_r12202
- note:note_nori_xiv_direction_resolved_projective_curvature_r12034
- subsection:curvature_realization_gauge_phases_and_rooted_square_defect_transport

## Research note

# Sharp relative directional-curvature rank

Let \(n\ge3\). Color the undirected edges of \(Q_n\) by \(c_i(x)=c_i(x\oplus e_i)\in\mathbb F_2\), satisfying \(c_i(\bar x)=1+c_i(x)\). Write \(Y=\partial[0,1]^n/\tau\cong\mathbb{RP}^{n-1}\). Let \(M\subseteq Y\) comprise the entire quotient one-skeleton and the images of all monochromatic proper cubical faces. No additional disks along closed walks are included.

For direction \(i\), define the descended 2-cochain \(\beta_i\) on an \((i,j)\)-square orbit by \(D_jc_i(x)=c_i(x)+c_i(x\oplus e_j)\), and put \(\beta_i=0\) on squares not involving \(i\). Antipodal oddness makes this well-defined. The known directional-curvature theorem gives \(d\beta_i=0\) and \([\beta_i]=u^2\in H^2(Y;\mathbb F_2)\), where \(u\) generates \(H^1(Y)\).

**Theorem (sharp relative rank).** Each \(\beta_i\) vanishes on \(M\), hence determines \(\eta_i\in H^2(Y,M;\mathbb F_2)\) mapping to \(u^2\). The kernel
\[
K(c)=\{S\subseteq[n]:\sum_{i\in S}\eta_i=0\}
\]
is a ring of subsets under symmetric difference and intersection. It consists of all unions of pairwise disjoint minimal nonempty blocks \(A_1,\dots,A_r\). Each block has even cardinality at least two, so
\[
\boxed{\dim\langle\eta_1,\dots,\eta_n\rangle=n-r\ge\lceil n/2\rceil.}
\]
Equality is attainable for every \(n\ge3\).

An equivalent characterization of \(S\in K(c)\) is: (a) \(D_jc_i=0\) for every \(i\in S,\ j\notin S\); (b) \(D_jc_i=D_ic_j\) for every distinct \(i,j\in S\), everywhere on the original cube. Thus the selected direction rules are independent of dimensions outside \(S\), and the induced color one-cochain is closed on the \(S\)-cube.

**Proof.** On every monochromatic square, parallel \(i\)-edges have identical colors, so \(\beta_i=0\). Hence each \(\beta_i\) is a relative cocycle. Because \(M\) contains every one-cell of \(Y\), \(C^1(Y,M)=0\); thus two relative degree-two cocycles represent the same class precisely when their cochains coincide. On an \((i,j)\)-square, \(\sum_{k\in S}\beta_k\) equals \(D_jc_i\) if \(i\in S,j\notin S\), equals \(D_ic_j\) if \(j\in S,i\notin S\), equals \(D_jc_i+D_ic_j\) if \(i,j\in S\), and equals zero otherwise. This proves (a),(b).

For nonempty \(S\in K(c)\), (a) makes the selected edge rules independent of all bits outside \(S\). By (b), they form a closed one-cochain on the contractible \(S\)-cube, so \(c_i(x)=f(x)+f(x\oplus e_i)\) for some Boolean potential \(f\) on \(Q_S\). Define \(h(x)=f(x)+f(\bar x)\), where the bar here complements all bits in \(S\). Oddness of the selected edge rules implies \(D_ih=c_i(x)+c_i(\bar x)=1\) for every \(i\in S\). Therefore \(h(x)=\sum_{i\in S}x_i+\lambda\). As \(h(\bar x)=h(x)\), the cardinality of \(S\) is even.

Linearity gives closure of \(K(c)\) under symmetric difference. For \(S,T\in K(c)\), put \(I=S\cap T\). If \(i\in I\) and \(j\notin I\), then \(j\notin S\) or \(j\notin T\), and (a) for that set gives \(D_jc_i=0\). Condition (b) on \(I\) follows from (b) on \(S\). Hence \(I\in K(c)\). The minimal nonempty members of a finite ring of subsets are disjoint; the entire ring is their collection of unions. Each has even size at least two, so \(r\le\lfloor n/2\rfloor\).

For sharpness pair the dimensions as \((1,2),(3,4),\ldots,(2m-1,2m)\), with \(m=\lfloor n/2\rfloor\). Define \(c_{2k-1}(x)=x_{2k}\), \(c_{2k}(x)=x_{2k-1}\). If \(n=2m+1\), additionally set \(c_n(x)=x_1\). These undirected edge rules are antipodally odd. Every paired block belongs to \(K(c)\), so \(r\ge m\), and therefore \(r=m\), attaining the rank bound. \(\square\)

**Relation to unrestricted NORI1.** The ordinary absolute classes \([\beta_i]=u^2\) coincide, while their relative lifts on the monochromatic cubical carrier retain at least \(\lceil n/2\rceil\) linearly independent classes. Dependencies arise precisely from autonomous, curl-free, even-dimensional blocks. This links the direction-resolved curvature of Article XIV to the monochromatic-filling relative obstruction of Article XI without restricting nonlinear edge rules or losing shared-edge consistency. The rank bound holds for successful colorings too; it supplies neither a monochromatic direction-simple antipodal geodesic nor a selection theorem. In particular its application to the central all-root Freudenthal sphere still requires a mechanism coupling these classes to compatible minimum-defect original-cube paths.

**First-cohomology corollary (transgression of independent curvature differences).** The same monochromatic cubical carrier satisfies
\[
\boxed{\dim_{\mathbb F_2}H^1(M;\mathbb F_2)\ge
\dim\langle\eta_1,\ldots,\eta_n\rangle\ge\lceil n/2\rceil.}
\tag{2}
\]
In fact, if \(R=\dim\langle\eta_i\rangle\), the \(R-1\) independent differences of relative directional curvature classes that map to zero in \(H^2(Y)\) lie in the image of the connecting homomorphism \(H^1(M)\to H^2(Y,M)\); they supply \(R-1\) linearly independent classes modulo the restriction of the antipodal covering class \(u\).

**Proof.** The long cohomology sequence of the pair includes
\[
H^1(Y)\xrightarrow{\mathrm{res}}H^1(M)
\xrightarrow{\delta}H^2(Y,M)\xrightarrow{j^*}H^2(Y).
\]
Every \(\eta_i\) maps to the same nonzero \(u^2\). Hence the intersection of their span with \(\ker j^*\) has dimension \(R-1\) and lies in \(\operatorname{im}\delta\). The restriction \(\mathrm{res}(u)\) is nonzero: the projected one-cycle of any original direction-simple full antipodal geodesic lies in the quotient one-skeleton contained in \(M\) and evaluates to one under the covering class \(u\). Thus \(\mathrm{res}\) has rank one. The sequence gives \(\ker\delta=\operatorname{im}\mathrm{res}\) of dimension one, so \(\dim H^1(M)\ge (R-1)+1=R\). \(\square\)

**Interpretation.** The extra independent relative directional-curvature data live as nontrivial loop classes of the monochromatic cubical carrier modulo the antipodal covering loop. This supplies a topological interface to test against ordered geodesic chambers. It does not establish that any of those extra loops lift to a single monochromatic original direction-simple antipodal geodesic, nor that a globally minimal defect family detects them.

**Canonical loop cocycles recover the established projective seam selector.** For distinct directions \(i,j\), let \(b_i\) upstairs be the edge one-cochain taking the given edge color on \(i\)-edges and zero on all other edges. Write \(x_k\) for the bit function at an original cube vertex. Choose a Boolean vertex function \(g_{ij}\) satisfying
\[
g_{ij}(x)+g_{ij}(\bar x)=x_i+x_j
\tag{3}
\]
on every antipodal vertex pair; such a function exists because the right-hand side is antipodally invariant. Then
\[
\boxed{\alpha_{ij}=b_i+b_j+d g_{ij}}
\tag{4}
\]
is invariant under the deck involution, so descends to a one-cochain on the folded cubical boundary \(Y\). Its coboundary is \(\beta_i+\beta_j\), hence it restricts to a closed one-cochain on \(M\), and
\[
\delta[\alpha_{ij}|_M]=\eta_i+\eta_j.
\tag{5}
\]
Its cohomology class on \(M\) is independent of the choice of \(g_{ij}\) satisfying (3).

**Proof.** Deck translation complements each original \(i\)-edge color, giving \(\tau^*(b_i+b_j)+(b_i+b_j)=d(x_i+x_j)\). Applying \(d\) to (3) shows \(\tau^*(d g_{ij})+d g_{ij}=d(x_i+x_j)\). Their sum (4) descends, and \(d\alpha_{ij}=\beta_i+\beta_j\). On monochromatic proper cubical faces the latter two-cochain vanishes, proving the restriction is closed and its relative connecting image is (5). The difference of two solutions of (3) is invariant under antipodality, so its coboundary downstairs does not change the restricted cohomology class. \(\square\)

Let \(C\) be any projective direction-once antipodal geodesic circuit, represented by an original full path \(P:x\to\bar x\). Write \(w_i(P)\) for the given color of its unique \(i\)-edge and \(m(C)\) for the established projective majority of the red-to-blue seam vertices. The global seam-gradient identity gives \(m_i=x_i+1+w_i(P)\), interpreted modulo antipodal complementation. Directly summing (4) along the lifted path gives
\[
\boxed{\langle[\alpha_{ij}|_M],[C]\rangle
=w_i(P)+w_j(P)+x_i+x_j=m_i(C)+m_j(C).}
\tag{6}
\]
This is independent of the chosen root along \(C\), reversal, and the gauge function \(g_{ij}\). Thus the complete family of pairwise loop evaluations reconstructs the established canonical projective selector \([m(C)]\). In particular, projective geodesic circuits homologous in \(M\) have identical seam-majority selectors.

**The remaining incidence obligation.** The known selector characterization says that NORI1 is equivalent to the existence of one projective direction-once circuit \(C\) such that
\[
\boxed{[m(C)]\in V(C).}
\tag{7}
\]
Indeed, root \(P\) at a vertex representing \([m(C)]\); then \(w_i(P)=1\) in every direction when \(x=m(C)\), or \(w_i(P)=0\) when \(x=\bar m(C)\). Formula (6) realizes the selector by cohomology, yet neither the rank lower bound nor the loop cocycles (4) force incidence (7). Standard single-path exchange disks pair with all \(\eta_i\) in the same way, since \(\langle\beta_i,\Sigma_P\rangle=1\) for every \(i\). Thus their evaluations annihilate all differences \(\eta_i+\eta_j\). Detecting the new relative information requires chains with nontrivial boundary in \(M\), geometrically linked to more than a single unmarked path. A successful continuation must retain path order and the position of its loop relative to its selector, for example through jointly marked all-root chamber families and shared-edge-compatible recombination.
