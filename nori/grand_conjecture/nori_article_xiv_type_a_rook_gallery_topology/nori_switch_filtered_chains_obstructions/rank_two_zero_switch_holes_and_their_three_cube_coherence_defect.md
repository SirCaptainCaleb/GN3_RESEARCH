# Rank-two zero-switch holes and their three-cube coherence defect

# Rank-two zero-switch holes and their three-cube coherence defect

We identify the first support-preserving obstruction to filling Freudenthal squares using monochromatic dimension-simple prefixes, and compute its initial three-cube compatibility law.

Let \(c:E(Q_n)\to\mathbb F_2\) be an arbitrary coloring. For a cubical square \(F\) and each corner \(v\), let \(C_v=K_v^0\cup K_v^1\) be the union of monochromatic rooted geodesic-prefix complexes. Put
\[
U_F^{[0]}=\bigcup_{v\in V(F)}(|C_v|\cap F).
\tag{1}
\]
The subcomplexes intersect \(F\) in simplices with all vertices in \(F\), since \(F\) is an exposed face of the geometric cube. Thus (1) depends only on the four edge bits around \(F\).

Write those bits cyclically \(a,b,c,d\), with arithmetic in \(\mathbb F_2\), and define
\[
\kappa(F)=a+b+c+d,\quad
\alpha(F)=(1+a+c)(1+b+d)(a+b),\quad
\theta(F)=\kappa(F)+\alpha(F).
\tag{2}
\]
Here \(\alpha(F)\) is the indicator that the edge bits alternate, and \(\kappa(F)\) is square curvature. These indicators are invariant under square symmetries and simultaneous complementation.

**Theorem 1 (complete square filling classification).** Up to dihedral symmetry and global color complement, the homotopy types and local relative homology groups are
\[
\begin{array}{c|c|c|c}
\text{cyclic bits}&U_F^{[0]}&H_1(U_F^{[0]};\mathbb F_2)&\theta(F)\\ \hline
0000&F&0&0\\
0011&F&0&0\\
0001&\text{two overlapping triangles plus a connecting boundary edge}&\mathbb F_2&1\\
0101&\partial F&\mathbb F_2&1 .
\end{array}
\tag{3}
\]
Consequently
\[
\boxed{\dim_{\mathbb F_2}H_2(F,U_F^{[0]};\mathbb F_2)=\theta(F).}
\tag{4}
\]
At filtration level one, every rooted prefix complex contains both two-step Freudenthal triangles of \(F\). Hence \(U_F^{[1]}=F\), and the nontrivial relative classes of (4) are filled by allowing one switch.

*Proof.* Every incident edge lies in each corner's monochromatic-prefix union. A rooted Freudenthal triangle belongs to it precisely when the associated two-edge route has equal edge bits. For \(0000\), all rooted routes are monochromatic. For \(0011\), a corner admits both opposite routes, of words \(00\) and \(11\), so its two triangles cover \(F\). For \(0001\), the sole monochromatic two-step routes run along the three consecutive equal-colored edges; their triangles on different square diagonals overlap in a contractible region, while the remaining boundary edge completes a circle. For \(0101\), no two-step route is monochromatic, leaving only \(\partial F\). These cases exhaust the square patterns. The first term of \(\theta\) detects odd patterns, the second detects alternating patterns, proving the last column. The long sequence of the pair \((F,U_F^{[0]})\), with \(F\) contractible and \(U_F^{[0]}\) connected, gives (4). Every length-two word has at most one switch, proving the final assertion. \(\square\)

For a legal antipodally odd cube coloring, \(\theta(\bar F)=\theta(F)\). Thus \(\theta\) descends to a projective 2-cochain. Its coboundary is a first three-dimensional coherence defect.

**Theorem 2 (flat three-cube law).** If the square curvature vanishes on every face of a cubical 3-face \(D\), then
\[
\boxed{\sum_{F\lessdot D}\alpha(F)
=\sum_{F\lessdot D}\theta(F)=0\pmod2.}
\tag{5}
\]
Thus \(\theta\) is a cocycle wherever the given coloring is flat.

