# High-index actual-geodesic carrier forces a Tucker-complementary pair of mirror-median color-change walls

# A Tucker complementary-median-switch pair among ACTUAL full NORI geodesics

Fix \(n\ge7\), any root \(x\in Q_n\), and an active physical ordered-three-face NORI coloring \(c(\bar F,\operatorname{rev}\pi)=1\oplus c(F,\pi)\). Let
\[
\mathcal B_x=\{\pi: w_1(x,\pi)\ne w_{n-2}(x,\pi)\}
\]
be the actual rooted FULL geodesics whose first and last ordered-three-face colors are OPPOSITE. The previously proved genuine-geodesic permutohedral face nerve \(K_x\) has vertices \(\mathcal B_x\), simplices consisting of endpoint-opposed permutation vertices lying in a common PROPER face of the standard permutohedron, a free involution \(\pi\mapsto\operatorname{rev}\pi\), and
\[
w_1(K_x/\tau)^{n-3}\ne0.
\tag{1}
\]

Write \(m=n-3\) for the number of adjacent-window switch positions. For each \(\pi\in\mathcal B_x\), let \(S(\pi)=\{j\in[m]:w_j(x,\pi)\ne w_{j+1}(x,\pi)\}\). Since the endpoint colors differ, \(|S(\pi)|\) is ODD and nonzero. Define \(j_*(\pi)\in[m]\) as its unique MEDIAN element. Under the actual full-path NORI antipodal reversal rooted at the SAME \(x\),
\[
S(\operatorname{rev}\pi)=\{m+1-j:j\in S(\pi)\},\qquad
j_*(\operatorname{rev}\pi)=m+1-j_*(\pi).
\tag{2}
\]

Put \(r=\lceil m/2\rceil\), and define a signed scalar Tucker label \(\lambda_x:\mathcal B_x\to\{\pm1,\ldots,\pm r\}\) by:

- If \(j_*(\pi)<(m+1)/2\), assign \(\lambda_x(\pi)=+\min\{j_*(\pi),m+1-j_*(\pi)\}=+j_*(\pi)\).
- If \(j_*(\pi)>(m+1)/2\), assign \(\lambda_x(\pi)=-\min\{j_*(\pi),m+1-j_*(\pi)\}=-(m+1-j_*(\pi))\).
- If \(m\) is odd and \(j_*(\pi)=(m+1)/2\) is the CENTRAL switch position (so \(n\) is EVEN), assign \(+r\) if \(p_{n/2}<p_{n/2+1}\) and \(-r\) otherwise, for any predetermined total order \(<\) on the coordinate direction names.

By (2), central direction-pair reversal, and the fact that all \(p_i\) are distinct,
\[
\boxed{\lambda_x(\operatorname{rev}\pi)=-\lambda_x(\pi).}
\tag{3}
\]

**Theorem (actual complementary median-seam Tucker pair).** For EVERY active NORI coloring and EVERY physical cube root \(x\) in every \(n\ge7\), there exist two **distinct actual FULL endpoint-opposed antipodal geodesics** \((x,\pi)\) and \((x,\sigma)\) with all three properties:

1. Their permutation vertices \(v_\pi,v_\sigma\) lie in a SINGLE COMMON PROPER permutohedral face. In particular the two path direction orders share one exact nonempty proper prefix-coordinate SUPPORT \(U\subsetneq[n]\).
2. Their signed median-switch labels are **exact complements**, \(\lambda_x(\pi)=-\lambda_x(\sigma)\).
3. Thus either their median switch positions are **mirror images**, \(j_*(\pi)+j_*(\sigma)=m+1=n-2\), located on opposite sides of the central position; or, when \(n\) is even, BOTH have the central median switch position \(j_*=(n-2)/2\) but their central ordered middle direction pairs \((p_{n/2},p_{n/2+1})\) have **opposite comparisons** in the fixed coordinate-name order.

**Proof.** Suppose no two vertices spanning an edge in the genuine-geodesic face nerve \(K_x\) have opposite signed labels. Map each vertex with label \(+k\) to \(+e_k\in\mathbb R^r\), and label \(-k\) to \(-e_k\), then extend affinely on every simplex. Since no simplex contains a pair of opposite labels (any such pair would span an edge), every simplex uses at most one sign of each coordinate vector. Hence its barycentric affine image avoids zero. Normalize the resulting continuous PL map to obtain an antipodally equivariant map
\[
K_x\longrightarrow S^{r-1}.
\tag{4}
\]
But \(r\le n-3\), so \(w_1(K_x/\tau)^r\ne0\) follows from (1), whereas a free equivariant map into \(S^{r-1}\) would make that power vanish by factoring through \(\mathbb RP^{r-1}\). This is a contradiction. Therefore some edge of \(K_x\) has labels \(+k,-k\).

