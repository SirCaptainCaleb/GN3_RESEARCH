# Sharp rootwise random cube geodesics by singleton-block second moments

# Rooted random cube geodesics and permutation overlap moments

Fix a cube vertex \(x\), a prescribed color \(\epsilon\), and an arbitrary antipodally odd coloring \(c_0\) of \(Q_n\). Independently flip both colors in each antipodal edge orbit with probability \(\rho\in(0,1/2]\), producing \(c\).

**Theorem (optimal rootwise noise threshold).** If \(n\rho\to\infty\), the probability that there is an \(\epsilon\)-monochromatic geodesic from \(x\) to \(\tau x\) tends to one, uniformly over \(c_0\). Put \(h=3e(\rho^{-1}-1)/n\). If \(h<1\), the failure probability is at most \(h\). The growth assumption \(n\rho\to\infty\) is necessary for the uniform fixed-root, fixed-color assertion.

**Lemma (shared-edge moment).** Fix a coordinate permutation \(\pi\), take \(\sigma\in S_n\) uniformly, and let \(s\) be the number of cube edges common to the two root-to-antipode geodesics. For every \(z\ge1\),
\[
\mathbb E z^s\le\sum_{t=0}^n\frac{[3(z-1)]^t}{(n)_t}
\le\sum_{t=0}^n\left(\frac{3e(z-1)}n\right)^t.
\tag{1}
\]

*Proof.* Relabel so that \(\pi=(1,\ldots,n)\). The edge at rank \(k\) is common precisely when the first \(k\) symbols of \(\sigma\) are \([k]\) and its next symbol is \(k+1\). This is a singleton component of its direct-sum permutation decomposition. Prescribing \(t\) such positions divides the other \(n-t\) entries into \(t+1\) consecutive blocks of sizes \(a_0,\ldots,a_t\). The number of compatible permutations is \(\prod_j a_j!\). Expanding \(z^s=(1+z-1)^s\) gives
\[
\mathbb E z^s=\frac1{n!}\sum_{t=0}^n(z-1)^t
\sum_{\substack{a_0+\cdots+a_t=n-t\\a_j\ge0}}\prod_j a_j!.
\]
For all \(m\ge0\), \(\sum_{j=0}^m j!(m-j)!=m!\sum_j\binom mj^{-1}\le3m!\), since the two extreme reciprocals are one and each interior reciprocal is at most \(1/m\). Convolution induction bounds the inner sum by \(3^t(n-t)!\), giving the first inequality. The inequality \((n)_t\ge(n/e)^t\), obtained by comparing the geometric means of the largest \(t\) integers among \(1,\ldots,n\) with \((n!)^{1/n}\ge n/e\), proves the second. \(\square\)

*Proof of the theorem.* Let \(A_\pi\) be the event that the path of coordinate permutation \(\pi\) is all color \(\epsilon\), and \(q_\pi=\Pr(A_\pi)\). A geodesic uses each direction once, so its edges lie in distinct antipodal orbits, and \(q_\pi=\prod_{f\in P_\pi}p_f\), where \(p_f=\Pr(c(f)=\epsilon)\in[\rho,1-\rho]\). Define
\[
Z=\sum_{\pi\in S_n}\frac{\mathbf1_{A_\pi}}{q_\pi};
\qquad\mathbb EZ=n!.
\]
For two geodesics \(P_\pi,P_\sigma\), their simultaneous all-\(\epsilon\) event has probability zero if an edge of one is antipodal to an edge of the other. Otherwise all orbit variables are independent except for common edges, each contributing a joint-to-product factor \(1/p_f\le1/\rho\). Consequently
\[
\frac{\mathbb EZ^2}{(\mathbb EZ)^2}
\le\mathbb E_{\pi,\sigma}\rho^{-|E(P_\pi)\cap E(P_\sigma)|}
\le\sum_{t=0}^n h^t\le(1-h)^{-1}.
\]
The second-moment inequality gives \(\Pr(Z>0)\ge1-h\), proving the quantitative claim and the limit. Conversely choose the initial coloring with all \(n\) edges at \(x\) colored \(1-\epsilon\), completing antipodal pairs consistently. With probability \((1-\rho)^n\), none of these root edges flips, so no \(\epsilon\)-monochromatic path starts at \(x\). This failure probability stays positive whenever \(n\rho\) is bounded. \(\square\)

The result concerns full geodesics under noise, and is uniform over the baseline coloring. The deterministic NORI1 conjecture remains open.

**Corollary (coordinate-face smoothing).** Let \(F\) be an \(m\)-dimensional coordinate face of \(Q_n\), \(2\le m\le n\), and fix \(x\in F\) and a color \(\epsilon\). Independently flip the colors on full-cube antipodal edge pairs with probability \(\rho\). Then, uniformly in the initial antipodally odd coloring,
\[
\Pr(\text{no \(\epsilon\)-monochromatic geodesic in \(F\) between opposite face corners})
\le\frac{3e(\rho^{-1}-1)}m
\]
whenever the right side is below one. In particular, the failure probability is \(o(1)\) if \(m\rho\to\infty\).

