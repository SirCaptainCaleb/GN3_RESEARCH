# Convex separation fails for rank-simple antipodal prefix carriers in all large dimensions

# Single-root reachability realization and failure of convex antipodal separation

The prefix-carrier route in Article XIV, Subsections 38, 40, 42–43, works with rooted monochromatic geodesic cones \(K_x^a\) whose simplices retain the set of used cube dimensions. Under a hypothetical NORI1 counterexample, the red reachable dimension-set family \(\mathcal R_x\) is accessible, contains no complementary pair, and contains no two disjoint sets whose union omits only one dimension (Subsection 38). We prove these conditions have **no additional single-root realizability obstruction** and construct, in every dimension \(n\ge7\), legally realizable such cones whose convex hulls contain the cube center. Consequently the existing equivariant Alexander-dual carrier framework cannot be replaced by an ordinary affine hyperplane separation of each cone from its antipode.

Write \(D=[n]\) and identify each vertex with a dimension subset \(S\subseteq D\) relative to root \(0^n\). An accessible family \(R\subseteq2^D\) contains \(\varnothing\) and, for every nonempty \(S\in R\), has some \(i\in S\) with \(S\setminus\{i\}\in R\). Say that \(R\) is *complement- and near-complement-free* when
\[
\boxed{
S,T\in R,\quad S\cap T=\varnothing
\quad\Longrightarrow\quad |S\cup T|\le n-2.
}
\tag{1}
\]
This excludes both a complementary pair and a pair omitting only one dimension.

## Theorem 1 (realization of every admissible accessible family at one root)

For every \(n\ge2\) and every accessible \(R\subseteq2^D\) satisfying (1), there exists an antipodally odd binary coloring of all undirected edges of \(Q_n\) for which the **full red-geodesic reachability family from \(0^n\) is \(R\)**.

*Proof.* Orient Boolean edges upwards in subset rank, \(S\to S\cup\{i\}\). Prescribe an edge **red** if both endpoints lie in \(R\). Prescribe an edge **blue** if its lower endpoint is in \(R\) and its upper endpoint is not in \(R\). Leave the other edges temporarily unassigned.

The antipode maps the increasing edge \(S\to S\cup\{i\}\) to the increasing edge
\[
(D\setminus(S\cup\{i\}))\longrightarrow D\setminus S.
\tag{2}
\]
Two prescribed red edges cannot be antipodal, since their upper endpoints would be complementary members of \(R\), violating (1). Two prescribed blue edges cannot be antipodal either: if both the original lower endpoint \(S\) and the opposing lower endpoint \(D\setminus(S\cup\{i\})\) belonged to \(R\), these would be disjoint members of \(R\) whose union has size \(n-1\), again violating (1). Thus every antipodal edge orbit contains at most one prescribed bit, or two prescribed *opposite* bits. Assign the complementary bit to any unassigned mate, and choose complementary bits freely on unused orbits. This extends the prescription to a legal antipodally odd coloring.

Every red geodesic starting at \(\varnothing\) increases subset rank and cannot exit \(R\), since all upward boundary edges from \(R\) were colored blue. Conversely accessibility provides a saturated chain from \(\varnothing\) to every \(S\in R\) with every intermediate set in \(R\). All its edges were colored red. Hence the red reachability family is \(R\), as asserted. \(\square\)

**Consequence.** Accessibility and the complementary/near-complementary exclusions are all that is required to realize an individual root's putative no-counterexample red reachability pattern in an antipodally odd coloring. This does not realize a global NORI1 counterexample: other roots in the resulting coloring may have a monochromatic full geodesic. Any contradiction must couple distinct roots or use more than the reachable sets of one root.

## Theorem 2 (convex-hull obstruction in every dimension at least seven)

