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

### Transverse curvature oscillation along near-spanning monochromatic geodesics

This subsection extracts an all-dimensional rigidity theorem from the complementary-arm residual-face barrier (Article XIV, Subsection 41). It directly links full-rank monochromatic reachability to **changes of ordinary square curvature along two transverse strips**. No restricted coloring subclass, regularity condition, or small-order enumeration is assumed.

Let \(n\ge3\), \(D=[n]\), and let \(c\) be any undirected binary cube-edge coloring with \(c(\tau e)=1-c(e)\). Use red \(0\), blue \(1\), and let \(\kappa(F)=\sum_{e\subset\partial F}c(e)\pmod2\). Suppose, for contradiction, that \(c\) admits **no monochromatic full antipodal geodesic**. Equivalently, it admits no full antipodal geodesic with at most one color change, since moving the root across the unique change converts such a path into a monochromatic one.

#### Theorem 1 (a residual-face barrier propagates along an entire monochromatic geodesic)

Let \(P=(v_0,v_1,\ldots,v_m)\) be a monochromatic red cube geodesic of length \(m=n-|M|\), where \(M\ne\varnothing\) is the set of dimensions not traversed by \(P\). For every \(0\le t\le m\), and for every permutation \(\sigma\) of \(M\), the monotone path across the face
\[
F_t=F_M(v_t)
\tag{1}
\]
starting at \(v_t\) and following the dimensions of \(M\) in order \(\sigma\) has a blue-to-red descent \(1\to0\).

The \(m+1\) residual faces \(F_0,\ldots,F_m\) are pairwise distinct and have disjoint vertex sets. If \(|M|\ge2\), each face contains at least \(|M|(|M|-1)\) descending directed two-edge turns, so the union of these faces contains at least
\[
\boxed{(n-|M|+1)|M|(|M|-1)}
\tag{2}
\]
distinct such turns.

*Proof.* Split \(P\) at \(v_t\) into its initial and terminal portions and reverse the first portion. These give two red geodesics from \(v_t\) to \(v_0\) and \(v_m\), with disjoint dimension supports partitioning \(D\setminus M\). Apply the two-arm residual-face gluing theorem of Subsection 41, at root \(v_t\). If a monotone route through the face \(F_M(v_t)\) lacked a blue-to-red descent, then gluing the two red arms across that route would give a complete antipodal geodesic with at most one switch, contrary to hypothesis. The faces \(F_t\) have free dimensions \(M\), and the fixed bits outside \(M\) are the pairwise different vertices of the simple geodesic \(P\). Hence they are pairwise disjoint. Each has at least \(|M|(|M|-1)\) descending two-edge turns by the sharp residual-face turn inequality of Subsection 41. Disjointness makes the counts additive. \(\square\)

For \(|M|=1\), the theorem gives an immediate contradiction: a one-edge path has no two-edge descent. This recovers the observation that a monochromatic geodesic of length \(n-1\) forces a full monochromatic antipodal geodesic somewhere.

#### Theorem 2 (the two transverse curvature words must oscillate in both directions)

Suppose \(|M|=2\), say \(M=\{i,j\}\). Write \(m=n-2\), and let \(d_t\) be the dimension traversed from \(v_{t-1}\) to \(v_t\), \(1\le t\le m\). Then at every vertex \(v_t\) of \(P\),
\[
\boxed{
c_i(v_t)=c_j(v_t)=1,\quad
c_j(v_t\oplus e_i)=c_i(v_t\oplus e_j)=0.
}
\tag{3}
\]
For each missing dimension \(a\in\{i,j\}\), define a **transverse curvature word**
\[
\boxed{
W^{(a)}_t
=\kappa\!\left(F_{\{a,d_t\}}(v_{t-1})\right),
\qquad 1\le t\le m.
}
\tag{4}
\]
Then each \(W^{(a)}\) contains **both** transitions
\[
\boxed{01\quad\text{and}\quad10}
\tag{5}
\]
as adjacent two-letter subwords. Equivalently, the curvature of the successive side squares is neither nonincreasing nor nondecreasing. In particular, each of the two strips contains a curved square and a flat square, and has at least two changes in its curvature word.

*Proof.* The two-dimensional part of Theorem 1 says that for every \(t\), both monotone paths across \(F_{\{i,j\}}(v_t)\) must have color word \(10\). This gives the blue-out/red-in gate (3).

For \(a=i\), the strip square \(F_{\{i,d_t\}}(v_{t-1})\) has longitudinal base edge \(v_{t-1}v_t\) red, and its two transverse dimension-\(i\) edges incident with \(v_{t-1},v_t\) are blue by (3). Their contributions cancel modulo two, so
\[
\boxed{
W^{(i)}_t
=c(\{v_{t-1}\oplus e_i,v_t\oplus e_i\}).
}
\tag{6}
\]
The same argument holds with \(i\) replaced by \(j\). Thus the curvature word along either strip is the color word of the translated path \(P+a\), which uses all dimensions of \(D\setminus\{i,j\}\) once.

