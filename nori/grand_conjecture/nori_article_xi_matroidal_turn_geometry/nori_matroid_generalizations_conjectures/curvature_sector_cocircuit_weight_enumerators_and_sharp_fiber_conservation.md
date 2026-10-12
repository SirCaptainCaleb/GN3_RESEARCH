# Curvature-sector cocircuit weight enumerators and sharp fiber conservation

Let \(n\ge3\), let \(H_n=L(Q_n/\tau)\) be the folded-cube turn graph, and let \(d\) be the turn cochain of an arbitrary antipodally odd cube-edge coloring. Write \(D=|\operatorname{supp}(d)|\) and \(E=|E(H_n)|=2^{n-1}\binom n2\).

Let \(\mathcal A_n\) denote the simple odd-monodromy cycles of length \(n\) (antipodal-geodesic cycles), and let \(\mathcal B_n\) denote the simple odd-monodromy cycles of length \(n+1\). Article XI's stationary-contact and two-port exchange theorems give a canonical parent map
\[
\pi:\mathcal B_n\longrightarrow\mathcal A_n
\]
whose fibers have size \(n(n-2)\). It identifies the two families with two equal-cardinality cocircuit sectors of the canonical bipointed binary matroid: both-port cocircuits versus monodromy-only cocircuits. Write \(w_d(C)\) for integer turn cost.

For \(C\in\mathcal A_n\), and for each turn \(e\in C\) of zero disagreement, let \(r_e(C)\) count the unused vertices in its local \(K_n\) star clique whose lifted edge color is opposite to the common color of the two endpoint states of \(e\). Put
\[
R_d(C)=\sum_{\substack{e\in C\\d(e)=0}}r_e(C).
\tag{1}
\]

**Theorem 1 (fiber weight enumerator).** The \(n(n-2)\) children of every \(C\in\mathcal A_n\) have integer turn weights
\[
\boxed{
w_d(C)\ \text{for }n(n-2)-R_d(C)\text{ children},\qquad
w_d(C)+2\ \text{for }R_d(C)\text{ children}.}
\tag{2}
\]
In particular, if
\[
A_d(z)=\sum_{C\in\mathcal A_n}z^{w_d(C)},\quad
B_d(z)=\sum_{C'\in\mathcal B_n}z^{w_d(C')},\quad
R_d(z)=\sum_{C\in\mathcal A_n}R_d(C)z^{w_d(C)},
\]
then the weight-distribution polynomials obey
\[
\boxed{B_d(z)=n(n-2)A_d(z)+(z^2-1)R_d(z).}
\tag{3}
\]

*Proof.* Each child of \(C\) inserts one unused local edge-state at one of its \(n\) cyclic turns, with \(n-2\) possibilities at each turn. For a changed turn, the endpoint colors differ, and either color of the inserted edge-state leaves precisely one changed turn. For an unchanged turn, the endpoint colors agree, and inserting the same color leaves zero changes while inserting the opposite color contributes two. Formula (1) counts precisely the latter choices. The stationary-contact contraction theorem makes the parent unique, so each child is counted once. Summing over parents gives (3). \(\square\)

**Theorem 2 (global fiber conservation).** The number of opposite-sector children that have cost two greater than their parents satisfies
\[
\boxed{
\sum_{C\in\mathcal A_n}R_d(C)
=\frac{(n-2)!(n-2)}2\,D.
}
\tag{4}
\]
Consequently, for a uniformly sampled \(C'\in\mathcal B_n\),
\[
\boxed{
\Pr\bigl[w_d(C')=w_d(\pi(C'))\bigr]
=1-\frac{D}{2E}.
}
\tag{5}
\]
Furthermore,
\[
\boxed{
\Pr\bigl[w_d(C')=w_d(\pi(C'))\bigr]
\ge 1-\frac{\lfloor n^2/4\rfloor}{n(n-1)}.
}
\tag{6}
\]
The lower bound in (6) is attained by antipodally odd edge colorings for every \(n\ge3\).

*Proof.* The automorphism group of the cube acts transitively on the turn edges of \(H_n\). There are
\[
|\mathcal A_n|=2^{n-2}(n-1)!
\]
geodesic cycles, each having \(n\) turns. Since \(|E(H_n)|=n(n-1)2^{n-2}\), every turn edge belongs to
\[
\frac{n|\mathcal A_n|}{|E(H_n)|}=(n-2)!
\tag{7}
\]
geodesic cycles.

At a quotient cube vertex \(v\), the \(n\) incident edge-state colors split into classes of sizes \(k_v,n-k_v\). The number of triples consisting of an **unchanged** pair of star states and a third state of the opposite color is
\[
\binom{k_v}{2}(n-k_v)+\binom{n-k_v}{2}k_v
=\frac{n-2}{2}k_v(n-k_v).
\tag{8}
\]
Every such pair is a turn edge and occurs in \((n-2)!\) geodesic cycles by (7). Summing (8) over all quotient vertices gives (4), since
\[
D=\sum_vk_v(n-k_v)
\tag{9}
\]
counts the changed turn edges. Because
\[
|\mathcal B_n|=n(n-2)|\mathcal A_n|,
\]
dividing (4) by this number yields the bad-child fraction \(D/(2E)\), proving (5). Finally
\[
k_v(n-k_v)\le\lfloor n^2/4\rfloor
\]
at every quotient vertex, and \(H_n\) has \(2^{n-1}\) local star cliques; substitute in (5) to obtain (6).

To prove sharpness in every dimension, label the coordinate directions \(1,\ldots,n\), and pair \((1,2),(3,4),\ldots\). For the first pair assign edge colors \(c_1(x)=x_3\) and \(c_2(x)=1-x_3\). For each subsequent complete pair \((i,i+1)\), assign \(c_i(x)=x_1\), \(c_{i+1}(x)=1-x_1\). If \(n\) is odd, assign the remaining direction \(n\) the color \(c_n(x)=x_1\). Each \(c_i\) is independent of \(x_i\), so it defines an undirected edge coloring. Complementing all cube coordinates reverses every \(c_i\), so the coloring is antipodally odd. Each complete pair supplies one edge of each color at every cube vertex; the unmatched coordinate when \(n\) is odd supplies one additional color. Thus \(k_v\in\{\lfloor n/2\rfloor,\lceil n/2\rceil\}\) for every star, and equality holds in the bound on \(D\) and hence in (6). \(\square\)

**Corollary 3 (first-moment transfer between two-port sectors).** Uniformly over \(\mathcal B_n\) and \(\mathcal A_n\), respectively, the turn costs satisfy
\[
\boxed{
\mathbb E_{\mathcal B_n}w_d
=\frac{n+1}{n}\mathbb E_{\mathcal A_n}w_d,
\qquad
\mathbb E_{\mathcal A_n}w_d=\frac{nD}{E}.
}
\tag{10}
\]
*Proof.* Formula (2) gives
\[
\sum_{C'\in\mathcal B_n}w_d(C')
=n(n-2)\sum_{C\in\mathcal A_n}w_d(C)
+2\sum_{C\in\mathcal A_n}R_d(C).
\]
Use (4), (7), and the family cardinalities. \(\square\)

Theorems 1–2 strengthen the earlier equality of minimum color costs in the two bipointed cocircuit sectors to a polynomial identity and a sharp global conservation law for fiber costs. They do not establish that the common minimum is one: the unresolved NORI1 problem remains the existence of a geodesic-sector cocircuit with two-point intersection.
