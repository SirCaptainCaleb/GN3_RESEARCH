# Two-block facet witnesses alone form a strongly connected root digraph — preserved pre-item development

## Two-block facet witnesses alone form a strongly connected root digraph

Assume a minimum ternary counterexample and fix, for every proper nonempty subset \(C\subsetneq V\), one NOR-good order \(g(C)\) of the induced instance on \(C\).

For every nontrivial ordered cut
\[
C\mid C^c,
\]
consider the canonical two-block full order
\[
\pi_C=g(C)\,g(C^c).
\]
Since the ambient instance is a counterexample, \(\pi_C\) is bad and its outermost-change root
\[
D(\pi_C)=e_{a_C}-e_{b_C}
\]
is nonzero.

By the proper-face crossing theorem §243, the source \(a_C\) lies in the first block \(C\) and the target \(b_C\) lies in the second block \(C^c\). Thus each nontrivial cut carries an actual directed root
\[
a_C\to b_C
\qquad\text{with }a_C\in C,\ b_C\notin C.
\]

Define the facet-root digraph \(H_{\mathrm{fac}}\) on \(V\) by including all these directed edges.

### Every proper vertex set has an outgoing edge

Let \(S\subsetneq V\) be nonempty. Apply the construction to the cut
\[
S\mid S^c.
\]
Its canonical facet root has source in \(S\) and target in \(S^c\). Therefore \(H_{\mathrm{fac}}\) has an edge leaving \(S\).

Hence no nonempty proper subset of vertices is closed under outgoing edges.

### Strong connectivity

Consider the condensation DAG of strongly connected components of \(H_{\mathrm{fac}}\). If there were more than one component, a sink component would be a nonempty proper vertex set with no outgoing edge, contradicting the previous paragraph.

Therefore
\[
\boxed{H_{\mathrm{fac}}\text{ is strongly connected}.}
\]

### Directed cycle and positive dependence

In particular \(H_{\mathrm{fac}}\) contains a directed simple cycle
\[
x_0\to x_1\to\cdots\to x_{m-1}\to x_0.
\]
Each edge is the outermost root of an actual canonical two-block full witness. Hence
\[
\sum_{i=0}^{m-1}(e_{x_i}-e_{x_{i+1}})=0
\]
is a positive dependence of genuine facet-witness outermost roots.

### Significance

This conclusion uses no Sperner degree, no flag interpolation, and no Radon extraction. Minimum-counterexample induction plus the proper-face crossing lemma already force a positive physical root cycle supported entirely on two-block canonical witnesses.

Thus one can attack Article III through the following sharply reduced theorem:

> A directed cycle of outermost roots arising from canonical two-block witnesses
> \[
> g(C_i)g(C_i^c)
> \]
> yields a spanning NOR-good order or a strict admissible improvement.

The supporting witnesses are now maximally simple proper-face objects: each has exactly two good blocks, and the root crosses the unique block cut.
