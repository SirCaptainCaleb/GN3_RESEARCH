# Odd girth and frustration of switch component quotients

### Systolic and maximum-cut constraints on switch-component graphs

Let \(p:T\to H\) be a connected free double cover of a connected comparison graph, and let a legal odd coloring yield a quotient switch cocycle \(\eta\) with support \(S\). Let \(Z=(V(H),E(H)\setminus S)\). Contract every connected component of \(Z\) to obtain the connected multigraph \(F\), retaining all switches as edges, including possible loops. These objects are the cographic deletion normal form of the preceding gauge-criticality Subsection.

**Theorem 1 (short odd cycle survives all nonswitch contractions).** Suppose \(H\) contains a closed walk \(C\) of length at most \(L\) whose lift under the double cover joins a state to its involutive mate. Then \(F\) contains an odd circuit of length at most \(L\), with loops counted as odd circuits of length one.

*Proof.* Every legal switch cochain represents the covering class, so \(\sum_{e\in C}\eta(e)=1\pmod2\). Contracting nonswitch edges maps \(C\) to a closed walk in \(F\); the walk traverses precisely the switched edges of \(C\), counted with multiplicity, and has odd length at most \(L\). Every odd closed walk in a multigraph decomposes into circuits, at least one of which has odd length no greater than the walk. QED.

**Corollary 2 (uniform odd-girth bounds in the two unrestricted models).** For any antipodally odd edge coloring of \(Q_n\), the component multigraph \(F\) has odd girth at most \(n\), attained as an upper bound by following a full projective dimension-simple Petrie loop of length \(n\). For any reversal-odd ordered-triple coloring on \(n\ge5\) symbols, \(F\) has odd girth at most six, using the six-step reversal-monodromy walk in the preceding local-cycle Subsection.

**Theorem 3 (quantitative persistent frustration).** Let \(m=|S|=|E(F)|\). Then
\[
\boxed{m-\operatorname{MaxCut}(F)\ \ge\
\begin{cases}
(n-1)2^{n-2},& H=L(Q_n)/J,\quad n\ge3,\\[2pt]
\dfrac{n-4}{4(n-3)}\,|E(H)|,&H=O_n/R,\quad n\ge6.
\end{cases}}
\tag{1}
\]
Consequently, if \(m\) exceeds the respective lower bound by fewer than \(\lambda(F)\) edges, then the zero-switch graph \(Z\) must be connected.

*Proof.* By the cographic deletion theorem, deleting a maximum cut of \(F\) is legal and removes \(\operatorname{MaxCut}(F)\) switches without adding others. The resulting odd coloring has \(m-\operatorname{MaxCut}(F)\) switched comparisons. Every legal cube comparison cochain has at least \((n-1)2^{n-2}\) switches, by the sharp Petrie-averaging cosystole calculation. Every legal reversal-odd triple comparison cochain has at least \(((n-4)/(4(n-3)))|E(H)|\) switches, by the complementary signed-spectral bound in the matroid generalizations section. This proves (1). If \(Z\) is disconnected, \(F\) has at least two vertices and therefore admits a nonempty cut of size at least \(\lambda(F)\). The maximum cut is at least that large, so (1) implies \(m\) is at least the lower bound plus \(\lambda(F)\). Contraposition proves the connectivity criterion. QED.

**Corollary 4 (frustration survives every legal monotone reduction).** The maximum-cut residual graph is still forced to contain an odd circuit of length at most the monodromy length bound from Corollary 2, and its remaining number of switched comparisons obeys (1). Thus no sequence of legal switch deletions can collapse the odd class to a bipartite component quotient; its frustrated core carries both a short odd-cycle certificate and a globally extensive support constraint.

**Interpretation.** The inherited short odd cycle is a *local witness of nonzero covering monodromy*, whereas the maximum-cut deficit measures the global complexity of maintaining that monodromy across all comparisons. The boundary model differs sharply from the cube: its residual signed switch support is a positive fraction of all turns asymptotically, while the cube can reach fraction \(1/n\). Neither statement by itself forces a spanning Hamilton path with one switch or a dimension-simple monochromatic cube geodesic. Their combined constraints provide quantitative tests for proposed switch-critical counterexamples and legal deletion strategies.

## A Minty-compatible walk metric retaining length and direction excess

The toolkit entry *Minty's walk-potential proof: paths emerge by extremality* suggests optimizing over walks with an additive local cost, and recovering simplicity by shortening. For balanced NORI1 there is a direct graph model with unit local costs.

Fix even \(n=2m\ge4\) and an antipodally odd cube-edge coloring \(c\). Let \(R(c)\) be its spanning color-zero subgraph, and let
\[
M=\{\{x,\bar x\}:x\in Q_n\}
\]
be the antipodal perfect matching. Define
\[
K(c)=(Q_n,E(R(c))\cup M).
\tag{WM1}
\]
Matching edges are distinguished from cube edges. They are different edges since \(n\ge4\).

For a nonempty cube walk \(W\) from some \(x\) to \(\bar x\), let \(L(W)\) be its length and let \(w_1,\ldots,w_L\) be its color word. Define its completed turn count
\[
g(W)=\sum_{t=1}^{L-1}[w_t\ne w_{t+1}]+[w_L=w_1],
\qquad
\Psi(W)=L(W)+g(W).
\tag{WM2}
\]
The integer \(g(W)\) is positive and odd. Both the starting root and the walk are variable.

**Theorem (walk minimum as ordinary odd girth).**
\[
\boxed{
\min_{W:x\leadsto\bar x}\Psi(W)=\operatorname{og}(K(c))
=n+1+2q(c)
}
\tag{WM3}
\]
for some integer \(q(c)\ge0\). The graph \(K(c)\) is connected and nonbipartite. Furthermore,
\[
\boxed{\text{NORI1 holds for }c\iff q(c)=0.}
\tag{WM4}
\]

*Proof.* Contracting \(M\) identifies every antipodal vertex pair. Each antipodal pair of cube edges has precisely one zero member, so the contracted graph is the folded cube. It is connected, proving connectedness of \(K(c)\).

If \(K(c)\) had a proper binary vertex labeling \(f\), its matching edges would force \(f(\bar x)=1-f(x)\). The zero cube edges force different labels at their ends. The antipodal image of each one-colored cube edge is zero, so the same inequality holds across every one-colored edge as well. Thus \(f\) would be a proper binary labeling of the full cube, necessarily its parity labeling up to a constant. For even \(n\), that labeling satisfies \(f(\bar x)=f(x)\), a contradiction. Hence \(K(c)\) is nonbipartite.

Given \(W\), replace each color-one block by its antipodal image; it becomes zero. Join consecutive blocks by an edge of \(M\), and use a closing matching edge precisely when \(w_L=w_1\). This gives a closed walk in \(K(c)\) with \(L(W)\) cube edges and \(g(W)\) matching edges. Its cube-edge count is even, because \(n\) is even and \(W\) is antipodal, and its matching-edge count is odd. It is therefore an odd closed walk of length \(\Psi(W)\). It contains an odd cycle no longer than itself, giving one inequality in (WM3).

Conversely, take a shortest odd cycle \(C\) in \(K(c)\). Cube edges reverse cube-vertex parity, whereas matching edges preserve it. Thus \(C\) has an even number of cube edges and an odd number \(r\) of matching edges. Consecutive matching edges would be an immediate reversal of one edge, impossible in a simple cycle. Unroll the zero-edge segments by alternating antipodal translation across the matching edges. They become a cube walk \(W\) joining a root to its antipode, whose color blocks alternate. Its completed turn count is \(r\), and \(\Psi(W)=|C|\). This proves the equality of minima.

The XOR of the increments around \(C\) is zero. Its odd number of matching edges contributes the all-ones vector. Consequently each cube direction occurs an odd positive number of times among its cube edges. There are at least \(n\) cube edges and at least one matching edge, so \(|C|\ge n+1\). Its odd length has the form in (WM3). Equality requires one matching edge and one occurrence of every cube direction. Deleting that matching edge gives a zero full antipodal geodesic. Conversely a zero full geodesic together with its antipodal matching edge is an odd cycle of length \(n+1\). This proves (WM4). \(\square\)

**Corollary (balanced regular model).** If \(c\) is vertex-balanced, \(K(c)\) is \((m+1)\)-regular. It retains the cube-edge lengths discarded by the switch-component contractions earlier in this Subsection. The global closure target is the sharp odd-girth equality
\[
\operatorname{og}(K(c))=2m+1
\tag{WM5}
\]
for these regular graphs.

**Additive potential over arbitrary walks.** Construct \(H(c)\subset Q_{n+1}\) with vertices \((x,b)\). Include every vertical edge \((x,0)(x,1)\), and for each cube edge \(xy\) of color \(b\), include the horizontal edge \((x,b)(y,b)\). The map
\[
(x,b)\longmapsto
\begin{cases}x,&b=0,\\ \bar x,&b=1,\end{cases}
\]
is a two-sheeted cover of \(K(c)\), with deck map
\(\tau_H(x,b)=(\bar x,1-b)\).
It is the bipartite double cover. Each walk has ordinary additive length, every nonempty closed excursion has positive length, and shortest walks are paths. Thus
\[
\boxed{
\operatorname{og}(K(c))
=\min_{z\in H(c)}\operatorname{dist}_{H(c)}(z,\tau_Hz).
}
\tag{WM6}
\]
For any source \(z\), the Bellman potential
\(d_z(u)=\min\{|P|:P\text{ is any }z\text{-to-}u\text{ walk in }H(c)\}\)
is finite and obeys \(|d_z(u)-d_z(v)|\le1\) on every edge. Under balance, \(H(c)\) is \((m+1)\)-regular. This gives the requested walk relaxation with a local additive cost and automatic ordinary cycle erasure. Its outstanding metric assertion is that some deck pair has distance \(n+1\), the ambient cube distance.

### Why the retained complementary-edge rule matters

Connectedness, regularity, antipodal symmetry and a full direction matching alone allow larger antipodal distance. An explicit example makes the additional structure visible.

In \(Q_4\), the cyclic direction word
\[
(0,1,0,2,1,0,1,3)^2
\tag{WM7}
\]
traces an antipodally invariant Hamiltonian cycle \(C_{16}\). Starting at zero, its first half visits
\(0,1,3,2,6,4,5,7,15\); the second half is its antipodal image. Every cyclic four-letter window repeats a direction, so this cycle contains no full four-direction geodesic. Its antipodal distance is eight at every vertex.

For every \(k\ge1\), the graph \(C_{16}\square Q_k\) is a connected antipodally invariant spanning subgraph of \(Q_{k+4}\), is \((k+2)\)-regular, contains all edges in each added direction, and has antipodal distance \(k+8\). Thus its degree fraction tends to one while its antipodal distance exceeds the cube distance by four.

The color-layer graph \(H(c)\) has a further restriction: for each old cube edge \(xy\), precisely one of the parallel horizontal edges at layer zero and layer one is present. Equivalently, in \(K(c)\), precisely one cube edge from each antipodal edge pair is retained. This rule carries the original odd coloring. Any potential argument for (WM5) must retain it together with regularity.

Independent enumeration verified the cycle, its antipodal symmetry and its absence of four-direction geodesics. The structural identities above are proved in every stated dimension.


## Antipodal spectral compression and the moment positivity bottleneck

The odd-girth model admits an equivalent matrix formulation retaining the distinction between the unconstrained spectral data and the required cube-edge positivity.

Let \(n=2m\), let \(A\) be the adjacency matrix of \(Q_n\), let \(M\) be the permutation matrix of vertexwise antipodal complementation, and let \(Z\) be the adjacency matrix of the color-zero cube-edge subgraph for an antipodally odd coloring \(c\). Put
\[
P_+=(I+M)/2,\qquad P_-=(I-M)/2.
\]
These are the orthogonal projections onto functions symmetric and antisymmetric under antipodal complementation.

**Theorem (fixed diagonal spectral compressions).** Every legal coloring satisfies
\[
\boxed{MZM=A-Z,\qquad
P_\pm ZP_\pm=\tfrac12P_\pm AP_\pm.}\tag{SC1}
\]
In the normalized Walsh-character basis \(\chi_S(x)=2^{-n/2}(-1)^{\sum_{i\in S}x_i}\), order the even-cardinality and odd-cardinality characters separately. Then
\[
\boxed{
Z=\begin{pmatrix}X&B\\B^{\mathsf T}&Y\end{pmatrix},\qquad
X\chi_S=(m-|S|)\chi_S\ (|S|\ {\rm even}),\quad
Y\chi_T=(m-|T|)\chi_T\ (|T|\ {\rm odd}).
}\tag{SC2}
\]
Thus all coloring dependence lies in the off-diagonal Walsh-parity block \(B\). Independently of the coloring,
\[
\boxed{\|B\|_F^2=n\,2^{n-3}.}\tag{SC3}
\]
If \(c\) is vertex-balanced, the rows of \(B\) indexed by \(S=\varnothing\) and \(S=[n]\) vanish, and \(\|Z\|_{\rm op}=m\).

*Proof.* Each cube edge belongs to one antipodal pair, and oddness retains its zero member while its antipodal mate is one; hence \(Z+MZM=A\). The matrices \(M,A\) commute. Multiplying the preceding equality on both sides by \(P_\pm\), on which \(M\) acts as \(\pm I\), gives (SC1). The Walsh basis diagonalizes \(M\) with eigenvalue \((-1)^{|S|}\) and diagonalizes \(A\) with eigenvalue \(n-2|S|\), proving (SC2).

Set \(D=2Z-A\). Its entries on oriented cube edges are \(\pm1\), and all other entries vanish. Hence \(\operatorname{tr}D^2=n2^n\). Equation (SC1) gives \(MDM=-D\), so in the Walsh parity decomposition \(D=\begin{psmallmatrix}0&2B\\2B^{\mathsf T}&0\end{psmallmatrix}\), and \(\operatorname{tr}D^2=8\|B\|_F^2\). This proves (SC3).

Vertex balance gives \(Z\mathbf1=m\mathbf1\). The cube bipartition sign \(\chi_{[n]}\) anticommutes with every cube-edge adjacency, so \(Z\chi_{[n]}=-m\chi_{[n]}\). These are the two extremal even-Walsh modes; their off-diagonal couplings must vanish. Finally an \(m\)-regular undirected graph has adjacency operator norm \(m\). \(\square\)

**Theorem (positive odd-cycle moment criterion).** For even \(n\), let \(K=M+Z\) and \(N_0(c)\) count unoriented monochromatic-zero full antipodal geodesics. Then
\[
\boxed{
2N_0(c)=\operatorname{tr}(MZ^n)
=\operatorname{tr}(P_+Z^nP_+)-\operatorname{tr}(P_-Z^nP_-),
}\tag{SC4}
\]
and
\[
\boxed{\operatorname{tr}(K^{n+1})
=(n+1)\operatorname{tr}(MZ^n)=2(n+1)N_0(c).}\tag{SC5}
\]
Consequently the even-dimensional NORI1 assertion is equivalent to a **strictly positive supertrace** in (SC4) for every legal cube-edge operator \(Z\).

