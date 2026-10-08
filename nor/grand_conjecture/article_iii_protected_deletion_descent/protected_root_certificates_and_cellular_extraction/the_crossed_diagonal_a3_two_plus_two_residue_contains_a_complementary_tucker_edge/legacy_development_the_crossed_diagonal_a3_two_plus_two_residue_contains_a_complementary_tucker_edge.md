# The crossed-diagonal A3 two-plus-two residue contains a complementary Tucker edge — preserved pre-item development

## Composition

(none yet)

## Development

Work in one exact ternary A3 block and the no-internal-switch-chamber branch of root 101. After global color complementation if necessary, label the four block coordinates
1<2<3<4
so every increasing triple has color 0. Normalize the switch target to 0 on the pre side and 1 on the post side.

A side-balanced lifted A3 zero necessarily uses both internal block-window ranks, so the switch lies between those two ranks: a pre-side internal label is carried by the first three block positions, while a post-side internal label is carried by the last three.

Root 101 shows that the only residual 2+2 support-minimal geometry is two same-side reversal pairs on the crossed diagonals {1,3} and {2,4}, with opposite side signs.

Consider the pre-side pair on diagonal 1<->3. In the transitive pattern, the color-1 realizations of this reversal pair are
(1,4,3)
and
(3,2,1).
Take the first. Since it is pre-side, it is realized in the chamber
(1,4,3,2),
where its middle coordinate 4 occupies the first internal window.

Swap the adjacent pair 4,3. The chamber becomes
(1,3,4,2).
Now the SAME tracked middle coordinate 4 occupies the second internal window, namely
(3,4,2).
Relative to the increasing triple (2,3,4), the order (3,4,2) is an even cyclic permutation, so its color is 0.

Thus:
- before the swap, the 4-centered internal window is a pre-side violation because its color is 1 while the pre target is 0;
- after the swap, the 4-centered internal window is a post-side violation because its color is 0 while the post target is 1.

Therefore this single genuine adjacent-transposition edge carries the complementary signed-middle pair
+4 and -4.

By the signed-middle Tucker edge theorem, the edge is an actual switch-crossing endpoint repair. No exterior window, changed-middle argument, or arbitrary face path is needed.

Hence the canonical crossed-diagonal 2+2 residue of root 101 is not terminal.

By symmetry/global color complement the same conclusion holds for the opposite assignment of transitive face color and for either choice of which diagonal pair lies on the pre side.

Consequently the remaining support-minimal honest lifted A3 frontier excludes:
- two-term reversal pairs;
- side-balanced simple four-cycles;
- the crossed-diagonal 2+2 no-switch-chamber residue.

What remains from root 101 is only the coupled case of oppositely side-imbalanced simple cycles with at least one triangle.
