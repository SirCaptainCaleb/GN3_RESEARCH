## Cubical Curvature and Exchange Topology

### Square defects and path-order holonomy in dimension-simple chain lifts

We examine a modification of Wu and Yang's Freudenthal chain map (arXiv:2607.19276, Sections 2 and 5.2–5.4) in which monochromatic reachability retains the set and order of used dimensions. There are two distinct local obstructions, both arising on squares, and a coherence identity in three dimensions.

Fix \(n\ge2\), a root \(x\in\mathbb F_2^n\), and an undirected binary edge coloring \(c\) with \(c(\bar e)=1-c(e)\). Put \(D=[n]\), \(y_S=x\oplus\mathbf1_S\), and for \(i\notin S\) set
\[
a_i^t(S)=\mathbf1_{\{c(\{y_S,y_{S\cup\{i\}}\})=t\}},
\qquad t\in\mathbb F_2.
\tag{1}
\]
On \(V=\mathbb F_2\langle [S]:S\subseteq D\rangle\), define rank-raising operators
\[
L_t[S]=\sum_{i\notin S}a_i^t(S)[S\cup\{i\}].
\tag{2}
\]
The coefficient of \([T]\) in \(L_t^{|T\setminus S|}[S]\) counts modulo two the color-\(t\) monotone paths from \(y_S\) to \(y_T\), with their dimension order retained. Every such path is dimension-simple.

#### Theorem 1 (monochromatic square defect and three-dimensional coherence)

For \(i,j\notin S\), \(i\ne j\), define the square defect
\[
\Omega_t(S;i,j)
=a_i^t(S)a_j^t(S\cup\{i\})
+a_j^t(S)a_i^t(S\cup\{j\})\pmod2.
\tag{3}
\]
It is one if and only if precisely one of the two increasing length-two routes across the square is monochromatic of color \(t\). The operators obey
\[
\boxed{L_t^2[S]=\sum_{\{i,j\}\subseteq D\setminus S}
\Omega_t(S;i,j)[S\cup\{i,j\}].}
\tag{4}
\]
Writing \(L=L_0+L_1\) gives
\[
\boxed{L^2=0,\qquad L_0^2+L_1^2=L_0L_1+L_1L_0.}
\tag{5}
\]
For three pairwise distinct \(i,j,k\notin S\), the defects satisfy
\[
\boxed{
\sum_{\{p,q,r\}=\{i,j,k\}\atop p<q}
\bigl[
a_r^t(S)\Omega_t(S\cup\{r\};p,q)
+\Omega_t(S;p,q)a_r^t(S\cup\{p,q\})
\bigr]=0
\quad\text{in }\mathbb F_2.
}
\tag{6}
\]
The antipodal symmetry is
\[
\boxed{\Omega_t(S;i,j)
=\Omega_{1-t}(D\setminus(S\cup\{i,j\});i,j).}
\tag{7}
\]

*Proof.* Two applications of (2) reach \(S\cup\{i,j\}\) by the two dimension orders, with monochromatic indicators the two summands in (3). This gives (4). Since \(a_i^0(S)+a_i^1(S)=1\), the operator \(L\) is the uncolored Boolean rank-raising operator, and \(L^2=0\) over \(\mathbb F_2\): every unordered pair contributes twice. Expanding \((L_0+L_1)^2=0\) proves (5).

Associativity gives \(L_tL_t^2+L_t^2L_t=L_t^3+L_t^3=0\). Extract the coefficient of \([S\cup\{i,j,k\}]\) to obtain (6). For (7), apply the cube antipode and reverse each increasing two-step route. A color-\(t\) route becomes a color-\((1-t)\) route on the complementary square, with the two orders exchanged, so their exclusive-or indicators agree. \(\square\)

Thus the uncolored Freudenthal incidence operator is a differential, while the two monochromatic operators generally are not. Their failure is concentrated on rank-two faces and satisfies the first higher compatibility relation (6). This is a non-flat rank-sensitive analogue of the uncolored differential, not an existence proof.

#### Theorem 2 (path composition alone cannot repair the square cancellation)

For fixed \(x,t\), define a category \(\mathcal P_t(x)\) with objects \(S\subseteq D\). A morphism \(S\to T\), \(S\subseteq T\), is a particular increasing color-\(t\) path from \(y_S\) to \(y_T\), with its full dimension order retained. Empty paths are identities; composition concatenates paths, preserving dimension-simpleness.

Take a square \((S;i,j)\) whose **two** increasing routes are both monochromatic of color \(t\). Write \(p_{ij},p_{ji}:S\to S\cup\{i,j\}\) for the two resulting composite morphisms. In the normalized simplicial chain complex of its category nerve, the one-cycle
\[
\boxed{z=[p_{ij}]+[p_{ji}]\in C_1(N\mathcal P_t(x);\mathbb F_2)}
\tag{8}
\]
represents a nonzero homology class.

*Proof.* Each path morphism has simplicial boundary \([S]+[S\cup\{i,j\}]\), so \(\partial z=0\). Choose the elementary directed edge \(e=(S\to S\cup\{i\})\), which appears in \(p_{ij}\) and not in \(p_{ji}\). Define a one-cochain \(w\) on each morphism \(p\) as the parity of the number of occurrences of \(e\) in \(p\). For any composable \(p,q\), additivity gives
\[
(\delta w)(p,q)=w(p)+w(q)+w(q\circ p)=0.
\]
Thus \(w\) is a cocycle, but \(w(z)=1\). No boundary pairs nontrivially with a cocycle, so \(z\) is not a boundary. \(\square\)

On the same square, the two Freudenthal triangles have an internal *common* diagonal edge and its two boundary contributions cancel. Mapping the triangles into the path-category nerve instead gives two **different** long-edge morphisms, \(p_{ij},p_{ji}\); their difference is the nonboundary class (8). Thus merely replacing connected-component labels with the ordinary nerve of complete monochromatic path morphisms cannot make Wu–Yang's Freudenthal cancellation work, even when both orders have the same color.

The example is legal under antipodal oddness: for \(n\ge3\), color all four edges of one two-dimensional cube face \(t\), the four edges of its antipodal face \(1-t\), and extend the other edge orbits arbitrarily. Both routes of the chosen square are monochromatic, so (8) applies.

#### Two independent square effects and the proposed correction

1. **Availability:** if just one color-\(t\) route survives, \(\Omega_t(S;i,j)=1\), so the rank-raising operator \(L_t\) fails to square to zero.
2. **Order holonomy:** if both routes survive, \(\Omega_t(S;i,j)=0\), yet \([p_{ij}]+[p_{ji}]\) remains a nontrivial homology class in the free path-category nerve.

A viable dimension-simple Wu–Yang modification must include coherent two-dimensional *exchange fillers* between the two dimension orders, while recording their color compatibility. Identity (6) gives a three-dimensional constraint on such corrections. Simply identifying both dimension orders unconditionally loses the color-incidence information; using only ordinary path composition does not cancel the second obstruction.

The uncolored quotient obtained by identifying path morphisms under adjacent-square exchanges is the Boolean inclusion category \(S\subseteq T\). Its proper part \(0<|S|<n\) has order complex \(S^{n-2}\), the barycentric subdivision of the boundary of an \((n-1)\)-simplex. Complementation acts antipodally under the vertex embedding
\[
S\longmapsto \mathbf1_S-\frac{|S|}{n}\mathbf1
\quad\text{in }W=\{z\in\mathbb R^n:\sum_i z_i=0\}.
\tag{9}
\]
This locates a classical type-A antipodal sphere directly in the square-exchange quotient of dimension-simple path geometry. The open problem is to construct a *color-sensitive* equivariant chain map that keeps enough of these exchanges to have the needed topological obstruction without identifying incompatible colored paths.

**Scope:** Theorems 1–2 are proved chain-level structural results and method-specific obstructions, not a proof of NORI1 or of the unified boundary-tournament conjecture.

#### Theorem 3 (root-slide repair of a boundary square exchange)

Let \(n\ge3\), and suppose a full antipodal geodesic \(P(x;i,j,\rho)\) has the monochromatic edge word \(t^n\). Exchange its first two dimensions, obtaining \(Q=P(x;j,i,\rho)\). The exchange affects only the first two edges, so let the word of \(Q\) be \((u,v,t,\ldots,t)\). The possibilities are:
\[
\begin{array}{c|c|c}
(u,v)&\text{root slides needed}&\text{result}\\
(t,t)&0&\text{monochromatic}\\
(1-t,t)&1&\text{monochromatic}\\
(1-t,1-t)&2&\text{monochromatic}\\
(t,1-t)&\text{no number of root slides}&\text{still nonmonochromatic}
\end{array}\tag{10}
\]
In the second row, one slide gives a full monochromatic geodesic rooted at \(x\oplus e_j\) with dimension order \((i,\rho,j)\). In the third, two slides give one rooted at \(x\oplus e_i\oplus e_j\), with order \((\rho,j,i)\). Every resulting path remains dimension-simple.

*Proof.* Root-slide transport rotates the edge word after position \(k\) by
\[
T^k(w_1,\ldots,w_n)=(w_{k+1},\ldots,w_n,1-w_1,\ldots,1-w_k)
\qquad(0\le k\le n).
\tag{11}
\]
Direct substitution proves the first three rows. In the fourth, \(Q\) has the word \((t,1-t,t,\ldots,t)\). Its antiperiodic cyclic comparison count, including the seam comparing the last letter with the complement of the first, equals three. This number is invariant under root slides, whereas a monochromatic word has cyclic comparison count one. Thus no root slide of \(Q\) can be monochromatic. \(\square\)

**A dimension-simple recovery in a coloring without monochromatic squares.** For even \(n=2m\ge4\), consider the legal NORI1 coloring
\[
c_i(y)=\sum_{k\ne i}y_k\pmod2.
\tag{12}
\]
Every square has opposite parallel edges of opposite colors, hence no square is monochromatic. A full geodesic from \(x\) is monochromatic precisely when the root bits read in its dimension order alternate. For any such geodesic, the opposite two-edge route obtained by swapping the first two dimensions has word \((1-t,1-t)\), while the unchanged suffix remains color \(t\): writing \(p=\sum_k x_k\), its original first edge has color \(p+x_i=t\), its second edge has color \(p+1+x_j=t\), so \(x_j=1-x_i\). The swapped first edge has color \(p+x_j=1-t\), and the next has color \(p+1+x_i=1-t\). Thus the **third row of (10)** repairs the exchange by moving the root through those two dimensions. In this family, simply retaining monochromatic adjacent-swap neighbors at a fixed root would find none, even though many monochromatic full geodesics exist.

Theorem 3 suggests incorporating *root slides as exchange corrections* rather than forbidding color-changing square swaps. The fourth row is a sharply identified remaining local obstruction: root slides preserve its three-change antiperiodic cyclic class. The theorem concerns the first two dimensions of a monochromatic complete path; extending such correction data to arbitrary internal exchanges and proving coherent higher-dimensional cancellation remains open.

#### Theorem 4 (matching obstruction to connectivity under root-sensitive boundary repairs)

Let \(n=2m\ge4\), and use the coloring (12). Consider a graph \(\mathcal G_c\) whose vertices are all monochromatic full antipodal geodesic flags \((x,\pi)\), with free roots and dimension orders. Permit path reversal \((x,\pi)\mapsto(\bar x,\pi^{\rm rev})\), antipodal translation \((x,\pi)\mapsto(\bar x,\pi)\), the two-root-slide correction at the first pair
\[
C(x;(i,j,\rho))=(x\oplus e_i\oplus e_j;(\rho,j,i)),
\tag{13}
\]
and its last-pair analogue obtained by conjugation with path reversal.

**Theorem.** The graph has at least
\[
\boxed{(n-1)!!=\frac{n!}{2^m m!}}
\tag{14}
\]
connected components. Every dimension permutation \(\pi\in S_n\) supports a monochromatic full geodesic from precisely two roots, so the graph has \(2n!\) vertices. No adjacent transposition of dimensions preserves monochromaticity at a fixed root.

*Proof.* In (12), the \(k\)-th edge bit of \(P(x,\pi)\) is \(|x|+x_{\pi_k}+k-1\pmod2\). Thus the geodesic is monochromatic if and only if the bits \(x_{\pi_1},\ldots,x_{\pi_n}\) alternate. For every permutation there are precisely two such root-bit assignments, namely \(0101\ldots01\) and \(1010\ldots10\). This gives \(2n!\) flags. Any adjacent exchange in an alternating word of length at least four creates a pair of equal adjacent bits, so no swap is monochromatic at the original root. Theorem 3 proves that \(C\) preserves monochromaticity, and reversal and antipodal translation also preserve it.

Define the perfect matching
\[
M(\pi)=\{\{\pi_1,\pi_2\},\{\pi_3,\pi_4\},\ldots,
\{\pi_{n-1},\pi_n\}\}.
\tag{15}
\]
Path reversal of an even-length word reverses its paired blocks. Antipodal translation leaves the word unchanged. The map \(C\) removes the first paired block and appends it in reversed order; its terminal analogue does the same at the other end. Consequently all permitted moves preserve \(M(\pi)\). Every perfect matching of \([n]\) occurs among monochromatic flags, since every permutation admits two such roots. There are \(n!/(2^m m!)\) perfect matchings, so different matchings lie in different components. \(\square\)

**Implication.** Root-sensitive boundary-square repairs can rescue monochromatic geodesics even though no square is monochromatic, but these moves alone cannot form a connected carrier of all favorable chambers. Any proposed color-sensitive replacement of the full Freudenthal chain must also relate distinct consecutive-pair matchings. That requires internal-square exchanges, perhaps through temporarily nonmonochromatic yet dimension-simple paths, or some additional homotopy-coherent correction. This result limits only the listed moves, not all possible root-changing operations.

#### Sharp odd-dimensional square-curvature systole and reversal transgression

Let \(c_i(x)\in\mathbb F_2\) be the color of the undirected direction-\(i\) edge at \(x\), obeying \(c_i(x\oplus e_i)=c_i(x)\) and \(c_i(\bar x)=1\oplus c_i(x)\). For \(i\ne j\), let
\[
\kappa_{ij}(x)=c_i(x)\oplus c_j(x\oplus e_i)\oplus c_i(x\oplus e_j)\oplus c_j(x)
\tag{RT1}
\]
be the parity of colors around the \(ij\)-square through \(x\). It is independent of which of the four corners is chosen, and \(\kappa_{ij}(\bar x)=\kappa_{ij}(x)\). Call a square *curved* if its curvature equals one.

For a permutation \(\pi=(p_1,\ldots,p_n)\) and root \(x\), write \(I_x(\pi)\) for the XOR of colors along the full geodesic starting at \(x\) with direction order \(\pi\).

**Theorem (triangular reversal transgression).** For every \(n\ge2\), every legal coloring, every root \(x\), and every direction order \(\pi\),
\[
\boxed{
\bigoplus_{1\le a<b\le n}
\kappa_{p_a p_b}\left(x\oplus
\bigoplus_{a<k<b}e_{p_k}\right)
=n\bmod 2.}\tag{RT2}
\]
For odd \(n\), the indicated collection of \(\binom n2\) squares contains an odd number of curved squares, hence at least one, for every root and every order.

*Proof.* Reverse a full geodesic from \(x\) to \(\bar x\), then translate it antipodally. The resulting path starts again at \(x\), uses the reversed direction order, and its edges are antipodal translates of the original edges. Thus
\[
I_x(\pi^{\rm rev})=I_x(\pi)\oplus(n\bmod2).
\tag{RT3}
\]
Transform \(\pi\) into \(\pi^{\rm rev}\) by moving \(p_1\) successively past all later directions, then \(p_2\) past its remaining later directions, and so forth. This is a sequence of \(\binom n2\) adjacent swaps, each unordered direction pair appearing once. At the swap of \(p_a,p_b\), \(a<b\), the directions preceding this pair are precisely \(p_{a+1},\ldots,p_{b-1}\). The two full geodesics before and after the swap share every edge except the two alternative routes through the corresponding square, so their path-color parities differ by the square curvature in (RT2). XORing these swaps telescopes to (RT3), establishing (RT2). \(\square\)

**Theorem (sharp universal curvature bound).** If \(n\ge3\) is odd, every legal coloring has at least
\[
\boxed{2^{n-2}\text{ curved elementary squares},\qquad
2^{n-3}\text{ antipodal pairs of curved squares}.}\tag{RT4}
\]
The bound is attained in every odd dimension. In every even dimension \(n\ge2\), there exists a legal coloring with zero curved squares.

*Proof.* Fix a direction order \(\pi\) and let \(x\) range uniformly over all \(2^n\) roots. In (RT2) one square is sampled from each unordered pair of directions \(\{i,j\}\). For each such pair, the sampled square is uniformly distributed over its \(2^{n-2}\) faces, because \(x\) is uniform. Write \(q_{ij}\) for the number of curved \(ij\)-squares. For odd \(n\), (RT2) gives at least one curved square for every root \(x\), hence
\[
1\le\mathbb E_x \sum_{a<b}
\kappa_{p_ap_b}\Bigl(x\oplus\bigoplus_{a<k<b}e_{p_k}\Bigr)
=\sum_{i<j}\frac{q_{ij}}{2^{n-2}}.
\]
Therefore \(\sum_{i<j}q_{ij}\ge2^{n-2}\). As curvature is invariant under antipodality and \(n\ge3\), each curved square has a distinct curved antipodal partner, yielding the orbit count.

For sharpness, put \(n=2k+1\) and define
\[
c_{2r}(x)=x_{2r+1},\qquad c_{2r+1}(x)=x_{2r}
\quad(0\le r<k),
\qquad c_{2k}(x)=x_0.
\tag{RT5}
\]
Every rule ignores its own bit and flips under global complementation. Its curvature vanishes in all direction pairs except \(\{0,2k\}\), where it equals one identically. Thus precisely \(2^{n-2}\) squares are curved. For even \(n=2k\), use only the paired-reader rules, without the last rule; their cross-derivative matrix is symmetric, so every square curvature vanishes. \(\square\)

**Constructive interpretation.** Formula (RT2) provides a deterministic search for an odd-curvature square using at most \(\binom n2\) square examinations, from any chosen root and direction order, whenever \(n\) is odd. No assumption about the distribution of good geodesics is involved. It also shows the lower bound is attained only if the reversal sweep encounters a single curved square for every root and order; this is a necessary condition for equality, not a classification.

**Computational cross-check.** Minimizing the number of curved square orbits by integer linear optimization over the independent antipodal edge-orbit coloring bits gives minima \(1\) for \(Q_3\) and \(4\) for \(Q_5\), in agreement with (RT4). In each case the optimizer confirms matching lower and upper bounds. An independent checker verified (RT2) on 1500 randomized legal colorings, roots, and orders for each \(n=3,4,5,6,7\), including the even-dimensional zero-parity identity. The proof above is dimension-uniform and does not depend on these calculations.

**Relation to the open problem.** The forced defect is local and direction-labelled: every odd-dimensional legal coloring has at least a \(1/\binom n2\) fraction of all squares carrying odd curvature, with equality possible. This does not by itself force a monochromatic full antipodal geodesic, but supplies a sharp parity/curvature constraint independent of reachability and component holonomy.


