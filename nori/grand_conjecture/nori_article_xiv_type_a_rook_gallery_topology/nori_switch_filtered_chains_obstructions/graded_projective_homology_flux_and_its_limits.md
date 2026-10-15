# Graded projective homology flux and its limits

# Graded projective Petrie homology and chamber-wall limitations

Two complementary phenomena occur for unrestricted antipodally odd cube colorings. A single type-D chamber wall can carry nonzero projective homology in two different positive switch grades, even with vanishing signed first switch moment. Yet the associated graded homology classes of wall differences form an ordinary coboundary on the full chamber adjacency graph, so their periods always vanish.

Let \(Y_n=\partial I^n/A\cong\mathbb RP^{n-1}\), \(n\ge3\), and let \(\eta\) be the generator of \(H_1(Y_n;\mathbb F_2)\). A Petrie cycle formed from an antipodal cube geodesic projects to a loop representing \(\eta\), since its lift joins a vertex to its antipode. Fix a legal coloring \(c\). For a type-D chamber tree \(T\), let \(\mathcal B(T)\) be its \(2^{n-2}\) Petrie cycles, \(h_c(C)\) their root-slide-invariant twisted switch grade, and set
\[
\Gamma_r(T)=\sum_{C\in\mathcal B(T):h_c(C)=r}[\bar C],\qquad
p_r(T)=\#\{C\in\mathcal B(T):h_c(C)=r\}\pmod2.
\tag{1}
\]

**Theorem 1 (homological fillability and zero chamber holonomy).** For every \(T,r\),
\[
\boxed{[\Gamma_r(T)]=p_r(T)\eta.}
\tag{2}
\]
A mod-two sum of projective Petrie loops bounds a projective cubical two-chain if and only if its number of summands is even. Every chamber book has \(\sum_rp_r(T)=0\). Along a directed chamber wall \(T\to T'\), the grade-\(r\) homology flux is
\[
\boxed{
\mathcal F_r(T,T')=[\Gamma_r(T')+\Gamma_r(T)]
=(p_r(T')+p_r(T))\eta=(\delta p_r)(T,T')\eta.}
\tag{3}
\]
Therefore the sum of \(\mathcal F_r\) around every closed chamber walk is zero, independently at every switch grade.

*Proof.* Every projected Petrie loop represents \(\eta\), so linearity proves (2). The cubical two-skeleton computes \(H_1(Y_n;\mathbb F_2)\), giving the filling criterion. The cardinality \(2^{n-2}\) is even for \(n\ge3\). Formula (3) is the coboundary of the globally defined chamber function \(p_r\); every closed walk telescopes. \(\square\)

For a central-edge-changing chamber wall, take leading directions \(i,j\), a reference vertex \(g\), and order \(K\) of the remaining \(n-2\) directions. The signed root-wall grade polynomial is
\[
W(t)=\sum_{\sigma\in\mathcal U(K)}\epsilon_K(\sigma)
\bigl(t^{h_c(C(g;i,j,\sigma))}-t^{h_c(C(g;j,i,\sigma))}\bigr).
\tag{4}
\]
Adjacent-exchange variation gives \(\Delta_\sigma=h_{ij}(\sigma)-h_{ji}(\sigma)\in\{-1,0,1\}\) and
\[
\boxed{W(t)=(t-1)\sum_\sigma\epsilon_K(\sigma)\Delta_\sigma
t^{\min(h_{ij}(\sigma),h_{ji}(\sigma))}.}
\tag{5}
\]
The previously proved endpoint theorem determines \(W'(1)\), but not all coefficients of \(W\).

**Theorem 2 (sharp higher-grade obstruction).** If \(4\le n\le6\), all contributing geodesics have positive switch grade, and \(W'(1)=0\), then \(W=0\). In dimension \(7\) the following legal antipodally odd affine coloring gives all contributing paths positive grade while
\[
\boxed{W(t)=-t(t-1)^2=-t+2t^2-t^3\ne0.}
\tag{6}
\]
Index dimensions \(0,\ldots,6\) and set
\[
c(\{x,x\oplus e_d\})=x_{j_d}+a_d\pmod2,\qquad
(j_0,\ldots,j_6)=(4,2,1,1,3,4,2),\quad
(a_0,\ldots,a_6)=(0,1,0,1,0,1,0).
\tag{7}
\]
Take \(g=0,i=0,j=1,K=(2,3,4,5,6)\). The projective grade-one and grade-three wall chains each represent \(\eta\), and cannot bound a projective two-chain separately.

*Proof.* Every \(W\) vanishes at \(t=1\). If all grades are positive, \(W(0)=0\); vanishing derivative at \(1\) means \(t(t-1)^2\mid W\). The largest twisted grade is \(\lfloor(n-1)/2\rfloor\le2\) for \(n\le6\), forcing \(W=0\).

For (7), \(j_d\ne d\), making the bit well-defined on an undirected edge, and vertex complementation flips the bit, proving legal antipodal oddness. Expand the sixteen words of the right-normed Lie bracket on \(K\). Read the edge bit \(x_{j_d}+a_d\) immediately before each dimension \(d\) is toggled. The two signed grade distributions are
\[
\sum_\sigma\epsilon_K(\sigma)t^{h_{01}(\sigma)}=-2t+2t^2,\qquad
\sum_\sigma\epsilon_K(\sigma)t^{h_{10}(\sigma)}=-t+t^3.
\tag{8}
\]
All 32 grades are in \(\{1,2,3\}\). Subtraction yields (6); its first derivative at one vanishes, but its mod-two reduction is \(t+t^3\). In odd dimension \(7\), this is the mod-two projected root-wall chain polynomial. Each of grades one and three is therefore an odd sum of projected Petrie loops and represents \(\eta\), proving the filling obstruction by Theorem 1. \(\square\)

The affine example does not refute NORI1: the rooted path of dimensions \((0,4,5,6,2,1,3)\) is monochromatic with all bits zero.

**Implication for the chain approach.** Theorem 2 rules out universally grade-preserving local wall fillings based solely on first-moment cancellation, even when every path at that wall has positive grade. Theorem 1 rules out obtaining a nonzero ordinary chamber-graph cohomology class merely by accumulating these scalar graded \(H_1\) differences around loops. Further progress needs support-sensitive relative chains, higher incidence information, or suitably twisted equivariant coefficients; scalar homology flux is insufficient.
