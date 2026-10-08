# Seven-coordinate shared-pivot endpoint constraints

## Endpoint pivots for ordered-face galleries

Let \(k\ge2\), and let \(c(F,\pi)\in\{0,1\}\) color ordered \(k\)-faces of a Boolean cube, independently of the traversal corner. On a geodesic segment with distinct direction order \(p_1,\ldots,p_m\), let \(w_i\) be its \(i\)-th consecutive ordered-\(k\)-face color. Fix all starting bits except those specified below.

**Theorem (endpoint-pivot dichotomy).** If \(m=2k\), varying \(u=x_{p_{k+1}}\) and \(v=x_{p_k}\) independently produces
\[
(w_1,\ldots,w_{k+1})=(A(u),M_1,\ldots,M_{k-1},E(v)).
\]
If \(m=2k+1\), varying the single bit \(t=x_{p_{k+1}}\) produces
\[
(w_1,\ldots,w_{k+2})=(A(t),M_1,\ldots,M_k,E(t)).
\]
In both formulas the interior colors \(M_i\) are independent of the varied bits.

**Proof.** A window is insensitive to the starting bits of its free directions, because these bits do not identify its underlying ordered face. For \(m=2k\), the free sets of windows \(2,\ldots,k\) have intersection \(\{p_k,p_{k+1}\}\). The first window contains \(p_k\) but excludes \(p_{k+1}\), while the last contains \(p_{k+1}\) but excludes \(p_k\). Hence the two pivots can affect only the respective endpoint colors. For \(m=2k+1\), the intersection of the free sets of windows \(2,\ldots,k+1\) is the singleton \(\{p_{k+1}\}\), and neither endpoint window contains it. \(\square\)

**Corollary (exact one-change criterion).** Let \(M=(M_1,\ldots,M_s)\) be the invariant middle word, and put \(q=\sum_{i=1}^{s-1}[M_i\ne M_{i+1}]\). A pivot choice achieves at most one change precisely when
\[
q+[A\ne M_1]+[E\ne M_s]\le1.
\]
In the shared-pivot case \(m=2k+1\), if \(q=0\) and neither \(t\) works, then \(A(0)=A(1)=E(0)=E(1)=1-M_1\). If \(q=1\) and both endpoint functions toggle with \(t\), neither choice works precisely when
\[
A(0)\oplus E(0)\ne M_1\oplus M_k.
\]

**Proof.** The color changes partition into the \(q\) changes inside \(M\) and the two boundary comparisons. For \(q=0\), failure under both choices forces both boundaries to disagree in both cases. For \(q=1\), success demands simultaneous agreement at both boundaries. Two endpoint functions that each toggle give complementary endpoint pairs, so one is the required pair exactly when their common XOR equals the target XOR. \(\square\)

When \(k=3\), the two cases are the six-move independent endpoint square and the seven-move shared endpoint obstruction. The statements require no antipodal symmetry. In a seven-dimensional NORI counterexample, they constrain every five-move interior whose color word has at most one change; compatibility of those constraints across different orders remains unresolved.
