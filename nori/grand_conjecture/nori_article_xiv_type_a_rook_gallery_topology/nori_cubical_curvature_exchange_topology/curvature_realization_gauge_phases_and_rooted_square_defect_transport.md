# Curvature realization, gauge phases, and rooted square-defect transport

# Curvature realization, gauge phases, and rooted square-defect transport

This subsection gives a complete description of what the square curvature of an unrestricted antipodally odd cube-edge coloring can be, and separates the resulting projective cohomology from the additional root-sensitive information needed in a Wu–Yang dimension-simple chain-map adaptation.

Fix \(n\ge3\), put \(B_n=\partial[0,1]^n\), \(Y_n=B_n/\tau\cong\mathbb{RP}^{n-1}\), and work over \(\mathbb F_2\). Let \(u\in H^1(Y_n)\) denote the generator. Write \(\pi:B_n\to Y_n\) for the quotient and let \(\mathbf1\in C^1(B_n)\) denote the cochain that is one on every cube edge. A **legal** cube-edge coloring is \(c\in C^1(B_n)\) satisfying
\[
\tau^*c=c+\mathbf1.
\tag{1}
\]
The cubical curvature \(\kappa=\delta c\) is antipodally invariant and descends to a two-cocycle \(\bar\kappa\in Z^2(Y_n)\). Article XIV, Subsection 28, proved \([\bar\kappa]=(n\bmod2)u^2\).

## Theorem 1 (complete curvature realization and fiber classification)

A two-cochain \(\eta\in C^2(Y_n)\) is the descended square curvature of some legal unrestricted cube-edge coloring **if and only if**
\[
\boxed{\delta\eta=0,\qquad [\eta]=(n\bmod2)u^2.}
\tag{2}
\]
Every such \(\eta\) has precisely
\[
\boxed{2^{\,2^{n-1}}}
\tag{3}
\]
legal edge-coloring lifts, and the total number of distinct realizable curvature configurations is
\[
\boxed{2^{\,(n-2)2^{n-2}}.}
\tag{4}
\]

*Proof.* Necessity is the projective-curvature theorem from Subsection 28. For sufficiency, choose one explicit legal reference coloring \(c_*\) with descended curvature \(\eta_*\). For even \(n\), one may take the flat coloring
\[
c_{*,i}(x)=\sum_{j\ne i}x_j,
\]
for which \(\eta_*=0\). For odd \(n\), fix two dimensions \(a\ne b\) and take
\[
c_{*,a}(x)=\sum_{j\notin\{a,b\}}x_j,\qquad
c_{*,i}(x)=x_a\quad(i\ne a),
\]
for which \(\eta_*=\bar K_{ab}\), representing \(u^2\). As \([\eta]=[\eta_*]\), there exists \(d\in C^1(Y_n)\) such that \(\delta d=\eta+\eta_*\). Then \(c=c_*+\pi^*d\) obeys (1), and its curvature descends to \(\eta\). This proves realizability.

Every legal \(c'\) differs from \(c_*\) by an antipodally invariant one-cochain and hence equals \(c_*+\pi^*d'\) for a unique quotient cochain \(d'\). Two such choices have the same curvature if and only if \(d'-d\in Z^1(Y_n)\). The quotient CW complex has \(2^{n-1}\) vertices. Its connected one-skeleton gives
\[
\dim B^1(Y_n)=2^{n-1}-1,\qquad
\dim H^1(Y_n)=1,
\]
so \(\dim Z^1(Y_n)=2^{n-1}\) and every curvature has the number of lifts in (3).

There are \(n2^{n-2}\) antipodal undirected-edge orbits, so all legal colorings number \(2^{n2^{n-2}}\). Dividing by the constant fiber size (3) gives (4). \(\square\)

**Interpretation.** The fixed projective class is the **only** restriction on the realizable square-curvature cochain, beyond the ordinary cocycle condition. In particular every cocycle representative of that class occurs without placing any further restrictions on the original edge coloring.

## Theorem 2 (two gauge phases above every curvature)

Define a **vertex gauge transformation** by
\[
c\longmapsto c+\delta h,
\tag{5}
\]
where \(h\) is an antipodally invariant zero-cochain, \(h(\tau x)=h(x)\). It preserves both legal antipodal oddness and every square curvature. For any fixed realizable curvature \(\eta\), its legal coloring lifts fall into **precisely two** orbits under these transformations.

Choose any dimension \(a\), and let \(d^{(a)}\) be the invariant one-cochain which is one on all edges in dimension \(a\), and zero on all other edges. Then \(d^{(a)}\) represents \(u\in H^1(Y_n)\); the two gauge phases of a coloring \(c\) can be represented by
\[
\boxed{c,\qquad c+d^{(a)}.}
\tag{6}
\]

*Proof.* Two lifts of one curvature differ by a closed one-cochain \(d\) on \(Y_n\). Gauge transformations change \(d\) by a quotient coboundary. The orbit set is therefore the affine space over \(H^1(Y_n;\mathbb F_2)\cong\mathbb F_2\), consisting of two classes. The cochain \(d^{(a)}\) is closed, as every square has two dimension-\(a\) edges. Its evaluation on the projected path of any full antipodal geodesic is one, since that path traverses dimension \(a\) once, so the class is nonzero and equals \(u\). This proves (6). \(\square\)

**Warning for the proof search.** A vertex gauge transformation is not generally a symmetry of the monochromatic-geodesic problem: it may change which paths have constant color. For example, in dimension four, start with the flat coloring \(c_{*,i}(x)=\sum_{j\ne i}x_j\), and take root \(x=(1,1,0,0)\). This root admits monochromatic full geodesics, since its bits can be read in alternating order. Let \(h(x)=x_1+x_2\), which is antipodally invariant, and let \(c'=c_*+\delta h\). The coloring \(c'\) has **the same zero curvature** but has no monochromatic full geodesic starting at that particular root: along a dimension order \(\pi\), its edge word is \(w_k=|x|+x_{\pi_k}+{\bf1}_{\{\pi_k\in\{1,2\}\}}+(k-1)=k-1\pmod2\), which always alternates. Other roots may still support favorable paths. Thus curvature does not determine even rooted monochromatic reachability, and cannot replace the full edge-incidence data in a Wu–Yang proof.

## Theorem 3 (rooted-square defect transport)

Fix a square in dimensions \(i,j\), with four undirected edge bits
\[
A=c_i(y),\quad B=c_j(y\oplus e_i),\quad
C=c_j(y),\quad D=c_i(y\oplus e_j).
\tag{7}
\]
The color-one monochromatic two-route defect, rooted at its corner \(y\), is
\[
\Omega_1(y;i,j)=AB+CD.
\tag{8}
\]
For the other corners the same definition gives
\[
\boxed{
\Omega_1(y\oplus e_i\oplus e_j;i,j)=\Omega_1(y;i,j),}
\tag{9}
\]
and
\[
\boxed{
\Omega_1(y\oplus e_i;i,j)
=\Omega_1(y\oplus e_j;i,j)
=\Omega_1(y;i,j)+(A+D)(B+C).
}
\tag{10}
\]
Write the parallel-edge discrepancies as
\[
\lambda_i=A+D,\qquad\lambda_j=B+C.
\]
Then
\[
\boxed{\kappa(F)=\lambda_i+\lambda_j,\qquad
\text{root-corner defect change}=\lambda_i\lambda_j.}
\tag{11}
\]

*Proof.* From the opposite corner the two increasing routes have edge-bit pairs \((D,C)\) and \((B,A)\), giving \(DC+BA=AB+CD\). From either adjacent corner the pairs are \((A,C)\) and \((B,D)\), giving \(AC+BD\). The difference
\[
AB+CD+AC+BD=(A+D)(B+C)
\]
proves (9)–(10). Equation (11) follows directly from the four-edge definition of \(\kappa\). \(\square\)

**Corollary 4 (curved-square rigidity versus flat-square root holonomy).** If \(\kappa(F)=1\), then \(\lambda_i\ne\lambda_j\), hence \(\lambda_i\lambda_j=0\): the monochromatic defects \(\Omega_0,\Omega_1\) are independent of which of the four square corners is chosen as the root. If \(\kappa(F)=0\), then \(\lambda_i=\lambda_j\), and the rooted defects change between adjacent corners if and only if both pairs of parallel square edges have differing colors.

Under the global antipodal involution, \(\Omega_1(\tau y;i,j)=\Omega_0(y;i,j)=\Omega_1(y;i,j)+\kappa(F)\). Thus, on **curved** squares the defect is intrinsic to the local square corner but flips color under antipodality; on **flat** squares antipodality preserves the defect but local root changes may not. This is a precise algebraic separation of two phenomena that ordinary curvature alone merges.

## Proposition 5 (full local defect freedom at fixed curvature)

For every \(n\ge3\), every legal coloring \(c\), every chosen cube two-face \(F\), and either bit \(\epsilon\in\mathbb F_2\), there exists an antipodally invariant vertex gauge \(h\) such that
\[
\delta(c+\delta h)=\delta c
\quad\text{on every square,}
\qquad
\Omega_1^{\,c+\delta h}(F;y)=\epsilon
\tag{12}
\]
at any prescribed corner \(y\) of \(F\).

*Proof.* Given any two assignments of four edge bits on \(F\) with the same total parity \(\kappa(F)\), their difference has even parity and hence is the coboundary of some assignment of bits \(h\) to the four square vertices. For \(\kappa=0\), patterns \((A,B,C,D)=(0,0,0,0)\) and \((1,1,0,0)\) realize \(\Omega_1=0,1\). For \(\kappa=1\), patterns \((1,0,0,0)\) and \((1,1,1,0)\) do the same. Therefore choose the target square assignment with the prescribed \(\epsilon\) and the original curvature. For \(n\ge3\), the square \(F\) and its antipodal face are disjoint. Extend the four prescribed values of \(h\) to the antipodal mates by \(h(\tau v)=h(v)\), and choose values arbitrarily on all other antipodal vertex pairs. Then \(h\) is invariant, \(c+\delta h\) is legal with identical global curvature, and the target local defect has the desired bit. \(\square\)

**Consequence for the Wu–Yang adaptation.** The projective class of curvature, the rooted red/blue square defects, and the original complete path orders are three distinct layers of information. The curvature is determined by a freely realizable projective two-cocycle of fixed cohomology class. Even fixing that entire curvature cochain leaves \(2^{2^{n-1}}\) legal colorings, with large gauge orbits that can alter reachability, and the local color-specific defects can be changed at will by vertex gauges. Therefore a prospective equivariant chain correction that only reads \(\bar\kappa\) cannot capture the needed monochromatic gallery structure. A viable chain map must use the full rank-increasing edge incidences, retaining the local corner transport (10) and the global antipodal pairing, while allowing square-curvature correction chains to retain the forced projective \(u^2\) class. These results impose structural requirements on the unrestricted NORI1 proof and neither assume nor establish its desired existence conclusion.

## Theorem 6 (uniform full-geodesic words in every curvature fiber)

Fix \(n\ge3\), any realizable projective square-curvature cocycle \(\eta\), and **any specified full antipodal geodesic** \(P=P(x,\pi)\). For each binary word \(w\in\mathbb F_2^n\), let
\[
\mathscr C_{\eta,w}(P)=
\{c:\ c\text{ is a legal edge coloring with descended curvature }\eta
\text{ and whose edge word on }P\text{ equals }w\}.
\]
Then
\[
\boxed{\ |\mathscr C_{\eta,w}(P)|=2^{\,2^{n-1}-n}\quad
\text{for every }w\in\mathbb F_2^n. \ }
\tag{13}
\]
In particular, **every** realizable curvature class contains a legal coloring making the prescribed full dimension-simple geodesic monochromatic of either color. Both monochromatic words occur equally often, and each one is represented by the number of colorings in (13).

*Proof.* Fix one legal coloring \(c_*\) with curvature \(\eta\). By Theorem 1, all such colorings form the affine space \(c_*+Z^1(Y_n;\mathbb F_2)\), whose translation space has dimension \(2^{n-1}\). Restricting a quotient cocycle to the projected path \(P\) gives a linear map
\[
\rho_P:Z^1(Y_n;\mathbb F_2)\longrightarrow \mathbb F_2^n.
\]
We show it is surjective.

First, an antipodally invariant vertex gauge \(h\) changes the color of the \(j\)-th edge of \(P=(x_0,\ldots,x_n)\) by \(h(x_{j-1})+h(x_j)\). Since \(x_n=\tau x_0\), gauge invariance forces \(h(x_n)=h(x_0)\), so the sum of these changes along \(P\) is zero. Conversely **every** even-parity modification \(v\in\mathbb F_2^n\) is attainable: choose \(h(x_0)\) freely, define \(h(x_j)=h(x_{j-1})+v_j\) successively along the path, and use \(\sum_jv_j=0\) to ensure \(h(x_n)=h(x_0)\). No two of the internal path vertices are antipodal to one another or to either endpoint, because their used-dimension prefix sets are linearly nested and cannot be complementary. Therefore these assignments extend to an antipodally invariant \(h\) on the entire cube vertex set.

Next, the nontrivial quotient one-cocycle \(d^{(a)}\) from Theorem 2 is one on every edge of a chosen dimension \(a\), and zero elsewhere. Along \(P\), this changes the bit at the unique traversal of dimension \(a\), hence gives an odd-parity modification. The even-parity gauge modifications together with this odd-parity generator span all of \(\mathbb F_2^n\). Thus \(\rho_P\) is surjective, and every word has
\[
|\ker\rho_P|=2^{\dim Z^1(Y_n)-n}=2^{\,2^{n-1}-n}
\]
lifts, proving (13). \(\square\)

**Corollary 7 (curvature-blindness on individual complete paths).** No hypothesis expressed solely in terms of the entire square-curvature cochain can forbid any particular color word on a specified complete dimension-simple geodesic. Any useful Wu–Yang color-sensitive lift must exploit **simultaneous compatibility across multiple geodesics**, not evaluate one path against the curvature class in isolation. At the level of the gauge-orbit decomposition, a prescribed path's parity is fixed within one vertex-gauge orbit, but the second \(H^1(Y_n)\) phase toggles that parity.

The theorem does not imply the unrestricted NORI1 existence conjecture: the chosen coloring depends on the prescribed path. It identifies which information curvature forgets, and why the higher Coxeter homotopies of the following subsections are structurally relevant.


## Gauge-orbit averaging and the antipodal vertex-star closure reduction

Let \(n\ge2\), let \(c\) be any legal antipodally odd undirected-edge coloring of \(Q_n\), and let \(\tau x=\bar x\). Put \(N=2^{n-1}\). An *invariant vertex gauge* is \(h:Q_n\to\mathbb F_2\) with \(h(\tau x)=h(x)\), acting by
\[
c_i^h(x)=c_i(x)+h(x)+h(x\oplus e_i).
\tag{GA1}
\]
The gauge group has \(2^N\) elements, and constants act trivially, so its orbit on legal edge colorings has \(2^{N-1}\) members. A *vertex-star flip at \([v]=\{v,\bar v\}\)* is (GA1) with \(h\) supported on this antipodal vertex pair. Its support consists of all edges incident to \(v\) or \(\bar v\).

**Theorem (uniform even-parity words and gauge-averaged trace).** For any fixed rooted full antipodal geodesic \(P=(v_0,\ldots,v_n)\), the color word of \(c^h\), for uniformly random invariant \(h\), is uniform among the \(2^{n-1}\) binary words having the same total parity as the word of \(c\) on \(P\). In particular,
\[
\boxed{
\mathbb E_h\operatorname{tr}\!\left(P_\tau
\left(\frac{A+tD(c^h)}2\right)^n\right)=n!
\quad\text{for every real }t,
}
\tag{GA2}
\]
where \(P_\tau\) is the antipodal permutation matrix and \(D(c^h)\) is the signed adjacency operator of \(c^h\). Consequently,
\[
\boxed{\mathbb E_h N_0(c^h)=n!,}
\tag{GA3}
\]
where \(N_0\) counts rooted oriented monochromatic-zero full antipodal geodesics.

*Proof.* On the quotient vertex set \(Q_n/\tau\), the path \(P\) projects to a cycle with \(n\) distinct vertices \([v_0],\ldots,[v_{n-1}]\), closing at \([v_n]=[v_0]\). To see distinctness, its used-direction prefix sets form a strict chain; two such sets can be complementary only for the initial and final vertices. Restricting \(h\) to these \(n\) quotient vertices gives independent uniform bits. Its edge coboundary around the cycle runs uniformly over the even-parity subspace of \(\mathbb F_2^n\), proving the word-distribution assertion.

For \(s_i=(-1)^{c_i}\), the full path expansion is
\[
F_{c^h}(t)=2^{-n}\sum_{P}\prod_{e\in P}
(1+t\,s_e(c^h)).
\]
Averaging over \(h\) removes every term involving a nonempty proper subset of the path edges, because such a subset has nonempty boundary on the quotient cycle. The empty-subset term contributes one, and the full-subset term contributes \(t^n\prod_{e\in P}s_e(c)\). Root sliding, which removes the first path edge and appends its antipodal mate, bijects the rooted full geodesics and negates this full signed product. Therefore \(\sum_P\prod_{e\in P}s_e(c)=0\). The remaining average is \(2^{-n}(2^nn!)=n!\), proving (GA2) and (GA3). \(\square\)

