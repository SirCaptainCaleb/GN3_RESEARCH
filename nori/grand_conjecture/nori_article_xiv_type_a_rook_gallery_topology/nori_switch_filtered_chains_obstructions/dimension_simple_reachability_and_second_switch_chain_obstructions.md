# Dimension-simple reachability and second-switch chain obstructions

# Dimension-simple modifications of the Wu–Yang obstruction

Wu and Yang's chain-level Borsuk–Ulam proof of the unrestricted monochromatic **antipodal path** theorem (arXiv:2607.19276, Sections 2 and 5) begins with ordinary red connected components. That quotient permits concatenating red paths that repeat cube dimensions. The aim here is to retain dimension-simplicity throughout, while replacing the component-pair rook labeling and preserving the original freely chosen geodesic root. The two constructions below give rigorous entry points and expose the remaining topological obstruction.

## 1. Geodesic reachability replaces ordinary components

Let \(c:E(Q_n)\to\mathbb F_2\) satisfy \(c(\bar e)=1-c(e)\). Use 0 for red and 1 for blue. For any cube vertex \(x\), define
\[
R(x)=\{y\in Q_n:\text{a red shortest path from }x\text{ to }y\text{ exists}\}.
\tag{1}
\]
A shortest cube path uses each of its dimensions once. Write \(\bar x=x\oplus\mathbf1\), \(H_{i,b}=\{y:y_i=b\}\), and \(x^i=x\oplus e_i\).

**Theorem 1 (two-cone meeting criterion).** The following statements are equivalent for each specified root \(x\):

(a) A red full antipodal geodesic begins at \(x\).

(b) There exists \(y\in R(x)\cap R(\bar x)\).

(c) There is a subset \(S\subseteq[n]\) such that a red path from \(x\) to \(x\oplus\mathbf1_S\) traverses precisely \(S\), and a blue path from \(x\) to \(x\oplus\mathbf1_{S^c}\) traverses precisely \(S^c\).

*Proof.* Any red antipodal geodesic can be split at a vertex \(y\), and reversing its second part gives red shortest paths from both \(x\) and \(\bar x\) to \(y\). Conversely, given \(y\in R(x)\cap R(\bar x)\), let \(S=\{i:x_i\ne y_i\}\). A shortest path from \(x\) to \(y\) uses the dimensions of \(S\) once, and a shortest path from \(\bar x\) to \(y\) uses those of \(S^c\) once. Concatenate the first with the reverse of the second: it is a red \(n\)-edge geodesic from \(x\) to \(\bar x\). Under the antipodal map, reversal of the second red path gives a blue shortest path from \(x\) to \(x\oplus\mathbf1_{S^c}=\bar y\). This gives (c), and reversing the construction gives (b). \(\square\)

**Proposition 2 (rank-preserving transport across a colored edge).** If \(c(\{x,x^i\})=0\), then
\[
R(x^i)\cap H_{i,x_i\oplus1}\subseteq R(x),
\qquad
R(x)\cap H_{i,x_i}\subseteq R(x^i).
\tag{2}
\]
If \(c(\{x,x^i\})=1\), the same inclusions hold with \(x,x^i\) replaced by \(\bar x,\overline{x^i}\).

*Proof.* Suppose \(y\in R(x^i)\cap H_{i,x_i\oplus1}\). A red shortest path from \(x^i\) to \(y\) avoids dimension \(i\). Prepending the red edge \(x\to x^i\) gives a red shortest path from \(x\) to \(y\). The other inclusion follows symmetrically by prepending \(x^i\to x\) to a path avoiding \(i\). If the given edge is blue, its antipodal edge is red, so the preceding argument applies there. \(\square\)

Consequently, a hypothetical coloring without any monochromatic antipodal geodesic gives pairs
\[
q(x)=(R(x),R(\bar x)),\qquad q(\bar x)=(R(\bar x),R(x)),
\tag{3}
\]
whose entries are disjoint by Theorem 1. Along a red edge, the first entries overlap and obey the rank-sensitive inclusions (2); along a blue edge the second entries do so. This is a set-valued counterpart of the Wu–Yang component-pair rook labeling, retaining the ranks of joined dimension sets.

