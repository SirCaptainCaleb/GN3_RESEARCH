# Square defects and path-order holonomy in dimension-simple chain lifts

# Square defects and path-order holonomy in dimension-simple chain lifts

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

## Theorem 1 (monochromatic square defect and three-dimensional coherence)

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

## Theorem 2 (path composition alone cannot repair the square cancellation)

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

## Two independent square effects and the proposed correction

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

## Theorem 3 (root-slide repair of a boundary square exchange)

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

## Theorem 4 (matching obstruction to connectivity under root-sensitive boundary repairs)

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

## Sharp odd-dimensional square-curvature systole and reversal transgression

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


## Complete curvature-code realizability and antipodal vertex gauges

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


## Rigidity of all curvature minimizers in odd dimension

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


## Vertex-gauge path-word laws within a fixed curvature fiber

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


## Independent adjacent-order repairs within a fixed curvature class

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


## Every curvature fiber has abundant red-rooted full geodesics

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


## Antipodal vertex-star gauges and critical geodesic transversals

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


## Universal sparse star-gauge profile correction

For any n>=3, any legal antipodally odd cube-edge coloring c, and any target direction-indexed geodesic color profile s, there exist at most floor((n-1)/2) antipodal vertex-pair star flips taking c to a legal coloring c' realizing profile s on a full antipodal geodesic. All square curvatures are preserved, and at most 2n floor((n-1)/2) edges change color. This holds without restrictions on the nonlinear edge rules.

Proof. Fix one rooted full geodesic P with direction order p_0,...,p_{n-1}, and put a_j=c(P_j P_{j+1}) xor s_{p_j}. Extend the discrepancy word by a_{j+n}=1 xor a_j. Sliding the starting root forward k edges and moving the original prefix to the end using antipodal edges yields a full geodesic with discrepancy window (a_k,...,a_{k+n-1}). Its parity is parity(a_0,...,a_{n-1}) xor (k mod 2). Select a shift k with even discrepancy parity. Integrating these discrepancies along the shifted path yields vertex potential values H_0=0 and H_{j+1}=H_j xor a_{k+j}, and even parity ensures H_n=H_0. The first n visited vertices represent distinct antipodal vertex pairs, so the H_j extend to an antipodally invariant potential, which removes every discrepancy by its edge gradient. Complementing all H_j on those n visited pairs produces the same correction along the chosen path. One may therefore use at most min(weight(H_0,...,H_{n-1}),n-weight), no more than floor(n/2), star flips. This proves the required bound for odd n.

For even n>=4, choose k in {0,1} so that shift k has even discrepancy parity. Then k+2 also has even parity. Define B_0=0 and B_{j+1}=B_j xor a_j over the twice-length twisted word, and let Z_k be the integer count of ones among B_k,...,B_{k+n-1}. The even window gives B_{k+n}=B_k, while the intermediate odd window gives B_{k+n+1}=1 xor B_{k+1}. Therefore
\[
Z_{k+2}-Z_k=1-2B_{k+1}\in\{-1,1\}.
\]
So these two even-parity windows cannot both have balanced weight n/2. At least one requires at most n/2-1 antipodal star flips. This is floor((n-1)/2) for even n, completing the proof.

An independent program nori_star_covering_radius.cpp exhaustively verifies all 64 legal Q3 colorings and all 65536 legal Q4 colorings against all possible target profiles, constructing each repaired path and checking its edge colors. It also checks 2000 random legal Q5 colorings with 15 target profiles per coloring. Separate enumeration of all binary discrepancy words through length 16 corroborates the uniform cyclic-window radius. This is a deterministic polynomial-size recoloring theorem, not a proof that the unmodified coloring realizes the target or that NORI1 holds.