*Proof.* The diagonal entry \((MZ^n)_{xx}\) counts length-\(n\) zero walks from \(x\) to \(\bar x\). Any such walk must traverse each cube direction once, so it is a geodesic. Summing over roots counts each unoriented path twice, proving (SC4). In any closed walk of length \(n+1\) on \(K\), an odd number \(r\) of matching edges is used: cube edges reverse cube-vertex parity while matching edges preserve it, and the walk has odd length. The matching edges together toggle every cube bit, so the cube edges must use each direction an odd positive number of times. There are at least \(n\) cube edges, hence \(r=1\) and every cube direction occurs once. Cyclically choosing the location of that one matching edge gives \(n+1\) copies of \(\operatorname{tr}(MZ^n)\), establishing (SC5). \(\square\)

**Proposition (coarse spectral constraints do not force positivity).** In dimension \(n=6\), one can form a real symmetric block matrix \(Z\) of the form (SC2) that satisfies the fixed diagonal compressions, has \(\|B\|_F^2=48\), annihilates the constant and full-parity extremal rows of \(B\), has operator norm \(3\), and anticommutes with the cube bipartition sign, but satisfies
\[
\boxed{\operatorname{tr}(MZ^6)=-17136/25<0.}\tag{SC6}
\]
Thus these spectral constraints alone are insufficient: the missing cube-edge support and entrywise nonnegativity cannot be discarded in a proof.

*Construction and verification.* In the even-Walsh block \(X\), the diagonal values are \(3\) once, \(1\) fifteen times, \(-1\) fifteen times, and \(-3\) once. In the odd block \(Y\) they are \(2\) six times, \(0\) twenty times, and \(-2\) six times. Leave the extremal \(X\)-modes uncoupled. Connect the thirty remaining even modes to distinct odd modes by a signed weighted matching, with absolute weight \(b=\sqrt{8/5}\): six pairs of diagonal values \((1,2)\), nine of \((1,0)\), nine of \((-1,0)\), and six of \((-1,-2)\). Leave the other two odd zero-modes uncoupled. Choose opposite weights on the paired Walsh-complement entries, ensuring anticommutation with the cube bipartition sign (which sends \(\chi_S\) to \(\chi_{[6]\setminus S}\)). Then \(\|B\|_F^2=30b^2=48\).

Every coupled \(2\times2\) block is
\(\begin{psmallmatrix}x&b\\b&y\end{psmallmatrix}\)
up to sign of \(b\). Its eigenvalues lie between \(-3\) and \(3\), since for \((x,y)=(1,2)\) they are \((3\pm\sqrt{37/5})/2\), for \((1,0)\) they are \((1\pm\sqrt{37/5})/2\), and the negative-value pairs are their negatives. The uncoupled extremal modes have eigenvalues \(\pm3\). Hence \(\|Z\|_{\rm op}=3\).

For a \((1,2)\) or \((-1,-2)\) block the difference of the sixth diagonal powers is \(-9(b^2+1)(b^2+7)=-5031/25\); for a \((1,0)\) or \((-1,0)\) block it equals \((b^2+1)(3b^2+1)=377/25\). Adding the two isolated sixth powers \(3^6\) and \((-3)^6\) gives
\[
\operatorname{tr}(MZ^6)
=2(3^6)+12(-5031/25)+18(377/25)
=-17136/25.
\]
This matrix is not a nonnegative cube-edge adjacency matrix; indeed a negative value of (SC4) proves that it cannot be one. \(\square\)

**Closure interpretation.** Antipodal oddness makes the diagonal Walsh-compression operators universal, and vertex balance isolates their two extreme modes. Nevertheless, these linear-algebraic constraints and the uniform norm bounds do not ensure the desired moment sign. Any spectral proof of unrestricted NORI1 must exploit the pointwise edge-support and positivity constraints on \(Z\), or an equivalent nonlinear compatibility identity. This is an all-dimensional reformulation and a counterexample to a possible proof shortcut, not a proof of the conjecture.


### Direction involutions retain the missing cubical exchange relations

The spectral compression (SC1)--(SC6) becomes a faithful matrix description of legal colorings only after reinstating the directionwise support and Boolean constraints. These admit concise generator relations.

For each direction i let \(U_i\) be the permutation matrix of the bit flip \(x\mapsto x^i\), and let \(P_i\) be the diagonal projection with entries \(P_i(x,x)=[c_i(x)=0]\). Define
\[
Z_i=P_iU_i,\qquad S_i=(2P_i-I)U_i,\qquad
Z=\sum_i Z_i.
\]

**Theorem (Boolean directional generators and twisted square exchange).** For every legal antipodally odd coloring,
\[
\boxed{
[P_i,U_i]=0,\quad P_i^2=P_i,\quad
MP_iM=I-P_i,\quad
Z_i^2=P_i,\quad Z_i^3=Z_i,\quad
S_i^{\mathsf T}=S_i,\quad S_i^2=I,\quad MS_iM=-S_i.
}\tag{SC7}
\]
For distinct directions i,j let \(s_i(x)=(-1)^{c_i(x)}\). Define the square-curvature sign
\[
\kappa_{ij}(x)=s_i(x)s_j(x^i)s_j(x)s_i(x^j)\in\{\pm1\}.
\]
As matrices,
\[
\boxed{
S_iS_j=\operatorname{diag}(\kappa_{ij})\,S_jS_i.
}\tag{SC8}
\]
The sign \(\kappa_{ij}\) is constant on each \(i,j\) square and is invariant under antipodal complementation. It equals \(-1\) precisely when the square has odd total edge-color sum.

For even n, the full zero-geodesic count has the faithful direction-word expression
\[
\boxed{
2N_0(c)=\sum_{\pi\in\mathfrak S_n}
\operatorname{tr}\left(MZ_{\pi_1}Z_{\pi_2}\cdots Z_{\pi_n}\right),
\qquad Z_i=(U_i+S_i)/2.
}\tag{SC9}
\]

*Proof.* The color of an undirected i-edge is independent of its i-bit, giving commutation of \(P_i,U_i\). The Boolean nature of its edge color gives \(P_i^2=P_i\). Antipodal oddness exchanges zero and one edges, hence \(MP_iM=I-P_i\), while the direction flips commute with M. The stated polynomial and involution relations follow immediately. Evaluating \(S_iS_j\) and \(S_jS_i\) on a basis vertex \(x\) gives coefficients \(s_i(x)s_j(x^i)\) and \(s_j(x)s_i(x^j)\) on the same vertex \(x^{i,j}\). Their ratio is the four-edge square sign \(\kappa_{ij}(x)\), proving (SC8). Edge undirectedness makes that sign constant around the square; oddness complements all four factors under the antipodal map, preserving the product.

Expand \(Z^n\) into all ordered n-tuples of direction operators. The trace with M can be nonzero only if the XOR of these n direction flips is the all-ones vector. Since every direction then has odd positive multiplicity, all n directions occur once. Only permutations remain, proving (SC9). Every trace summand is a nonnegative integer counting zero full geodesics of that direction order from their two possible orientations. \(\square\)

**Proof target.** To close NORI1 in this representation one must use (SC7)--(SC8) and the entrywise-support constraints to establish that at least one summand in (SC9) is positive. The real symmetric counterexample (SC6) shows why retaining only the fixed Walsh compressions, operator norm, balance, and antipodal parity is inadequate. The square-curvature relations are the local exchange operations available to a Minty-style argument; no argument forcing the desired positive summand has yet been established.


## Isometric shortest odd cycles and folded-cube projection

Fix even n>=4 and a legal antipodally odd coloring c. Let K(c) comprise the zero-colored cube edges plus the antipodal matching, and let C be a **shortest odd cycle** of length L, containing r matching edges.

**Theorem (isometric projective normal form).**
(i) C is isometric in K(c): for any vertices u,v on C, their distance in K(c) equals the shorter arc distance on C. It is therefore induced.
(ii) If both u and its antipode occur on C, their matching edge belongs to C.
(iii) After contracting its r matching edges and projecting to the folded cube Q_n/(x~bar x), C becomes a **simple projective cycle** of length L-r; each cube direction occurs an odd positive number of times. There exist s,t>=0 with
\[
\boxed{r=2t+1,\qquad L-r=n+2s,\qquad L=n+1+2(s+t).}\tag{MP1}
\]
(iv) If two vertices u,v on C represent adjacent folded-cube vertices, then their shorter arc distance on C is at most three. In particular, a folded-cube chord cannot join original cycle vertices separated by four or more steps. At excess L=n+3 there are only two defect modes: r=1 and one repeated direction occurring three times, or r=3 with every direction occurring once.

*Proof.* Suppose vertices u,v on C have arc lengths a<=b, a+b=L odd, but admit a K(c)-path of length d<a. Joining this path with the two arcs yields closed walks of lengths d+a and d+b, both less than L; one is odd because a,b have opposite parities. It contains a shorter odd cycle, contradiction. This proves isometry and inducedness. The antipodal matching connects any u,bar u, so inducedness forces this edge onto C whenever both endpoints occur, proving (ii).

Cube edges switch vertex-weight parity, while antipodal matching edges preserve it because n is even. The number of cube edges in the odd cycle is even, hence r is odd. XORing all edge displacements around C shows that the cube-edge direction counts have parity r modulo two in every direction; consequently each is odd and positive. Contracting the r matching edges cannot identify any further vertices under antipodal quotient, by (ii), so the projected cycle is simple, proving (iii) and (MP1).

Folded adjacency of the orbits of u,v means either v=u^i or v=bar(u^i). In the former case the i-edge u,v is zero and supplies a K-path of length one, or its antipodal mate is zero and supplies a K-path u,bar u,bar v,v of length three. In the latter case one of the i-edges u,bar v and bar u,v is zero, and a matching edge produces a path of length two. Therefore d_K(u,v)<=3, and isometry proves (iv). \(\square\)

**Audited obstruction to merely local shortening.** In dimension eight there exists a legal coloring with an isometric eleven-cycle, with cube-direction word
\[
(4,2,3,5,0,7,0,6,1,0)
\tag{MP2}
\]
from integer-coded root 0 to antipode 255, closed by its one matching edge. Its eleven cycle vertices are
\(0,16,20,28,60,61,189,188,252,254,255\).
Nevertheless the same coloring has a zero full antipodal geodesic from root zero with direction order
\[
(5,0,1,2,3,7,4,6),
\tag{MP3}
\]
hence a globally shorter odd cycle of length nine.

To reproduce, for every direction-i undirected edge let x be its endpoint whose i-bit is zero. Set \(a=\min(x,(x\oplus255)\mathbin{\&}\neg2^i)\) and
\[
c_i(x)=\mathbf1[x\ne a]\oplus\mathbf1[a\in T_i],
\]
with the following eight sets of integer-coded representative lower endpoints:
\[
\begin{array}{c|l}
0&0,62,66,124,126\\
1&0,1,16,28,60,61,80,92,124\\
2&24,48\\
3&16,48,52,84,116\\
4&64\\
5&16,20,24,30,84,92,94\\
6&0,3,20,28,30,52,60,61,62\\
7&60,62
\end{array}\tag{MP4}
\]
Antipodal oddness is immediate from the representative convention. Independent graph construction and BFS verified the zero edges of (MP2), isometry between all pairs of cycle vertices, and the separate zero geodesic (MP3). An initial mixed-integer model accidentally omitted upper bounds on forced zero edge bits; its output was rejected. The corrected model enforced equality on all fixed bits, and the independent graph BFS confirmed the result.

**Scope.** The normal form is an all-dimensional necessary condition on any hypothetical globally shortest odd cycle; it does not exclude positive odd-girth excess. The dimension-eight witness shows that an isometric longer odd cycle need not be globally shortest. A closure argument must exploit competition between different cycles, beyond mere arc-shortcut elimination.


## Universal reduction to the first odd-girth excess and a three-matching witness

The shortest-odd-cycle program has a **closure-equivalent first-excess restriction**. It avoids any dimension ladder or growing defect classification.

For a fixed even \(n\ge2\), denote by \(\mathcal C_n\) the Boolean hypercube of all antipodally odd edge colorings of \(Q_n\), with one bit per antipodal edge-pair orbit. Two colorings are adjacent when they flip one orbit. A coloring is good if it has a monochromatic full antipodal geodesic and bad otherwise. The graph \(\mathcal C_n\) is connected, and its good subset is nonempty: prescribe the edges of one full geodesic to be zero, their antipodes one, and color the other edge orbits arbitrarily.

**Theorem (critical first-excess reduction).** For every even \(n\ge2\), the following are equivalent:

1. A bad antipodally odd coloring exists in dimension \(n\).
2. A bad coloring exists in dimension \(n\) with a full antipodal geodesic whose color word has just one one-colored edge (or, after antipodal reflection, one zero-colored edge).
3. A bad coloring exists in dimension \(n\) whose odd-cycle graph \(K(c)\) has a shortest odd cycle of length \(n+3\) containing **three antipodal matching edges**, while its \(n\) cube edges use all \(n\) directions once.

In particular, the existence of **any** NORI1 counterexample in any dimension implies the existence of a counterexample in some even dimension with
\[
\boxed{\operatorname{og}(K(c))=n+3}
\tag{CE1}
\]
and a globally shortest three-matching-edge cycle. Therefore to prove unrestricted NORI1, it suffices to rule out **bad** colorings having a one-defect full geodesic; equivalently to rule out bad colorings whose \(K(c)\) has a three-matching-edge cycle of length \(n+3\). No statement for excess levels \(n+5,n+7,\ldots\) is needed.

