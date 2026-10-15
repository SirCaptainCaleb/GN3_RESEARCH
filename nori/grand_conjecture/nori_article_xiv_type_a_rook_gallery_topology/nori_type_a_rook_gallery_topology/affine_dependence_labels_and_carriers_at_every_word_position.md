# Affine dependence labels and carriers at every word position

# Affine dependence labels and carriers at every word position

A binary word has at most one switch precisely when its signs can be separated by an affine function of position. The complementary case has an explicit positive affine dependence. This supplies a color-sensitive replacement for the signed-second-switch label, with a contractible carrier at every fixed word position.

Let \(s=(s_1,\ldots,s_m)\in\{-1,1\}^m\), \(m\ge3\), and put
\[
L_m=\{z\in\mathbb R^m:\ \sum_i z_i=0,\ \sum_i i z_i=0\}.
\tag{1}
\]
For \(i<j<k\) with \(s_i=s_k=-s_j\), define
\[
r_{ijk}(s)=s_i\bigl((k-j)e_i-(k-i)e_j+(j-i)e_k\bigr),
\]
and set
\[
\boxed{z(s)=\sum_{\substack{i<j<k\\s_i=s_k=-s_j}}r_{ijk}(s).}
\tag{2}
\]

**Theorem 1 (positive affine dependence).** The following are equivalent:

(i) \(s\) has at least two switches.

(ii) There is \(z\in L_m\) such that \(s_i z_i>0\) for every \(i\).

When these conditions hold, (2) is such a vector. Moreover
\[
\boxed{z(-s)=-z(s),\qquad
z(\operatorname{rev}s)=\operatorname{rev}z(s).}
\tag{3}
\]

*Proof.* Each summand in (2) has both sums in (1) equal to zero. Its nonzero entries have the signs of \(s\). If the word has at least three runs, each position belongs to an alternating triple: for a position in an interior run, choose one position in each adjacent run; for a position in the first or last run, choose positions in the next or previous two runs. Thus each entry of (2) receives a contribution with its required sign, and none with the opposite sign. This proves (i) implies (ii).

If the word has at most one switch, an affine function \(f(t)\) has sign \(s_i\) at every integer position \(i\): choose its zero strictly between the two runs, or take a constant function for a constant word. If (ii) held, then
\[
0=\sum_i f(i)z_i>0,
\]
where the equality follows from (1). This proves the converse. Negation gives the first identity in (3). Reversal bijects the triples and exchanges their first and last coefficients, proving the second. \(\square\)

The labels
\[
\ell(s)=z(s)/\|z(s)\|\in S(L_m)\cong S^{m-3}
\tag{4}
\]
therefore retain a nonzero signed entry at every position. The sphere is fixed independently of the source flags.

**Theorem 2 (carriers for partial sign constraints).** Let \(\mathcal S\) be a nonempty family of words, each with at least two switches. Suppose a nonempty set \(A\subseteq[m]\) of positions has fixed signs \(\sigma_i\) throughout \(\mathcal S\). Then
\[
\boxed{C(A,\sigma)=
S(L_m)\cap\{z:\sigma_i z_i\ge0\text{ for all }i\in A\}}
\tag{5}
\]
is nonempty and contractible, and contains all labels (4) of the family. Adding fixed sign constraints shrinks the carrier. Complementing all signs negates it.

*Proof.* Choose any \(s\in\mathcal S\) and put \(v=\ell(s)\). Every constrained entry of \(v\) has strict prescribed sign. Hence \(-v\) does not belong to (5). For \(q\in C(A,\sigma)\), normalized linear interpolation
\[
(q,t)\longmapsto
\frac{(1-t)q+tv}{\|(1-t)q+tv\|}
\]
never vanishes: vanishing would require \(q=-v\). The interpolation remains in the convex sign cone before normalization, giving a contraction. The remaining assertions follow from the defining inequalities. \(\square\)

## Application to full cube geodesics

Let \(n\ge4\), let \(c(\bar e)=1-c(e)\), and provisionally suppose no monochromatic full antipodal geodesic exists. Every full rooted geodesic has at least two switches: a one-switch edge word becomes monochromatic after sliding its root across the change. Let \(X\cong S^{n-1}\) be the dual type-B Coxeter cellulation. Its vertices are the full rooted geodesics \(g=(x,\pi)\), and central antipodality sends \(g\) to \(\bar g=(\bar x,\pi)\).

