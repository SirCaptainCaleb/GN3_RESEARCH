# Audit correction: mixed Hamiltonian weaves obey a binary second-order recurrence

## Metadata

- ID: a_balanced_switching_split_has_an_explicit_monochromatic_spanning_weave
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 358
- Row version: 2
- Development version: 2
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Audit correction: arbitrary run-at-most-two merging is not monochromatic

The original development claimed that, in the switching-normalized split
\[
B\to C,\qquad C=A\cup\{x,z\},
\]
merging directed Hamiltonian paths from \(B\) and \(C\) with no three consecutive vertices from one side makes every ternary window monochromatic.

That claim is false. The mixed-window colors depend on the binary shore pattern.

Let
\[
b_i\to b_{i+1}
\]
be consecutive vertices on the chosen directed Hamiltonian path of \(B\), and similarly for \(C\).

Then:

- for pattern \(BBC\),
\[
\alpha(b_i,b_{i+1},c)
=
1\oplus1\oplus0
=
0;
\]

- for pattern \(BCB\),
\[
\alpha(b_i,c,b_{i+1})
=
1\oplus0\oplus0
=
1.
\]

Likewise \(BCC\) has color \(0\) and \(CBC\) has color \(1\).

Thus a mixed window has:

\[
\boxed{\alpha=1\iff\text{its first and third vertices lie on the same shore}.}
\]

Equivalently, for a binary shore word \(s_1s_2\cdots\), the mixed-window color at rank \(i\) is
\[
s_i=s_{i+2}
\]
interpreted as a bit.

### Valid monochromatic merge patterns

Consequently:

1. the alternating shore pattern
\[
010101\cdots
\]
gives monochromatic color \(1\);

2. the double-run pattern
\[
0011001100\cdots
\]
gives monochromatic color \(0\).

More generally, a monochromatic mixed weave requires the binary shore word to satisfy the second-order recurrence
\[
s_{i+2}=s_i
\]
for color \(1\), or
\[
s_{i+2}=1-s_i
\]
for color \(0\), throughout the mixed region.

Both recurrences keep the two shore counts balanced up to a constant endpoint discrepancy. They do NOT yield the previously claimed ratio-two size bound.

### Correct retained consequence

Uniform dominance still converts the mixed-window problem into a one-dimensional binary recurrence. This is useful: once directed Hamiltonian subsequences on the two shores are fixed, phase compatibility of any interleaving is determined entirely by the shore-pattern word.

The quantitative conclusion
\[
|B|\ge2|A|+7
\]
from the original version is withdrawn.

The viable next route is to splice a one-change binary shore pattern: use one recurrence before the global switch and the other after it, while handling the bounded transition between the two recurrences.

## Frontier

- Development version when composed: None
- Development version now: 2
