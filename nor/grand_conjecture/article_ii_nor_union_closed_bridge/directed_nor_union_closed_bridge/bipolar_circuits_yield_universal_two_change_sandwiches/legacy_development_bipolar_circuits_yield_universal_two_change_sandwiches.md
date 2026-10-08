# Bipolar circuits yield universal two-change sandwiches — preserved pre-item development

## Development

## Bipolar circuits yield universal two-change sandwiches

Let \(P\) be a maximal \(\sigma\)-tight path with first state \(F\), last state \(R\), and omitted set \(X\). Put \(\tau=1-\sigma\). Assume \(X\) is a **bipolar circuit**:
\[
\mathcal F_{\tau,F}|_X=2^X\setminus\{X\},
\qquad
\mathcal F_{\sigma,R^{\rm rev}}|_X=2^X\setminus\{X\}.
\tag{1}
\]
Thus every proper subset of \(X\) has a \(\tau\)-tight witness ending at the left pole \(F\), and a \(\sigma\)-tight witness ending at the reversed right pole \(R^{\rm rev}\).

### Theorem 1: every proper bipartition gives a spanning two-change sandwich
Let
\[
X=A\dot\cup B,\qquad A,B\subsetneq X.
\]
Choose a \(\tau\)-tight witness \(Q_A\) on \(A\) ending at \(F\), and a \(\sigma\)-tight witness \(Q_B\) on \(B\) ending at \(R^{\rm rev}\). Reverse \(Q_B\); it becomes a \(\tau\)-tight path beginning at \(R\). Glue these two witnesses to the two ends of \(P\). The resulting spanning coordinate order has status word
\[
\tau^{|A|}\,\sigma^{|P|-r+1}\,\tau^{|B|},
\tag{2}
\]
with zero-length outer blocks omitted when the corresponding part is empty.

#### Proof
The left overlap is exactly the terminal state \(F\), so every window before the first window belonging solely to \(P\) is a window of \(Q_A\) and has color \(\tau\). The middle windows are exactly the windows of \(P\), all color \(\sigma\). Reversal antisymmetry turns \(Q_B\) into a \(\tau\)-tight path beginning at \(R\), so after the last window of \(P\), all remaining windows have color \(\tau\). The supports \(A\), \(V(P)\), and \(B\) are disjoint and cover \(V\). \(□\)

Thus a bipolar circuit is not an arbitrary unresolved obstruction: it supplies a full family of spanning orders with exactly the same middle monochromatic core and freely chosen proper support on either outer side.

### Corollary 2: singleton-cap sandwiches
For every \(x\in X\), taking
\[
A=\{x\},\qquad B=X\setminus\{x\}
\]
gives a spanning order whose first run consists of exactly one \(\tau\)-window:
\[
\tau\,\sigma^{|P|-r+1}\,\tau^{|X|-1}.
\tag{3}
\]
Taking instead
\[
A=X\setminus\{x\},\qquad B=\{x\}
\]
gives a spanning order whose final run consists of exactly one \(\tau\)-window:
\[
\tau^{|X|-1}\,\sigma^{|P|-r+1}\,\tau.
\tag{4}
\]
Hence the bipolar obstruction is always one local repair away from a spanning one-change word at either end.

### Corollary 3: opposite-direction deletion orders for every hole
For every \(x\in X\), the proper support \(X\setminus\{x\}\) is feasible at both poles. Therefore \(V\setminus\{x\}\) has two one-change orders sharing the same monochromatic core \(P\):

- a left-facet order with word \(\tau^{|X|-1}\sigma^{|P|-r+1}\);
- a right-facet order with word \(\sigma^{|P|-r+1}\tau^{|X|-1}\).

Thus every deleted vertex admits one certificate switching \(\tau\to\sigma\) and another switching \(\sigma\to\tau\). In a minimum counterexample both certificates are endpoint-blocked, so the same vertex is constrained simultaneously by two oppositely oriented one-change paths.

### Closure significance
The no-descent case has therefore collapsed from 'two punctured Boolean families' to a highly structured two-pole system:

- every proper support can be assigned to either pole;
- every proper bipartition gives a spanning two-change sandwich;
- every singleton can be made the unique first or unique final outer run;
- every vertex deletion has one-change certificates in both switch directions.

A closure proof for bipolar circuits only needs to eliminate the remaining middle return from \(\sigma\) to \(\tau\) in this universal sandwich family. This is a substantially narrower target than arbitrary witness synchronization.
