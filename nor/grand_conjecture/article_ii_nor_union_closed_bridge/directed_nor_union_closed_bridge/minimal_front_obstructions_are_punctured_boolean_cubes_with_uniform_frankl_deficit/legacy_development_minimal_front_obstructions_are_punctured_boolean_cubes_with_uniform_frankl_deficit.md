# Minimal front obstructions are punctured Boolean cubes with uniform Frankl deficit — preserved pre-item development

## A counterexample exposes a punctured Boolean cube with uniform Frankl deficit

Continue with a maximal \(\sigma\)-tight witness \(P\) ending at \(S\), exposed front \(F\), and omitted set
\[
X=V\setminus V(P).
\]
By the maximal-front theorem, in a NOR counterexample the restricted opposite-color support family
\[
\mathcal G(P)=\{A\subseteq X:A\in\mathcal F_{1-\sigma,F}\}
\]
contains \(\varnothing\) and every singleton of \(X\), but omits \(X\).

Choose an inclusion-minimal set
\[
U\subseteq X
\]
with \(U\notin\mathcal G(P)\). Then \(|U|\ge2\).

### Proposition
The restriction of \(\mathcal G(P)\) to \(U\) is exactly
\[
2^U\setminus\{U\}.
\]
Equivalently, every proper subset of \(U\) has a \((1-\sigma)\)-tight witness ending at \(F\), while \(U\) itself has none.

### Proof
By inclusion-minimality of \(U\), every proper subset \(A\subsetneq U\) belongs to \(\mathcal G(P)\). The set \(U\) does not. There are no other subsets of \(U\). \(\square\)

Thus a NOR counterexample does not merely produce an arbitrary non-union-closed accessible family. It produces, around every maximal monochromatic branch after passing to a minimal obstruction, a complete Boolean cube with only its top removed.

### Deletion certificates
For every \(u\in U\),
\[
U\setminus\{u\}\in\mathcal F_{1-\sigma,F}.
\]
Choose a \((1-\sigma)\)-tight witness \(Q_u\) for this deletion. Since \(U\) itself is infeasible, prepending \(u\) to \(Q_u\) cannot preserve color \(1-\sigma\). Hence
\[
h(u,F_{Q_u})=\sigma,
\]
where \(F_{Q_u}\) is the exposed first \((r-1)\)-tuple of \(Q_u\).

So the punctured cube comes with a full family of same-tail deletion witnesses, each blocked by its missing vertex at the exposed front. This is the ordered information that must be exploited to close the obstruction.

### Frankl frequency calculation
Let \(m=|U|\) and
\[
\mathcal H=2^U\setminus\{U\}.
\]
Then
\[
|\mathcal H|=2^m-1.
\]
For every coordinate \(u\in U\), exactly \(2^{m-1}-1\) members of \(\mathcal H\) contain \(u\). Therefore
\[
2f_u-|\mathcal H|
=
2(2^{m-1}-1)-(2^m-1)
=
-1.
\]

Hence every coordinate lies strictly below half the sets, and all coordinates have the same smallest integral negative bias.

Adding the single missing top \(U\) turns \(\mathcal H\) into the full Boolean family \(2^U\), where every coordinate has bias zero. Moreover, because \(|U|\ge2\), any union-closed superfamily of \(\mathcal H\) inside \(2^U\) must add \(U\): for distinct \(a,b\in U\), both \(U\setminus\{a\}\) and \(U\setminus\{b\}\) are present and their union is \(U\).

Thus the local NOR obstruction is one set away from union closure and one set away from the Frankl equality boundary.

### Consequence for Article II
This sharpens the bridge target. A hypothetical NOR counterexample canonically generates a punctured Boolean support cube whose set-theoretic data are completely understood. The remaining information is entirely in the incompatible tight witness orders attached to its proper subsets.

Accordingly, no further set-family theorem is needed at this minimal scale: union closure would add exactly the missing top and close NOR by the maximal-front splice. The closure problem has become an ordered lifting problem over the unique missing join:

> Given tight witnesses ending at one common terminal tuple for every proper subset of \(U\), prove that either one witness system synchronizes to realize \(U\), or the blocked deletion witnesses yield a spanning one-change order by a different splice.

This is a more rigid target than a generic minimal top-missing square: every face below the missing top is already feasible.
