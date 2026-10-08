# Four-path Hall obstructions force a four-support or endpoint transfer — preserved pre-item development

## Any four-path Hall obstruction gives a four-support or endpoint transfer

Let
\[
A_1\mid A_2\mid B_1\mid B_2
\]
be four vertex-disjoint tight paths spanning a boundary tournament \(H\), with empty paths omitted. Form the bipartite concatenation graph on \(\{A_1,A_2\}\) and \(\{B_1,B_2\}\), joining \(A_i\) to \(B_j\) exactly when the displayed concatenation \(A_iB_j\) is a tight path.

If this graph has a perfect matching, the two matched concatenations form a spanning two-cover. Suppose it has no perfect matching. For a \(2\times2\) bipartite graph this means some nonempty block is isolated.

Assume first that the isolated block is a left path
\[
A=(\ldots,u,v)
\]
of order at least two.

For an opposite path
\[
B_j=(a_j,b_j,\ldots)
\]
of order at least two, failure of \(AB_j\) occurs at one of the two seam triples
\[
h(u,v,a_j),\qquad h(v,a_j,b_j).
\]
If the second seam fails for both opposite paths of order at least two, then boundary antisymmetry gives
\[
h(b_j,a_j,v)=1
\]
for both \(j\). Thus the single carrier \(v\) reverses two vertex-disjoint initial edges, and the common-reverser lemma gives a Hamiltonian four-support.

Otherwise some opposite path has
\[
h(v,a_j,b_j)=1.
\]
Since \(A\) is isolated, the first seam must fail:
\[
h(u,v,a_j)=0,
\]
hence
\[
h(a_j,v,u)=1.
\]
The boundary-layer reversal conversion then uses the already-tight second seam to transfer \(v\) legally:
\[
A-v\ \mid\ (v,B_j).
\]

If an opposite block \(B_j\) is a singleton, the same transfer is automatically legal: \(A-v\) is tight and \((v,B_j)\) is a two-vertex tight path. Thus singleton tails create no exception.

If the isolated block \(A\) itself is a singleton \(v\), then for every opposite path \(B_j=(a_j,b_j,\ldots)\) of order at least two, isolation says
\[
h(v,a_j,b_j)=0,
\]
so
\[
h(b_j,a_j,v)=1.
\]
With two nonempty opposite paths this again makes \(v\) a common reverser of two disjoint initial edges and forces a Hamiltonian four-support. A singleton opposite block could not be nonadjacent to \(A\), since two singleton paths always concatenate.

The isolated-right-block case is symmetric.

Therefore every spanning four-path cover satisfies:

> either two cross-concatenations form a spanning two-cover, or the exposed four-block interface contains a Hamiltonian four-support, or one endpoint can be transferred legally from an isolated block to an opposite block.

The matched-prefix Hall theorem is a special case obtained when the four blocks arise from two crossing deletion-cover cuts.
