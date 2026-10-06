# Smallest counterexamples force a tight cyclic transition block

## Metadata

- ID: smallest_counterexamples_force_a_tight_cyclic_transition_block
- Parent Section: higher_memory_norine_geodesics
- Position: 14
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Lemma: smallest counterexamples force a tight cyclic transition block

Fix \(k\ge2\), and suppose \(N_k\) fails. Let \(n\) be minimal such that a counterexample exists on an \(n\)-element ground set, and write
\[
r=n-k.
\]
Then \(r\ge3\).

For every vertex \(v\), choose any one-change permutation
\[
\sigma=(x_1,\ldots,x_{n-1})
\]
of \(V\setminus\{v\}\), which exists by minimality. Let its status word be
\[
c_1,\ldots,c_r.
\]

Then:

1. the word \(c_1,\ldots,c_r\) is not constant, hence has exactly one change;
2. if its initial color is \(a\), then its final color is \(1-a\);
3. the prepended permutation \((v,\sigma)\) has status word
   \[
   1-a,\ c_1,\ldots,c_r
   \]
   and exactly two changes;
4. the appended permutation \((\sigma,v)\) has status word
   \[
   c_1,\ldots,c_r,\ a
   \]
   and exactly two changes.

### Proof

If the reduced word \(c_1,\ldots,c_r\) were constant, then prepending \(v\) would add only one new status bit and therefore produce a word with at most one change, contradicting that the \(n\)-vertex coloring is a counterexample. Thus the reduced word has exactly one change. Write its first color as \(a\), so its last color is \(1-a\).

Let
\[
L=h(v,x_1,\ldots,x_{k-1}).
\]
The word of \((v,\sigma)\) is \(L,c_1,\ldots,c_r\). If \(L=a=c_1\), this word retains only the single old change, again contradicting failure. Hence \(L=1-a\), and the prepended word has exactly two changes.

Similarly, with
\[
R=h(x_{n-k+1},\ldots,x_{n-1},v),
\]
the word of \((\sigma,v)\) is \(c_1,\ldots,c_r,R\). If \(R=1-a=c_r\), it has only the old change. Hence \(R=a\), and the appended word also has exactly two changes.

Now close \((v,\sigma)\) into the cyclic order
\[
C=(v,x_1,\ldots,x_{n-1}),
\]
write its cyclic status word as \(s_i\), and its cyclic transition bits as
\[
d_i=s_i\oplus s_{i+1}.
\]
Choose indices so that
\[
s_0=L,\qquad s_i=c_i\ (1\le i\le r),\qquad s_{r+1}=R.
\]
Then
\[
d_0=1,\qquad d_r=1,\qquad \sum_{i=1}^{r-1}d_i=1.
\]
Consequently the two adjacent length-\(r\) transition blocks
\[
(d_0,\ldots,d_{r-1}),\qquad(d_1,\ldots,d_r)
\]
both have weight \(2\), while their common length-\((r-1)\) core has weight \(1\).

Because the original coloring is a counterexample, every cut of every cyclic order is bad. Hence every length-\(r\) block of the cyclic transition word of \(C\) has weight at least \(2\).

Thus every smallest counterexample contains a cyclic order whose transition word satisfies the counterexample density constraint everywhere and attains equality on two consecutive windows, with endpoint transition bits both equal to \(1\).

### Consequence

A smallest counterexample is much more rigid than an arbitrary bad coloring: it has a cyclic transition profile with two consecutive tight windows. Any closure argument may assume this normalization and attempt to propagate equality, force periodicity, or contradict realizability under reversal antisymmetry.
