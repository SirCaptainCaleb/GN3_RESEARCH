# Freudenthal charts based at arbitrary poles — preserved pre-item development

## Development


The usual Freudenthal triangulation of the cube organizes monotone chains from \(\varnothing\) to \(V\): a permutation \((v_1,\ldots,v_n)\) gives the maximal simplex
\[
\varnothing
\subset
\{v_1\}
\subset
\{v_1,v_2\}
\subset\cdots\subset
V.
\]

For NOR it is useful to regard this not as one privileged triangulation, but as one chart in a family indexed by cube vertices.

Fix \(S\subseteq V\). Define the \(S\)-chart order by
\[
A\preceq_S B
\quad\Longleftrightarrow\quad
A\triangle S\subseteq B\triangle S.
\]
Then \(S\) is the bottom element and \(\bar S\) is the top element. Every antipodal geodesic from \(S\) to \(\bar S\) is monotone in this chart, and its flip order is a permutation of \(V\). Thus the Freudenthal chamber picture may be centered at any antipodal pole pair.

This use of \(A\mapsto A\triangle S\) is only a coordinate chart on the ambient cube. It does not alter or renormalize the NOR coloring. The ordered tuple
\[
(X_i,\ldots,X_{i+k})
\]
retains its original color; the chart merely records that the ambient geodesic is monotone relative to \(S\).

Hence NOR naturally carries a family of overlapping Freudenthal charts indexed by antipodal pole pairs. The same coordinate permutation may occur in different charts with different Boolean-rank up/down patterns in the original chart.

This suggests treating the pole as a geometric parameter rather than fixing \(\varnothing,V\) at the outset.