**Proposition 3 (intersection alone cannot replace rook equality).** If \(n\ge3\), put
\[
R_1(x)=\{x\}\cup\{x^i:c(\{x,x^i\})=0\}.
\tag{4}
\]
For every antipodally odd coloring of \(Q_n\), the pair labeling \(q_1(x)=(R_1(x),R_1(\bar x))\) has disjoint entries, is swapped by antipodality, and has the property that across each cube edge either its first entries or its second entries intersect. Therefore these three conditions, without geodesic-extension closure such as (2), can hold even when a monochromatic antipodal geodesic exists.

*Proof.* The two sets in a pair are contained in Hamming balls of radius one about antipodal vertices, whose centers are distance \(n\ge3\) apart; the balls are disjoint. An antipodal vertex swaps the entries. If an edge is red, its two endpoints occur in both neighboring first-entry sets. If it is blue, its antipodal edge is red and the same assertion holds for the neighboring second-entry sets. \(\square\)

The critical extra structure beyond Wu–Yang's rook relation is thus **rank-preserving extension of geodesic witnesses**. Ordinary connected-component equality loses this structure; mere intersection of set labels is insufficient.

## 2. A dimension-simple equivariant labeling of Coxeter chambers

Let \(n\ge4\). The type-\(B_n\) spherical Coxeter complex is a triangulation of \(S^{n-1}\). Its chambers are labeled by \((x,\pi)\), with \(x\in\mathbb F_2^n\) and \(\pi\in S_n\); the chamber represents the full antipodal geodesic \(P(x,\pi)\) using every dimension once. Negation takes \((x,\pi)\) to \((\bar x,\pi)\).

Two chambers share a facet precisely when one of the following holds: (i) the root changes from \(x\) to \(x\oplus e_{\pi_1}\), with the dimension order unchanged; or (ii) two consecutive dimensions in the order are interchanged, with the root unchanged.

For a full geodesic write \(w=(w_1,\ldots,w_n)\) for its edge colors, and let \(s_k(w)\in[k,n-1]\) be the position of its \(k\)-th color change, when it exists. If a coloring had no monochromatic full antipodal geodesic at any root, **every** full-geodesic word would have at least two changes: a one-change word can be cyclically root-slid at its sole change into a monochromatic word, and a zero-change word is already monochromatic. Under this hypothetical assumption define
\[
\ell(x,\pi)=(-1)^{w_1(x,\pi)}e_{s_2(w(x,\pi))}
\in\{\pm e_2,\ldots,\pm e_{n-1}\}\subset\mathbb R^{n-2}.
\tag{5}
\]

**Theorem 4 (second-switch labeling on the Coxeter dual 1-skeleton).** Under the hypothetical absence of monochromatic full antipodal geodesics, the labeling (5) has the following properties:

(i) It is antipodally odd: \(\ell(\bar x,\pi)=-\ell(x,\pi)\).

(ii) Any two chambers sharing a facet receive nonopposite labels.

(iii) Hence, on the 1-skeleton of the dual type-\(B_n\) Coxeter cell decomposition of \(S^{n-1}\), linear interpolation along dual edges yields a continuous antipodally equivariant map to the crosspolytope boundary \(S^{n-3}\).

*Proof.* Complementing the starting vertex complements all word bits under antipodal oddness; it preserves every change position while reversing the sign in (5), proving (i).

Consider two adjacent chambers. If the facet move flips the sign of the first dimension, the two geodesics traverse the same undirected first edge, so their first word bits agree. If it interchanges dimensions in positions \(i,i+1\) with \(i\ge2\), their first edges also agree. Thus their labels have the same sign in both cases and cannot be opposites.

