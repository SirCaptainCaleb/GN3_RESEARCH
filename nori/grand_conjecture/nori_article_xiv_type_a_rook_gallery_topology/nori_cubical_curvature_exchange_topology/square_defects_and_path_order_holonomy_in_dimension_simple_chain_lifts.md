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
