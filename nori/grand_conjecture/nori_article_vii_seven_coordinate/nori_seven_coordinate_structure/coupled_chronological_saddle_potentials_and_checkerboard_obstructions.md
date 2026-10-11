# Coupled chronological saddle potentials and checkerboard obstructions

# Coupled chronological saddle potentials and checkerboard obstructions

## 1. An exact simultaneous-compatibility criterion

Let \(A=\{a_1,\dots,a_p\}\) and \(B=\{b_1,\dots,b_q\}\) be the parts of an edge-ordered complete bipartite graph, with \(p=q\) or \(p=q+1\). Write \(w(a,b)\) for the distinct numerical ranks of its edges. For an ordering \(A^\ast=(a_1,\dots,a_p)\) and \(B^\ast=(b_1,\dots,b_q)\), define
\[
F(A^\ast,B^\ast)=\sum_{j=1}^{q}\sum_{i=1}^{j}w(a_i,b_j).
\tag{1}
\]

**Theorem 1 (coupled chronological saddle).** The interleaved spanning path
\[
a_1,b_1,a_2,b_2,\dots,a_q,b_q
\quad (p=q),
\qquad
a_1,b_1,\dots,a_q,b_q,a_{q+1}
\quad (p=q+1)
\]
has strictly increasing edge ranks if and only if \(A^\ast\) is an adjacent-transposition local **minimum** of \(F(\cdot,B^\ast)\) and \(B^\ast\) is an adjacent-transposition local **maximum** of \(F(A^\ast,\cdot)\).

**Proof.** Swapping \(a_i,a_{i+1}\), \(1\le i<p\), changes (1) by
\[
\Delta_{A_i}F=w(a_{i+1},b_i)-w(a_i,b_i).
\tag{2}
\]
For \(p=q\), the relevant indices end at \(q-1\); for \(p=q+1\) they end at \(q\). Swapping \(b_i,b_{i+1}\), \(1\le i<q\), changes (1) by
\[
\Delta_{B_i}F=w(a_{i+1},b_i)-w(a_{i+1},b_{i+1}).
\tag{3}
\]
Because all edge weights are distinct, the first local-optimality requirement is precisely \(w(a_i,b_i)<w(a_{i+1},b_i)\), and the second is precisely \(w(a_{i+1},b_i)<w(a_{i+1},b_{i+1})\). Together they are *all* consecutive edge inequalities for the displayed interleaving, with the correct endpoint convention in either parity. \(\square\)

Thus the two chronological tournament constraints admit an exact **pure local saddle** formulation on two permutation spaces. The existing chronological theorem for transitive tournaments guarantees the minimizing half for each fixed \(B^\ast\); the simultaneous maximizing half is the missing coupling. The four-vertex example in *Endpoint-tournament factorization and monochromatic orders* shows that an arbitrary edge order need not possess such a local saddle for a spanning interleaving.

The criterion uses only ranks of edges between \(A\) and \(B\) and makes no assumption on edges within the two parts. It therefore transfers directly to the edge-order-generated ordinary boundary 3-tournament on an interleaving of those directions. For physical cube three-faces the transfer is valid for direction-only colors, where every exterior fiber has the same chart.

## 2. Threshold chain graphs and the two-by-two obstruction

Call a \(2\times2\) submatrix of the weight matrix **checkerboard-obstructed** when the two entries on one diagonal are both smaller than the entries on the other diagonal. This includes the symmetric case with the roles of the diagonals reversed. Equivalently, its two smallest edges are disjoint. An initial edge segment is its set of smallest \(t\) edges, and a **chain graph** means a bipartite graph with nested neighborhoods on either side, equivalently no induced \(2K_2\).

**Proposition 2 (chain-prefix equivalence).** An edge ordering of a complete bipartite graph has no checkerboard-obstructed \(2\times2\) rectangle if and only if every initial edge segment is a chain graph.

**Proof.** If such a rectangle exists, take the initial segment ending with the larger of its two smaller, disjoint edges. On the four selected vertices the prefix induces exactly two disjoint edges. Conversely, an induced \(2K_2\) in any prefix consists of the two diagonal edges of a \(2\times2\) rectangle, both preceding its crossed edges; the rectangle is obstructed. \(\square\)

On an obstructed \(K_{2,2}\), no alternating spanning path has strictly increasing ranks: the first and last edges in any three-edge path are disjoint, hence constitute one diagonal; its middle edge belongs to the other diagonal.

## 3. A hereditary minimax connector lemma

**Theorem 3 (row-maximum / column-minimum pivot).** Let \(M\) be a real matrix whose every \(2\times2\) submatrix is checkerboard-free. There exists an entry \(M_{ab}\) which is simultaneously a maximum in row \(a\) and a minimum in column \(b\). The same conclusion holds in every nonempty submatrix.

