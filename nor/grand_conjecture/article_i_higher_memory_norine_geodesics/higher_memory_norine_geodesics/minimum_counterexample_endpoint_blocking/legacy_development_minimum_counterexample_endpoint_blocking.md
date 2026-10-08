# Minimum-counterexample endpoint blocking — preserved pre-item development

## Development

## Minimum-counterexample endpoint blocking

Fix \(r\ge 2\), and suppose \(h\) is a counterexample to \(N_k\) on a ground set \(V\) of minimum possible size \(n\).

For \(x\in V\), let
\[
\pi=(v_1,\ldots,v_{n-1})
\]
be any permutation of \(V\setminus\{x\}\) whose sliding \(r\)-window word
\[
c_1,\ldots,c_m,\qquad m=n-r,
\]
has at most one change. Such a permutation exists by minimality.

Then:

1. \(c_1,\ldots,c_m\) has exactly one change; it cannot be constant.
2. Prepending \(x\) forces
\[
h(x,v_1,\ldots,v_{r-1})=1-c_1.
\]
3. Appending \(x\) forces
\[
h(v_{n-r},\ldots,v_{n-1},x)=1-c_m.
\]

### Proof

If the deletion word were constant, prepending \(x\) would add only one new window, so the full word would still have at most one change, contradicting counterexamplehood. Hence the deletion word has exactly one change.

Prepending \(x\) gives the word \(d,c_1,\ldots,c_m\), where \(d=h(x,v_1,\ldots,v_{r-1})\). Since the suffix already has exactly one change and the full word must have at least two, \(d\ne c_1\). The right-end statement is identical.

### Consequence

Every one-change ordering of every vertex deletion in a minimum counterexample is blocked at both ends. This converts minimality into local directed constraints on terminal \((r-1)\)-tuples, without any small-order assumption.
