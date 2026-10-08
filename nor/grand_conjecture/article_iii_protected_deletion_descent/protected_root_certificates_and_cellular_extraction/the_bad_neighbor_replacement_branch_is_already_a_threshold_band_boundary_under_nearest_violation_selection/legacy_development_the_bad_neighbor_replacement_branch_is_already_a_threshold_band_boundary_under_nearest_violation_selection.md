# The bad neighbor-replacement branch is already a threshold-band boundary under nearest-violation selection — preserved pre-item development

## Composition

(none yet)

## Development

Use the corrected four-window neighbor-replacement notation. On the pre-switch side let the tracked b-centered defect be at rank t+1<=k and suppose the proposed neighbor-disappearance move has B=C=0, the exceptional case where the fixed-cut potential need not improve.

Assume the tracked defect was chosen by nearest-violation selection. Then every pre-switch rank strictly between t+1 and the cut k is satisfied; otherwise a closer pre-side violation would have been selected. Thus ranks t+2,...,k all equal the pre target eta.

The tracked rank t+1 has color 1-eta. Therefore, reading toward the cut, the adjacent pair consisting of rank t+1 and the first matched rank t+2 (when t+1<k) is exactly a mismatch-to-match boundary. After global color complementation if necessary it is a 10 transition bounding a target-compatible band that reaches the cut.

Hence the B=C=0 branch is already in the audited threshold-band geometry. Do NOT perform the neighbor replacement whose potential may increase. Instead stop the chamber path and take the maximal target-compatible band containing the cut and extending through ranks t+2,...,k and the already matched opposite-side portion.

At its pre-side boundary:
- if the boundary tetrahedron is flat in the outward direction, the threshold-band repair preserves the whole matched band and moves the boundary defect strictly one rank farther from the cut;
- if it is fully curved, it is already a terminal protected barrier.

Repeated flat repairs strictly enlarge the matched band, so they terminate either in a spanning one-change state or at a fully-curved barrier.

If t+1=k, the tracked defect is cut-adjacent. Then a single vertical cut move across that rank flips its target and removes the defect directly, so the exceptional neighbor move is again unnecessary.

The post-switch reflected case is identical.

Therefore nearest-violation complementary-cell extraction has a corrected local rule for every neighbor-disappearance event:
1. if B+C>=1, use the sharp lexicographic descent theorem;
2. if B=C=0, abandon the neighbor swap and enter the terminating threshold-band dichotomy;
3. if the defect is cut-adjacent, use the vertical cut repair.

This repairs the specific gap exposed by the four-window audit. It still leaves the common downstream obstruction of a fully-curved terminal barrier, but no uncontrolled neighbor-replacement step is needed.
