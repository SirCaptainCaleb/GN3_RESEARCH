# Audit adjacent swap transport omitted a fourth changed status — preserved pre-item development

## Composition

(none yet)

## Development

## Audit: adjacent-swap transport omitted a fourth changed status

Two recent subsections overstated the effect of an adjacent coordinate swap:
- "Adjacent swapping across a fully curved transition toggles the two outer change bits";
- "Non full transitions transport by two or annihilate".

The issue is that in ternary memory, swapping two adjacent coordinates changes up to four consecutive status windows, not three.

For a local order
[
(ldots,a,b,c,d,q,r,ldots)
]
and the swap (c,d), the old affected windows are
[
(a,b,c),quad (b,c,d),quad (c,d,q),quad (d,q,r).
]
After the swap they are
[
(a,b,d),quad (b,d,c),quad (d,c,q),quad (c,q,r).
]

The first three new colors can be related to the old tetrahedral data and reversal:
[
alpha(a,b,d),qquad
1-alpha(b,c,d),qquad
1-alpha(c,d,q).
]
But the fourth new color
[
alpha(c,q,r)
]
is not determined by the old fourth color
[
alpha(d,q,r)
]
without additional information.

Therefore the exact claims that only two outer transition bits toggle, or that a successful non-full repair transports a transition by exactly two slots, are unsupported.

### What survives

The local endpoint-repair theorem remains valid:
for a transition on ((a,b,c,d)), at least one of the two endpoint swaps removes the **central** transition unless the tetrahedron is fully curved. That statement depends only on the four face colors of the tetrahedron.

Likewise, a fully-curved tetrahedron remains a universal switch gadget, and the unique-predecessor extension theorem remains valid.

### Corrected closure obligation

To turn a local endpoint repair into a decrease of global cyclic variation, one must control the additional far-side boundary window created by the adjacent swap. This is exactly analogous to the reconnection-zone issue in full interval reversal. Any future transport lemma must retain the full four-window swap packet, not truncate it to the tetrahedral core.
