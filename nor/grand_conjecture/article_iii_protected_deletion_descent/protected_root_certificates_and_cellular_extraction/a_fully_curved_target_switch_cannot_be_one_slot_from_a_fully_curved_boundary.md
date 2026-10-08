# A fully-curved target switch cannot be one slot from a fully-curved boundary

## Composition

(none yet)

## Development

## A full-curvature target switch cannot sit one slot from a full boundary

Work in the coboundary-flat ternary sector. Choose a bad switch state with globally maximal target-compatible band length (B), and among those states impose the usual secondary extremality. By the existing mixed-corridor analysis, the target-switch tetrahedron is fully curved. Every unresolved band boundary is also fully curved.

Assume the nearest unresolved boundary lies one transition slot to the right of the target switch. Normalize five consecutive coordinates as
[
0,1,2,3,4
]
and put (B_0=1-A). The local actual status word is
[
alpha(0,1,2)=A,qquad
alpha(1,2,3)=B_0,qquad
alpha(2,3,4)=A.
]
The first transition (A	o B_0) is the desired target switch, and the second transition (B_0	o A) is the first mismatch beyond the matched band.

By assumption both transition tetrahedra
[
{0,1,2,3},qquad {1,2,3,4}
]
are fully curved. Thus this is exactly the double-full singleton packet already solved by the one-sided monotone-resolution theorem.

Choose the resolution preserving the left boundary pair. Swapping only the last pair gives
[
(0,1,2,3,4)longmapsto(0,1,2,4,3)
]
with local status word
[
A,A,B_0.
]
Move the proposed cut one window rank to the right, onto the surviving transition (A	o B_0).

Then every displayed window is target-compatible:
- the first two have the pre-switch target (A);
- the third has the post-switch target (B_0).

Moreover the chosen one-sided resolution preserves the ordered left boundary pair, so every window strictly to the left of the packet is unchanged. The old first boundary mismatch has become matched. Any newly affected window lies strictly to the exported right side, beyond the old boundary.

Therefore the maximal target-compatible band around the moved cut strictly contains the old band: its left extent is unchanged and it includes the old boundary rank. Hence its length is (>B), contradicting global maximality.

The left-boundary version is obtained by reversal.

### Consequence

In a doubly extremal bad state whose target-switch tetrahedron is fully curved, the nearest unresolved fully-curved threshold-band boundary cannot be one transition slot away.

Thus after the existing elimination of all flat-target-switch cases, the first unresolved full-full corridor has width at least two. The width-two local word is
[
A,B_0,B_0,A,
]
with both end transition tetrahedra fully curved; this is the next genuine barrier core.
