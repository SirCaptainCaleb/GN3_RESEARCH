# A rigid width-two residue reduces to one reconnection bit or a double-full singleton

## Metadata

- ID: a_rigid_width_two_residue_reduces_to_one_reconnection_bit_or_a_double_full_singleton
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 226
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## A rigid width-two residue exports only one reconnection bit, and the bad bit is a double-full singleton

Work in the coboundary-flat alternating ternary sector and continue from the rigid terminal width-two table on coordinates
[
(0,1,2,3,4,5)
]
with local word
[
0,1,1,0.
]
The rigid table includes
[
alpha(0,3,1)=0,qquad
alpha(3,1,2)=1,qquad
alpha(1,2,4)=1,qquad
alpha(2,4,5)=1.
]
Indeed (alpha(0,3,1)=1-alpha(0,1,3)=0), while ((3,1,2)) is a cyclic permutation of ((1,2,3)).

Consider the six-coordinate weave
[
(0,3,1,2,4,5).
]
Its status word is exactly
[
0,1,1,1.
]

This weave is stronger than the earlier right-preserving weave ((2,3,0,1,4,5)): it preserves both

- the first coordinate (0), and
- the ordered right boundary pair ((4,5)).

Hence, if the old corridor sits after an exterior prefix
[
ldots,p,q,0,1,2,3,4,5,ldots,
]
then every window strictly to the right is unchanged, the old crossing window (alpha(p,q,0)) is unchanged, and the only new left reconnection window is
[
r:=alpha(q,0,3).
]
Thus the new local word, including the unique reconnection bit, is
[
r,0,1,1,1,
]
with all farther left matched windows unchanged.

### If (r=0), the rigid barrier is removed

When (r=0), the whole displayed packet is target-compatible with the switch between the (0) and the first (1). Therefore the old width-two full-full boundary has been crossed without disturbing either exterior beyond the single replaced crossing window.

### If (r=1), the obstruction is exactly a double-full singleton

The old left crossing window satisfies
[
alpha(q,0,1)=0
]
because it lies in the matched pre-switch band. The rigid table gives
[
alpha(0,1,3)=1.
]
Hence on the tetrahedron ({q,0,1,3}) the old ordered transition
[
(q,0,1,3)
]
has status word (0,1).

Now (r=alpha(q,0,3)=1). For a coboundary-flat transition (0	o1), this is the fully-curved off-face value (the flat value would be (0)). Thus this tetrahedron is fully curved. Reordering it as
[
(q,0,3,1)
]
gives the first two statuses
[
1,0.
]

The next transition in the new weave is
[
alpha(0,3,1)=0,qquad alpha(3,1,2)=1.
]
Its tetrahedron is also fully curved: in the ordering ((0,3,1,2)), the off-face
[
alpha(0,3,2)=1-alpha(0,2,3)=1
]
is the fully-curved value for a (0	o1) transition (and (alpha(0,1,2)=0) is the complementary off-face).

Therefore the five consecutive coordinates
[
(q,0,3,1,2)
]
carry the exact double-full singleton word
[
1,0,1
]
with both transition tetrahedra fully curved.

By the proved double-full singleton theorem, this packet has a one-sided monotone resolution preserving the ordered right boundary pair. Consequently the rigid width-two residue has only two outcomes:

1. the single reconnection bit is (0), and the width-two barrier is crossed immediately; or
2. the bit is (1), and the residue hands off canonically to the already-controlled double-full singleton, with all further risk exported to the left and the entire right exterior preserved.

### Consequence

A rigid width-two full-full corridor is not a new terminal species and does not require a separate reflection-recurrence analysis. After the stronger weave ((0,3,1,2,4,5)), its unresolved content is at most one reconnection bit; the bad value of that bit is precisely an existing double-full singleton gadget.

Thus the closure problem after a rigid width-two encounter returns to the established one-sided threshold-band transport on the exported side. Any remaining obstruction must come from the termination of that exported transport, not from the six-set itself.

## Frontier

- Development version when composed: None
- Development version now: 1
