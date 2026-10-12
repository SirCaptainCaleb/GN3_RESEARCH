# Star-bundle rigidity and the weighted monochromatic-component quotient

Let \(n\ge3\), let \(\tau\) be cube antipodality, and put \(G=Q_n/\langle\tau\rangle\), \(H=L(G)\). Fix an antipodally odd coloring \(c:E(Q_n)\to\mathbb F_2\). Its turn cochain \(d:E(H)\to\mathbb F_2\) assigns the difference of the colors of two incident cube edges. Put \(H_0=(V(H),\{t:d(t)=0\})\). Every turn of \(H\) has a unique center \(v\in V(G)\), and the turns centered at \(v\) form a clique \(K_v\cong K_n\).

Choose a lift \(x\) of \(v\), and partition the \(n\) cube edges incident with \(x\) into their color classes \(A_v^0,A_v^1\). Changing the lift interchanges these classes. Thus \(\lambda_v=|A_v^0||A_v^1|\) is well-defined. Write \(v\) *mixed* if \(\lambda_v>0\). All vertices of the turn clique corresponding to \(A_v^i\) belong to one connected component \(R_v^i\) of \(H_0\), because every turn inside a color class is a zero turn. The two components \(R_v^0,R_v^1\) may coincide.

Define a weighted multigraph \(\Gamma_c\) whose vertices are the connected components of \(H_0\). Each mixed \(v\) contributes one edge joining \(R_v^0\) and \(R_v^1\), of weight \(\lambda_v\), with loops allowed. Thus the \(\lambda_v\) different-color turns at one cube-vertex star form a single weighted edge bundle in \(\Gamma_c\).

**Theorem 1 (star-bundle rigidity).** Let \(b=\delta g\) be a binary cut cochain of \(H\) satisfying \(\operatorname{supp}(b)\subseteq\operatorname{supp}(d)\). Then, for every \(v\in V(G)\),
\[
\boxed{b|_{E(K_v)}=0\quad\text{or}\quad b|_{E(K_v)}=d|_{E(K_v)}.}\tag{1}
\]
Moreover, \(g\) descends to a binary vertex potential \(\bar g\) on \(\Gamma_c\). At a mixed \(v\), the second alternative of (1) holds if and only if \(\bar g(R_v^0)\ne\bar g(R_v^1)\). Conversely, any binary vertex potential on \(\Gamma_c\) determines a cut cochain of \(H\) supported on \(d\). Consequently,
\[
\boxed{|\operatorname{supp}(b)|=
\sum_{\substack{v\ \mathrm{mixed}\\\bar g(R_v^0)\ne\bar g(R_v^1)}}\lambda_v.}\tag{2}
\]
The support-minimizing cochains \(d'=d+b\) with \(\operatorname{supp}(d')\subseteq\operatorname{supp}(d)\) are therefore represented by maximum-weight cuts of \(\Gamma_c\).

*Proof.* The support inclusion forces \(b=0\) on \(H_0\); hence \(g\) is constant on every connected component of \(H_0\) and descends to \(\bar g\). At \(K_v\), it is constant on each of the two local color classes. If those constants agree then \(b\) vanishes on \(K_v\); if they differ then it is one precisely on turns between different color classes, which are the turns where \(d=1\). This proves (1). The converse follows by pulling any \(\bar g\) back to \(V(H)\); all zero turns then have equal endpoint values, so the pulled-back cut is supported on \(d\). The cliques \(K_v\) partition \(E(H)\), and a mixed clique has \(\lambda_v\) nonzero turns. This proves (2) and the weighted-cut statement. \(\square\)

**Theorem 2 (a cut-resistant star bundle).** Every antipodally odd coloring \(c\) admits a mixed vertex \(v\in V(G)\) such that \(R_v^0=R_v^1\). In particular,
\[
\boxed{\lambda_v\ge n-1,\qquad
d'|_{E(K_v)}=d|_{E(K_v)}}
\tag{3}
\]
for every admissible support-decreasing switching \(d'=d+b\). Equivalently, \(\Gamma_c\) has a positive-weight loop, whose whole turn bundle survives every such switching.

*Proof.* By the Wu–Yang theorem on antipodal edge colorings, there is a monochromatic cube path \(P\) from some vertex \(x\) to \(\tau x\). Denote its successive edges by \(e_1,\ldots,e_m\). Their antipodal-pair vertices \([e_1],\ldots,[e_m]\) form a zero-turn path in \(H_0\), so \([e_1]\) and \([e_m]\) lie in the same component. At \(x\), the incident cube edges \(e_1\) and \(\tau e_m\) have opposite colors, while their vertices downstairs are \([e_1]\) and \([e_m]\). Hence the two color classes of the star centered at \([x]\) lie in the same \(H_0\)-component, making its bundle a loop. Since the star has two nonempty classes of cardinalities \(k,n-k\), its weight is \(k(n-k)\ge n-1\). Theorem 1 shows that cuts supported on \(d\) vanish on loops, so this bundle persists in every \(d'\). \(\square\)

**Proposition 3 (a sparse-cut zero-penalty criterion).** Every binary cut \(b\) of \(H\) satisfying
\[
\boxed{|\operatorname{supp}(b)|<(n-1)2^{n-1}}
\tag{4}
\]
is disjoint from some length-\(n\) monodromy-one simple cycle \(C\), corresponding to a full antipodal geodesic. Thus this conclusion applies to every supported cut of Theorem 1 whose crossing weight (2) satisfies (4).

*Proof.* The cube automorphism group acts transitively on turns and preserves the family \(\mathcal R_n\) of length-\(n\) monodromy-one cycles. Every such cycle has \(n\) turns, and \(|E(H)|=\binom n2 2^{n-1}\). Therefore for uniformly sampled \(C\in\mathcal R_n\),
\[
\mathbb E_C|\operatorname{supp}(b)\cap C|
=\frac{n|\operatorname{supp}(b)|}{|E(H)|}
=\frac{2|\operatorname{supp}(b)|}{(n-1)2^{n-1}}<2.
\]
Every graph cut meets every graph cycle in an even number of edges. Hence a nonnegative even-valued random variable with mean below two must attain zero. \(\square\)

The weighted quotient makes support deletion a cut problem on indivisible local switch bundles. Theorem 2 supplies a permanently retained bundle; Proposition 3 gives a checkable sufficient condition for a shortest port cocircuit to incur zero cut penalty.

**Sharpness of (4).** The constant in Proposition 3 cannot be increased for general graph cuts. Fix a coordinate \(s\), and define a vertex potential \(g\) on \(H\) by \(g([e])=1\) when the direction of the cube edge \(e\) is \(s\), and \(g([e])=0\) otherwise. For \(b=\delta g\), every star \(K_v\) contributes \(n-1\) turns to \(\operatorname{supp}(b)\). Since \(G\) has \(2^{n-1}\) vertices,
\[
|\operatorname{supp}(b)|=(n-1)2^{n-1}.
\]
Every length-\(n\) monodromy-one cycle visits every coordinate direction once, so precisely two of its turns cross between the direction-\(s\) vertex and the remaining directions. Thus
\[
|\operatorname{supp}(b)\cap C|=2
\]
for every \(C\in\mathcal R_n\).