#### Complete curvature-code realizability and antipodal vertex gauges

Let \(n\ge2\), and write \(\tau x=\bar x\) for cube antipodality. Use \(\mathbb F_2\)-valued cubical cochains. Let \(p(x)=\sum_i x_i\bmod2\), so that \(\delta p\) is the constant-one edge cochain and \(p(\bar x)\oplus p(x)=n\bmod2\). A legal coloring is a cubical edge cochain \(c\) with
\[
\tau^*c=c\oplus\delta p.
\tag{CR1}
\]
Its curvature is the square cochain \(\kappa=\delta c\).

For any square cochain \(\kappa\), define the reversal pairing \(T_{x,\pi}(\kappa)\) as the left side of (RT2), the XOR of one square curvature for each unordered direction pair along the bubble reversal of order \(\pi\) from root \(x\).

**Theorem (complete curvature-code characterization).** A binary assignment \(\kappa\) to the elementary squares of \(Q_n\) arises as the curvature of a legal antipodally odd edge coloring if and only if all three conditions hold:

1. \(\tau^*\kappa=\kappa\) (opposite squares have equal values);
2. \(\delta\kappa=0\) (the XOR of its six face values on every elementary 3-cube is zero);
3. \(T_{x,\pi}(\kappa)=n\bmod2\) for one root \(x\) and one direction order \(\pi\).

Under the first two conditions, \(T_{x,\pi}(\kappa)\) is independent of the root and direction order, so the last condition may equivalently be imposed for every root and order. Given a valid \(\kappa\), a legal coloring realizing it can be constructed by cubical integration and one antipodal vertex-pair assignment.

*Proof.* Necessity follows from \(\kappa=\delta c\), the identity \(\delta^2=0\), and (RT2). Conversely, assume the first two conditions. The cubical complex of \(Q_n\) is contractible, so every closed square cochain is the coboundary of an edge cochain: choose \(a\) with \(\delta a=\kappa\). By opposite-square invariance,
\[
\delta(a\oplus\tau^*a)=\kappa\oplus\tau^*\kappa=0.
\]
Again cubical contractibility supplies a vertex function \(\phi\) satisfying
\[
a\oplus\tau^*a=\delta\phi.
\tag{CR2}
\]
Applying \(\tau\) shows \(\delta(\phi\oplus\tau^*\phi)=0\), so
\[
\phi(x)\oplus\phi(\bar x)=\alpha
\tag{CR3}
\]
for one constant \(\alpha\in\mathbb F_2\).

For any root and order, the XOR of path integrals of \(a\) along the order and its reversal equals the integral of \(a\oplus\tau^*a\) along the original path, which telescopes via (CR2) to \(\phi(x)\oplus\phi(\bar x)=\alpha\). Reversing the order by adjacent swaps, as in the proof of (RT2), shows \(T_{x,\pi}(\kappa)=\alpha\), independent of \(x,\pi\). By condition 3, \(\alpha=n\bmod2\).

Now \(g=\phi\oplus p\) is invariant under antipodality, because \(g(x)\oplus g(\bar x)=\alpha\oplus n=0\). Choose a vertex function \(h\) satisfying
\[
h(x)\oplus h(\bar x)=g(x).
\tag{CR4}
\]
This is always possible: assign \(h\) arbitrarily at one vertex of each antipodal pair and use (CR4) to determine its mate. Define \(c=a\oplus\delta h\). Then \(\delta c=\kappa\), while
\[
c\oplus\tau^*c
=\delta\phi\oplus\delta(h\oplus\tau^*h)
=\delta\phi\oplus\delta(\phi\oplus p)
=\delta p.
\]
Hence \(c\) is legal. \(\square\)

