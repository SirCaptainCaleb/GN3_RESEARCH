# High-index Tucker forcing yields two actual same-root endpoint-opposed geodesics meeting at a vertex with opposite mirror-switch asymmetry

# A genuine Tucker connector: odd-dimensional NORI forces two endpoint-opposed full geodesics to meet and have opposite mirror-switch asymmetry

Let n>=7 be ODD, and let c be ANY active NORI coloring of PHYSICAL ORDERED three-faces satisfying c(bar F,rev pi)=1−c(F,pi). Fix ANY physical cube root x. For each full n-direction permutation p, let w(x,p)=(w_1,...,w_{n-2}) be the ACTUAL ordered-face color word and let D=n−3 be its number of switch positions. Because n is odd, D is EVEN. Let
\[
s_j(p)=w_j\oplus w_{j+1},\quad j=1,...,D.
\]
Call p ENDPOINT-OPPOSED if \(w_1\ne w_{n-2}\), equivalently its switch word has ODD Hamming weight.

For each endpoint-opposed p, define its CANONICAL MIRROR-SWITCH SIGNED LABEL:
\[
j(p)=\min\{1\le j\le D/2:s_j(p)\ne s_{D+1-j}(p)\},
\]
\[
\lambda(p)=
\begin{cases}
+j(p),&s_{j(p)}(p)=1,\\
-j(p),&s_{j(p)}(p)=0.
\end{cases}
\]
The label is well-defined: if all D/2 mirror pairs had matching bits, the total switch count would be EVEN, contradicting endpoint opposition. Under the actual full-geodesic NORI antipodal-reversal operation p→rev p at THE SAME root x, the entire window word transforms as \(w(rev p)=1-\operatorname{rev}w(p)\); hence the switch vector transforms as \(s(rev p)=\operatorname{rev}s(p)\), and
\[
\lambda(\operatorname{rev}p)=-\lambda(p).
\]
This is a genuine \(\mathbb Z_2\)-odd vertex labeling on all ACTUAL endpoint-opposed geodesics, with only k=D/2=(n−3)/2 coordinate labels.

**THEOREM (physical root-compatible mirror-switch Tucker pair).** For EVERY odd n>=7 and EVERY root x, there exist TWO ACTUAL full antipodal directed geodesics \(P=(x,p)\) and \(Q=(x,q)\), both endpoint-opposed, such that:
1. Their signed mirror-switch labels are COMPLEMENTARY, \(\lambda(p)=+j\), \(\lambda(q)=-j\), for some \(1\le j\le(n−3)/2\). Thus
\[
s_j(p)=1,\quad s_{n-2-j}(p)=0,\qquad
s_j(q)=0,\quad s_{n-2-j}(q)=1,
\]
where the reflected position is D+1−j=n−2−j.
2. Their direction permutations share SOME proper nonempty INITIAL COORDINATE SUPPORT:
\[
\{p_1,...,p_\ell\}=\{q_1,...,q_\ell\}
\quad\text{for some }1\le\ell\le n−1.
\]
In particular P and Q pass through the SAME genuine physical cube vertex \(y=x\oplus\{p_1,...,p_\ell\}\) at time \ell, as well as their common antipodal endpoints x and bar x.
3. The permutations q and rev p are necessarily DIFFERENT: the pair is not merely the tautological antipodal-reversed copy of one geodesic.

**PROOF.** Let P_n be the standard centered (n−1)-dimensional permutohedron whose original vertices are full direction orders, with antipodal involution p→rev p. Its boundary is a free-antipodal sphere S^(n−2). Use the genuine integer-valued endpoint imbalance \(f(v_p)=w_1(x,p)+w_{n−2}(x,p)-1\in\{-1,0,+1\}\). The NORI antipodal-reversal law makes f ODD; it is 1-Lipschitz on ACTUAL adjacent-transposition edges of the permutohedron, since swapping adjacent positions changes at most one of the first and final ordered three-face colors when n>=7. Let F be the equivariant barycentric piecewise-linear extension averaging f over original vertices of each face and interpolating over flags of faces, and put Z=F^(-1)(0).

