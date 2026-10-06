# Uniformity descent by centered windows

Investigate whether higher-uniformity NOR implies lower-uniformity NOR, especially same-parity descent N_{k+2} => N_k. The centered-window projection is canonical and antipodally compatible, but currently leaves boundary defects uncontrolled.


### Same-parity centered-window reduction

Let \(N_k\) denote the ordered-\(k\)-tuple NOR conjecture.

If \(k-j=2r\), every ordered geodesic \(k\)-segment
\[
(X_0,\ldots,X_k)
\]
contains a canonical centered ordered \(j\)-segment
\[
(X_r,\ldots,X_{r+j}).
\]

Hence every \(j\)-coloring \(\chi_j\) induces a \(k\)-coloring
\[
\chi_k(X_0,\ldots,X_k)
=
\chi_j(X_r,\ldots,X_{r+j}).
\]

Because complement-plus-reversal preserves the centered subwindow, antipodal antisymmetry is preserved.

Along an antipodal geodesic, the induced \(k\)-word is the \(j\)-word with its first \(r\) and last \(r\) entries deleted.

Therefore a proof of \(N_k\) yields a lower-uniformity geodesic whose \(j\)-word has at most one change after deleting \(r\) entries from each end.

### The remaining gap

This does not immediately prove \(N_j\): the discarded boundary entries can introduce additional changes.

For \(k=j+2\), \(N_{j+2}\) would imply the existence of a geodesic whose \(j\)-word becomes one-change after deleting its first and last bits. The problem is to control or absorb those two boundary defects.

### Possible mechanism

Directed NOR has arbitrary antipodal starting vertices and global symmetric-difference translation symmetry. Investigate whether one can slide the geodesic, pole chart, or chamber representation so that a boundary defect is moved into the controlled interior while preserving enough of the existing one-change structure.

If this can be iterated, it may prove
\[
N_{k+2}\Longrightarrow N_k,
\]
and hence two descending towers
\[
N_1\leftarrow N_3\leftarrow N_5\leftarrow\cdots,
\qquad
N_2\leftarrow N_4\leftarrow N_6\leftarrow\cdots.
\]

### Opposite-parity caution

There is no equally canonical centered reduction when \(k-j\) is odd. The number of consecutive \(j\)-windows inside a \(k\)-window is then even, and reverse-complement on the resulting local binary word has fixed points. This obstructs a simple binary local function \(f\) satisfying
\[
f(\overline{w^{\rm rev}})=1-f(w)
\]
on all such words.

So the most natural monotonicity question is same-parity descent first.

### Research questions

1. Can one prove \(N_{k+2}\Rightarrow N_k\) by eliminating the two boundary defects?
2. Does global XOR/translation symmetry supply the needed boundary-to-interior transport?
3. Is there a chain-level or Freudenthal interpretation of the centered-window projection that makes descent topological?
4. If full descent fails, what weaker statement about bounded boundary defects follows uniformly in \(k\)?
