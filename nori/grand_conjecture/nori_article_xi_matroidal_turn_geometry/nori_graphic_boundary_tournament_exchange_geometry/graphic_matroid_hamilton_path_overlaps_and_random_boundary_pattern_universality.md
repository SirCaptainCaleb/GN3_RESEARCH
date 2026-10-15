# Graphic-matroid Hamilton path overlaps and random boundary pattern universality

# Hamilton path-forest overlaps and random boundary pattern universality

Let \(n\ge3\). Give each reversal-pair of distinct ordered triples an independent fair bit and its reverse the complementary bit. For a Hamilton vertex ordering \(\pi\), let \(W_b(\pi)\in\{0,1\}^{n-2}\) be its consecutive triple-color word. The \(n-2\) reversal-orbits along \(\pi\) are distinct, so \(W_b(\pi)\) is uniform.

**Theorem 1 (full-rank pattern second moment).** For any predetermined nonempty set \(A\subseteq\{0,1\}^{n-2}\), let \(Z\) count the Hamilton orders with word in \(A\), and put
\[
p=|A|2^{2-n},\qquad c_n=\frac{(e^2-1)(n-2)}{n(n-1)}.
\]
Then
\[
\boxed{\mathbb EZ=n!p,\quad\operatorname{Var}(Z)\le c_n(\mathbb EZ)^2,\quad
\Pr(Z>0)\ge(1+c_n)^{-1}.}
\tag{1}
\]
Moreover \(\Pr(Z<(1-\delta)\mathbb EZ)\le c_n/\delta^2\) for \(0<\delta<1\).

*Proof.* For two vertex permutations \(\pi,\sigma\), let \(K\) count the reversal-orbits of length-three windows they share. Their two color words together involve \(2(n-2)-K\) independent bits. Counting pairs of allowed words while disregarding compatibility on shared bits gives
\[
\Pr(W_b(\pi)\in A,\ W_b(\sigma)\in A)\le p^2 2^K.
\tag{2}
\]
Fix \(\pi\). Any \(k\) of its consecutive-triple windows contain a path forest of \(s\ge k+1\) edges of \(K_n\), with at most \(k\) nontrivial path components. For \(\sigma\) to contain all the selected triple-orbits, its consecutive adjacency edges must contain this forest. A path forest of \(s\) edges and \(c\) nontrivial components occurs in \(2^c(n-s)!\) permutations: orient each path component, contract it to one block, and permute all blocks. Thus
\[
\mathbb E_\sigma\binom Kk
\le\binom{n-2}k\frac{2^k(n-k-1)!}{n!}
=\frac{2^k(n-k-1)}{k!\,n(n-1)}.
\tag{3}
\]
Using \(2^K=\sum_{k=0}^K\binom Kk\), we obtain
\[
\mathbb E_\sigma 2^K\le1+
\frac{n-2}{n(n-1)}\sum_{k\ge1}\frac{2^k}{k!}
=1+c_n.
\tag{4}
\]
Sum (2) over all ordered permutation pairs to obtain
\(\mathbb E Z^2\le(1+c_n)(\mathbb EZ)^2\).
The variance estimate follows by subtraction, the positivity bound by Cauchy–Schwarz, and the lower-tail bound by Chebyshev. \(\square\)

**Corollary 2 (almost-all spanning one-turn boundary paths).** The number of binary words of length \(n-2\) with at most one color change is \(2(n-2)\). Therefore, if \(Z_{\le1}\) counts full spanning at-most-one-turn vertex-simple tight paths,
\[
\boxed{\mathbb EZ_{\le1}=n!(n-2)2^{3-n},\qquad
\Pr(Z_{\le1}=0)\le\frac{c_n}{1+c_n}=O(n^{-1}).}
\tag{5}
\]
With probability at least \(1-4c_n\), there are at least \(\frac12\mathbb EZ_{\le1}\) such paths. For any single prescribed color word, its realization by some Hamilton order has probability at least \(1/(1+c_n)\). Simultaneous realization of all color words is not claimed.

**Theorem 3 (fixed fractional Hamilton selector obstruction).** Let \(\lambda\) be an arbitrary distribution on Hamilton vertex paths selected independently of the tournament coloring, and let \(\operatorname{sw}_b(\pi)\) count the changes along its triple-color word. Then
\[
\boxed{\mathbb E_b\mathbb E_{\pi\sim\lambda}\operatorname{sw}_b(\pi)=\frac{n-3}{2}.}
\tag{6}
\]
In particular, for \(n\ge6\), some reversal-odd coloring has \(\mathbb E_{\pi\sim\lambda}\operatorname{sw}_b(\pi)>1\).

*Proof.* For any fixed \(\pi\), its two successive triple windows lie in distinct reversal-orbits and their colors are independent fair bits. Each of its \(n-3\) change indicators therefore has expectation \(1/2\). Average first over \(b\), then over \(\lambda\). Some coloring attains at least that mean. \(\square\)

**Graphic-matroid interpretation.** A Hamilton path's \(n-1\) edges form a basis of \(M(K_n)\), with the additional degree-two path condition. Each triple window is a two-edge flag of that basis. Any \(k\) common flags between two Hamilton words require at least \(k+1\) shared graphic basis edges. This additional edge gives the \(O(n^{-1})\) overlap-energy bound. The results are full-resource and all-dimensional, but do not close the worst-case spanning one-turn conjecture. Theorem 3 precludes a coloring-independent fractional basis mixture as a universal average-cost certificate; the missing witness must adapt to the coloring and preserve the integral path constraints.
