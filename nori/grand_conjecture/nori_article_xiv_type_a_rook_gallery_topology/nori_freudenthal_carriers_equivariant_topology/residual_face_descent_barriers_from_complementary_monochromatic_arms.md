# Residual-face descent barriers from complementary monochromatic arms

# Residual-face descent barriers from complementary monochromatic arms

This section combines the rooted geodesic-prefix complexes of Article XIV, Subsection 38, with the projective square-curvature theory of Subsection 28. It proves a local-to-global gluing criterion for **arbitrary residual dimension sets**, and, in codimension two, converts the hypothetical failure of NORI1 into an explicit constraint on every square accessible from complementary red geodesic arms. The conclusion is uniform in dimension and uses no restricted coloring family.

Let \(n\ge3\), \(D=[n]\), and let \(c:E(Q_n)\to\mathbb F_2\) satisfy \(c(\tau e)=1-c(e)\). Write \(\mathcal R_x=\{S\subseteq D:\text{some red geodesic from }x\text{ uses precisely }S\}\), as in Subsections 29 and 38. Suppose \(S,T\in\mathcal R_x\) are disjoint, and put
\[
M=D\setminus(S\cup T),\qquad y_S=x\oplus\mathbf1_S,\qquad y_T=x\oplus\mathbf1_T.
\tag{1}
\]
Let \(F_S\) be the cubical \(|M|\)-face based at \(y_S\) with free dimension set \(M\). Its antipodal mate is the parallel face \(F_T\): indeed
\(\tau y_S=y_T\oplus\mathbf1_M\).

**Theorem 1 (two-arm residual-face gluing).** For every ordering \(\sigma\) of the missing dimensions \(M\), let \(w_{F_S}(\sigma)\) be the color word of the monotone path from \(y_S\) to \(y_S\oplus\mathbf1_M\), traversing \(M\) in that order. Then there is a complete dimension-simple antipodal geodesic whose color word is
\[
\boxed{0^{|S|}\ w_{F_S}(\sigma)\ 1^{|T|}.}
\tag{2}
\]
Consequently, if any \(w_{F_S}(\sigma)\) is nondecreasing (belongs to \(0^*1^*\)), the coloring has a monochromatic full antipodal geodesic from some root.

*Proof.* Choose red monotone geodesics \(P_S:x\to y_S\) and \(P_T:x\to y_T\), using the disjoint dimension sets \(S,T\). Let \(R_\sigma\) traverse the missing face from \(y_S\) to \(y_S\oplus\mathbf1_M\). Antipodally translate \(P_T\) and reverse it; this is a blue geodesic starting at \(\tau y_T=y_S\oplus\mathbf1_M\) and ending at \(\tau x\), using precisely the dimensions of \(T\). Concatenating \(P_S,R_\sigma,(\tau P_T)^{\rm rev}\) gives (2), uses each of the three disjoint dimension sets precisely once, and ends at \(\tau x\). If \(w_{F_S}(\sigma)\) is nondecreasing, the full word has at most one switch. Rotating the starting point across its possible unique switch and using \(c(\tau e)=1-c(e)\) converts the path into a monochromatic full geodesic. \(\square\)

**Corollary 2 (uniform descent barrier in a hypothetical counterexample).** If a legal coloring has no monochromatic full antipodal geodesic, then for every root \(x\) and every pair of disjoint members \(S,T\in\mathcal R_x\), every monotone full path across the residual face \(F_S\) has a color descent \(1\to0\). Equivalently, no such path has a word in \(0^*1^*\). This includes the rank-\((n-1)\) impossibility of Subsection 38 when \(|M|=1\), since a one-edge word has no descent.

**Theorem 3 (the codimension-two blue-out/red-in square gate).** Assume no monochromatic full antipodal geodesic exists. Let \(S,T\in\mathcal R_x\) be disjoint and leave two missing dimensions \(M=\{i,j\}\). Writing \(y=y_S\), the square \(F_S\) satisfies
\[
\boxed{
c_i(y)=c_j(y)=1,\qquad
c_j(y\oplus e_i)=c_i(y\oplus e_j)=0.
}
\tag{3}
\]
Thus **both** dimension-simple paths across the square have word \(10\), and
\[
\boxed{\kappa(F_S)=0,\qquad
\Omega_0(F_S;y)=\Omega_1(F_S;y)=0.}
\tag{4}
\]
The opposite face \(F_T=\tau F_S\) obeys the same blue-out/red-in rule at its lower corner \(y_T\) in the rooted Boolean order.

