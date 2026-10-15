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
