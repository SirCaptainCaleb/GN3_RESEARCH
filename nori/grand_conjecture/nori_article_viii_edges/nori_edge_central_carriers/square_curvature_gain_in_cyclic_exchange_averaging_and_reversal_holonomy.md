# Square-curvature gain in cyclic exchange averaging and reversal holonomy

Let \(n\ge5\), and let \(c\) be an antipodally odd coloring of the undirected edges of \(Q_n\). Write \(c_i(v)\) for the color of the edge in direction \(i\) incident with \(v\), and set
\[
d_{ij}(v)=[c_i(v)\ne c_j(v)],\qquad
k_v=\sum_i c_i(v),\qquad m_v=\min(k_v,n-k_v).
\]
For \(i\ne j\), put \(v^{ij}=v\oplus e_i\oplus e_j\) and define the square curvature
\[
\kappa_{ij}(v)=c_i(v)\oplus c_j(v^i)\oplus c_i(v^j)\oplus c_j(v).
\tag{1}
\]
All sums in (1) are modulo two. Since \(c_i(v^j)=c_i(v^{ij})\) and \(c_j(v^i)=c_j(v^{ij})\), we have
\[
\boxed{\kappa_{ij}(v)=d_{ij}(v)\oplus d_{ij}(v^{ij}).}\tag{2}
\]
Thus curvature is the disagreement between the two opposite-vertex bichromatic-turn indicators of a square.

Recall the functions \(\lambda_n(k)\), \(\Phi_n(k)\), and \(q_n=\lfloor(n-1)/3\rfloor\) from the preceding cyclic-turn exchange theorem. Define
\[
\eta_n(k)=
\begin{cases}
0,&\min(k,n-k)=0,\\[1mm]
\dfrac{2(\min(k,n-k)-1)}{n-2}
+\dfrac{\mathbf1_{\{n\ {\rm even},\,k=n/2\}}}{n-3},
&\min(k,n-k)\ge1,
\end{cases}
\tag{3}
\]
and the nonnegative curvature-weighted statistic
\[
\mathcal K_n(c)=
\frac1{2^n n(n-1)}
\sum_{v\in Q_n}\sum_{i\ne j}
[d_{ij}(v)=1,\ d_{ij}(v^{ij})=0]\,
\eta_n(k_v).
\tag{4}
\]

**Theorem 1 (curvature-sensitive all-dimensional exchange bound).** Every antipodally odd edge coloring of \(Q_n\), \(n\ge5\), satisfies
\[
\boxed{\displaystyle
\mu(c)\le 2\left\lfloor
\frac{\frac1{2^n}\sum_v\Phi_n(k_v)
-\frac{q_n}{2}\mathcal K_n(c)-1}{2}
\right\rfloor.}
\tag{5}
\]
In particular, a counterexample to \(\mu(c)\le2\) in dimension \(n\) must satisfy
\[
\boxed{\displaystyle
\frac1{2^n}\sum_v\Phi_n(k_v)
-\frac{q_n}{2}\mathcal K_n(c)\ge5.}
\tag{6}
\]
The improvement over the earlier exchange bound is additive and nonnegative for every coloring, with a positive contribution whenever some curved square has a bichromatic corner at which both edge colors occur at least twice.

**Proof.** For a uniformly chosen vertex \(v\) and distinct ordered directions \(h,i,j,\ell\), form the two full geodesics differing by the exchange of adjacent directions \(i,j\) inside the consecutive block \(h,i,j,\ell\), with \(v\) immediately after \(h\). Let \(\Delta\) be the change in their cyclic turn counts. Set \(w=v^{ij}\). The comparison formula established in the preceding exchange lemma is
\[
\Delta=d_{hj}(v)-d_{hi}(v)
+d_{ij}(v^j)-d_{ij}(v^i)
+d_{i\ell}(w)-d_{j\ell}(w).\tag{7}
\]
Here \(d_{ij}=d_{ji}\). The middle difference is zero if \(d_{ij}(v)=d_{ij}(w)\), and is \(+1\) or \(-1\) otherwise; this follows from the four-corner identity
\[
d_{ij}(v)\oplus d_{ij}(v^i)\oplus
d_{ij}(v^j)\oplus d_{ij}(w)=0.\tag{8}
\]

