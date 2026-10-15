# Parabolic syndrome saturation by commuting exchanges and root slides

### Parabolic saturation of affine root syndromes

Let \(B\in\mathbb F_2^{n\times n}\) have zero diagonal and satisfy \(B\mathbf1=\mathbf1\). Color undirected direction-\(i\) edges of \(Q_n\) by \(c_i(x)=a_i+(Bx)_i\). Put \(V=\mathbb F_2^n/\operatorname{im}B\), \(q=\dim V\), and define the root syndrome of a full order \(\pi\) by
\[
\Phi(\pi)=\left[\left(\sum_{j\text{ before }i}B_{ij}\right)_{i=1}^n\right]\in V.
\]
A full geodesic of constant color exists with this direction order if and only if \(\Phi(\pi)=[a]\).

**Theorem 1 (additivity over parabolic products).** Fix an ordered partition \(\mathcal P=C_1|\cdots|C_s\). Let \(D_h\subset V\) be the differences in syndrome obtained by varying the permutation inside \(C_h\), relative to a fixed reference order. Then
\[
\boxed{\Phi(\{\pi:\pi\text{ refines }\mathcal P\})
=\Phi(\pi_0)+D_1+\cdots+D_s.}
\tag{1}
\]
Consequently the parabolic product cell certifies a monochromatic full geodesic for every affine offset \(a\) whenever \(D_1+\cdots+D_s=V\).

*Proof.* The predecessor sum for an element of block \(C_h\) splits into contributions from all earlier blocks, fixed by the partition, and its predecessors inside \(C_h\), which vary only with that block. Changes from different blocks have disjoint row supports and add independently, giving (1). QED.

Write \(\Delta_{ij}=B_{ij}e_i+B_{ji}e_j\). By the adjacent-exchange syndrome formula, swapping consecutive directions \(i,j\) changes \(\Phi\) by \([\Delta_{ij}]\).

**Theorem 2 (commuting exchange cube).** Suppose \(q\) mutually vertex-disjoint unordered pairs \(\{i_h,j_h\}\) have projected exchange vectors \([\Delta_{i_hj_h}]\) forming a basis of \(V\). Then every offset \(a\) admits a monochromatic full antipodal geodesic. The \(2^q\) orders obtained by swapping these pairs independently, each pair kept consecutive, enumerate \(V\) bijectively under \(\Phi\).

*Proof.* Use the selected pairs as size-two blocks of a parabolic partition, with all remaining symbols as singleton blocks. The syndrome changes independently by the \(q\) basis vectors, so the \(2^q\) syndromes cover \(V\). QED.

**Theorem 3 (one cyclic root slide completes the cube).** It suffices to find an index \(k\) and \(q-1\) mutually disjoint pairs avoiding \(k\), for which
\[
\boxed{[e_k],\ [\Delta_{i_1j_1}],\ldots,[\Delta_{i_{q-1}j_{q-1}}]}
\tag{2}
\]
form a basis of \(V\). Then every affine offset admits a monochromatic full geodesic. Specifically, \(2^{q-1}\) independent pair-swap orders starting with \(k\), together with their cyclic rotations moving the initial \(k\) to the end, have all \(2^q\) possible syndromes.

*Proof.* The pair-swap orders cover one affine hyperplane in \(V\). Moving the first symbol \(k\) to the end changes the predecessor sum by \(e_k+Be_k\), since \(B\mathbf1=\mathbf1\); its quotient syndrome changes by \([e_k]\). This translates the first affine hyperplane to its disjoint complement, as required. QED.

