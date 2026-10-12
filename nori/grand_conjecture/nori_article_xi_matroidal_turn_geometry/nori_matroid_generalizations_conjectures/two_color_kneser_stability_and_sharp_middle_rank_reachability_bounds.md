# Two-color Kneser stability and sharp middle-rank reachability bounds

# Two-color Kneser stability and sharp middle-rank reachability bounds

## 1. Uniform two-color Kneser upper bound

Let \(n=2k+1\), \(k\ge2\), and let \(\mathcal F\subseteq\binom{[n]}k\) be a vertex family whose induced disjointness graph in the Kneser graph \(KG(n,k)\) is bipartite.

**Theorem 1 (two-color Kneser bound).** Every such family satisfies
\[
\boxed{
|\mathcal F|\le
\max\left\{
\binom{2k}{k-1}+\binom{2k-1}{k-1},
\quad
2\binom{2k}{k-1}-2(k-1)
\right\}.
}
\tag{1}
\]
In particular the upper bound is \(7\) when \(n=5\), and \(26\) when \(n=7\).

*Proof.* A proper bipartition writes \(\mathcal F=\mathcal A\sqcup\mathcal B\), where \(\mathcal A\) and \(\mathcal B\) are disjoint intersecting families of \(k\)-subsets.

If \(\mathcal A\) has a common coordinate \(i\), it lies in the full star \(\mathcal S_i=\{S:i\in S\}\). Of the members of \(\mathcal B\), those also containing \(i\) lie in this star; those avoiding \(i\) form an intersecting family of \(k\)-subsets on \(2k\) points. Erdős–Ko–Rado bounds the latter by \(\binom{2k-1}{k-1}\). Thus
\[
|\mathcal F|\le|\mathcal S_i|+
|\{B\in\mathcal B:i\notin B\}|
\le\binom{2k}{k-1}+\binom{2k-1}{k-1}.
\]
The same argument applies with the classes reversed.

If neither color class has a common coordinate, the Hilton–Milner theorem bounds each by
\[
\binom{2k}{k-1}-\binom{k}{k-1}+1
=\binom{2k}{k-1}-k+1.
\]
Adding the two bounds proves (1). For empty classes, applying Erdős–Ko–Rado or Hilton–Milner to the nonempty class is no weaker. \(\square\)

**Corollary 2 (NORI1 middle-layer obstruction).** Let \(c\) be an antipodally odd undirected cube-edge coloring, and let \(R_x^\varepsilon\) be the coordinate subsets reachable from root \(x\) by a monochromatic geodesic of color \(\varepsilon\). If the coloring has no full monochromatic antipodal geodesic, then for every root \(x\),
\[
\mathcal F_x=(R_x^0\cup R_x^1)\cap\binom{[n]}k
\]
obeys (1). In particular \(|\mathcal F_x|\le7\) for \(Q_5\), and \(|\mathcal F_x|\le26\) for \(Q_7\).

*Proof.* Article VII's color-free reachability odd-cycle theorem shows that, absent a full monochromatic antipodal geodesic, the induced Kneser disjointness graph on \(\mathcal F_x\) must be bipartite: an edge joins two disjoint \(k\)-sets covering all but one coordinate, and two same-colored monochromatic arms at such endpoints would produce a monochromatic near-full geodesic, which extends to a full one by antipodal oddness. Every support incident to a disjointness edge then has a uniquely forced witness color, giving a proper bipartition. Apply Theorem 1. \(\square\)

The bound is necessary for a counterexample, not sufficient for a witness: a single rooted family may attain equality without any monochromatic geodesic of length \(n-1\) from that root.

## 2. Sharpness and rigidity for dimensions five and seven

For \(n=5\), the union of the full stars of two distinct coordinates among two-element subsets has seven distinct members. Its disjointness graph is bipartite, assigning each support to one of the two stars, so the bound seven is sharp for the abstract Kneser problem.

