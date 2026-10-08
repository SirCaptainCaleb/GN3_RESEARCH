# Every counterexample exposes a punctured-Boolean Frankl obstruction — preserved pre-item development

## Composition

(none yet)

## Development

## Every counterexample exposes a punctured-Boolean Frankl obstruction

The maximal-front theorem gives a particularly rigid local object in every directed NOR counterexample. Let \(P\) be an inclusion-maximal \(\sigma\)-tight path, let \(F\) be its exposed first \((r-1)\)-tuple, and let \(X\) be the omitted vertices. Put \(\tau=1-\sigma\) and restrict the opposite-color front family to \(X\):
\[
\mathcal G=\{A\subseteq X:A\in\mathcal F_{\tau,F}\}.
\]
The maximal-front theorem gives
\[
\varnothing\in\mathcal G,\qquad \{x\}\in\mathcal G\ 	ext{ for every }x\in X,\qquad X\notin\mathcal G.
\tag{1}
\]

### Theorem 1: a punctured Boolean restriction is forced
There is a set \(U\subseteq X\), \(|U|\ge2\), such that
\[
\mathcal G|_U=2^U\setminus\{U\}.
\tag{2}
\]
Equivalently, every proper subset of \(U\) has a \(\tau\)-tight witness ending at the same terminal state \(F\), while \(U\) itself has no such witness.

### Proof
Because \(X\notin\mathcal G\) and \(X\) is finite, choose an inclusion-minimal set \(U\subseteq X\) with \(U\notin\mathcal G\). By (1), \(U\) is neither empty nor a singleton, so \(|U|\ge2\). Inclusion minimality says that every proper subset \(A\subsetneq U\) belongs to \(\mathcal G\), which is exactly (2). \(\square\)

Thus a counterexample does not merely contain some top-missing square. At the front of every maximal monochromatic tight path it contains a minimal obstruction whose entire proper Boolean boundary is feasible. In particular, for every \(u\in U\), the deletion support \(U\setminus\{u\}\) has a same-color tight witness ending at the common tail \(F\).

### Corollary 2: complete same-tail deletion certificates
Choose for each \(u\in U\) a \(\tau\)-tight witness \(P_u\) on \(U\setminus\{u\}\) followed by \(F\). Since \(U\) is infeasible, the omitted vertex cannot be prepended to its witness. Hence if \(F_u\) denotes the exposed first \((r-1)\)-tuple of \(P_u\), then
\[
h(u,F_u)=1-\tau=\sigma
\]
for every \(u\in U\).

So the punctured Boolean obstruction carries a complete deletion cover with a common terminal state and one blocked-front identity for every deleted coordinate. This is substantially stronger than the generic two-deletion certificate obtained from an arbitrary minimal failure of union closure.

### Corollary 3: exact Frankl deficit
The abstract set family in (2) has
\[
|2^U\setminus\{U\}|=2^{|U|}-1.
\]
For every coordinate \(u\in U\), exactly \(2^{|U|-1}-1\) members contain \(u\). Therefore its signed Frankl bias is
\[
2\bigl(2^{|U|-1}-1\bigr)-(2^{|U|}-1)=-1.
\tag{3}
\]
Thus every coordinate misses the half-frequency threshold by exactly one unit. Adding the single missing top \(U\) repairs union closure and changes every coordinate bias from \(-1\) to \(0\).

This gives an exact quantitative bridge between the two conjectural geometries: the local NOR obstruction exposed by maximality is a punctured Boolean family which fails Frankl's conclusion in the smallest possible symmetric way, and the missing object needed to repair the Frankl deficit is precisely the missing common tight witness on \(U\).

### Closure target
It is enough to rule out these punctured-Boolean witness obstructions. More explicitly, a directed NOR closure theorem may be sought in the following form:

> Let \(U\) be a finite coordinate set and \(F\) a fixed ordered terminal state. If every proper subset of \(U\) admits a \(\tau\)-tight witness ending at \(F\), then either \(U\) itself admits such a witness or the complete family of deletion witnesses can be spliced/recentered into a spanning one-change order.

The first alternative fills the missing top and restores exact Frankl balance; the second closes NOR directly. The remaining difficulty is therefore no longer generic union closure, but compatibility of a complete same-tail deletion cover.