For every \(n\ge7\), a legal antipodally odd \(Q_n\) coloring exists with root \(x\) whose red prefix complex \(K_x^0\) has the following three properties:
\[
\boxed{
K_x^0\cap A K_x^0=\varnothing,\qquad
\operatorname{conv}(|K_x^0|)\ni(\tfrac12,\ldots,\tfrac12),\qquad
\operatorname{conv}(|A K_x^0|)\ni(\tfrac12,\ldots,\tfrac12).
}
\tag{3}
\]
The red reachability family at \(x\) excludes all complementary and near-complementary pairs. In particular, the two disjoint antipodal prefix cones cannot be separated by a strict affine hyperplane.

*Proof.* Begin in dimension seven. Write subsets as seven-bit strings, with dimensions ordered left to right. Define \(R_7\) to be the union of all prefixes of the following five increasing Boolean paths:
\[
\begin{array}{l}
0000000\to0000001,\\
0000000\to0010000\to0110000\to0110010\to0111010\to0111011,\\
0000000\to0000010\to0000110\to1000110,\\
0000000\to0010000\to0010100\to1010100,\\
0000000\to0100000\to0101000\to0101100\to1101100.
\end{array}
\tag{4}
\]
There are sixteen distinct vertices in \(R_7\). It is accessible by construction. Direct comparison of the sixteen strings gives
\[
S,T\in R_7,\quad S\cap T=\varnothing
\quad\Longrightarrow\quad |S\cup T|\le5.
\tag{5}
\]
For audit, condition (5) may be checked solely from the displayed union of chains by inspecting pairs of binary strings: no pair has disjoint supports covering six or seven positions.

Among these reachable vertices select five:
\[
\begin{array}{c|ccccc}
U&0000001&0111011&1000110&1010100&1101100\\
\text{weight }6\alpha_U&1&2&1&1&1.
\end{array}
\tag{6}
\]
For each of the seven dimensions, the weighted sum of its bits in (6) equals \(3/6=1/2\), so
\[
\boxed{
\sum_{U\text{ in }(6)}\alpha_U\mathbf1_U
=(\tfrac12,\ldots,\tfrac12).
}
\tag{7}
\]
Theorem 1 gives a legal antipodally odd coloring whose red geodesic reachability family from zero is \(R_7\). Hence the red prefix complex contains every listed vertex and its convex hull contains the center. The family is complement-free; both \(K_0^0\) and its antipodal image are subcomplexes of the same rooted Freudenthal triangulation, so their geometric intersection is empty because they have no common vertices. Antipodality fixes the center and preserves convex hulls, proving (3) for \(n=7\).

For \(n>7\), take the product family
\[
R_n=\{S\cup J:S\in R_7,\ J\subseteq\{8,\ldots,n\}\}.
\tag{8}
\]
It is accessible. If two members are disjoint and cover all but at most one of the \(n\) dimensions, their restrictions to the first seven dimensions are disjoint and cover at least six of those seven dimensions, contradicting (5). Thus (1) holds, so Theorem 1 realizes \(R_n\) as a red reachability family for a legal \(n\)-cube coloring. Finally
\[
\operatorname{conv}(R_n)=\operatorname{conv}(R_7)\times[0,1]^{n-7}
\]
contains the center, and the same antipodal-disjointness argument applies. \(\square\)

**Implication for the Wu–Yang modification.** The dimension-simple prefix-carrier complexes have much richer geometry than disjoint convex subsets. Even the full complement-avoidance and one-missing-dimension exclusion constraints, which hold at each root under a hypothetical NORI1 counterexample, do not force an affine linear separation of a carrier from its antipode. A proof cannot simply average reachable endpoints, subtract antipodal barycenters, and normalize to obtain the required low-dimensional odd map: that difference may vanish. The topological complement \(S^{n-1}\setminus(K_x^0\cup A K_x^0)\), its Alexander-dual sphere structure, and support-filtered transport retain information that ordinary convexification destroys. This is a method-specific obstruction, not a counterexample to NORI1; the constructed legal coloring is not asserted to lack full monochromatic geodesics at other roots.