The previously proved endpoint-zero index theorem, Item nori_permutohedral_antipodal_sphere_endpoint_color_balance_high_index_20261008, gives
\[
w_1(Z/\tau)^{n−3}\ne0,
\]
so no equivariant continuous map Z→S^(k−1) exists for k=(n−3)/2.

We now construct a GENUINELY CARRIED simplicial labeling of Z. Every point z∈Z lies in a unique relative interior of a PROPER permutohedron face H(z). This face H(z) has an ACTUAL endpoint-opposed original permutation vertex. Indeed, if H(z) had no f=0 original vertex, its connected original 1-skeleton (true for any convex-polytope face) together with the 1-Lipschitz property of f would force f to be CONSTANT +1 or CONSTANT −1 on all vertices of H(z). The barycentric extension F would then be identically that sign on H(z), contradicting F(z)=0.

Choose a finite centrally equivariant triangulation of the PL zero complex Z that refines the barycentric triangulation of ∂P_n. For each triangulation vertex z, choose an actual f=0 permutation p_z contained in the minimal P_n-face H(z). Choose the permutations in antipodal pairs so \(p_{\tau z}=\operatorname{rev}p_z\); this is consistent because proper permutohedron faces come in DISJOINT antipodal pairs, and the involution is free. Assign the signed label \lambda(p_z)∈{±1,...,±k} to z. The labels are genuinely antipodally ODD.

Suppose for contradiction that NO edge of this zero-set triangulation has opposite labels +j and -j. Then every simplex's vertex-label set contains no complementary pair (every pair of simplex vertices is an edge). Map each labeled vertex +j to the standard basis vector e_j∈R^k and -j to -e_j; interpolate linearly on simplices. Since a simplex contains no complementary pair, its positive barycentric combinations of signed basis vectors CANNOT vanish: for each coordinate index the appearing signs are either all + or all −, and at least one nonzero coordinate appears. Normalize to obtain a continuous τ-equivariant map Z→S^(k−1), contradicting the high antipodal index of Z. Therefore some genuine ZERO-SET SIMPLEX EDGE zz' has complementary labels ±j.

Because the triangulation refines the barycentric face-flag triangulation of ∂P_n, the two z,z' lie in a common flag simplex and therefore in a common PROPER polytope face H. Their selected actual f=0 permutations p_z,p_z' lie in the respective minimal faces H(z),H(z')⊆H, hence both lie in H. Every proper permutohedron face is contained in some proper FACET. A facet of the standard permutohedron is given by a nonempty proper subset S of coordinates occupying the first |S| positions of the order (or by its complementary last-block equivalent). Thus any two original vertices p,q in that facet share an exact proper prefix used-coordinate SUPPORT S. Their full geodesics from root x therefore meet at x⊕S. Moreover a proper convex face cannot contain both centrally antipodal original vertices p and rev p: their midpoint is the CENTER of P_n, an interior point. So q≠rev p. Finally their switch labels ±j give the displayed physically verified opposite reflected switch bits. QED.

**INTERPRETATION.** This is a DIMENSION-INDEPENDENT GENUINE TOPOLOGICAL FORCING THEOREM, NOT a virtual barycentric zero only: high index and Tucker's no-complement obstruction force TWO HONEST full physical geodesic witnesses at the SAME ROOT, with a common intermediate cube vertex and opposed mirror-switch patterns. The proof uses physical face locality, active NORI oddness, and the actual permutohedron face incidence. It does NOT YET force either geodesic to have <=1 switch; the remaining combinatorial obligation is to leverage the common-prefix-support connector and opposite mirror-switch orientations to exchange segments or slides while preserving a full geodesic and strictly reducing defects.

**OPEN NEXT STEP.** Strengthen this Tucker pair to a *compatible local exchange*: either force q to be obtained from p by one adjacent transposition with controlled two-window effects, or force a common intermediate vertex at a switch boundary with monochromaticly compatible ordered-two-direction tails, thereby connecting directly to the exact reversed-tail support-overlap NORI closure theorem. No such strengthening is claimed in this item.
