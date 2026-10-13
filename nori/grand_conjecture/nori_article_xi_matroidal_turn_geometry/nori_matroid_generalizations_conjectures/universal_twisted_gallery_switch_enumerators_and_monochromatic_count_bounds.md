# Universal twisted-gallery switch enumerators and monochromatic count bounds

# Universal twisted-gallery switch enumeration and degree mixing

Let \(n\ge2\) and let \(c:E(Q_n)\to\mathbb F_2\) be any undirected edge coloring satisfying \(c(\bar e)=1-c(e)\). For the \(T=2^n n!\) rooted directed full geodesics \((x,\pi)\), let \(S_j\) count those with \(j\) changes in their length-\(n\) edge-color word. There is no affine or other regularity assumption.

**Theorem 1 (switch spectrum under rooted rotations).** For \(2r+1\le n\),
\[
\boxed{(2r+1)S_{2r+1}=(n-2r-1)S_{2r}.}\tag{1}
\]
In particular
\[
\boxed{S_1=(n-1)S_0.}\tag{2}
\]
More strongly, there are integers \(A_{2r+1}\ge0\) such that
\[
\boxed{S_{2r}=2(2r+1)A_{2r+1},\quad
S_{2r+1}=2(n-2r-1)A_{2r+1}.}\tag{3}
\]

**Proof.** If a path \(P=(x;i_1,\dots,i_n)\) has color word \(w=(w_1,\dots,w_n)\), its rooted cyclic rotation
\[
R(P)=(x^{i_1};i_2,\dots,i_n,i_1)
\]
has color word
\[
\boxed{w(R(P))=(w_2,\dots,w_n,1-w_1).}\tag{4}
\]
The last new edge is antipodal to the original first edge. The action \(R\) has orbit size \(2n\): before \(n\) steps the coordinate permutation has not returned, and after \(n\) steps the root becomes its antipode. The associated length-\(2n\) circular word is \(w_1,\dots,w_n,1-w_1,\dots,1-w_n\). Define its half-circle change count
\[
k(P)=\sum_{i=1}^{n-1}[w_i\ne w_{i+1}]+[w_n\ne1-w_1].
\]
It is odd, because its transitions change the initial bit to its complement. It is invariant under \(R\). In an orbit with \(k=2r+1\), every rooted linear word omits one of the \(n\) comparisons of a twisted half-circle. If the omitted comparison is a change, the linear word has \(k-1=2r\) changes; otherwise it has \(k=2r+1\). Over all \(2n\) rotations, \(2k\) omit a change and \(2(n-k)\) omit an equality. Thus each orbit contributes \(2(2r+1)\) paths of type \(2r\) and \(2(n-2r-1)\) paths of type \(2r+1\). Summation gives (1)--(3). \(\square\)

**Theorem 2 (local color mixing determines the first cyclic moment).** Put \(a(v)=\deg_{c=0}(v)\), the number of zero-color edges incident with vertex \(v\). For uniformly random rooted full geodesic \(P\),
\[
\boxed{\mathbb E k(P)=\frac{2}{2^n(n-1)}
\sum_{v\in Q_n}a(v)(n-a(v)).}\tag{5}
\]

**Proof.** Each of the \(n-1\) internal transitions of the full geodesic is an ordered pair of distinct directions at a uniformly random cube vertex. The closing comparison is between the final edge and the antipodal image of the initial edge at the terminal vertex; its vertex and ordered direction pair have the same uniform law. At a vertex \(v\), the proportion of mixed-color ordered edge pairs is
\[
\frac{2a(v)(n-a(v))}{n(n-1)}.
\]
Summing the \(n\) cyclic comparisons and averaging proves (5). \(\square\)

**Corollary 3 (quantitative existence criterion).** For every antipodally odd coloring,
\[
\boxed{S_0\ge2^{n-1}(n-1)!\,
\max\left\{0,\ 3-\frac{2}{2^n(n-1)}
\sum_v a(v)(n-a(v))\right\}.}\tag{6}
\]
In particular, if the mean of \(a(v)(n-a(v))\) over cube vertices is less than \(3(n-1)/2\), a monochromatic antipodal geodesic exists.

