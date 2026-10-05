# Independent audit: switch-span Proposition 6.3 gap

## Metadata

- ID: independent_audit_switch_span_proposition_6_3_gap
- Parent Section: convex_root_balance_and_bourgin_yang
- Position: 3
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Independent audit: switch-span Proposition 6.3 is not proved

The current proof of Proposition 6.3,
\[
b(\pi)-a(\pi)\ge3
\]
for every spanning order of a counterexample, is invalid as written.

The argument says that if the first-to-last switch span is at most two, “a cut immediately after the short middle run” splits the order into two monochromatic blocks, each having a tight orientation. This does not follow from the status word.

For example, the status word
\[
0110
\]
has first switch at position \(1\) and last switch at position \(3\), so
\[
b-a=2.
\]
Nevertheless no cut of this displayed order satisfies the exact inversion-window criterion: here
\[
p=1,\qquad q=3,
\]
so \(q>p+1\). Equivalently, the forbidden pattern \(011\) is already present. Directly checking the possible cuts also shows that no cut makes the left inherited statuses all tight and the reversed right inherited statuses all tight.

This example does not refute the proposition under the additional global hypothesis that \(H\) is a counterexample; the proposition might conceivably admit a different proof using more structure. It does refute the stated local justification, so the claimed consequence
\[
\dim\Phi^{-1}(0)\ge5
\]
from the extreme-switch map is presently unsupported.

The later exact-inversion-root route does not need Proposition 6.3: its dimension saving comes directly from the exact deficiency \(\delta=q-p-1\). Thus this defect is nonfatal to the current intended endgame, but Article VII should not treat Proposition 6.3 as audited until repaired or removed.
