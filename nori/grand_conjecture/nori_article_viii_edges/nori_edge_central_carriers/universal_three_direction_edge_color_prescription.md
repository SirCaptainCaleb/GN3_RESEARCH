# Universal three-direction edge-color prescription

# Universal three-direction prescription for unrestricted antipodally odd cube-edge colorings

**Theorem.** Let \(n\ge3\) and let \(c_i(x)\in\mathbb F_2\) color each *physical undirected* direction-\(i\) edge of \(Q_n\), satisfying
\[
c_i(x)=c_i(x\oplus e_i),\qquad c_i(\bar x)=1+c_i(x).
\]
For **every** three distinct directions \(i,j,k\) and **every** prescribed color triple \((t_i,t_j,t_k)\in\mathbb F_2^3\), some genuine full antipodal geodesic (root and complete permutation unrestricted) traverses its \(i\)-, \(j\)- and \(k\)-edges in exactly the prescribed colors. Equivalently, the set \(\mathcal W(c)\) of full direction-indexed edge-color profiles projects **surjectively** to \(\mathbb F_2^3\) on every three-coordinate set. There are no restrictions on nonlinearity, exterior dependence, or the colors of the remaining \(n-3\) edges.

**Root-rotation identity.** For a full geodesic with root \(x\) and direction order \(p=(p_1,\ldots,p_n)\), use root \(x\oplus e_{p_1}\) and order \((p_2,\ldots,p_n,p_1)\). The new path traverses the *same physical edges* in all directions other than \(p_1\). Its final \(p_1\)-edge is antipodal to the original first edge; thus its direction-indexed color profile is the original profile with precisely coordinate \(p_1\) complemented. This relies on both undirected physicality and edge antipodal oddness.

**Proof.** Suppose some prescribed triple never occurs. Complement the color of *every physical edge* in direction \(r\in\{i,j,k\}\) by \(t_r\), leaving all other edge directions alone. Both edge axioms survive, and the impossible triple becomes \(000\). Taking the antipodal root of any full geodesic with the **same** coordinate order complements every direction's color, so \(111\) is also impossible.

Choose an arbitrary root \(x\) and complete direction order \(p=(i,j,k,r_4,\ldots,r_n)\); write \(A,B,D\) for the actual edge colors at its first three steps. Rotate the first direction to the end three times, updating the root as above. The four resulting **genuine full antipodal geodesics** have projected triples
\[
(A,B,D),\
(A+1,B,D),\
(A+1,B+1,D),\
(A+1,B+1,D+1).
\tag{1}
\]
None may be \(000\) or \(111\). A three-step geodesic of the three-cube avoiding these two opposite vertices must have starting bits \(010\) or \(101\) in its *step order*: its four successive Hamming weights must be \(1,2,1,2\), or \(2,1,2,1\). Consequently for **every root** and **every full order with prefix \(i,j,k\)** the first three edge colors are
\[
(A,B,D)=(q,1+q,q). \tag{2}
\]

Now compare the two full direction orders \((i,j,k,r_4,\ldots,r_n)\) and \((j,i,k,r_4,\ldots,r_n)\) *from the same arbitrary root \(x\)*. They traverse the **same physical \(k\)-edge** at their third step, since in both cases they have already flipped exactly the directions \(i,j\). By (2), the first color on each path equals its common third color. Therefore
\[
c_i(x)=c_j(x)\qquad\text{for every }x\in Q_n. \tag{3}
\]
Apply (3) also at \(x\oplus e_i\) and use that \(c_i\) is the color of an **undirected** \(i\)-edge:
\[
c_j(x\oplus e_i)=c_i(x\oplus e_i)=c_i(x).
\]
But these are exactly the colors of the first and second edges in the original path with prefix \((i,j,k)\), and (2) demands that those two colors are *different*. Contradiction. Thus every prescribed triple occurs. \(\square\)

**Research significance and exact limitation.** This strengthens NORI's previously recorded unrestricted **two-direction prescription** corollary to **three-direction prescription** for the *whole* NORI1 class. Full affine span of the profile set by itself does not imply triple surjectivity; the essential new ingredient is that cyclic geodesic root slides realize the three-cube walk (1), whose avoidance of one antipodal pair is rigid. Any failure to realize a *complete* target \(n\)-bit word must therefore involve compatibility among **at least four directions**, not a missing one-, two-, or three-direction marginal. The result does not yet force the all-zero or all-one full profile and does not solve unrestricted NORI1. It also does not prove a statement for ordered-three-face boundary tournaments: here the local colors attach to actual edges, and the root slide complements exactly one direction-indexed edge color.

**Consistency check (not used in proof).** Direct enumeration of all \(2^{16}\) legal physical antipodally odd edge colorings of \(Q_4\) found complete four-bit profile coverage; separate binary-integer feasibility tests found no obstruction to triple prescription in dimensions five, six, and seven. The argument above is valid in every dimension independently of these checks.