It remains to exchange the first two dimensions. The two geodesics have color words \(w,w'\) agreeing in positions \(j\ge3\), since they reach the same vertex after the two exchanged steps and then traverse identical edges. If their first bits also agree, their labels have the same sign. Otherwise assume for contradiction that their second switches occur at the same index \(r\ge2\). Then each word has two switches among its first \(r\) comparisons, so
\[
w_1\oplus w_{r+1}=0=w'_1\oplus w'_{r+1}.
\]
But \(w_{r+1}=w'_{r+1}\), while \(w_1\ne w'_1\), a contradiction. This proves (ii).

The dual cellulation has one vertex per Coxeter chamber and one edge per shared chamber facet. Each label in (5) is a vertex of the \((n-2)\)-dimensional crosspolytope; any pair of nonopposite vertices spans an edge of its boundary. Linear extension along dual edges therefore gives the required odd continuous map of 1-skeleta. \(\square\)

The same argument applies to a signed \(k\)-th-switch label for every \(k\ge2\), provided each word contains at least \(k\) switches. The second-switch choice is the one supplied by the absence of monochromatic full geodesics and has only \(n-2\) absolute labels.

**Corollary 5 (extension through the lower skeleton).** For \(n\ge5\), the map in Theorem 4 extends antipodally equivariantly over the \((n-3)\)-skeleton of the dual Coxeter cell complex.

*Proof.* The target \(S^{n-3}\) is \((n-4)\)-connected. Inductively, for each dual \(j\)-cell with \(2\le j\le n-3\), its attaching map has domain \(S^{j-1}\), and \(\pi_{j-1}(S^{n-3})=0\). Extend over representatives of antipodal cell pairs and define the other extensions by equivariance. The antipodal action is free on the spherical cellulation, so cells occur in distinct antipodal pairs. \(\square\)

## 3. The first missing cellwise compatibility

Even though facet-adjacent chambers receive nonopposite second-switch labels, chambers meeting in a codimension-two Coxeter face can receive opposite labels. The following witness demonstrates why Theorem 4 does not automatically extend by radial coning over all dual cells.

**Proposition 6 (codimension-two warning).** In \(Q_4\) there is an antipodally odd edge coloring for which the chambers with root \(0000\) and orders \((1,2,3,4)\) and \((2,3,1,4)\) have respective words
\[
(1,0,1,0)\quad\text{and}\quad(0,1,0,0).
\]
Both have a second switch at position \(2\), so their labels in (5) are \(-e_2\) and \(+e_2\). Yet their type-\(B_4\) chambers meet at the face where the first three absolute-value magnitudes are equal, a codimension-two face.

*Proof.* Start at \(0000\), and specify the following seven undirected edge colors (bits index dimensions \(1,2,3,4\)):
\[
\begin{array}{c|c|c}
\text{edge start}&\text{dimension}&\text{color}\\ \hline
0000&1&1\\
1000&2&0\\
1100&3&1\\
1110&4&0\\
0000&2&0\\
0100&3&1\\
0110&1&0
\end{array}
\]
No two of these edges are antipodal (their dimension names differ or, for parallel edges, at least one other dimension has matching endpoint bits). Give each antipodal edge the complementary bit and color the remaining antipodal pairs arbitrarily. The specified paths have the displayed words. Their orders differ only by permutations of the first three dimensions, so their chambers are incident with the same codimension-two face of the type-B arrangement. \(\square\)

This example asserts a **local obstruction to a naive radial extension**, not a counterexample to NORI1: other root-and-order flags may contain monochromatic geodesics. A full chain-map construction must provide compatible fillings of dual cells even when their sets of chamber labels include opposite vectors. This is the proper analogue of Wu–Yang's dependent-radial cancellation and rook-gallery rank bound, rather than an assumption that all cell labels lie in one positive cone.

## 4. The revised proof target

Wu and Yang create an equivariant augmentation-preserving chain map from a sphere of dimension \(K-1\) to one of dimension \(K-2\). Their Freudenthal paths use distinct dimensions, but the *component-pair reduction* forgets this rank constraint. Theorems 1–4 replace the lost information by rooted red reachability and by an odd second-switch label on complete type-B chambers. Both approaches preserve arbitrary starting roots and all cube dimensions.

The immediate open obligation is to produce a **color-consistent equivariant extension of the second-switch 1-skeleton map to the full dual cell chain complex**, or an analogous chain assignment built from the rank-preserving inclusions (2). Such a full extension would contradict the Borsuk–Ulam obstruction, since it would give an antipodally equivariant map \(S^{n-1}\to S^{n-3}\). Corollary 5 already provides the extension through the \((n-3)\)-skeleton; the substantive obstructions begin in dimension \(n-2\).

This work is targeted at the unrestricted NORI1 geodesic problem. Boundary tournaments remain a required eventual specialization of a unified theorem, but additional restricted coloring families and finite-order computations are not proposed as the proof mechanism.