For each vertex put
\[
\ell(g)=\ell\bigl((-1)^{w_1(g)},\ldots,(-1)^{w_n(g)}\bigr)
\in S(L_n).
\tag{6}
\]
This label is odd by (3). Let \(X_{\mathrm{pos}}\) be the union of closed dual cells on which at least one edge-color position is constant over all chamber vertices.

**Theorem 3 (extension using every constant position).** \(X_{\mathrm{pos}}\) is an antipodally invariant subcomplex containing the full dual one-skeleton. The labels (6) extend to an odd continuous map
\[
\boxed{F_{\mathrm{pos}}:X_{\mathrm{pos}}\to S^{n-3}}
\tag{7}
\]
using nested contractible carriers.

*Proof.* Constancy is inherited by cell faces, and antipodality complements each fixed sign. For a cell \(D\), use (5) with all its constant positions. Theorem 2 gives nonempty contractible carriers, nested under cell inclusion and negated by antipodality.

Every dual edge has a constant position. Flipping the initial-root bit in the first traversed dimension leaves the first undirected edge unchanged. Swapping adjacent dimensions beyond the first two leaves the first edge unchanged. Swapping the first two dimensions leaves the common suffix from position three onward unchanged. Thus every edge belongs to \(X_{\mathrm{pos}}\).

The prescribed vertex labels lie in their carriers. Extend over cell boundaries inductively inside these carriers, choosing one cell of each free antipodal pair and defining its partner by negation. Nestedness gives compatibility. \(\square\)

The previous signed-second-switch construction supplied position carriers for positions \(1,3,\ldots,n\). Formula (2) supplies them for **all** positions, including position two.

**Corollary 4 (complete positional variation in an obstruction cell).** There is an odd extension over
\[
X_{\mathrm{pos}}\cup X^{(n-3)}.
\]
For every such extension, its mod-two degree obstruction on the \((n-2)\)-cells represents
\[
\boxed{u^{n-2}\ne0\in H^{n-2}(\mathbb RP^{n-1};\mathbb F_2).}
\tag{8}
\]
Consequently some unfilled \((n-2)\)-cell has both colors represented at **every one of the \(n\) word positions**.

*Proof.* The sphere \(S^{n-3}\) is \((n-4)\)-connected, so the map extends equivariantly over the remaining cells through dimension \(n-3\). It is a section of the sphere bundle of \((n-2)\gamma\) on the antipodal quotient, where \(\gamma\) is the covering line bundle. The primary degree obstruction reduces modulo two to
\[
w_{n-2}((n-2)\gamma)=u^{n-2}.
\]
This class is nonzero in \(\mathbb RP^{n-1}\). Every position-constant cell has already been filled, so a degree-contributing cell has no constant position. \(\square\)

## Higher switch thresholds

The dependence criterion extends to every number of switches. For \(1\le r<m\), define
\[
L_{m,r}=\{z:\sum_i i^q z_i=0,\ 0\le q<r\}.
\]
A sign word has at least \(r\) switches if and only if \(L_{m,r}\) contains a vector with strict sign \(s_i\) in every entry. Indeed, \(r+1\) alternating positions support a signed Vandermonde dependence: on positions \(i_0<\cdots<i_r\), its aligned entries are
\[
\frac{s_{i_j}}{\prod_{\ell\ne j}|i_j-i_\ell|}.
\]
The moment identities follow by comparing the degree-\(r\) coefficients in Lagrange interpolation of polynomials of degree below \(r\). Summing these aligned dependences over all alternating \((r+1)\)-subsequences gives strict prescribed signs everywhere; every position lies in such a subsequence because the word has at least \(r+1\) runs. Conversely, a word with fewer than \(r\) switches is separated by a polynomial of degree below \(r\), contradicting the moment identities. The fixed-position carrier proof then applies in \(S(L_{m,r})\cong S^{m-r-1}\).

The unrestricted NORI1 application uses \(r=2\). The remaining task is to control cells with simultaneous variation at every position. The construction supplies a global color-sensitive labeling and stronger valid fillings; it does not yet annihilate the nonzero obstruction (8).