*Proof.* The only two paths across a square use the orders \(i,j\) and \(j,i\). Theorem 1 forbids the three nondecreasing two-bit words \(00,01,11\); thus each must have word \(10\), proving (3). Their color sums are both one, so the sum of the four square-edge bits is zero, giving \(\kappa=0\). Neither route is monochromatic in either color, so \(\Omega_0=\Omega_1=0\). Antipodal translation reverses colors and interchanges the top and bottom of the square, sending a route word \(10\) to the reversed-complemented word \(10\), proving the statement for the opposite face. \(\square\)

The gate is stronger than ordinary flatness: a flat square can have monochromatic two-step paths, while (3) rules out even a one-switch ascending route compatible with the two red arms. In particular, if a legal coloring contains two disjoint red geodesic arms from a root whose missing pair of dimensions spans a curved square, **then a monochromatic full geodesic exists**, without requiring any no-counterexample hypothesis.

## Projective reachability coverage

Call a two-face \(F\) **two-arm covered** if for some root \(x\) and disjoint \(S,T\in\mathcal R_x\) with \(S\cup T=D\setminus\{i,j\}\), the face \(F\) is the residual square \(F_S\) in dimensions \(i,j\). Since the same data gives \(F_T=\tau F_S\), coverage is antipodally invariant. Let \(Y=\partial Q_n/\tau\cong\mathbb RP^{n-1}\), and let \(B(c)\subseteq Y\) be the cubical subcomplex consisting of its entire one-skeleton together with all projected two-arm-covered squares and their faces.

**Theorem 4 (homological coverage certificate in odd dimension).** Suppose \(n\ge3\) is odd. If the inclusion
\[
\iota_*:H_2(B(c);\mathbb F_2)\longrightarrow
H_2(Y;\mathbb F_2)\cong\mathbb F_2
\tag{5}
\]
is nonzero, then the unrestricted NORI1 conclusion holds: some monochromatic full antipodal geodesic exists.

Equivalently, **under a hypothetical NORI1 counterexample in odd dimension, the inclusion (5) must be zero**. Furthermore at least \(2^{n-3}\) antipodal square orbits lie outside \(B(c)\); each canonical projected exchange disk contains an odd number of uncovered squares with nonzero curvature.

*Proof.* Suppose there is no monochromatic full geodesic. By Theorem 3, the square curvature \(\bar\kappa\) vanishes on every two-face of \(B(c)\). Article XIV, Subsection 28, proves \([\bar\kappa]=u^2\), the nonzero degree-two class of \(Y\). Therefore every two-cycle supported in \(B(c)\) pairs to zero with \(\bar\kappa\), and cannot represent the nonzero class of \(H_2(Y)\). This proves the claim about (5). The same subsection proves that \(\bar\kappa\) has at least \(2^{n-3}\) supported square orbits; all of them lie outside \(B(c)\). Its antipodal exchange-disk Stokes identity gives odd curvature evaluation on each canonical projected disk, so each disk contains an odd number of curvature squares, all uncovered. \(\square\)

**Proof-search implication.** The theorem translates the topological \(u^2\) obstruction into a **geometrically defined deficiency of dimension-simple monochromatic reachability**. An odd-dimensional counterexample would have to leave enough uncovered squares to prevent the red two-arm coverage subcomplex from carrying any projective two-homology generator. Proving instead that its reachability coverage carries such a generator would settle odd-dimensional NORI1. This is a sufficient structural target, not a new hypothesis defining a restricted graph family. In even dimension, the ordinary curvature class vanishes and this particular \(u^2\)-pairing argument does not apply; the rooted square-gate and residual-face descent theorems remain valid in both parities. A full Wu–Yang chain lift must account for that additional root/order information.

## Theorem 5 (sharp all-rank descending-turn demand)

Let \(F\) be an arbitrary \(m\)-dimensional Boolean face with a specified starting corner \(y\), \(m\ge2\), and an arbitrary binary undirected-edge coloring (no antipodal condition needed inside \(F\)). Suppose **every** monotone full geodesic in \(F\), starting at \(y\) and using its \(m\) free dimensions once, contains a consecutive color descent \(1\to0\).

Let \(D_{10}(F;y)\) denote the number of distinct directed two-edge monotone paths
\[
y\oplus\mathbf1_A
\longrightarrow y\oplus\mathbf1_{A\cup\{i\}}
\longrightarrow y\oplus\mathbf1_{A\cup\{i,j\}}
\quad(A\subseteq M,\;i,j\in M\setminus A,\;i\ne j)
\]
whose first edge has color \(1\) and second edge color \(0\). Then
\[
\boxed{D_{10}(F;y)\ge m(m-1).}
\tag{6}
\]
Equality is attained for every \(m\): give all edges leaving rank zero color \(1\), all edges leaving rank one color \(0\), and all edges at higher ranks color \(0\). Then every full path has a descent at its first two steps and there are precisely \(m(m-1)\) descending two-edge paths.

