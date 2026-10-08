# Positive reflected-double carriers have unbounded local spans — preserved pre-item development

## Composition

(none yet)

## Development

## Positive reflected-double carriers can have arbitrarily long determining spans

There is also an unbounded local obstruction to transferring the dual-polarity finite-terminal theorem into the positive-word filtration.

For any \(n\ge10\), put \(m=n-2\) and prescribe the status word
\[
w_n=0\,1^4\,0^{\,n-8}\,1.
\]
Its only occurrences of \(\{001,011,0101\}\) are \(011\) at start 1 and \(001\) at start \(m-2\). These starts are exchanged by the span-two reflection \(i\mapsto m-1-i\).

Let the source face have singleton blocks except for one two-vertex block at positions 4 and 5. Its two chambers differ only by that adjacent swap. Prescribe the word \(w_n\) in both chambers.

This is realizable by a boundary tournament. A triple unaffected by the swap has the same prescription in both chambers. For affected triples, the only repeated unordered triple supports are those containing both swapped vertices and one fixed neighbor; the two orders have different middle vertices, so they belong to different boundary-reversal pairs. An adjacent swap cannot itself be a boundary reversal of a three-vertex order. Thus all prescriptions are consistent and extend arbitrarily to the remaining reversal pairs.

Both chambers have both reflected positive occurrences, and no other positive forbidden occurrence. If the permitted external tie-break sign is the relative order of the two vertices in the nonsingleton block, the two labels are opposite orientations of the same unsigned witness edge. This is a pure balanced carrier, protected against every inward positive witness.

The two five-vertex determining windows are positions \(1,\ldots,5\) and \(n-4,\ldots,n\); their full determining span has order \(n\). Thus positive selected-depth protectedness and local face symmetry alone do not bound reflected-double determining spans by ten.

As in the disjoint single-sided example, the dual-polarity predicate excludes this construction: the central transition from the run of ones to zeros produces \(110\) and \(100\) strictly inward. The distinction is therefore exactly the one identified in [[audit_terminal_surgery_and_compression_use_different_witness_polarities]].

This family is a local counterexample to a stronger compression statement, not a counterexample to the grand conjecture. No claim is made that its arbitrary extensions lack a two-cover. If the finite-terminal theorem is meant only under a global no-two-cover assumption, that assumption must do substantive work beyond the displayed local arguments.

The single-sided adjacency lemma cannot repair this branch, since its essential equation \(L+R=1\) is replaced here by \(L=R=1\). A one-polarity repair must therefore treat the external-gauge reflected-double branch separately, use the global counterexample hypothesis explicitly, or change the witness encoding with a proved dimension and equivariance analysis.
