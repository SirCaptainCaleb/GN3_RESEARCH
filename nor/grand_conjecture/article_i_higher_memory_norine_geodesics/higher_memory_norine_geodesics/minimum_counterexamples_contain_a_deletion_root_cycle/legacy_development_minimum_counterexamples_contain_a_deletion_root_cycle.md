# Minimum counterexamples contain a deletion-root cycle — preserved pre-item development

## Development

## Deletion orders generate a root recurrence without topology

Fix coordinate-label arity \(r\ge2\), and suppose \(h\) is a minimum directed-sector counterexample on an \(n\)-element ground set \(V\).

For each \(x\in V\), choose any one-change ordering
\[
\sigma_x=(v_1,\ldots,v_{n-1})
\]
of \(V\setminus\{x\}\). By endpoint blocking its status word has exactly one change. Write
\[
c_1\cdots c_s=a^p(1-a)^q,
\qquad
p,q\ge1,
\qquad
s=n-r.
\]
Define the two coordinates immediately outside the transition center by
\[
L_x:=v_p,
\qquad
R_x:=v_{p+r}.
\]
The indices are valid because \(p,q\ge1\).

Recall the canonical pair-defect
\[
D(\pi)
=
\sum_{\substack{i<j\\ d_i=d_j=1}}
(e_{\pi_i}-e_{\pi_{j+r}}).
\]

### Lemma 1: prepending and appending the deleted vertex give single roots

For the prepended order
\[
\pi_x^-=(x,v_1,\ldots,v_{n-1}),
\]
endpoint blocking makes the full status word
\[
(1-a),a^p,(1-a)^q.
\]
Its only two changes are at transition indices \(1\) and \(p+1\). Therefore
\[
D(\pi_x^-)=e_x-e_{R_x}.
\]

For the appended order
\[
\pi_x^+=(v_1,\ldots,v_{n-1},x),
\]
the full status word is
\[
a^p,(1-a)^q,a.
\]
Its only two changes are at indices \(p\) and \(s\), hence
\[
D(\pi_x^+)=e_{L_x}-e_x.
\]

Thus every deleted vertex sits in a directed two-edge root path
\[
L_x\longrightarrow x\longrightarrow R_x
\]
realized by pair-defects of two full coordinate orders, each having exactly two status changes.

### Corollary 2: a positive root cycle exists

Choose the outgoing root at every vertex,
\[
x\longrightarrow R_x.
\]
This is a functional digraph on the finite set \(V\), so it contains a directed cycle
\[
x_1\to x_2\to\cdots\to x_t\to x_1.
\]
For the corresponding prepended orders,
\[
D(\pi_{x_i}^-)=e_{x_i}-e_{x_{i+1}},
\]
and therefore
\[
\sum_{i=1}^t D(\pi_{x_i}^-)=0.
\]

So every minimum counterexample already contains a nonempty positive balance of canonical pair-defects, supported on a directed coordinate cycle. No cellular extension, target compression, or Borsuk--Ulam step is needed to obtain this recurrence.

### Interpretation

The topological route was using positive root balance to manufacture directed recurrence among defect coordinates. Minimum-counterexample endpoint blocking supplies such a recurrence directly, and in the especially rigid class of orders with exactly two changes and one change forced at an endpoint.

The remaining difficulty is geometric rather than algebraic: the deletion orders belonging to the cycle need not refine a common proper permutahedral face, so the existing face-localization descent cannot yet be applied to this balance. A closure argument should therefore try to synchronize these cycle certificates, or show that a shortest deletion-root cycle can be represented in one common face block.

### Audit

The root endpoint \(R_x=v_{p+r}\) is the coordinate immediately after the \((r-1)\)-vertex transition center in the linear deletion order; \(L_x=v_p\) is the coordinate immediately before it. No claim is made that either is an outer branch endpoint. The cycle balance alone does not imply a smaller counterexample.