*Proof.* A flat edge cochain on \(D\) is a coboundary \(\delta h\) of a vertex function. Write \(\Delta_i h(x)=h(x)+h(x+e_i)\) for the Boolean directional difference. Let \(i,j,k\) be the three directions and, at the lowest corner, abbreviate
\[
a=\Delta_i h,\quad b=\Delta_j h,\quad d=\Delta_k h,\quad
p=\Delta_i\Delta_j h,\quad q=\Delta_i\Delta_k h,\quad
r=\Delta_j\Delta_k h,\quad s=\Delta_i\Delta_j\Delta_k h .
\]
On the lower \(ij\) face, the opposite parallel-edge discrepancies both equal \(p\), giving \(\alpha_{ij}(0)=(1+p)(a+b)\) by (2). On the corresponding upper \(ij\) face,
\[
\alpha_{ij}(1)=(1+p+s)(a+b+q+r).
\]
Their sum is \((1+p)(q+r)+s(a+b+q+r)\). The analogous formulas for the \(ik\) faces paired in direction \(j\), and the \(jk\) faces paired in direction \(i\), sum to
\[
\begin{aligned}
\delta\alpha(D)
={}&(1+p)(q+r)+(1+q)(p+r)+(1+r)(p+q)\\
&+s[(a+b+q+r)+(a+d+p+r)+(b+d+p+q)].
\end{aligned}
\tag{6}
\]
Every term occurs an even number of times, so (6) is zero. Since \(\kappa=\delta c\), also \(\delta\kappa=\delta^2c=0\), proving (5). \(\square\)

**Theorem 3 (nonclosed defect in unrestricted legal colorings).** For every \(n\ge4\), there exists a legally antipodally odd coloring and a cubical 3-face \(D\) with
\[
\boxed{(\delta\theta)(D)=1.}
\tag{7}
\]

*Proof.* Choose a 3-face with directions \(i,j,k\). Give the two parallel dimension-\(i\) edges of its \(ij\)-square at \(k=0\) bit one, and give every other edge of \(D\) bit zero. This produces precisely one alternating face: the selected \(ij\) face has cyclic word \(1010\); its opposite face is monochromatic; the two \(ik\) faces each contain one colored edge; and the two \(jk\) faces are monochromatic. Hence \(\delta\alpha(D)=1\). As \(\delta\kappa=0\), equation (7) follows. When \(n\ge4\), the 3-face and its antipodal mate are disjoint. Prescribe the complementary coloring on that mate, then complete the remaining antipodal edge orbits arbitrarily. This yields the stated legal coloring. \(\square\)

**Theorem 4 (classification of all symmetric closed square-local rules).** Let \(f:\mathbb F_2^4\to\mathbb F_2\) be any function of the cyclic edge-color word of a square, invariant under dihedral symmetries and simultaneous color complementation. Assign to every square \(F\) of a cubical 3-face the value \(f(c|_{\partial F})\). The following are equivalent:

(i) For every binary edge coloring of every cubical 3-face \(D\), the sum \(\sum_{F\lessdot D}f(c|_{\partial F})\) vanishes.

(ii) There are constants \(u,v\in\mathbb F_2\) such that
\[
\boxed{f(c|_{\partial F})=u+v\kappa(F)\qquad\text{for every square }F.}
\tag{8}
\]

*Proof.* Dihedral symmetry and color complementation leave four orbits of cyclic square words, represented by \(0000,0001,0011,0101\). Write their values under \(f\) as \(A,B,C,D\).

First consider a cubical 3-face in which precisely two mutually perpendicular edges incident to the same corner have color one, and all ten remaining edges have color zero. Its six squares consist of three \(0000\) faces, two \(0001\) faces, and one \(0011\) face. The closedness condition forces
\[
3A+2B+C=A+C=0.
\]
Next give color one to precisely the two parallel edges in a single square, and zero to every other 3-face edge. This yields three \(0000\) faces, two \(0001\) faces, and one alternating \(0101\) face. Closedness forces \(A+D=0\). Thus \(C=D=A\), while \(B\) is unrestricted.

On the four word orbits, square curvature takes the respective values \(0,1,0,0\). Therefore the resulting rule is \(f=A+(A+B)\kappa\), establishing (ii). Conversely the constant square cochain has zero coboundary because every 3-cube has six square facets, and the curvature cochain is closed since \(\kappa=\delta c\) and \(\delta^2=0\). Every linear combination of these two rules is consequently closed. \(\square\)