**Proof.** Put
\[
\alpha=\min_a\max_b M_{ab},
\qquad
\beta=\max_b\min_a M_{ab}.
\]
The elementary minimax inequality gives \(\beta\le\alpha\). Suppose \(\beta<\alpha\), and choose \(\beta<t<\alpha\). Make a bipartite graph of entries \(M_{ab}\le t\). Every column has at least one neighbor, because its minimum is at most \(\beta\), whereas every row has at least one nonneighbor, because its maximum is at least \(\alpha\). By Proposition 2 this graph is \(2K_2\)-free. Its column neighborhoods are nested; their smallest member is nonempty, so any row in that neighborhood belongs to *every* column neighborhood. This contradicts the nonneighbor in every row. Thus \(\alpha=\beta\). A row attaining its row maximum \(\alpha\) and a column attaining its column minimum \(\beta\) intersect in an entry that is both. Heredity of the forbidden-rectangle hypothesis proves the same statement for every submatrix. \(\square\)

With distinct edge ranks this pivot \((a,b)\) gives, for any remaining \(a'\ne a,b'\ne b\), an increasing three-edge connector
\[
b' \;-\; a \;-\; b \;-\; a',
\qquad
w(a,b')<w(a,b)<w(a',b).
\tag{4}
\]
The missing step is **global compatibility**: choosing successive pivots and their connectors without reusing vertices or reversing the chronology of earlier edges. The following open problem is a natural exact test of the mechanism.

**Chain-prefix Hamilton conjecture (OPEN).** Every edge ordering of \(K_{m,m}\) in which every initial edge segment is a chain graph has a strictly increasing alternating Hamilton path. The assertion concerns the complete spanning path; Theorem 3 proves only the hereditary local pivot property.

As finite evidence, exhaustive enumeration of all \(6!\) orders of \(K_{3,2}\) identifies exactly 264 checkerboard-free orders; all have an increasing alternating spanning path beginning and ending in the larger part. Enumeration of all \(9!\) orders of \(K_{3,3}\) identifies exactly 30,240 checkerboard-free orders; all have an increasing alternating spanning path. These finite checks establish **no** general Hamilton theorem.



## 6. A full-class path/defect reduction

Let \(h\) be any ordinary boundary 3-tournament on \(N\) vertices (with no global-edge-order hypothesis), and let \(p=(p_1,\dots,p_N)\) be a permutation. Define the number of bad windows relative to the target color 1 by
\[
D(p)=\#\{1\le i\le N-2: h(p_i,p_{i+1},p_{i+2})\ne1\}.
\tag{8}
\]

**Lemma 6 (extracting one long path).** If \(D(p)=D\), and \(N-2-D>0\), a positive vertex-simple tight path has order at least
\[
2+\left\lceil\frac{N-2-D}{D+1}\right\rceil.
\tag{9}
\]
**Proof.** The \(N-2-D\) positive windows form at most \(D+1\) consecutive runs. A longest run has at least the displayed number of windows minus two, and a run of \(r\) windows uses exactly \(r+2\) vertices. \(\square\)

**Lemma 7 (packing paths into a low-defect spanning order).** Suppose a hereditary class of ordinary boundary tournaments has a constant \(c>0\) such that every induced instance on \(s\ge1\) vertices admits a positive vertex-simple path on at least \(c\sqrt{s}\) vertices (with one- and two-vertex paths regarded as trivially positive). Then every instance on \(N\) vertices has a permutation \(p\) with
\[
D(p)\le 4\sqrt N/c.
\tag{10}
\]
**Proof.** Greedily remove a positive path from the remaining \(s\) vertices. If its vertex count is \(r\ge c\sqrt s\), then
\[
\sqrt s-\sqrt{s-r}=\frac{r}{\sqrt s+\sqrt{s-r}}\ge c/2.
\]
Consequently at most \(2\sqrt N/c\) blocks are removed. Concatenate their vertex sequences. Every window internal to a block is positive; at most two windows cross each block boundary. Thus \(D\le2(\#\text{blocks}-1)\le4\sqrt N/c\). \(\square\)

**Implication for the full grand-conjecture boundary goal.** The established hereditary square-root path guarantee supplies a spanning permutation with \(D=O(\sqrt N)\). A universal bound \(D=o(\sqrt N)\) for **every** ordinary boundary tournament would, by Lemma 6, force a positive path on \(\omega(\sqrt N)\) vertices, improving the universal square-root baseline. Conversely, improving path bounds can be leveraged back into stronger defect bounds by the same greedy packing argument.

The triangular potential (1) applies specifically to globally edge-ordered instances, whereas the defect variable (8) is meaningful in the **full** ordinary boundary class. Their relationship is a candidate direction for research, not an asserted transfer to unrestricted NORI1: the latter requires independent physical-edge and root-fiber compatibility.

## Status and significance

Theorems 1, 3, 4, Propositions 2, 5 and Lemmas 6–7 are proved with exact hypotheses; the chain-prefix Hamilton conjecture remains OPEN. This package isolates a joint local-saddle mechanism, a genuine four-local obstruction, a probabilistic barrier to extracting clean submatrices, and a quantitative route by which stronger coupling could improve the full ordinary-boundary lower bound. No theorem here settles unrestricted NORI1 or the Hamilton/long-path problem for every ordinary boundary 3-tournament.