By construction of \(K_x\), the two vertices of that edge represent ACTUAL rooted full cube geodesics whose direction permutations belong to one common proper permutohedral face. Any such proper face lies inside a facet corresponding to a nonempty proper prefix direction support \(U\), establishing (1). Complementary labels give exactly the two cases in (3): opposite signs with identical \(|k|\) imply reflected off-center median positions, or for the special central position, opposite comparisons of the two central direction names. \(\square\)

**Interpretation under hypothetical grand failure.** Every endpoint-opposed full path then has an ODD number of switches at least THREE, and the theorem forces two such bad paths with *mirror-compatible median defects* and a common exact prefix support. This is a fully legal **Tucker complementary-pair extraction inside a high-index carrier of genuine full NORI geodesics**, not just a neutral convex-average simplex. However, the *complementary labels* here describe median SWITCH POSITIONS, not complementary MONOCHROMATIC REACHABILITY SUPPORTS. Their two paths may have entirely different internal coordinate orders, and a common prefix *set* does not make their corresponding ordered windows coincide. Thus this theorem is not the desired full one-switch NORI closure. The next decisive physical lemma would transform this forced same-face complementary median-switch pair into either (i) a defect-reducing legal root/order exchange, or (ii) the same-root reversed-tail complementary reachability supports of the exact grand theorem. That extraction is still unproved.

**Topological significance.** Unlike applying Tucker to interpolated barycenters, this theorem's forced complementary edge belongs to a complex whose vertices are ONLY genuine endpoint-opposed FULL paths and whose simplices have exact original permutohedral face incidence. It gives a concrete combinatorial target—two mirror-related median walls sharing a prefix support—on which the needed root-coupled physical exchange argument can operate.

## Cubical bit-string neutrality on the genuine geodesic nerve

The same high-index argument establishes a bit-string version directly aligned with the desired fixed-point program.

**Corollary (true-path cubical Tucker neutrality).** Fix \(1\le k\le n-3\). For ANY assignment
\[
\Lambda:\mathcal B_x\to\{0,1\}^k
\quad\text{with}\quad
\Lambda(\operatorname{rev}\pi)=\mathbf 1-\Lambda(\pi),
\tag{5}
\]
there exists a **single proper permutohedral face** \(H\) and a finite family of ACTUAL endpoint-opposed full geodesic orders \(\pi_1,\ldots,\pi_s\in H\) such that, in EVERY bit coordinate \(j\in[k]\), their assigned labels include both 0 and 1.

**Proof.** Let \(V(\pi)=(2\Lambda_1(\pi)-1,\ldots,2\Lambda_k(\pi)-1)\in\{\pm1\}^k\), which is odd under full direction-order reversal. Suppose no simplex of \(K_x\) is **cubically neutral**, i.e. no simplex contains both signs in every coordinate. Affinely interpolate \(V\) over every simplex. In each simplex some fixed coordinate has ALL vertex signs equal, so that coordinate of the interpolated map is \(\pm1\) everywhere inside that simplex, and the interpolated map never vanishes. Normalizing gives an antipodally equivariant map \(K_x\to S^{k-1}\). Since \(k\le n-3\), this contradicts \(w_1(K_x/\tau)^{n-3}\ne0\). Thus a neutral simplex exists and, by definition of the genuine-path nerve, all of its actual permutation vertices lie in one common proper face. \(\square\)

**Conditional complementary-bitstring sharpening.** Suppose in addition that for every proper permutohedral face, the \(\Lambda\)-labels of all actual endpoint-opposed paths lying in that face are **totally ordered by coordinatewise inclusion** (equivalently their one-bit support sets form a nested chain). Then the above neutral simplex includes an ACTUAL label \((0,\ldots,0)\) and an ACTUAL label \((1,\ldots,1)\), i.e. a complete complementary bit-string pair among two actual paths in that common proper face: the minimal and maximal members of a nested neutral chain must be the all-zero and all-one vectors.

This extra **chain-compatibility hypothesis is NOT presently known for any natural monochromatic-reachability support labeling on \(K_x\)**. Moreover the roots in this construction are fixed, while prescribed-root grand closure is known false, so it cannot be silently interpreted as a full NORI proof. It is an exact description of what extra physical path-incidence property would elevate the theorem's unavoidable cubical NEUTRALITY to a genuine complementary pair. The current theorem is already more concrete than a cubical Tucker neutral simplex with virtual state vertices: every label here belongs to an ACTUAL full cube geodesic.