For either \(a\), let \(b\) be the other missing dimension. Starting from \(v_0\), take the blue dimension-\(a\) edge to \(v_0+a\), traverse the translated path \(P+a\), and finally take the red dimension-\(b\) edge from \(v_m+a\) to \(v_m+i+j=\tau v_0\). The gate (3) guarantees both endpoint colors. This is a complete dimension-simple antipodal geodesic with word
\[
\boxed{1\,W^{(a)}\,0.}
\tag{7}
\]
If \(W^{(a)}\) had no ascending transition \(01\), its word would belong to \(1^*0^*\), so (7) would have at most one change, contradicting the hypothesis. Thus \(W^{(a)}\) contains \(01\).

Now reverse the original red geodesic \(P\). Its vertices run from \(v_m\) back to \(v_0\), so it remains red and the same gates (3) hold at each vertex. Repeating the construction from the reversed path gives the complete word
\[
1\,\operatorname{rev}(W^{(a)})\,0.
\]
It must also have more than one switch, forcing an ascending transition \(01\) in the reversed curvature word, equivalently a descending transition \(10\) in \(W^{(a)}\). This proves (5). \(\square\)

**Corollary 3 (two-dimensional long-path obstruction).** Every red geodesic using all but two dimensions in a hypothetical NORI1 counterexample determines two **different transverse square-curvature strips**. Along each strip the curvature must change at least twice, in both binary directions; in particular each contains at least one face of curvature \(1\) and one of curvature \(0\). The \(n-1\) parallel residual squares along the original path have curvature zero and carry the unique blue-out/red-in pattern. The same theorem holds with the colors exchanged.

For \(n=4\), the translated strip words have length \(2\) and cannot contain both kinds of transition. Therefore Theorem 2, together with the earlier rank-\((n-1)\) geodesic extension principle, rules out any monochromatic geodesic of length \(n-2\) in a hypothetical counterexample. This is an incidental low-dimensional consequence; the theorem's main content is the uniform all-rank curvature-oscillation requirement.

**Remark (why this is stronger than the square gate alone).** The flatness of each residual \(\{i,j\}\)-square is a single local parity condition. Theorem 2 forces *variability of the ordinary curvature on other squares*, in two separate dimensions, **along the entire ordered red path**. The two transitions are constrained in the path's dimension order. This is new color-sensitive incidence information that the projective class \([\bar\kappa]\) does not capture by itself. It is a necessary condition under the no-full-geodesic hypothesis, not a proof that such a coloring exists. The next proof question is whether the imposed red-prefix corridor barriers and two transverse curvature oscillations can be incompatible with the all-rank Coxeter exchange homotopies after aggregating them across roots and dimension orders.

#### Corollary 4 (one-sided Freudenthal defects on every transverse strip)

Under Theorem 2's hypotheses, consider the side square
\[
G_t^{(a)}=F_{\{a,d_t\}}(v_{t-1}),\qquad a\in\{i,j\}.
\]
Let \(\Omega_b(G_t^{(a)};z)\) denote the mod-two parity of monochromatic color-\(b\) two-step routes across this square, rooted at any corner \(z\) of the square (as in Subsections 21 and 39). Then **for all four corners**,
\[
\boxed{
\Omega_0(G_t^{(a)};z)=0,\qquad
\Omega_1(G_t^{(a)};z)=\kappa(G_t^{(a)})=W_t^{(a)}.
}
\tag{8}
\]
Thus the blue exchange-defect sequence along each strip contains both binary transitions \(01\) and \(10\), while the red exchange defect vanishes identically along that strip.

*Proof.* The longitudinal base edge in dimension \(d_t\) has color \(0\). Both transverse edges in dimension \(a\) have color \(1\) by the gate condition (3). The remaining longitudinal edge has color \(W_t^{(a)}\), by equation (6). The two root-based routes therefore have respective color words \(01\) and \(1W_t^{(a)}\). Neither route is red-monochromatic; precisely one is blue-monochromatic if and only if \(W_t^{(a)}=1\). This proves (8) at the base corner. The formula for the two root-relative route counts is unchanged at the other corners, because the two parallel \(a\)-edges both have color \(1\), giving zero parallel-edge discrepancy in dimension \(a\). Apply the root-corner transport identity in Subsection 31 to conclude corner independence. The oscillation assertion follows from Theorem 2. \(\square\)

**Implication for color-filtered chain corrections.** Along any near-spanning red geodesic under a hypothetical counterexample, the two transverse strips are rank-simple sequences of adjacent squares with \(\Omega_0=0\) and non-monotone \(\Omega_1\). This supplies a forced, position-dependent pattern **directly on the internal Freudenthal facet defects** of Subsection 39, rather than only on their color-blind sum. For a blue base geodesic, the two color roles are interchanged. Any proposed global cancellation must respect these one-sided defect profiles, since they follow from the original unrestricted coloring and the no-full-geodesic assumption.

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