**Corollary 5 (sharp limitation of square-only chain repairs).** There is no dihedrally symmetric, color-complement-invariant rule that detects the relative zero-switch hole in every square and is also a 2-cocycle for all unrestricted binary edge colorings. More generally, among all such square-local rules, the only universally closed information is a constant and square curvature. Any filtered Wu--Yang repair encoding the alternating flat-square obstruction must use additional data from roots, adjacent cells, or higher-dimensional incidence. A rooted or orientation-sensitive construction is not excluded by the theorem.

*Proof.* Theorem 1 identifies the desired hole rule as \(\theta\), whose values on the four orbits are \(0,1,0,1\). These fail the necessary equality between the \(0000\) and \(0101\) values in Theorem 4. The classification supplies the stronger assertion. \(\square\)

**Theorem 6 (projective class of the constant square cochain).** For \(n\ge3\), let \(Y_n=\partial[0,1]^n/A\cong\mathbb RP^{n-1}\). The cochain \(\mathbf1_2\in C^2(Y_n;\mathbb F_2)\), assigning one to every projective square, satisfies
\[
\boxed{[\mathbf1_2]=\left(\binom n2\bmod2\right)u^2,}
\tag{9}
\]
where \(u=w_1(S^{n-1}\to Y_n)\). In particular this cochain is a coboundary precisely for \(n\equiv0,1\pmod4\).

*Proof.* Every cubical 3-cell has six square facets, so \(\mathbf1_2\) is closed. Upstairs, define an undirected-edge one-cochain \(b\) by
\[
b_i(x)=\sum_{j<i}x_j\pmod2
\]
on an edge of direction \(i\). Every square has \(\delta b=1\): for \(i<j\), crossing \(i\) changes \(b_j\) and crossing \(j\) leaves \(b_i\) fixed. Let \(\tau x=\bar x\). Then
\[
\tau^*b+b=\delta g,\qquad
g(x)=\sum_{i=1}^n(i-1)x_i.
\tag{10}
\]
If a quotient one-cochain has coboundary \(\mathbf1_2\), its pullback \(d\) is invariant under \(\tau\) and satisfies \(\delta d=\delta b\). Because the covering boundary \(S^{n-1}\) has \(H^1=0\) for \(n\ge3\), we must have \(d=b+\delta h\) for some vertex function \(h\). Invariance is equivalent to
\[
\delta(g+h+\tau^*h)=0,
\]
meaning that \(g+h+\tau^*h\) is constant on the connected cube graph. But \(h+\tau^*h\) is invariant under \(\tau\), whereas
\[
g(\bar x)+g(x)=\sum_{i=1}^n(i-1)=\binom n2\pmod2.
\tag{11}
\]
Thus an invariant primitive is impossible if \(\binom n2\) is odd.

Conversely, if this binomial coefficient is even, \(g\) is invariant. Define \(h\) independently on antipodal vertex pairs so that \(h(x)+h(\bar x)=g(x)\). Then \(d=b+\delta h\) is invariant and has \(\delta d=\mathbf1_2\), giving a quotient primitive. Hence the constant cochain is a coboundary just when \(\binom n2\) is even. Since \(H^2(Y_n;\mathbb F_2)\cong\mathbb F_2\) is generated by \(u^2\), this proves (9). \(\square\)

**Corollary 7 (classification of universal local projective classes).** Let \(c\) be any legal antipodally odd edge coloring, \(n\ge3\). Every dihedrally symmetric, color-complement-invariant square-local rule that is a cocycle for all unrestricted colorings has the form \(f=a+b\kappa\), with \(a,b\in\mathbb F_2\), and
\[
\boxed{[f]=\left(a\binom n2+bn\right)u^2.}
\tag{12}
\]
Thus its projective cohomology class depends only on \(n,a,b\), independently of the edge coloring.

*Proof.* Theorem 4 gives the classification \(f=a+b\kappa\). Theorem 6 computes the constant cochain class, and the established projective-curvature theorem of Article XIV gives \([\bar\kappa]=(n\bmod2)u^2\). Add these classes. \(\square\)

**Implication for Wu--Yang chain corrections.** The indicator \(\theta=\kappa+\alpha\) detects one relative square-filling class for every zero-switch deficiency, including flat alternating squares invisible to curvature. Theorem 3 proves that these classes do not form a universal closed 2-cochain: their square-level cancellation can have a nonzero three-cube defect. A coherent filtered construction must therefore incorporate additional local incidence data and higher fillings. This result supplies a verified obstruction to a curvature-only or independently filled-square repair, while making no claim to resolve unrestricted NORI1 or the Hamilton boundary conjecture.
