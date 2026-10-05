# Positive protection allows a disjoint single-sided span-two carrier

## Metadata

- ID: positive_protection_allows_a_disjoint_single_sided_span_two_carrier
- Parent Section: local_witness_topology_and_the_finite_terminal_theorem
- Position: 5
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False
- Provisional declared dependencies: ["verified_five_position_obstruction_and_ordered_tuple_compression", "audit_terminal_surgery_and_compression_use_different_witness_polarities", "explicit_proofs_for_finite_terminal_compression"]

## Cold composition

(none yet)

## Development

## A disjoint single-sided carrier survives positive-word protection

This local construction distinguishes the positive three-word filtration from the dual-polarity filtration. It is not a counterexample to the grand two-cover conjecture.

Take vertices \(0,\ldots,9\) and the proper ordered-partition face
\[
F=\{0\}|\{1\}|\{2\}|\{3\}|\{4,5\}|\{6\}|\{7\}|\{8\}|\{9\}.
\]
Its chambers are
\[
\pi=(0,1,2,3,4,5,6,7,8,9),\qquad
\pi'=(0,1,2,3,5,4,6,7,8,9).
\]
Prescribe the statuses by
\[
\begin{array}{c|rrrrrrrr}
(u,v,w)&012&123&234&345&456&567&678&789\\
h(u,v,w)&0&1&1&1&1&1&0&1
\end{array}
\]
and
\[
h(235)=h(354)=h(546)=h(467)=0.
\]
Assign boundary reverses complementary values and extend all remaining boundary-reversal pairs arbitrarily. These prescriptions are consistent: no displayed ordered triple is the boundary reverse of another displayed triple with the same middle vertex.

Thus
\[
\epsilon(\pi)=01111101,\qquad
\epsilon(\pi')=01000001.
\]

In the first word the only positive forbidden occurrence is \(011\) at start 1. In the second the only positive forbidden occurrence is \(001\) at start 6. Neither word has an occurrence of \(0101\), and neither has \(001\) or \(011\) at any other start.

Here \(m=8\), and the span-two reflection \(i\mapsto m-1-i\) exchanges starts 1 and 6. Their five-vertex determining windows are positions \(1,\ldots,5\) and \(6,\ldots,10\), which are disjoint. The unique common face block is \(\{4,5\}\), contributing one position to each window. The two chambers therefore realize opposite intrinsic orientations of the same unsigned reflected witness edge. Both have no strictly inward positive witness. The face is a pure, protected, disjoint single-sided carrier for the positive-word labeling.

The footprint conclusion holds here:
\[
|B|=2,\qquad\alpha=\beta=1.
\]
What fails is elimination of the remaining two-vertex branch from positive-word protectedness. Across the central swap the four affected statuses change from \(1111\) to \(0000\), while the unaffected neighboring bits remain respectively 1 and 0. Both resulting protected intervals satisfy the positive exact two-cover language.

The dual-polarity predicate excludes this example: \(\epsilon(\pi)\) contains \(110\) at start 5, and \(\epsilon(\pi')\) contains \(100\) at start 2. Those occurrences are inward. This explains exactly why the final disjoint-span-two argument in [[explicit_proofs_for_finite_terminal_compression]] needs the negative patterns.

The ambient tournament has a two-cover by the established ten-vertex theorem. Accordingly this construction refutes only the assertion that disjoint single-sided terminal carriers are eliminated using boundary antisymmetry, face independence, and positive selected-depth protection alone. It does not refute a theorem with an additional global counterexample hypothesis, but any use of that additional hypothesis must be explicit; none is used in the currently displayed local elimination proof.

Together with [[audit_terminal_surgery_and_compression_use_different_witness_polarities]], this rules out silently choosing the positive depth predicate for surgery and the dual predicate for compression. A corrected one-polarity route must handle this surviving branch by outward surgery or a different carrier argument, rather than declaring it impossible.