**Corollary (every gauge orbit intersects the good-coloring set).** Every legal coloring has a gauge-equivalent coloring containing a monochromatic full antipodal geodesic. More quantitatively, each gauge orbit contains at least
\[
\boxed{2^{\,2^{n-1}-n}}
\tag{GA4}
\]
good colorings, a fraction at least \(2^{-(n-1)}\) of its members. There is a gauge transforming \(c\) to a good coloring which is a product of at most \(\lfloor n/2\rfloor\) vertex-star flips.

*Proof.* Root sliding pairs rooted full geodesics with opposite total color parity, so some path \(P\) has even parity. The first theorem gives precisely the fraction \(2^{-(n-1)}\) of gauges making its word all zero, and taking the quotient by the two constant gauges proves (GA4). For the flip bound, prescribe \(h\) successively along the \(n\) distinct quotient vertices of \(P\) to cancel all its edge colors. The even path parity ensures consistency on closing the projected cycle. The two complementary assignments on these \(n\) vertices induce the same edge corrections on \(P\); choose the one with at most \(\lfloor n/2\rfloor\) ones, and extend \(h=0\) at all other quotient vertices. Thus at most that many antipodal vertex-pair stars are flipped. \(\square\)

**Theorem (single vertex-star preservation is equivalent to unrestricted NORI1).** The following assertions are equivalent:

1. Every legal antipodally odd cube-edge coloring in every dimension has a monochromatic full antipodal geodesic.
2. For every legal coloring \(c\) having a monochromatic full antipodal geodesic, and every antipodal vertex pair \([v]\), the coloring obtained by one vertex-star flip at \([v]\) also has such a geodesic.

*Proof.* The first assertion directly implies the second. Conversely, by the preceding corollary, every gauge orbit contains a good coloring. The orbit is connected by single vertex-star flips, each staying within the legal coloring class. Under assertion 2, success propagates along every edge of this gauge-orbit graph and hence to every member. This proves assertion 1. \(\square\)