*Proof.* There are \(m!\) monotone full dimension orders. A prescribed two-edge turn occurring after a prefix of \(a=|A|\) dimensions is contained in precisely
\[
a!\,(m-a-2)!
\]
full ordered geodesics: the first \(a\) dimensions may be permuted freely before the turn and the remaining \(m-a-2\) afterward. For \(0\le a\le m-2\),
\[
a!\,(m-a-2)!\le(m-2)!.
\]
Every full geodesic contains at least one descending turn by assumption, so counting pairs consisting of a full geodesic and one of its descending turns gives
\[
m!\le D_{10}(F;y)\,(m-2)!,
\]
proving (6). In the exhibited rank coloring, the only descents occur between the first and second edges, and the two dimensions in those positions can be any of the \(m(m-1)\) ordered pairs, giving equality. \(\square\)

**Corollary 6 (quantitative residual-face condition in a hypothetical NORI1 counterexample).** For every root \(x\) and disjoint red-reachable dimension sets \(S,T\) leaving \(m\ge2\) unused dimensions, their residual face \(F_S\) contains at least \(m(m-1)\) distinct descending monotone two-edge turns. At \(m=2\) there are just two possible turns, so the lower bound forces both to descend, recovering Theorem 3's blue-out/red-in square gate.

The inequality is independent of any specialized coloring family, is sharp in every rank, and provides a local turn-count lower bound for future attempts to double count residual-face demands against the global distribution of red and blue incidences. It does not by itself yield a global contradiction.

## Corollary 7 (rank-weighted descent inequality)

In the setting of Theorem 5, let \(D_r(F;y)\) denote the number of descending two-edge paths whose first edge is traversed after precisely \(r\) preceding dimensions, \(0\le r\le m-2\). Then
\[
\boxed{
\sum_{r=0}^{m-2}
\frac{D_r(F;y)}{m(m-1)\binom{m-2}{r}}\ge1.
}
\tag{7}
\]
The inequality is sharp for all \(m\ge2\). In the absence of a monochromatic full antipodal geodesic, every residual face of two disjoint red-reachable arms obeys (7).

*Proof.* A fixed descent with \(r\) preceding dimensions lies on \(r!(m-r-2)!\) of the \(m!\) full dimension orders, hence on a fraction \(1/[m(m-1)\binom{m-2}{r}]\) of them. The left-hand side is the expected number of descents on a uniformly random monotone full geodesic. Every such geodesic has at least one descent by hypothesis, so the expectation is at least one. The rank-zero blue-then-red coloring from Theorem 5 produces precisely one descent per complete path, attaining equality. \(\square\)

The rank-weighted form distinguishes where in a residual face descending turns occur; a turn in a middle rank lies on fewer complete dimension orders than one near an endpoint. It may be more useful than the unweighted lower bound when combining multiple overlapping residual-face demands.

## Corollary 8 (unique gate corner and maximal root-sensitive square defects)

Suppose a two-arm-covered square satisfies the gate relation (3). In the square itself, **one corner is distinguished** by having both outward square edges blue and both edges entering its opposite corner red. This corner is unique, independent of the red-arm witness. At that corner and its opposite, the two monochromatic exchange defects both vanish. At either of the two adjacent corners, the two traversals across the square have respective color words \(00\) and \(11\), so
\[
\boxed{\Omega_0=\Omega_1=1\quad\text{at both adjacent corners},}
\tag{8}
\]
while \(\kappa=0\) everywhere on the face.

*Proof.* Write the original gate corner as \(y\). Its incident square edges both have color \(1\); the edges at the opposite corner \(y\oplus e_i\oplus e_j\) both have color \(0\). Each adjacent corner therefore has one incident blue edge and one incident red edge, so no other corner can have the blue-out/red-in pattern. From either adjacent corner, the two increasing routes cross the four square edges in the patterns \(00\) and \(11\). Thus one route is red-monochromatic, the other blue-monochromatic, giving (8). From \(y\), both routes have word \(10\), and from the opposite corner both have word \(01\), so neither is monochromatic. Flatness follows from the two blue and two red edge bits. \(\square\)

This specifies the **additional order-sensitive signal in a flat square**: its rooted monochromatic defects change maximally between adjacent corners even though ordinary curvature is zero. The unique source corner supplies an intrinsic way to label such a gate for any future color-sensitive chain correction. In particular, merely enforcing zero curvature would miss all these defects.
