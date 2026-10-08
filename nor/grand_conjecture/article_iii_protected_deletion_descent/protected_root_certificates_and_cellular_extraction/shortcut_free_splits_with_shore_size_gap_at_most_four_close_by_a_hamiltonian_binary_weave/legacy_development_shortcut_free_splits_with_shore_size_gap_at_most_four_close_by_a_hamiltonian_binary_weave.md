# Shortcut-free splits with shore-size gap at most four close by a Hamiltonian binary weave — preserved pre-item development

## Development

## Shortcut-free splits with shore-size gap at most four close by a Hamiltonian binary weave

Use the switching-normalized shortcut-free split
\[
B\to z\to A\to x
\]
and put
\[
C=A\cup\{x,z\}.
\]
Then
\[
B\to C.
\]

Choose directed Hamiltonian paths
\[
b_1\to\cdots\to b_m
\]
in \(B\), and
\[
c_1\to\cdots\to c_n
\]
in \(C\), where
\[
m=|B|,\qquad n=|A|+2.
\]

Merge the two paths while preserving their internal orders. Whenever every length-three window is mixed, its color depends only on its binary shore pattern:

- \(BBC\) and \(BCC\) have color \(0\);
- \(BCB\) and \(CBC\) have color \(1\).

Equivalently,
\[
\alpha_i=1\iff s_i=s_{i+2}
\]
for the binary shore word \(s_1s_2\cdots\).

### Equal counts and excess one

If
\[
|m-n|\le1,
\]
use a purely alternating shore word, beginning and ending on the larger side when the counts differ by one:
\[
BCBC\cdots
\]
or
\[
CBCB\cdots.
\]

Every length-three shore pattern is \(BCB\) or \(CBC\), so every ternary window has color \(1\). The resulting spanning order is monochromatic.

### Excess two

Suppose
\[
m=n+2.
\]
Use an alternating merge of \(n+1\) vertices from each side beginning and ending with \(B\), then append the final \(B\)-vertex:
\[
BCBC\cdots B\,B.
\]

All windows before the last are alternating and have color \(1\). The unique final window has shore pattern
\[
CBB
\]
and therefore color \(0\).

Hence the ternary word is
\[
1\cdots10,
\]
with exactly one change.

The case
\[
n=m+2
\]
is symmetric.

Therefore
\[
\boxed{|m-n|\le2\Longrightarrow\text{a spanning NOR-good merge exists}.}
\]

Substituting
\[
m=|B|,
\qquad
n=|A|+2,
\]
and using \(|A|\le|B|\), gives
\[
|B|-|A|\le4
\Longrightarrow
\text{NOR closes}.
\]

Thus every surviving shortcut-free split in a minimum counterexample satisfies
\[
\boxed{|B|\ge |A|+5.}
\]

### Scope

This conclusion uses only:

- the universal dominance \(B\to C\);
- directed Hamiltonian paths in the two induced tournaments;
- the alternating ternary identity.

No connector parity or curvature calculation is needed.

When the shore gap is at least five, any binary merge of the two Hamiltonian paths with no three consecutive vertices from one side has too few minority vertices to cover the larger side. Further closure must then exploit actual ternary structure inside a run of at least three vertices of the large shore.