For \(n=7\), partition the seven labels into a three-element set \(T\) and four-element set \(Q\), and fix \(q\in Q\). Put
\[
\begin{aligned}
\mathcal A&=\{S\in\tbinom{[7]}3:|S\cap T|\ge2\},\\
\mathcal B&=\{S\in\tbinom{[7]}3:q\in S,\ 
S\cap(Q\setminus\{q\})\ne\varnothing\}\cup\{Q\setminus\{q\}\}.
\end{aligned}
\tag{2}
\]
These are disjoint intersecting families, each of cardinality thirteen. Therefore their union realizes the upper bound twenty-six.

**Theorem 3 (classification of sharp seven-point Kneser families).** Every induced-bipartite family \(\mathcal F\subseteq\binom{[7]}3\) of size twenty-six admits a bipartition into two disjoint thirteen-element nontrivial intersecting families. Up to relabeling, there are precisely two possibilities:
\[
\begin{array}{ll}
\text{(I)}&J(T)\sqcup J(U),\quad T\cap U=\varnothing;\\
\text{(II)}&H(c;T)\sqcup J([7]\setminus(T\cup\{c\})),
\end{array}
\tag{3}
\]
where
\[
J(T)=\{S\in\tbinom{[7]}3:|S\cap T|\ge2\},\qquad
H(c;T)=\{T\}\cup\{\{c,a,b\}:\{a,b\}\cap T\ne\varnothing\},
\]
with \(|T|=3\) and \(c\notin T\). There are seventy labeled unordered pairs of type (I) and one hundred forty of type (II), for a total of
\[
\boxed{210\text{ labeled extremal pairs, in two permutation orbits}.}
\tag{4}
\]

*Proof.* The common-coordinate case in Theorem 1 gives at most \(15+10=25\), so a twenty-six-member family must have two nontrivial intersecting color classes. Hilton–Milner bounds each by thirteen, hence each attains equality.

The equality classification for nontrivial intersecting triple families on seven labels has two forms: the triangle-majority family \(J(T)\), or the canonical Hilton–Milner family \(H(c;T)\). Both have thirteen members, and there are respectively \(\binom73=35\) and \(7\binom63=140\) labeled families.

Two majority families \(J(T),J(U)\) are disjoint precisely when the indexing triples \(T,U\) are disjoint. Indeed, if \(T\cap U\ne\varnothing\), choose two points of \(T\) and two of \(U\), using their shared point so that the resulting three-element set has at least two in each. Conversely, no three-set can contain two elements from each of disjoint three-sets. Thus the number of unordered disjoint majority pairs is \(\binom73\binom43/2=70\).

A canonical family \(H(c;T)\) is disjoint from a majority family \(J(U)\) precisely when \(U=[7]\setminus(T\cup\{c\})\). If \(U\) avoids the four-point set \(T\cup\{c\}\), members of \(H(c;T)\) contain at most one point of \(U\). Conversely, if \(U\) contains two points of \(T\), it lies with a suitable third point in \(J(U)\cap H(c;T)\); if \(U\) contains \(c\) and any point of \(T\), choose a triple containing both and a further point of \(U\); the remaining configurations likewise supply a triple of \(H(c;T)\) with two members of \(U\). Hence there is one disjoint majority family for each of the \(140\) canonical families.

Two canonical families cannot be disjoint. If their centers coincide, a triple containing the center and meeting both exceptional triples belongs to both. If their centers \(c,d\) differ, a triple \(\{c,d,a\}\) belongs to both provided \(\{d,a\}\) meets the first exceptional triple and \(\{c,a\}\) meets the second. Such \(a\) exists unless both exceptional triples are disjoint and exclude both centers, which is impossible for distinct \(c,d\) on seven labels. This proves the two types and their counts. \(\square\)

The sharp configuration classification describes a **single root's** Kneser layer only. It does not imply the global existence of a counterexample to NORI1.
