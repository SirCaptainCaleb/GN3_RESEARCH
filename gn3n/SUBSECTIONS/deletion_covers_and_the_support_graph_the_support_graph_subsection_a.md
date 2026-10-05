# deletion_covers_and_the_support_graph_the_support_graph_subsection_a

## Metadata

- ID: deletion_covers_and_the_support_graph_the_support_graph_subsection_a
- Parent Section: deletion_covers_and_the_support_graph_the_support_graph
- Position: 1
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Let \(J\) be the graph whose vertices are the distinct supports occurring among the selected covers \(F_x\), with an edge \(e_x\) joining the two supports of \(F_x\). The edge is labeled by \(x\). The graph is simple: its two endpoint supports have union \(V(H)-\{x\}\), so they determine the label \(x\).

**Lemma 4 (support-graph dichotomy).** Either \(J\) is a forest, or \(V(H)\) has odd order \(2k+1\), every vertex of \(H\) occurs as an edge label, and \(J\) is one cycle of length \(2k+1\). In the cyclic case every support has order \(k\).

**Proof.** Fix \(z\in V(H)\). On every edge \(e_x\) with \(x\ne z\), exactly one endpoint support contains \(z\); on \(e_z\), if present, neither endpoint contains \(z\). Hence membership of \(z\) gives a bipartition of \(J-e_z\).

Suppose \(J\) contains a cycle \(C\) and \(e_z\in E(C)\). The path \(C-e_z\) joins two supports omitting \(z\), while membership of \(z\) alternates at each edge. Thus \(|C|-1\) is even, so \(C\) is odd.

If some \(y\in V(H)\) is not a label of \(C\), membership of \(y\) alternates around all edges of the odd cycle, which is impossible. Therefore the labels of \(C\) are all vertices of \(H\). Since edge labels are distinct, no selected edge lies outside \(C\). Every support vertex is incident with a selected edge, so \(J=C\). On each edge, the endpoint support sizes sum to \(n-1\). Alternating this equality around an odd cycle forces all support sizes to be \((n-1)/2\). \(\square\)

Two selected covers are support-compatible exactly when their edges of \(J\) share a support vertex.

**Lemma 5.** For distinct labels \(a,b\), the selected covers \(F_a,F_b\) are support-compatible if and only if \(e_a,e_b\) are adjacent in \(J\).

**Proof.** A shared endpoint of \(e_a,e_b\) is a common path support, so the restricted support partitions agree.

Conversely, write \(F_a=A\mid B\) with \(b\in A\), and assume that the restrictions of \(F_a,F_b\) to \(H-\{a,b\}\) have the same support partition. Since neither component of a deletion cover is a singleton, the two restricted classes are \(A-\{b\}\) and \(B\). In \(F_b\), the restored vertex \(a\) must join one of them. If it joins \(B\), then \(A\) and \(B\cup\{a\}\) are disjoint Hamiltonian supports covering \(H\), a contradiction. Hence it joins \(A-\{b\}\), and \(B\) is a support of both selected covers. \(\square\)

Thus the graph of support compatibility is the line graph \(L(J)\).
