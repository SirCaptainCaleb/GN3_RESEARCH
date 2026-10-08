# Common-ideal separation reduces dissimilar deletion covers to a four-cell order rectangle — preserved pre-item development

## Common ideals are the correct interface for two deletion covers

Let
\[
F_a=P_0\mid P_1,\qquad F_b=R_0\mid R_1
\]
be arbitrary deletion two-covers of \(H-a\) and \(H-b\), with empty paths allowed.

Forget tightness temporarily and retain only the displayed path orders. Let \(D=D(F_a,F_b)\) be the directed graph on \(V(H)\) obtained by putting an arc \(u\to v\) whenever \(u\) occurs before \(v\) in one of the two \(P\)-orders or in one of the two \(R\)-orders. Thus each cover contributes the transitive closure of two disjoint chains. The hole \(a\) occurs only in the \(R\)-orders and \(b\) only in the \(P\)-orders.

A subset \(I\subseteq V(H)\) is a lower ideal of \(D\) exactly when its intersection with each displayed path is a prefix.

### Ideal-separation lemma

There are cuts
\[
P_i=L_iT_i,\qquad R_i=M_iN_i
\]
with the matched-prefix identity
\[
V(L_0)\cup V(L_1)
=
\bigl(V(M_0)\cup V(M_1)\bigr)\cup\{b\}
\]
if and only if \(D\) has no directed path from \(a\) to \(b\).

Proof. Such cuts are equivalent to a lower ideal \(I\) of \(D\) with
\[
b\in I,\qquad a\notin I:
\]
take \(I=V(L_0)\cup V(L_1)\), so \(I-\{b\}=V(M_0)\cup V(M_1)\). Conversely every such lower ideal gives the four prefixes.

A lower ideal containing \(b\) and excluding \(a\) exists exactly when \(a\) is not a predecessor of \(b\) in the transitive closure of \(D\). If no directed \(a\)-to-\(b\) path exists, take the full predecessor closure of \(b\). If such a path exists, every lower ideal containing \(b\) must contain \(a\). \(\square\)

Exchanging \(a,b\) gives the reverse orientation. Therefore either at least one oriented matched cut exists, or \(a\) and \(b\) lie in the same strongly connected component of \(D\).

### Two-sided failure compresses to a four-cell order rectangle

Assume neither oriented matched cut exists. Then \(D\) has directed paths both \(a\to b\) and \(b\to a\), hence a directed cycle.

Choose a shortest directed cycle in the transitive-order graph \(D\). It contains neither hole. Indeed, if it contained \(a\), its predecessor and successor on the cycle would both lie in the same \(R_j\)-chain, because \(a\) occurs in no \(P\)-chain. Transitivity of that chain shortcuts the two edges through \(a\), contradicting minimality. The same argument removes \(b\).

Now restrict to the common domain \(V(H)-\{a,b\}\). Align the support names arbitrarily and write the four support-intersection cells
\[
C_{ij}=V(P_i)\cap V(R_j),\qquad i,j\in\{0,1\}.
\]

If two common vertices in one cell occur in opposite relative orders in the two covers, there is already an order-disagreement certificate. Assume no such disagreement.

Then a shortest directed cycle contains at most one vertex from each cell \(C_{ij}\). For if \(x,y\in C_{ij}\), the two path orders compare them in the same direction. If they are nonconsecutive on the cycle, that comparison is a directed chord producing a shorter cycle. If they are consecutive, say \(x\to y\), then the predecessor edge \(z\to x\) belongs to one of the two cover orders; since \(x,y\) lie in the same support of that cover and \(x<y\) there, transitivity gives \(z\to y\), again shortening the cycle.

Edges between different cells can join only cells sharing a row or a column. The cell-adjacency graph is therefore the four-cycle
\[
C_{00}-C_{01}-C_{11}-C_{10}-C_{00}.
\]
It has no triangle. Since the shortest directed cycle uses at most one vertex from each cell, it must have length four and use all four cells.

Thus, after exchanging support names and reversing the displayed cyclic notation if necessary, there are distinct vertices
\[
x_{00}\in C_{00},\quad
x_{01}\in C_{01},\quad
x_{11}\in C_{11},\quad
x_{10}\in C_{10}
\]
such that
\[
x_{00}<_{P_0}x_{01},
\qquad
x_{01}<_{R_1}x_{11},
\qquad
x_{11}<_{P_1}x_{10},
\qquad
x_{10}<_{R_0}x_{00}.
\]

### Dichotomy

Every pair of deletion two-covers therefore has at least one of the following:

1. an oriented matched-prefix cut, hence access to the matched-cut Hall splicing theorem;
2. an order disagreement on a common support intersection;
3. a four-vertex alternating order rectangle, with one corner in each of the four crossing support cells.

In particular, if one support-intersection cell is empty, then outcome 3 is impossible: some oriented matched cut exists unless there is already an order disagreement.

This is purely order-theoretic and uses no small-order cutoff, no minimum-counterexample assumption, and no bounded-support conclusion. It changes the dissimilar-cover frontier: matched cuts need not be forced by overlap maximization or peeling. Their exact obstruction is alternating reachability, and after eliminating ordinary order disagreement the entire two-sided obstruction is one four-corner crossing rectangle.

The four-corner rectangle should not yet be identified with the protected terminal-pair carrier \(C_4\): the latter is a mutual admissibility loop, whereas this object is a directed cycle in the union of two path-order relations. The closure question is now whether the late four-label/rectangle machinery can be strengthened to convert this earlier order rectangle into a spanning two-cover, a matched cut with a perfect Hall matching, or a protected carrier loop.