*Proof.* Suppose a bad coloring exists. Take any path in the connected coloring hypercube from that bad coloring to a good coloring. At its first edge between a bad coloring \(c\) and a good coloring \(c'\), one antipodal edge-pair orbit changes. Choose a color-zero full antipodal geodesic \(P\) in \(c'\) (if necessary antipodally translate a monochromatic-one geodesic). A full geodesic uses every direction once and so meets any antipodal edge-pair orbit at most once. If \(P\) avoided the flipped orbit, it would also be a zero geodesic in bad \(c\). Thus \(P\) meets the flipped orbit on one edge \(e=uv\), which is one in \(c\) and zero in \(c'\); all other edges of \(P\) are zero in \(c\). This proves (1) implies (2).

Given the one-defect full geodesic \(P\) from root \(x\) to \(\bar x\), replace its unique one-colored edge \(u v\) by the three-edge path
\[
\boxed{u\ \longrightarrow\ \bar u\ \longrightarrow\ \bar v\
\longrightarrow\ v}
\tag{CE2}
\]
in \(K(c)\). The first and last edges are in the antipodal matching. The middle edge \(\bar u\bar v\) is zero because \(c\) is antipodally odd. Every other edge of \(P\) is already zero in \(K(c)\). Finally close the resulting walk by the matching edge \(\bar x x\). This constructs an odd closed walk of length \(n+3\) with three matching-edge occurrences and \(n\) cube-edge occurrences, all in distinct cube directions.

The general odd-girth lower bound is \(n+1\). Because \(c\) is bad, no odd cycle of length \(n+1\) exists. The length-\((n+3)\) odd closed walk thus must itself be a simple odd cycle: otherwise decomposing it at a repeated vertex would give a shorter odd cycle, and no such cycle is permitted. It is consequently a **globally shortest** odd cycle with the required three matching edges. This proves (2) implies (3). Finally, (3) explicitly asserts that c is bad, proving (3) implies (1).

An odd-dimensional bad coloring lifts to the next even dimension by using the original coloring identically in the two horizontal facets and choosing the bridge-edge colors to be antipodally odd in the old variables. Every monochromatic full geodesic in the enlarged cube would project to a monochromatic full geodesic in the old cube, so badness persists. Thus excluding the even-dimensional first-excess configuration proves the unrestricted conjecture. \(\square\)

**Corollary (interior critical pivot).** In a bad coloring, the lone one-colored edge of a one-defect full geodesic cannot be its initial or terminal step. If it were, root sliding would produce a monochromatic full geodesic. In the three-matching cycle (CE2), this is also forced by its simplicity: a terminal defect would make one of the two newly inserted matching edges coincide with the closing matching edge.

**Precise closure target.** Any hypothetical bad example can be replaced, in the same even dimension, by a bad-good boundary example possessing a **dimension-simple path with precisely one isolated wrong-color edge**. In the odd-girth graph, it has the distinguished three-matching-edge simple shortest cycle of length \(n+3\). A valid global exchange theorem need only exclude this first-excess cycle in a *bad coloring*. Merely finding an isometric \(n+3\) cycle is insufficient, as the separately audited eight-dimensional example shows: such a cycle may coexist with a shorter \(n+1\) cycle elsewhere. The essential task is to force a distinct shorter cycle from the near-monochromatic geodesic, using the antipodal complementarity of the remaining edges and the resulting path-root interactions.


## An exponentially large family of globally shortest three-matching cycles in any hypothetical bad coloring

The first-excess reduction (CE1)--(CE2) strengthens markedly when combined with the independently proved maximizing-facet/private-pivot theorems in the gauge-critical Subsection. The latter apply without structural restrictions to any hypothetical antipodally odd NORI1 counterexample.

Fix even n>=4 and suppose there is a bad coloring. Among all bad colorings of Q_n choose c maximizing the absolute red/blue imbalance over all codimension-one facets, and choose a maximizing facet F, interchanging color names if necessary so that color zero is in the majority on F. Let D be the set of color-one edges of F. The established geodesic-blocker minority bound gives
\[
\boxed{
|D|\ge2^{n-2}+\delta_n,\qquad
\delta_n=\left\lceil\frac{2^{n-3}}{1+(n-1)(n-2)}\right\rceil>0.
}\tag{FM1}
\]

**Theorem (critical isometric-cycle congestion).** Every e in D determines a zero full antipodal geodesic P_e after flipping the antipodal orbit of e, and P_e in the original bad c contains e as its sole one-colored edge, strictly internally. Replacing this defect edge by matching--zero--matching and adding its antipodal closing matching edge gives a globally shortest simple odd cycle C_e of K(c), with
\[
\boxed{|C_e|=n+3,\qquad \#(C_e\cap M)=3.}\tag{FM2}
\]
Each C_e is isometric, and its projection to the folded cube is a simple direction-rainbow projective cycle of length n. The folded-chord restriction (MP2) holds for every C_e simultaneously.

Orient every P_e to start in F. It crosses a unique **zero-colored** edge \(b(e)\) perpendicular to F after traversing its exceptional edge e. There are only \(2^{n-2}\) zero-colored perpendicular edges, by antipodal oddness. Hence
\[
\boxed{
\sum_{\substack{b\perp F\\c(b)=0}}
\bigl(|\{e\in D:b(e)=b\}|-1\bigr)_+
\ge |D|-2^{n-2}\ge\delta_n.
}\tag{FM3}
\]
Thus, if any bad coloring exists, it has an imbalance-extremal representative exhibiting **many globally shortest three-matching cycles whose associated nearly monochromatic antipodal geodesics collide at common zero bridges**. The previously published same-facet injection theorem further ensures distinct cycles for distinct e; without invoking that theorem, each three-matching cycle has at most three candidate defect edges between its three matching pairs, so a weaker linear multiplicity bound would suffice.

*Proof.* For each e in D, the antipodal orbit flip changes its color-one facet edge into color zero and strictly increases the absolute imbalance of F. Since c maximizes facet imbalance among bad colorings, the flipped legal coloring is good. Choose a zero full antipodal geodesic in the flipped coloring. It must contain e, not its antipodal mate bar e: the two differ only on the flipped orbit, and only e was changed from one to zero. In c the resulting path is zero except for e; its defect is internal, since a terminal one-edge defect in an odd coloring would yield a zero full geodesic by the root-slide lemma.

The first-excess theorem (CE2) converts each such geodesic into an odd closed walk of length n+3 containing three matching edges. Because c is bad, its odd girth is at least n+3; the walk must therefore be a simple globally shortest odd cycle. Isometry, folded simplicity and the chord bound follow from (MP1)--(MP2). For the final statement, orient each path from F to the opposite facet. Its bridge direction is used just once; the defect e is an edge in F and must be traversed before that bridge. All other path edges, including the bridge, are zero. There are \(2^{n-1}\) perpendicular cube edges, paired antipodally with opposite colors, hence precisely \(2^{n-2}\) zero such edges. Counting the assignments e->b(e) gives the excess-collision inequality (FM3). \(\square\)

**Global closure target, not a bounded-size trap.** Proving that no legal coloring can support the entire extremal configuration (FM1)--(FM3) would prove NORI1 in every dimension by the even-dimensional lift. The missing step is still **cross-cycle interaction**: two shortest odd cycles sharing a zero bridge need not admit a rank-compatible splice. Their individual isometry and folded-chord constraints are now available in addition to the older shared-bridge and private-pivot restrictions. A successful argument must use those joint constraints, rather than trying to shorten one arbitrarily chosen isometric cycle.


## Fourier-sector decomposition of the balanced cube-edge matrix

Let \(n=2m\ge4\), \(A\) be the adjacency matrix of \(Q_n\), \(P\) its antipodal permutation, and \(R\) the color-zero adjacency matrix of a vertex-balanced antipodally odd edge coloring:
\[
R+PRP=A,\qquad R\mathbf1=m\mathbf1.
\]
In the orthonormal Walsh basis \(w_S(x)=2^{-n/2}(-1)^{\sum_{j\in S}x_j}\), split the even- and odd-cardinality Walsh modes. The fixed diagonal compressions and variable block \(B\) are those of (SC2):
\[
R=\begin{pmatrix}X&B\\ B^{\mathsf T}&Y\end{pmatrix}.
\]
For each direction \(i\), let \(s_i(x)=(-1)^{c_i(x)}\). It ignores bit \(i\), satisfies \(s_i(\bar x)=-s_i(x)\), and obeys \(\sum_i s_i(x)=0\) by balance. Write
\[
\widehat s_i(K)=2^{-n}\sum_xs_i(x)(-1)^{\sum_{j\in K}x_j}.
\]

**Theorem (Fourier-sector restrictions and singular values).** For every even-cardinality \(S\), odd-cardinality \(T\), and \(K=S\triangle T\),
\[
\boxed{
B_{S,T}=\frac12\sum_{i\notin K}(-1)^{\mathbf1_{i\in T}}\widehat s_i(K).
}\tag{FS1}
\]
Only odd-cardinality \(K\) occur. For each such \(K\), define \(a(K)=(\widehat s_i(K))_{i\notin K}\). Then
\[
\boxed{\sum_{i\notin K}a_i(K)=0.}\tag{FS2}
\]
Decompose \(B=\sum_{|K|\ {\rm odd}}B^{(K)}\), where \(B^{(K)}_{S,T}=B_{S,T}\) when \(S\triangle T=K\) and is zero otherwise. Each \(B^{(K)}\) is a weighted permutation matrix between the even and odd Walsh modes. Its singular values are the numbers
\[
\boxed{
\frac12\left|\sum_{i\notin K}a_i(K)z_i\right|,
\quad z\in\{-1,+1\}^{[n]\setminus K},
}\tag{FS3}
\]
each occurring with multiplicity \(2^{|K|-1}\). Consequently
\[
\boxed{
\|B^{(K)}\|_{\mathrm{op}}=\frac12\|a(K)\|_1,\qquad
\|B^{(K)}\|_F^2=2^{n-3}\|a(K)\|_2^2.
}\tag{FS4}
\]
Different \(K\)-sectors have disjoint matrix-entry supports, so
\[
\boxed{
\|B\|_F^2=2^{n-3}\sum_{|K|\ {\rm odd}}\sum_{i\notin K}\widehat s_i(K)^2
=n2^{n-3}.
}\tag{FS5}
\]
Of particular importance, when \(|K|=n-1\), the vector \(a(K)\) has one component and (FS2) forces that component to vanish. Therefore
\[
\boxed{
B_{S,T}=0\qquad \text{whenever }|S\triangle T|=n-1.
}\tag{FS6}
\]

*Proof.* Let \(U_i\) flip bit \(i\), and let \(D=2R-A=\sum_i\operatorname{diag}(s_i)U_i\). Since \(U_iw_T=(-1)^{\mathbf1_{i\in T}}w_T\), its Walsh matrix entry is
\[
\langle w_S,Dw_T\rangle
=\sum_i(-1)^{\mathbf1_{i\in T}}\widehat s_i(S\triangle T).
\]
The coefficient \(\widehat s_i(K)\) vanishes if \(i\in K\), since \(s_i\) ignores bit \(i\). Antipodal oddness makes it vanish for even-cardinality \(K\). Since \(A\) is Walsh-diagonal, \(D_{S,T}=2B_{S,T}\) for opposite Walsh parities, proving (FS1).

Taking the Walsh coefficient indexed by \(K\) in the balance equation \(\sum_i s_i=0\) proves (FS2). For a fixed odd \(K\), each even \(S\) has a unique odd partner \(T=S\triangle K\), and conversely. In (FS1), the signs for \(i\notin K\) are \((-1)^{\mathbf1_{i\in S}}\). As \(S\) ranges over all even subsets, every assignment \(z_i=(-1)^{\mathbf1_{i\in S}}\) outside \(K\) occurs \(2^{|K|-1}\) times: because \(K\ne\varnothing\), the bits inside \(K\) can be chosen with either parity to make \(S\) even. The singular values of a weighted permutation matrix are the absolute values of its nonzero entries, proving (FS3). Maximizing over all sign assignments proves the operator norm in (FS4), and averaging the square of the signed linear form over all sign assignments proves the Frobenius formula. Orthogonality of the entrywise sectors and Parseval for each \(s_i:\{0,1\}^n\to\{-1,+1\}\) give (FS5). Finally \(|K|=n-1\) leaves only one \(i\notin K\), and (FS2) yields (FS6). \(\square\)

**Relation to the grand matrix positivity problem.** The full target remains
\(\operatorname{tr}(PR^n)>0\).
The fixed antipodal diagonal blocks, total off-diagonal Frobenius norm, regularity and operator norm do not by themselves enforce positivity: a previously published dimension-six real symmetric block model violates the desired sign while satisfying those coarse conditions. Equations (FS1)--(FS6) add a family of **cube-specific, balance-induced linear identities** and a singular-value formula for each Fourier sector. They do not yet imply positivity of the trace; interactions between different \(K\)-sectors and Boolean edge-rule realizability remain the global obstruction.

**Verification.** Direct Walsh transforms of balanced antipodally odd signed-reader colorings in dimensions four and six confirmed (FS1)--(FS6) entrywise; in dimension six the computed norm was \(\|B\|_F^2=48\), and the \(|K|=5\) sector vanished.


### Quadratic Fourier realization of the balanced cube matrix class

The preceding linear sector identities do not capture the Boolean nature of cube-edge color rules. There is a complementary quadratic characterization that does.

**Theorem.** Let \(n=2m\ge4\). Real arrays \(a_i(K)\), indexed by direction \(i\in[n]\) and subsets \(K\subseteq[n]\), are the Walsh coefficients of the signed direction rules of a vertex-balanced antipodally odd cube-edge coloring if and only if
\[
\boxed{
a_i(K)=0\text{ whenever }i\in K\text{ or }|K|\text{ is even};
}\tag{QR1}
\]
\[
\boxed{\sum_{i=1}^n a_i(K)=0\quad(K\subseteq[n]);}\tag{QR2}
\]
\[
\boxed{
\sum_{L\subseteq[n]}a_i(L)a_i(K\triangle L)
=\mathbf1_{K=\varnothing}\quad(i\in[n],\ K\subseteq[n]).
}\tag{QR3}
\]
The signed edge rules and their zero-edge adjacency matrix are then
\[
\boxed{
s_i(x)=\sum_Ka_i(K)(-1)^{\sum_{j\in K}x_j},\qquad
R=\sum_i\operatorname{diag}((1+s_i)/2)\,U_i,
}\tag{QR4}
\]
where \(U_i\) is the bit-flip permutation in direction \(i\).

The corresponding unrestricted closure target, after the established even-dimensional balanced reduction, becomes polynomial positivity on the quadratic variety (QR1)--(QR3):
\[
\boxed{
\operatorname{tr}(PR^n)
=\sum_{\pi\in\mathfrak S_n}\sum_{x\in Q_n}
\prod_{k=1}^n
\frac{1+s_{\pi_k}(x\oplus\sum_{h<k}e_{\pi_h})}{2}>0.
}\tag{QR5}
\]

*Proof.* For a legal coloring, \(s_i(x)=(-1)^{c_i(x)}\) ignores its own bit \(i\), reverses under antipodal complementation, and has zero sum across all directions at every vertex. Its Fourier transform therefore obeys (QR1)--(QR2). The Fourier coefficient at \(K\) of \(s_i^2=1\) is the subset-XOR convolution in (QR3).

Conversely define \(s_i\) by (QR4) from arrays satisfying (QR1)--(QR3). Fourier inversion and (QR3) give \(s_i(x)^2=1\) at every vertex, so the real-valued \(s_i\) takes only signs \(+1,-1\). The support restriction (QR1) gives independence of bit \(i\) and oddness under vertex complementation; (QR2) gives \(\sum_i s_i(x)=0\), hence \(m\) edges of each color incident at every vertex. Thus (QR4) reconstructs the required symmetric binary zero-edge adjacency matrix. Expand \(R^n\) in direction flips \(U_i\). The trace with the antipodal permutation \(P=\prod_i U_i\) vanishes unless every one of the \(n\) directions occurs once, leaving precisely the rooted path product on the right of (QR5). Its terms are nonnegative, and the trace is positive precisely when a monochromatic-zero antipodal full geodesic exists. \(\square\)

**Use.** The Fourier-sector formula (FS1) computes the variable Walsh block \(B\) from these \(a_i(K)\). The linear divergence constraints (QR2), forbidden high-frequency band (FS6), and quadratic sign constraints (QR3) are all forced by legal balanced cubes. The prior real symmetric spectral-relaxation counterexample does not satisfy the full realization system; any matrix-only positivity proof must use restrictions at least as strong as (QR1)--(QR3). The theorem is a faithful global encoding, not a proof of positivity.


## Matrix trace vanishing order equals distance to geodesic success

The balanced-matrix conjecture \(\operatorname{tr}(PR^n)>0\) has a useful deformation-theoretic interpretation that applies to **every** legal antipodally odd coloring, without requiring vertex balance.

Let \(n\ge2\), \(A\) be the cube adjacency matrix, \(P\) the antipodal permutation, and \(R\) the zero-edge adjacency matrix of a legal coloring c. Put \(D=2R-A\), and for real \(t\) define
\[
\boxed{R_t=\frac{A+tD}{2}=\frac{1+t}{2}R+\frac{1-t}{2}(A-R),\qquad
F_c(t)=\operatorname{tr}(P R_t^n).}\tag{NT1}
\]
For each full oriented antipodal geodesic \(G\), let \(k_c(G)\) be its number of one-colored edges, and put
\[
g_k(c)=|\{G:k_c(G)=k\}|,\qquad
r(c)=\min_G k_c(G).
\]
Every legal coloring has the same number of all rooted full geodesics, \(2^n n!\).

**Theorem (noise-trace and metric identity).** For every legal odd coloring,
\[
\boxed{F_c(t)=\sum_{k=0}^n g_k(c)
\left(\frac{1+t}{2}\right)^{n-k}
\left(\frac{1-t}{2}\right)^k,}\tag{NT2}
\]
\[
\boxed{g_k(c)=g_{n-k}(c),\qquad
F_c(-t)=F_c(t),\qquad F_c(0)=n!.}\tag{NT3}
\]
Let \(\mathcal G_n\) be the set of legal colorings admitting a zero full antipodal geodesic, and give the coloring space Hamming distance by counting flipped antipodal edge-pair orbits. Then
\[
\boxed{
r(c)=\operatorname{dist}_{\rm Ham}(c,\mathcal G_n)
=\operatorname{ord}_{t=1}F_c(t)
=\operatorname{ord}_{t=-1}F_c(t).
}\tag{NT4}
\]
Consequently there is a polynomial \(H_c(t)\) such that
\[
\boxed{F_c(t)=(1-t^2)^{r(c)}H_c(t),\qquad
H_c(1)=H_c(-1)=4^{-r(c)}g_{r(c)}(c)>0.}\tag{NT5}
\]
The polynomial \(H_c\) is positive for \(-1<t<1\), and has \(H_c(0)=n!\). In particular if c is bad, \(r(c)\ge1\) and \(F_c(1)=0\); at a bad-good boundary coloring, \(r(c)=1\) and
\[
\boxed{F_c'(1)=-\tfrac12 g_1(c).}\tag{NT6}
\]

*Proof.* Every length-n walk from x to bar x uses each cube direction once. In the trace expansion of \(PR_t^n\), each such path G receives weight \(p^{n-k_c(G)}q^{k_c(G)}\), where \(p=(1+t)/2\) and \(q=(1-t)/2\), proving (NT2). Antipodal translation of G changes each edge color and keeps its direction order, giving an involution between paths with k and n-k one-edges. This proves the count symmetry and evenness in (NT3). At t=0 every full path has weight \(2^{-n}\), so the total trace is \(n!\).

If G has r one-edges, flipping their r antipodal edge-pair orbits produces a legal coloring with G entirely zero. The r orbits are distinct: a full geodesic uses each direction only once, whereas antipodal edge mates have the same direction. Thus the distance to \(\mathcal G_n\) is at most r(c). Conversely if a coloring c' at orbit-Hamming distance h has a zero full geodesic G, then G uses only zero edges of c outside the h changed orbits; hence \(k_c(G)\le h\), and \(r(c)\le h\). This proves the distance identity.

For t near 1, the smallest power of \(q=(1-t)/2\) appearing with nonzero coefficient in (NT2) is r(c), and its coefficient \(g_{r(c)}(c)\) is positive. Therefore \(F_c\) has a zero of order r(c) at t=1. Evenness gives the same order at -1. Dividing by \((1-t^2)^{r(c)}\) yields (NT5), with endpoint limit \(g_r/4^r\). Every term of (NT2) is positive for \(-1<t<1\), proving the stated positivity. Differentiating at t=1 for r=1 proves (NT6). \(\square\)

**Corollary (quantitative critical slope).** If c is a hypothetical bad coloring maximizing majority/minority facet imbalance, and D_F is its minority-colored edge set in a maximizing facet, the established individual-pivot theorem supplies a distinct full one-defect geodesic through every \(e\in D_F\). Reversing each path gives another oriented witness, so \(g_1(c)\ge 2|D_F|\). Consequently
\[
\boxed{-F_c'(1)\ge |D_F|
\ge 2^{n-2}+\left\lceil\frac{2^{n-3}}{1+(n-1)(n-2)}\right\rceil.}\tag{NT7}
\]
This is a nontrivial lower bound on the inward derivative at a hypothetical extremal bad boundary matrix, but it does not contradict any known matrix-moment inequality.

**Relevance and limitation.** The matrix moment is an even polynomial whose vanishing multiplicity on the coloring boundary is precisely a discrete **distance to the good-coloring set**. In particular, the first-excess reduction has a first-order analytic counterpart: if any counterexample exists, an adjacent counterexample has a simple endpoint zero. The equality uses the direction-once property and the antipodal orbit action, not merely regularity or coarse spectral bounds. By itself, however, it does not prove that \(F_c(1)>0\), since nonnegative even polynomials can have simple or higher-order endpoint zeros. The missing statement is a cube-specific prohibition on such zeros on the Boolean quadratic-realization variety (QR1)--(QR3).

**Independent numerical check.** Enumerating every oriented full geodesic for random odd colorings in dimensions four and six gave symmetric vectors \((g_k)\), verified \(F_c(0)=n!\), and matched the direct weighted trace at rational \(t=\pm1/3\).


## Signed-adjacency gauge invariance and a balanced spectral ambiguity

Fix an antipodally odd binary cube-edge coloring, put \(A=\sum_iU_i\) for cube adjacency, \(R\) for the zero-edge adjacency, \(D=2R-A=\sum_i\operatorname{diag}(s_i)U_i\), with \(s_i=(-1)^{c_i}\), and \(P\) for the antipodal permutation. For any subset J of directions, let \(c^J\) reverse the colors of **every** edge in each direction belonging to J. Define \(G_J(x,x)=(-1)^{\sum_{j\in J}x_j}\).

**Theorem (full gauge spectrum and sector spectra).** One has
\[
\boxed{D(c^J)=G_J D(c)G_J,\qquad PG_J=(-1)^{|J|}G_JP.}\tag{DG1}
\]
Consequently D and \(D(c^J)\) have identical eigenvalue multisets. The variable off-diagonal block B in the antipodal Walsh-parity splitting also has identical full singular-value multisets under this operation: for even |J|, \(B(c^J)=G_+B(c)G_-^{\mathsf T}\) for orthogonal restrictions of G; for odd |J|, the transformation exchanges the two antipodal blocks and transposes B, up to orthogonal factors. Furthermore, **each** Fourier sector \(B^{(K)}\) has the same singular-value multiset: in (FS3), the signed coefficient vector \(a_i(K)\) changes to \((-1)^{[i\in J]}a_i(K)\), which can be absorbed into the freely ranging sign vector z. The color inversion preserves vertex balance if and only if
\[
\boxed{\sum_{i\in J}s_i(x)=0\quad\text{for every vertex }x.}\tag{DG2}
\]

*Proof.* Since G_J commutes with diagonal multiplication by \(s_i\) and conjugates \(U_i\) to \((-1)^{[i\in J]}U_i\), the first formula follows. Antipodal complementation changes G_J by the constant sign \((-1)^{|J|}\), proving the second. The spectral conclusions follow from orthogonal conjugacy and the Fourier-sector singular-value formula (FS3). Reversing signs of the selected direction rules changes the signed incident sum by \(-2\sum_{i\in J}s_i(x)\), proving the balance condition. \(\square\)

**Proposition (the full signed spectrum cannot determine the geodesic trace).** On Q6 index directions 0,...,5, put \(M(a,b,c)=1\) if at least two input bits are one, and define
\[
\begin{array}{c|l}
i&c_i(x)\\
0&x_2\\
1&1-x_2\\
2&M(x_0,x_1,x_4)\\
3&1-M(x_0,x_1,x_4)\\
4&M(x_0,x_2,x_3)\\
5&1-M(x_0,x_2,x_3).
\end{array}\tag{DG3}
\]
Let c' reverse all direction-2 and direction-3 colors. Both colorings are legal antipodally odd and vertex-balanced, because the three displayed direction pairs are pointwise complementary; the reader and majority functions are antipodally odd and ignore the bits of their own respective directions. By (DG1), their signed adjacency spectra and full B singular spectra match, and each individual Fourier-sector singular spectrum also matches.

Nevertheless, for \(R_t=(A+tD)/2\),
\[
\boxed{
\begin{aligned}
\operatorname{tr}(P R_t^6)&=720-672t^2+144t^4,\\
\operatorname{tr}(P (R'_t)^6)&=720-672t^2+160t^4.
\end{aligned}}\tag{DG4}
\]
In particular the numbers of **oriented** zero full antipodal geodesics are 192 and 208.

*Audit.* Full enumeration of the \(64\cdot6!=46080\) rooted full geodesics independently gives the color-count vectors, indexed by 0,...,6 one-colored edges,
\[
\begin{aligned}
g(c)&=(192,2688,11328,17664,11328,2688,192),\\
g(c')&=(208,2656,11312,17728,11312,2656,208).
\end{aligned}
\]
Substitution in the previously proved noise-trace formula (NT2) yields (DG4). Independent subset-state dynamic programming for zero paths, \(d_x(\varnothing)=1\), \(d_x(S\cup\{i\})\mathrel{+}=d_x(S)[c_i(x\oplus\mathbf1_S)=0]\), returns 192 and 208. Matrix calculation confirms \(D'=G_{\{2,3\}}DG_{\{2,3\}}\) entrywise and equal singular spectra of the full 32-by-32 B blocks. \(\square\)

**Theorem (Boolean harmonic vertex gauges).** Let \(c\) be any antipodally odd cube-edge coloring, write \(s_i(x)=(-1)^{c_i(x)}\), and let \(D=\sum_i\operatorname{diag}(s_i)U_i\) be its signed adjacency matrix. For a sign function \(g:Q_n\to\{-1,1\}\), set \(G=\operatorname{diag}(g)\) and
\[
s_i^{g}(x)=g(x)g(x^i)s_i(x),\qquad D^{g}=GDG.
\tag{VG1}
\]
Then \(s^g\) defines another antipodally odd undirected binary edge coloring if and only if there is a constant \(\varepsilon\in\{-1,1\}\) such that
\[
\boxed{g(\bar x)=\varepsilon g(x)\quad\text{for every }x.}\tag{VG2}
\]
Under (VG2), the transformed coloring is vertex-balanced if and only if
\[
\boxed{Dg=0.}\tag{VG3}
\]
Thus the balanced colorings obtainable by vertex-sign switching are parameterized by the sign-valued vectors in \(\ker D\) of either antipodal parity. All these transformations preserve the eigenvalue multiset of \(D\). For even \(n\), they also preserve the full singular-value multiset of the off-diagonal antipodal Walsh-parity block \(B\) of the zero adjacency \(R=(A+D)/2\).

*Proof.* The formula in (VG1) is invariant under \(x\leftrightarrow x^i\), so the new direction rule represents an undirected edge. Antipodal oddness of \(s_i^g\), using that \(s_i(\bar x)=-s_i(x)\), is equivalent to \(g(\bar x)g(\bar x^i)=g(x)g(x^i)\) for every \(i,x\). The sign function \(h(x)=g(\bar x)g(x)\) must therefore satisfy \(h(x^i)=h(x)\) for every cube edge. Connectedness of the cube makes \(h\) constant, proving (VG2) in both directions.

The signed incident sum of the switched coloring equals
\[
\sum_i s_i^g(x)=g(x)\sum_i s_i(x)g(x^i)=g(x)(Dg)(x),
\]
which vanishes precisely when (VG3) holds. Since \(G^2=I\), the signed operators are orthogonally conjugate. Under (VG2), \(PG=\varepsilon GP\); hence \(G\) either preserves or exchanges the two antipodal parity subspaces. In both cases the off-diagonal block of \(D^g=GDG\) has the same singular values as that of \(D\), proving the final assertion. \(\square\)

**Example (nonlinear balanced gauges change the quadratic noise moment).** In the legal balanced \(Q_6\) coloring (DG3), the signed rules occur in three pointwise opposite pairs, \(s_{2j+1}=-s_{2j}\), and each pair ignores both of its own bits. Put
\[
y_0=x_0\oplus x_1,\qquad y_1=x_2\oplus x_3,\qquad
y_2=x_4\oplus x_5,\qquad
g(x)=(-1)^{y_0y_1y_2}.
\tag{VG4}
\]
Antipodal complementation fixes every \(y_j\), so \(g\) is antipodally even. Flipping either bit of pair \(j\) changes the same \(y_j\), whence \(g(x^{2j})=g(x^{2j+1})\). Consequently the two signed terms of pair \(j\) in \(Dg\) cancel, proving \(Dg=0\) and therefore balance of \(c^g\). More explicitly, switching reverses the two colors in direction pair \(j\) precisely where the other two \(y\)-variables are both one.

The trace polynomials for the original and transformed balanced legal colorings are
\[
\boxed{
F_c(t)=720-672t^2+144t^4,\qquad
F_{c^g}(t)=720-624t^2+160t^4.
}\tag{VG5}
\]
For reproducibility, enumeration of all \(64\cdot6!\) rooted full geodesics gives the respective one-colored-edge distributions
\[
\begin{aligned}
(g_0,\ldots,g_6)(c)&=(192,2688,11328,17664,11328,2688,192),\\
(g_0,\ldots,g_6)(c^g)&=(256,2752,11264,17536,11264,2752,256).
\end{aligned}\tag{VG6}
\]
Substitution in (NT2) proves (VG5). Independent subset-state geodesic counting gives \(g_0(c)=192\) and \(g_0(c^g)=256\). The signed matrices are related by (VG1), so their eigenvalues coincide, and their full off-diagonal Walsh-parity blocks have the same singular values. In contrast to the direction-only gauges (DG1)--(DG4), this nonlinear balanced gauge changes even the coefficient of \(t^2\), which is the weighted Fourier energy in (NM2). Hence neither signed-adjacency eigenvalues nor full off-diagonal singular values determine that quadratic mixed moment on the legal balanced matrix class.

**Proof-theoretic limit.** Neither the eigenvalues of the full signed color operator D nor the singular values of all the individual Fourier sectors determine \(\operatorname{tr}(PR^n)\), even in the balanced legal cube class. The different fourth-order coefficients in (DG4) exhibit the missing relative alignment of D against the fixed cube adjacency A and between its Fourier sectors. This does **not** rule out positivity inequalities based on spectra alone, but rules out a spectral reconstruction formula which ignores that mixed alignment. A possible proof of unrestricted NORI1 must incorporate the mixed moments of A and D, or an equivalent structure retaining their relative position.


## Cyclic cancellation and negative quadratic noise moment

Let \(n=2m\ge4\), let \(c\) be any vertex-balanced antipodally odd cube-edge coloring, and retain the signed direction rules \(s_i=(-1)^{c_i}\), their normalized Walsh coefficients \(a_i(K)=2^{-n}\sum_xs_i(x)(-1)^{\sum_{j\in K}x_j}\), the matrices \(D=2R-A\), \(P\), and \(F_c(t)=\operatorname{tr}(P((A+tD)/2)^n)\).

**Theorem (cyclic top-degree cancellation).** For every antipodally odd edge coloring, with or without balance and in any dimension \(n\ge2\),
\[
\boxed{\operatorname{tr}(PD^n)=0.}\tag{NM1}
\]
In particular, in even dimension the even polynomial \(F_c(t)\) has degree at most \(n-2\).

*Proof.* Expand \(\operatorname{tr}(PD^n)\) over all rooted directed full antipodal geodesics. Each summand is the product of the signed colors of its edges. Given a geodesic with ordered edges \(e_1,\ldots,e_n\), shift its root across \(e_1\) and rotate the directions to obtain the geodesic with edges \(e_2,\ldots,e_n,\bar e_1\). Here \(\bar e_1\) is the antipodal image of the first edge. This defines a bijection on the rooted full geodesics, and the signed product changes sign, because \(s_i(\bar x)=-s_i(x)\). Its total sum is therefore zero. The coefficient of \(t^n\) in \(F_c\) is \(2^{-n}\operatorname{tr}(PD^n)\). As \(F_c(-t)=F_c(t)\), for even \(n\) the stated degree bound follows. \(\square\)

**Theorem (weighted Fourier energy formula).** Every vertex-balanced antipodally odd coloring in even dimension \(n\ge4\) satisfies
\[
\boxed{
[t^2]F_c(t)=-\frac{n!}{2}
\sum_{\substack{K\subseteq[n]\\ |K|\ {\rm odd}}}
\frac{\sum_{i=1}^n a_i(K)^2}{|K|+2}<0.
}\tag{NM2}
\]
Moreover,
\[
\boxed{
-\frac{nn!}{6}\ \le\ [t^2]F_c(t)\
\le-\frac{nn!}{2(n-1)}<0.
}\tag{NM3}
\]
In dimension four, \([t^2]F_c(t)=-16\) for every balanced legal coloring.

*Proof.* Choose uniformly a starting vertex \(x\) and a direction permutation \(\pi\), and denote the signed color of the edge at position \(p\) by \(u_p\). Since each length-\(n\) term of the trace is \(2^{-n}\prod_p(1+tu_p)\), the coefficient of \(t^2\) is
\[
n!\,\mathbb E_{x,\pi}\sum_{p<q}u_pu_q.
\]
Fix distinct directions \(i,j\). Condition on \(i\) preceding \(j\), and let \(T\) be the set of directions strictly between them in \(\pi\). For uniform \(x\), Walsh orthogonality and the property that \(s_i\) ignores bit \(i\) and \(s_j\) ignores bit \(j\) give
\[
\mathbb E_x\bigl[s_i(x)\,s_j(x\oplus e_i\oplus\mathbf1_T)\bigr]
=\sum_{K:\ i,j\notin K}a_i(K)a_j(K)(-1)^{|K\cap T|}.
\]
The initial path prefix has been absorbed into uniform \(x\). For any fixed \(K\) of odd size \(k\) disjoint from \(i,j\), the relative order of \(i,j\) and the \(k\) directions in \(K\) is uniform. Given \(i\) before \(j\), the number of \(K\)-directions strictly between them equals \(d\) with probability
\[
\frac{k+1-d}{\binom{k+2}{2}},\qquad 0\le d\le k.
\]
As \(k\) is odd,
\[
\mathbb E_\pi(-1)^{|K\cap T|}
=\frac{\sum_{d=0}^k(-1)^d(k+1-d)}{\binom{k+2}{2}}
=\frac1{k+2}.
\]
The case \(j\) preceding \(i\) gives the same correlation. Thus
\[
[t^2]F_c(t)=n!\sum_{K:\ |K|\ {\rm odd}}
\frac{\sum_{i<j}a_i(K)a_j(K)}{|K|+2}.
\]
Vertex balance implies \(\sum_i a_i(K)=0\), whence \(\sum_{i<j}a_i(K)a_j(K)=-\tfrac12\sum_i a_i(K)^2\), proving (NM2).

Parseval and \(s_i^2=1\) give \(\sum_{i,K}a_i(K)^2=n\). The support and balance constraints imply that any nonzero \(a_i(K)\) has \(1\le|K|\le n-3\) and odd \(|K|\): a coefficient with \(|K|=n-1\) has only one eligible direction, and the balance equation kills it. Therefore \(1/(n-1)\le1/(|K|+2)\le1/3\), proving (NM3). When \(n=4\), only \(|K|=1\) survives and the formula gives \(-4\cdot4!/6=-16\). \(\square\)

The quadratic term is therefore strictly negative throughout the legal balanced Boolean realization variety (QR1)--(QR3), with an explicit Fourier-energy decomposition. This controls a mixed moment of \(A,D\) unavailable from the separate signed-adjacency eigenvalues. It does not determine the endpoint \(F_c(1)\), where higher-order terms still govern the NORI1 closure question.


### General imbalance formula and geodesic color-excess variance

The weighted Fourier formula (NM2) extends to every antipodally odd coloring, including those without vertex balance. Retain the signed direction rules \(s_i\), Walsh coefficients \(a_i(K)\), and the polynomial \(F_c(t)\), and put \(h(x)=\sum_i s_i(x)\).

**Theorem.** For every antipodally odd coloring of \(Q_n\), \(n\ge2\),
\[
\boxed{
[t^2]F_c(t)=\frac{n!}{2}
\sum_{\substack{K\subseteq[n]\\ |K|\ {\rm odd}}}
\frac{\widehat h(K)^2-\sum_i a_i(K)^2}{|K|+2},
\qquad \widehat h(K)=\sum_i a_i(K).
}\tag{NM4}
\]
In particular, the imbalance contribution is a nonnegative weighted Fourier energy. If \(c\) is vertex-balanced, then, for the color excess \(W\) (zero edges minus one edges) of a uniformly chosen rooted full antipodal geodesic,
\[
\boxed{
\mathbb E W=0,\qquad
\mathbb E W^2=n-\sum_{\substack{K\subseteq[n]\\ |K|\ {\rm odd}}}
\frac{\sum_i a_i(K)^2}{|K|+2}
\ge\frac{2n}{3}.
}\tag{NM5}
\]
Under balance, the quadratic coefficient is also
\[
\boxed{
[t^2]F_c(t)=-\frac{n!}{2^{n-2}}
\sum_{\substack{K\subseteq[n]\\ |K|\ {\rm odd}}}
\frac{\|B^{(K)}\|_F^2}{|K|+2}.
}\tag{NM6}
\]

*Proof.* The random-root, random-permutation expansion in the proof of (NM2) applies without balance through the identity
\[
[t^2]F_c(t)
=n!\sum_{\substack{K\subseteq[n]\\ |K|\ {\rm odd}}}
\frac{\sum_{i<j}a_i(K)a_j(K)}{|K|+2}.
\]
Apply \(2\sum_{i<j}a_i(K)a_j(K)=(\sum_i a_i(K))^2-\sum_i a_i(K)^2\), giving (NM4). For the random color excess \(W=\sum_{r=1}^n u_r\), antipodal translation gives \(\mathbb E W=0\). Since \(W^2=n+2\sum_{r<s}u_ru_s\), the quadratic trace expansion used in the proof of (NM2) gives the identity in (NM5). Parseval yields \(\sum_{i,K}a_i(K)^2=n\), and the weights are at most \(1/3\), proving the bound. Finally (FS4) states \(\|B^{(K)}\|_F^2=2^{n-3}\sum_i a_i(K)^2\); substituting into (NM2) proves (NM6). \(\square\)

The first formula isolates the contribution of the incident signed-degree imbalance \(h\); the second gives a dimension-uniform fluctuation lower bound; and the third expresses the quadratic trace coefficient in the sector singular-value statistics. Unlike the fourth and higher trace coefficients, this coefficient is unchanged by any direction-color gauge operation that preserves vertex balance, because such a gauge only changes the signs of the individual \(a_i(K)\).


## Cartesian tensorization and the multiplicity of endpoint zeros

Let \(c_a\) and \(c_b\) be antipodally odd binary edge colorings of \(Q_a\) and \(Q_b\), where \(a,b\ge2\). Their independent Cartesian product \(c=c_a\boxtimes c_b\) on \(Q_{a+b}\) colors an edge according to the factor containing its changing direction. Use the signed adjacency \(D_j=2R_j-A_j\), antipodal permutation \(P_j\), and noise trace \(F_j(t)=\operatorname{tr}(P_j((A_j+tD_j)/2)^j)\) from the preceding Subsections. Write \(g_k(c)\) for the number of rooted, oriented full antipodal geodesics containing \(k\) one-colored edges, and \(r(c)=\min\{k:g_k(c)>0\}\).

**Theorem (tensorization of the full trace and defect distribution).** The product \(c\) is antipodally odd and satisfies, with \(n=a+b\),
\[
\boxed{F_c(t)=\binom{n}{a}F_a(t)F_b(t),\qquad
\frac{F_c(t)}{n!}=\frac{F_a(t)}{a!}\frac{F_b(t)}{b!}.}
\tag{CT1}
\]
For every integer \(k\),
\[
\boxed{g_k(c)=\binom{n}{a}\sum_{j\in\mathbb Z}g_j(c_a)g_{k-j}(c_b),\quad
r(c)=r(c_a)+r(c_b).}
\tag{CT2}
\]
In particular
\[
\boxed{\operatorname{tr}(P R^n)
=\binom{n}{a}\operatorname{tr}(P_aR_a^a)
\operatorname{tr}(P_bR_b^b).}
\tag{CT3}
\]
The product has a monochromatic full antipodal geodesic if and only if both factors do. If both factors are vertex-balanced, the product is vertex-balanced.

*Proof.* Antipodal complementation acts separately on the two factors, proving the coloring condition. Matrix tensor identities give
\[
R_t=R_{a,t}\otimes I+I\otimes R_{b,t},\qquad P=P_a\otimes P_b.
\]
The two summands in \(R_t\) commute. In the binomial expansion of \(\operatorname{tr}(P R_t^n)\), any term with fewer than \(a\) moves in the first factor or fewer than \(b\) moves in the second has zero trace: a shorter cube walk cannot connect antipodes of that factor. Only the term with \(a\) and \(b\) moves survives, establishing (CT1). A full product geodesic consists of one full geodesic in each factor and one of \(\binom na\) interleavings of their direction orders. The number of one-colored edges adds, giving the convolution (CT2); the first nonzero term in a convolution of nonnegative sequences occurs at the sum of their first nonzero indices. Taking \(t=1\) proves (CT3). Antipodal translation sends any monochromatic-one full geodesic to a zero full geodesic, so success is equivalent to \(g_0>0\). Zero degrees add at product vertices, preserving balance. \(\square\)

**Corollary (endpoint multiplicity amplification).** For the \(h\)-fold product of a coloring \(c\) of \(Q_d\),
\[
\boxed{F_{c^{\boxtimes h}}(t)
=\frac{(hd)!}{(d!)^h}F_c(t)^h,\qquad
r(c^{\boxtimes h})=h\,r(c).}
\tag{CT4}
\]
Thus a hypothetical balanced counterexample would generate balanced counterexamples with arbitrarily large endpoint vanishing multiplicity. This conclusion applies to even-dimensional balanced factors and retains the antipodal oddness constraints.

**Theorem (asymptotic defect-density dichotomy).** For each even \(d\ge4\), let \(\mathcal B_d\) be the vertex-balanced antipodally odd cube-edge colorings and define
\[
M_d=\max_{c\in\mathcal B_d}r(c),\qquad
r(c)=\min_{G}\#\{\text{one-colored edges of }G\},
\]
where \(G\) ranges over full oriented antipodal geodesics. Then
\[
\boxed{\rho:=\lim_{\substack{d\to\infty\\d\text{ even}}}\frac{M_d}{d}
=\sup_{\substack{d\ge4\\d\text{ even}}}\frac{M_d}{d}\in[0,\tfrac12].}\tag{CT6}
\]
Under the established counterexample-preserving reduction to even-dimensional balanced colorings, unrestricted NORI1 is equivalent to \(\rho=0\). More strongly, it is equivalent to the existence of any unbounded sequence of even dimensions \(d_j\) for which \(M_{d_j}=o(d_j)\).

If a balanced bad coloring \(c\) exists in even dimension \(d\), with \(r(c)=r\ge1\), then for every sufficiently large even \(N\) there is a balanced bad coloring \(c_N\) on \(Q_N\) satisfying
\[
\boxed{r(c_N)>\frac{r}{d}N-2r.}\tag{CT7}
\]
Thus one counterexample forces positive linear minimum geodesic defect in *every* sufficiently large even dimension.

*Proof.* The balanced class \(\mathcal B_d\) is nonempty for every even \(d\ge4\): pair the directions \((2j,2j+1)\) and take the signed rules \(s_{2j}=\chi_{\{2j+2\bmod d\}}\), \(s_{2j+1}=-\chi_{\{2j+2\bmod d\}}\). Each rule ignores its own direction, is antipodally odd, and the rules sum to zero at every vertex. The class is finite, so \(M_d\) is attained. The tensorization formula (CT2) gives
\[
M_{a+b}\ge M_a+M_b\qquad(a,b\ge4\text{ even}).
\]
Fix even \(d\ge4\), and let \(N\) be sufficiently large and even. Put \(h=\lfloor N/d\rfloor-1\); then \(h\ge1\) and \(b=N-hd\) is even with \(d\le b<2d\). Take \(h\) copies of an extremizing coloring in \(\mathcal B_d\) and any coloring in \(\mathcal B_b\). By (CT2), the product belongs to \(\mathcal B_N\) and has defect at least \(hM_d\). Consequently
\[
\liminf_{\substack{N\to\infty\\N\text{ even}}}\frac{M_N}{N}\ge\frac{M_d}{d}.
\]
Taking the supremum over \(d\) makes the liminf at least \(\sup_d M_d/d\); the reverse bound for the limsup follows from the definition of that supremum. This proves (CT6). Antipodal translation of any geodesic replaces \(k\) one-colored edges by \(d-k\), so \(0\le M_d\le d/2\).

If a balanced bad coloring exists then \(M_d\ge r(c)>0\), and therefore \(\rho\ge r(c)/d>0\). Using that coloring rather than a maximizing one in the same product construction gives \(r(c_N)\ge hr>(r/d)N-2r\), proving (CT7). Conversely, if \(\rho>0\), some \(M_d>0\), so a balanced bad coloring exists. The reduction from unrestricted NORI1 to the balanced even-dimensional class proves the stated equivalence. Finally, if \(\rho>0\), convergence in (CT6) excludes any unbounded sequence with \(M_{d_j}/d_j\to0\); if \(\rho=0\), every such sequence has this property. \(\square\)

**Closure consequence.** A dimension-uniform theorem guaranteeing a full geodesic with \(o(d)\) one-colored edges for every balanced legal coloring along even a single unbounded sequence of dimensions settles unrestricted NORI1. Any hypothetical bad coloring rules out this entire class of asymptotic approximation theorems, by (CT7). This provides a quantitative all-dimensional target compatible with the Boolean realization constraints (QR1)--(QR3), while the identity (CT6) alone leaves the possibility \(\rho>0\) open.

**Corollary (dilution of normalized positive traces).** In \(Q_4\), set \(s_0=\chi_{\{2\}},s_1=-\chi_{\{2\}},s_2=\chi_{\{0\}},s_3=-\chi_{\{0\}}\). This is a balanced antipodally odd coloring with \(g_0=8\). Indeed a zero geodesic requires direction 2 between directions 0 and 1, and direction 0 between directions 2 and 3. Two direction orders satisfy both conditions, each admitting four starting vertices. Its \(h\)-fold product is balanced, and
\[
\boxed{\frac{\operatorname{tr}(P_{4h}R_{4h}^{4h})}{(4h)!}=3^{-h}.}
\tag{CT5}
\]
Hence strict positivity can hold while the normalized positive trace tends to zero exponentially.

The multiplicativity (CT1) gives a necessary calibration for prospective trace inequalities. A bounded endpoint-zero-multiplicity proof restricted to the balanced class requires an independent reduction to interaction-prime or bad-good boundary colorings; the entire balanced class is closed under products.


### Sharpness and balance-only quadratic negativity

**Sharpness of (NM3).** Partition the \(n\) directions into pairs \(\{i,j\}\). For each pair select an odd \(K_{ij}\subseteq[n]\setminus\{i,j\}\), and set \(s_i=\chi_{K_{ij}}\), \(s_j=-\chi_{K_{ij}}\). These define a legal vertex-balanced antipodally odd coloring. Taking every \(|K_{ij}|=1\) attains the lower bound of (NM3); taking every \(|K_{ij}|=n-3\) attains the upper bound. Both constructions exist for all even \(n\ge4\).

**Theorem.** For any even \(n\ge2\) and any vertex-balanced binary cube-edge coloring, without requiring antipodal oddness, let \(s_i=(-1)^{c_i}\), \(a_i(K)=\widehat{s_i}(K)\), \(D=2R-A\), and \(F_c(t)=\operatorname{tr}(P((A+tD)/2)^n)\). Then
\[
\boxed{
[t^2]F_c(t)=-\frac{n!}{2}\sum_{K\subseteq[n]}\lambda_{|K|}\sum_i a_i(K)^2<0,\quad
\lambda_k=\begin{cases}1/(k+1),&k\ {\rm even},\\1/(k+2),&k\ {\rm odd}.\end{cases}
}\tag{NM7}
\]

*Proof.* Every signed direction rule ignores its own bit. The uniform-root and uniform-direction-order expansion of (NM2) therefore applies for all Fourier subsets \(K\), regardless of their parity. When \(|K|=k\), the average of \((-1)^d\) over the number \(d\) of \(K\)-directions between two prescribed directions is
\[
\frac{\sum_{d=0}^k(-1)^d(k+1-d)}{\binom{k+2}{2}}=\lambda_k.
\]
Hence \([t^2]F_c(t)=n!\sum_K\lambda_{|K|}\sum_{i<j}a_i(K)a_j(K)\). Balance implies \(\sum_i a_i(K)=0\), so the inner cross term is \(-\tfrac12\sum_i a_i(K)^2\). Each \(\lambda_k>0\), and Parseval gives \(\sum_{i,K}a_i(K)^2=n\). This establishes the strict inequality. \(\square\)

Thus quadratic negativity holds for balanced cube-edge colorings even without antipodal oddness. The antipodal hypothesis supplies the stronger bounds (NM3) and top-degree cancellation (NM1).


**Corollary (balance is factorwise and excludes small independent blocks).** If \(c=c_1\boxtimes\cdots\boxtimes c_h\) is antipodally odd and vertex-balanced, then every factor \(c_j\) is antipodally odd and vertex-balanced. Consequently every nonempty independent direction block has even size at least four. In particular, the interaction graph of every vertex-balanced antipodally odd coloring of \(Q_4\) or \(Q_6\) is connected.

*Proof.* Write \(h_j(x_j)=\sum_{i\text{ in factor }j}s_i(x_j)\) for the signed incident sum in factor \(j\). Balance in the product gives \(\sum_j h_j(x_j)=0\) for all independent choices of the factor vertices. Fix all factor vertices except \(x_j\), and replace \(x_j\) by its antipode. Antipodal oddness changes \(h_j(x_j)\) to \(-h_j(x_j)\), while the other summands are unchanged. Subtracting the two balance equations yields \(2h_j(x_j)=0\). Thus every factor is balanced. A balanced vertex in a cube of dimension \(d\) has equally many incident edges of the two colors, so \(d\) is even. In dimension two, each signed edge rule is a signed character of the other bit, and the two rules cannot sum to zero for all vertices. Hence a nonempty factor has dimension at least four. The interaction graph components are the finest independent direction blocks, proving the last assertion. \(\square\)


**Corollary (closure-equivalent interaction-prime matrix class).** Assume the established counterexample-preserving reduction from unrestricted NORI1 to even-dimensional vertex-balanced antipodally odd colorings. Then unrestricted NORI1 is equivalent to its restriction to balanced even-dimensional colorings whose direction-interaction graph is connected.

*Proof.* The unrestricted claim implies every restriction. Conversely suppose a counterexample exists. The balance reduction supplies a balanced even-dimensional bad coloring. Choose one of minimum dimension among all such balanced bad colorings. If its interaction graph were disconnected, each component would define an independent Cartesian factor, by invariance of each edge rule under all bits outside that component. The preceding factorwise-balance corollary makes every factor balanced, and (CT3) forces at least one factor to be bad. That factor has smaller dimension, contradicting minimality. Thus a balanced bad coloring of minimum dimension is interaction-connected. \(\square\)

The interaction graph is visible in the quadratic Fourier realization: distinct directions \(i,j\) are adjacent if and only if some odd \(K\subseteq[n]\) with \(j\in K\), \(i\notin K\) has \(a_i(K)\ne0\), or the same condition holds with \(i,j\) interchanged. Indeed the Boolean derivative of \(s_i\) in bit \(j\) is nonzero precisely when a Walsh coefficient with \(j\in K\) is nonzero. Hence the closure-equivalent interaction-prime class is definable directly from the legal matrix parameters (QR1)--(QR3).


## Alternating-trail connectivity of balanced cube colorings and the folded square space

Let \(n=2m\ge4\), and let \(\mathcal B_n\) be the antipodally odd binary edge colorings of \(Q_n\) with zero degree \(m\) at every vertex. Put \(\tau x=\bar x\). A closed trail is *alternating* when successive edges, including the final and initial pair, have different colors. An alternating-trail trade reverses all colors in \(C\cup\tau C\), where \(C\) and \(\tau C\) are edge-disjoint alternating closed trails.

**Theorem 1 (balanced exchange connectivity).** Any \(c,d\in\mathcal B_n\) are joined by a sequence of alternating-trail trades, all within \(\mathcal B_n\).

*Proof.* In the disagreement edge set \(W=\{e:c(e)\ne d(e)\}\), each vertex has equally many edges of original color zero and original color one, because both colorings have zero degree \(m\). Pair incident disagreement edges of opposite original colors. Choose these pairings at one representative of each antipodal vertex pair and transport them by \(\tau\); this remains a pairing of opposite colors, since \(c\) is antipodally odd. Following paired half-edges decomposes \(W\) into edge-disjoint alternating closed trails, equivariantly permuted by \(\tau\).

No resulting trail can be preserved by \(\tau\). If one were, the induced fixed-point-free involution on its abstract cycle of edge occurrences would be the half-turn: a reflection of a cycle fixes a vertex occurrence or an edge occurrence, whereas \(\tau\) fixes neither cube vertices nor cube edges. Write its length \(2L\). Corresponding vertices \(L\) steps apart are antipodal, hence belong to the same cube bipartition class because \(n\) is even. Therefore \(L\) is even. Alternation gives equal colors to edges \(L\) positions apart, contradicting the opposite colors imposed by \(\tau\). Hence the trails occur in disjoint pairs \(C,\tau C\).

Reversing one pair preserves antipodal oddness and, at every vertex, reverses equally many edges of each color. It thus preserves balance. The other trails are edge-disjoint and retain their alternation. Reversing all trail pairs gives \(d\). \(\square\)

Let \(H_n=Q_n/\tau\) be the folded cube, whose edges correspond to antipodal cube-edge pairs. Regard edge subsets as vectors over \(\mathbb F_2\), and let \(S_n\) be the span of the images in \(H_n\) of the boundaries of the square faces of \(Q_n\).

**Theorem 2 (binary square-span constraint).** For every \(c,d\in\mathcal B_n\), the edge-orbit disagreement vector \(\bar W\) belongs to \(S_n\), and
\[
\boxed{\dim_{\mathbb F_2}S_n=(n-2)2^{n-2}.}
\tag{AT1}
\]
Consequently the number of disagreeing antipodal edge-pair orbits in each direction is even.

*Proof.* The decomposition above gives \(\bar W=\sum_{\{C,\tau C\}}\bar C\). Each \(C\) is a closed cube trail. Every closed cube walk is a binary sum of square boundaries: commute consecutive flips of different directions across square faces, and cancel consecutive repeated flips. Hence each \(\bar C\in S_n\).

Let \(\omega\) be the covering-monodromy linear functional on the binary cycle space of \(H_n\). Every projected square has zero monodromy. Conversely, a cycle with zero monodromy lifts to a closed cube walk and thus belongs to \(S_n\). More generally, pair constituent cycles of nonzero monodromy in any cycle vector from \(\ker\omega\); joining each pair by a path traversed twice produces a zero-monodromy closed walk with the same binary edge vector. Therefore \(S_n=\ker\omega\). A projected full antipodal geodesic has nonzero monodromy, so \(\omega\ne0\). The connected graph \(H_n\) has \(2^{n-1}\) vertices and \(n2^{n-2}\) edges, and its binary cycle space has dimension \(n2^{n-2}-2^{n-1}+1\). Taking the kernel of the nonzero functional gives (AT1). Each projected square has zero or two edges of every fixed direction, establishing the final assertion. \(\square\)

**Corollary 3 (one-trade closure equivalence).** The coloring
\[
c^*_{2j}(x)=x_{2j+2\bmod n},\qquad
c^*_{2j+1}(x)=1-x_{2j+2\bmod n}\quad(0\le j<m)
\tag{AT2}
\]
belongs to \(\mathcal B_n\) and has a zero full antipodal geodesic from \(e_0\) in direction order
\[
(n-1,0,2,1,4,3,\ldots,n-2,n-3).
\tag{AT3}
\]
The even-dimensional balanced form of NORI1 is equivalent to **paired-trail geodesic preservation**: a single alternating-trail trade applied to a coloring admitting a zero full antipodal geodesic must yield another such coloring. Thus a hypothetical balanced bad coloring can be selected one paired-trail trade away from a balanced good coloring; the traded edges originally colored zero then meet every zero full antipodal geodesic of the good coloring.

*Proof.* In (AT2) each adjacent direction pair has complementary rules depending on a bit outside that pair, so balance, antipodal oddness, and the undirected edge condition hold. Starting from \(e_0\), direction \(n-1\) reads \(x_0=1\) and direction \(0\) reads \(x_2=0\). The subsequent even directions read as-yet-zero next even bits, whereas the intervening odd directions read the even bits just flipped to one. The final even direction \(n-2\) reads \(x_0=0\), which direction \(0\) has already flipped. Therefore (AT3) is all zero.

If paired-trail geodesic preservation holds, apply Theorem 1 along a trade sequence from this good seed to any member of \(\mathcal B_n\); every member is good. Conversely NORI1 directly implies preservation. If a bad coloring exists, take the first bad coloring along such a sequence. Any zero full geodesic in its good predecessor avoiding the reversed zero edges would survive the trade, a contradiction. \(\square\)

Theorems 1 and 2 hold for every even \(n\ge4\). The paired-trail preservation assertion remains open; trade lengths are unrestricted. The square-span condition supplies a global mod-two constraint on the legal balanced Boolean matrix class, while the preservation assertion isolates one possible dimension-uniform closure lemma.


### Sublinear-defect and near-spanning-path closure equivalences

For an antipodally odd coloring \(c\) of \(Q_n\), let \(r(c)\) be the minimum number of one-colored edges on a full antipodal geodesic, as in (NT4). Let \(\ell(c)\) be the maximum length of a monochromatic cube path using each direction at most once, with either color allowed. Let \(\mathcal B_n\) denote the vertex-balanced antipodally odd colorings in even dimension \(n\ge4\).

**Theorem (asymptotic closure criteria).** Subject to the established balanced counterexample-preserving reduction, the following are equivalent to unrestricted NORI1:

1. There is a function \(f(n)=o(n)\) such that \(r(c)\le f(n)\) for every \(c\in\mathcal B_n\).
2. There is a function \(f(n)=o(n)\) such that \(\ell(c)\ge n-f(n)\) for every \(c\in\mathcal B_n\).
3. There is a finite constant \(C\), independent of dimension, such that \(r(c)\le C\) for every \(c\in\mathcal B_n\).

In particular, establishing an \(O(\sqrt n)\), \(O(\log n)\), or uniform bounded-defect theorem for all balanced odd cube colorings would prove unrestricted NORI1.

*Proof.* The unrestricted conjecture implies all three statements with \(f=0\) and \(C=0\). A monochromatic direction-simple path of length \(n-k\) can be extended to a full antipodal geodesic by traversing each of its \(k\) missing directions once, in any order. If its color is one, first antipodally translate it to a zero path. The resulting full path has at most \(k\) one-edges. Thus (2) implies (1), and (3) implies (1).

Conversely suppose NORI1 fails. The balanced reduction provides a bad \(c\in\mathcal B_d\), with \(d\) even and \(r(c)=r\ge1\). Form its \(h\)-fold independent Cartesian product \(c^{\boxtimes h}\in\mathcal B_{hd}\). By the tensorization theorem (CT2),
\[
r(c^{\boxtimes h})=hr.
\]
Consequently any proposed bound \(f(hd)=o(hd)\) fails for sufficiently large \(h\), disproving (1). Likewise any fixed upper bound \(C\) fails for \(h>C/r\), disproving (3). This establishes equivalence. \(\square\)

**Near-spanning consequence.** In a bad coloring, no monochromatic direction-simple path has length \(n-1\): its unique missing-direction edges at the two endpoints are antipodal and have opposite colors, so one extends the path monochromatically to length \(n\). Therefore a hypothetical balanced bad coloring \(c\in\mathcal B_d\) has \(\ell(c)\le d-2\). Projecting any monochromatic direction-simple path of \(c^{\boxtimes h}\) to the \(h\) factors yields monochromatic direction-simple paths in those factors, so
\[
\ell(c^{\boxtimes h})\le h\ell(c)\le hd-2h.
\]
Thus the failure of NORI1 forces a fixed positive fractional deficit \(2/d\) along infinitely many even dimensions. A uniform \(n-o(n)\) monochromatic path theorem would eliminate all such bad colorings at once; the approximation statement is itself a grand-theorem closure criterion, rather than a dimensional induction.



### Highest-order mixed trace moment and interaction primeness

Let \(n=2m\ge4\), \(H=A/2\), \(V=D/2\), and \(P\) be the antipodal permutation. The Walsh-parity decomposition gives
\[
H=\begin{pmatrix}X&0\\0&Y\end{pmatrix},\qquad
V=\begin{pmatrix}0&B\\B^{\mathsf T}&0\end{pmatrix},\qquad
P=\begin{pmatrix}I&0\\0&-I\end{pmatrix},
\]
with \(X_{SS}=m-|S|\) for even \(S\) and \(Y_{TT}=m-|T|\) for odd \(T\). Put \(F(t)=\operatorname{tr}(P(H+tV)^n)\).

**Theorem (two-even-insertion identity).** For every antipodally odd cube-edge coloring, without requiring balance,
\[
\boxed{
[t^{n-2}]F(t)=
\sum_{j=0}^{m-1}\operatorname{tr}
\bigl(P H V^{2j} H V^{2(m-1-j)}\bigr).
}\tag{HM1}
\]
Writing \(C_+=BB^{\mathsf T}\), \(C_-=B^{\mathsf T}B\), and \(q=m-1\), this becomes
\[
\boxed{
[t^{n-2}]F(t)=\sum_{j=0}^{q}
\left[
\operatorname{tr}(X C_+^{j}X C_+^{q-j})
-\operatorname{tr}(Y C_-^{j}Y C_-^{q-j})
\right].
}\tag{HM2}
\]
In a singular-value decomposition \(B=U\Sigma W^{\mathsf T}\), let \(\lambda_a=\Sigma_{aa}^2\), \(X'=U^{\mathsf T}XU\), \(Y'=W^{\mathsf T}YW\), and \(h_q(u,v)=\sum_{j=0}^{q}u^jv^{q-j}\). Then
\[
\boxed{
[t^{n-2}]F(t)=
\sum_{a,b}h_q(\lambda_a,\lambda_b)
\bigl((X'_{ab})^2-(Y'_{ab})^2\bigr).
}\tag{HM3}
\]
Thus the highest potentially nonzero even trace coefficient is the difference of two nonnegative weighted quadratic energies determined by the singular values of \(B\) and the alignment of its singular vectors with \(X,Y\).

*Proof.* Write \(\operatorname{Str}(T)=\operatorname{tr}(PT)\). Since \(PH=HP\) and \(PV=-VP\), cyclically moving a leading \(V^i\) past a word containing \(n-2-i\) other \(V\)'s changes its supertrace by \((-1)^{i(n-2-i)}=(-1)^i\). The coefficient containing two \(H\)'s and \(n-2\) copies of \(V\) is the sum of
\[
\operatorname{Str}(V^i H V^a H V^{n-2-a-i})
\quad(0\le a\le n-2,\ 0\le i\le n-2-a).
\]
For fixed \(a\), cyclicity gives the coefficient
\(\sum_{i=0}^{n-2-a}(-1)^i\) multiplying
\(\operatorname{Str}(H V^a H V^{n-2-a})\). This sum is one when \(a\) is even and zero when \(a\) is odd, proving (HM1). Since \(V^{2j}=\operatorname{diag}(C_+^j,C_-^j)\), block multiplication proves (HM2). Diagonalizing \(C_+\) and \(C_-\) by the left and right singular vectors of \(B\), then expanding both matrix traces entrywise, gives (HM3). Every \(\lambda_a\ge0\), so all weights \(h_q(\lambda_a,\lambda_b)\) are nonnegative. \(\square\)

**Corollary (a mixed-moment certificate for interaction primeness).** Suppose a vertex-balanced antipodally odd coloring of \(Q_n\) splits as an independent Cartesian product of \(h\ge2\) nonempty direction blocks of dimensions \(d_1,\ldots,d_h\). Then
\[
\boxed{\deg F\le n-2h,\qquad [t^{n-2}]F(t)=0.}\tag{HM4}
\]
Consequently \([t^{n-2}]F(t)\ne0\) certifies that the direction-interaction graph is connected. More generally, the degree of the noise polynomial bounds above the number of independent balanced factors.

*Proof.* The factorwise-balance theorem in this Subsection makes every block balanced and even-dimensional. The cyclic top-degree cancellation (NM1) and evenness of each factor's noise polynomial give \(\deg F_j\le d_j-2\). The Cartesian tensorization identity (CT1) gives \(F(t)=\frac{n!}{\prod_jd_j!}\prod_jF_j(t)\). Summing the degree bounds proves (HM4). \(\square\)

For \(n=6\), (HM2) reads
\[
[t^4]F(t)=2\operatorname{Str}(H^2V^4)
+\operatorname{Str}(HV^2HV^2).
\]
The two balanced dimension-six gauge-related examples (DG3)--(DG4) have equal signed-adjacency spectra and equal singular-value multisets in every Fourier sector, but their values of this coefficient differ by \(16\). Equations (HM2)--(HM3) locate the distinguishing information in mixed singular-vector alignment. They impose no sign on \(F(1)\); the strict endpoint positivity problem remains open.



## explicit seam-uniform mixed traces and the arbitrary-color one-change operator

Let \(Q_n\) have adjacency \(A\), antipodal permutation \(P\), and a legal antipodally odd edge coloring, with color-zero adjacency \(R\) and color-one adjacency \(B=A-R=PRP\). No vertex balance is assumed.

**Theorem (seam-uniform full-geodesic counts).** For every \(0\le k\le n\),
\[
\boxed{
\operatorname{tr}\!\left(P R^k B^{n-k}\right)
=\operatorname{tr}(P R^n).
}\tag{SM1}
\]
The left side counts rooted, oriented full antipodal geodesics whose positional color word is \(0^k1^{n-k}\); hence the count is independent of the location of the color change, including the monochromatic endpoints \(k=0,n\). Consequently
\[
\boxed{
\sum_{k=0}^n\operatorname{tr}(P R^kB^{n-k})
=(n+1)\operatorname{tr}(PR^n).
}\tag{SM2}
\]
Every admissible seam position contributes precisely the same count.

*Proof.* The antipodal condition gives \(B=PRP\), so \(B^{n-k}=PR^{n-k}P\). Using \(P^2=I\), associativity, and cyclicity of the trace,
\[
\begin{aligned}
\operatorname{tr}(P R^k B^{n-k})
&=\operatorname{tr}(P R^k P R^{n-k}P)\\
&=\operatorname{tr}(R^k P R^{n-k})\\
&=\operatorname{tr}(P R^{n-k}R^k)
=\operatorname{tr}(PR^n).
\end{aligned}
\]
All operators have nonnegative entries, and any length-\(n\) walk from a vertex to its antipode traverses each cube direction once. Thus the trace terms count precisely the asserted geodesics. Sum the equality over \(k\) to get (SM2). \(\square\)

**Combinatorial orbit interpretation.** Cyclically rotate a rooted full geodesic by moving its first direction to the end and sliding the root across that first edge. The moved edge is replaced by its antipodal mate, so its color toggles and the other edge colors persist. Every orbit of this rotation has precisely \(2n\) rooted geodesics. If the orbit includes a monochromatic word, it contains each word \(0^{n-k}1^k\) and \(1^{n-k}0^k\), \(0\le k<n\), precisely once. Orbits with no monochromatic word have no one-change word, since a one-change word rotates to a monochromatic word. Hence (SM1) also follows by an explicit bijection; the matrix proof shows this symmetry only requires \(B=PRP\) and trace cyclicity.

**Corollary (explicit unconditioned one-change trace test).** For **any** binary edge coloring of \(Q_n\), without antipodal conditions, write \(R\) and \(B=A-R\) for its two adjacency matrices and define
\[
\boxed{
\mathcal T_n(R,B)=\sum_{k=0}^n\operatorname{tr}(P R^k B^{n-k}).
}\tag{SM3}
\]
Then \(\mathcal T_n(R,B)>0\) if and only if there is a full antipodal geodesic with at most one color change. Indeed all-red and all-blue words are included, and a word \(1^k0^{n-k}\) can be reversed to \(0^{n-k}1^k\). Thus the arbitrary-color Leader--Long geodesic two-color-path assertion \(B_n\) is equivalent to \(\mathcal T_n(R,A-R)>0\) for every binary undirected-edge partition \(R+(A-R)=A\). For legal antipodally odd colorings, (SM2) gives the stronger identity
\[
\boxed{\mathcal T_n(R,A-R)=(n+1)\operatorname{tr}(PR^n).}\tag{SM4}
\]

Finally, treating \(z\) as a formal variable,
\[
\boxed{
\mathcal T_n(R,B)
=[z^n]\operatorname{tr}\!\left(P(I-zR)^{-1}(I-zB)^{-1}\right)
=(n+1)![z^n]\int_0^1
\operatorname{tr}\!\left(Pe^{ztR}e^{z(1-t)B}\right)\,dt.
}\tag{SM5}
\]
The first identity expands two geometric series; the second uses
\(\int_0^1t^k(1-t)^{n-k}dt=k!(n-k)!/(n+1)!\).
This faithfully encodes a single allowed change as an ordered two-phase resolvent/heat-kernel coefficient, preserving the cube-edge support missing in coarse spectral relaxations. Positivity of this coefficient for arbitrary edge partitions remains precisely the open grand theorem, while seam uniformity (SM1) is proved for the odd subclass.



### Complementary rooted reachability convolution at every rank

The seam-uniform mixed-trace identity (SM1) also yields an explicit same-color path-counting formulation at **every** rank, including ranks other than the midpoint. For each root \(x\) and subset \(S\subseteq[n]\), define \(h_x(S)\) to be the number of zero-colored direction-simple paths from \(x\) to \(x\oplus \mathbf1_S\) using precisely the directions in \(S\), in some order. Put \(h_x(\varnothing)=1\).

**Corollary (all-rank complementary convolution).** Every legal antipodally odd cube coloring satisfies, for every \(0\le k\le n\),
\[
\boxed{
\operatorname{tr}(PR^n)
=\sum_{x\in Q_n}\ \sum_{\substack{S\subseteq[n]\\|S|=k}}
h_x(S)\,h_x([n]\setminus S).
}\tag{SM6}
\]
In particular, NORI1 is equivalent to the existence of a root \(x\), a rank \(k\), and two **zero-colored direction-simple paths starting at the same root**, whose direction sets partition \([n]\). In fact if a solution exists at one rank, the equality gives positive contributions at *every* rank.

*Proof.* Expand the mixed trace from (SM1) at a vertex \(x\) and intermediate vertex \(v=x\oplus\mathbf1_S\) of Hamming distance \(k\):
\[
\operatorname{tr}(P R^k B^{n-k})
=\sum_{x,S:|S|=k}
(R^k)_{x,v}(B^{n-k})_{v,\bar x}.
\]
Because \(B=PRP\), the last factor equals \((R^{n-k})_{\bar v,x}=(R^{n-k})_{x,\bar v}\). The two factors are \(h_x(S)\) and \(h_x(S^c)\). Apply (SM1). \(\square\)

**explicit forbidden-complement support condition.** For \(\mathcal R_k(x)=\{S:|S|=k,\ h_x(S)>0\}\), any hypothetical NORI1 counterexample must obey
\[
\boxed{
\mathcal R_k(x)\cap
\{[n]\setminus T:T\in\mathcal R_{n-k}(x)\}
=\varnothing
\quad\text{for all }x,k.
}\tag{SM7}
\]
Equivalently,
\[
\boxed{
|\mathcal R_k(x)|+|\mathcal R_{n-k}(x)|
\le\binom nk\quad\text{for every root and every rank.}
}\tag{SM8}
\]
At the central rank \(n=2m,k=m\), the sharper antipodal-pair condition reads
\[
\boxed{
|\mathcal R_m(x)|\le\tfrac12\binom{2m}{m}
\quad\text{in every bad coloring, at every root.}
}\tag{SM9}
\]
The bounds are only necessary for badness, not sufficient. They isolate a global rank-by-rank Hall-type obstruction: a counterexample must keep the same-color rootwise reachable support from hitting its complementary direction support simultaneously on all ranks. Balance supplies lower bounds \(|\mathcal R_k(x)|\ge\binom mk\) for \(k\le m\) (HC1), but those lower bounds do not yet contradict (SM8)--(SM9).

The convolution provides a symmetric count, rather than merely an existential midpoint condition, and gives a direct target for an expansion proof retaining Boolean direction-support compatibility.



## Universal anisotropic positive definiteness of full-geodesic signed-color correlations

Let \(c\) be any antipodally odd undirected-edge coloring of \(Q_n\), \(n\ge2\), without assuming balance. Write \(s_i(x)=(-1)^{c_i(x)}\), \(a_i(K)=\widehat s_i(K)\), and let \(X_i\in\{-1,+1\}\) denote the signed color of the unique direction-\(i\) edge of a uniformly sampled rooted full antipodal geodesic. Root antipodal translation sends \(X\mapsto-X\), so \(\mathbb EX=0\). Put \(C_{ij}=\mathbb E(X_iX_j)\).

**Theorem (Fourier Gram decomposition and dimension-free ellipticity).** For all distinct \(i,j\),
\[
\boxed{C_{ij}=\sum_{\substack{K\subseteq[n]\\ |K|\ {\rm odd}}}
\frac{a_i(K)a_j(K)}{|K|+2}.}\tag{AG1}
\]
Define \(a(K)=(a_i(K))_{i=1}^n\), and
\[
q_i=\sum_{\substack{K\subseteq[n]\\ |K|\ {\rm odd}}}\frac{a_i(K)^2}{|K|+2},
\qquad L=\sum_{\substack{K\subseteq[n]\\ |K|\ {\rm odd}}}\frac{a(K)a(K)^{\mathsf T}}{|K|+2}.
\]
Then
\[
\boxed{
C=I-\operatorname{diag}(q_1,\ldots,q_n)+L,\qquad
L\succeq0,\qquad 0<q_i\le\frac13,
\qquad \boxed{C\succeq\frac23 I}.
}\tag{AG2}
\]
Equivalently, **every** real directional weight vector \(v\in\mathbb R^n\) satisfies
\[
\boxed{\mathbb E\left(\sum_i v_iX_i\right)^2\ge\frac23\sum_i v_i^2.}\tag{AG3}
\]
The constant \(2/3\) is optimal, already among vertex-balanced antipodally odd colorings in dimension four.

If \(c\) is vertex-balanced in even dimension \(n\ge4\), the decomposition moreover has
\[
\boxed{
L\mathbf1=0,\quad
\sum_{j\ne i}C_{ij}=-q_i,\quad
\frac1{n-1}\le q_i\le\frac13.
}\tag{AG4}
\]
Thus every individual direction has strictly negative *total* pairwise correlation with the other directions, even though some individual correlations can be positive.

*Proof.* If direction \(i\) precedes direction \(j\) in a uniform permutation, the two edge positions differ by an \(i\)-flip and the intervening direction set \(T\). Uniformity of the starting root, Walsh orthogonality, and the fact that each \(s_i\) ignores bit \(i\), give
\[
\mathbb E_x(s_i(x)s_j(x\oplus e_i\oplus\mathbf1_T))
=\sum_{K\subseteq[n]}a_i(K)a_j(K)(-1)^{|K\cap T|}.
\]
The Fourier summands vanish when \(i\in K\) or \(j\in K\); only odd \(K\) remain by antipodal oddness. For such \(K\), \(k=|K|\) is odd, and the relative order of \(i,j\) and the \(k\) directions of \(K\) is uniform. Conditioned on \(i\) before \(j\),
\[
\mathbb E_{\pi}(-1)^{|K\cap T|}
=\frac{\sum_{d=0}^{k}(-1)^d(k+1-d)}{\binom{k+2}{2}}
=\frac1{k+2}.
\]
The same value holds in the opposite ordering, proving (AG1). Since \(X_i^2=1\), its diagonal covariance is one, so adjoining the diagonal of the positive-semidefinite Gram matrix \(L\) yields \(C=I-\operatorname{diag}(q)+L\). Parseval gives \(\sum_Ka_i(K)^2=1\), and every nonzero Fourier level is odd and at least one, so \(0<q_i\le1/3\). It follows that \(C\succeq I-\operatorname{diag}(q)\succeq(2/3)I\), proving (AG2)--(AG3).

Under vertex balance, \(\sum_i s_i(x)=0\), hence \(\sum_i a_i(K)=0\) at every \(K\), and \(L\mathbf1=0\). In particular the off-diagonal row sum of \(C\) is \(-q_i\). The support restriction \(i\notin K\) and balance eliminate odd \(|K|=n-1\) coefficients, so any nonzero coefficient has \(1\le |K|\le n-3\). Parseval then gives \(1/(n-1)\le q_i\le1/3\), proving (AG4). \(\square\)

**Sharp example.** On \(Q_4\), take \(c_0=x_2,\ c_1=1-x_2,\ c_2=x_0,\ c_3=1-x_0\), the already established balanced legal coloring. Its signed direction-color correlation matrix is
\[
C=\begin{pmatrix}
1&-1/3&0&0\\-1/3&1&0&0\\
0&0&1&-1/3\\0&0&-1/3&1
\end{pmatrix},
\]
whose eigenvalues are \(2/3,2/3,4/3,4/3\). Thus (AG2) cannot be improved uniformly.

**Consequences and closure boundary.** Taking \(v=\mathbf1\) gives \(\mathbb E(\sum_i X_i)^2\ge2n/3\) for *all* antipodally odd colorings, extending the previously recorded balanced-only variance estimate (NM5). By antipodal sign symmetry, some full geodesic has at most \((n-\sqrt{2n/3})/2\) wrong-colored edges, with the evident integer rounding. More generally (AG3) supplies a directional-weighted variance certificate valid for every chosen direction set. The formal six-direction profile model (FA1)--(FA4) can still satisfy the Gram inequality: its symmetric correlation matrix has off-diagonal entries \(-2/45\) and least eigenvalue \(7/9>2/3\). Hence the theorem alone does not rule out a bad profile distribution; full Boolean realization and higher correlations remain essential.



### Quantitative universal two- and three-direction prescriptions

The anisotropic Gram bound (AG2) gives robust direction-prescription counts, strengthening the mere existence of prescribed color profiles on small direction sets.

**Corollary (uniform two- and three-direction profile populations).** Fix any legal antipodally odd coloring of \(Q_n\), \(n\ge2\), and distinct directions \(i,j\). For any prescribed colors \(b_i,b_j\in\{0,1\}\),
\[
\boxed{\Pr(w_i=b_i,\ w_j=b_j)\ge\frac16.}\tag{AG5}
\]
For \(n\ge3\), any three distinct directions \(i,j,k\) and any three prescribed colors satisfy
\[
\boxed{\Pr(w_i=b_i,\ w_j=b_j,\ w_k=b_k)\ge\frac1{16}.}\tag{AG6}
\]
Probabilities refer to a uniform rooted oriented full geodesic; thus the corresponding explicit population lower bounds are \(2^n n!/6\) and \(2^n n!/16\), respectively. No balance assumption is needed.

*Proof.* Each signed profile bit \(X_i=(-1)^{w_i}\) is unbiased by antipodal translation, and the joint law of the full profile \(X\) is invariant under \(X\mapsto-X\). For two directions, the event of specified signs \((\alpha_i,\alpha_j)\) has probability
\[
\frac14(1+\alpha_i\alpha_j C_{ij}).
\]
By (AG1) and Cauchy--Schwarz, \(|C_{ij}|\le\sqrt{q_iq_j}\le1/3\), proving (AG5). The bound is sharp: the balanced legal four-cube coloring in the sharpness example of (AG2) has \(C_{01}=-1/3\), and hence \(\Pr(X_0=X_1=1)=1/6\).

For three directions let \(Y=(\alpha_iX_i,\alpha_jX_j,\alpha_kX_k)\), where \(\alpha_r=(-1)^{b_r}\). The global sign symmetry makes all odd moments of \(Y\) vanish, including its third moment. Therefore the explicit prescribed-event probability is
\[
\Pr(Y=(1,1,1))
=\frac18(1+\mathbb E Y_1Y_2+\mathbb E Y_1Y_3+\mathbb E Y_2Y_3).
\]
By (AG3), \(\mathbb E(Y_1+Y_2+Y_3)^2\ge(2/3)\cdot3=2\). Expanding the square yields \(\sum_{a<b}\mathbb E Y_aY_b\ge-1/2\), proving the probability is at least \(1/16\). \(\square\)

**Conditional-extension obstruction.** The three-direction lower bound cannot simply be iterated by demanding the fourth direction first. For example the balanced legal \(Q_4\) coloring
\[
c_0=x_2,\quad c_1=1-x_2,\quad c_2=x_0,\quad c_3=1-x_0
\]
has the following property: every full geodesic with *first direction zero* traverses its direction-2 and direction-3 edges in opposite colors. Indeed after the first direction-zero step, bit \(x_0\) remains fixed throughout the other three steps; consequently \(c_2=x_0\) and \(c_3=1-x_0\) cannot agree. Thus no full geodesic starting in direction zero realizes a prescribed triple on directions \(1,2,3\) with equal colors on \(2,3\), despite the universal unrestricted lower bound (AG6). This explicitly defeats an otherwise tempting first-direction Ward-extension induction.


## Tensorization of the walk frontier and the grade-three closure branch

The recent walk, matrix, and product reductions identify a common all-dimensional target. The full length--turn frontier tensorizes additively, whereas its geodesic grade threshold tensorizes by a maximum. This distinction determines what the Minty walk potential can force after the first-excess reduction.

Let \(c\) be an antipodally odd coloring of \(Q_n\). For an antipodal walk \(W\), write \(L(W)\) for its length and
\[
g(W)=\sum_{j<L}[w_j\ne w_{j+1}]+[w_L=w_1]
\]
for its positive odd completed grade. Define
\[
\ell_c(r)=\min\{L(W):W:x\leadsto\bar x,\ g(W)\le r\},\qquad
E_r(c)=\ell_c(r)-n,
\tag{TF1}
\]
with \(+\infty\) allowed. Both root and walk vary. Let
\[
\gamma(c)=\min\{g(P):P\text{ is a full antipodal geodesic}\}.
\tag{TF2}
\]
The shortest monochromatic antipodal-path excess equals \(E_1(c)\): a grade-one antipodal walk can be root-slid to a monochromatic antipodal walk of the same length. Closed excursions can then be erased. In particular, \(\gamma(c)=1\) is equivalent to NORI1 for \(c\).

**Theorem (additive frontier and maximum geodesic grade).** For independent legal colorings \(c,d\) on \(Q_a,Q_b\),
\[
\boxed{\ell_{c\boxtimes d}(r)=\ell_c(r)+\ell_d(r),\qquad
E_r(c\boxtimes d)=E_r(c)+E_r(d)}
\tag{TF3}
\]
for every \(r\ge1\). Moreover
\[
\boxed{\gamma(c\boxtimes d)=\max\{\gamma(c),\gamma(d)\}.}
\tag{TF4}
\]

*Proof.* Project a product antipodal walk to each factor, deleting the other factor's steps. Each projection is an antipodal walk, with its original factor colors. Twisted subsequence monotonicity gives factor grades at most the product grade, and the two projected lengths add to the original length. Thus a product walk of grade at most \(r\) has length at least \(\ell_c(r)+\ell_d(r)\).

For the converse, suppose both frontier values are finite and choose minimizing factor walks with grades \(g_c,g_d\le r\). Slide each root to a changed completed comparison, then antipodally translate if needed. Each resulting word starts and ends in zero and has precisely \(g_j\) nonempty alternating monochromatic runs, beginning with zero and ending with zero. Root sliding preserves length, grade, and antipodal endpoints.

Let \(G=\max(g_c,g_d)\). Pad the shorter run list by empty alternating runs after its last zero run, until each list has \(G\) positions. Interleave the two walks run by run: perform both zero runs at position one, both one runs at position two, and so on. Independence of the factors makes this a valid antipodal walk. The factor having \(G\) nonempty runs ensures that the merged word has completed grade \(G\le r\). Its length is the sum of the chosen factor lengths. This proves (TF3), including the infinite cases by projection.

Every antipodal walk has length at least its cube dimension. Equality means every direction occurs once. Hence
\(\ell_c(r)=a\) precisely when \(\gamma(c)\le r\). Applying this observation to (TF3) proves (TF4). \(\square\)

This extends the earlier same-factor invariance of the full-geodesic minimum switch count and the one-change shortest-path product formula: it treats distinct odd factors and every completed-grade threshold simultaneously.

### A uniform approximation theorem on grade three suffices for grand closure

The first-excess reduction supplies a hypothetical bad coloring having a full geodesic with one isolated one-edge defect. Its completed grade is three. The defect-preserving balanced lift supplies a balanced bad coloring with the same property. Thus any failure of unrestricted NORI1 implies a balanced bad coloring \(c\) in some even dimension \(d\) satisfying
\[
\boxed{\gamma(c)=3,\qquad E_1(c)>0.}
\tag{TF5}
\]
Conversely, excluding such balanced colorings proves NORI1 by that reduction.

**Theorem (grade-three bounded-overhead closure criterion).** Each of the following assertions is equivalent to unrestricted NORI1:

1. A dimension-independent finite constant \(C\) bounds \(E_1(c)\) for every balanced legal coloring with \(\gamma(c)\le3\).
2. A uniform function \(f(n)=o(n)\) bounds \(E_1(c)\) for every such coloring of \(Q_n\).
3. Every balanced legal coloring with \(\gamma(c)\le3\) has a monochromatic full antipodal geodesic.

The same equivalence holds if the approximation is imposed only on \(\gamma(c)=3\), with the \(\gamma=1\) cases understood to have zero excess.

*Proof.* NORI1 gives every assertion with zero bound. Conversely, if NORI1 fails, choose the balanced coloring in (TF5). Its \(h\)-fold Cartesian power remains balanced and legal. By (TF3)--(TF4),
\[
\boxed{
\gamma(c^{\boxtimes h})=3,\qquad
E_1(c^{\boxtimes h})=hE_1(c).
}
\tag{TF6}
\]
If \(E_1(c)=+\infty\), either approximation already fails. Otherwise its value is a positive even integer, since antipodal walk length has the parity of the dimension. The excess in (TF6) is then at least \(2h\), in dimension \(hd\). It contradicts a fixed bound or a uniform \(o(hd)\) bound. Assertion 3 excludes (TF5) directly. \(\square\)

Thus it suffices to start with a balanced odd cube possessing a full geodesic whose color word has three alternating runs, and produce **some** monochromatic antipodal path with uniformly bounded additive length overhead. A uniform sublinear overhead also suffices. The path need not use each direction once in the approximation theorem. This is a single grade-three global branch in arbitrary dimension; no sequence of increasing switch cases is required.

### Saturation of fixed-weight Minty potentials

For a real \(\lambda>0\), define the normalized walk potential
\[
\mathcal P_\lambda(c)
=\min_{W:x\leadsto\bar x}
\{\lambda(L(W)-n)+g(W)-1\}.
\tag{TF7}
\]

**Theorem (grade-three potential formula).** If \(\gamma(c)=3\), then
\[
\boxed{\mathcal P_\lambda(c)=\min\{\lambda E_1(c),\,2\}.}
\tag{TF8}
\]
Consequently, for the powers in (TF6),
\[
\boxed{\mathcal P_\lambda(c^{\boxtimes h})
=\min\{\lambda hE_1(c),\,2\}.}
\tag{TF9}
\]

*Proof.* Among grade-one walks the minimum value is \(\lambda E_1(c)\). Every walk of grade at least three has value at least two, because its length is at least \(n\). A grade-three full geodesic realizes value two. These exhaust the possibilities, proving (TF8); apply (TF6) for (TF9). \(\square\)

**Consequence for the earlier erasure program.** In a hypothetical bad grade-three coloring, \(E_1(c)\ge2\). Therefore for every integer \(\lambda\ge1\), a minimizer of \(\lambda L+g\), with minimum length breaking ties, is already a **full geodesic of grade three**. Any nongeodesic competitor has either grade one and excess at least two, or grade at least three and a positive length excess; it cannot beat that geodesic, and ties have greater length. Thus the repeated-direction derivative-run constraints on this minimizer are vacuous in a closure-equivalent branch.

For finite positive \(E_1(c)\), the transition between the two objectives occurs at
\[
\boxed{\lambda_*(c)=2/E_1(c),\qquad
\lambda_*(c^{\boxtimes h})=\lambda_*(c)/h.}
\tag{TF10}
\]
For any fixed \(\lambda>0\), the potential in (TF9) saturates at two even while the shortest monochromatic antipodal-path excess grows linearly. This precisely identifies the information lost by a fixed scalar weighting.

**Odd-girth interpretation.** In even dimension, the unit-weight model satisfies
\[
\operatorname{og}(K(c))=n+1+\mathcal P_1(c).
\]
Hence the hypothetical powers in (TF6) all have odd girth \(hd+3\), while their shortest odd cycles containing one antipodal matching edge have length
\[
hd+1+hE_1(c).
\tag{TF11}
\]
Their full-geodesic minimum one-edge count also grows additively by the earlier trace tensorization theorem. A three-matching-edge shortest cycle of first excess can therefore coexist, conditionally on any counterexample, with arbitrarily large additive distance to a one-matching-edge cycle. The first-excess condition retains every direction once but permits a long internal block of wrong-colored edges; it is broader than the one-wrong-edge boundary normal form.

**Revised closure target.** The walk relaxation remains faithful. In the grade-three branch its useful objective is quantitative conversion to a grade-one walk, with sublinear or bounded additive overhead. Ordinary cycle erasure and dimension erasure of the fixed-weight minimizer are already available there. A new argument must couple the three monochromatic runs, or the three matching seams, strongly enough to obtain that conversion. The paired-sweep strengthening is separately refuted and supplies no such conversion. The approximation in the theorem above remains open.