**Theorem (gauge fibers and curvature-code dimension).** Two legal colorings \(c,c'\) have the same curvature if and only if
\[
\boxed{c'=c\oplus\delta h,\qquad h(x)\oplus h(\bar x)=\epsilon}
\tag{CR5}
\]
for some vertex function \(h\) and a constant \(\epsilon\in\mathbb F_2\). Every admissible curvature pattern is realized by
\[
\boxed{2^{2^{n-1}}}
\tag{CR6}
\]
different legal edge colorings. Their complete-path color parities agree up to the common phase \(\epsilon\), recovering the parity-transport theorem of the companion Coxeter Subsection from the vertex gauge.

The set \(\mathcal K_n\) of realizable curvatures is therefore an affine binary code of dimension
\[
\boxed{\dim\mathcal K_n=n2^{n-2}-2^{n-1}.}
\tag{CR7}
\]
For \(n\ge3\) this code is naturally represented on \(\binom n2 2^{n-3}\) antipodal square orbits. In particular, for \(n=5\) it has length 40, dimension 24, and \(2^{24}=16{,}777{,}216\) patterns.

*Proof.* If \(\delta c=\delta c'\), their difference \(b=c\oplus c'\) is a closed edge cochain. Contractibility supplies \(b=\delta h\). Both colorings are legal, hence \(\tau^*b=b\); thus \(\delta(h\oplus\tau^*h)=0\), forcing \(h(x)\oplus h(\bar x)=\epsilon\) constant. Conversely every such \(h\) gives a legal difference with zero square curvature, proving (CR5).

There are \(2^{n-1}\) antipodal vertex pairs. For each chosen \(\epsilon\), the function \(h\) is free on one vertex from each pair, giving \(2^{2^{n-1}}\) potentials. There are two choices of \(\epsilon\). The kernel of \(\delta\) on vertex functions consists of the two constant functions \(h=0,1\), which yield the same edge difference. Thus the number of distinct allowed edge differences is \(2\cdot2^{2^{n-1}}/2=2^{2^{n-1}}\). Since the space of legal colorings has \(n2^{n-2}\) independent antipodal edge-orbit bits, its curvature image has dimension \(n2^{n-2}-2^{n-1}\). This proves (CR6)--(CR7). Integrating \(\delta h\) along any full antipodal geodesic yields \(h(x)\oplus h(\bar x)=\epsilon\), showing the common parity phase. \(\square\)

**Finite equality-class audit in dimension five.** The curvature code \(\mathcal K_5\) has length 40 and dimension 24, as in (CR7). Exhaustive enumeration of all \(2^{24}\) code members by Gray-code updates gave minimum weight four and precisely ten minimum-weight members. Each of these ten members is the indicator of all four antipodal square orbits in a single direction pair; there is one for each of the ten unordered direction pairs. Thus the sharp bound (RT4) has only the single-direction-pair curvature patterns as equality cases in \(Q_5\). This is a finite statement, not an assertion of analogous rigidity in every odd dimension.

**Interpretation.** The full local consistency conditions on the curvature are sufficient, once the single reversal-phase bit is imposed. The resulting affine code and antipodal gauge normal form are valid for unrestricted nonlinear legal colorings. Curvature determines the parity of every full geodesic up to a common bit, but it does not determine which geodesics are monochromatic; the finer path-color words vary under the vertex gauges.


#### Rigidity of all curvature minimizers in odd dimension

Let \(n\ge3\) be odd, and retain the curvature \(\kappa_{ij}(x)\), the reversal sum (RT2), the curvature lower bound (RT4), and the legal-coloring gauge-fiber theorem (CR5)--(CR7). Call the *direction type* of an elementary square its unordered pair of varying directions.

**Lemma (two prescribed square types can be synchronized).** Let \(F\) and \(G\) be arbitrary elementary squares with distinct direction types \(p=\{a,b\}\) and \(q=\{c,d\}\). There exist a root \(x\in Q_n\) and a direction permutation \(\pi\in S_n\) for which the reversal collection of (RT2) contains both \(F\) and \(G\).

*Proof.* For every square type \(\{i,j\}\), specify a square by its fixed bits outside \(\{i,j\}\); the two varying bits are immaterial. During the bubble reversal of \(\pi\), the square corresponding to the pair of directions \(i=p_u,j=p_v\), \(u<v\), has the same fixed bits as the vertex
\[
x\oplus\bigoplus_{u<r<v}e_{p_r}.
\tag{RR1}
\]
This is the sampling formula in (RT2).

First assume \(p,q\) are disjoint. Label their members so that \(p=\{a,b\}\), \(q=\{c,d\}\). Choose
\[
\pi=(a,b,c,\ T,\ d,\ U),
\tag{RR2}
\]
where \(T\sqcup U=[n]\setminus\{a,b,c,d\}\), and \(T\) is a freely chosen ordered subset. The \(p\)-square in the reversal collection is sampled at \(x\), and the \(q\)-square at \(x\oplus\mathbf1_T\). For each direction outside \(p\cup q\), put that direction in \(T\) if the prescribed fixed bits of \(F\) and \(G\) disagree, and in \(U\) otherwise. Now choose \(x\) to match the prescribed fixed bits of \(F\) outside \(p\), and the prescribed fixed bits of \(G\) in \(p\). No conflicts remain: \(G\) ignores the bits \(c,d\), \(F\) ignores \(a,b\), and \(T\) resolves every bit outside their union.

If \(p,q\) share one member, relabel so that \(p=\{a,b\}\), \(q=\{a,c\}\). Choose
\[
\pi=(b,a,\ T,\ c,\ U),
\tag{RR3}
\]
with \(T\sqcup U=[n]\setminus\{a,b,c\}\). Again the \(p\)-square is sampled at \(x\) and the \(q\)-square at \(x\oplus\mathbf1_T\). Put a direction in \(T\) precisely when the two prescribed squares have different fixed bits in that direction. The remaining bits can be assigned independently: \(F\) ignores \(a,b\), \(G\) ignores \(a,c\), and the only jointly constrained directions are those outside \(\{a,b,c\}\). Thus the prescribed squares appear together. \(\square\)

**Theorem (global rigidity at the sharp curvature threshold).** If a legal antipodally odd coloring \(c\) of odd-dimensional \(Q_n\), \(n\ge3\), has \(2^{n-2}\) curved squares, then there is a unique unordered pair of directions \(p=\{i,j\}\) such that
\[
\boxed{\kappa(F)=\mathbf1_{\{\operatorname{type}(F)=p\}}.}
\tag{RR4}
\]
Conversely every pair \(p\) is realized by legal colorings attaining this bound. Thus the minimum-weight words of the affine curvature code \(\mathcal K_n\) are precisely the \(\binom n2\) words supported on all squares of one direction type.

*Proof.* For every root and order, the integer-valued reversal count
\[
X_c(x,\pi)
=\sum_{1\le u<v\le n}
\kappa_{p_up_v}\left(x\oplus\bigoplus_{u<r<v}e_{p_r}\right)
\tag{RR5}
\]
is odd by (RT2), hence at least one. Fix an arbitrary order \(\pi\). As \(x\) is uniformly distributed, the summand for each pair of directions is uniformly sampled among its \(2^{n-2}\) elementary squares. If \(c\) has the sharp number \(2^{n-2}\) of curved squares, then
\[
\mathbb E_x X_c(x,\pi)
=\frac{\#\{\text{curved squares}\}}{2^{n-2}}=1.
\]
A positive integer-valued random variable bounded below by one with mean one is identically one. Consequently \(X_c(x,\pi)=1\) for every root and order.

Suppose curvature were nonzero on two squares \(F,G\) of distinct direction types. By the synchronization lemma there exist \(x,\pi\) whose reversal collection includes both. Then \(X_c(x,\pi)\ge2\), contradiction. Therefore nonzero curvature is supported in only one direction type \(p\). There are precisely \(2^{n-2}\) squares of that type, and the assumed total of curved squares is also \(2^{n-2}\); every square of type \(p\) must therefore be curved. The sharp constructions of (RT5), after permuting direction names, realize this curvature for any prescribed unordered pair. \(\square\)

**Corollary (complete enumeration and gauge normal form).** For odd \(n\ge3\), the number of legal antipodally odd \(Q_n\) edge colorings attaining the minimum curvature \(2^{n-2}\) is
\[
\boxed{\binom n2\,2^{2^{n-1}}.}
\tag{RR6}
\]
Modulo legal vertex-potential transformations \(c\mapsto c\oplus\delta h\), with \(h(x)\oplus h(\bar x)\) constant, there are precisely \(\binom n2\) minimum-curvature classes, distinguished by their unique curved direction pair. Each class has an explicit affine representative from (RT5), with direction names permuted, and the complete family of its representatives is given by (CR5).

*Proof.* The theorem gives \(\binom n2\) admissible minimum-curvature patterns. By the previously proved gauge-fiber theorem (CR6), each pattern is realized by \(2^{2^{n-1}}\) different legal colorings. Distinct patterns are disjoint fibers, and within a fiber the gauge group acts transitively. Multiplication gives (RR6). \(\square\)

**Audit.** The square synchronization lemma was checked independently for every pair of distinct square types and every pair of specified elementary squares in dimensions \(3,4,5,6\), respectively \(12,240,2880,26880\) choices; all choices admitted the explicit root and order prescribed in (RR2)--(RR3). This supplies an independent finite check of the combinatorial lemma, though its proof is unrestricted. The \(n=5\) conclusion agrees with the earlier exhaustive enumeration of all \(2^{24}\) curvature-code words: precisely ten minimum-weight words, one per direction pair.

**Significance.** The earlier numerical curvature lower bound is rigid in every odd dimension, even for arbitrarily nonlinear colorings: minimum curvature forces its entire support onto one complete family of parallel square faces. This is a full-class theorem, not a restricted coloring construction. It does not assert that the resulting colorings have a prescribed number of monochromatic full geodesics, because legal vertex gauges can alter their color words while preserving curvature.


**Corollary (constructive curvature-complexity dichotomy).** Let \(n\ge3\) be odd and let \(c\) be any legal antipodally odd coloring. One of the following mutually exclusive cases holds:

(i) Its curvature is the complete indicator of a single direction pair, and \(c\) attains the sharp minimum \(2^{n-2}\) curved squares;

(ii) There exist a root \(x\) and a permutation \(\pi\) whose \(\binom n2\)-square reversal sweep (RT2) contains at least three curved squares.

Given the list of curved elementary squares, a witness \((x,\pi)\) in case (ii) can be constructed in \(O(n)\) operations from any two curved squares of distinct direction types using the synchronization lemma (RR2)--(RR3).

*Proof.* If curvature is supported on just one direction pair \(p=\{i,j\}\), select an order starting with \(i,j\). The reversal parity identity (RT2) then reduces to \(\kappa_{ij}(x)=1\) for every root \(x\). Therefore every square of type \(p\) is curved and case (i) holds. If at least two direction types occur, choose a curved square from each. The synchronization lemma produces one root and order whose reversal sweep contains both. The number of curved squares in that sweep is odd by (RT2), so it must be at least three. Cases (i) and (ii) are exclusive because any sweep under case (i) contains just one curved square. \(\square\)

This dichotomy concerns individual root-and-order witnesses and does not posit collective path behavior. It also gives a deterministic way to distinguish a curvature minimizer from a non-minimizer once square curvature has been computed.


#### Vertex-gauge path-word laws within a fixed curvature fiber

Fix \(n\ge2\) and any realizable square-curvature pattern \(\kappa\). By the reconstruction theorem, any legal coloring \(c'\) of curvature \(\kappa\) is \(c'=c\oplus\delta h\) with \(h(\bar u)=h(u)\oplus\epsilon\) for a common bit \(\epsilon\); the fiber has \(2^{2^{n-1}}\) members.

**Theorem (uniform complete-path word).** For any fixed full antipodal geodesic \(P\) and any target color word \(s\in\mathbb F_2^n\), a uniformly chosen legal coloring with curvature \(\kappa\) satisfies
\[
\boxed{\Pr[w_{c'}(P)=s\mid\kappa]=2^{-n}.}\tag{VG1}
\]
*Proof.* If \(P=(v_0,\ldots,v_n=\bar v_0)\), its first \(n\) vertices represent distinct antipodal vertex pairs: its proper direction-prefix sets are nested and never complementary. The gauge changes the \(j\)-th edge color by \(h(v_{j-1})\oplus h(v_j)\). Values of \(h\) at these \(n\) representatives may be selected independently, together with \(\epsilon=h(v_n)\oplus h(v_0)\). Given any \(n\) desired edge-color changes, choose \(h(v_0)\), propagate the changes along the path, and choose \(\epsilon\) for its last edge. Each target has the same number of preimages. \(\square\)

**Theorem (joint word criterion using antipodal vertex-pair graph).** Let \(\mathcal P\) be a nonempty family of full geodesics, with a prescribed binary color \(t_e\) on every selected edge occurrence. Form the multigraph \(H\) whose vertices are the antipodal vertex pairs \([u]=\{u,\bar u\}\) visited by these paths; every selected edge occurrence \(e=uv\) joins \([u]\) and \([v]\). Choose one reference representative \(r([u])\) of each vertex pair, and let \(\sigma(u)\) be zero if \(u=r([u])\), or one otherwise. Label every selected edge occurrence by
\[
\lambda_e=\sigma(u)\oplus\sigma(v),\qquad
d_e=c(e)\oplus t_e.
\tag{VG2}
\]
The prescribed colors can all be realized simultaneously by some coloring of curvature \(\kappa\) if and only if there exists a single bit \(\epsilon\) such that every cycle \(C\) of this multigraph, including parallel-edge two-cycles, satisfies
\[
\boxed{\bigoplus_{e\in C}d_e
=\epsilon\bigoplus_{e\in C}\lambda_e.}\tag{VG3}
\]
Let \(v(H)\) and \(k(H)\) be its vertex and connected-component counts. If (VG3) holds then
\[
\boxed{\Pr[\text{all specified colors}\mid\kappa]
=2^{-(v(H)-k(H)+1)};}
\tag{VG4}
\]
otherwise the probability is zero.

*Proof.* Write an arbitrary legal potential as \(h(u)=z_{[u]}\oplus\epsilon\sigma(u)\), using independent bits \(z_{[u]}\) on antipodal vertex pairs. The edge constraints are
\[
z_{[u]}\oplus z_{[v]}\oplus\epsilon\lambda_e=d_e.
\tag{VG5}
\]
For fixed \(\epsilon\), these are graph-potential equations, soluble if and only if the sums around all cycles vanish. A projected full antipodal geodesic is a closed walk of voltage \(\oplus\lambda_e=\sigma(v_0)\oplus\sigma(\bar v_0)=1\). Hence at least one cycle of \(H\) has odd voltage, and the compatible value of \(\epsilon\), if any, is unique. Every connected component then contributes one free potential bit; unused antipodal vertex pairs remain unconstrained. With \(V=2^{n-1}\) total antipodal vertex pairs, there are \(2^{V-v(H)+k(H)}\) satisfying potential assignments among \(2^{V+1}\) assignments including \(\epsilon\). Potentials differing by a global constant induce the same edge gauge, so this ratio is also the probability among the distinct colorings in the fixed curvature fiber. \(\square\)

**Corollaries.** Every curvature fiber satisfies
\[
\boxed{\mathbb E N_R=n!,\qquad \mathbb E N_M=2n!,}
\tag{VG6}
\]
where \(N_R\) counts rooted red full geodesics and \(N_M\) counts rooted full geodesics monochromatic in either color; there are \(2^n n!\) rooted geodesics and their respective event probabilities are \(2^{-n}\) and \(2^{1-n}\). Thus each curvature fiber contains at least one coloring with \(N_R\ge n!\), without implying the NORI1 assertion for every member.

If two full geodesics \(P,Q\) visit disjoint sets of antipodal vertex pairs, and the representative \(c\) gives path color parities \(p(P),p(Q)\), then
\[
\boxed{\Pr[P,Q\text{ both red}\mid\kappa]
=\begin{cases}
2^{1-2n},&p(P)=p(Q),\\
0,&p(P)\ne p(Q).
\end{cases}}
\tag{VG7}
\]
They are correlated through the common antipodal phase even though the two paths share no antipodal vertex pair.

Finally, for every realizable \(\kappa\), any collection of fewer than \(2^{n-1}\) predetermined rooted full geodesics can simultaneously be made nonmonochromatic by some legal coloring in that same curvature fiber. Indeed the union bound and (VG1) give a probability less than one of any selected path being monochromatic.

The signed graph construction gives an unrestricted joint-law description, not an argument that every individual member of a curvature fiber possesses a monochromatic full geodesic. A verification program checked the Boolean potential rank and joint-word probabilities by exhaustive gauge enumeration on random path collections for dimensions 2--4, and by algebraic rank checks through dimension 8.


#### Independent adjacent-order repairs within a fixed curvature class

Let \(n\ge4\), and let \(P=(v_0,v_1,\ldots,v_n=\bar v_0)\) be a red full antipodal geodesic in an arbitrary legal coloring \(c\). Let \(\pi=(p_1,\ldots,p_n)\) be its direction order. For \(1\le r<n\), let \(P^{(r)}\) be the path with directions \(p_r,p_{r+1}\) interchanged, and put
\[
y_r=v_{r-1}\oplus e_{p_{r+1}},\qquad
F_r=\{v_{r-1},v_r,v_{r+1},y_r\}.
\tag{LS1}
\]
Thus \(F_r\) is the square used by the \(r\)-th adjacent exchange, and \(y_r\) is its corner outside the original path. Let \(J=\{r:\kappa(F_r)=0\}\), with \(f=|J|\).

**Theorem (independent local exchange control).** For every subset \(A\subseteq J\), there exists a legal coloring \(c_A\) with precisely the same square curvature as \(c\) such that:

1. \(P\) is still red under \(c_A\);
2. for \(r\in J\), the exchanged path \(P^{(r)}\) is red under \(c_A\) if and only if \(r\in A\);
3. for \(r\notin J\), \(P^{(r)}\) is never red under any legal coloring with the same curvature that keeps \(P\) red.

All \(2^f\) configurations are realized by commuting vertex-potential moves supported on the antipodal pairs \(\{y_r,\bar y_r\}\). Furthermore, if \(c'\) is uniformly distributed over the entire curvature fiber conditioned on \(P\) being red, the indicators
\[
\left(\mathbf1_{\{P^{(r)}\text{ red under }c'\}}\right)_{r\in J}
\]
are independent fair Bernoulli bits. Consequently
\[
\boxed{\#\{r:P^{(r)}\text{ red}\}\sim\operatorname{Binomial}(f,1/2).}
\tag{LS2}
\]
In a curvature fiber of size \(2^{2^{n-1}}\), there are \(2^{2^{n-1}-n}\) colorings keeping \(P\) red and
\[
\boxed{2^{2^{n-1}-n-f}}
\tag{LS3}
\]
colorings realizing each prescribed local exchange configuration.

*Proof.* Along a square \(F_r\), the two original edges used by \(P\) are red. Their two alternate edges consequently have equal colors if \(\kappa(F_r)=0\), or opposite colors if \(\kappa(F_r)=1\). Thus an odd-curvature exchange cannot be red while \(P\) stays red.

For the zero-curvature case, define a vertex potential \(h_r\) equal to one precisely on \(\{y_r,\bar y_r\}\), and zero elsewhere. It obeys \(h_r(\bar u)=h_r(u)\). Its gradient is a legal curvature-preserving recoloring. It toggles both alternate edges at \(y_r\), and no edge of the original path, provided \(y_r,\bar y_r\) lie outside \(P\).

We now prove all \(n-1\) unused corners belong to distinct antipodal vertex pairs, none meeting \(P\), when \(n\ge4\). Translate the root to zero and rename the path directions \(0,\ldots,n-1\). The path vertices are the nested prefixes \(S_t=\{0,\ldots,t-1\}\), while
\[
y_r=\{0,\ldots,r-2\}\cup\{r\},\qquad 1\le r<n.
\tag{LS4}
\]
Each \(y_r\) differs from every path vertex: it has a gap at \(r-1\) and an included bit at \(r\). It also differs from every complement of a path vertex: it is neither empty nor full, contains bit zero when \(r\ge2\), and the case \(r=1\) is a singleton that is not a terminal suffix. For \(r<s\), the two \(y_r,y_s\) are distinct. If \(s\ge r+2\), both contain bit \(r\), so they are not complements. If \(s=r+1\), then either \(r\ge2\), in which case both contain bit zero, or \(r=1\), in which case \(n\ge4\) supplies a bit outside \(\{0,1,2\}\) omitted by both. Hence the \(y_r\) represent distinct antipodal vertex pairs. The moves \(h_r\) are therefore independently selectable, commute, and do not affect any other exchanged path's two alternative edges. Choosing their coefficients prescribes the indicators at every flat square and proves the first three assertions.

For the distribution, the curvature-fiber vertex-gauge theorem shows that conditioning on \(P\) red leaves \(2^{2^{n-1}-n}\) colorings; along a path with \(n\) distinct antipodal vertex-pair representatives, the \(n\) red-edge constraints are independent. They impose zero antipodal phase on the gauge from the fixed red representative, and the remaining vertex-pair potential variables include independent bits for each \(y_r\), modulo an irrelevant global potential. Changing each such bit toggles only the corresponding adjacent-exchange status. Hence every one of the \(2^f\) status configurations has equally many colorings, giving (LS2)--(LS3). \(\square\)

**The exceptional three-cube.** In \(Q_3\), the two unused corners of the two adjacent direction swaps are antipodal: for the reference order \((0,1,2)\), they are \(e_1\) and \(e_0\oplus e_2=\bar e_1\). Thus the two repairs are controlled by the same vertex-gauge bit after conditioning on \(P\) red. They need not be independently selectable. An explicit legal edge-orbit mask \(\texttt{0x14}\), using antipodal edge orbits introduced by scanning the edges by smaller endpoint and then direction, has the reference path \(0\to1\to3\to7\) red and both exchange squares flat; one adjacent swap is red and the other is not. In its curvature fiber, retaining the reference path red permits only the two exchange-status patterns \((1,0)\) and \((0,1)\), never \((0,0)\) or \((1,1)\). This is a sharp counterexample to extending local independence to dimension three.

**Independent checks.** A standalone test script enumerated all \(2^6=64\) legal \(Q_3\) colorings and \(2^{16}=65536\) legal \(Q_4\) colorings under the reference-order root. There are respectively 8 and 4096 assignments for which that prescribed full path is red. Every one of these passed the local exchange theorem and its claimed exceptional behavior. Additional random legal coloring checks confirmed distinct antipodal repair corners in dimensions five, six, and seven. The proof above applies without dimension bound.

**Significance.** This is a direct operation on full, direction-simple geodesics across legal colorings in the same curvature fiber. It determines the complete local red-exchange neighborhood of a prescribed red path, and shows that the zero-curvature swaps can be switched independently. It does not infer a red full path in an arbitrary fixed coloring, and its recoloring operation is not a path modification within the original coloring.


#### Every curvature fiber has abundant red-rooted full geodesics

Fix \(n\ge2\), a realizable square-curvature cochain \(\kappa\), and a vertex \(x\). Let \(c\) be uniform among legal antipodally odd edge colorings with curvature \(\kappa\), and let \(N_x(c)\) count red full antipodal geodesics rooted at \(x\). Define
\[
A_0=1,\quad A_n=\sum_{j=1}^n j!A_{n-j},\quad
D_n=A_n/n!=\frac1{n!}\sum_{d_1+\cdots+d_r=n,\ d_i\ge1}\prod_i d_i!.
\tag{SG1}
\]
The sum is over ordered compositions.

**Theorem (curvature-uniform rooted second moment).** For every curvature fiber and root,
\[
\boxed{\mathbb E N_x=n!2^{-n},\qquad
\mathbb E N_x^2\le(n!2^{-n})^2(4D_n-2),}
\tag{SG2}
\]
and therefore
\[
\boxed{\Pr(N_x>0)\ge(4D_n-2)^{-1}\ge1/6.}
\tag{SG3}
\]
Moreover \(D_n=1+2/n+O(n^{-2})\), yielding
\[
\boxed{\Pr(N_x>0)\ge1/2-2/n+O(n^{-2}).}
\tag{SG4}
\]
The leading constant one half is asymptotically optimal for bounds uniform over the curvature and chosen root.

*Proof.* The uniform single-path gauge law (VG1) gives probability \(2^{-n}\) for each of the \(n!\) paths. For two paths \(P,Q\) sharing \(t(P,Q)\) antipodal vertex pairs, their quotient union graph is connected and contains \(2n-t(P,Q)\) vertices. The full signed-quotient joint-word criterion (VG3)--(VG4) gives
\[
\Pr(P,Q\text{ both red})\in\{0,2^{-(2n-t(P,Q))}\},
\tag{SG5}
\]
depending on compatibility.

Fix \(P\) to be the direction order \((1,\ldots,n)\), with nontrivial prefix sets \(S_k=\{1,\ldots,k\}\). For random \(Q\), let \(T_k\) be its prefix sets. Put \(a=\#\{k:T_k=S_k,\ 1\le k<n\}\), and \(b=\#\{k:T_{n-k}=[n]\setminus S_k,\ 1\le k<n\}\). The shared antipodal vertex-pair count is
\[
t(P,Q)=1+a+b,\qquad ab=0.
\]
Both match types cannot coexist, because a nontrivial initial segment of \((1,\ldots,n)\) is incomparable with every nontrivial terminal segment, whereas the prefixes of \(Q\) are nested. Reversing \(Q\) exchanges the laws of \(a,b\). Therefore
\[
\mathbb E2^{t(P,Q)}=2\mathbb E(2^a+2^b-1)
=4\mathbb E2^a-2.
\tag{SG6}
\]
Expand \(2^a=\prod_{k=1}^{n-1}(1+\mathbf1_{\{T_k=S_k\}})\). Every subset of the matched ranks partitions \((1,\ldots,n)\) into consecutive blocks of lengths \(d_1,\ldots,d_r\). The probability of those rank constraints is \(\prod_i d_i!/n!\), because \(Q\) may permute within each block. Hence \(\mathbb E2^a=D_n\). Combining this with (SG5)--(SG6) proves (SG2). Cauchy--Schwarz yields \(\Pr(N_x>0)\ge(\mathbb E N_x)^2/\mathbb E N_x^2\), proving (SG3).

The composition recurrence gives
\[
D_n=1+\sum_{j=1}^{n-1}\frac{D_{n-j}}{\binom nj}.
\]
Its first six terms are \(1,3/2,11/6,47/24,77/40,1303/720\). For \(n\ge7\), the reciprocal-binomial sum is less than \(1/2\) and decreases with \(n\); induction yields \(D_n\le2\), establishing the bound \(1/6\). The reciprocal sum is \(2/n+O(n^{-2})\), giving \(D_n=1+2/n+O(n^{-2})\), and therefore (SG4).

For sharpness, take even \(n\) and the flat curvature fiber \(\kappa=0\), which exists by the paired-reader construction. Every coloring in this fiber is a gradient \(\delta h\), with antipodal law \(h(\bar u)\oplus h(u)=|u|\bmod2\oplus\alpha\), where \(\alpha\) is one binary phase. A red full geodesic from \(x\) requires its endpoint potential values to agree, hence requires \(\alpha=|x|\bmod2\). Adding a constant-one edge cochain in any one direction preserves curvature and toggles \(\alpha\); consequently half of the fiber forbids a red full geodesic from \(x\). This upper bound of \(1/2\) along even dimensions combines with (SG4) to establish asymptotic optimality. \(\square\)

**Finite audit.** A standalone program nori_curvature_fiber_secondmoment.py independently enumerates all relative direction orders for \(2\le n\le9\), verifying \(\mathbb E2^t=4D_n-2\) against the recurrence. For \(Q_4\), exhaustive testing of all 256 colorings in each of a flat and a nonflat curvature fiber gives red-rooted success rates \(98/256\) and \(192/256\), respectively, and mean rooted red-geodesic count \(24/16=3/2\) in both cases. The theorem is unrestricted in the coloring rules and curvature pattern, but its probability bound does not assert a red geodesic for every individual member of a fiber.


#### Antipodal vertex-star gauges and critical geodesic transversals

For a legal antipodally odd coloring \(c\) of \(Q_n\), \(n\ge2\), and an antipodal vertex pair \(U=\{u,\bar u\}\), let \(h_U\) be one on both vertices of \(U\) and zero elsewhere, and define \(T_U(c)=c\oplus\delta h_U\). This flips all edges incident to \(U\), and preserves legality and all square curvatures. By the curvature-gauge theorem, each fixed-curvature fiber splits into two star-flip components, one for each value of the constant \(\epsilon=h(v)\oplus h(\bar v)\).

**Theorem (each star component has a red full-geodesic witness).** Every star-flip component, in every realizable curvature fiber, contains a coloring with a red full antipodal geodesic.

*Proof.* Take any coloring \(c\) in the component and any rooted full geodesic with color word \(a_1,\ldots,a_n\). Moving its first direction to the end while shifting its starting vertex across that first edge gives another full geodesic with word \(a_2,\ldots,a_n,1\oplus a_1\). The two words have opposite parity. Choose the path with even color parity, written \(P=(v_0,\ldots,v_n=\bar v_0)\). Set \(h(v_0)=0\) and recursively \(h(v_j)=h(v_{j-1})\oplus c(v_{j-1}v_j)\). Even parity gives \(h(v_n)=h(v_0)\). The \(n\) antipodal vertex pairs represented by the path vertices are distinct; two proper nested direction-prefix sets cannot be complements. Thus the values extend to an antipodally invariant vertex potential on the cube, and \(c'=c\oplus\delta h\) is red on all edges of \(P\). Invariant potentials are generated by the pair indicators \(h_U\), so \(c'\) is in the same star component. \(\square\)

**Theorem (local stability is equivalent to unrestricted NORI1).** Unrestricted NORI1 holds if and only if the following property holds: for every successful legal coloring \(c\) and every antipodal vertex pair \(U\), the star-flipped coloring \(T_U(c)\) also has a monochromatic full antipodal geodesic.

*Proof.* NORI1 implies the property. Conversely every star component contains a successful member by the previous theorem, and all other members are reached by a sequence of star flips. If each such flip preserves success, the entire component succeeds. Every legal coloring belongs to some component. \(\square\)

**Corollary (critical-star transversal and localized defects).** If NORI1 is false, there is a legal coloring \(c\) with a monochromatic full geodesic and a pair \(U\) such that \(T_U(c)\) is bad. Every monochromatic full geodesic of \(c\) must meet \(U\). Furthermore \(T_U(c)\) possesses a full geodesic with either one minority-color edge, or two consecutive minority-color edges (using a cyclic root slide in the endpoint case).

*Proof.* In the star component of a bad coloring, join a successful member to the bad member by star flips, and choose the first good-to-bad transition. Any monochromatic full path avoiding \(U\) would survive that flip. Take a red full path in the good coloring, using antipodal translation of a blue one if necessary. If its visit to \(U\) is internal, both incident and consecutive edges change from red to blue and all other steps remain red. If \(U\) is its antipodal endpoint pair, the first and last edges change to blue; the resulting word \(1\,0^{n-2}\,1\) becomes \(0^{n-2}\,1\,0\) after sliding the initial root along the first step. \(\square\)

**Theorem (large good subcubes).** Put \(V=2^{n-1}\). Given a red rooted full geodesic \(P\) in a legal coloring \(c\), precisely \(2^{V-n}\) colorings in its phase-zero star-gauge component retain that same red path. For \(n\ge3\), at least \(V-n\) different individual star flips preserve \(P\).

*Proof.* The path visits \(n\) different antipodal vertex pairs. An invariant potential preserves all its red edges if and only if its values on these \(n\) pairs agree. The values on the remaining \(V-n\) pairs are free; dividing by the globally constant potential leaves \(V-n\) independent bits. Flipping any unvisited pair changes none of the path edges. \(\square\)

**Explicit affine \(Q_4\) obstruction to short-range red repair.** With low-bit-first indexing let
\[
c_0(x)=x_1,\quad c_1(x)=x_2,\quad
c_2(x)=x_0\oplus x_1\oplus x_3,\quad c_3(x)=1\oplus x_2.
\tag{ST1}
\]
These rules are legal. The path \(P=(0,1,3,7,15)\) in order \((0,1,2,3)\) is red. Flip the vertex pair \(U=\{3,12\}\). The color word of \(P\) becomes \((0,1,1,0)\). Enumeration of all \(16\cdot4!=384\) rooted full antipodal geodesics in the transformed coloring finds 16 red and 16 blue. Every red full geodesic is edge-disjoint from the original path \(P\), even though the transformed coloring remains successful. For instance, a new red geodesic starts at vertex 2 with direction order \((0,3,1,2)\). Some blue full geodesics meet edges of \(P\); thus the obstruction is specific to an all-red repair retaining a red edge.

**Exhaustive low-dimensional antipodal-pair transversals.** Intersect the visited antipodal-vertex-pair sets of all red full geodesics. Antipodal translation maps any blue full geodesic to a red one and preserves the visited-pair set. Among all 64 legal \(Q_3\) colorings, 40 have a nonempty intersection and 24 do not. Among all 65536 legal \(Q_4\) colorings, every intersection is empty. Consequently every legal \(Q_4\) coloring has, for each chosen antipodal vertex pair \(U\), a monochromatic full antipodal geodesic avoiding \(U\). The \(Q_4\) finding is finite and does not imply such an avoidance theorem in arbitrary dimension. The independent verification files are nori_star_hitting.cpp and nori_star_gauge_verify.py.

**Status.** The local-stability condition remains unproved and has the full logical strength of NORI1. The affine witness invalidates the simplest repair method based on retaining an original red edge. Neither the star-component existence theorem nor the low-dimensional transversals establishes local stability for every coloring.


#### Universal sparse star-gauge profile correction

For any n>=3, any legal antipodally odd cube-edge coloring c, and any target direction-indexed geodesic color profile s, there exist at most floor((n-1)/2) antipodal vertex-pair star flips taking c to a legal coloring c' realizing profile s on a full antipodal geodesic. All square curvatures are preserved, and at most 2n floor((n-1)/2) edges change color. This holds without restrictions on the nonlinear edge rules.

Proof. Fix one rooted full geodesic P with direction order p_0,...,p_{n-1}, and put a_j=c(P_j P_{j+1}) xor s_{p_j}. Extend the discrepancy word by a_{j+n}=1 xor a_j. Sliding the starting root forward k edges and moving the original prefix to the end using antipodal edges yields a full geodesic with discrepancy window (a_k,...,a_{k+n-1}). Its parity is parity(a_0,...,a_{n-1}) xor (k mod 2). Select a shift k with even discrepancy parity. Integrating these discrepancies along the shifted path yields vertex potential values H_0=0 and H_{j+1}=H_j xor a_{k+j}, and even parity ensures H_n=H_0. The first n visited vertices represent distinct antipodal vertex pairs, so the H_j extend to an antipodally invariant potential, which removes every discrepancy by its edge gradient. Complementing all H_j on those n visited pairs produces the same correction along the chosen path. One may therefore use at most min(weight(H_0,...,H_{n-1}),n-weight), no more than floor(n/2), star flips. This proves the required bound for odd n.

For even n>=4, choose k in {0,1} so that shift k has even discrepancy parity. Then k+2 also has even parity. Define B_0=0 and B_{j+1}=B_j xor a_j over the twice-length twisted word, and let Z_k be the integer count of ones among B_k,...,B_{k+n-1}. The even window gives B_{k+n}=B_k, while the intermediate odd window gives B_{k+n+1}=1 xor B_{k+1}. Therefore
\[
Z_{k+2}-Z_k=1-2B_{k+1}\in\{-1,1\}.
\]
So these two even-parity windows cannot both have balanced weight n/2. At least one requires at most n/2-1 antipodal star flips. This is floor((n-1)/2) for even n, completing the proof.

An independent program nori_star_covering_radius.cpp exhaustively verifies all 64 legal Q3 colorings and all 65536 legal Q4 colorings against all possible target profiles, constructing each repaired path and checking its edge colors. It also checks 2000 random legal Q5 colorings with 15 target profiles per coloring. Separate enumeration of all binary discrepancy words through length 16 corroborates the uniform cyclic-window radius. This is a deterministic polynomial-size recoloring theorem, not a proof that the unmodified coloring realizes the target or that NORI1 holds.


### Braid cancellation versus commuting-square winding

The second-switch labeling of the type-\(B_n\) Coxeter **chambers**, developed in the preceding subsection, preserves full dimension-simplicity. Under a hypothetical coloring with no monochromatic antipodal geodesic, each complete-geodesic color word has at least two switches, so we may label its chamber
\[
L(x,\pi)=(-1)^{w_1(x,\pi)}e_{s_2(x,\pi)}
\in\{\pm e_2,\ldots,\pm e_{n-1}\},
\tag{1}
\]
where \(s_2\) is the position of the second color change. Adjacent chambers never receive opposite labels. The target crosspolytope boundary is \(S^{n-3}\).

This subsection distinguishes **braid residues**, which always admit a canonical local filling, from **commuting-exchange residues**, which can have nonzero winding in the first dimension where winding is meaningful. It thereby identifies a missing cancellation that a Wu–Yang-style chain map must accommodate.

#### A uniform braid-residue filling

Let \(s_1,s_2\) exchange dimensions in positions \(1,2\) and \(2,3\). Their rank-two parabolic residue is the hexagon consisting of all six orderings of the same first three dimensions, with one fixed root \(x\) and the same remaining dimension order.

**Theorem 1 (braid hexagons are nullhomotopic in a contractible carrier).** Suppose \(n\ge4\), and every chamber of a rank-two \(s_1,s_2\)-residue has a color word with at least two switches. Then the piecewise-linear signed-second-switch labeling on its six dual edges extends continuously to the dual two-cell, through a contractible subcomplex of the crosspolytope boundary.

*Proof.* Write the six color words as \(w^{(\pi)}\), indexed by the six permutations of the first three dimensions. Every such path ends its third step at the same cube vertex, then traverses the same remaining dimensions. Thus
\[
w^{(\pi)}_j=u_j\qquad(4\le j\le n)
\tag{2}
\]
for a suffix \(u=(u_4,\ldots,u_n)\) independent of \(\pi\).

If the second switch of \(w^{(\pi)}\) occurs at position \(r\ge3\), then the first \(r\) comparisons contain precisely two changes, so
\[
w^{(\pi)}_1=w^{(\pi)}_{r+1}=u_{r+1}.
\tag{3}
\]
Consequently **for each axis index \(r\ge3\), only one of the two opposite labels \(\pm e_r\) can occur on the hexagon**; its sign is prescribed by \(u_{r+1}\).

Let \(T\) be the set of labels \((-1)^{u_{r+1}}e_r\) with \(r\ge3\) that occur. If \(T\ne\varnothing\), all six labels belong to the simplicial subcomplex
\[
L=S^0_{\{\pm e_2\}}*\Delta(T)
\subseteq\partial\operatorname{Crosspolytope}_{n-2}.
\tag{4}
\]
Here the simplex \(\Delta(T)\) uses one signed vertex for each of the distinct axes \(r\ge3\), and the join is contractible because \(\Delta(T)\) is nonempty and contractible. The edge images also lie in \(L\), since adjacent labels are nonopposite. Hence their circular boundary map extends over a disk in \(L\).

If \(T=\varnothing\), every label is \(+e_2\) or \(-e_2\). Adjacent chambers cannot have opposite labels, so connectedness of the six-cycle forces one constant label on the residue; its boundary image is constant and extends. \(\square\)

The theorem holds at all dimensions and does not assume any restriction beyond the original shared-edge coloring and the availability of the second switch on the six constituent complete paths.

#### A commuting exchange with nonzero local winding

**Theorem 2 (nontrivial square obstruction to the canonical one-skeleton map).** In \(Q_4\) there is a valid antipodally odd edge coloring for which the rank-two commuting residue \(\langle s_1,s_3\rangle\) at cube root \(0000\) consists of the four complete-geodesic orders
\[
1234,\quad2134,\quad2143,\quad1243
\tag{5}
\]
with respective words
\[
(1,0,0,1),\quad(0,1,0,1),\quad(0,1,1,0),\quad(1,0,1,0).
\tag{6}
\]
All four words have at least two switches. Their second-switch labels, listed around the square, are
\[
-e_3,\quad+e_2,\quad+e_3,\quad-e_2.
\tag{7}
\]
Consequently the map of the dual square boundary to \(S^1=\partial\operatorname{Crosspolytope}_2\), obtained by mapping each chamber to its label and every dual edge to the shorter crosspolytope edge, has winding number \(+1\). It cannot be extended to this dual two-cell with its prescribed boundary map.

*Proof.* The following eight undirected edges determine the required local coloring; dimension numbers start at \(1\), and the four-bit starting vertices list bits in dimension order:
\[
\begin{array}{c|c|c}
\text{starting vertex}&\text{edge dimension}&\text{color}\\\hline
0000&1&1\\
1000&2&0\\
1100&3&0\\
1110&4&1\\
0000&2&0\\
0100&1&1\\
1100&4&1\\
1101&3&0
\end{array}
\tag{8}
\]
These eight edges lie in distinct antipodal edge orbits. Assign complementary colors to their antipodal mates, and complete the other orbits arbitrarily. Reading the four orders (5) gives the words (6). The first and third words have their second switch at position \(3\), with first bits \(1\) and \(0\), respectively; the second and fourth words have their second switch at position \(2\), with first bits \(0\) and \(1\). This yields (7). Traversing their four crosspolytope edges follows the circle once. \(\square\)

**Scope.** Theorem 2 concerns the forced short-edge interpolation in the second-switch 1-skeleton map. It does **not** contradict NORI1, since the coloring can have favorable complete geodesics elsewhere. Nor does it preclude an altered chain map that sends the same dual edges to longer target chains, or uses additional source faces for cancellation. In higher dimensions, the displayed loop lies in a circle inside a higher-dimensional sphere and is nullhomotopic when the target has dimension at least two.

#### Structural lesson for Wu–Yang's chain cancellation

Wu and Yang's Lemmas 5.1 and 5.4 control radial chains by rook-gallery rank and even multiplicity of dependent facets. For the rank-preserving second-switch construction:

* braid residues generated by \(s_1,s_2\) already admit contractible-carrier fillings, with the proof relying on equality of the suffix edges after three steps;
* commuting residues generated by \(s_1,s_3\) can carry a nontrivial boundary cycle for the canonical short-edge chain assignment, despite respecting shared cube edges and full rank;
* therefore a modified chain map cannot be justified solely by verifying braid relations or by a pairwise nonopposition lemma.

The next substantive proof obligation is a **coherent chain correction across commuting exchanges**, whose boundaries cancel over larger Coxeter cells or over a suitably chosen subdivision. This is a direct rank-simple analogue of the cubical face cancellation in Wu–Yang's construction, not a statement about a restricted family of colorings.

### Projective square curvature and antipodal exchange disks

Let \(n\ge3\), let \(B_n=\partial[0,1]^n\cong S^{n-1}\), and let \(\tau y=\mathbf1-y\) be central antipodality. Its quotient is \(Y_n=B_n/\tau\cong\mathbb{RP}^{n-1}\). Work with cubical cellular (co)chains over \(\mathbb F_2\). A legal NORI1 edge coloring is a one-cochain \(c\) with
\[
c(\tau e)=1+c(e)\qquad(e\text{ an undirected cube edge}).
\tag{1}
\]
Define its **square curvature** by \(\kappa=\delta c\):
\[
\kappa_{ij}(y)
=c_i(y)+c_j(y\oplus e_i)+c_i(y\oplus e_j)+c_j(y).
\tag{2}
\]
This depends only on the square, not the chosen corner. Since a square has four edges, \(\kappa(\tau F)=\kappa(F)\), so \(\kappa\) descends to a two-cocycle \(\bar\kappa\) on \(Y_n\).

**Theorem 1 (canonical antipodal exchange disk).** Let \(x\) be any cube vertex and \(\pi=(d_1,\ldots,d_n)\) any permutation. Let \(P=P(x,\pi)\) be the full antipodal geodesic, and concatenate it with its antipodal translate \(\tau P\). For \(i<j\), define \(F_{ij}(x,\pi)\) to be the two-face spanned by dimensions \(d_i,d_j\) with one corner
\[
q_{ij}=x\oplus\bigoplus_{k=i}^{j-1}e_{d_k}.
\tag{3}
\]
Then the two-chain
\[
\boxed{\Sigma_P=\sum_{1\le i<j\le n}F_{ij}(x,\pi)}
\tag{4}
\]
satisfies
\[
\boxed{\partial\Sigma_P=P+\tau P,}
\qquad
\boxed{\sum_{i<j}\kappa(F_{ij}(x,\pi))=n\pmod2.}
\tag{5}
\]

*Proof.* The closed walk \(P+\tau P\) has direction word \(d_1\cdots d_nd_1\cdots d_n\). Commute the second \(d_1\) left past \(d_n,\ldots,d_2\), then cancel the resulting consecutive pair \(d_1d_1\). Repeat for \(d_2,\ldots,d_n\). Each adjacent commutation is realized by one cubical square, and the commutation of the second \(d_i\) across \(d_j\) uses the face in (3). Each pair \(i<j\) is used once. The final walk is empty, so the boundary of their sum equals \(P+\tau P\), proving the first identity. Stokes' identity and antipodal oddness give
\[
\sum_{i<j}\kappa(F_{ij})=\langle c,P+\tau P\rangle
=\sum_{e\in P}(c(e)+c(\tau e))=n\pmod2.
\]
\(\square\)

The chain uses \(\binom n2\) squares, one for every unordered pair of dimensions. The identity holds for every dimension and every legal coloring; it was also checked independently on random colorings in dimensions \(3\) through \(7\).

**Theorem 2 (projective curvature class).** Let \(u\in H^1(\mathbb{RP}^{n-1};\mathbb F_2)\) be the standard generator. Then for every legal coloring,
\[
\boxed{[\bar\kappa]=(n\bmod2)u^2
\in H^2(\mathbb{RP}^{n-1};\mathbb F_2).}
\tag{6}
\]
In particular square curvature is an unavoidable nontrivial cohomology class on the antipodal quotient in odd dimension, but is a coboundary on that quotient in even dimension.

*Proof.* The quotient projection \(\pi:B_n\to Y_n\) sends the two copies of \(P\) to the same edge chain. Hence \(\pi_*\Sigma_P\) is a two-cycle. Theorem 1 implies
\[
\langle\bar\kappa,\pi_*\Sigma_P\rangle
=\langle\kappa,\Sigma_P\rangle=n\pmod2.
\]
For odd \(n\) the class is nonzero; the one-dimensional cohomology group \(H^2(\mathbb{RP}^{n-1};\mathbb F_2)\) has generator \(u^2\), proving (6).

For even \(n\), the legal coloring
\[
c_i^*(y)=\sum_{j\ne i}y_j
=\delta f(\{y,y\oplus e_i\}),\qquad
f(y)=\sum_{i<j}y_i y_j\pmod2
\tag{7}
\]
has zero square curvature. For any other legal coloring \(c\), the difference \(d=c+c^*\) is invariant under \(\tau\) and descends to a one-cochain \(\bar d\) on \(Y_n\). Therefore \(\bar\kappa=\delta\bar d\), proving the even case. \(\square\)

**Corollary 3 (classification of flat legal colorings).** A legal coloring satisfying \(\kappa=0\) exists **if and only if** \(n\) is even. For necessity, on the full contractible cube \(\kappa=0\) implies \(c=\delta f\). Put \(h(y)=f(y)+f(\tau y)\). Antipodal oddness yields \(h(y\oplus e_i)=h(y)+1\), so \(h(y)=h(0)+|y|\pmod2\). But \(h(\tau y)=h(y)\), requiring \(n\) even. Sufficiency is (7). Thus odd-dimensional antipodal colorings necessarily have curved squares, while even-dimensional legal flat colorings exist.

**Theorem 4 (red-blue monochromatic defect decomposition).** On a square, write the successive edge bits of its two increasing two-step routes as \((A,B)\) and \((C,D)\). Define the color-\(t\) exchange defect to be the parity of the number of routes that are monochromatic of color \(t\):
\[
\Omega_t=\mathbf1_{\{A=B=t\}}+\mathbf1_{\{C=D=t\}}\pmod2.
\]
Then
\[
\boxed{\Omega_0+\Omega_1=A+B+C+D=\kappa(F).}
\tag{8}
\]

*Proof.* Writing bits in \(\mathbb F_2\) gives \(\Omega_1=AB+CD\) and \(\Omega_0=(1+A)(1+B)+(1+C)(1+D)\). Their sum is \(A+B+C+D\). \(\square\)

By Theorem 1, every canonical antipodal exchange disk satisfies
\[
\boxed{\sum_{F\in\Sigma_P}(\Omega_0(F)+\Omega_1(F))=n\pmod2.}
\tag{9}
\]
For odd \(n\), this forces an odd number of squares where the two color-specific defects disagree. For even \(n\), the flat coloring (7) can nevertheless have \(\Omega_0=\Omega_1=1\) on individual squares, even though \(\kappa=0\): choose \(y_i\ne y_j\) and a suitable parity of the exterior bits. Thus ordinary square curvature and the path-order obstruction studied in Article XIV, Subsection 21, are independent phenomena.

**Corollary 5 (cup-product relation to the second-switch obstruction).** For odd \(n\ge5\), identify \(Y_n\) with the antipodal type-\(B_n\) Coxeter sphere quotient via radial projection. The primary obstruction to the signed-second-switch map, proved in Article XIV, Subsection 25, is \([o]=u^{n-2}\). Hence
\[
\boxed{[o]=u^{n-4}\smile[\bar\kappa].}
\tag{10}
\]
This is a cohomology identity, not a pointwise formula for the degrees of individual Coxeter residues. For even \(n\), \([\bar\kappa]=0\) while \([o]=u^{n-2}\ne0\), so no such factorization through ordinary square curvature is possible.

**Implications for Wu–Yang's dimension-simple chain repair.** Color-sensitive square defects cannot be dismissed as accidental errors: in odd dimensions their sum carries the forced class \(u^2\), and its cup power reproduces the high-rank second-switch obstruction. Simply demanding that all square defects vanish would exclude every odd-dimensional coloring. Conversely the flat even-dimensional example shows that correcting ordinary cubical curvature alone does not correct order-holonomy. A viable chain construction must account for both the projective curvature and the additional path-order information without losing the dimension-simple path geometry. Neither theorem proves NORI1, but they give a uniform cohomological constraint on any attempted correction.

#### Theorem 6 (sharp square-curvature systole in every odd dimension)

For every odd \(n\ge3\), and every unrestricted antipodally odd binary coloring of the undirected cube edges, the number of two-dimensional cube faces with nonzero curvature satisfies
\[
\boxed{|\operatorname{supp}(\kappa)|\ge2^{n-2}.}
\tag{11}
\]
The bound is **attained** for every such \(n\). One extremal coloring has curvature supported entirely on the \(2^{n-2}\) squares spanned by any one chosen pair of dimensions.

*Proof of the bound.* There are \(2^n n!\) full rooted antipodal geodesic flags and \(N_2=\binom n2 2^{n-2}\) two-faces. For every flag \(P\), the exchange-disk theorem supplies a chain \(\Sigma_P\) containing precisely \(\binom n2\) distinct two-faces and satisfying \(\sum_{F\in\Sigma_P}\kappa(F)=1\) because \(n\) is odd. Thus every \(\Sigma_P\) meets \(\operatorname{supp}(\kappa)\).

The hyperoctahedral group acts transitively on cube two-faces and permutes the full geodesic flags and their exchange disks equivariantly. Each two-face therefore belongs to the same number \(r\) of exchange disks. Counting flag–face incidences gives
\[
r=\frac{(2^n n!)\binom n2}{\binom n2\,2^{n-2}}=4n!.
\]
Let \(M=|\operatorname{supp}(\kappa)|\). Double counting incidences between geodesic disks and curved faces yields
\[
2^n n!\le 4n!\,M,
\]
hence \(M\ge2^{n-2}\).

*Proof of attainment.* Choose two different dimensions \(a,b\in[n]\), and define the following edge coloring, with \(y\in\mathbb F_2^n\) denoting either endpoint of the specified edge:
\[
\boxed{
c_a(y)=\sum_{k\notin\{a,b\}}y_k\pmod2,\qquad
c_i(y)=y_a\quad (i\ne a).
}
\tag{12}
\]
Each \(c_i\) ignores the bit \(y_i\), so it defines an undirected-edge coloring. For \(i\ne a\), the antipode flips \(y_a\). For \(i=a\), the defining sum has \(n-2\) terms, an odd number, so antipodality also flips this color.

For a square in dimensions \(i,j\), its curvature is the sum of the cross-differences
\[
\kappa_{ij}=\Delta_j c_i+\Delta_i c_j.
\]
If neither dimension equals \(a\), both cross-differences vanish. If \(i=a\) and \(j\ne a\), then \(\Delta_a c_j=1\), whereas \(\Delta_j c_a=1\) for \(j\ne b\) and zero for \(j=b\). Consequently
\[
\boxed{\kappa_{ij}(y)=\mathbf1_{\{\{i,j\}=\{a,b\}\}}}
\quad\text{for every two-face.}
\tag{13}
\]
There are precisely \(2^{n-2}\) squares with free dimensions \(\{a,b\}\), so the construction attains (11). \(\square\)

**Corollary 7 (projective support minimum).** The projective two-cocycle \(\bar\kappa\) representing \(u^2\in H^2(\mathbb{RP}^{n-1};\mathbb F_2)\) has at least \(2^{n-3}\) nonzero antipodal two-face orbits, and this bound is attained by (12). Thus the cohomological square-curvature obstruction has an explicit minimal-support representative in the quotient cubical cellulation.

**Proof-search implication.** Odd-dimensional antipodal oddness forces many curved squares in absolute count, yet it is compatible with all those squares lying in one pair of dimensions. A proposed Wu–Yang correction that assumes curvature is distributed among many different dimension pairs cannot apply to the full NORI1 class. The all-dimensional lower bound and its concentrated extremizer are constraints on the incidence-based chain-map mechanism, not separate conjectures for a specialized coloring family.

#### Theorem 8 (every antipodal exchange disk generates projective two-homology)

For **every** \(n\ge3\), including even dimensions, the projected canonical exchange disk
\[
Z_P=\pi_*\Sigma_P\in Z_2(Y_n;\mathbb F_2)
\]
represents the nonzero element of
\[
\boxed{H_2(\mathbb{RP}^{n-1};\mathbb F_2)\cong\mathbb F_2.}
\tag{16}
\]

Fix an unordered pair \(\{a,b\}\) of dimensions. Define a two-cochain \(K_{ab}\) on the cubical boundary \(B_n\) by setting \(K_{ab}(F)=1\) if \(F\) has free dimensions \(\{a,b\}\), and \(K_{ab}(F)=0\) otherwise. It is antipodally invariant and descends to \(\bar K_{ab}\in C^2(Y_n;\mathbb F_2)\). Then
\[
\boxed{\delta\bar K_{ab}=0,\qquad
[\bar K_{ab}]=u^2,\qquad
\langle\bar K_{ab},Z_P\rangle=1}
\tag{17}
\]
for every complete antipodal geodesic \(P\).

*Proof.* The canonical exchange chain \(\Sigma_P\) contains one face for each unordered pair of dimensions. Its projection is a cycle by Theorem 1. Every three-dimensional cubical face contains either no squares with free dimensions \(\{a,b\}\), or two opposite such squares. Thus \(\delta K_{ab}=0\), and the same holds after descent to the quotient. Since \(\Sigma_P\) contains one \(\{a,b\}\)-square,
\[
\langle\bar K_{ab},Z_P\rangle
=\langle K_{ab},\Sigma_P\rangle=1.
\]
Both \([\bar K_{ab}]\) and \([Z_P]\) are therefore nonzero. Their projective homology and cohomology groups have dimension one, with \(u^2\) generating cohomology. \(\square\)

**Corollary 9 (sharp projective two-cosystole).** For \(n\ge3\), every two-cocycle \(\eta\) representing \(u^2\) on the antipodal cubical quotient has at least
\[
\boxed{2^{n-3}}
\tag{18}
\]
antipodal two-face orbits in its support. The bound is attained by every \(\bar K_{ab}\). Equivalently, its invariant lift has at least \(2^{n-2}\) two-faces in its support upstairs.

*Proof.* Since \(Z_P\) generates homology, \(\langle\eta,Z_P\rangle=1\) for every full geodesic flag \(P\). Hence every canonical exchange disk contains an odd, and therefore positive, number of faces in the support of the lifted cocycle. There are \(2^n n!\) rooted full geodesic flags. By transitivity of the cube automorphism group, each two-face lies in \(4n!\) exchange disks: this follows by counting the \(\binom n2\) faces per flag among \(\binom n2 2^{n-2}\) two-faces. Double counting forces at least \(2^{n-2}\) supported faces, or \(2^{n-3}\) antipodal orbits. The cochain \(\bar K_{ab}\) has just those \(2^{n-3}\) orbits of \(\{a,b\}\)-squares. \(\square\)

**Corollary 10 (projective factorization in both parities).** For all \(n\ge5\), the universal primary obstruction \([o]=u^{n-2}\) of the signed-second-switch map from Subsection 25 satisfies
\[
\boxed{[o]=u^{n-4}\smile[\bar K_{ab}]}
\quad\text{for every dimension pair }\{a,b\}.
\tag{19}
\]
For odd \(n\), the color-curvature class \([\bar\kappa]\) also represents \(u^2\); for even \(n\), it is zero. Thus the projective generator can be realized by a single fixed-dimension-pair incidence cocycle regardless of parity, while the two color-specific square defects behave differently in odd and even dimension. These are cohomology identities and do not identify the individual residual Coxeter-cell degrees.

Theorem 8 provides a canonical all-dimensional homological interpretation of the antipodal exchange disks themselves, independent of coloring: each is a projective two-homology generator. This gives a fundamental family of two-cycles on which proposed rank-sensitive Wu–Yang correction chains can be tested before attempting high-dimensional fillings.

**Corollary 11 (exchange-disk rigidity at the sharp bound).** Let \(n\ge3\) and let \(\eta\) be a representative of \(u^2\) on the antipodal cubical quotient. If the invariant lifted support has the minimum size \(2^{n-2}\), then **every** complete antipodal geodesic's canonical exchange disk contains precisely one supported square:
\[
\boxed{
\left|\operatorname{supp}(\pi^*\eta)\cap
\{F_{ij}(x,\pi):1\le i<j\le n\}\right|=1
\quad\text{for all }x,\pi.
}
\tag{21}
\]
Conversely, this one-square-per-disk property implies the support has size \(2^{n-2}\).

*Proof.* Every projected disk is a two-homology generator, so its evaluation against \(\eta\) is one. Therefore it meets the lifted support in an odd positive number of faces. By transitivity, every cube two-face belongs to \(4n!\) of the \(2^n n!\) canonical exchange disks. With minimum support \(2^{n-2}\), the total number of support–disk incidences is
\[
(4n!)\,2^{n-2}=2^n n!,
\]
which is the number of disks. Each disk contributes at least one incidence, so each contributes precisely one. Conversely, double counting a family with one supported face per disk gives the asserted support size. \(\square\)

For odd-dimensional color curvature, this means every coloring attaining Theorem 6's lower bound has a perfect transversal property across the **entire collection of dimension-simple antipodal exchange disks**. The extremal coloring (12) realizes it by concentrating all curvature on one dimension pair. This rigidity is not a classification of all extremizers; showing whether other dimension-pair arrangements attain the same bound is a separate question and is not needed for the present theorem.

#### Exchange-disk Radon rigidity and classification of every sharp curvature representative

Fix \(n\ge3\). Let \(\mathcal F_n\) be the antipodal square-face orbits of \(Q_n\). For any function \(f:\mathcal F_n\to\mathbb R\), define its **exchange-disk transform**
\[
(Rf)(x,\pi)=\sum_{1\le a<b\le n}f([F_{ab}(x,\pi)]),
\tag{RD1}
\]
where \(F_{ab}(x,\pi)\) denotes the canonical square in the exchange disk of the rooted full geodesic \(P(x,\pi)\), as defined in Theorem 1 above.

**Theorem 12 (full real kernel of the disk transform).** The transform \(Rf\) is independent of the rooted full geodesic \((x,\pi)\) if and only if \(f\) is constant on the family of all square orbits in any given unordered pair of dimensions. More precisely, if \((Rf)(x,\pi)=c\) for all \(x,\pi\), then there are real numbers \(\lambda_{ij}\) with
\[
f([F])=\lambda_{ij}\quad\text{whenever }F
\text{ has free dimensions }\{i,j\},\qquad
\sum_{i<j}\lambda_{ij}=c.
\tag{RD2}
\]
Consequently
\[
\boxed{\dim\ker R=\binom n2-1,\qquad
\operatorname{rank}_{\mathbb R}R=
\binom n2(2^{n-3}-1)+1.}
\tag{RD3}
\]

*Proof.* For each unordered pair \(i<j\), let \(f_{ij}(z)\) be the value of \(f\) on the square with free dimensions \(i,j\) and other fixed vertex bits \(z\). The equality \(f_{ij}(z+\mathbf1)=f_{ij}(z)\) permits a real Walsh expansion
\[
f_{ij}(z)=\sum_{\substack{S\subseteq[n]\setminus\{i,j\}\\ |S|\text{ even}}}
a_{ij}(S)(-1)^{\sum_{k\in S}z_k}.
\tag{RD4}
\]
On the disk of \((x,\pi)\), the outside bits of its \(i,j\) square are those of \(x\), toggled in precisely the dimensions occurring strictly between \(i,j\) in \(\pi\). Thus for any fixed nonempty even \(S\), the coefficient of the root Walsh character indexed by \(S\) in \(Rf(x,\pi)\) equals
\[
\sum_{\substack{i<j\\i,j\notin S}}
a_{ij}(S)\,
(-1)^{|S\cap B_\pi(i,j)|},
\tag{RD5}
\]
where \(B_\pi(i,j)\) is the set of directions strictly between \(i,j\) in the order.

For \(i\notin S\), put \(\epsilon_i=(-1)^{|\{k\in S:k\prec_\pi i\}|}\). The sign in (RD5) equals \(\epsilon_i\epsilon_j\). Every assignment of \(\epsilon_i\in\{-1,+1\}\) for \(i\notin S\) is realizable by a permutation: put the positive-sign directions before the first member of \(S\), the negative-sign directions between its first and second members, and all remaining members of \(S\) afterward. The hypothesis that \(Rf\) is constant in \(x\) makes (RD5) vanish for every such assignment. Hence
\[
\sum_{i<j,\ i,j\notin S}a_{ij}(S)\epsilon_i\epsilon_j=0
\quad\text{for every sign assignment}.
\]
Orthogonality of the degree-two Walsh characters forces every \(a_{ij}(S)=0\) for \(S\ne\varnothing\). Therefore every \(f_{ij}\) is constant, with value \(\lambda_{ij}=a_{ij}(\varnothing)\). Conversely such functions give constant disk transform equal to \(\sum_{i<j}\lambda_{ij}\), proving (RD2). There are \(\binom n2 2^{n-3}\) square orbits, and the kernel consists of the \(\binom n2\) dimension-pair constants with one relation, giving (RD3). \(\square\)

**Corollary 13 (classification of all minimizers of the projective two-cosystole).** Every projective cubical two-cocycle representing \(u^2\in H^2(\mathbb{RP}^{n-1};\mathbb F_2)\) with minimum support \(2^{n-3}\) equals \(\bar K_{ab}\) for a unique unordered pair of dimensions \(\{a,b\}\), where \(\bar K_{ab}\) is one on all \(\{a,b\}\)-square orbits and zero on all other square orbits. In particular there are precisely \(\binom n2\) minimum-support cocycle representatives of \(u^2\).

*Proof.* Corollary 11 established that a minimum-support representative meets every projective exchange disk in precisely one square: its zero-one support indicator \(f\) satisfies \(Rf=1\) for all rooted full geodesics. Theorem 12 gives \(f(F)=\lambda_{ij}\) on every \(\{i,j\}\)-square. Since \(f\) is zero-one valued, the \(\lambda_{ij}\) belong to \(\{0,1\}\), and \(\sum\lambda_{ij}=1\) shows that precisely one is one. Each \(\bar K_{ab}\) represents \(u^2\) and attains the bound by Theorem 8 and Corollary 9. \(\square\)

**Corollary 14 (all minimum-curvature legal colorings in odd dimensions).** For odd \(n\ge3\), a legal antipodally odd edge coloring has the minimum number \(2^{n-3}\) of curved antipodal square orbits if and only if its curvature equals \(K_{ab}\) for some pair \(\{a,b\}\). The number of such legal colorings is
\[
\boxed{\binom n2\,2^{2^{n-1}}.}\tag{RD6}
\]
*Proof.* In odd dimension its projective curvature represents \(u^2\); apply Corollary 13. By the curvature-fiber classification in the accompanying curvature-realization Subsection, each admissible curvature has \(2^{2^{n-1}}\) distinct legal coloring lifts. The \(\binom n2\) curvature representatives are disjoint fibers. \(\square\)

**Finite audit.** Computing the real ranks of the exchange-disk incidence matrices for \(n=3,4,5,6\) gives \(1,7,31,106\), respectively, agreeing with (RD3). The matrix sizes are \(48\times3\), \(384\times12\), \(3840\times40\), and \(46080\times120\). The all-dimensional Fourier proof does not depend on these computations.

This classifies the sharp cases of the previously established projective two-cosystole, not just the minimum support value. It leaves unrestricted NORI1 open: the classification constrains the curvature of its sharp colorings but makes no assumption about the remaining legal colorings.


### Curvature realization, gauge phases, and rooted square-defect transport

This subsection gives a complete description of what the square curvature of an unrestricted antipodally odd cube-edge coloring can be, and separates the resulting projective cohomology from the additional root-sensitive information needed in a Wu–Yang dimension-simple chain-map adaptation.

Fix \(n\ge3\), put \(B_n=\partial[0,1]^n\), \(Y_n=B_n/\tau\cong\mathbb{RP}^{n-1}\), and work over \(\mathbb F_2\). Let \(u\in H^1(Y_n)\) denote the generator. Write \(\pi:B_n\to Y_n\) for the quotient and let \(\mathbf1\in C^1(B_n)\) denote the cochain that is one on every cube edge. A **legal** cube-edge coloring is \(c\in C^1(B_n)\) satisfying
\[
\tau^*c=c+\mathbf1.
\tag{1}
\]
The cubical curvature \(\kappa=\delta c\) is antipodally invariant and descends to a two-cocycle \(\bar\kappa\in Z^2(Y_n)\). Article XIV, Subsection 28, proved \([\bar\kappa]=(n\bmod2)u^2\).

#### Theorem 1 (complete curvature realization and fiber classification)

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

#### Theorem 2 (two gauge phases above every curvature)

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

#### Theorem 3 (rooted-square defect transport)

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

#### Proposition 5 (full local defect freedom at fixed curvature)

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

#### Theorem 6 (uniform full-geodesic words in every curvature fiber)

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


#### Gauge-orbit averaging and the antipodal vertex-star closure reduction

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



#### Vertex-star Petrie grade flux and distance-two defect repair

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



#### Two-step gauge strands, universal grade statistics, and sharp monotone Petrie repair

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



#### Joint projective vertex-incidence geometry and gauge transfer

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


#### Strand matching measures the distance to a successful vertex gauge

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



#### Simultaneous cycle repair: an affine overlap syndrome and a balanced incompatibility certificate

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



#### Second-moment theorem: almost every coloring in every vertex-gauge orbit is successful

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



##### Precise cycle-intersection exponential moment and exponentially sharper bad-orbit density

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



##### Even-dimensional parity cancellation sharpens the gauge-orbit second moment by a factor of n

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



##### Precise signed pair-covariance law for cycle repairs

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



##### Joint independence for parity-peelable families of Petrie cycles

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



##### Curved squares suppress the degree-two Fourier influence of a vertex-gauge pair

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



##### Curvature-sensitive global gauge-orbit variance budget

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



##### Leading asymptotic constant of the even-gauge variance estimate

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


#### Odd face networks give doubly exponential success abundance in every gauge orbit

The second-moment bounds can be amplified using networks containing many full geodesics. The seam obstruction is resolved by odd block sizes and one block root slide. Entropy covering then permits the translated networks to overlap.

Write \(n\ge3\), \(M=2^{n-1}\), and fix an arbitrary legal antipodally odd coloring \(c\) of \(Q_n\). The invariant vertex gauge bits \(h([v])\), indexed by the \(M\) antipodal vertex pairs, are independent and uniform. All probabilities below are within this one fixed gauge orbit; balance is unnecessary.

##### A uniform connection bound on an ordinary face with prescribed endpoint gauges

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

##### Choosing compatible seams by an odd block slide

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

##### Counting all translated failures by entropy covering

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

##### An explicit decoder using disjoint networks

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



##### A sharp entropy barrier for parity-peelable Petrie-cycle families

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



#### Simultaneous zero-geodesic gauges: full incidence criterion and the projective holonomy obstruction

The preceding repair and odd-face network results concern the event that *at least one* geodesic becomes monochromatic under an invariant vertex gauge. For a **prescribed family** of full geodesics, simultaneous repair is governed by a finite binary graph-incidence system. Importantly, ordinary square curvature does not capture its entire obstruction, because the projective antipodal identification creates additional closed walks.

Fix \(n\ge3\), a legal antipodally odd coloring \(c\), and a nonempty finite family \(\mathscr P\) of rooted, oriented full antipodal geodesics. Build a labeled undirected **multigraph** \(H_{\mathscr P}\) as follows: its vertices are the antipodal vertex pairs \([x]=\{x,\bar x\}\) visited by at least one member of \(\mathscr P\). For **each occurrence** of a cube edge \(e=\{x,x^i\}\) in any \(P\in\mathscr P\), insert a graph edge joining \([x]\) to \([x^i]\), with binary label \(c(e)\). Keep parallel occurrences, including the two antipodal lifts of one projective edge, as separate graph edges. Put \(v=|V(H_{\mathscr P})|\), and let \(q\) be the number of connected components of this multigraph.

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

**Consequence for face-network closure.** The obstruction to making any *fixed collection* of network path witnesses simultaneously zero is now a finite affine cycle-syndrome, with two distinct sources: local cubical square curvature and projective antipodal holonomy. A tree of flat adjacent-square exchanges with fresh projective vertices always repairs, whereas collisions of previously used projective vertices can create global incompatibilities even when all local square curvatures vanish. This gives a specific target for overlap arguments among odd-face networks: control the cycle syndromes produced when their path families reuse projective vertices, rather than impose pairwise square-flatness alone. The theorem does not establish a successful witness for the original ungauged coloring.



##### Flat-face polarization maximizes all Petrie grades; curvature gives quantitative stability

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



##### Every facet of a balanced odd cube has nonzero curvature

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



##### Quantitative nonflatness of every balanced facet

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


#### Leading Boolean-degree charges of unrestricted square curvature

For a Boolean function \(f\), write \(D_vf(x)=f(x+v)+f(x)\). Let \(e_d(z_1,\ldots,z_m)\) be the elementary symmetric multilinear polynomial of degree \(d\) over \(\mathbb F_2\). Algebraic degree refers to the unique multilinear polynomial representation.

**Theorem (leading curvature charges).** Let \(n\ge4\) and let \(c=(c_i)\) be an arbitrary legal antipodally odd coloring of \(Q_n\). There are unique bits \(a_i\) such that
\[
c_i(x)=a_i e_{n-2}(x_{[n]\setminus\{i\}})+r_i(x),\qquad \deg r_i\le n-3. \tag{LC1}
\]
For each pair \(i\ne j\), its square curvature satisfies
\[
\boxed{\ \kappa_{ij}=D_jc_i+D_ic_j
=(a_i+a_j)e_{n-3}(x_{[n]\setminus\{i,j\}})+s_{ij},
\quad\deg s_{ij}\le n-4.\ } \tag{LC2}
\]
In particular all square curvatures have degree at most \(n-4\) if and only if \(a_1=\cdots=a_n\). If \(a_i=1\), then \(D_vc_i\) has degree \(n-3\) for every \(v\) whose projection away from direction \(i\) is neither zero nor the all-ones vector. Consequently the full translation stabilizer of \(c_i\) is \(\{0,e_i\}\).

Under a vertex gauge \(c\mapsto c+\delta h\), where \(h(x+\mathbf1)=h(x)\), all charges \(a_i\) change by one common bit \(t\). Both choices of \(t\) are realized, since
\[
h_*(x)=\prod_{j=1}^{n-1}(x_j+x_n) \tag{LC3}
\]
is antipodally invariant and its gauge changes every charge by one. Hence the leading square curvatures determine the charge vector modulo its common complement, and this indeterminacy is realized by a legal vertex gauge.

*Proof.* Because \(c_i\) ignores \(x_i\), regard it as a function \(f\) of \(m=n-1\ge3\) variables. Legal antipodal oddness gives \(f(z+\mathbf1_m)=f(z)+1\), so \(f\) is balanced and its full-degree polynomial coefficient vanishes. For \(j\in[m]\), let \(b_j\) denote the coefficient of the degree-\((m-1)\) monomial missing \(j\). The coefficient of the degree-\((m-2)\) monomial missing \(j,k\) in \(D_{\mathbf1_m}f=1\) is \(b_j+b_k\). Thus all \(b_j\) equal a bit \(a_i\), giving (LC1). For a general translation \(v\), the same coefficient in \(D_vf\) is \(a_i(v_j+v_k)\). When \(a_i=1\), it is nonzero for some pair unless \(v\) is zero or all ones. The all-ones derivative equals one, proving the translation statement.

Differentiating (LC1) in direction \(j\ne i\) gives leading term \(a_i e_{n-3}(x_{[n]\setminus\{i,j\}})\). Adding the corresponding derivative of \(c_j\) gives (LC2).

Now let \(h(x+\mathbf1)=h(x)\). Its support is antipodally paired, so its full-degree coefficient is zero. The same calculation, with \(D_{\mathbf1}h=0\), shows that the homogeneous degree-\((n-1)\) part of \(h\) is \(t e_{n-1}(x)\) for a bit \(t\). Its derivative \(D_ih\) has leading degree-\((n-2)\) part \(t e_{n-2}(x_{[n]\setminus\{i\}})\), shifting every \(a_i\) by \(t\). Each factor \(x_j+x_n\) in (LC3) is invariant under antipodality, and its product has degree-\((n-1)\) part \(e_{n-1}(x)\). This yields \(t=1\). \(\square\)

**Corollary (one-orbit normalization preserving a selected geodesic).** In any legal coloring, one can make all \(a_i=1\) by changing at most one antipodal orbit of undirected edges in each direction. The changed orbits can be chosen disjoint from any prescribed full antipodal geodesic; all its colors remain unchanged.

*Proof.* For the rule \(c_i\), add the indicator of an antipodal pair of its \(n-1\) input vectors. This reverses the colors on one antipodal edge orbit in direction \(i\), preserves legality, and changes its leading polynomial component by \(e_{n-2}\), hence toggles \(a_i\). There are \(2^{n-2}\ge4\) edge orbits in each direction; a full geodesic meets only one of them. Choose another whenever a toggle is needed. \(\square\)

The charge identity is valid for all legal colorings, in both dimension parities. Maximal Boolean rule degree and translation rigidity therefore admit sparse legal normalization while keeping any chosen path profile. The curvature constraints alone do not force a monochromatic geodesic in the original coloring.


### Three-cube chain homotopy for adjacent dimension exchanges

Work over \(\mathbb F_2\) on the cubical boundary \(B_n=\partial[0,1]^n\), \(n\ge4\). For a set of free dimensions \(I\), let \(F_I(y)\) denote the cubical face containing the corner \(y\); changing bits of \(y\) inside \(I\) leaves this face unchanged.

For a full geodesic \(P=P(x;d_1,\ldots,d_n)\), Article XIV, Subsection 28, defines
\[
\Sigma_P=\sum_{i<j}F_{\{d_i,d_j\}}\left(x\oplus\bigoplus_{r=i}^{j-1}e_{d_r}\right),
\quad \partial\Sigma_P=P+\tau P.
\tag{1}
\]

**Theorem (adjacent-swap three-chain).** Suppose \(P'\) differs from \(P\) by swapping the adjacent dimensions \(a=d_k\), \(b=d_{k+1}\), where \(1\le k<n\). Put
\[
y=x\oplus\bigoplus_{r<k}e_{d_r},\quad F=F_{\{a,b\}}(y).
\]
Define a three-chain with \(n-2\) terms:
\[
\boxed{
\begin{aligned}
T_k={}&\sum_{r<k}F_{\{d_r,a,b\}}\left(x\oplus\bigoplus_{j=r+1}^{k-1}e_{d_j}\right)\\
&+\sum_{r>k+1}F_{\{a,b,d_r\}}\left(x\oplus\bigoplus_{j=k+2}^{r-1}e_{d_j}\right).
\end{aligned}}
\tag{2}
\]
Then
\[
\boxed{\Sigma_P+\Sigma_{P'}=F+\tau F+\partial T_k.}
\tag{3}
\]

*Proof.* Squares involving neither \(a\) nor \(b\), as well as the common \(\{a,b\}\) square, cancel between \(\Sigma_P\) and \(\Sigma_{P'}\). For every dimension \(d_r\) occurring before the swapped pair, the four surviving squares of types \(\{d_r,a\}\) and \(\{d_r,b\}\) are precisely the four side faces of the corresponding first-sum three-cube in (2). The analogous statement holds for every \(d_r\) occurring after the pair and its second-sum three-cube. These exhaust the difference of the two exchange disks.

Every three-cube also has two faces of type \(\{a,b\}\). In the first sum these extra faces telescope from the square at \(x\) to the square \(F\) at \(y\). In the second sum they telescope from the square at \(x\) to the square at \(x\oplus\bigoplus_{j=k+2}^ne_{d_j}\). The two squares at \(x\) cancel, and the remaining second endpoint is the antipode of \(F\), since its corner differs from \(\tau y\) only in the free bits \(a,b\). The cases with either sum empty follow by the same endpoint cancellation. This proves (3). \(\square\)

**Corollary (projective chain homotopy).** On the antipodal quotient \(\pi_B:B_n\to\mathbb{RP}^{n-1}\), the two squares \(F,\tau F\) project to the same cell and cancel. Therefore
\[
\boxed{\pi_{B*}\Sigma_P+\pi_{B*}\Sigma_{P'}=\partial(\pi_{B*}T_k).}
\tag{4}
\]
For any two-cocycle \(\eta\) on the quotient, its evaluations on these two projected exchange disks agree.

The formula was checked independently by cubical boundary expansion on 150 random root-and-order choices for every \(4\le n\le7\), at each adjacent swap position. The proof is uniform for all dimensions.

**Relation to the dimension-simple Wu–Yang adaptation.** Equation (3) supplies a prescribed three-dimensional correction for each Coxeter adjacent transposition, using only ordinary cube faces and an antipodal pair of the two-dimensional exchange squares. The uncolored exchange-disk homotopy is therefore already explicit. The remaining mathematical difficulty is lifting these corrections through the color-sensitive, dimension-preserving reachability records, including coherence for Coxeter braid and commuting relations. No monochromatic-path existence claim follows from (3) alone.

### All-rank Coxeter-generator homotopies and the top boundary defect

This extends the all-rank antipodal cubical resolution of Article XIV, Subsection 33, from a collection of chains indexed by full geodesics to an explicit **chain homotopy under every type-\(B_n\) simple Coxeter generator**, in every rank. The existing three-cube adjacent-swap theorem (Subsection 32) is the rank-two case of one uniform formula. The root-flip generator admits a parallel formula. No edge coloring is restricted.

Work over \(\mathbb F_2\). A complete geodesic flag is \(g=(x,\pi)\), where \(\pi=(d_0,\ldots,d_{n-1})\) is an ordered list of all dimensions. The type-\(B_n\) generators are \(s_0\), which flips the initial-root bit in dimension \(d_0\) without changing \(\pi\), and \(s_i\) for \(1\le i<n\), which transposes dimensions in positions \(i-1,i\), keeping the root fixed. Put \(N=1+\tau\), where \(\tau\) is central cube antipodality.

For any set \(U\subseteq\{0,\ldots,n-1\}\) and any bit function \(q\) on its complement, denote by \([U;q]_x\) the cubical face whose free dimensions are \(d_j\), \(j\in U\), and whose remaining bit in dimension \(d_j\) is \(x_{d_j}+q(j)\). The all-rank chain \(E_k(g)\) has one face for each \(k\)-subset \(U\), with
\[
E_k(g)=\sum_{|U|=k}[U;q_U]_x,\qquad
q_U(j)=|\{r\in U:r>j\}|\pmod2\quad(j\notin U).
\tag{1}
\]
It obeys \(\partial E_k(g)=NE_{k-1}(g)\).

#### Theorem 1 (homotopy for every adjacent-swap generator)

For \(s_i\), \(1\le i<n\), write \(A_i=\{i-1,i\}\). Define \(H_0(g,s_i)=0\), and for \(1\le k\le n-1\) put
\[
\boxed{
H_k(g,s_i)=
\sum_{\substack{R\subseteq[n]_0\setminus A_i\\|R|=k-1}}
[A_i\cup R;q_{i,R}]_x,\qquad
q_{i,R}(j)=
|\{r\in R:r>j\}|+\mathbf1_{\{j<i-1\}}\pmod2,
}
\tag{2}
\]
where \([n]_0=\{0,\ldots,n-1\}\). Then \(H_k(g,s_i)\) contains precisely
\(\binom{n-2}{k-1}\) faces of dimension \(k+1\), and
\[
\boxed{
E_k(g)+E_k(gs_i)
=\partial H_k(g,s_i)+NH_{k-1}(g,s_i),
\qquad 1\le k\le n-1.
}
\tag{3}
\]
At \(k=1\), \(H_1\) is the local square exchanged by the two full geodesics. At \(k=2\), \(H_2\) is the sum of the \(n-2\) three-cubes of Subsection 32.

*Proof.* Compare the face indexed by a fixed \(k\)-subset \(U\) in (1) before and after swapping positions \(i-1,i\). If \(U\) contains both swapped positions, or neither, the face is unchanged, and the two copies cancel. Otherwise \(U\) contains one position of \(A_i\) and some \((k-1)\)-subset \(R\) of the other positions. As \(U\) runs over the two choices of its member in \(A_i\), the four resulting faces (two from each chain) are the four side facets of the single \((k+1)\)-face \([A_i\cup R;q_{i,R}]_x\), with the two exchanged dimensions left free.

The other boundary facets arise by fixing one of the positions \(r\in R\). For each fixed set \(R'\) of size \(k-2\), these facets assemble, as \(r\) runs through the remaining positions in ascending order, into the successive links of a monotone path between the face \([A_i\cup R';q_{i,R'}]_x\) and its antipodal face. Their total modulo-two boundary is \(N[A_i\cup R';q_{i,R'}]_x\). Summing over \(R'\) proves (3). The initial case \(k=1\) has no remaining \(R\)-facets. \(\square\)

#### Theorem 2 (homotopy for the root-flip generator)

For \(s_0\) and \(0\le k\le n-1\), define
\[
\boxed{
H_k(g,s_0)=
\sum_{\substack{R\subseteq\{1,\ldots,n-1\}\\|R|=k}}
[\{0\}\cup R;q_R]_x,\qquad
q_R(j)=|\{r\in R:r>j\}|\pmod2.
}
\tag{4}
\]
This consists of \(\binom{n-1}k\) faces of dimension \(k+1\). With \(H_{-1}=0\), it satisfies
\[
\boxed{
E_k(g)+E_k(gs_0)
=\partial H_k(g,s_0)+NH_{k-1}(g,s_0),
\qquad 0\le k\le n-1.
}
\tag{5}
\]
In particular \(H_0(g,s_0)\) is the initial edge of the complete geodesic.

*Proof.* Flipping the root only in dimension \(d_0\) leaves any \(E_k\)-face whose free set contains position \(0\) unchanged. Faces whose free set omits \(0\) come in pairs at opposite \(d_0\) positions. Each such pair appears as the two boundary facets obtained by fixing dimension \(d_0\) in a unique \((k+1)\)-face of (4). The remaining boundary facets come from fixing one position in \(R\); for every common \((k-1)\)-subset they telescope, in increasing order of the remaining positions, from \(H_{k-1}(g,s_0)\) to its antipodal mate. This gives (5). For \(k=0\), the identity says that the boundary of the initial edge is the two possible initial roots. \(\square\)

#### Theorem 3 (a sharp top-rank distinction)

All correction chains in (2) and (4) with \(k\le n-2\) lie in the cubical boundary sphere \(B_n=\partial[0,1]^n\). But at rank \(k=n-1\),
\[
\boxed{H_{n-1}(g,s)=Q_n}
\tag{6}
\]
for **every** simple Coxeter generator \(s\). Accordingly the preceding identities in the highest rank are
\[
\boxed{
E_{n-1}(g)+E_{n-1}(gs)+NH_{n-2}(g,s)
=\partial Q_n=[B_n].
}
\tag{7}
\]
The right-hand side is the nonzero mod-two fundamental cycle in \(H_{n-1}(B_n;\mathbb F_2)\). Thus the displayed normalized homotopies are internal to the boundary through rank \(n-2\), while their final correction necessarily uses the full ambient \(n\)-cube. This statement is about the explicit homotopies (2) and (4), not an assertion that every other choice of higher correction is impossible.

*Proof.* For \(s_i\), \(i\ge1\), the only \((n-1)\)-rank term in (2) has \(R=[n]_0\setminus A_i\), so its free dimensions are all of \([n]_0\). For \(s_0\), the only term in (4) has \(R=\{1,\ldots,n-1\}\), likewise giving the full cube. A cubical face with at most \(n-1\) free dimensions belongs to \(B_n\). Formula (7) now follows from (3) and (5); its right-hand side is the full cellular boundary of the top cube, representing the mod-two sphere fundamental class. \(\square\)

**Computational audit.** Formulas (2)–(5) were independently expanded and checked as cubical chains for all generator positions, all ranks and dimensions \(2\le n\le7\), including arbitrary initial roots and scrambled dimension orders.

**Proof-search significance.** The all-rank resolution is now compatible by explicit chain homotopies with each of the generators of the complete type-\(B_n\) flag geometry. This is stronger than the rank-two square and three-cube identities: the formulas already account for arbitrary higher dimension sets. To make a chain-valued representation of the Coxeter relations, one must next compare these generator homotopies around the braid and commuting polygons, requiring homotopies of homotopies. Those can be sought inside the same cubical face system. The principal open issue remains a color-sensitive lift of these relations under unrestricted edge coloring; the uncolored homotopies themselves do not imply the desired monochromatic full geodesic.

### Higher coherences for all rank-two type-B Coxeter relations

Continue the antipodal cubical chains \(E_k(g)\) and the generator homotopies \(H_k(g,s)\) from Article XIV, Subsections 33–34. We prove that every rank-two Coxeter relation, including the four-braid involving the initial root, admits an explicit *homotopy of homotopies* in every rank. No assumptions on the edge-coloring class are made.

Let \(g=(x;d_0,\ldots,d_{n-1})\) be a complete geodesic flag. The generator \(s_0\) flips the initial root in dimension \(d_0\), and \(s_i\) for \(1\le i<n\) interchanges the dimensions in positions \(i-1,i\). Put \(N=1+\tau\). For a set \(U\) of dimension positions and a bit assignment \(q\) on its complement, write \([U;q]_x\) for the cubical face with free dimensions \(\{d_j:j\in U\}\) and fixed bits \(x_{d_j}+q(j)\).

For any two generators \(s,t\), let \(m=m(s,t)\) be their Coxeter exponent, which is \(2,3\), or \(4\). Traverse the relation polygon, a cycle of \(2m\) flag edges with alternating generators:
\[
g_0=g\xrightarrow{a_0}g_1\xrightarrow{a_1}\cdots
\xrightarrow{a_{2m-1}}g_{2m}=g,
\qquad a_j\in\{s,t\}.
\]
The corresponding degree-\((k+1)\) correction chain is
\[
B_k(g;s,t)=\sum_{j=0}^{2m-1}H_k(g_j,a_j).
\tag{1}
\]
The first-order homotopy identity from Subsection 34 implies
\[
\boxed{\partial B_k=NB_{k-1},}
\tag{2}
\]
since every \(E_k(g_j)\) appears twice when summed around a closed polygon.

#### The four uniform formulas

Define a core set \(C\) of positions and a base bit function \(q_0\), using the following table. The variable \(r\) is the position at which the bit function is evaluated.

| Relation | Core \(C\) | \(q_0(r)\) outside \(C\) | Initial \(k_0\) |
|---|---|---|---|
| Four-braid \(s_0,s_1\) | \(\{0,1\}\) | \(0\) | \(0\) |
| Ordinary braid \(s_i,s_{i+1}\), \(i\ge1\) | \(\{i-1,i,i+1\}\) | \(\mathbf1_{\{r<i-1\}}\) | \(1\) |
| Root commuting \(s_0,s_j\), \(j\ge2\) | \(\{0,j-1,j\}\) | \(\mathbf1_{\{0<r<j-1\}}\) | \(1\) |
| Disjoint commuting \(s_i,s_j\), \(1\le i<j-1\) | \(\{i-1,i,j-1,j\}\) | \(\mathbf1_{\{i\le r<j-1\}}\) | \(2\) |

In all cases \(k_0=|C|-2\). For \(k_0\le k\le n-2\), define
\[
\boxed{
K_k(g;s,t)=
\sum_{\substack{R\subseteq\{0,\ldots,n-1\}\setminus C\\|R|=k-k_0}}
[C\cup R;q_R]_x,\qquad
q_R(r)=q_0(r)+|\{v\in R:v>r\}|\pmod2.
}
\tag{3}
\]
Set \(K_k=0\) outside that range. Each nonzero \(K_k\) is a \((k+2)\)-chain supported on
\[
\boxed{\binom{n-|C|}{k-k_0}}
\tag{4}
\]
cubical faces, one per admissible additional free dimension set \(R\).

**Theorem 1 (second-level Coxeter coherence in all ranks).** For every \(n\), every full geodesic flag \(g\), every rank-two type-B Coxeter relation and every \(0\le k\le n-1\),
\[
\boxed{
B_k(g;s,t)=\partial K_k(g;s,t)+N K_{k-1}(g;s,t).
}
\tag{5}
\]
Thus the root-flip and adjacent-swap homotopies satisfy the Coxeter braid and commuting identities *up to explicitly prescribed higher cubical chains*.

*Proof.* Separate the dimensions into the core \(C\) of the rank-two relation and all other, spectator, dimensions. When no spectator dimension is free, the relation gives one of four elementary cubical identities.

For the \(s_0,s_1\) four-braid, the four root-edge corrections \(H_0\) traverse the four edges bounding the square in dimensions \(d_0,d_1\), giving \(B_0=\partial K_0\).

For the ordinary braid \(s_i,s_{i+1}\), its six generator-swap square corrections \(H_1\) are the six two-faces bounding the three-cube on its three consecutive dimensions, giving \(B_1=\partial K_1\).

For root commuting \(s_0,s_j\), the root-edge corrections \(H_0\) cancel pairwise; its six noncancelling rank-one square corrections are the boundary of the three-cube on \(\{d_0,d_{j-1},d_j\}\), giving \(B_1=\partial K_1\).

For the commuting pair \(s_i,s_j\) with \(|i-j|\ge2\), the four rank-one corrections cancel in pairs; its eight surviving rank-two three-cube corrections bound the four-cube on \(\{d_{i-1},d_i,d_{j-1},d_j\}\), giving \(B_2=\partial K_2\).

For a fixed nonempty spectator set \(R\), every face of \([C\cup R;q_R]_x\) obtained by fixing a core dimension reproduces the appropriate remaining term in the generator-homotopy sum \(B_k\); the listed \(q_0\) offsets encode the portions of the complete geodesic traversed before the relation's core. The other boundary facets arise by fixing one \(r\in R\). Hold \(R'=R\setminus\{r\}\) fixed and sum over the possible \(r\). Those facets concatenate into a monotone path in the still-fixed spectator dimensions, traversed in increasing position order, whose two ends are \([C\cup R';q_{R'}]_x\) and its full antipodal mate. All intermediate facets cancel over \(\mathbb F_2\). The resulting boundary contribution is \(N K_{k-1}\). Summing over all \(R,R'\) establishes (5). \(\square\)

**Theorem 2 (top-rank location).** For \(k\le n-3\), every \(K_k\) consists of proper cube faces and lies on \(B_n=\partial[0,1]^n\). For \(k=n-2\) and every relation,
\[
\boxed{K_{n-2}(g;s,t)=Q_n,}
\quad\text{hence}\quad
\boxed{B_{n-2}+NK_{n-3}=[B_n].}
\tag{6}
\]
Here \([B_n]\) is the nonzero fundamental mod-two cycle of the cubical boundary sphere.

*Proof.* Each \(K_k\) has dimension \(k+2\). When \(k=n-2\), the only choice of \(R\) in (3) is the full complement of \(C\), so every dimension is free and the term is the full cube. Equation (6) follows from (5) and \(\partial Q_n=[B_n]\). \(\square\)

**Verification and scope.** Equations (3)–(5) were independently checked by explicitly expanding cubical boundaries on every rank-two type-B relation, with arbitrary dimension orders, for \(n\le7\). The proof uses the same cancellation in arbitrary dimension. The theorem constructs the complete set of **rank-two coherence fillers** for this uncolored chain resolution; it does not establish coherence on higher Coxeter residues or a color-compatible chain map. The root- and dimension-order constraints remain visible throughout, and no arbitrary graph-gallery class is introduced. The next step toward Wu–Yang is to lift these second-level homotopies through the monochromatic edge-incidence filtration, then analyze rank-three coherence.

### Rank-two cocycles and the antipodal cover

Let \(L_n\) be the line graph of \(Q_n\), \(n\ge2\): its vertices are the undirected cube edges, with adjacent vertices representing incident edges. It is connected. Antipodal complementation gives a free graph involution \(A\), and the quotient projection \(p:L_n\to L_n/A\) is a connected double cover.

For every antipodally odd binary edge coloring \(c\), define an \(A\)-invariant one-cochain on \(L_n\) by
\[
\epsilon_c(e,f)=c(e)+c(f)\pmod2
\]
for incident cube edges \(e,f\). This bit equals zero precisely when the two-step path through \(e,f\) is monochromatic, equivalently when its rooted Freudenthal triangle lies in the two-color prefix cone of Article XIV.

**Theorem 1 (covering class).** The descended cochain \(\bar\epsilon_c\) on the quotient graph represents the first Stiefel–Whitney class of the covering:
\[
\boxed{[\bar\epsilon_c]=w_1(p)\in H^1(L_n/A;\mathbb F_2).}
\]

*Proof.* A loop in \(L_n/A\) lifts to a path \(e_0,e_1,\ldots,e_r\) in \(L_n\), with \(e_r=A^h e_0\) for the covering-monodromy bit \(h\). The sum of the cochain around that loop telescopes:
\[
\sum_{j=1}^r\epsilon_c(e_{j-1},e_j)
=c(e_0)+c(e_r)=h
\]
by antipodal oddness. This is the defining evaluation of the double-cover class on the loop. \(\square\)

**Theorem 2 (complete rank-two encoding).** Sending \(c\) to its quotient cocycle induces a bijection
\[
\boxed{
\{\text{antipodally odd edge colorings}\}/(c\sim1-c)
\cong
\{\eta\in Z^1(L_n/A;\mathbb F_2):[\eta]=w_1(p)\}.
}
\]

*Proof.* Equality of local comparison cochains for two colorings makes their difference constant across all adjacent cube-edge pairs. Connectivity of \(L_n\) forces global constancy, proving uniqueness modulo complement. Conversely, if \([\eta]=w_1(p)\), the lifted cochain \(p^*\eta\) is a coboundary on \(L_n\), because the covering class pulls back to zero. Integrate \(p^*\eta\) to a function \(c\) on the vertices of \(L_n\), unique up to a constant. Along any path from \(e\) to \(Ae\), the integral equals the covering monodromy of its projected loop, which is one. Therefore \(c(Ae)=1-c(e)\), so \(c\) is a legal coloring inducing \(\eta\). \(\square\)

**Chain-level significance.** The rank-two prefix data remembers the entire unrestricted coloring up to a global color swap. Its cohomology *class*, however, is the fixed covering class and knows no coloring. A Wu–Yang-style full-geodesic proof must exploit the cocycle representative together with the Boolean constraint of disjoint dimension supports; oddness topology without this higher rank structure is insufficient.


#### Cubical switch realizability, legal moves, and criticality

The preceding antipodal line-graph cocycle theorem has a fully intrinsic presentation on projective cube turns. It eliminates the original color bits while retaining the complete unrestricted NORI1 condition.

Write \(Y_n=\partial I^n/A\cong\mathbb RP^{n-1}\), \(G_n=Q_n/A\), \(n\ge3\), and \(m=|E(G_n)|=n2^{n-2}\). A switch system consists of symmetric bits \(s_{[v]}(i,j)\in\mathbb F_2\) for unordered distinct incident dimensions at each projective cube vertex \([v]\).

**Theorem 3 (triangle--square--period characterization).** The system is induced by an antipodally odd coloring of undirected cube edges if and only if:

(i) At each projective vertex, every three distinct directions satisfy
\[
\boxed{s_{[v]}(i,j)+s_{[v]}(j,k)+s_{[v]}(i,k)=0.}
\tag{3}
\]
(ii) On every cube square \(F\) with directions \(i,j\), the four corner switches sum to zero:
\[
\boxed{\sum_{v\in V(F)}s_{[v]}(i,j)=0.}
\tag{4}
\]
(iii) The sum of switch bits along one projective Petrie loop is odd.

If (i)--(ii) hold, all projective Petrie loops have the same switch-sum parity \(p\). Such a system is realized by an edge coloring satisfying \(c(Ae)=c(e)+p\), unique up to global complementation. Thus NORI1 is equivalent to the assertion that every system satisfying (3)--(4) and odd period admits a full dimension-simple Petrie loop with just one active switch.

*Proof.* Comparing three incident edge colors gives (3) by cancellation; summing corner comparisons around a square counts each edge color twice, proving (4). A projected antipodal full geodesic has odd switch sum because the color of its final lifted edge is complemented at the seam.

Conversely choose a reference direction \(r\), and put \(\lambda_r([v])=0\), \(\lambda_i([v])=s_{[v]}(r,i)\). By (3),
\(s_{[v]}(i,j)=\lambda_i([v])+\lambda_j([v])\).
For a projective edge of direction \(i\), define
\[
a([v],[v\oplus e_i])=\lambda_i([v])+\lambda_i([v\oplus e_i]).
\tag{5}
\]
The coboundary of \(a\) on an \(ij\)-square is the four-corner sum (4), so \(a\) is a cocycle on \(Y_n\). Pull it back to \(S^{n-1}=\partial I^n\); its cohomology class vanishes since \(n\ge3\). Consequently there exists a vertex function \(f\) with
\(f(v)+f(v\oplus e_i)=a([v],[v\oplus e_i])\).
Define the undirected edge color
\[
c(\{v,v\oplus e_i\})=f(v)+\lambda_i([v]).
\tag{6}
\]
Equation (5) proves independence of the chosen endpoint, and its local switches recover the prescribed system. Because \(a\) is antipodally invariant, \(p=f(v)+f(\bar v)\) is constant across \(v\); hence \(c(Ae)=c(e)+p\).

For an antipodal path \(v_0,\ldots,v_n=\bar v_0\) using directions \(i_1,\ldots,i_n\), the integral of \(a\) around its projective Petrie loop equals
\[
p=\sum_{j=1}^{n-1}s_{[v_j]}(i_j,i_{j+1})
+s_{[v_0]}(i_n,i_1).
\tag{7}
\]
This is obtained by grouping the endpoint \(\lambda\) terms in the edge sum; the two endpoint contributions meet at one projective vertex. Every Petrie loop represents the nonzero class in \(H_1(Y_n;\mathbb F_2)\), so all its periods agree. Condition (iii) gives \(p=1\). If two colorings realize the same system, their edge-color difference is constant on all edges incident to each vertex, hence constant over the connected cube. They differ by global complementation. A one-switch projective Petrie loop can be cyclically rooted at its unique switch, giving a monochromatic antipodal geodesic, and the converse holds. \(\square\)

**Corollary 4 (linear dimensions).** The switch assignments satisfying just (3)--(4) form a binary vector space of dimension \(m\). The odd-period assignments form an affine subspace of dimension \(m-1\), hence there are \(2^{m-1}\) realizable odd switch systems.

*Proof.* Colorings of both uniform antipodal parities \(p\) have \(m\) independent orbit-edge bits plus \(p\), giving dimension \(m+1\). The linear switch map is onto the triangle--square solution space by Theorem 3. Its kernel is the globally constant color flip, of dimension one. Odd period imposes one nontrivial linear equation. \(\square\)

For each projective edge \(e\in E(G_n)\), let \(T_e\) be the legal operation of flipping the colors on its antipodal pair of cube edges. It toggles the \(n-1\) comparisons involving its direction at either projective endpoint.

**Theorem 5 (sharp affine switch code).** The \(m\) moves \(T_e\) generate all differences between legal odd switch systems. Their only linear relation is
\[
\boxed{\sum_{e\in E(G_n)}T_e=0.}
\tag{8}
\]
The Hamming distance between any two distinct legal odd switch systems is at least \(2(n-1)\). Equality holds if and only if one is obtained from the other by one move \(T_e\) (equivalently, the complementary set of all other moves). The minimum-distance adjacency graph on legal switch systems is the folded \(m\)-cube \(Q_m/A\), of degree \(m\).

*Proof.* The difference of two odd edge colorings is an antipodally even function, so it is represented by a subset \(B\subseteq E(G_n)\). The resulting switch difference is \(\sum_{e\in B}T_e\), and vanishes if and only if the edge-bit difference is constant across all incident edge pairs. Connectedness forces \(B=\varnothing\) or \(B=E(G_n)\), establishing (8).

Let \(d_B(v)\) denote the number of selected edges incident to a projective vertex \(v\). A local turn changes when precisely one of its incident edges is selected; thus
\[
\boxed{d_H(s,s')=\sum_{v\in V(G_n)}d_B(v)(n-d_B(v)).}
\tag{9}
\]
Call \(v\) mixed when \(0<d_B(v)<n\). Every mixed vertex contributes at least \(n-1\). If none is mixed, connectivity forces the change to vanish. Just one mixed vertex is impossible: deleting it leaves a connected graph, so all remaining vertices have the same unmixed state and force it to have that state as well. Therefore a nonzero change has at least two mixed vertices and weight at least \(2(n-1)\).

At equality there are two mixed vertices, while all others are unmixed. The graph \(G_n\) stays connected after deletion of any two vertices: \(G_3=K_4\), and when \(n\ge4\) it has a spanning \((n-1)\)-cube whose vertex connectivity is \(n-1\ge3\). Thus all the remaining vertices have the same unmixed state. Up to replacing \(B\) by its complement, none of their edges is selected. Any selected edge must then join the two mixed vertices, giving just one selected projective edge. Conversely one such edge changes \(2(n-1)\) turn bits. The orbit-edge coloring cube modulo global color complement is \(Q_m/A\), and its minimum-distance adjacency is induced by the \(T_e\). \(\square\)

**Proposition 6 (dimension-simple criticality under legal moves).** A projective edge belongs to \((n-1)!\) Petrie cycles. Flipping its antipodal edge orbit changes only the two switches adjacent to that edge on any containing Petrie loop, and hence changes its grade \(h=(w-1)/2\) by at most one. A grade-one cycle is repaired to grade zero if and only if both adjacent switches were active before the flip.

For \(n\ge4\), if a coloring has no grade-zero cycles and \(H\subseteq E(G_n)\) consists of edges whose atomic flip creates a grade-zero cycle, then
\[
\boxed{|H|\le2Z_1(c),}
\tag{10}
\]
where \(Z_1(c)\) is the number of grade-one Petrie cycles. In particular, a hypothetical bad coloring for which every atomic move creates a monochromatic geodesic must contain at least \(m/2\) grade-one cycles. No claim is made that all bad colorings have this critical property.

*Proof.* Count loop-edge incidences to obtain \(n|\mathcal P_n|/m=(n-1)!\). The local flip toggles two adjacent turn bits and changes their number by \(-2,0,\) or \(2\). To reach grade zero from a coloring having no grade-zero loop, the original loop must have grade one and both toggled turns must be active. Three active turns on an \(n\)-cycle with \(n\ge4\) form at most two adjacent active pairs. Each grade-one cycle therefore witnesses the healability of at most two projective edges, proving (10). \(\square\)

**Research significance.** This presentation is equivalent to the preceding line-graph covering-class reconstruction, but adds native triangle and square constraints, a sharp switch-code distance, and a canonical legal perturbation geometry. One-turn deletion is never a realizable operation for \(n\ge3\); criticality and induction must use the paired edge-star moves or their combinations. These moves preserve the full dimension-simple path family and change each individual witness grade by at most one.



#### The cographic matroid underlying legal switch changes

The preceding cubical presentation admits a succinct graphic-matroid interpretation. Unlike a hypothetical matroid whose bases are full Petrie turn sets, this matroid is intrinsic and exists in every dimension.

Let \(G=Q_n/A\), \(n\ge3\), and \(H=L(G)\). Thus the vertices of \(H\) are the \(m=n2^{n-2}\) projective edge orbits of the cube, and its edges are the
\[
t=2^{n-1}\binom n2
\tag{11}
\]
projective turns, one for each unordered incident pair of distinct projective edge orbits. The graph \(H\) is connected and regular of degree \(2(n-1)\). Write \(\operatorname{Cut}(H)=\operatorname{im}(\delta:C^0(H;\mathbb F_2)\to C^1(H;\mathbb F_2))\).

**Theorem 8 (affine cut-space description and a cycle presentation).** Fix one legal odd coloring and its turn signature \(s_0\). The space of turn signatures of **all** legal odd colorings is
\[
\boxed{s_0+\operatorname{Cut}(H).}
\tag{12}
\]
Its differences are cocycles of the graphic matroid \(M(H)\), or equivalently vectors of the cycle space of the cographic matroid \(M^*(H)\).

Moreover, the entire binary cycle space \(Z_1(H;\mathbb F_2)\) is generated by the following three families of cycles of \(H\):

(a) triangles formed by three projective edges incident with one vertex of \(G\);

(b) four-cycles formed by the four successive projective edges of each cubical square of \(G\);

(c) any one cycle formed by the sequence of projective edges of a complete Petrie loop of \(G\).

The local triangle cycles are linearly independent across projective vertices up to the usual local \(K_n\) triangle dependencies; their span has rank
\[
\boxed{2^{n-1}\binom{n-1}{2}.}
\tag{13}
\]
Modulo this span, the square cycles have rank \((n-2)2^{n-2}\), and one Petrie cycle contributes the last independent relation. In particular, these families collectively have cycle rank
\[
\boxed{\dim Z_1(H;\mathbb F_2)=t-m+1.}
\tag{14}
\]

*Proof.* Relative to the fixed coloring \(c_0\), the difference of any other odd coloring \(c\) descends to a bit \(b_e=c(e)+c_0(e)\) for each projective edge orbit \(e\), i.e. a vertex function \(b\) on \(H\). The comparison at a turn between orbit-edges \(e,f\) changes by \(b_e+b_f=(\delta b)(ef)\). Conversely, every vertex labeling \(b\) can be implemented by flipping the indicated antipodal edge orbits. This proves (12).

The turn comparison sum around a triangle in a local \(K_n\) is condition (3). The comparison sum around the four-cycle in \(H\) corresponding to a cubical square is condition (4). The sum around a Petrie line-graph cycle is its global projective switch period. By Theorem 3, a cochain \(z\in C^1(H;\mathbb F_2)\) has zero sum on all triangles, squares and the chosen Petrie cycle if and only if its local reconstruction has period zero, i.e. if and only if \(z=\delta b\) for some vertex function on \(H\). Therefore the orthogonal complement of the span of those cycles is \(\operatorname{Cut}(H)\). By cut--cycle orthogonality for connected graphs, that span is the full cycle space \(Z_1(H;\mathbb F_2)\).

For each vertex \(v\) of \(G\), the \(n\) orbit-edges incident with \(v\) form a clique \(K_n\) in \(H\). Its triangle cycles span a space of rank \(\binom{n-1}{2}\). Distinct projective vertices give disjoint sets of turn edges in \(H\), because two distinct edges of the simple graph \(G\) share at most one endpoint. Hence the local triangle spaces form a direct sum, proving (13).

Contracting the local triangle-cycle relations leaves the ordinary cycle space of \(G\). The projective cubical squares generate \(B_1(Y_n;\mathbb F_2)\), whose dimension is
\[
|E(G)|-|V(G)|+1-\dim H_1(Y_n;\mathbb F_2)
=m-2^{n-1}.
\]
Since \(H_1(Y_n;\mathbb F_2)\cong\mathbb F_2\) and every Petrie loop represents its nonzero element, the squares and any one Petrie cycle generate the remaining graph-cycle relations, contributing \((n-2)2^{n-2}\) and one dimension. Summing with (13) gives \(t-m+1\). \(\square\)

**Corollary 9 (the relevant matroid and its bonds).** The set of all legal switch *differences* is the cocycle space of the graphic matroid \(M(H)\). The elementary support-minimal nonzero differences are the bonds of \(H\), the circuits of the cographic matroid \(M^*(H)\). Its shortest bonds have size \(2(n-1)\), and Theorem 5 shows they are precisely the stars of individual vertices of \(H\), corresponding to flips of one projective cube edge orbit.

The natural switch-criticality induction should therefore use **cographic bonds and unions of bonds**, with the shortest bond acting on both endpoints of a projective cube edge. This is compatible with the earlier non-matroid theorem for complete Petrie turn sets: the cographic matroid governs *legal color-switch changes*, not which collections of turns constitute complete paths.

*Proof.* In a graph, nonzero cut vectors decompose into bonds, and bonds are the cocircuits of its graphic matroid, equivalently circuits of the dual. Theorem 5 identifies all minimum-size cut vectors and their support. \(\square\)

**Consequence for the covering obstruction.** The global antipodal twist appears here as the value one on the chosen Petrie cycle in the cycle-space presentation. All local triangle and cubical-square periods vanish; one distinguished noncontractible projective cycle detects the parity class. This is an explicit finite presentation of the projective covering class on \(H\), while the cographic bond structure describes every legal perturbation of its representative.


Atomic switch energy. Write m=n*2^(n-2) for the projective cube edge count, N for the total number of active projective turns, and d(e) for the active turns incident to the projective edge e. Flipping the antipodal edge orbit e gives N(new)-N(old)=2(n-1)-2d(e). Summing over e gives 2m(n-1)-4N, since every active turn is incident to two projective edges. Consequently N>m(n-1)/2 forces some legal atomic flip to decrease the switch support. This identity is valid for all antipodally odd colorings and uses only the intrinsic line-graph cut structure.

**Theorem (critical near-good witness bound).** Assume \(n\ge4\), a NORI1 counterexample exists, and \(c\) minimizes its projective switch support \(N\) among counterexamples. Let \(Z_1\) be its number of grade-one Petrie cycles. Set \(F=\{e:d(e)>n-1\}\), with \(d(e)\) the number of active turn comparisons incident to the projective edge \(e\). Then
\[
\boxed{2Z_1\ge |F|\ge
\max\{0,(2N-m(n-1))/(n-1)\}.}
\]
In particular the earlier universal necessary bound \(N\ge3\cdot2^{n-2}(n-1)\) for any counterexample gives
\[
\boxed{Z_1\ge2^{n-3}\max(0,6-n).}
\]

*Proof.* An edge \(e\in F\) has a support-decreasing legal flip by the atomic energy identity. The flipped coloring cannot remain bad, since \(c\) minimizes support among bad colorings. Hence that flip creates a grade-zero Petrie loop. Before the flip this loop must have grade one, with both turns adjacent to \(e\) active. Three active turns on a cyclic word of length \(n\ge4\) contain at most two adjacent active pairs, so any single grade-one loop can witness at most two such edges. This gives \(|F|\le2Z_1\). Every \(e\notin F\) has \(d(e)\le n-1\); every \(e\in F\) has \(d(e)\le2(n-1)\). Since \(\sum_e d(e)=2N\), we have \(2N\le m(n-1)+|F|(n-1)\), giving the lower bound on \(|F|\). Substitute the necessary bad-coloring density to obtain the last inequality. \(\square\)

The bound becomes vacuous at dimension six, exposing the limit of one-edge first-variation arguments. This is a conditional criticality theorem; it does not presume existence of counterexamples.

Atomic stationarity classification (proved). If every projective edge-orbit flip preserves total switch support, then n is even and every direction-i edge has color sum_{j!=i} x_j + a_i modulo two. Conversely all these affine odd colorings are stationary. The proof sums the endpoint switch-degree equations to obtain (A+(n-2)I)(s-n/2)=0 for the cube adjacency A and s(x)=number of incident one-edges. The Walsh eigenvalue -(n-2) forces s-n/2 to be a combination of size-(n-1) Walsh characters. Adding at neighboring vertices isolates each coefficient, which must be plus or minus one half; this reconstructs the asserted edge colors. For even n the reader matrix I+J squares to I over F2, so the affine Petrie distribution theorem gives n!/2 favorable Petrie loops. Therefore every bad coloring at or above the average atomic energy has some support-decreasing legal flip.

**Detailed spectral proof and full path certificate.** Write \(s(x)=\sum_{i=1}^n c_i(x)\) as an ordinary integer, and let \(d(e)\) denote the number of active turn comparisons involving the projective edge \(e\). If the color of \(e=\{x,y=x\oplus e_i\}\) is \(b\), then \(d(e)=s(x)+s(y)\) when \(b=0\), and \(d(e)=2n-s(x)-s(y)\) when \(b=1\). Stationarity sets \(d(e)=n-1\), so
\[
s(x)+s(x\oplus e_i)=n-1+2c_i(x).
\]
Summing over \(i\) gives \((A+(n-2)I)(s-n/2)=0\), with \(A\) the cube adjacency operator. Its eigencharacters are \(\chi_S(x)=(-1)^{\sum_{j\in S}x_j}\) of eigenvalue \(n-2|S|\). Therefore
\[
s(x)-n/2=\sum_i b_i\chi_{[n]\setminus\{i\}}(x).
\]
Add this expression at \(x\) and at \(x\oplus e_i\). Every term cancels except that indexed by \(i\). Comparing with the edge equation yields
\[
2b_i\chi_{[n]\setminus\{i\}}(x)=2c_i(x)-1\in\{-1,1\}.
\]
Hence each \(b_i=\pm1/2\), and each edge color is the parity of all input bits other than \(i\), possibly complemented. For odd \(n\), such a function is antipodally even and cannot be a legal odd coloring. For even \(n\), substitution verifies stationarity.

A direct monochromatic path certificate is available without the affine distribution theorem. For any dimension ordering \(\pi=(\pi_1,\ldots,\pi_n)\), put
\[
x_{\pi_t}=t-1+a_{\pi_t}+B\pmod2,\qquad B\in\mathbb F_2.
\]
Before the \(t\)-th step, the vertex parity is \(\sum_i x_i+t-1\), while the bit in dimension \(\pi_t\) is still \(x_{\pi_t}\). Thus the edge color is
\(\sum_i x_i+t-1+x_{\pi_t}+a_{\pi_t}=\sum_i x_i+B\), independent of \(t\). Every dimension ordering therefore has a monochromatic realization at two antipodal roots. The reader matrix \(I+J\) is invertible for even \(n\), giving the complete binomial Petrie count and \(Z_0=n!/2\).

At dimension six, the necessary bad-coloring switch support satisfies \(N\ge3\cdot2^{n-2}(n-1)=m(n-1)/2\). If \(N\) is larger, the summed atomic variation is negative, so some edge flip lowers \(N\). At equality, the absence of a lowering flip forces all variations to vanish, contradicting the favorable-path certificate. Hence any hypothetical bad \(Q_6\) coloring has a support-decreasing legal flip, although this alone does not prove that the original coloring has a good path.

### Endpoint residual barriers and corrected transverse oscillation

This subsection records the endpoint consequences of complementary monochromatic arms. An earlier version applied the residual-face gluing theorem at the common root of the arms. Its residual face is instead based at an arm endpoint. The assertions of a barrier at every interior corridor vertex, the resulting corridor-wide ordinary-curvature oscillation, and the associated one-sided exchange-defect profile are withdrawn.

Let c be an antipodally odd coloring of Q_n, and suppose it has no monochromatic full antipodal geodesic. Let P=(v_0,...,v_m) be a red dimension-simple path, and let M be its unused directions.

#### Theorem 1 (endpoint residual-face barriers)

Every full path through the M-face based at v_0, starting at v_0, contains a descent 10. The same holds at v_m. If m>0 and |M|>=2, the two disjoint endpoint faces together contain at least 2|M|(|M|-1) descending directed two-edge turns.

*Proof.* At v_0 take the empty red arm and the whole path P as the other arm. The residual-face gluing theorem then has its starting corner v_0. Repeat from v_m with reversed P. The two faces are disjoint when m>0. Apply the sharp residual-face turn bound separately. Splitting P at an interior vertex produces arms ending at v_0 and v_m, so it gives these same endpoint faces, rather than an additional face at the splitting vertex. QED.

For |M|=1 the endpoint barrier is impossible, recovering the full-geodesic extension principle for a monochromatic path of length n-1.

#### Theorem 2 (translated color oscillation in codimension two)

Let M={a,b}. At each endpoint u in {v_0,v_m}, the residual square is a gate:
\[
c_a(u)=c_b(u)=1,\qquad c_b(u+a)=c_a(u+b)=0.
\]
For h in {a,b}, let w_j^(h) be the color of the j-th edge of P+h. Then the word w^(h) contains both 01 and 10.

*Proof.* Both residual square routes must descend, giving the displayed gates. For k the other unused direction, the path consisting of the h-edge at v_0, then P+h, then the k-edge to the antipode of v_0 has word 1 w^(h) 0. It uses every direction once. If w^(h) had no 01, this full word would have at most one switch, which yields a monochromatic full path by root sliding. Reversing P gives 1 rev(w^(h)) 0, forcing 10 as well. Only the two endpoint gates are used. QED.

In particular, a hypothetical bad coloring cannot contain a monochromatic (n-2)-path when n<=4, since its translated word is too short to have both transitions.

#### The strip formula and its scope

Put h_j=c_h(v_j), let d_j be the j-th direction of P, and put
\[
\kappa_j^{(h)}=\kappa(F_{\{h,d_j\}}(v_{j-1})).
\]
Since P is red,
\[
w_j^{(h)}=\kappa_j^{(h)}+h_{j-1}+h_j\pmod2.
\]
Consequently the corrected curvature word on the right has both transitions. Endpoint gates give h_0=h_m=1 and hence
\[
\sum_j\kappa_j^{(h)}=\sum_jw_j^{(h)}\pmod2.
\]
They do not force the interior h_j to equal one. Ordinary curvature need not coincide termwise with the translated color word by this argument. Likewise, the earlier corner-independent one-sided Freudenthal defect formula requires blue transverse edges at both ends of each individual side square; that condition has only been established for a side square when its two transverse edges are separately known to be blue.

At either endpoint, a full monochromatic face path supplies both ordinary monotone orientations. The adjacent parallel face roots at that endpoint are empty by the two-step lift. This proves at least two empty roots in each adjacent face when m>=1. It does not prove the former 2m bound. Interior seams and transverse edge colors remain part of the unrestricted closure problem.


### Boundary triple-overlap cocycles and the common antipodal cover

For \(n\ge5\), define the graph \(O_n\) on injective ordered triples of \(n\) original vertices, with adjacency \(abc\sim bcd\) when \(a,b,c,d\) are distinct. Triple reversal \(R(abc)=cba\) is a free graph involution.

**Lemma 1 (connectivity).** The graph \(O_n\) is connected.

*Proof.* Given five distinct symbols \(a,b,c,d,e\), the paths
\[
abc\sim bcd\sim cde\sim acd\sim bac,
\qquad
abc\sim dab\sim eda\sim dac\sim acb
\]
exchange the first two or last two positions. Furthermore \(abc\sim eab\sim abd\) replaces the third entry \(c\) by an unused \(d\). Adjacent exchanges allow the replacement to occur in any position. Thus all injective triples are connected. Reversal sends the first overlap edge \(abc\sim bcd\) to \(dcb\sim cba\); no triple or undirected overlap edge is fixed, by injectivity. \(\square\)

Let \(b\) be an arbitrary reversal-odd boundary 3-tournament, so \(b(c,h,a)=1-b(a,h,c)\). Set
\[
\epsilon_b(t,u)=b(t)+b(u)\pmod2
\]
on adjacent triples. The cochain is invariant under reversal, so descends to \(\bar\epsilon_b\) on the quotient \(O_n/R\).

**Theorem 2.** If \(p:O_n\to O_n/R\) is the double covering, then
\[
\boxed{[\bar\epsilon_b]=w_1(p)\in H^1(O_n/R;\mathbb F_2).}
\]
The assignment \(b\mapsto\bar\epsilon_b\) also gives a bijection
\[
\boxed{
\{\text{reversal-odd boundary tournaments}\}/(b\sim1-b)
\cong
\{\eta\in Z^1(O_n/R;\mathbb F_2):[\eta]=w_1(p)\}.
}
\]

*Proof.* Lift any closed walk in the quotient to a path \(t_0,\ldots,t_m\) ending at \(R^h t_0\), where \(h\in\mathbb F_2\) is its covering monodromy. Summing its comparison bits telescopes to \(b(t_0)+b(R^h t_0)=h\). Thus the comparison class evaluates on every loop as the covering class.

If two legal triple colorings have the same comparison bits, their difference is constant on the connected graph \(O_n\), giving uniqueness modulo complement. Conversely, a quotient cocycle in class \(w_1(p)\) pulls back to a coboundary on \(O_n\). Integrate it to a triple-color function \(b\). Its integral from \(t\) to \(Rt\) is one, hence it obeys reversal oddness. \(\square\)

**Common structure with NORI1.** The earlier cube-edge incidence cocycle theorem uses the line graph \(L(Q_n)\), whose vertices are undirected cube edges; its involution is antipodal edge translation. For a cube coloring \(c\), the comparison bit on adjacent edges is \(\epsilon_c(e,f)=c(e)+c(f)\). It obeys the same two theorems. Accordingly both unrestricted colorings, modulo global color exchange, correspond to cocycle representatives of the canonical first Stiefel–Whitney class of a connected local-incidence double cover.

The **full-rank path constraint is indispensable**. Hamilton tight paths advance through *directed* overlapping triples using each original vertex once. Cube geodesics advance through consistently concatenated edges using each dimension once. Their switch counts equal sums of the respective comparison cocycle along the associated incidence sequence. Arbitrary walks in either incidence graph need not decode into admissible full paths. The next Wu–Yang-style argument must use the particular cocycle representative and its support-preserving higher path geometry; the covering class alone is independent of the coloring and insufficient.

### Interior exchanges preserve switch parity; endpoint exchanges control odd defects

Let \(c:E(Q_n)\to\mathbb F_2\) be an arbitrary coloring of undirected cube edges, with antipodal oddness imposed where stated. For a rooted full geodesic \(P(x,\pi)\), write \(w_j=c(e_j)\) and
\[
S(x,\pi)=\sum_{j=1}^{n-1}\mathbf1_{\{w_j\ne w_{j+1}\}}
\]
for its number of switches.

**Lemma 1 (endpoint parity).** For every binary word \(w\),
\[
\boxed{S(w)\equiv w_1+w_n\pmod2.}
\tag{1}
\]
If \(c\) is antipodally odd, define \(a_i(x)=c(\{x,x\oplus e_i\})\). Then
\[
\boxed{S(x,\pi)\equiv1+a_{\pi_1}(x)+a_{\pi_n}(x)\pmod2.}
\tag{2}
\]

*Proof.* The sum modulo two of neighboring comparison bits \(w_j+w_{j+1}\) telescopes to \(w_1+w_n\). The first edge of \(P(x,\pi)\) has color \(a_{\pi_1}(x)\), while its last edge is the antipodal mate of the edge incident to \(x\) in dimension \(\pi_n\), so \(w_n=1+a_{\pi_n}(x)\). Substitution proves (2). \(\square\)

**Theorem 2 (interior-exchange two-step law).** Let \(n\ge4\), and suppose \(\pi'\) differs from \(\pi\) by exchanging the dimensions at positions \(j,j+1\), with
\[
2\le j\le n-2.
\]
Then
\[
\boxed{S(x,\pi')-S(x,\pi)\in\{-2,0,2\}.}
\tag{3}
\]
No antipodal condition is needed for (3). In particular a single interior exchange cannot create or eliminate precisely one color switch.

*Proof.* Both geodesics start at \(x\), agree in their first \(j-1\) edges, traverse the two opposite routes through the same dimension-\(\{\pi_j,\pi_{j+1}\}\) square, and rejoin at the same cube vertex. Thus their color words agree outside positions \(j,j+1\). Write the common bits immediately before and after the square as \(A=w_{j-1}=w'_{j-1}\), \(B=w_{j+2}=w'_{j+2}\). The only possibly changed comparisons are
\[
(A,u,v,B)\quad\hbox{versus}\quad(A,u',v',B),
\]
where \(u,v,u',v'\) are the colors of the two routes through the square. For any binary pair \((u,v)\), the number of changes among the three comparisons has parity \(A+B\) and lies between 0 and 3. Therefore its difference for two pairs is in \(\{-2,0,2\}\). All other comparisons agree, proving (3). \(\square\)

**Proposition 3 (zero square curvature still permits a jump of two).** For \(n\ge4\) there are valid antipodally odd cube colorings and interior neighboring orders whose word segments are
\[
(A,u,v,B)=(0,0,0,0),\qquad
(A,u',v',B)=(0,1,1,0).
\]
Then the switch count increases by two, although the square curvature
\[
\kappa(F)=u+v+u'+v'=0\pmod2.
\tag{4}
\]

*Proof.* Choose any root and any dimension order with the exchanged positions interior, for instance \(n=4\), \(\pi=(1,2,3,4)\), and \(\pi'=(1,3,2,4)\). Color the common first and fourth edges zero, both edges of the \(2\)-then-\(3\) route zero, and both edges of the \(3\)-then-\(2\) route one. These six edges have distinct antipodal orbits; in a dimension different from those of the square their fixed bits distinguish the parallel edges from antipodal mates. Complete each orbit by giving the antipodal edge the complementary bit. The color words are \(0000\) and \(0110\), with zero and two switches, respectively, while (4) holds. \(\square\)

**Corollary 4 (two parity sectors at a cube root).** Fix \(x\) and ordered first and last dimensions \(p,q\ne p\). Every complete geodesic from \(x\) beginning with \(p\) and ending with \(q\) has the same switch-count parity,
\[
S\equiv1+a_p(x)+a_q(x)\pmod2.
\tag{5}
\]
The intermediate dimension orders are connected by interior adjacent exchanges and the switch count changes by zero or two at each exchange. In a hypothetical NORI1 counterexample, when \(a_p(x)=a_q(x)\) every such word must have at least three switches; when \(a_p(x)\ne a_q(x)\), every such word must have at least two switches.

*Proof.* Equation (5) follows from Lemma 1. The permutations of the remaining \(n-2\) dimensions are connected by swaps among positions \(2,\ldots,n-1\), each interior in the sense of Theorem 2. If no one-switch or monochromatic full geodesic exists, every full word has at least two switches; combine this with the parity distinction. \(\square\)

#### Consequence for a Wu–Yang-type filtered chain argument

The rank-two color-comparison data produces a **parity-preserving exchange geometry** whenever both ends of the complete path are held fixed. The only adjacent dimension exchanges that can change the parity of the switch count are those touching the first or last position; the type-B sign-flip move changing the root can alter many later color bits without a uniform local switch bound. This independently explains the endpoint-sensitive exceptional parabolic cells identified earlier by the second-switch obstruction.

In particular, an equivariant correction scheme that attempts to use only ordinary cubical square curvature is insufficient: Proposition 3 exhibits a filtration jump without curvature. Such a scheme must retain the ordered neighboring color comparisons (or an equivalent switch filtration), as well as the distinct dimensions, when constructing its higher chain homotopies.
