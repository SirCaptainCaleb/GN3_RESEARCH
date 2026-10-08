# Every vertex admits four-edge monochromatic paths from all but four incoming directions; most roots are good

# Codimension-four universal incoming reachability and density of monochromatic four-edge roots

Let c be ANY binary coloring of physical ordered three-faces in Q_n, n>=5, without requiring antipodal oddness. For r∈Q_n define
\[
I(r)=\{i\in[n]:\text{there exists a monochromatic four-edge geodesic }
(r\oplus e_i)\to r\to\cdots\},
\]
where its first step uses direction i and its next three steps are along distinct other coordinates. Let
\[
X=\{x\in Q_n:\text{some monochromatic four-edge geodesic starts at }x\}.
\]

**Theorem (at most four prohibited incoming directions per vertex).** For every vertex r,
\[
\boxed{|I(r)|\ge n-4.}
\]
Consequently,
\[
\boxed{|X|\ge 2^n\left(1-\frac4n\right).}
\]
More quantitatively, at least \((n-4)2^n\) directed cube edges \(x\to r\) can serve as the FIRST edge of some monochromatic four-edge geodesic.

**Proof.** If [n]\I(r) contained five distinct directions, take them as a cyclic 5-tuple. The universal odd-cyclic monochromatic seed theorem gives a four-edge monochromatic geodesic whose first edge arrives at r along one of those five directions. This would put that direction into I(r), contradiction. Hence at most four directions are excluded.

There are 2^n vertices r and at least n-4 good incoming directed edges into each, totaling at least (n-4)2^n such edges. Let B=Q_n\X be roots having NO monochromatic four-edge path. Every one of their n outgoing directed edges must be bad (cannot extend to a monochromatic length-four path), and these bad directed edges have distinct tails, so n|B| is at most the total number of bad directed edges, which is at most 4·2^n. Thus |B|≤4·2^n/n and the asserted root-density bound follows. QED.

**Antipodal-pair corollary.** For n>=9, |X|>2^{n-1}. Since the cube's antipodal involution partitions its 2^n vertices into 2^{n-1} pairs, at least one such pair is fully contained in X. More quantitatively the number of antipodal root pairs with BOTH roots in X is at least \(|X|-2^{n-1}\ge 2^{n-1}(1-8/n)\).

**Uniform k-face generalization.** Let k>=1 and m be the least odd integer >=k+1. For arbitrary binary ordered-k-face coloring of Q_n with n>=m, define I_k(r) as incoming directions of a monochromatic (k+1)-edge geodesic whose first step arrives at r. The same odd-cycle proof yields
\[
|I_k(r)|\ge n-m+1,\qquad
|X_{k+1}|\ge 2^n\left(1-\frac{m-1}{n}\right).
\]
The active k=3 case has m=5.

**Research link.** This imposes a strong necessary local reachability coverage on any hypothetical counterexample to full NORI: almost all roots (proportion at least 1-4/n) possess nontrivial monochromatic terminal-two-tail reachability labels of support rank 2. The next closure obligation is to use antipodal symmetry, root mobility, and the exact REVERSED-TWO-TAIL complementary-support equivalence to turn this abundant low-rank reachability into a complementary high-rank collision. The density bound by itself does not supply that collision.