There are four possibilities for \((d_{ij}(v),d_{ij}(w))\).

When it equals \((0,0)\), all three differences in (7) vanish.

When it equals \((1,1)\), the middle difference vanishes and each outer difference is \(+1\) or \(-1\). Fixing \(\ell\), the first difference takes these two signs as the color of \(h\) varies. There are \(n-3\) choices of \(h\), with color multiplicities \(a,b\) among these directions. The triangle inequality shows that the mean of \(|\Delta|\) over \(h\) is at least \(2\min(a,b)/(n-3)\). Averaging over \(\ell\) yields the lower bound
\[
g_n(k_v)=
\begin{cases}
\dfrac{2(m_v-1)}{n-2},&2m_v<n,\\
\dfrac{2(m_v-2)}{n-3},&2m_v=n,
\end{cases}\tag{9}
\]
provided \(d_{ij}(v)=1\).

When the pair is \((1,0)\), the last difference vanishes, and the middle difference has absolute value one. The first difference has the two possible signs according to the color of \(h\). Since \(h\) is uniform among the \(n-2\) directions outside \(\{i,j\}\), the mean satisfies
\[
\mathbb E_{h,\ell}|\Delta|
\ge g_n'(k_v):=\frac{2(m_v-1)}{n-2}.\tag{10}
\]
Thus relative to the bound (9), this case supplies the extra \(g_n'(k_v)-g_n(k_v)\), which is \(1/(n-3)\) when \(n\) is even and \(k_v=n/2\), and zero otherwise.

Finally, when the pair is \((0,1)\), the first difference vanishes and the middle difference has absolute value one. The last difference, as \(\ell\) varies among the \(n-2\) remaining directions, has two possible signs. Consequently
\[
\mathbb E_{h,\ell}|\Delta|\ge g_n'(k_w).\tag{11}
\]
Averaging (11) over uniformly chosen \(v,i,j\) and replacing \(v\) by \(w=v^{ij}\) identifies its contribution with the \((1,0)\) cases, weighted by \(g_n'(k_v)\). Combining the four cases, using (9)--(11), gives
\[
\boxed{
\mathbb E|\Delta|
\ge \frac1{2^n}\sum_v\lambda_n(k_v)+\mathcal K_n(c).
}\tag{12}
\]
Indeed, the first term is the mean over bichromatic ordered pairs at \(v\) of the bound \(g_n(k_v)\), and the remaining two contributions total \(2g_n'-g_n=\eta_n\) on the \((1,0)\) cases.

Apply the \(q_n\) independent position-pair exchanges from the preceding theorem. Their changes in cyclic turn count are additive; each has mean zero and has the absolute-change estimate (12). As before, averaging over the initial rooted geodesic and choosing the better orientation of every exchange gives a full geodesic with odd cyclic turn count at most
\[
\frac1{2^n}\sum_v\Phi_n(k_v)-\frac{q_n}{2}\mathcal K_n(c).
\]
Cyclically rotating its coordinate order removes one changed comparison, proving (5). If \(\mu(c)>2\), then this odd turn count is at least five, yielding (6). \(\square\)

**Corollary 2 (a restriction on eleven-dimensional counterexamples).** Suppose \(n=11\) and every vertex is incident with five or six edges of color one. Let
\[
\delta(c)=
\frac{\#\{\text{two-dimensional faces with odd curvature}\}}
{\binom{11}{2}2^9}.
\tag{13}
\]
Then
\[
\boxed{
\mu(c)\le
2\left\lfloor\frac{58/11-(2/3)\delta(c)-1}{2}\right\rfloor.
}\tag{14}
\]
In particular, \(\delta(c)>9/22\) implies \(\mu(c)\le2\). Every putative four-switch example with balanced incident-color degrees must have \(\delta(c)\le9/22\).

*Proof.* At every vertex, \(\Phi_{11}(k_v)=58/11\) and \(m_v=5\), so \(\eta_{11}(k_v)=8/9\). On each odd-curvature square, precisely two of its four vertices satisfy \(d_{ij}(v)=1\) and \(d_{ij}(v^{ij})=0\). Counting both orders of \(i,j\) gives \(\mathcal K_{11}(c)=(4/9)\delta(c)\). Since \(q_{11}=3\), substitute in (5). \(\square\)

The curvature statistic also obeys an independent parity law.

**Theorem 3 (antipodal reversal holonomy).** Let \(P\) be any full antipodal geodesic, rooted at \(x\), with direction order \(p_1,\ldots,p_n\). Reverse this order at the same root by adjacent exchanges. If \(S_1,\ldots,S_{\binom n2}\) are the successive squares traversed by any reduced adjacent-transposition reversal, then
\[
\boxed{\bigoplus_{r=1}^{\binom n2}\kappa(S_r)=n\pmod2.}\tag{15}
\]
Consequently, in every odd dimension, every such reversal sequence encounters an odd number of curved squares. Writing \(\delta_{ij}\) for the proportion of curved squares parallel to directions \(i,j\), every admissible coloring in odd dimension satisfies
\[
\boxed{\sum_{i<j}\delta_{ij}\ge1,\qquad
\delta(c):=\frac1{\binom n2}\sum_{i<j}\delta_{ij}
\ge \frac1{\binom n2}.}\tag{16}
\]
The second bound is sharp even among colorings for which every vertex is incident with \((n-1)/2\) or \((n+1)/2\) edges of color one.

*Proof.* Let \(w_1,\ldots,w_n\) be the edge colors along \(P\). The geodesic with reversed direction order and the same root has colors \(1-w_n,\ldots,1-w_1\), because each of its edges is antipodal to the corresponding edge of \(P\). Therefore the parity of the sum of its edge colors differs by \(n\pmod2\). Each adjacent transposition replaces a two-edge route across a square by the other two-edge route, changing this parity by the square curvature. Summing over the reversal proves (15).

For odd \(n\), the number of curved squares in every reversal is odd and positive. Choose the root and the original order uniformly. Each unordered direction pair is exchanged once in the reduced reversal, and the square at which it is exchanged is uniform among the \(2^{n-2}\) squares of those directions (by translation symmetry of the sampled root). Hence the expected number of curved squares in the reversal is \(\sum_{i<j}\delta_{ij}\), proving (16).

For sharpness, write \(n=2m+1\), designate the final coordinate by \(u\), and on an edge in direction \(i\) assign
\[
c_{2a-1}(v)=v_u,\qquad c_{2a}(v)=1-v_u
\quad(1\le a\le m),\qquad
c_u(v)=v_1\oplus\cdots\oplus v_{2m-1}.
\tag{17}
\]
These values are independent of the coordinate being traversed, so define undirected-edge colors. All defining functions change under complementation of every coordinate, making the coloring antipodally odd. Every pair \(2a-1,2a\) contributes one edge of each color at every vertex, while direction \(u\) contributes either color; the degree condition follows. The curvature vanishes on every direction pair except \(\{2m,u\}\), and every square in that pair has curvature one. Thus \(\sum_{i<j}\delta_{ij}=1\), proving sharpness. \(\square\)

Theorems 1 and 3 combine two complementary constraints on unrestricted instances: color imbalance at individual vertex stars governs the baseline cyclic turn count, while nonflat two-faces force extra exchange opportunities. The sharpness example shows that parity alone supplies only \(O(n^{-2})\) square-curvature density in odd dimension; stronger dimension-uniform conclusions require additional correlations between these local statistics.
