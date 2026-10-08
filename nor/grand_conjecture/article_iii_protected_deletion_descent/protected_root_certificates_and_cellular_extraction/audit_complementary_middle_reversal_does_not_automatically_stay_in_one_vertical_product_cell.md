# Audit: complementary middle reversal does not automatically stay in one vertical product cell

## Composition

(none yet)

## Development

## Audit of the top-cell complementary-middle claim

The reversal calculation behind the top-cell complementary-middle lemma is correct, but its same-product-cell conclusion needs a vertical-locality hypothesis.

Take a violating ternary window (u,m,v) of color c at window rank i, with honest side sign s. Reversing the triple gives (v,m,u), whose color is 1-c by alternation and whose physical root is the opposite root.

If one also places the reversed window on the opposite threshold side, the threshold target flips from T to 1-T. Since c != T implies 1-c != 1-T, the reversed state is again a violation, with the same middle m and opposite side sign. Thus the desired complementary signed-middle state certainly exists somewhere in the full switch prism.

What is not automatic is that it lies in the SAME product carrier cell.

The top permutahedron factor removes the chamber obstruction: when the supporting permutahedron face is the top face, both local coordinate orders may be realized in that physical face. But the switch-prism factor also contains the vertical cut coordinate. To move a window from the pre-switch side to the post-switch side, the cut must cross that window rank. If the selected violation lies distance d from the active cut, this can require d cut-level moves.

A local vertical product cell over one adjacent cut edge contains only neighboring cut levels. Therefore a violation far from the cut cannot in general be moved to the opposite side while remaining in that same vertical cell.

### Corrected lemma

The complementary-middle reversal is same-cell whenever the tracked violating window is cut-adjacent in the active vertical cell, so that crossing the one vertical edge moves that window from one threshold side to the other.

More generally it is same-cell only for a carrier construction whose vertical cell explicitly contains both required cut levels; that stronger carrier property must be proved rather than inferred from the top permutahedron factor.

### Consequence

The sign-separated-middle reduction remains nontrivial. One cannot combine it with the unqualified top-cell complementary-middle sentence to conclude that every full-dimensional figure-eight/theta circuit is immediately extractable.

A promising closure target is now precise: force a repeated middle fiber to become cut-adjacent, or transport that fixed middle through the intervening threshold band without losing its sign/provenance. This reconnects the full-dimensional lifted-circuit frontier to the already-developed fixed-middle threshold-band transport problem rather than bypassing it by reversal alone.
