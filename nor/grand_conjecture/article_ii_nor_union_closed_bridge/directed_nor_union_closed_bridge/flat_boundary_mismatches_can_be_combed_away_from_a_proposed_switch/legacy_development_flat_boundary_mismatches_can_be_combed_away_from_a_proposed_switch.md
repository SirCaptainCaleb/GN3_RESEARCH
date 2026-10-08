# Flat boundary mismatches can be combed away from a proposed switch — preserved pre-item development

## Composition

(none yet)

## Development


Fix a one-change target word with cut k and polarity s in the coboundary-flat ternary sector. Suppose a current full order agrees with the target on a contiguous interval of window ranks containing the cut.

Let j be the nearest mismatching window immediately to the left of that matched interval. Then window j has the wrong constant-side color while window j+1 has the correct color, so the four consecutive coordinates supporting these two windows carry a transition.

If that tetrahedron is flat, the first-pair endpoint repair replaces the local status pair (wrong,right) by (right,right). The adjacent swap affects only this pair and windows farther to the left; every already-matched window closer to or to the right of the cut remains unchanged. Hence the matched interval expands one rank to the left.

The right-hand statement is the reversed analogue.

Therefore every switch state admits a deterministic outward combing process: repeatedly repair the nearest mismatch on either side whenever its boundary tetrahedron is flat. The process stops only when either every window matches the one-change target, or the maximal matched central band is bracketed on one or both sides by fully-curved tetrahedra.

So a closed repair component can be normalized to a full-support state whose unresolved obstruction consists of fully-curved barriers bounding a target-compatible central band.