**Critical two-defect normal form.** If the grand conjecture fails, there are a good legal coloring \(d\) and an antipodal vertex pair \([v]\) such that \(d'=d+\delta\mathbf1_{[v]}\) is bad. Every monochromatic-zero full geodesic of \(d\) must meet \([v]\), since otherwise it remains zero in \(d'\). A full geodesic meets \([v]\) at one internal vertex or at its two antipodal endpoints. In the former case its word in \(d'\) has precisely two adjacent one-colored edges, while in the latter case its first and last edges are one-colored and all other edges zero. Thus a hypothetical counterexample has a gauge-adjacent representative with a two-defect geodesic whose defective edges form an antipodal vertex-star intersection.

The single-star preservation statement remains open. This result localizes the needed invariance to a perturbation supported on two antipodal vertex stars, independent of dimension, and does not assume vertex balance or bounds on square curvature.



## Vertex-star Petrie grade flux and distance-two defect repair

Fix \(n\ge3\) and a legal antipodally odd coloring. As in the projective Petrie grade theory of Article XV, let \(C\) range over projective Petrie cycles, whose twisted cyclic turn words \(\delta(C)=(\delta_0,\ldots,\delta_{n-1})\) have odd grade \(g(C)=\sum_j\delta_j\). Denote by \(N_g\) the number of such cycles of grade \(g\). Let \(c^{[v]}\) be the invariant vertex gauge that reverses all cube edges incident to the antipodal vertex pair \([v]\), and set
\[
\mathcal L_{\star}f(c)=\sum_{[v]\in Q_n/\tau}\bigl(f(c^{[v]})-f(c)\bigr).
\tag{SF1}
\]

For odd \(g\) let \(A_g^{(2)}\) count pairs \((C,[v])\) with \(g(C)=g\), \([v]\) on \(C\), and both *distance-two* cyclic turn positions affected by the star having \(\delta=1\). Define \(B_g^{(2)}\) analogously for both affected turns being zero. Put these counts equal to zero for inadmissible grades.

**Theorem (star-grade flux and balance drift).**
\[
\boxed{\mathcal L_\star N_g
=B_{g-2}^{(2)}+A_{g+2}^{(2)}-A_g^{(2)}-B_g^{(2)}.}
\tag{SF2}
\]
In particular
\[
\boxed{\mathcal L_\star N_1=A_3^{(2)}-(n-2)N_1.}
\tag{SF3}
\]
With \(T_1=\sum_g gN_g\) and \(M=2^{n-2}(n-1)!\) projective Petrie cycles,
\[
\boxed{\mathcal L_\star T_1=2nM-4T_1.}
\tag{SF4}
\]
If \(n=2m\ge4\) and \(c\) is vertex-balanced, **each individual** antipodal vertex-star flip has
\[
\boxed{T_1(c^{[v]})=T_1(c)-n(n-2)!.}
\tag{SF5}
\]

*Proof.* If \([v]\) is not among the \(n\) antipodal vertex pairs on \(C\), the star does not change \(C\)'s edge colors. Otherwise it reverses the two consecutive projective-edge colors incident to that vertex. Writing their cyclic indices as \(j-1,j\), the twisted turn bits at positions \(j-2\) and \(j\) are toggled, while the intervening turn is unchanged. Thus the grade increases by two for a 00 affected pair, decreases by two for 11, and stays unchanged for 01 or 10. Counting incoming and outgoing transitions over all stars proves (SF2). A grade-one turn word has precisely \(n-2\) star positions whose two affected turn bits are both zero and none with both one, proving (SF3).

For each cyclic word \(\delta\) of grade \(g\), summing over all \(n\) distance-two turn pairs gives
\[
\sum_j\bigl((1-\delta_j)(1-\delta_{j+2})-\delta_j\delta_{j+2}\bigr)
=\sum_j(1-\delta_j-\delta_{j+2})=n-2g.
\]
Its contribution to \(\mathcal L_\star T_1\) is \(2(n-2g)\). Summing over all cycles proves (SF4).

For (SF5), use the previously established identity
\[
T_1(c)=\frac{(n-2)!}{2}\sum_{x\in Q_n}r(x)(n-r(x)),
\]
where \(r(x)\) counts the incident one-colored edges. Balance gives \(r(x)=m\) everywhere. A star flip at \([v]\) interchanges zero and one incident edges at \(v,\bar v\), retaining \(r=m\) there, and changes \(r\) by \(+1\) or \(-1\) at each of the \(2n\) distinct neighboring vertices. Each such neighboring term \(r(n-r)\) decreases by one. This yields the drop \(n(n-2)!\). \(\square\)

**First-excess star criterion.** If \(c\) is bad (\(N_1(c)=0\)), then the *number* of good one-star neighbors, counted with multiplicity of newly successful grade-one cycles, is \(A_3^{(2)}\). In particular \(c\) has a good one-star neighbor if and only if some grade-three projective Petrie cycle has two switched turns separated by two positions. This local signature is distinct from the **adjacent** switched-turn pair arising in the previously established single-edge-orbit repair theorem. A boundary star flip turns the three-switch cycle into grade one and, correspondingly, creates a full monochromatic geodesic; its precursor geodesic has a pair of adjacent one-colored edges (or first and last one-colored edges).

The grade-flux identity was independently checked by enumeration of the rooted geodesic turn signatures and all \(2^{n-1}\) star neighbors in dimensions \(3,4,5\); the balanced pointwise drop (SF5) was checked in \(Q_4,Q_6\). These finite checks are not used in the general proof. Equation (SF3) is a structural necessary criterion, not proof that every bad coloring is adjacent to a good one: the known gauge-orbit connectivity guarantees a good coloring somewhere in its orbit, but a bad vertex may lie more than one star flip from its good subset.



## Two-step gauge strands, universal grade statistics, and sharp monotone Petrie repair

Fix \(n\ge3\), a legal antipodally odd cube-edge coloring \(c\), and one uncolored projective Petrie cycle \(C\). Label its \(n\) projective vertices \(v_j\) and successive projective edge orbits \(e_j\) cyclically, \(j\in\mathbb Z/n\mathbb Z\). Choose an oriented lift. Write \(b_j\in\mathbb F_2\) for its edge colors and \(\delta_j=b_j+b_{j+1}\), with the standard antipodal twist across the closing seam: the resulting turn word \(\delta\) satisfies \(\sum_j\delta_j=1\pmod2\). Let \(h_j\) be the bits of an invariant vertex gauge on these \(n\) distinct projective vertices.

**Theorem (two-step gauge derivative and orbit classification).**
\[
\boxed{\delta_j(c+\delta h)=\delta_j(c)+h_j+h_{j+2}.}\tag{GS1}
\]
All subscripts are cyclic. Therefore, setting \(q=\gcd(n,2)\), the gauge-action image on the turn word consists precisely of the vectors having even parity on each cycle of the step-two permutation \(j\mapsto j+2\). It has dimension \(n-q\).

For odd \(n\), the gauge orbit of the turn word is the **entire** set of odd-parity turn words. For even \(n=2m\), it is the half of all odd-parity turn words with prescribed parities
\[
\boxed{\sum_{j\ {\rm even}}\delta_j=\epsilon,\qquad
\sum_{j\ {\rm odd}}\delta_j=1+\epsilon.}\tag{GS2}
\]
Here \(\epsilon\) is unchanged by every vertex-star flip; shifting the cycle's chosen origin by one exchanges the two parity strands.

*Proof.* The edge of \(C\) from \(v_j\) to \(v_{j+1}\) changes color by \(h_j+h_{j+1}\); adding the changes on the two edges incident across turn \(j\) cancels the shared bit and leaves \(h_j+h_{j+2}\). The antipodally twisted closing term is a constant and does not change. The linear map \(h\mapsto(h_j+h_{j+2})_j\) is the edge coboundary of the graph whose components are the \(q\) cycles of the step-two permutation. Its kernel is formed by functions constant on each component and its image by even-parity words on each component. This proves the assertions. \(\square\)

**Theorem (full grade enumerator is universal inside each gauge orbit).** Let \(h\) be uniformly sampled from all \(2^{2^{n-1}}\) invariant vertex gauges, and \(g(C;c+\delta h)=|\delta(c+\delta h)|\). Then for every odd \(g\in\{1,3,\ldots,n\}\),
\[
\boxed{\Pr_h(g(C;c+\delta h)=g)=\frac{\binom ng}{2^{n-1}}.}\tag{GS3}
\]
The probability is zero for even \(g\). Consequently, with \(M=2^{n-2}(n-1)!\) projective Petrie cycles,
\[
\boxed{
\mathbb E_h\sum_Cz^{g(C;c+\delta h)}
=\frac{M}{2^n}\bigl((1+z)^n-(1-z)^n\bigr),
\qquad
\mathbb E_h N_g(c+\delta h)=\frac{(n-1)!}{2}\binom ng.
}\tag{GS4}
\]
These identities hold inside **each individual vertex-gauge orbit**, not merely on averaging across all legal edge colorings.

*Proof.* Uniform \(h\) restricts to uniform independent bits on the \(n\) distinct projective vertices of \(C\), hence produces the uniform distribution on the orbit in (GS1). If \(n\) is odd, the orbit is the set of \(2^{n-1}\) odd turn words, immediately giving (GS3). If \(n=2m\), its weight-generating function is
\[
\frac{(1+z)^m-(1-z)^m}{2}
\frac{(1+z)^m+(1-z)^m}{2}
=\frac{(1+z)^n-(1-z)^n}{4}
=\frac12\sum_{g\ {\rm odd}}\binom ngz^g.
\]
Dividing by the orbit size \(2^{n-2}\) gives precisely (GS3). Sum over \(C\) and use the stated value of \(M\) to obtain (GS4). \(\square\)

**Theorem (sharp star radius and monotone repair on a chosen cycle).** For every \(c\) and \(C\), there exists an invariant vertex gauge \(h\), supported entirely on the \(n\) projective vertex pairs of \(C\), such that
\[
\boxed{g(C;c+\delta h)=1,\qquad
|\operatorname{supp}h|\le\left\lfloor\frac{n-1}{2}\right\rfloor.}\tag{GS5}
\]
Moreover there is a sequence of individual star flips leading from \(c\) to a coloring with \(g(C)=1\) along which the grade **never increases**: every move either transports one turned position to a neighboring position on its step-two strand without changing grade, or annihilates a pair and decreases grade by two.

The bound in (GS5) is optimal if only this chosen Petrie cycle may be used: in odd dimension the admissible turn word with all \(n\) turn bits equal to one needs at least \((n-1)/2\) flips, while in even dimension the turn word with all but one turn bit equal to one needs at least \((n-2)/2\) flips. Every such odd-parity turn word can occur on the chosen cycle of a globally legal coloring, because its \(n\) projective edge orbits can be colored independently and the remaining edge orbits can be completed legally. Thus in even dimension \(n=2m\), every legal coloring is at most \(m-1\) star flips away from a coloring with a monochromatic full antipodal geodesic, improving the preceding \(m\)-flip estimate.

*Proof of (GS5).* For odd \(n\), choose any singleton target turn word \(\delta'=e_j\). The equation \(\partial_2h=\delta+\delta'\) is solvable by the image classification, and its two solutions are complementary on the single step-two cycle. One has support at most \(\lfloor n/2\rfloor=\lfloor(n-1)/2\rfloor\).

For even \(n=2m\), precisely one of the two length-\(m\) strands has odd defect parity. On the even-parity strand, solve the step-two coboundary equation to eliminate all defects and choose the better of the two complementary solutions; its support is at most \(\lfloor m/2\rfloor\). On the odd-parity strand, choose one remaining defect position \(j\) and solve the equation with target \(e_j\). When \(m\) is odd, taking the lighter complementary solution costs at most \((m-1)/2\) flips. When \(m\) is even, varying \(j\) over consecutive positions of the strand changes a chosen solution by the indicator of one vertex (up to a componentwise complement), because the two targets differ at adjacent positions. Thus not all candidate solutions can have weight precisely \(m/2\); for some \(j\), one of the complementary solutions has weight at most \(m/2-1\). Combining strands gives at most \(m-1=\lfloor(n-1)/2\rfloor\) flips.

For the monotone sequence, regard each strand as a cyclic binary word. Whenever a strand contains at least two defects, select two successive ones in cyclic order. If adjacent, flip their shared star to toggle 11 to 00. If separated by zeros, successively toggle 10 to 01 along their intervening arc, moving one defect until the pair is adjacent, and then cancel it. These moves never increase total grade and eventually leave no defects on even-parity strands and one on the odd-parity strand. Every such local toggle is a valid antipodally invariant vertex-star flip on \(C\), proving the assertion.

For optimality, a vertex-star flip changes precisely two turn bits and can reduce their total number by at most two. Starting at grade \(n\) when \(n\) is odd, or at grade \(n-1\) when \(n\) is even, therefore needs at least \((n-1)/2\) or \((n-2)/2\) flips, respectively. Arbitrary odd-parity twisted turn words are realizable by prescribing the \(n\) independent projective edge-orbit colors along \(C\), proving sharpness. \(\square\)

**Interpretation for unrestricted closure.** Individual Petrie cycles have no vertex-gauge obstruction to grade-one repair, even with a sharp short repair path and a nonincreasing grade potential. The entire gauge orbit of every fixed cycle also exhibits the universal random-coloring grade distribution (GS3). Therefore a hypothetical NORI1 obstruction must be *simultaneous across intersecting cycles*: the vertex-star flips that monotonically repair one cycle can disturb others. This identifies the missing compatibility problem rather than a restriction on any one cycle.



## Joint projective vertex-incidence geometry and gauge transfer

Represent an antipodal vertex pair by \([x]=\{x,\bar x\}\). A rooted full cube geodesic visits precisely \(n\) distinct projective vertex pairs; write \(\mathcal V(P)\subseteq Q_n/\tau\) for that set. The following enumerations are for the uniform population of \(2^n n!\) rooted oriented full geodesics, and do not depend on any coloring.

**Theorem (pair-incidence law).** Let \([u]\ne[v]\), and put \(d=d_H(u,v)\), \(1\le d\le n-1\). Then
\[
\boxed{
\Pr([v]\in\mathcal V(P)\mid[u]\in\mathcal V(P))
=\frac{2}{\binom nd},\qquad
\#\{P:[u],[v]\in\mathcal V(P)\}=\frac{4nn!}{\binom nd}.
}\tag{JI1}
\]
In particular adjacent projective vertex pairs are positively correlated in a random complete path relative to widely separated pairs, and the correlation depends only on the Hamming distance up to antipodal complement.

*Proof.* Condition on \([u]\) lying on \(P\), and cyclically slide the root to \(u\) in the projective Petrie cycle. The resulting ordered direction list is uniform in \(S_n\). The orbit \([v]\) appears among the proper prefixes if and only if the difference support \(A=\operatorname{supp}(u\oplus v)\), of size \(d\), or its complement \(A^c\), appears as a prefix. These two disjoint events have probability \(1/\binom nd\) each. The unconditioned number of rooted full geodesics hitting \([u]\) is \(2nn!\), established in (VA2), proving (JI1). \(\square\)

**Theorem (three-vertex laminarity criterion).** Let \([u],[v],[w]\) be three distinct projective vertex pairs. Set
\[
A=\operatorname{supp}(u\oplus v),\quad B=\operatorname{supp}(u\oplus w).
\]
There is a full antipodal geodesic containing all three projective vertex pairs if and only if
\[
\boxed{
A\cap B=\varnothing\ \text{or}\ A\setminus B=\varnothing\
\text{or}\ B\setminus A=\varnothing\
\text{or}\ [n]\setminus(A\cup B)=\varnothing.
}\tag{JI2}
\]
Equivalently, writing \(a=d_H(u,v),b=d_H(u,w),d=d_H(v,w)\), the criterion is that at least one equality holds:
\[
\boxed{a+b=d,\quad a+d=b,\quad b+d=a,\quad a+b+d=2n.}\tag{JI3}
\]
Both formulations are invariant under replacing any representative by its antipode.

For a quantitative version, define \(T_n(A,B)\) as the sum, over all \(X\in\{A,A^c\}\) and \(Y\in\{B,B^c\}\), of
\[
\mathbf1_{X\subsetneq Y}|X|!(|Y|-|X|)!(n-|Y|)!
+\mathbf1_{Y\subsetneq X}|Y|!(|X|-|Y|)!(n-|X|)!.
\tag{JI4}
\]
Then
\[
\boxed{
\#\{P:[u],[v],[w]\subseteq\mathcal V(P)\}=2n\,T_n(A,B).
}\tag{JI5}
\]
In particular this number is zero precisely when (JI2) fails.

*Proof.* Anchor a uniform Petrie direction ordering at \([u]\). The orbit \([v]\) can appear as a prefix only through either \(A\) or \(A^c\), and \([w]\) only through \(B\) or \(B^c\). Two distinct proper prefixes of one direction permutation are nested. Thus both orbits can occur if and only if one choice from each complementary pair is properly contained in the other. Expanding the four choices shows this is equivalent to one of the four Venn regions in (JI2) being empty. Their cardinalities are
\[
|A\cap B|=(a+b-d)/2,\quad
|A\setminus B|=(a+d-b)/2,\quad
|B\setminus A|=(b+d-a)/2,\quad
|[n]\setminus(A\cup B)|=n-(a+b+d)/2,
\]
proving (JI3). For nested \(X\subsetneq Y\), the permutation must first list precisely the \(|X|\) directions of \(X\), then those of \(Y\setminus X\), then the complement of \(Y\), in arbitrary internal orders. This gives the first factorial term in (JI4), and similarly for reversed nesting. The listed cases are mutually exclusive for a given permutation: no permutation has both a set and its nonempty proper complement as prefixes. Therefore \(T_n(A,B)\) counts anchored permutations. There are \(2nn!\) rooted full geodesics through \([u]\), so each anchored permutation represents \(2n\) such rooted geodesics and (JI5) follows. \(\square\)

**Theorem (color-independent gauge transfer for any projective path event).** Let \(\mathcal E\) be any collection of full geodesics defined solely through their projective vertex-orbit sets \(\mathcal V(P)\). For every legal coloring \(c\), uniformly random invariant vertex gauge \(h\), and \(Z_{\mathcal E}(c+\delta h)\) the number of full *zero-colored* geodesics in \(\mathcal E\),
\[
\boxed{\mathbb E_h Z_{\mathcal E}(c+\delta h)=\frac{|\mathcal E|}{2^n}.}\tag{JI6}
\]
In particular, for a fixed specified pair \([u],[v]\),
\[
\boxed{
\mathbb E_h Z_{\{[u],[v]\text{ both visited}\}}
=\frac{n\,n!}{2^{n-2}\binom nd}.
}\tag{JI7}
\]
For a fixed triple the expectation is \(nT_n(A,B)/2^{n-1}\).

*Proof.* The root-slide map from (VA3) cyclically permutes the visited projective vertex pairs and complements the color of one edge, thereby reversing the total color parity while preserving membership in \(\mathcal E\). Thus precisely half the uncolored paths in \(\mathcal E\) have even edge-color parity, for every legal \(c\). Invariant vertex gauges make each such path all zero with probability \(2^{-(n-1)}\), as in (GA2), and never make an odd-parity path all zero. Summing gives (JI6). Substitution of (JI1) and (JI5) gives the special cases. \(\square\)

**Geometric obstruction to triple-star overlap.** For example, in \(Q_4\), the projective pairs \([0000],[1100],[1010]\) have the three Hamming distances \(2,2,2\). None of (JI3) holds (their sum is six, not eight), so *no full antipodal geodesic whatsoever* visits all three pairs. Consequently any simultaneous gauge flip supported on three projective vertices satisfying the non-laminar condition can affect at most two stars on any one projective Petrie cycle, changing its grade by at most four. This applies regardless of the number or arrangement of other Petrie cycles, and provides a explicit constraint on how local repairs can overlap.

**Verification.** Independent enumeration of all rooted full cube paths in dimensions \(n=2,\ldots,6\) gives the pair counts \(4nn!/\binom nd\); exhaustive anchored-permutation checks of every three-distinct-orbit configuration in dimensions \(3,\ldots,6\) give (JI4)--(JI5). The proofs do not depend on the finite checks.


## Strand matching measures the distance to a successful vertex gauge

The two-step derivative (GS1) permits a complete optimization over star flips on a chosen projective Petrie cycle. This also separates low completed grade from a short gauge repair.

Fix a legal coloring \(c\) on \(Q_n\), \(n\ge3\), and a projective Petrie cycle \(C\). Put
\[
D_C=\{j:\delta_j(C)=1\}.
\]
Let \(S_C\) be the graph on turn positions with one edge \(\{j,j+2\}\) for each \(j\), indices taken modulo \(n\). Its edges correspond to the individual stars in (GS1), after a cyclic index shift. It has one strand when \(n\) is odd and two when \(n\) is even. When a strand has length two, retain its two parallel edges. Let \(d_S\) denote shortest-path distance within a strand.

Since \(|D_C|\) is odd, precisely one strand contains an odd number of its defects. Define \(\mu_C\) as follows. Leave one defect unpaired in that odd strand; pair all remaining defects within their respective strands; and minimize the sum of the pair distances \(d_S\), allowing all choices of the unpaired defect and pairing.

**Theorem (strand matching formula).** The minimum number of distinct antipodal vertex stars whose combined flip makes \(C\) have grade one is
\[
\boxed{\mu_C.}\tag{GM1}
\]
There is an optimal repair using no star outside \(C\). If \(\rho(c)\) is the minimum number of antipodal vertex stars whose combined flip produces any coloring with a monochromatic full antipodal geodesic, then
\[
\boxed{\rho(c)=\min_C\mu_C.}\tag{GM2}
\]

*Proof.* By (GS1), choosing a set of stars is choosing an edge set \(H\) of \(S_C\), and its effect on the turn word is the odd-degree boundary \(\partial H\). A singleton target at position \(z\) therefore requires
\[
\partial H=D_C\mathbin{\triangle}\{z\}.
\]
The strand parities force \(z\) into the odd strand.

A minimum such edge set has no cycle: deleting an entire cycle preserves its boundary and reduces its size. Its components are consequently edge-disjoint paths pairing the boundary positions. If \(z\notin D_C\), the path ending at \(z\) has another endpoint \(u\in D_C\). Delete that path. The remaining edge set repairs to the singleton \(u\), with no larger cost. Thus an optimal singleton may be taken in \(D_C\). Its remaining path components pair all other original defects within strands. Their total length is at least the corresponding sum of shortest strand distances, proving the lower bound in (GM1).

Conversely, take a minimizing pairing in the definition of \(\mu_C\), choose a shortest strand path for each pair, and take the symmetric difference of their edge sets. Its boundary is all defects except the unpaired one, and its edge count is at most the sum of the path lengths. This gives the upper bound, hence equality.

Stars outside the \(n\) projective vertices of \(C\) do not affect it. Finally a coloring is successful precisely when at least one projective Petrie cycle has grade one: root sliding at its unique turn produces a monochromatic full geodesic. Any successful global gauge therefore repairs some \(C\), while a minimizing repair of any \(C\) is a legal global gauge. This proves (GM2). \(\square\)

**Corollary (sharp radius for a grade-three cycle).** If \(g(C)=3\), then
\[
\boxed{\mu_C\le
\begin{cases}
\lfloor n/3\rfloor,&n\text{ odd},\\
\lfloor n/4\rfloor,&n\text{ even}.
\end{cases}}\tag{GM3}
\]
Both bounds are attained by turn words of legal colorings on a chosen cycle.

*Proof.* For odd \(n\), the three defects lie on one length-\(n\) strand; leave one unpaired and join the closest pair. The smallest of their three cyclic gaps is at most \(\lfloor n/3\rfloor\), with equality for three as evenly spaced as possible positions.

For even \(n=2m\), either all three defects lie in one strand, giving a closest-pair bound \(\lfloor m/3\rfloor\), or two lie in the even-parity strand and one in the odd-parity strand. In the latter case (GM1) is the distance between the forced pair, at most \(\lfloor m/2\rfloor=\lfloor n/4\rfloor\). Choose that pair at maximum distance to attain the bound. Every odd turn word on \(C\) is realized by assigning its distinct projective edge-orbit colors and completing the other orbits legally, as in the preceding sharp-radius theorem. These sharpness assertions concern repair of the chosen cycle; other cycles may already be successful. \(\square\)

**Theorem (profile obstruction to a short global gauge repair).** Let
\[
r(c)=\min_P\#\{\text{one-colored edges of }P\},
\]
where \(P\) ranges over full antipodal geodesics of \(c\). Then
\[
\boxed{\rho(c)\ge\lceil r(c)/2\rceil.}\tag{GM4}
\]
For independent odd factors \(c_1,\ldots,c_h\),
\[
\boxed{\rho(c_1\boxtimes\cdots\boxtimes c_h)
\ge\left\lceil\frac12\sum_{a=1}^h r(c_a)\right\rceil.}\tag{GM5}
\]

*Proof.* Suppose a gauge supported on \(k\) antipodal vertex pairs makes a full geodesic monochromatic. Translate that geodesic antipodally if necessary, so its final color is zero. Each selected star meets its \(n\) projective edge orbits in at most two edges, including the first and last edges when the star is its antipodal endpoint pair. Before the gauge there were consequently at most \(2k\) one-colored edges on this path. Thus \(r(c)\le2k\), giving (GM4).

For a product coloring, projecting a full geodesic to each factor gives a full factor geodesic; the total number of one-colored edges is the sum of the factor counts. Conversely any choices of factor full geodesics can be interleaved, retaining those counts. Hence \(r(c_1\boxtimes\cdots\boxtimes c_h)=\sum_a r(c_a)\). Apply (GM4). \(\square\)

**Implication for closure.** The first-excess and balance reductions of Article XV imply that any failure of NORI1 yields a balanced bad \(c\) having a grade-three full geodesic. The frontier tensorization theorem gives
\[
\gamma(c^{\boxtimes h})=3,\qquad
\rho(c^{\boxtimes h})\ge\lceil h r(c)/2\rceil\ge\lceil h/2\rceil.
\tag{GM6}
\]
Thus, conditionally on any counterexample, the least global gauge repair distance grows linearly in Cartesian powers while the least geodesic grade stays three. A bound on repair cost depending only on the number of turns would already require global NORI1 content. In contrast, a uniform sublinear bound \(\rho(c)=o(n)\), restricted to balanced colorings with \(\gamma(c)\le3\), would close the full conjecture by (GM6). Such a bound remains open.

The matching formula was independently checked against shortest-path search on the full turn-word star-action graph for every odd turn word in dimensions \(3\) through \(11\). The observed maximum repair cost among grade-three words was respectively \(1,1,1,1,2,2,3,2,3\), in agreement with (GM3). These checks are separate from the dimension-uniform proofs.

The monotone transport construction (GS5) remains valid. Formula (GM1) supplies its optimal cost and (GM6) explains why a bound on that cost cannot be inferred from low grade alone. The remaining problem is to find a successful cycle in the original coloring, or to prove a sublinear quantitative repair bound using compatibility across cycles.



## Simultaneous cycle repair: an affine overlap syndrome and a balanced incompatibility certificate

The sharp individual-cycle star matching formula (GM1) does not establish that arbitrary chosen cycles can be repaired by the *same* invariant vertex gauge. Here is a complete linear-algebra test for any fixed pair, and an explicit obstruction already present in a balanced affine four-cube.

For each projective Petrie cycle \(C\), let \(V_C\) be its \(n\) projective vertex pairs, and let
\[
\partial_{2,C}:\mathbb F_2^{V_C}\to\mathbb F_2^n,\qquad
(\partial_{2,C}h)_j=h(v_j)+h(v_{j+2})
\]
be the two-step derivative (GS1). Let \(\delta_C\) be its odd turn word, and put
\[
J_C=\{j:\delta_C+e_j\in\operatorname{im}\partial_{2,C}\}.
\]
Thus \(J_C=[n]\) for odd \(n\), and \(J_C\) is the unique odd-parity turn strand for even \(n\). For \(j\in J_C\), choose any particular solution \(h_C^{(j)}\) of
\(\partial_{2,C}h=\delta_C+e_j\). Let \(K_C=\ker\partial_{2,C}\), consisting of functions constant on each step-two parity strand (one strand in odd dimension, two in even).

**Theorem (two-cycle gauge compatibility).** Two prescribed projective Petrie cycles \(C,D\) can simultaneously attain grade one under a single globally legal invariant vertex gauge if and only if there exist \(j\in J_C\), \(k\in J_D\), \(a\in K_C\), and \(b\in K_D\) such that
\[
\boxed{
(h_C^{(j)}+a)|_{V_C\cap V_D}
=(h_D^{(k)}+b)|_{V_C\cap V_D}.
}\tag{SC1}
\]
For every fixed pair \(j,k\), this is an ordinary affine linear system on at most four phase bits and the overlapping vertices. Consequently pairwise simultaneous repair can be decided by at most \(n^2\) small binary linear systems, without enumerating global colorings or gauges.

In particular, cycles with at most one common projective vertex pair are always simultaneously repairable. In even dimension, two cycles with precisely two shared projective vertex pairs are simultaneously repairable whenever those vertices belong to opposite step-two parity strands of **at least one** of the two cycles.

*Proof.* A local gauge repairs \(C\) to grade one precisely when its turn word becomes \(e_j\) for some \(j\in J_C\). By (GS1), all local solutions form the affine cosets \(h_C^{(j)}+K_C\). Similarly for \(D\). A pair of local assignments extends to a single global antipodally invariant vertex gauge if and only if they agree on the common vertex pairs, establishing (SC1). When the overlap has size at most one, the constant function in \(K_C\) can adjust a single required bit to agree with any selected repairing assignment for \(D\). When \(n\) is even and the two shared vertices lie on opposite strands of \(C\), the two independent strand constants in \(K_C\) allow arbitrary adjustment of both values without affecting the repaired turn word; the same argument works with \(C,D\) exchanged. \(\square\)

**Even-strand rigidity.** For even \(n=2m\), let \(E_C\subset V_C\) denote the strand whose turn defect sum is even. Every gauge making \(g(C)=1\) must annihilate every turn defect on \(E_C\), so
\[
\boxed{h(v_j)+h(v_{j+2})=\delta_j(C)\qquad(j\in E_C).}\tag{SC2}
\]
For any \(u,v\in E_C\), this forces a unique relative gauge bit
\[
\boxed{
h(u)+h(v)=\sigma_C(u,v):=
\sum_{j\text{ along either step-two arc }u\to v\text{ in }E_C}\delta_j(C).
}\tag{SC3}
\]
The two arc sums agree because the total defect parity on \(E_C\) is even. Consequently, if two cycles \(C,D\) share \(u,v\in E_C\cap E_D\) but \(\sigma_C(u,v)\ne\sigma_D(u,v)\), their simultaneous grade-one repair is impossible, regardless of choices on the odd strands.

**Balanced affine \(Q_4\) certificate.** Take the vertex-balanced antipodally odd coloring
\[
c_0(x)=x_2,\quad c_1(x)=1+x_2,\quad
c_2(x)=x_0,\quad c_3(x)=1+x_0\pmod2.
\tag{SC4}
\]
Consider the two full cube geodesics rooted at \(0000\) with direction orders
\[
C:\ (0,3,1,2),\qquad D:\ (1,2,0,3).
\tag{SC5}
\]
Their projective vertex sequences, represented by minimum binary integers in each antipodal pair, are
\[
C:\ (0,1,6,4),\qquad D:\ (0,2,6,7);
\]
their underlying directional edge-color words and twisted cyclic turn words are
\[
b_C=(0,0,1,1),\qquad \delta_C=(0,1,0,0),
\]
\[
b_D=(1,0,1,0),\qquad \delta_D=(1,1,1,0).
\tag{SC6}
\]
Both have the **even-turn-parity strand at positions \(0,2\)**, corresponding to the same two shared projective vertices \([0000]\) and \([0110]\). Equation (SC2) forces
\[
\boxed{g(C^{h})=1\Longrightarrow h(0)+h(6)=0,\qquad
g(D^{h})=1\Longrightarrow h(0)+h(6)=1.}\tag{SC7}
\]
Therefore no legal invariant vertex gauge makes both of these cycles grade one, although each is individually repairable, and the coloring itself already has monochromatic antipodal geodesics.

The incompatibility was independently checked by enumerating all \(2^8\) invariant vertex gauges on \(Q_4\). It disproves a potential global-closure route based on the assumption that any two cycles can always be jointly repaired. The overlap syndrome (SC1) instead isolates explicit conflicting affine constraints that any higher-order compatibility argument must handle.



## Second-moment theorem: almost every coloring in every vertex-gauge orbit is successful

Fix \(n\ge3\) and any legal antipodally odd coloring \(c\). Sample an invariant vertex gauge \(h:Q_n/\tau\to\mathbb F_2\) uniformly, write \(N=2^{n-1}\) for the number of projective vertices, and put
\[
X(h)=N_1(c+\delta h)
=\sum_{C\in\mathscr C_n}\mathbf1_{\{g(C;c+\delta h)=1\}},
\]
where \(|\mathscr C_n|=M=2^{n-2}(n-1)!\). By (GS3)--(GS4), each cycle is repaired with probability \(p=n/2^{n-1}\), independently of \(c\), and
\(\mathbb E_h X=Mp=n!/2\).

**Theorem (universal gauge-orbit abundance).** Define
\[
\boxed{
\varepsilon_n=\frac{n}{2^{n-1}}
\sum_{r=2}^{n}\frac{2^{r-1}(n-r+1)}{r!}
\ \le\ \frac{(e^2-3)n^2}{2^n}.
}\tag{SM1}
\]
Then for every legal coloring \(c\),
\[
\boxed{
\frac{\operatorname{Var}_h X}{(\mathbb E_hX)^2}\le\varepsilon_n,
\qquad
\Pr_h\bigl(c+\delta h\text{ has a monochromatic full antipodal geodesic}\bigr)
\ge\frac{1}{1+\varepsilon_n}.
}\tag{SM2}
\]
In particular, the fraction of **bad** colorings inside every invariant vertex-gauge orbit is at most \(\varepsilon_n/(1+\varepsilon_n)=O(n^2 2^{-n})\). This is a dimension-uniform bound valid even if the unrestricted NORI1 conjecture is false. The entire distribution is within the orbit of the starting coloring and the bound requires no balance assumption.

*Proof, part I: dependence occurs only through shared projective vertices.* For cycles \(C,D\), write \(K=|V_C\cap V_D|\), and \(I_C(h)=\mathbf1_{\{g(C;c+\delta h)=1\}}\). The event \(I_C=1\) depends only on the \(n\) independent gauge bits on \(V_C\), and similarly for \(D\). If \(K=0\), these indicators are independent.

For \(K\ge1\), condition on the \(K\) shared gauge bits \(s\in\mathbb F_2^K\), and set
\(f_C(s)=\Pr(I_C=1\mid s)\), \(f_D(s)=\Pr(I_D=1\mid s)\).
All other gauge bits used by \(C,D\) are disjoint, so these two events are independent given \(s\), and
\[
\mathbb E I_CI_D=2^{-K}\sum_sf_C(s)f_D(s).
\]
Complementing **all** gauge bits on \(V_C\) leaves its edge-coboundary, hence its grade-one event, unchanged. This maps shared assignment \(s\) to \(s+\mathbf1\), so \(f_C(s)=f_C(s+\mathbf1)\). Since \(2^{-K}\sum_sf_C(s)=p\), we have
\[
0\le f_C(s)\le 2^{K-1}p
\qquad(K\ge1).
\]
Consequently
\[
\mathbb E I_CI_D\le 2^{K-1}p^2,\qquad
\operatorname{Cov}(I_C,I_D)\le(2^{K-1}-1)p^2.
\]
For \(K=1\), this forces \(f_C(s)=p\) identically and hence zero covariance; thus any two cycles sharing at most **one** projective vertex pair have *independent grade-one events* under a random invariant gauge. For \(K\ge2\), use
\[
2^{K-1}-1\le 2^K-1-K=\sum_{r=2}^K\binom Kr.
\]
Hence for every ordered cycle pair, including \(K=0,1\),
\[
\boxed{
\operatorname{Cov}(I_C,I_D)\le
p^2\sum_{r=2}^K\binom Kr.
}\tag{SM3}
\]

*Proof, part II: sparse cycle intersections.* Fix \(C\), and choose another projective Petrie cycle \(D\) uniformly. For any specified nonempty set \(S\subseteq V_C\) of \(r\) projective vertices, \(1\le r\le n\), anchor \(u\in S\). The probability \(D\) contains \(u\) is \(n/N\). Conditional on this, slide its root to \(u\) and orient it uniformly; its list of \(n\) directions is a uniform permutation.

For each of the other \(r-1\) projective vertices in \(S\), membership in \(D\) requires that either its difference-bit set from \(u\), or its complement, occur among the proper prefixes of the permutation. There are at most \(2^{r-1}\) choices of those representatives. The chosen proper prefixes must be strictly nested, giving \(r\) positive direction blocks of sizes \(d_1,\ldots,d_r\) with total \(n\). For any fixed nested choice, the number of permitted permutations is \(\prod_{i=1}^r d_i!\), which is at most \((n-r+1)!\) by factorial log-convexity. Therefore
\[
\boxed{
\Pr(S\subseteq V_D)\le
\frac nN\,2^{r-1}\frac{(n-r+1)!}{n!}.
}\tag{SM4}
\]
Write \(K=|V_C\cap V_D|\). Using
\(\sum_{r=2}^{K}\binom Kr
=\sum_{S\subseteq V_C,\,|S|\ge2}\mathbf1_{\{S\subseteq V_D\}}\),
then (SM4), gives
\[
\begin{aligned}
\mathbb E_D\sum_{r=2}^{K}\binom Kr
&\le\frac nN\sum_{r=2}^n
\binom nr\,2^{r-1}\frac{(n-r+1)!}{n!}\\
&=\frac nN\sum_{r=2}^n\frac{2^{r-1}(n-r+1)}{r!}
=\varepsilon_n.
\end{aligned}\tag{SM5}
\]
The upper bound is independent of \(C\). Since \(n-r+1\le n\) and
\(\sum_{r=2}^\infty2^{r-1}/r!=(e^2-3)/2\),
(SM1) follows.

*Proof, part III: second moment and success density.* Sum (SM3) over all \(M^2\) ordered cycle pairs. Bound the cycle-intersection average by (SM5):
\[
\operatorname{Var}_h X
\le M^2p^2\varepsilon_n
=(\mathbb E_hX)^2\varepsilon_n.
\]
By Cauchy--Schwarz,
\[
\Pr(X>0)\ge\frac{(\mathbb EX)^2}{\mathbb E X^2}
\ge\frac1{1+\varepsilon_n}.
\]
A grade-one projective Petrie cycle is precisely a monochromatic full antipodal geodesic witness. This proves (SM2). \(\square\)

**Quantitative instances.** Direct evaluation of the finite sum (SM1) gives
\[
\begin{array}{c|c|c}
n&\varepsilon_n&\Pr_h(\text{successful})\text{ lower bound}\\
10&0.346695&0.74256\\
12&0.129726&0.88517\\
16&0.015097&0.98512\\
20&0.001515&0.99848\\
24&0.000139&0.99986
\end{array}
\tag{SM6}
\]
where the displayed lower bounds are rounded down for safety.

**Independent checks.** Exhaustive enumeration of the projective cycle vertex sets in \(Q_3,Q_4,Q_5,Q_6\) confirms the shared-vertex intersection counts and the bound (SM5). Separate enumeration of all \(2^n\) local gauge assignments on a fixed cycle for \(n=3,\ldots,9\) verifies its universal grade-one probability \(p=n/2^{n-1}\). These checks are not used in the proof.

**Implication for NORI1.** Any counterexample is forced into an exponentially vanishing exceptional subset of its vertex-gauge orbit, even when its square curvature and projective cohomology class are held fixed. This is markedly stronger than the earlier elementary \(2^{-(n-1)}\) *lower* bound on the good fraction. It does **not** yet rule out a single bad coloring: a gauge orbit has \(2^{2^{n-1}-1}\) members, so an \(O(n^2/2^n)\) exceptional fraction may still contain many colorings. A complete proof requires an integrality, connectivity, or cross-cycle argument upgrading the overwhelmingly typical success to success at every gauge.



### Precise cycle-intersection exponential moment and exponentially sharper bad-orbit density

The second-moment estimate (SM2) can be strengthened by exploiting the special *prefix-chain* geometry of two intersecting Petrie cycles, instead of the coarse bound (SM4) for an arbitrary projective vertex subset.

For positive integers \(n,k\), define
\[
A_{n,k}=\frac1{n!}
\sum_{\substack{d_1+\cdots+d_k=n\\d_i\ge1}}\prod_{i=1}^k d_i!,
\qquad
B_n=\sum_{k=1}^n A_{n,k},\qquad
\boxed{
\theta_n=\frac{2n^2}{2^{n-1}}\sum_{k=2}^n\frac{A_{n,k}}{k}.
}\tag{CM1}
\]
Here \(A_{n,k}\) is a finite weighted sum over compositions into \(k\) positive parts. The numbers \(B_n\) have the recurrence
\[
\boxed{B_0=1,\qquad
B_n=1+\sum_{j=1}^{n-1}\frac{B_{n-j}}{\binom nj}\quad(n\ge1).}\tag{CM2}
\]

**Theorem (joint-cycle exponential-intersection law).** If \(C,D\) are independent uniform projective Petrie cycles in \(Q_n\), and \(K=|V_C\cap V_D|\), then
\[
\boxed{
\mathbb E_{C,D}\bigl(2^K-1-K\bigr)
=\theta_n
\le\frac{16n}{2^n}.
}\tag{CM3}
\]
Consequently, for **every** legal antipodally odd coloring \(c\) of \(Q_n\), and uniformly random invariant vertex gauge \(h\),
\[
\boxed{
\frac{\operatorname{Var}_hN_1(c+\delta h)}
{(\mathbb E_hN_1)^2}\le\theta_n,\qquad
\Pr_h\bigl(N_1(c+\delta h)>0\bigr)\ge\frac1{1+\theta_n}.
}\tag{CM4}
\]
The bad fraction within every gauge orbit is therefore at most \(\theta_n/(1+\theta_n)=O(n\,2^{-n})\), an exponential-factor-\(n\) improvement over (SM2). The refined bound holds without balance or any restriction on square curvature.

*Proof, permutation-prefix calculation.* Fix \(C\) and a projective vertex \(u\in V_C\). Conditional on a uniform second cycle \(D\) visiting \(u\), anchor both cycles at \(u\) and orient \(C\) along the standard direction order \((1,\ldots,n)\). The anchored direction order of \(D\) is a uniform permutation \(\pi\). Let \(Z=|V_C\cap V_D|-1\), the number of additional common projective vertices. A noninitial vertex of \(C\) corresponds to a proper prefix set \([d]\), \(1\le d<n\), modulo complement. It appears on \(D\) if and only if the first \(d\) entries of \(\pi\) form \([d]\) (a *forward common cut*), or the first \(n-d\) entries form \([n]\setminus[d]\) (a *reverse common cut*).

No permutation has both a forward and a reverse common cut: the two required sets \([d]\) and \([n]\setminus[e]\) are nonempty proper subsets neither containing the other, whereas two prefixes of one permutation must be nested. Let \(U\) count forward cuts and \(V\) reverse cuts. Therefore \(Z=U+V\), but \(UV=0\). The two cut-count distributions are identical by reversing the direction labels, whence
\[
\mathbb E_\pi\bigl((1+t)^Z-1\bigr)
=2\left(\mathbb E_\pi(1+t)^U-1\right).
\]
For a prescribed set of \(k-1\) forward cuts \(0<d_1<\cdots<d_{k-1}<n\), the \(k\) consecutive block lengths \(a_1,\ldots,a_k>0\) sum to \(n\). The number of permutations respecting those cuts is \(\prod_i a_i!\). Expanding \((1+t)^U\) by subsets of cuts thus yields
\[
\boxed{
\mathbb E_\pi\bigl((1+t)^Z-1\bigr)
=2\sum_{k=2}^n A_{n,k}t^{k-1}.
}\tag{CM5}
\]

*Proof, anchored factorial moments.* Every projective Petrie cycle contains \(n\) projective vertices among \(N=2^{n-1}\); thus \(\Pr(u\in V_D)=n/N\). The identity, valid for every integer \(K\ge0\),
\[
2^K-1-K
=K\int_0^1((1+t)^{K-1}-1)\,dt
\]
is interpreted as zero at \(K=0\). Sum the RHS over the \(K\) possible anchors \(u\in V_C\cap V_D\). The conditional random variable \(K-1\) is \(Z\) from the preceding paragraph, independently of the chosen anchor. Therefore (CM5) gives
\[
\begin{aligned}
\mathbb E_D(2^K-1-K)
&=\frac{n^2}{N}\int_0^1
\mathbb E_\pi\bigl((1+t)^Z-1\bigr)\,dt\\
&=\frac{2n^2}{N}\sum_{k=2}^n\frac{A_{n,k}}{k}
=\theta_n,
\end{aligned}
\]
proving the equality in (CM3).

*Proof, elementary upper bound.* The sum \(B_n\) enumerates all positive compositions of \(n\) weighted by their block factorial products and divided by \(n!\). Splitting by the first block gives (CM2). We claim \(B_n\le2\) for every \(n\ge1\). Direct substitution verifies \(n\le7\). For \(n\ge8\), assuming the earlier bounds and using
\[
\sum_{j=1}^{n-1}\frac1{\binom nj}\le\frac4n\le\frac12,
\]
the recurrence yields \(B_n\le1+2(1/2)=2\), proving the claim inductively. (The reciprocal-binomial bound follows by treating the two endpoint terms \(1/n\) separately and bounding every other term by \(1/\binom n2\).)

It follows that
\[
\sum_{k=2}^n\frac{A_{n,k}}k
\le\frac{B_n-1}2
\le\sum_{j=1}^{n-1}\frac1{\binom nj}
\le\frac4n.
\]
Substitution into (CM1) proves
\(\theta_n\le (2n^2/N)(4/n)=8n/N=16n/2^n\).

*Proof, success probability.* The previous variance argument (SM3) shows that for two cycle grade-one indicators with projective vertex intersection size \(K\), their covariance is at most
\[
p^2(2^K-1-K),\qquad p=n/2^{n-1}.
\]
Average this inequality over ordered cycle pairs and use (CM3):
\[
\operatorname{Var}_hN_1(c+\delta h)
\le (Mp)^2\theta_n
=(\mathbb E_hN_1)^2\theta_n.
\]
Cauchy--Schwarz again gives \(\Pr(N_1>0)\ge1/(1+\theta_n)\). \(\square\)

**Examples and independent verification.** Recursively evaluating the composition sums gives
\[
\begin{array}{c|c|c}
n&\theta_n&\text{lower bound on good-gauge fraction}\\
10&0.064741&0.93919\\
12&0.017257&0.98303\\
16&0.001255&0.99874\\
20&0.000091745&0.999908\\
24&0.000006628&0.999993
\end{array}
\tag{CM6}
\]
with probability bounds rounded downward. Independent exhaustive enumeration of all projective Petrie cycle pairs in dimensions \(n=3,4,5,6\) gives the exponential-intersection moments \(1.75,\,1.708333\ldots,\,1.255208\ldots,\,0.783854\ldots\), matching (CM1) precisely.

**Closure significance and limitation.** This is a *uniform dimension-wide* statement: the complement of the successful-coloring set is at most \(O(n2^{-n})\) of **every** invariant vertex-gauge orbit, including every prescribed curvature fiber's individual gauge phase. The improvement uses valid multi-cycle prefix-chain geometry, not a marginal noise-trace sign assumption. The result does not exclude an isolated exceptional gauge, and hence does not by itself prove unrestricted NORI1. It suggests that any hypothetical bad coloring must exploit highly exceptional cross-cycle alignment beyond the pair-intersection structure captured in the second moment.



### Even-dimensional parity cancellation sharpens the gauge-orbit second moment by a factor of n

All statements here require even \(n\ge4\), precisely the dimensions sufficient for the established balanced reduction. In even dimension, antipodal vertices have the same bipartite parity, so the projective vertex set \(Q_n/\tau\) splits canonically into even and odd classes \(E,O\).

Let \(I_C(h)\) be the indicator that the twisted turn grade of a given projective Petrie cycle \(C\) becomes one after the invariant vertex gauge \(h\), and let \(p=\mathbb E_h I_C=n/2^{n-1}\).

**Theorem (parity-strand orthogonality).** The Boolean function \(I_C(h)\), viewed as a function of the \(n\) gauge bits along \(V_C\), is invariant under separately complementing all its even-vertex gauge bits and all its odd-vertex gauge bits. Its Walsh Fourier coefficient indexed by \(S\subseteq V_C\) therefore vanishes unless
\[
\boxed{|S\cap E|\equiv |S\cap O|\equiv0\pmod2.}\tag{PC1}
\]
If two distinct projective Petrie cycles \(C,D\) share at most two projective vertices, and any two shared vertices have opposite cube bipartite parity, then \(I_C,I_D\) are statistically independent under a uniform invariant gauge.

*Proof.* Every projective cycle edge runs between opposite cube bipartite parities. Complementing the gauge bits on one parity class inside \(V_C\) reverses every edge color along \(C\). This leaves all cyclic twisted turn bits, and hence their grade, unchanged. Separately complementing either parity class proves the two invariances. Walsh orthogonality proves (PC1). For two cycles sharing bits on a set \(R\), the conditional expectation of \(I_C\) given those bits has a nonconstant Walsh mode only on a nonempty \(S\subseteq R\) satisfying (PC1), and likewise for \(I_D\). When \(|R|\le2\) and any two shared vertices have opposite parity, no such \(S\) exists. Their conditional success probabilities are consequently constant \(p\), and the indicators are independent after averaging over the remaining disjoint gauge bits. \(\square\)

Let \(\theta_n\) be the previous positive composition sum (CM1). Define
\[
\boxed{
\theta^{\rm par}_n
=\theta_n-\frac{n^2}{2^{n-1}}
\sum_{\substack{1\le d<n\\d\ {\rm odd}}}\frac1{\binom nd}
=
\frac{n^2}{2^{n-1}}
\left[
\sum_{\substack{2\le d\le n-2\\d\ {\rm even}}}\frac1{\binom nd}
+
2\sum_{k=3}^n\frac{A_{n,k}}k
\right].
}\tag{PC2}
\]
The expression is visibly nonnegative.

**Theorem (parity-improved success abundance).** For every legal antipodally odd coloring \(c\) of \(Q_n\), \(n\) even,
\[
\boxed{
\frac{\operatorname{Var}_hN_1(c+\delta h)}
{(\mathbb E_h N_1)^2}
\le\theta_n^{\rm par},
\qquad
\Pr_h(N_1(c+\delta h)>0)\ge\frac1{1+\theta_n^{\rm par}}.
}\tag{PC3}
\]
Furthermore,
\[
\boxed{\theta_n^{\rm par}\le\frac{72}{2^n}
\quad\text{for every even }n\ge4.}\tag{PC4}
\]
Thus the fraction of unsuccessful colorings in every invariant vertex-gauge orbit of an even-dimensional legal cube is \(O(2^{-n})\), improving the earlier \(O(n2^{-n})\) bound by an additional factor of \(n\).

*Proof.* For projective cycles \(C,D\), let \(R=V_C\cap V_D\), \(K=|R|\), \(K_E=|R\cap E|\), and \(K_O=|R\cap O|\). Condition on the \(K\) shared independent gauge bits. The cycle indicators are conditionally independent, and both conditional success probabilities have mean \(p\). Expand them in Walsh characters on the shared bits. By (PC1), only nonempty subsets \(S\subseteq R\) with even cardinality in **each** parity class can contribute to their covariance. Each conditional Walsh coefficient has absolute value at most \(p\), because its conditional probability function is nonnegative and averages to \(p\). In particular,
\[
\boxed{
\operatorname{Cov}_h(I_C,I_D)
\le p^2\bigl(2^K-1-K-K_EK_O\bigr).
}\tag{PC5}
\]
The bracket counts a superset of the permissible nonempty Fourier index sets: from all subsets of size at least two it discards the \(K_EK_O\) mixed-parity pairs, which are prohibited by (PC1).

Fix \(C\), choose \(D\) uniformly, and count its common opposite-parity vertex pairs with \(C\). For any two projective vertices \([u]\ne[v]\) at distance \(d=d_H(u,v)\), the prior precise pair-incidence formula (JI1) gives
\[
\Pr_D(\{[u],[v]\}\subseteq V_D)=\frac n{2^{n-1}}\frac2{\binom nd}.
\]
Along the fixed projective Petrie cycle, two vertices have opposite bipartite parity precisely when their cyclic separation \(d\) is odd. Summing over all unordered mixed-parity pairs, with each such pair represented twice as an ordered offset along the cycle, yields
\[
\boxed{\mathbb E_D(K_EK_O)
=\frac{n^2}{2^{n-1}}
\sum_{\substack{1\le d<n\\d\ {\rm odd}}}\frac1{\binom nd}.}\tag{PC6}
\]
The earlier precise intersection identity (CM3) gives
\(\mathbb E_D(2^K-1-K)=\theta_n\).
Subtract (PC6) and sum (PC5) over all ordered cycles to bound the variance by \((Mp)^2\theta_n^{\rm par}\). Cauchy--Schwarz proves (PC3). Splitting the \(k=2\) term of the composition sum into odd and even \(d\) gives (PC2).

For the elementary numerical bound, the reciprocal-binomial inequality used in (CM3) and its recurrence imply \(B_j-1\le8/j\) for all \(j\ge1\). Consequently
\[
\sum_{k=3}^n A_{n,k}
=\sum_{j=1}^{n-2}\frac{B_{n-j}-1}{\binom nj}
\le\frac8n\sum_{j=1}^{n-2}\frac1{\binom{n-1}{j}}
\le\frac{32}{n(n-1)}.
\]
For \(n\ge6\),
\[
\sum_{\substack{2\le d\le n-2\\d\ {\rm even}}}
\frac1{\binom nd}
\le\frac4{n(n-1)}
+\frac{6(n-5)}{n(n-1)(n-2)}
\le\frac{10}{n(n-1)}.
\]
It follows that
\[
\theta_n^{\rm par}
\le\frac{n^2}{2^{n-1}}
\left(\frac{10}{n(n-1)}+\frac{64}{3n(n-1)}\right)
=\frac{94n}{3(n-1)\,2^{n-1}}
\le\frac{72}{2^n}
\]
for \(n\ge8\). Direct substitution into (PC2) verifies the same inequality for \(n=4,6\). This proves (PC4). \(\square\)

**Numerical comparison from the finite composition sum.**
\[
\begin{array}{c|c|c}
n&\theta_n^{\rm par}&\Pr_h(\text{successful})\text{ lower bound}\\
8&0.09633247&0.91213\\
10&0.02164784&0.97881\\
12&0.00472130&0.99530\\
16&0.000244740&0.999755\\
20&0.0000139852&0.9999860\\
24&0.000000833798&0.99999916
\end{array}\tag{PC7}
\]

The new effect is cubical and uses the antipodal quotient's **even-dimensional bipartition**. Pairs of cycles overlapping on just one even and one odd projective vertex contribute zero covariance, removing the leading term of the previous second-moment estimate. The remaining variance is supported by same-parity overlap pairs and higher-order intersections. The theorem does not exclude isolated bad gauges, but makes their permitted density exponentially smaller in precisely the dimension parity relevant to unrestricted NORI1.



### Precise signed pair-covariance law for cycle repairs

For a projective Petrie cycle \(C\), write \(I_C(h)=\mathbf1_{\{g(C;c+\delta h)=1\}}\). Its success probability under uniform invariant vertex gauges is \(p=n/2^{n-1}\), independent of \(c,C\). Given two distinct projective vertex pairs \(u,v\in V_C\), define its *pair repair correlation*
\[
\boxed{\mu_C(u,v)=\mathbb E_h[(-1)^{h(u)+h(v)}\mid I_C(h)=1].}\tag{RC1}
\]

**Theorem (pair repair correlation).** Retain the two-step turn-coboundary model \(\delta_j\mapsto\delta_j+h_j+h_{j+2}\) from (GS1).

1. If \(n\) is odd, all \(n\) positions form one odd-defect strand. Choose either arc \(A\) along its step-two cycle from \(u\) to \(v\), containing \(d\) strand edges. Then
   \[
   \boxed{\mu_C(u,v)=(-1)^{\sum_{j\in A}\delta_j}\left(1-\frac{2d}{n}\right).}\tag{RC2}
   \]
2. If \(n=2m\) is even and \(u,v\) lie in different parity strands, then
   \[
   \boxed{\mu_C(u,v)=0.}\tag{RC3}
   \]
3. If \(n=2m\) is even and \(u,v\) lie in the same strand, choose a step-two arc \(A\) of length \(d\). If that strand has **even** turn-defect parity, then
   \[
   \boxed{\mu_C(u,v)=(-1)^{\sum_{j\in A}\delta_j}\in\{+1,-1\}.}\tag{RC4}
   \]
   If the strand has **odd** turn-defect parity, then
   \[
   \boxed{\mu_C(u,v)=(-1)^{\sum_{j\in A}\delta_j}\left(1-\frac{2d}{m}\right).}\tag{RC5}
   \]
All formulas are independent of the choice of arc: in an odd strand the complementary arc changes the sign of the defect sum and replaces \(d/L\) by \(1-d/L\), leaving the product unchanged; in an even strand both arc sums agree.

**Theorem (full covariance for a two-vertex overlap).** If two projective Petrie cycles \(C,D\) meet in precisely the two projective vertex pairs \(u,v\), then
\[
\boxed{
\Pr_h(I_C=I_D=1)=p^2(1+\mu_C(u,v)\mu_D(u,v)),
\quad
\operatorname{Cov}_h(I_C,I_D)=p^2\mu_C(u,v)\mu_D(u,v).
}\tag{RC6}
\]
Thus, for a two-vertex intersection, zero pair correlation in either cycle gives independent success events; opposite deterministic repair correlations \((+1,-1)\) give absolute incompatibility; and matching deterministic correlations give maximal positive covariance \(p^2\).

*Proof.* Under \(I_C=1\), the final turn vector on its unique odd-parity step-two strand is \(e_z\), where \(z\) ranges uniformly among the \(L\) positions of that strand. Indeed each choice of \(z\) permits the same number \(2^q\) of local gauge solutions, with \(q=\gcd(n,2)\). Every even-parity strand is forced to final turn word zero. Along a step-two arc \(A:u\to v\), summing
\(\delta_j+h_j+h_{j+2}=\delta'_j\)
telescopes to
\[
h(u)+h(v)=\sum_{j\in A}\delta_j+\sum_{j\in A}\delta'_j.
\]
On an even strand the second sum is zero. On the odd strand it equals \(\mathbf1_{\{z\in A\}}\), with \(z\) uniformly distributed, giving the factor \(1-2d/L\). For vertices on different strands, independently complementing all gauge bits on either strand preserves the event \(I_C=1\) while reversing the pair character, forcing correlation zero. This proves (RC2)--(RC5).

For (RC6), condition on the two shared independent gauge bits \(s=(h(u),h(v))\). Since each repair event is invariant under simultaneous complementation of its local gauge bits, its conditional success probability must be
\[
\Pr(I_C=1\mid s)
=p\left[1+\mu_C(u,v)(-1)^{s_u+s_v}\right]
\]
and similarly for \(D\). After conditioning on \(s\), their remaining gauge bits are disjoint, so the events are independent. Averaging the product of the two conditional probabilities over the four values of \(s\) proves (RC6). \(\square\)

**Reconciliation with the balanced four-cube obstruction.** In the two cycles of (SC4)--(SC7), the common vertices \(0000\) and \(0110\) lie on the even-turn-parity strand in both cycles. Their forced relative gauge bits differ, so (RC4) gives \(\mu_C=+1,\mu_D=-1\), and (RC6) recovers the impossibility of joint repair by an precise zero intersection probability. The parity cancellation theorem (PC1) is the opposite extreme, where shared vertices lie in different strands and the covariance vanishes.

**Research use.** The earlier second-moment estimates bound every nonzero pair overlap correlation by its maximal magnitude. Equations (RC2)--(RC6) expose the underlying signed correlation, including deterministic incompatibility and many additional zero-correlations. They are a starting point for color-sensitive variance improvements and higher-order repair-compatibility inequalities. They do not alone imply that every gauge is successful.



### Joint independence for parity-peelable families of Petrie cycles

The pairwise independence phenomenon (PC1) extends to valid multi-cycle independence. This provides a structural input for future higher-moment bounds; pairwise correlation control alone does not identify the potentially dependent clusters.

**Theorem (parity-peeling independence).** Fix even \(n\ge4\) and any legal antipodally odd coloring. Let \(\mathscr F\) be a finite collection of distinct projective Petrie cycles. Suppose its cycles can be removed in some order \(C_1,\ldots,C_r\) so that at the moment \(C_j\) is removed,
\[
\boxed{
\bigl|V_{C_j}\cap E\cap\bigcup_{i>j}V_{C_i}\bigr|\le1,
\qquad
\bigl|V_{C_j}\cap O\cap\bigcup_{i>j}V_{C_i}\bigr|\le1.
}\tag{PI1}
\]
Then, under a uniformly random invariant vertex gauge, the indicators \(\{I_C:C\in\mathscr F\}\) are **mutually independent** Bernoulli variables with common success probability \(p=n/2^{n-1}\). In particular,
\[
\boxed{
\Pr_h(I_C=1\text{ for every }C\in\mathscr F)=p^{|\mathscr F|},
\qquad
\Pr_h(I_C=0\text{ for every }C\in\mathscr F)=(1-p)^{|\mathscr F|}.
}\tag{PI2}
\]

The same theorem holds for odd \(n\) if the stronger peeling condition \(|V_{C_j}\cap\bigcup_{i>j}V_{C_i}|\le1\) is used.

*Proof.* For even \(n\), the conditional success probability of \(I_C\), given arbitrary fixed values of at most one gauge bit from \(E\cap V_C\) and one from \(O\cap V_C\), equals \(p\) by the separate parity-complement invariances proved in (PC1). Indeed these symmetries act transitively on the possible assignments to the selected bits while preserving the success event and the uniform distribution on the remaining local gauge bits.

At the first removal stage, \(I_{C_1}\) depends only on its \(n\) local gauge bits, and is conditionally Bernoulli(\(p\)) after all bits appearing in the remaining cycles have been revealed. It is therefore independent of every function of the remaining cycles' bits, in particular of their success indicators. Remove \(C_1\) and repeat. This proves mutual independence by induction. Every subfamily inherits the same peeling order, so independence applies to all joint success/failure patterns, proving (PI2).

For odd \(n\), complementing all local gauge bits on \(V_C\) preserves every cycle-edge color and hence the grade. Conditional success is thus unbiased with respect to any one revealed gauge bit, and the analogous induction applies. \(\square\)

**Higher-moment implication.** In an expansion of joint moments or cumulants of \(N_1(c+\delta h)=\sum_C I_C(h)\), any family satisfying (PI1) contributes as an independent family. Thus only **non-peelable clusters** can produce new connected dependencies. In even dimensions, a non-peelable collection contains a nonempty subcollection in which **every** cycle shares at least two projective vertices of one parity class with the union of the other cycles in that subcollection. This follows by iteratively deleting cycles with at most one shared vertex of each parity until no further deletion is possible. This is a combinatorial parity-core condition on the incidence hypergraph of projective Petrie cycles, and it sharpens the dependency structure beyond mere overlap of their vertex sets. The theorem does not itself bound all such cores or establish NORI1.



### Curved squares suppress the degree-two Fourier influence of a vertex-gauge pair

Fix an even dimension \(n=2m\ge6\) and an arbitrary legal antipodally odd cube-edge coloring \(c\); balance is not assumed. On the invariant vertex-gauge cube \(h:Q_n/\tau\to\mathbb F_2\), put
\[
X_c(h)=N_1(c+\delta h),\qquad
\widehat X_c(\{u,v\})=\mathbb E_h\bigl[X_c(h)(-1)^{h(u)+h(v)}\bigr].
\]
Here \(u,v\) denote projective vertex pairs. Its mean is \(\mathbb E_hX_c=n!/2\), by (GS4).

**Theorem (local square-curvature formula).** Fix \(x\in Q_n\) and two distinct directions \(i,j\). Let
\[
u=[x],\qquad v=[x\oplus e_i\oplus e_j],\qquad N=2^{n-1},
\]
\[
a=c_i(x)+c_j(x\oplus e_i),\quad
\kappa=c_i(x)+c_j(x\oplus e_i)+c_j(x)+c_i(x\oplus e_j)
\quad(\bmod2).
\]
For each permutation \(\sigma\) of the remaining \(n-2\) directions, let \(t_\sigma\) be the **sum modulo two of the edge colors along its directed length-\((n-2)\) path**, starting at \(x\oplus e_i\oplus e_j\). Define the signed suffix sum
\[
T_{x;ij}=\sum_{\sigma\in S_{[n]\setminus\{i,j\}}}(-1)^{t_\sigma}.
\]
Then the degree-two gauge Fourier coefficient is
\[
\boxed{
\widehat X_c(\{u,v\})
=\frac4N T_{x;ij}
+\frac{2(n-2)(n-2)!}{N}\,
\mathbf1_{\{\kappa=0\}}(-1)^a.
}\tag{SQF1}
\]
Thus on a *curved* square (\(\kappa=1\)),
\[
\boxed{|\widehat X_c(\{u,v\})|
\le\frac{4(n-2)!}{N},}\tag{SQF2}
\]
whereas on a *flat* square the general upper bound is
\[
\boxed{|\widehat X_c(\{u,v\})|
\le\frac{2n(n-2)!}{N}.}\tag{SQF3}
\]
A curved square therefore suppresses the maximum possible local pair influence by a factor \(n/2\), independently of the coloring's balance.

*Proof.* By the precise pair-incidence formula (JI1), cycles containing the two projective vertices \(u,v\) are in bijection, for \(n\ge6\), with rooted direction orders \((i,j,\sigma)\) and \((j,i,\sigma)\) starting at \(x\). Each such cycle has precisely one direction order from \(x\) placing \(v\) at step two (the opposite orientation puts it at step \(n-2\)). In all, there are \(2(n-2)!\) such cycles.

For one of these cycles let \(b_0,\ldots,b_{n-1}\) be the edge-color word of the rooted geodesic. Its twisted cyclic turn word has
\[
\delta_k=b_k+b_{k+1}\quad(0\le k<n-1),\qquad
\delta_{n-1}=b_{n-1}+b_0+1
\quad(\bmod2).
\]
Because \(n\) is even, the parity of the even-indexed turn strand equals \(\sum_jb_j\bmod2\), while the odd-indexed strand has the complementary parity. The step-two arc from \(u\) to \(v\) is the turn at position zero; its bit equals the parity \(a\) of the first two colors. By (RC4)--(RC5), its pair repair correlation is
\[
\mu_{(i,j,\sigma)}(u,v)
=(-1)^a f_m(a+t_\sigma),\qquad
f_m(0)=1,\quad f_m(1)=1-\frac2m.
\]
For the swapped order \((j,i,\sigma)\), the first-two-edge parity is \(a+\kappa\), while the entire suffix and its parity \(t_\sigma\) are unchanged. Thus
\[
\mu_{(j,i,\sigma)}(u,v)
=(-1)^{a+\kappa}f_m(a+\kappa+t_\sigma).
\]
If \(\kappa=1\), their sum simplifies to
\[
\boxed{\mu_{(i,j,\sigma)}+\mu_{(j,i,\sigma)}
=\frac2m(-1)^{t_\sigma},}\tag{SQF4}
\]
independent of the colors on the square except through its curvature. If \(\kappa=0\), their sum equals
\[
2(-1)^a\left(1-\frac1m\right)+\frac2m(-1)^{t_\sigma}.
\]
For each cycle \(C\), its contribution to \(\widehat X_c(\{u,v\})\) is
\[
\mathbb E_h[I_C(h)(-1)^{h(u)+h(v)}]
=p\,\mu_C(u,v),\qquad p=\frac nN.
\]
Sum these paired contributions over all \((n-2)!\) suffix orders, and use \(n=2m\). This gives (SQF1). The bounds (SQF2)--(SQF3) follow from \(|T_{x;ij}|\le(n-2)!\). \(\square\)

**Normalizations and curvature consequence.** Since \(\mathbb E_hX_c=n!/2\),
\[
\boxed{
\frac{|\widehat X_c(\{u,v\})|}{\mathbb E_hX_c}
\le
\begin{cases}
8/[Nn(n-1)],&\kappa=1,\\
4/[N(n-1)],&\kappa=0.
\end{cases}}\tag{SQF5}
\]
For \(n\ge6\), the two projective pairs at Hamming distance two uniquely determine the underlying square's two directions, so this is an intrinsic pairwise statement. It makes the color-curvature cochain appear directly in the Fourier analysis of the **global count** of monochromatic geodesic cycles. Curved squares cause a cancellation of repair correlations between two neighboring direction orders; the even-turn-strand obstruction is correspondingly weakened. This does not by itself give a pointwise positive lower bound for \(X_c(h)\), because higher-order gauge Fourier modes remain uncontrolled.

**Checks.** The paired cycle-correlation identity (SQF4) and resulting coefficient (SQF1) were checked independently using brute-force local invariant-gauge enumeration for arbitrary sampled legal colorings in dimensions \(n=6,8\), comparing against all \((n-2)!\) suffix orders. The theorem is proved without computational assumptions.



### Curvature-sensitive global gauge-orbit variance budget

Keep \(n\ge6\) even and \(X_c(h)=N_1(c+\delta h)\), with \(N=2^{n-1}\) and \(\mathbb E_hX_c=n!/2\). Let
\[
\rho_\kappa(c)=
\frac{\#\{\text{cubical square faces with odd color parity}\}}
{2^{n-2}\binom n2}
\]
be the proportion of curved squares. Let \(\theta_n^{\rm par}\) denote the positive universal bound in (PC2).

**Theorem (curvature-depleted quadratic variance).** The contribution from two-vertex gauge Walsh coefficients at projective Hamming distance two obeys
\[
\boxed{
\sum_{\substack{\{u,v\}\subset Q_n/\tau\\d_{\rm proj}(u,v)=2}}
\left(\frac{\widehat X_c(\{u,v\})}{\mathbb E_hX_c}\right)^2
\le
\frac{4n}{N(n-1)}
\left[1-\rho_\kappa(c)\left(1-\frac4{n^2}\right)\right].
}\tag{CV1}
\]
Consequently the complete relative variance satisfies
\[
\boxed{
\frac{\operatorname{Var}_h X_c}{(\mathbb E_hX_c)^2}
\le
\theta_n^{\rm par}
-\frac{4n}{N(n-1)}
\rho_\kappa(c)\left(1-\frac4{n^2}\right)
=:\Theta_n(c),
}\tag{CV2}
\]
and the fraction of successful colorings in the invariant vertex-gauge orbit of \(c\) is at least \(1/(1+\Theta_n(c))\).

*Proof.* The pairwise Fourier bounds (SQF5) are
\(4/[N(n-1)]\) on a flat square and \(8/[Nn(n-1)]\) on a curved one. There are precisely \(N\binom n2/2=Nn(n-1)/4\) unordered projective vertex pairs at projective Hamming distance two (the restriction \(n\ge6\) excludes the special four-dimensional coincidence). Every projective antipodal square orbit contributes two such diagonal vertex pairs, both carrying its square curvature. Hence the proportion of curved pairs is precisely \(\rho_\kappa(c)\). Squaring (SQF5), summing over the pairs, and simplifying yields (CV1).

For any subset \(S\subseteq Q_n/\tau\), the Fourier coefficient of \(X_c\) is \(\sum_{C:S\subseteq V_C}\widehat I_C(S)\). The separate parity-strand symmetry (PC1) forces \(\widehat I_C(S)=0\) unless \(S\) meets both cube-parity vertex classes evenly. Also \(|\widehat I_C(S)|\le p\), where \(p=n/N\). Parseval therefore bounds the total relative variance by the expected number of nonempty gauge subsets lying inside the intersection of two random projective Petrie cycles, even in each parity class. The earlier estimate (PC2) bounds this by
\(\theta_n^{\rm par}\) after allowing **all** even-cardinality intersection subsets other than a mixed-parity pair.

Of the pair-subsets counted in that earlier bound, those at projective Hamming distance two contribute precisely
\[
\frac{4n}{N(n-1)}
\]
to its geometric upper bound: these are the \(d=2,n-2\) terms in the \(k=2\) composition part of (PC2). Replacing only this component by the stronger true degree-two Fourier energy bound (CV1), and retaining the previous bounds on all other Fourier subsets, yields (CV2). Cauchy--Schwarz gives the success fraction. \(\square\)

**Scope.** Balanced legal cubes have \(\rho_\kappa(c)>0\), by the previously established quantitative curvature-density theorem, so (CV2) is strictly stronger than (PC3) on the balanced class. However that same toolkit constructs badness-preserving balanced lifts, conditional on a bad original coloring, with \(\rho_\kappa(c)\to0\). Thus the strict correction in (CV2) does **not** imply a dimension-uniform positive curvature density or unrestricted NORI1 closure. Its importance is structural: the leading quadratic gauge-dependence can now be bounded in terms of the underlying cubical curvature, rather than by projective cycle intersections alone.



### Leading asymptotic constant of the even-gauge variance estimate

The finite composition formula (PC2) permits a sharp asymptotic expansion, improving its coarse uniform \(72/2^n\) bound.

**Theorem (sharp leading term for the pair-overlap estimate).** As even \(n\to\infty\),
\[
\boxed{
\theta_n^{\rm par}=\frac{12+O(1/n)}{2^n}.
}\tag{AS1}
\]
For the curvature-sensitive upper bound \(\Theta_n(c)\) in (CV2),
\[
\boxed{
\Theta_n(c)=\frac{12-8\rho_\kappa(c)+O(1/n)}{2^n},
}\tag{AS2}
\]
with an \(O(1/n)\) remainder uniform over all legal colorings \(c\). In particular the proved gauge-orbit bad-fraction bound is asymptotically at most
\[
\boxed{\Pr_h(N_1(c+\delta h)=0)
\le \frac{12-8\rho_\kappa(c)+O(1/n)}{2^n}.}\tag{AS3}
\]

*Proof.* Recall \(A_{n,k}=n!^{-1}\sum_{d_1+\cdots+d_k=n}\prod d_i!\) from (CM1). The \(k=2\) term is
\[
A_{n,2}=\sum_{j=1}^{n-1}\binom nj^{-1}
=\frac2n+O(n^{-2}).
\]
For \(k=3\), the three compositions obtained by permuting \((n-2,1,1)\) contribute
\(3/[n(n-1)]\). All other three-block compositions contribute \(O(n^{-3})\), giving
\[
A_{n,3}=\frac3{n^2}+O(n^{-3}).
\]
For completeness, the tail is \(\sum_{k\ge4}A_{n,k}=O(n^{-3})\). Indeed the known bound from the proof of (PC4) gives \(\sum_{k\ge3}A_{m,k}=O(m^{-2})\) for \(m\ge3\). Splitting the first block yields
\[
\sum_{k\ge4}A_{n,k}
=\sum_{j=1}^{n-3}\binom nj^{-1}\sum_{k\ge3}A_{n-j,k}.
\]
For \(j\le n/2\), the inner sum is \(O(n^{-2})\) and the reciprocal-binomial sum is \(O(n^{-1})\). For \(j>n/2\), writing \(m=n-j\ge3\) gives a bounded inner sum and \(\sum_{m=3}^{\lfloor n/2\rfloor}\binom nm^{-1}=O(n^{-3})\). Thus the tail is \(O(n^{-3})\).

The even-distance pair sum in (PC2) is
\[
\sum_{\substack{2\le d\le n-2\\d\ \mathrm{even}}}\binom nd^{-1}
=\frac2{\binom n2}+O(n^{-3})
=\frac4{n^2}+O(n^{-3}).
\]
Also \(\sum_{k=3}^n2A_{n,k}/k=2/n^2+O(n^{-3})\). Substitution into (PC2), with \(N=2^{n-1}\), yields
\[
\theta_n^{\rm par}
=\frac{n^2}{N}\left(\frac6{n^2}+O(n^{-3})\right)
=\frac{12+O(n^{-1})}{2^n}.
\]
The correction in (CV2) is
\[
\frac{4n}{N(n-1)}\rho_\kappa(c)\left(1-\frac4{n^2}\right)
=\frac{8\rho_\kappa(c)+O(1/n)}{2^n},
\]
uniformly since \(0\le\rho_\kappa(c)\le1\). This proves (AS1)--(AS3). \(\square\)

**Interpretation.** The leading contribution \(8/2^n\) in (AS1) comes from same-parity projective vertex pairs at cube distance two, while the remaining \(4/2^n\) comes from the three-block composition sector of higher cycle intersections. Odd square curvature suppresses the former. The known balanced counterexample-preserving sparse-curvature lifts permit \(\rho_\kappa(c)\to0\) even conditional on hypothetical badness, so a proof using only the curvature density in (AS2) cannot eliminate that conditional construction. Further closure must exploit signed multi-cycle compatibility rather than positivity of curvature density alone.


## Odd face networks give doubly exponential success abundance in every gauge orbit

The second-moment bounds can be amplified using networks containing many full geodesics. The seam obstruction is resolved by odd block sizes and one block root slide. Entropy covering then permits the translated networks to overlap.

Write \(n\ge3\), \(M=2^{n-1}\), and fix an arbitrary legal antipodally odd coloring \(c\) of \(Q_n\). The invariant vertex gauge bits \(h([v])\), indexed by the \(M\) antipodal vertex pairs, are independent and uniform. All probabilities below are within this one fixed gauge orbit; balance is unnecessary.

### A uniform connection bound on an ordinary face with prescribed endpoint gauges

Let \(f\) be any ordinary coloring of a \(k\)-cube, with specified opposite corners \(u,v\), \(k\ge1\). For each full \(u\)-to-\(v\) geodesic \(P\), let \(t(P)\) be the parity of its edge-color sum. Choose \(q\in\mathbb F_2\) represented by at least \(k!/2\) of these path parities.

**Lemma (preferred face parity).** Fix arbitrary gauge values \(a,b\) at \(u,v\) with \(a+b=q\). Sample all other face vertex-gauge values independently and uniformly. Then
\[
\boxed{\Pr(\text{a full zero geodesic from }u\text{ to }v
\text{ in }f+\delta h\mid h(u)=a,h(v)=b)\ge\tfrac18.}\tag{FN1}
\]

*Proof.* For a path with \(t(P)=q\), its \(k-1\) internal gauge bits have a unique assignment making the path zero once the endpoint gauges are fixed. Its probability is therefore \(2^{-(k-1)}\). Let \(\mathscr P_q\) be the family of those paths and let \(Y\) count its zero paths. Then
\[
\mathbb EY=|\mathscr P_q|\,2^{-(k-1)}.
\]
For two such paths with \(U\) common internal vertices, their required gauge values either conflict, giving joint probability zero, or agree, giving joint probability \(2^{-2(k-1)+U}\).

For uniform direction permutations \(\pi,\sigma\), the common internal vertices are their common proper prefix sets. Expanding \(2^U\) by subsets of common cuts gives
\[
\mathbb E_{\pi,\sigma}2^U
=B_k:=\frac1{k!}
\sum_{\substack{a_1+\cdots+a_r=k\\a_i\ge1,\ 1\le r\le k}}
\prod_{i=1}^r a_i!.
\tag{FN2}
\]
Indeed a prescribed set of cuts splits the direction list into positive consecutive block lengths, and the permutations respecting those cuts number the product of their factorials.

The composition bound \(B_k\le2\) was established in (CM2)--(CM3). It also follows from
\[
B_0=1,\qquad B_k=1+\sum_{j=1}^{k-1}\frac{B_{k-j}}{\binom kj},
\]
using \(\sum_{j=1}^{k-1}\binom kj^{-1}\le4/k\) for \(k\ge8\) and direct evaluation for \(k\le7\); the corresponding numerators \(k!B_k\) are \(1,3,11,47,231,1303,8431\).

Bounding the sum over \(\mathscr P_q^2\) by the sum over all path pairs yields
\[
\frac{\mathbb EY^2}{(\mathbb EY)^2}
\le \left(\frac{k!}{|\mathscr P_q|}\right)^2B_k
\le8.
\]
Cauchy--Schwarz proves (FN1). Simultaneously complementing all local gauge bits proves the same assertion for either permitted choice of \(a,b\). \(\square\)

This lemma is for an ordinary face coloring. Inside a proper face of \(Q_n\), its vertices represent distinct projective vertex pairs, so the lemma applies to the restriction of an invariant full-cube gauge.

### Choosing compatible seams by an odd block slide

Partition the \(n\) directions into \(r\ge2\) nonempty blocks \(I_1,\ldots,I_r\), each of odd size \(k_j\). Thus \(r\equiv n\pmod2\). Put \(k=\max_j k_j\). Fix a starting vertex \(x_0\) and define
\[
x_j=x_0+\sum_{i\in I_1\cup\cdots\cup I_j}e_i,
\qquad 0\le j\le r.
\]
In particular \(x_r=\bar x_0\). Let \(F_j\) be the \(I_j\)-face joining \(x_{j-1}\) to \(x_j\). Call the projective union of these faces \(A\).

The \(r\) projective corner vertices \([x_0],\ldots,[x_{r-1}]\) are distinct. Consecutive faces share their corner; nonconsecutive faces have disjoint projective interiors. The first and last faces also share \([x_0]\). For \(r=2\), the two faces share both corners and no internal projective vertex. In every case,
\[
\boxed{|A|=\sum_{j=1}^r2^{k_j}-r\le r2^k.}\tag{FN3}
\]
These intersection assertions follow directly by examining the fixed values of all direction blocks outside a face.

Choose a preferred path parity \(q_j\) for the ordinary coloring on each \(F_j\), as in (FN1). If \(\sum_jq_j=0\), retain this face order. Otherwise move its first block to the end, using
\[
F_2,F_3,\ldots,F_r,\bar F_1,
\]
starting at \(x_1\) and ending at \(\bar x_1\). Antipodal oddness complements every edge color in \(F_1\); since \(k_1\) is odd, the preferred parity of \(\bar F_1\) is \(q_1+1\). Thus this block slide changes the total preferred parity by one. After one of these two choices it is zero. The projective support \(A\) stays the same.

**Lemma (uniform network success).** One of those two root cuts, selected from \(c\) before sampling the gauge, has
\[
\boxed{\Pr_h(\text{all its faces have full zero connections})
\ge p_r:=2^{1-4r}.}\tag{FN4}
\]
Consequently the same probability lower bound holds for a full zero antipodal geodesic supported on this face network.

*Proof.* After choosing the even-sum cut, require at its \(r\) projective corners
\[
h([x_{j-1}])+h([x_j])=q_j
\]
in cyclic order, with the selected parities and corners relabeled when the first block was moved. This cycle of equations has rank \(r-1\), since its right sides sum to zero. Its probability is \(2^{-(r-1)}\).

Conditional on any satisfying corner assignment, the internal gauge bits of the \(r\) faces are mutually independent. By (FN1), each face has a full zero connection with probability at least \(1/8\). Their joint probability is at least \(8^{-r}\). Multiplication gives \(2^{-(r-1)}8^{-r}=2^{1-4r}\).

Concatenate the face connections. Every direction is traversed once, and the selected initial and terminal vertices are antipodal. This is a full zero geodesic. \(\square\)

The odd block requirement is the seam mechanism: it supplies a root cut with a consistent corner system for every baseline coloring.

### Counting all translated failures by entropy covering

Let \(s=|A|\), and translate this same block network by every \(x\in Q_n\). In each translate, choose its successful-parity root cut from the fixed coloring \(c\). Its success event depends only on the \(s\) gauge bits in the translated projective support. By (FN4), at most \((1-p_r)2^s\) assignments on that support fail the selected network test.

**Theorem (uniform doubly exponential gauge bound).**
\[
\boxed{
\Pr_h(c+\delta h\text{ is bad})
\le(1-p_r)^{M/s}
\le
\exp\!\left(-\frac{2^{\,n-k-4r}}r\right).
}\tag{FN5}
\]
This holds for every legal baseline coloring and every odd-block partition above.

*Proof.* If there are no bad gauge assignments the conclusion holds. Otherwise choose a uniformly random assignment \(H\) from the bad gauge assignments. Every translated restriction \(H|_{A+x}\) must lie in that network's failure set, so
\[
\mathcal H(H|_{A+x})\le s+\log_2(1-p_r).
\]
The family of \(2^n\) translated projective supports covers each of the \(M\) gauge variables precisely \(2s\) times, by translation transitivity.

The entropy covering inequality gives
\[
\begin{aligned}
\log_2\#\{\text{bad gauge assignments}\}
=\mathcal H(H)
&\le\frac1{2s}\sum_{x\in Q_n}\mathcal H(H|_{A+x})\\
&\le M+\frac Ms\log_2(1-p_r).
\end{aligned}
\]
For completeness, the covering inequality follows by ordering the variables, expanding every restricted entropy by the chain rule, and using that conditioning on fewer earlier variables gives at least the corresponding fully conditioned entropy. Each variable's fully conditioned contribution is counted \(2s\) times.

Divide the count bound by \(2^M\) for the first inequality in (FN5). Use \(1-p\le e^{-p}\), \(M=2^{n-1}\), \(p_r=2^{1-4r}\), and \(s\le r2^k\) for the second. Uniform invariant gauges give the uniform distribution on their orbit because the edge-coboundary kernel consists of the two constant gauges. Thus the same bound is the bad *fraction* inside that orbit. \(\square\)

**Corollary (asymptotic orbit abundance).** Uniformly over all legal baseline colorings,
\[
\boxed{
\Pr_h(c+\delta h\text{ is bad})
\le
\exp\!\left(-2^{\,n-4\sqrt n-O(\log n)}\right)
=
\exp\!\left(-2^{\,n-O(\sqrt n)}\right).
}\tag{FN6}
\]
Indeed choose \(r=\sqrt n/2+O(1)\), adjusted to have the same parity as \(n\), and divide \(n\) into \(r\) odd positive sizes differing by at most two. Then \(k\le n/r+2\), so \(k+4r\le4\sqrt n+O(1)\); the extra denominator \(r\) contributes \(O(\log n)\) to the exponent. The assertion is asymptotic; the partition form (FN5) is the finite statement.

The estimate holds inside every invariant gauge orbit, including each individual projective gauge phase with its square curvature held fixed. Averaging over gauge orbits gives the same upper bound for the bad fraction among all legal odd colorings.

### An explicit decoder using disjoint networks

There is a direct encoding version that uses fewer translates and gives a weaker bound of the same doubly exponential form. Let \(A_0\subset Q_n\) be the ordinary vertex union of the faces before projective identification; \(|A_0|\le r2^k\). Two translates have intersecting projective supports only if their translation difference lies in
\[
(A_0+A_0)\ \cup\ (\mathbf1+A_0+A_0).
\]
There are at most \(2r^2 2^{2k}\) such differences. Greedy packing therefore gives at least
\[
t\ge\frac{2^n}{2r^2 2^{2k}}
\tag{FN7}
\]
pairwise disjoint projective network supports.

For a bad gauge assignment, record its gauge bits outside those supports. Within each support, record the index of its local assignment in the lexicographically ordered list of assignments failing that support's preselected network test. These lists depend only on the known coloring and network. The decoder restores the outside bits and independently retrieves each local assignment by its index. This reconstructs the whole gauge assignment.

Use a single mixed-radix rank for the tuple of local indices, avoiding separate binary-rounding costs. Since every local list has at most \((1-p_r)2^s\) entries, the count of encoded bad assignments is at most
\[
2^M(1-p_r)^t
\le
2^M\exp\!\left(-\frac{2^{\,n-2k-4r}}{r^2}\right).
\tag{FN8}
\]
Thus the decoder saves at least \(p_rt/\ln2\) bits in logarithmic code-space size. Taking \(r\) proportional to \(\sqrt n\) gives a saving \(2^{\,n-O(\sqrt n)}\). The entropy covering argument improves this by using all overlapping translates rather than discarding their overlaps.

**Checks.** The preferred-parity face assertion was checked by complete enumeration of all ordinary baseline colorings in face dimensions one, two and three, and all internal gauges after fixing the preferred endpoint relation. The minimum observed success probabilities were \(1,1/2,1/2\), respectively, above the proved \(1/8\). Ten independently generated legal six-cube baselines were also tested on two odd three-direction faces with 2,000 uniform gauges each. The selected-cut network success frequencies ranged from \(0.1775\) to \(0.2995\), above \(2^{-7}\). These finite checks are separate from the proofs.

**Closure significance.** This strengthens the previous \(O(2^{-n})\) exceptional gauge fraction to a doubly exponential upper bound by solving seam compatibility inside a whole face network. The encoder supplies a proved saving \(2^{n-O(\sqrt n)}\) among \(M=2^{n-1}\) gauge bits. The positive-entropy bad flats (EA10) and the zero-or-full balanced entropy dichotomy (EA6) remain compatible with this saving: its fraction of \(M\) tends to zero. A complete entropy proof still needs enough compatibility among overlapping networks, or an additional global invariant, to reach the counting closure criteria in that subsection. NORI1 remains open.



### A sharp entropy barrier for parity-peelable Petrie-cycle families

The stronger linear packing bound **already obtained** in the Article XV subsection *Gauge critical switches and clustered witnesses on full paths* (equation (EA12)) supersedes the earlier weaker quadratic pair-packing estimate. We restate it here in the parity-peeling notation to make its consequence for the new gauge-orbit abundance theorems explicit.

Let \(n\ge4\) be even, \(N=2^{n-1}\) be the number of projective cube vertices, and \(p=n/N\) the grade-one success probability of any one Petrie cycle under a uniformly random invariant vertex gauge.

**Theorem (parity-peeling linear packing, previously established as EA12).** If \(\mathscr F\) is any family of projective Petrie cycles meeting the parity-peeling criterion (PI1), then
\[
\boxed{
|\mathscr F|\le\left\lfloor\frac{N-2}{n-2}\right\rfloor.
}\tag{PB1}
\]
Because the corresponding repair indicators are mutually independent, the expected number of successful members is at most
\[
\boxed{
\mathbb E_h\sum_{C\in\mathscr F}I_C
=p|\mathscr F|\le\frac{n(N-2)}{N(n-2)}
=1+O(1/n).
}\tag{PB2}
\]
Furthermore, uniformly over every such family,
\[
\boxed{
\Pr_h(I_C=0\text{ for every }C\in\mathscr F)
=(1-p)^{|\mathscr F|}
\ge (1-p)^{\lfloor(N-2)/(n-2)\rfloor}
\longrightarrow e^{-1}
}
\tag{PB3}
\]
in the sense that the displayed explicit lower bound tends to \(e^{-1}\) as even \(n\to\infty\). Thus no family certified independent solely through parity-peeling can make its joint failure probability tend to zero, let alone prove pointwise NORI1.

*Proof.* Read the peeling order backward. The first added cycle has \(n\) projective vertices. Every later added cycle meets the union of those already present in at most one even and one odd projective vertex, hence supplies at least \(n-2\) new vertices. Since the projective cube has only \(N\) vertices,
\[
N\ge n+(|\mathscr F|-1)(n-2)=2+|\mathscr F|(n-2).
\]
This proves (PB1), the established EA12 argument. Multiply by \(p=n/N\) for (PB2). The independence theorem (PI2) gives the first identity of (PB3), and \(p=n/N\to0\) with \(\lfloor(N-2)/(n-2)\rfloor p\to1\) gives the limit. \(\square\)

The earlier quadratic pair-counting bound
\(|\mathscr F|\le N(N-2)/[n(n-2)]\)
is valid but much weaker; it must not be mistaken for the effective parity-peeling limitation.

**Comparison with the new face-network method.** The independently published odd-face network theorem (FN5)--(FN6) gives much smaller joint failure probabilities by exploiting overlapping local events and network-level seam compatibility. It bypasses (PB3) because its translated events are **not** required to form a parity-peelable independent family. The linear packing barrier therefore reinforces the mathematical necessity of exploiting dependent overlap cores, or structured face networks, rather than trying to choose more individually independent Petrie cycles.



## Simultaneous zero-geodesic gauges: full incidence criterion and the projective holonomy obstruction

The preceding repair and odd-face network results concern the event that *at least one* geodesic becomes monochromatic under an invariant vertex gauge. For a **prescribed family** of full geodesics, simultaneous repair is governed by a finite binary graph-incidence system. Importantly, ordinary square curvature does not capture its entire obstruction, because the projective antipodal identification creates additional closed walks.

Fix \(n\ge3\), a legal antipodally odd coloring \(c\), and a nonempty finite family \(\mathscr P\) of rooted, oriented full antipodal geodesics. Build a labeled undirected **multigraph** \(H_{\mathscr P}\) as follows: its vertices are the antipodal vertex pairs \([x]=\{x,\bar x\}\) visited by at least one member of \(\mathscr P\). For **each occurrence** of a physical cube edge \(e=\{x,x^i\}\) in any \(P\in\mathscr P\), insert a graph edge joining \([x]\) to \([x^i]\), with binary label \(c(e)\). Keep parallel occurrences, including the two antipodal lifts of one projective edge, as separate graph edges. Put \(v=|V(H_{\mathscr P})|\), and let \(q\) be the number of connected components of this multigraph.

**Theorem (complete affine overlap-syndrome criterion).** The following are equivalent:

1. There exists an antipodally invariant vertex gauge \(h\) such that **every** path in \(\mathscr P\) is completely zero-colored in \(c+\delta h\).
2. Every closed walk \(W\) in the labeled multigraph \(H_{\mathscr P}\) has label sum zero:
   \[
   \boxed{\bigoplus_{e\in W}c(e)=0.}\tag{HG1}
   \]
3. The labeled edge cochain of \(H_{\mathscr P}\) lies in the image of its vertex-incidence coboundary.

If these conditions hold, the number of full invariant vertex gauges meeting all the prescribed paths is
\[
\boxed{2^{\,2^{n-1}-v+q},\qquad
\Pr_h(\mathscr P\text{ all zero})=2^{-(v-q)}.}\tag{HG2}
\]
Otherwise the number and probability are both zero.

*Proof.* Every occurrence \(e=\{x,x^i\}\) gives the binary gauge equation
\(h([x])+h([x^i])=c(e)\).
These equations form the incidence-coboundary system on \(H_{\mathscr P}\). Summing around a closed walk proves necessity of (HG1). Conversely choose one projective vertex in each connected component, choose its gauge value freely, and propagate values along a spanning tree. Every non-tree edge equation holds precisely when its fundamental-cycle label sum vanishes. The \(q\) chosen component values and the \(2^{n-1}-v\) unused gauge bits are free, yielding (HG2). Parallel edge occurrences are essential: when two paths prescribe opposite antipodal lifts of an edge, they impose different labels on the same endpoint pair, producing an obstructed two-edge closed walk. \(\square\)

**Corollary (two-path overlap criterion).** For a single geodesic \(P\), the projected graph is an \(n\)-cycle, so the gauge condition is that its total edge-color parity be even. In that case its two solutions on its \(n\) projective vertices differ by a common constant. Let \(P,Q\) both have even edge-color parity, and let \(S=V_P\cap V_Q\). Denote by \(h_P,h_Q\) any two particular repairing assignments on their own vertex sets. Then
\[
\boxed{
P,Q\text{ are simultaneously repairable}
\ \Longleftrightarrow\
(h_P+h_Q)|_S\text{ is constant}.
}\tag{HG3}
\]
In particular, **any two even-parity full geodesics sharing at most one projective vertex are simultaneously repairable**. For shared vertices \(u,v\), the first obstruction is the relative-bit syndrome
\[
h_P(u)+h_P(v)+h_Q(u)+h_Q(v).
\]
This is a direct pathwise analogue of the affine overlap system (SC1) for the more permissive grade-one events; the prescribed-zero event is much more rigid.

**Theorem (fresh-square gallery extension).** Let \(P_0,\ldots,P_r\) be rooted full geodesics, with \(P_0\) having even total edge-color parity. Suppose each \(P_j\), \(j\ge1\), is obtained from one preceding path \(P_i\), \(i<j\), by exchanging two consecutive direction steps on a cubical square \(F_j\). Assume:

- Every \(F_j\) has zero cubical color curvature.
- The intermediate projective vertex introduced by that exchange has not appeared in \(P_0,\ldots,P_{j-1}\).

Then there is a **single** invariant vertex gauge that makes all \(P_0,\ldots,P_r\) zero-colored simultaneously.

*Proof.* First solve the gauge equations on \(P_0\), possible since its projected \(n\)-cycle has even total label parity. For each successive square exchange, all edge occurrences except the two-edge route across the exchanged square are inherited from its parent path and are already zero. The two replaced edges have endpoint gauge bits already assigned, while the intermediate projective vertex is new and hence unassigned. The square's zero curvature says that the XOR of the labels on the old route equals that on the new route. Therefore the two new edge equations are consistent and uniquely determine the new vertex bit. Extend the partial gauge there. Induction proves simultaneous repair, and remaining projective gauge values can be chosen arbitrarily. \(\square\)

**Flat-square obstruction from antipodal projective holonomy.** Zero curvature on **every** square is not sufficient for arbitrary families of even-parity geodesics to admit a common gauge. In any even dimension \(n\ge4\), take the legal flat coloring
\[
\boxed{c_i(x)=\sum_{j\ne i}x_j\pmod2,}\tag{HG4}
\]
whose square color parity is zero and whose antipodal edge color is complemented. Choose a root \(x\) whose vertex-bit sum satisfies
\[
|x|\equiv \binom n2\pmod2.
\]
Every full path from this root has even color parity: for the order \(\pi=(i_1,\ldots,i_n)\), its \(k\)-th color is
\(|x|-x_{i_k}+(k-1)\pmod2\), so the full XOR is
\(|x|+\binom n2=0\pmod2\).

Now consider the two rooted orders
\[
P=(i_1,i_2,\ldots,i_n),\qquad
Q=(i_2,\ldots,i_n,i_1).
\tag{HG5}
\]
Each can individually be made zero by an invariant gauge. But their first and last edges respectively are
\[
e=\{x,x^{i_1}\},\qquad
\bar e=\{\overline{x^{i_1}},\bar x\},
\]
which are antipodal lifts of one projective edge and consequently have opposite colors under **every legal invariant-gauge transform**. Thus \(P,Q\) can never both be zero. Equivalently \(H_{\{P,Q\}}\) has two parallel graph-edge occurrences with opposite labels, violating (HG1). The obstruction survives though *all cubical squares are flat*. It comes from the antipodal projective holonomy, not ordinary curvature.

**Finite audit.** The flat example was checked by enumerating all invariant gauges in \(Q_4\): for \(P=(0,1,2,3)\) and \(Q=(1,2,3,0)\) from root zero, each has \(32\) successful gauges among \(256\), but their joint success count is zero. In contrast, exchanging the first two adjacent steps yields two paths having \(16\) common zero gauges, as predicted by the fresh-square extension. The general assertions are proved by incidence linear algebra and do not rely on these checks.

**Consequence for face-network closure.** The obstruction to making any *fixed collection* of network path witnesses simultaneously zero is now a finite affine cycle-syndrome, with two distinct sources: local cubical square curvature and projective antipodal holonomy. A tree of flat adjacent-square exchanges with fresh projective vertices always repairs, whereas collisions of previously used projective vertices can create global incompatibilities even when all local square curvatures vanish. This gives a concrete target for overlap arguments among odd-face networks: control the cycle syndromes produced when their path families reuse projective vertices, rather than impose pairwise square-flatness alone. The theorem does not establish a successful witness for the original ungauged coloring.



### Flat-face polarization maximizes all Petrie grades; curvature gives quantitative stability

Fix \(n\ge3\) and an arbitrary legal antipodally odd cube-edge coloring \(c\), not necessarily balanced. Let \(H\) be either \((n-1)\)-dimensional face perpendicular to a chosen direction \(i\), and let \(\bar H\) be its antipodal opposite face. These two faces partition the cube vertices, and \(H\) contains precisely one representative of each of the \(N=2^{n-1}\) antipodal vertex pairs.

Let \(t_H(c)\) be the number of ordinary two-dimensional squares contained in \(H\) with odd four-edge color sum. Let \(M=2^{n-2}(n-1)!\) be the total number of projective Petrie cycles and \(N_1\) their grade-one count.

**Theorem (flat-facet maximal-polarization normal form).** If \(t_H(c)=0\), an antipodally invariant vertex gauge \(h\) exists such that:

1. **Every** edge lying in \(H\) is zero-colored and **every** edge lying in \(\bar H\) is one-colored in \(c+\delta h\).
2. **Every full antipodal geodesic**, from every root and in every direction order, has at most one ordinary color change.
3. Consequently
   \[
   \boxed{N_1(c+\delta h)=M,\qquad
   \#\{\text{rooted full zero geodesics}\}=2M
   =2^{n-1}(n-1)!.}\tag{FF1}
   \]

Thus a gauge orbit containing a coloring with one flat facet contains a representative with the **maximum conceivable grade-one count**, rather than merely one monochromatic full geodesic. The result holds in both parities of the ambient dimension.

*Proof.* Flatness on the ordinary cubical face \(H\) means that the restriction of the edge coloring is a vertex coboundary: choose \(f:H\to\mathbb F_2\) so that \(c(e)=f(u)+f(v)\) for every face edge \(e=uv\). This is possible by integrating edge labels from a basepoint and commuting path steps across flat squares. Define \(h([u])=f(u)\) using the unique representative \(u\in H\) of each antipodal pair. This gives an invariant full-cube gauge and makes every edge of \(H\) zero. Antipodal oddness then makes every edge of the opposite face \(\bar H\) one.

Every full antipodal geodesic crosses direction \(i\) precisely once. Its non-\(i\) edges before that crossing lie in one of \(H,\bar H\), and its non-\(i\) edges afterward lie in the other. Its color word is therefore of the form \(0^a b1^d\) or \(1^a b0^d\), where \(b\in\{0,1\}\), allowing empty blocks. Such a word has at most one ordinary color change. Its twisted cyclic turn word has precisely one defect, so every projective Petrie cycle has grade one. Each grade-one cycle has one unoriented monochromatic full geodesic, or two rooted oriented zero descriptions, by the projective grade theorem. This proves (FF1). \(\square\)

**Lemma (unit-cost cubical curvature filling).** Let \(f\) be any arbitrary binary edge coloring on an ordinary \(d\)-cube, \(d\ge2\), with \(t\) curved square faces. Then there exists a vertex potential \(a\) such that
\[
\boxed{
\#\{e=uv:f(e)+a(u)+a(v)=1\}\le t.
}\tag{FF2}
\]

*Proof.* Choose a basepoint \(b\) and a permutation \(\pi\) of the \(d\) directions independently and uniformly. For each vertex \(x\), define \(a(x)\) as the edge-color sum along the canonical shortest \(b\)-to-\(x\) path, traversing all differing directions in order \(\pi\). For an edge in direction \(i\), compare the two canonical root paths to its endpoints. Commuting the unique \(i\)-step past the subsequently ordered directions \(j\) on which the endpoint differs from \(b\) expresses the edge defect as a binary sum of square curvatures. Therefore its defect indicator is bounded by the number of curved squares appearing in that commuting sequence.

Over a uniformly sampled cube edge, random \(b\), and random \(\pi\), each other direction \(j\) is included with probability \(1/4\): its bit disagrees with \(b\) with probability \(1/2\), and it follows \(i\) in \(\pi\) with probability \(1/2\). Conditional on inclusion, its square location is uniform among the \(2^{d-2}\) squares in directions \(i,j\). Summing over ordered pairs \(i\ne j\) gives
\[
\mathbb E_{b,\pi}(\#\text{defective edges})
\le \frac{d\,2^{d-1}}{d}\,
\frac1{4\cdot2^{d-2}}\,
\sum_{i\ne j}t_{ij}
=t,
\]
where \(t_{ij}\) counts curved squares in the unordered pair of directions \(i,j\) and \(\sum_{i\ne j}t_{ij}=2t\). Some \(b,\pi\) therefore attain at most \(t\) defective edges. \(\square\)

**Theorem (facet-curvature stability of maximal grade).** For every legal coloring \(c\) and any chosen facet \(H\), there exists an invariant vertex gauge \(h\) such that
\[
\boxed{
N_1(c+\delta h)\ \ge\
\max\{0,\,M-t_H(c)(n-1)!\}.
}\tag{FF3}
\]
Equivalently,
\[
\boxed{
\frac{N_1(c+\delta h)}M
\ge \max\left\{0,\,1-\frac{t_H(c)}{2^{n-2}}\right\}.
}\tag{FF4}
\]
In particular if \(t_H(c)<2^{n-2}\), the resulting coloring has at least one grade-one cycle; if \(t_H(c)=0\), it has the maximum \(M\).

*Proof.* Use (FF2) on the \((n-1)\)-face \(H\) to choose a potential \(f\) leaving at most \(m\le t_H(c)\) one-colored face edges. Extend it to an invariant gauge using the representatives in \(H\), as in the first theorem. The corresponding antipodal face \(\bar H\) has all non-\(i\) edge colors complementary, so every noncrossing edge outside those \(m\) antipodal edge-pair orbits has the same face-polarized color pattern as the flat-facet case.

Any projective Petrie cycle that does not use one of those \(m\) exceptional edge-pair orbits therefore has grade one. Each antipodal undirected edge-pair orbit belongs to precisely \((n-1)!\) projective Petrie cycles, by the standard incidence count in Article XV. At most \(m(n-1)!\) cycles encounter the exceptional orbits. Removing them from the \(M\) total gives (FF3)--(FF4). \(\square\)

**Balanced-coloring separation.** In contrast, a vertex-balanced coloring of \(Q_n\), \(n=2m\ge4\), cannot have every projective cycle at grade one. At any vertex \(v\), choose a central one-colored edge in one of \(m\) directions. There are \(m\) zero-colored incoming directions at \(v\) and \(m\) zero-colored outgoing directions at its opposite endpoint; at least \(m(m-1)\) choices of the incoming and outgoing directions are distinct. This produces a three-edge direction-simple segment with color pattern \(010\). The same count applies with colors exchanged. Counting all \(2^n\) choices of \(v\), both central colors, and all \((n-3)!\) completions to a full path gives at least the fraction
\[
\frac{2m^2(m-1)}{n(n-1)(n-2)}
=\frac{n}{4(n-1)}
\]
of rooted full geodesics having at least two ordinary color changes. All such geodesics belong to projective Petrie cycles of grade at least three; since every projective cycle has the same number of rooted descriptions,
\[
\boxed{
N_1(c)\le
\left(1-\frac{n}{4(n-1)}\right)M.
}\tag{FF5}
\]
Thus a balanced coloring is separated by an asymptotically \(1/4\) fraction from the maximal grade-one state (FF1), even though an invariant gauge need not preserve balance.

**Scope for grand closure.** The curvature-filling lemma and face-polarization theorem provide a constructive **local-curvature-to-global-grade** estimate inside every gauge orbit, but they do not establish that the original coloring is good. Balanced counterexample-preserving lifts may retain large absolute face curvature even when their curved-square **fraction** is small. Consequently (FF3) is a quantitative stability statement and a potential ingredient for interaction with gauge-star exchange, not an unrestricted NORI1 proof. The key gap remains transporting this abundance from a favorable gauge back to the original coloring without crossing a bad gauge.



### Every facet of a balanced odd cube has nonzero curvature

The previous flat-facet gauge theorem has a strong counterpart in the balanced regime. Unlike the earlier result that a balanced antipodally odd coloring must have *some* curved square, the following shows that curvature cannot be confined away from **any** cubical facet.

**Theorem (balanced facet nonflatness).** Let \(n=2m\ge4\), and let \(c\) be an antipodally odd binary edge coloring of \(Q_n\) having \(m\) incident edges of each color at every vertex. Then
\[
\boxed{\text{Every one of the }2n\text{ ordinary }(n-1)\text{-faces contains a square of odd color curvature.}}\tag{BF1}
\]

*Proof.* Suppose some facet \(H\) perpendicular to direction \(i\) has zero square curvature. Regard \(H\) as the ordinary cube \(Q_d\), with \(d=2m-1\). All its square curvatures vanish, so there exists a sign-valued vertex potential \(g:H\to\{-1,+1\}\) such that its internal signed edge colors satisfy
\[
s_j(y)=g(y)g(y^j),\qquad j\ne i.
\]
Let \(A_H\) be the adjacency operator of \(Q_d\). Vertex balance gives
\[
\sum_{j\ne i}s_j(y)=-s_i(y),
\qquad\text{hence}\qquad
\boxed{g(y)(A_Hg)(y)=b(y):=-s_i(y)\in\{-1,+1\}.}\tag{BF2}
\]

Let \(Jy\) denote the bitwise complement of \(y\) in the \(d\) directions of \(H\). An \(i\)-edge at \(y\) and the \(i\)-edge at \(Jy\) are antipodal edges of \(Q_n\). Thus
\[
\boxed{b(Jy)=-b(y).}\tag{BF3}
\]
Since \(g(y)^2=b(y)^2=1\), (BF2) implies
\(\|A_Hg\|_2^2=\|g\|_2^2=2^d\).

The Walsh character of a subset \(K\subseteq[d]\) is an eigenvector of \(A_H\) with eigenvalue \(d-2|K|\). Since \(d\) is odd, every eigenvalue has absolute value at least one. Equality of the two squared norms therefore forces the Walsh expansion of \(g\) to be supported **only** on the two levels with eigenvalues \(+1\) and \(-1\), namely \(|K|=m-1\) and \(|K|=m\). Write
\[
g=g_{m-1}+g_m,\qquad A_Hg=g_{m-1}-g_m.
\]
Pointwise multiplication gives
\[
\boxed{b=gA_Hg=g_{m-1}^2-g_m^2.}\tag{BF4}
\]

Under complementing all \(d\) bits, a Walsh homogeneous component at level \(k\) gains sign \((-1)^k\). Hence both squares on the RHS of (BF4) are **invariant** under \(J\), forcing \(b(Jy)=b(y)\). This contradicts (BF3), because \(b(y)\) is always \(+1\) or \(-1\). Therefore no facet is flat. \(\square\)

**Interpretation.** Balance places an internal facet gradient, if it existed, at the minimum of the odd-cube adjacency spectral norm, where only the two middle Walsh levels survive. That spectral extremality forces an antipodally even local signed-degree pattern, contradicting the antipodally odd crossing-edge requirement. Consequently no balanced odd coloring itself admits the maximal flat-facet polarization construction (FF1). Its **gauge orbit** may contain unbalanced representatives with very different vertex degrees, so (BF1) is not a gauge-invariant condition and does not contradict the universal gauge-orbit abundance results.

In dimension four, exhaustive enumeration of all 48 balanced legal colorings confirms that none of their eight facets is flat. The theorem covers all even dimensions without relying on finite enumeration.



### Quantitative nonflatness of every balanced facet

The qualitative spectral obstruction (BF1) has a dimension-uniform stability version. It shows that a balanced antipodally odd cube cannot concentrate essentially all of its curvature outside one exceptional almost-flat facet.

**Theorem (facetwise quantitative curvature).** For every even \(n=2m\ge4\), every perfectly balanced antipodally odd coloring \(c\) of \(Q_n\), and **every** ordinary facet \(H\cong Q_{n-1}\), the number \(t_H(c)\) of curved two-dimensional square faces contained in \(H\) satisfies
\[
\boxed{
t_H(c)\ >\ \frac{2^{n-1}}{4n^3}.
}\tag{BS1}
\]
The constant is not claimed optimal. In particular every facet has exponentially many curved squares, even though its curved-square *proportion* may approach zero with dimension.

*Proof.* Put \(d=n-1=2m-1\) and \(V=2^d\), and regard the restriction of \(c\) to \(H\) as an arbitrary \(d\)-cube edge coloring. By the unit-cost curvature-filling lemma (FF2), there exists \(g:H\to\{-1,+1\}\) such that the gradient signs
\[
s'_j(y)=g(y)g(y^j)
\]
disagree with the signed internal colors \(s_j(y)=(-1)^{c_j(y)}\) on at most \(r\le t_H(c)\) undirected face edges.

Let \(A\) be the \(d\)-cube adjacency operator. Balance says that the signed internal-degree sum
\[
b(y)=\sum_{j=1}^d s_j(y)=-s_i(y)
\]
is in \(\{-1,+1\}\), where \(i\) is the omitted facet direction. Antipodal oddness says \(b(Jy)=-b(y)\), with \(Jy\) the complement of the \(d\) facet bits. Put
\[
F(y)=g(y)(Ag)(y),\qquad D(y)=F(y)-b(y).
\]
If \(r_y\) gradient-sign disagreements touch \(y\), then \(|D(y)|\le2r_y\), \(\sum_y r_y=2r\), and \(r_y\le d\). Consequently
\[
\boxed{\|D\|_1\le4r,\qquad
\|D\|_2^2\le 8dr.}\tag{BS2}
\]
Because \(g(y)^2=b(y)^2=1\),
\[
\|Ag\|_2^2=\|F\|_2^2
=\|b+D\|_2^2
\le V+2\|D\|_1+\|D\|_2^2
\le V+8(d+1)r.
\tag{BS3}
\]

Let \(P\) be the orthogonal Walsh projection onto the two middle Fourier levels \(|K|=m-1,m\), whose adjacency eigenvalues are \(+1,-1\). Write \(q=Pg\), \(e=g-q\). Every other Walsh adjacency eigenvalue has absolute value at least three. Therefore
\[
\|Ag\|_2^2-\|g\|_2^2
=\sum_K((d-2|K|)^2-1)|\widehat g(K)|^2\,V
\ge8\|e\|_2^2,
\]
and (BS3) gives
\[
\boxed{\|e\|_2^2\le(d+1)r.}\tag{BS4}
\]

The function \(qAq\) is **even** under facet complementation \(J\): if \(q=q_{m-1}+q_m\), then \(Aq=q_{m-1}-q_m\), so
\(qAq=q_{m-1}^2-q_m^2\), invariant under \(J\).
Meanwhile \(b\) is **odd** under \(J\) and takes only signs, so \(\|b\|_1=V\).

Expand
\[
F=gAg=qAq+qAe+eAq+eAe.
\]
Taking the \(J\)-odd parts, applying \(\ell^1\)-\(\ell^2\) Cauchy--Schwarz, and using
\(\|Aq\|_2=\|q\|_2\le\sqrt V\), \(\|Ae\|_2\le d\|e\|_2\), yields
\[
\|F_{\rm odd}\|_1
\le(d+1)\sqrt V\,\|e\|_2+d\|e\|_2^2.
\]
Because \(F=b+D\) and \(b\) is odd, the odd projection of \(D\) has \(\ell^1\) norm at most \(\|D\|_1\), so
\[
\begin{aligned}
V=\|b\|_1
&\le \|F_{\rm odd}\|_1+\|D\|_1\\
&\le(d+1)\sqrt{V(d+1)r}
+\bigl[d(d+1)+4\bigr]r.
\end{aligned}\tag{BS5}
\]
Put \(x=r/V\). If \(x\le1/[4(d+1)^3]\), the first term on the RHS of (BS5), divided by \(V\), is at most \(1/2\); the second is at most \(1/[2(d+1)]\le1/8\). This contradicts (BS5). Thus
\[
r>\frac{V}{4(d+1)^3}
=\frac{2^{n-1}}{4n^3}.
\]
Since \(t_H(c)\ge r\), the asserted bound follows. \(\square\)

**Scope and comparison.** The previously established global balanced-curvature density theorem is stronger when curvature is aggregated over the whole cube. The new feature of (BS1) is **uniform localization to every single facet**: no facet of a balanced odd cube can have curvature support smaller than exponential scale \(2^n/\operatorname{poly}(n)\). This is a quantitative obstruction to a bad balanced coloring whose curvature were confined to a small collection of distant facets. It does not imply geodesic existence, and counterexample-preserving lifts with a vanishing *fraction* of curved squares remain compatible with the bound.