**Example 4 (strict strength of the root-slide criterion).** Let \(n=6\), and specify the six row masks of \(B\), with binary bit \(j\) giving entry \(B_{ij}\), by
\[
(22,21,2,2,1,1).
\]
The matrix has zero diagonal, odd row sums and rank three. In the quotient, the nonzero pair-exchange syndromes are
\[
[\Delta_{02}]=1,\quad [\Delta_{04}]=[\Delta_{05}]=17,\quad
[\Delta_{12}]=[\Delta_{13}]=5,\quad[\Delta_{14}]=1.
\]
All remaining pair-exchange syndromes vanish. The nonzero exchange graph has no matching of three edges, so Theorem 2 cannot be applied. Nevertheless, \(k=2\), the pairs \(\{0,4\},\{1,3\}\), and the three vectors
\[
[e_2]=4,\qquad[\Delta_{04}]=17,\qquad[\Delta_{13}]=5
\]
satisfy (2). The eight orders obtained by swapping pairs \(04,13\) within \((2,0,4,1,3,5)\) and optionally moving the leading 2 to the end have syndrome representatives
\[
\{0,1,4,5,16,17,20,21\}=V.
\]
Thus the cyclic root slide closes an instance missed by the commuting matching.

**Interpretation.** These are dimension-simple gallery saturation criteria for arbitrary corank, with no restriction on the affine constants. They complement the known unconditional corank-at-most-two affine NORI1 result, but do not imply that every affine matrix possesses either certificate; the high-corank and nonlinear cases remain open.

**Theorem 5 (corank-three braid and root-slide saturation).** Let \(\dim V=3\). Choose \(k\) with \(w_k=[e_k]\ne0\) and three distinct directions \(i,j,h\ne k\). In \(\bar V=V/\langle w_k\rangle\cong\mathbb F_2^2\), put
\[
u=[\Delta_{ij}],\quad v=[\Delta_{ih}],\quad w=[\Delta_{jh}]
\quad\text{modulo }\langle w_k\rangle.
\]
If these vectors span \(\bar V\) and
\[
\boxed{u+v+w\ne0,}
\tag{3}
\]
then the six full orders starting with \(k\), followed by the six permutations of the braid block \(i,j,h\), then all remaining directions in one fixed order, together with their cyclic rotations moving \(k\) to the end, enumerate every syndrome in \(V\). Hence every affine offset has a monochromatic full antipodal geodesic.

*Proof.* Relative to ordering \(i,j,h\), the six braid permutations change the quotient syndrome by
\[
\{0,u,w,u+v,v+w,u+v+w\}.
\tag{4}
\]
These are sums of the three pair-inversion changes, each independent of the surrounding order. In a two-dimensional binary space, if \(u,v,w\) span, the set (4) contains all four values if and only if \(u+v+w\ne0\). Indeed, when their sum is zero, the three vectors are the distinct nonzero elements and (4) contains only \(\{0,u,w\}\). In every remaining spanning configuration (4) contains the fourth value as well. Root-sliding \(k\) to the end translates every syndrome by the independent class \(w_k\), supplying both lifts of all four values and exhausting \(V\). QED.

**Example 6 (braid closure with no nonzero independent matching).** Let \(n=6\) and take the binary influence matrix whose six row masks are
\[
(4,28,25,4,4,4).
\]
It has zero diagonal, odd row sums, and rank three. Its quotient has representatives with \([e_0]=1\); its nonzero projected exchange vectors are
\[
[\Delta_{02}]=1,\quad[\Delta_{23}]=8,\quad
[\Delta_{24}]=16,\quad[\Delta_{25}]=25,
\]
and every other pair-exchange vector vanishes. In particular, all nonzero exchanges share direction \(2\), so no two nonzero pairs can be disjoint. The earlier commuting-swap theorems cannot apply.

For \(k=0\) and braid triple \(\{2,3,4\}\), the quotient \(\bar V=V/\langle1\rangle\) has \(u=8,v=16,w=0\). These span \(\bar V\) and have sum \(24\ne0\). The six unrotated braid orders attain four distinct syndromes \(\{1,9,17,25\}\); sliding the leading \(0\) to the end adds one, giving \(\{0,8,16,24\}\). All eight syndromes therefore occur.

This establishes a strict hierarchy of dimension-simple certificates: commuting exchanges, one cyclic slide plus commuting exchanges, and a braid hexagon plus a cyclic slide. It is a general sufficient result for corank-three affine colorings, not a complete affine classification.