**Proof.** Let \(p\) be the fraction of rotation orbits with \(k=1\). All other odd switch counts are at least three, hence \(\mathbb E k\ge p+3(1-p)\) and \(p\ge(3-\mathbb E k)/2\). Each orbit has \(2n\) rooted paths; a \(k=1\) orbit has two monochromatic paths, and no other orbit has any. Thus \(S_0=(T/n)p=2^n(n-1)!p\). Substitute (5). \(\square\)

**Corollary 4 (sharp low-dimensional witness multiplicities).** Every antipodally odd coloring has
\[
\boxed{S_0(Q_3)\ge8,\qquad S_0(Q_4)\ge16.}\tag{7}
\]
Both bounds are attained. In \(Q_4\), equality holds if and only if each vertex has two edges of each color.

**Proof.** For \(n=3\), integer \(a\) satisfies \(a(3-a)\le2\), so \(\mathbb E k\le2\); (6) gives \(S_0\ge8\). The coloring
\[
c_1=x_2,\quad c_2=x_1,\quad c_3=1+x_1
\]
is antipodally odd, and both colors occur at every vertex, making \(\mathbb E k=2\). Since the twisted count \(k\in\{1,3\}\), the proof of (6) gives \(S_0=8\).

For \(n=4\), \(a(4-a)\le4\) gives \(\mathbb E k\le8/3\), and (6) yields \(S_0\ge16\). The coloring
\[
c_1=x_2,\quad c_2=x_1,\quad c_3=1+x_2,\quad c_4=1+x_1
\]
is antipodally odd and has two colors of each type in every vertex star. Its cyclic counts likewise belong to \(\{1,3\}\), so it attains \(S_0=16\). Conversely, equality \(S_0=16\) forces the mean in (5) to be \(8/3\); hence every vertex maximizes \(a(4-a)\), meaning \(a(v)=2\) for all \(v\). \(\square\)

**Corollary 5 (rigidity of a putative \(Q_5\) counterexample).** If an antipodally odd coloring of \(Q_5\) had no monochromatic antipodal geodesic, then every vertex would have two or three edges of color zero, and **every** rooted full geodesic would have cyclic switch number \(k=3\). Its ordinary switch word would always have two or three changes, with \(3S_3=2S_2\).

**Proof.** Since \(a(5-a)\le6\), (5) gives \(\mathbb E k\le3\). If \(S_0=0\), Theorem 1 excludes any \(k=1\) rotation orbit, so \(k\ge3\) everywhere. Equality of the upper and lower means forces \(a(v)\in\{2,3\}\) at every vertex and \(k=3\) throughout. Equation (1) for \(r=1\) completes the statement. \(\square\)

**Scope.** These theorems hold for *every* legal antipodally odd cube-edge coloring, unlike affine-subclass results. The odd-switch rotation is established elsewhere in Article XI; Theorem 1 upgrades it to full integer-valued switch-spectrum relations, and Theorem 2 connects those counts to a simple vertex-degree observable. The sharp multiplicity bound settles dimensions 3 and 4 by a new count and yields explicit sufficient conditions in all dimensions. For large \(n\), the first-moment threshold is not sufficient near balanced vertex stars: one would need further moments or square-turn correlations to force \(k=1\). No unrestricted NORI1 proof follows from the displayed bounds alone.

## Theorem 6 (rank-one antipodal completion and facet enumeration)

Let \(M_{n-1}(c)\) denote the number of **directed** monochromatic geodesics of length \(n-1\) in \(Q_n\), counted with their initial vertices and their ordered sets of \(n-1\) distinct coordinate directions. Then
\[
\boxed{M_{n-1}(c)=2S_0(c),\qquad
S_1(c)=\frac{n-1}{2}M_{n-1}(c).}
\tag{10}
\]
Moreover, writing \(F_{j,0}=\{x\in Q_n:x_j=0\}\), and letting \(B(F_{j,0})\) count all monochromatic directed full geodesics within the \((n-1)\)-dimensional face \(F_{j,0}\) under the inherited coloring, one has
\[
\boxed{S_0(c)=\sum_{j=1}^n B(F_{j,0}).}
\tag{11}
\]

