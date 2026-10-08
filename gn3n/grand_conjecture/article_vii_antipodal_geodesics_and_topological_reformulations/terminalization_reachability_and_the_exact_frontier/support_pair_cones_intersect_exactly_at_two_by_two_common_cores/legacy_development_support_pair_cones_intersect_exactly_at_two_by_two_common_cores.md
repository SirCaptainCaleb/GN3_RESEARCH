# Support-pair cones intersect exactly at two-by-two common cores — preserved pre-item development

## Two-cover compatibility should be measured by common support-pair cores, not by path-order agreement

Let
\[
U=(A,B),\qquad V=(C,D)
\]
be vertices of the Hamiltonian support-pair poset \(\mathcal P(H)\): \(A,B,C,D\) are Hamiltonian supports, the two entries of each ordered pair are disjoint, and each has order at least two.

Write
\[
\downarrow U=\{(E,F)\in\mathcal P(H):E\subseteq A,\ F\subseteq B\}
\]
for the principal lower interval.

### Exact two-state intersection criterion

\[
\boxed{
\downarrow U\cap\downarrow V\neq\varnothing
\iff
|A\cap C|\ge2\ \text{and}\ |B\cap D|\ge2.
}
\]

Proof. If \((E,F)\) lies in both lower intervals, then
\[
E\subseteq A\cap C,\qquad F\subseteq B\cap D,
\]
and by definition \(|E|,|F|\ge2\), giving the necessary inequalities.

Conversely, choose any two vertices
\[
e_1,e_2\in A\cap C,\qquad f_1,f_2\in B\cap D.
\]
Every two-vertex set is vacuously a tight Hamiltonian support, so
\[
(\{e_1,e_2\},\{f_1,f_2\})\in\mathcal P(H)
\]
and belongs to both lower intervals. \(\square\)

Since the involution exchanges the two entries, two *unordered* deletion states have intersecting oriented lower cones in one of the two pairings exactly when either
\[
|A\cap C|,|B\cap D|\ge2
\]
or
\[
|A\cap D|,|B\cap C|\ge2.
\]

### Family version

For oriented support pairs
\[
U_\alpha=(A_\alpha,B_\alpha),
\]
the principal lower intervals have a common vertex iff
\[
\left|\bigcap_\alpha A_\alpha\right|\ge2,
\qquad
\left|\bigcap_\alpha B_\alpha\right|\ge2.
\]
Again, any chosen two labels from each common intersection give the common lower support pair.

### Consequence for the proof architecture

In a minimum-order counterexample every \(H-x\) has a spanning two-cover, hence every hole \(x\) supplies one or more top-rank support pairs of total order \(n-1\). The natural cover of the top-rank region by their principal cones should therefore be analyzed through these \(2+2\) common cores.

This is a much weaker compatibility requirement than the deletion-cover notions used earlier:
- support partitions need not agree;
- the Hamilton orders need not agree on any common vertices;
- support-intersection cells may be heavily crossing;
- no matched cut is required.

Thus two deletion covers that are extremely dissimilar as ordered paths may nevertheless lie in the same support-pair carrier as soon as they retain two common labels on each oriented side.

The old unanimity sets in the \(\kappa_2=1\) Ky Fan argument are the one-label shadow of this criterion. For support-pair topology the natural threshold is two unanimous labels on each side, because that is exactly what creates a common vertex of \(\mathcal P(H)\).

Accordingly a more closure-directed reformulation of the fixed-hole/topological branch is:

> either the relevant family of one-hole deletion states has an oriented \(2+2\) common core and hence a common support-pair carrier, or some source face loses the second common label on one side.

The latter is the genuine carrier-degeneration event. It should be compared with the late four-label protected-loop and endpoint-rectangle machinery; ordinary order disagreement by itself is not a degeneration in \(\mathcal P(H)\).

This lemma is order-free, scale-independent, and applies immediately after minimum-counterexample reduction to \(\kappa_2=1\).