*Proof.* A face geodesic uses each of its \(m\) free coordinates once, and hence meets distinct full-cube antipodal edge orbits. If \(F\) is proper, the full-cube antipodal translate of any edge of \(F\) lies outside \(F\), so two face geodesics can share an orbit only by using the same edge. In the full-face case, opposite edges between different geodesics produce incompatible prescribed-color events and contribute zero to their joint probability. Thus the weighted second-moment calculation and the permutation singleton-block bound of the theorem apply in either case, with \(m\) in place of \(n\). \(\square\)

**Lemma (opposite-chain edge exclusion).** Let \(P_\pi\) be the root-to-antipode coordinate geodesic given by a permutation \(\pi=(i_1,\ldots,i_n)\), and let \(P_{\pi^R}\) use its reverse permutation. Every root-to-antipode coordinate geodesic \(P_\sigma\) shares an edge with at most one of \(P_\pi,P_{\pi^R}\).

*Proof.* In resource-set coordinates relative to the root, the first path has edges between its consecutive prefix sets
\[
A_k=\{i_1,\ldots,i_k\},\qquad 0\le k\le n,
\]
whereas the second has edges between consecutive suffix sets
\[
B_j=\{i_{n-j+1},\ldots,i_n\},\qquad 0\le j\le n.
\]
If a monotone resource chain contained an edge \(A_k\to A_{k+1}\) followed by an edge \(B_j\to B_{j+1}\), its sets would satisfy \(A_{k+1}\subseteq B_j\). But \(i_1\in A_{k+1}\) and \(i_1\notin B_j\), since \(j\le n-1\). If the suffix edge occurred first, the chain would require \(B_{j+1}\subseteq A_k\), contradicted by \(i_n\in B_{j+1}\) and \(i_n\notin A_k\). These exhaust the possible orders. \(\square\)

**Theorem (full edge-color profile universality).** Under the hypotheses of the rootwise smoothing theorem, fix an arbitrary predetermined word \(w=(w_1,\ldots,w_n)\in\{0,1\}^n\) and a root \(x\). There is a root-to-antipode geodesic whose consecutive edge colors form \(w\), with failure probability at most
\[
\boxed{\frac{2h}{1+h},\qquad
h=\frac{3e(\rho^{-1}-1)}n<1.}
\]
In particular this probability tends to one uniformly in the baseline coloring and prescribed word whenever \(n\rho\to\infty\). The growth condition is necessary for a uniform fixed-root, fixed-word assertion.

*Proof.* For every \(\pi\in S_n\), let \(A_\pi\) be the event that the sequence of colors along \(P_\pi\) is \(w\), let \(q_\pi=\Pr(A_\pi)>0\), and set \(Z=\sum_\pi\mathbf1_{A_\pi}/q_\pi\). Since each coordinate is used once, a single path visits distinct antipodal noise-variable orbits and \(\mathbb EZ=n!\).

A pair of paths may share a noise orbit through a common cube edge or through antipodal partner edges. When the two demands on a shared orbit conflict, their joint success probability is zero; otherwise that orbit contributes a joint-to-product factor at most \(\rho^{-1}\). Let \(K_+(\pi,\sigma)\) count edges common to \(P_\pi,P_\sigma\), and let \(K_-(\pi,\sigma)\) count edges common to \(P_{\pi^R},P_\sigma\). The antipodal image of the edge set of \(P_\pi\) is the edge set of \(P_{\pi^R}\), so \(K_++K_-\) counts shared noise orbits. By the opposite-chain exclusion lemma, \(K_+K_-=0\). Therefore, for \(z\ge1\),
\[
\begin{aligned}
\mathbb E_{\pi,\sigma}z^{K_++K_-}
&=1+\mathbb E(z^{K_+}-1)+\mathbb E(z^{K_-}-1)\\
&=2\mathbb E_{\pi,\sigma}z^{K_+}-1.
\end{aligned}
\]
The two overlap counts have identical marginal distributions under uniform permutations. Apply the singleton-block moment bound with \(z=\rho^{-1}\) to obtain
\[
\frac{\mathbb EZ^2}{(\mathbb EZ)^2}
\le2(1-h)^{-1}-1=\frac{1+h}{1-h}.
\]
Cauchy--Schwarz now yields \(\Pr(Z>0)\ge(1-h)/(1+h)\), proving the failure estimate. For necessity, prescribe the first edge color \(w_1\) and choose the initial coloring with all \(n\) root-incident edges of color \(1-w_1\). The probability that none flips is \((1-\rho)^n\), bounded away from zero when \(n\rho\) stays bounded. \(\square\)

On a proper \(m\)-face, no two of its edges lie in the same full-cube antipodal orbit. Hence the face corollary also holds for every prescribed length-\(m\) color word with its original failure bound \(3e(\rho^{-1}-1)/m\). The new theorem establishes a common fixed-pattern smoothing principle with the rooted boundary Hamiltonian-window theorem.
