# Uniform buffer blocking alone does not force a farther positive witness — preserved pre-item development

## Development

## Uniform buffer blocking does not by itself force a farther positive witness

The rooted polarization in [[a_blocked_outward_buffer_creates_a_boundary_straddling_common_core_packet]] is genuine, but it cannot by itself close the repair.

Consider a displayed mixed reflected-double status word with left selected endpoint word \(011\) and right selected endpoint word \(001\). Extend the displayed status word farther outward on the left by an arbitrary nonempty block of \(1\)'s, and farther outward on the right by an arbitrary nonempty block of \(0\)'s. Thus schematically the displayed word has the form
\[
1^k\,011\,(\text{positive-word-free corridor})\,001\,0^\ell,
\qquad k,\ell\ge1,
\]
with the interior chosen as in the valid mixed-double classification.

On the left, no positive word begins strictly before the selected \(011\): every such start either begins with \(1\), or lies wholly in the all-\(1\) prefix. In particular neither \(001\), \(011\), nor \(0101\) occurs there. Symmetrically, the all-\(0\) suffix creates no positive occurrence strictly beyond the selected right \(001\).

Now let \(x\) be the selected left exterior vertex and \(c_1,c_2\) the first two corridor vertices. For every outer-prefix vertex \(z\), prescribe
\[
h(z,c_1,c_2)=0,
\]
and hence by boundary antisymmetry
\[
h(c_2,c_1,z)=1.
\]
These prescriptions are compatible with the displayed consecutive status assignments: only the choice \(z=x\) is itself a displayed consecutive triple at the selected occurrence, and it already has value \(0\). For all other \(z\), the prescribed triples are nonconsecutive and may be assigned independently of the displayed status word, together with their boundary reversals. The remaining reversal pairs can be completed arbitrarily.

Therefore one may have simultaneously:

- no farther positive witness on the left in the displayed order;
- every available left buffer blocked;
- every outer-prefix vertex a common reverser of the same rooted edge \(c_2c_1\).

The right-hand mirror can be imposed as well.

This is a counterexample to the repair principle
\[
\text{uniform blocked-side polarization}
\Longrightarrow
\text{farther positive witness}
\]
under positive-word/protection hypotheses alone.

It is **not** asserted to realize the full genuine \(\kappa_2=2\) packet constraints. Consequently it does not challenge the current grand-conjecture route. It identifies exactly what additional information must be used next: deletion-distance-two connector exclusion, packet Hamiltonicity, or exterior-assisted absorption. Pure status-word geometry cannot turn the blocked-side family into the third alternative.
