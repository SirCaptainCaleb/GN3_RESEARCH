# Cyclic-turn averaging, disjoint exchanges, and the ten-dimensional two-switch theorem

Let \(n\ge5\), and let \(c\) color the undirected edges of \(Q_n\) with values in \(\{0,1\}\), subject to \(c(\bar e)=1-c(e)\). Write \(c_i(v)\) for the color of the edge in direction \(i\) incident with \(v\). Let \(\sigma(P)\) denote the number of color changes on a full antipodal geodesic \(P\), and put \(\mu(c)=\min_P\sigma(P)\).

For \(0\le k\le n\) set \(m(k)=\min\{k,n-k\}\) and define
\[
\lambda_n(k)=
\begin{cases}
0,&m(k)=0,\\
\dfrac{4k(n-k)(m(k)-1)}{n(n-1)(n-2)},&0<m(k)<n/2,\\
\dfrac{4k(n-k)(m(k)-2)}{n(n-1)(n-3)},&m(k)=n/2.
\end{cases}\tag{1}
\]
The last case occurs only when \(n\) is even. Set
\[
q_n=\left\lfloor\frac{n-1}{3}\right\rfloor,\qquad
\Phi_n(k)=\frac{2k(n-k)}{n-1}-\frac{q_n}{2}\lambda_n(k).\tag{2}
\]

**Theorem 1 (unrestricted exchange-averaging bound).** Every antipodally odd coloring of the edges of \(Q_n\) satisfies
\[
\boxed{\mu(c)\le
2\left\lfloor
\frac{\max_{0\le k\le n}\Phi_n(k)-1}{2}
\right\rfloor.}\tag{3}
\]
No restriction is imposed on the dependence of an edge color on the other coordinates.

**Corollary 2 (dimension ten).** Every antipodally odd edge coloring of \(Q_{10}\) has a full antipodal geodesic with at most two changes:
\[
\boxed{\mu(c)\le2\qquad(n=10).}\tag{4}
\]

**Corollary 3 (linear bound in all dimensions).** Uniformly over antipodally odd edge colorings,
\[
\mu(c)\le \frac{28\sqrt7-40}{81}\,n+O(1)
       =0.42075354\ldots\,n+O(1).\tag{5}
\]

The proof counts disagreements between incident edge colors and improves the resulting average by exchanging disjoint pairs of consecutive directions.

**Lemma 4 (cyclic comparison identity).** Let \(P\) start at \(x\), traverse directions \(p_1,\ldots,p_n\), and have edge-color word \(w_1,\ldots,w_n\). Put \(v_s=x\oplus e_{p_1}\oplus\cdots\oplus e_{p_s}\), and for distinct \(i,j\) write \(d_{ij}(v)=[c_i(v)\ne c_j(v)]\). Define
\[
T(P)=\sum_{s=1}^{n-1}d_{p_s,p_{s+1}}(v_s)
                         +d_{p_n,p_1}(v_n).\tag{6}
\]
Then
\[
T(P)=\sum_{s=1}^{n-1}[w_s\ne w_{s+1}]
                         +[w_n\ne1-w_1]\tag{7}
\]
is a positive odd integer. A cyclic rotation of \(P\), with its root moved along the geodesic, has \(T(P)-1\) changes. If \(P\) is chosen uniformly among all \(2^n n!\) rooted full geodesics, and \(k_v=|\{i:c_i(v)=1\}|\), then
\[
\mathbb E T(P)=\frac{2}{(n-1)2^n}
                    \sum_{v\in Q_n}k_v(n-k_v).\tag{8}
\]

*Proof.* The first \(n-1\) terms of (6) are the successive comparisons in the word of \(P\). At \(v_n=\bar x\), the incoming \(p_n\)-edge has color \(w_n\), while the \(p_1\)-edge has color \(1-w_1\), by antipodal oddness. This proves (7). The XOR of its \(n\) comparison bits is one, hence \(T(P)\) is odd.

Moving the root across the first \(s\) directions and transferring those directions to the end gives the color word
\[
w_{s+1},\ldots,w_n,1-w_1,\ldots,1-w_s.
\]
Its \(n-1\) comparisons omit one of the \(n\) comparisons of (7), and the omitted position ranges over all \(n\) positions as \(s\) varies. One omitted comparison can be a change, giving \(T(P)-1\).

For a uniformly rooted full geodesic, at each of the \(n\) positions in (6) the vertex is uniform in \(Q_n\), and the incident directions form a uniform ordered pair of distinct directions. At vertex \(v\), there are \(2k_v(n-k_v)\) bichromatic ordered pairs among the \(n(n-1)\) possibilities. Adding their expected contributions over \(n\) positions proves (8). \(\square\)

**Lemma 5 (exchange gain from a colored vertex star).** Sample uniformly a vertex \(v\) and four distinct ordered directions \(h,i,j,\ell\). Consider a full geodesic with consecutive directions \(h,i,j,\ell\) such that its vertex after the \(h\)-step is \(v\). Let \(\Delta\) be the change in \(T\) when \(i,j\) are exchanged. Then
\[
\mathbb E|\Delta|\ge\frac1{2^n}\sum_{v\in Q_n}\lambda_n(k_v).\tag{9}
\]

