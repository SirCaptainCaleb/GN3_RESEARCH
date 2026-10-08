# Rank parity refutes the unrestricted tuple-window N_k — preserved pre-item development

## Composition

(none yet)

## Development

## Refutation of the unrestricted tuple-window formulation

Under the current tuple-arity indexing, suppose \(N_k\) is interpreted as allowing an arbitrary binary coloring
\[
\chi(X_0,\ldots,X_{k-1})
\]
of ordered \(k\)-tuples of consecutive cube vertices, subject only to
\[
\chi(\bar X_{k-1},\ldots,\bar X_0)=1-\chi(X_0,\ldots,X_{k-1}).
\]

Then this unrestricted formulation is false for every \(k\ge1\).

Take cube dimension
\[
n=k+2
\]
and define
\[
\chi(X_0,\ldots,X_{k-1})=|X_0|\pmod 2.
\]

Along any geodesic segment of \(k-1\) steps,
\[
|X_{k-1}|\equiv |X_0|+(k-1)\pmod2.
\]
Hence
\[
|\bar X_{k-1}|
\equiv n+|X_{k-1}|
\equiv |X_0|+n+k-1
\equiv |X_0|+1
\pmod2,
\]
because \(n=k+2\), so \(n+k-1=2k+1\) is odd. Therefore
\[
\chi(\bar X_{k-1},\ldots,\bar X_0)
=1-\chi(X_0,\ldots,X_{k-1}),
\]
as required.

Now let
\[
G=(X_0,\ldots,X_n)
\]
be any antipodal geodesic. Each cube step flips rank parity, so the sliding \(N_k\) word is
\[
|X_0|,|X_1|,|X_2|,|X_3|\pmod2,
\]
because \(n-k+2=4\). Thus every such word is
\[
0101\quad\text{or}\quad1010,
\]
and has three changes.

So the unrestricted basepoint-dependent tuple-window version of \(N_k\) fails already in dimension \(k+2\), for every \(k\).

### Consequence for the current reindexing

Changing the project index so that \(k\) denotes cube-vertex tuple arity does not remove the old rank-parity obstruction. Any viable grand conjecture must retain an additional restriction excluding absolute-basepoint dependence (for example the directed translation-invariant coordinate sector), or adopt a different repaired family.

This refutation concerns the widened tuple-window formulation only. It does not refute the directed translation-invariant coordinate conjecture.