**Proof.** Let \(P\) be a monochromatic geodesic of length \(n-1\), from \(x\) to \(y\), missing direction \(j\). Then \(y=\bar x^{j}\). The \(j\)-edge at the start, \(xx^{j}\), and the \(j\)-edge at the end, \(yy^{j}\), are antipodal images of each other. By the oddness condition, their colors are opposite. Precisely one of them agrees with the common color of \(P\), allowing one and only one monochromatic full-geodesic extension by adding direction \(j\) at the appropriate end. Conversely, deleting the first or the last edge of any monochromatic full geodesic produces two different directed \((n-1)\)-edge monochromatic geodesics, each of which is uniquely extended back to the original full geodesic. This is a two-to-one correspondence, proving the first identity in (10). The second identity follows from (2).

Every \((n-1)\)-edge cube geodesic lies in precisely one coordinate facet, determined by its omitted direction \(j\) and the fixed \(j\)-bit of its vertices. The cube antipode maps the facet \(F_{j,0}\) bijectively to its opposite facet \(F_{j,1}\), reversing all edge colors; hence their monochromatic spanning-geodesic counts coincide. Therefore
\[
M_{n-1}(c)=\sum_{j=1}^n \bigl(B(F_{j,0})+B(F_{j,1})\bigr)
=2\sum_{j=1}^n B(F_{j,0}).
\]
Combine with \(M_{n-1}(c)=2S_0(c)\) to obtain (11). \(\square\)

This count identity makes precise the distinction between **partial witness growth** and **rank saturation**. An \((n-1)\)-resource monochromatic path extends automatically, thanks to the antipodal pair of final resource ports. However, a path of only \(\sqrt n\), \(n/2\), or \(n-2\) independent resources need not have such an antipodal pair at its endpoints. An unrestricted proof via the common matroid terminal theorem must therefore either grow witnesses up to rank \(n-1\) or find an analogue of the complementary-endport completion mechanism at larger resource defect. The reversal-odd boundary tournament does not automatically possess this two-end extension rule, so the possible unification must encode different seam arities without discarding the resource constraints.

## Theorem 7 (second-moment certificate for arbitrary antipodally odd colorings)

Let \(n\ge3\), let \(K\) be the largest odd integer at most \(n\), and regard \(k(P)\in\{1,3,\ldots,K\}\) as a random variable over uniformly chosen rooted full geodesics. Put \(m_1=\mathbb E k\), \(m_2=\mathbb E k^2\). Then
\[
\boxed{
S_0\ge
2^{n-1}(n-1)!\,
\max\left\{0,\frac{m_2-(K+3)m_1+3K}{K-1}\right\}.}
\tag{12}
\]
This is a second-moment certificate independent of any affine or regularity condition.

**Proof.** The polynomial \(g(k)=(k-3)(K-k)\) vanishes at \(k=3,K\), is nonnegative at every admissible odd \(k\ge3\), and has \(g(1)=-2(K-1)\). If \(p\) is the fraction of rotation orbits with \(k=1\), it follows that
\[
\mathbb E g(k)\ge -2(K-1)p.
\]
But \(-\mathbb E g(k)=m_2-(K+3)m_1+3K\). As proved in Corollary 3, \(S_0=2^n(n-1)!p\). The inequality follows. \(\square\)

**Corollary 8 (a variance characterization of the balanced \(Q_5\) case).** Suppose \(n=5\) and every vertex star has zero-color degree two or three. Then \(m_1=3\), and
\[
\boxed{S_0(c)=96\,\operatorname{Var}(k).}
\tag{13}
\]
Consequently in this balanced-star regime, a monochromatic antipodal geodesic exists if and only if the cyclic switch number is not constant over the rooted full geodesics.

**Proof.** By (5), balanced stars give \(m_1=3\). The cyclic switch count can be \(1,3,5\). Its probabilities at 1 and 5 are equal because their contributions to \(m_1-3\) are opposite. If that common probability is \(p\), then \(\operatorname{Var}(k)=4p+4p=8p\), while \(S_0=2^5\cdot4!p=768p\). Therefore \(S_0=96\operatorname{Var}(k)\). \(\square\)

This suggests a possible unrestricted strategy beyond average-degree bounds: estimate cyclic-switch variance (or suitable higher positive polynomial moments) from square-turn correlations and rooted gallery exchanges. The first moment depends only on the vertex color degrees; the second moment detects correlations across turns and may remain informative when all vertex stars are perfectly balanced. Formula (13) is a sharp manifestation in dimension five. It is not, by itself, a proof that such variance must be positive in every balanced coloring.
