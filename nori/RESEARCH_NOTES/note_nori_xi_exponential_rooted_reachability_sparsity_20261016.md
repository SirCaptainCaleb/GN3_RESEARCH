# Exponentially sparse reachability and favorable roots in antipodally odd cubes

- Stable ID: note_nori_xi_exponential_rooted_reachability_sparsity_20261016
- Author: unspecified; session provenance retained
- Primary home: subsection:flat_graded_resource_automata_and_antipodal_reachability_certificates
- Labels: NORI1, reachability, balanced, product, dimension-uniform
- Lifecycle: active
- Epistemic status: proved
- Current version: 3
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10487_2
- Updated session: session_nori_r10487_2
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Let \(R_x(c)=\{S\subseteq[n]:\text{a color-zero geodesic from }x\text{ traverses precisely the dimensions in }S\}\). The antipodal Boolean reachability criterion states that NORI1 follows if some \(R_x\) contains complementary subsets. The sufficient cardinality condition \(|R_x|>2^{n-1}\) is far from necessary, uniformly in dimension.

**Theorem (exponential failure of rooted-majority reachability).** For every \(m\ge1\), there is an antipodally odd edge coloring \(c\) of \(Q_{4m}\) such that, for every root \(x\) and both colors \(a\), the family \(R_x(c;a)\) of \(a\)-monochromatically reachable dimension supports satisfies
\[
|R_x(c;a)|\le8^m=2^{3m}.
\]
Nevertheless this coloring admits monochromatic full antipodal geodesics. Thus the maximum possible proportion of reachable subsets is at most \(2^{-m}\), although the sufficient complement-pair threshold is greater than \(1/2\).

**Proof.** On \(Q_4\), with bits \(x_1,x_2,x_3,x_4\), define
\[
c_1(x)=1+x_4,\quad c_2(x)=1+x_3,\quad c_3(x)=x_4,\quad c_4(x)=x_3
\quad(\bmod 2).
\]
Every rule ignores its own bit and changes value under complementation of all four bits, so the coloring is legal. Let \(s=x_3\) and \(t=x_4\) at a root. A zero-colored step in dimensions \(1,2,3,4\), respectively, is permitted precisely when \(t=1,s=1,t=0,s=0\). Steps 3 and 4 toggle \(s\) and \(t\), respectively, and steps 1 and 2 leave them unchanged. Straight enumeration of dimension-simple zero-step words gives
\[
\begin{array}{c|l}
(s,t)&R_x(c;0)\\ \hline
(0,0)&\varnothing,3,4,23,14\\
(0,1)&\varnothing,1,4,14,34,134,234,1234\\
(1,0)&\varnothing,2,3,23,34,134,234,1234\\
(1,1)&\varnothing,1,2,12
\end{array}
\]
where a word such as \(134\) denotes the subset \(\{1,3,4\}\). In particular all roots have at most eight zero-reachable subsets; the same holds for color one by antipodal complementation, since \(R_x(c;1)=R_{\bar x}(c;0)\) as support families.

Now partition the \(4m\) dimensions into \(m\) blocks of four and put the displayed coloring independently on each block. It remains antipodally odd. An all-zero dimension-simple path interleaves all-zero paths in the individual blocks; conversely any collection of blockwise paths may be interleaved. Therefore
\[
R_x(c;0)=\prod_{j=1}^m R_{x^{(j)}}(c^{(j)};0),\qquad
|R_x(c;0)|\le8^m.
\]
The color-one bound follows likewise. For \((s,t)=(0,1)\), the direction order \((1,4,3,2)\) is entirely color zero. Choose such a root on every block and concatenate these block paths to obtain a color-zero full antipodal geodesic on \(Q_{4m}\). \(\square\)

The result eliminates any approach that attempts to force NORI1 solely by proving a universal rooted-reachability density above one half; compatibility of the reachable support families across roots is essential.

**Corollary (exponentially few favorable roots, even under vertex balance).** The construction is vertex-balanced: \(c_1=1+c_3\) and \(c_2=1+c_4\), so every vertex has two incident edges of each color in each four-dimensional block. Moreover a root supports a monochromatic full antipodal geodesic (of either color) if and only if \(s\ne t\) in every block. Indeed the reachability table shows that support \(1234\) is reachable by color zero precisely when \((s,t)\in\{(0,1),(1,0)\}\). Antipodal complementation gives the same criterion for color one. Projection of a monochromatic full product geodesic into each block is a monochromatic full geodesic there; conversely block geodesics concatenate. Thus precisely \(8^m\) of the \(16^m\) roots support a monochromatic full geodesic, a proportion \(2^{-m}\).

This also rules out a dimension-independent positive lower bound on the proportion of favorable roots, even in the perfectly vertex-balanced class.

**Sharper favorable-root density without vertex balance.** For any \(m\ge1\) on \(Q_{2m}\), use independent two-dimensional blocks with \(c_{2j-1}(x)=x_{2j}\) and \(c_{2j}(x)=x_{2j-1}\). These rules are antipodally odd. In each two-dimensional block, a root \((u,v)\) supports a monochromatic full geodesic of either color if and only if \(u\ne v\): when \(u=v\), either initial edge changes color after the first step, whereas when \(u\ne v\), choosing the initially color-zero edge first gives a zero full geodesic, and choosing the other first gives a one full geodesic. A full product geodesic projects to a full geodesic on each block, and compatible block geodesics concatenate. Hence precisely \(2^m\) of \(4^m\) roots support a monochromatic full geodesic: the proportion is \(2^{-m}=2^{-n/2}\). Moreover each rooted monochromatic support family on one block has at most three elements, giving \(|R_x(c;a)|\le3^m\) in the product.

The four-dimensional construction above retains vertex balance and gives a sharper bound on the proportion of reachable dimension subsets; the two-dimensional construction gives a sharper bound on favorable-root density.
