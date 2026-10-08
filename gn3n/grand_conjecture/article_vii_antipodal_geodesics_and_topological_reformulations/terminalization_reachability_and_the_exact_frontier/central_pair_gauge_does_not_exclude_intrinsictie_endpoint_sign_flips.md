# Central-pair gauge does not exclude intrinsic–tie endpoint sign flips

## Composition

(none yet)

## Development

## A fixed central gauge does not make all endpoint factors sign-neutral

The central-pair tie-break in [[central_pair_gauge_removes_endpoint_block_sign_changes]] is odd and does eliminate flips of the gauge itself under endpoint exchanges. Its stronger sign-localization conclusion needs an additional hypothesis: an endpoint swap may change whether the chamber is a tie case or a unique-orientation case, even though the gauge is unchanged.

For any \(n\ge10\), use the positive reflected span-two starts 1 and \(m-2\), with \(m=n-2\). Consider a two-chamber face with a nonsingleton block at vertex positions 1 and 2 and all other blocks singleton. Prescribe the words
\[
w=0\,1^4\,0^{n-8}\,1,\qquad
w'=1\,1^4\,0^{n-8}\,1.
\]
Only the first status changes under the swap. These prescriptions are consistent with a boundary tournament: the affected triples have different middle vertices or different supports, and no conflicting boundary-reversal pair is prescribed. Unspecified reversal pairs can be oriented arbitrarily.

The first chamber has both reflected positive span-two occurrences: \(011\) at start 1 and \(001\) at start \(m-2\). The second has only the right occurrence. Both words have no positive forbidden occurrence on any strictly more central edge.

The central symmetric pair of vertex positions has the same occupants in both chambers. Choose the fixed vertex order so that the tie-break in the first chamber has the left intrinsic sign. Then the labels are:
\[
\ell(\pi)=+e \quad\text{(both occurrences, central tie-break)},\qquad
\ell(\pi')=-e \quad\text{(right occurrence only)}.
\]
The gauge itself has not changed. Nevertheless the first-position endpoint swap is a terminal sign-flip edge.

This is again a local counterexample, not a counterexample to the grand conjecture. It shows that the claim “a gauge-induced flip meets the central pair” does not account for transitions between the intrinsic and tie regimes. The actual label can flip at a determining-window endpoint while the central gauge stays fixed.

For branches where protectedness excludes coexistence altogether, the intrinsic persistence argument remains valid: a sign-flip edge must affect both determining occurrences. The new positive alternating results supply that condition for sufficiently separated alternating windows. The positive span-two double branch does not satisfy it.

Thus the central-pair gauge can be retained, but unbounded endpoint factors cannot be discarded from the span-two double analysis merely because they preserve the gauge. A repair must control intrinsic/tie transitions or replace the orientation rule with one whose complete sign-localization theorem is proved.