*Proof.* Only the comparisons at the three vertices \(v,v^i\) or \(v^j\), and \(v^{ij}\) can change. Hence, with the sign convention new minus old,
\[
\begin{aligned}
\Delta={}&d_{h,j}(v)-d_{h,i}(v)
+d_{j,i}(v^j)-d_{i,j}(v^i)\\
&+d_{i,\ell}(v^{ij})-d_{j,\ell}(v^{ij}).\tag{10}
\end{aligned}
\]
Fix \(v,i,j,\ell\). The last four terms are independent of \(h\). When \(c_i(v)=c_j(v)\), use the lower bound zero. Otherwise the first two terms total \(+1\) or \(-1\), with the sign determined by \(c_h(v)\).

Let \(a,b\) count the directions of the two colors among the \(n-3\) remaining directions after excluding \(i,j,\ell\). For any real \(K\), the triangle inequality gives
\[
\frac{a|K+1|+b|K-1|}{n-3}
\ge\frac{2\min(a,b)}{n-3}.\tag{11}
\]
This bounds the conditional mean of \(|\Delta|\) over \(h\).

Fix \(k=k_v\), \(m=\min(k,n-k)\). The probability that uniformly chosen distinct \(i,j\) are bichromatic is \(2k(n-k)/(n(n-1))\). Conditional on this event, removal of \(i,j\) leaves color counts \(m-1,n-m-1\). Choose \(\ell\) uniformly from the other \(n-2\) directions. If \(m<n/2\), the mean of the smaller remaining color count after removal of \(\ell\) is \((m-1)(n-3)/(n-2)\). If \(m=n/2\), it is \(m-2\). Combining these quantities with (11) gives the two nonzero cases of \(\lambda_n(k)\) in (1). For \(m=0\), there are no bichromatic pairs. Average over \(v\) to obtain (9). \(\square\)

*Proof of Theorem 1.* Select the \(q=q_n\) adjacent pairs of positions
\[
(2,3),\ (5,6),\ (8,9),\ldots,
(2+3(q-1),3+3(q-1)).\tag{12}
\]
Each has a preceding and following direction. For a full geodesic \(P\), let \(\Delta_s(P)\) be the difference in \(T(P)\) caused by exchanging the directions in pair \(s\).

The three consecutive comparison positions affected by each exchange are disjoint from those affected by the other exchanges in (12). Exchanging a pair also preserves the vertex and used-coordinate set following its second step. Thus the changes are additive. Choosing the exchanges independently, the least comparison count among the resulting \(2^q\) orders is
\[
T(P)+\sum_{s=1}^q\min\{0,\Delta_s(P)\}.\tag{13}
\]
Now choose \(P\) uniformly among all rooted full geodesics. Swapping either specified pair is an involution of this uniform space, so \(\mathbb E\Delta_s(P)=0\). Using \(\min(0,z)=(z-|z|)/2\), equations (8)--(9) give
\[
\begin{aligned}
\mathbb E[\text{quantity in (13)}]
&\le\frac1{2^n}\sum_v
\left(\frac{2k_v(n-k_v)}{n-1}
-\frac q2\lambda_n(k_v)\right)\\
&\le \max_{0\le k\le n}\Phi_n(k).
\end{aligned}\tag{14}
\]
There is therefore a modified full geodesic with \(T\) no larger than the right side. Its \(T\) is odd. Lemma 4 and the parity of \(T\) give (3). \(\square\)

*Proof of Corollary 2.* For \(n=10\), \(q_n=3\) and \(\Phi_{10}(k)=\Phi_{10}(10-k)\). Substitution in (1)--(2), for \(k=0,1,2,3,4,5\), gives
\[
0,\quad2,\quad\frac{154}{45},\quad\frac{259}{60},
\quad\frac{71}{15},\quad\frac{305}{63}.
\]
Thus \(\max_k\Phi_{10}(k)=305/63<5\). The odd positive integer \(T\) of the supplied full geodesic is at most three. A root rotation therefore gives \(\mu(c)\le2\). \(\square\)

*Proof of Corollary 3.* Let \(t=\min(k,n-k)/n\in[0,1/2]\). Since \(q_n=n/3+O(1)\), equations (1)--(2) yield uniformly in \(k\)
\[
\frac{\Phi_n(k)}n
=2t(1-t)-\frac23t^2(1-t)+O(n^{-1}).\tag{15}
\]
The polynomial is maximized on \([0,1/2]\) at \(t_*=(4-\sqrt7)/3\), with value \((28\sqrt7-40)/81\). Insert this maximum into (3). \(\square\)

The inequalities constrain every admissible coloring through the degrees of the two colors at its vertices. They combine antipodal root rotation with several simultaneously available path exchanges. The ten-dimensional conclusion does not require an inductive hypothesis or a structural classification of face colorings.
