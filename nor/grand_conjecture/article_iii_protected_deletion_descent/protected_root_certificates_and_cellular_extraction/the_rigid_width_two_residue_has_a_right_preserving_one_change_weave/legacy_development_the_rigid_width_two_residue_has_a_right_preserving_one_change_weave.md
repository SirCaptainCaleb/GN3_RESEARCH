# The rigid width-two residue has a right-preserving one-change weave — preserved pre-item development

## A one-sided splice for the rigid width-two six-set

Continue from the rigid terminal width-two table on coordinates {0,1,2,3,4,5}. In increasing orientation the needed values include
alpha(0,2,3)=0,
alpha(0,1,3)=1,
alpha(0,1,4)=1,
alpha(1,4,5)=1.

Consider the full-support six-coordinate order
(2,3,0,1,4,5).

Its consecutive ternary statuses are
alpha(2,3,0)=alpha(0,2,3)=0
by cyclic invariance,
alpha(3,0,1)=alpha(0,1,3)=1
by cyclic invariance,
alpha(0,1,4)=1,
alpha(1,4,5)=1.

Hence its local word is exactly
0,1,1,1.

Place the target switch between the first and second displayed window ranks. The entire six-coordinate packet is target-compatible.

### Right boundary is preserved exactly

The old rigid corridor uses the order
(0,1,2,3,4,5).
The new weave ends in the SAME ordered pair
(4,5).

Therefore every ternary window strictly to the right of the six-coordinate packet, including the first crossing window (4,5,r) with the next exterior coordinate r, is literally unchanged.

On the left, the old ordered pair (0,1) is replaced by (2,3). Thus only the two ternary windows crossing the left edge of the packet can change.

### One-sided splice theorem

A rigid width-two full-full residue admits a replacement by a locally one-change six-coordinate order that:
- preserves the entire right exterior exactly;
- makes every internal six-set window target-compatible;
- confines all reconnection risk to at most two windows on the LEFT.

By reversal there is the mirror statement for a rigid width-two residue approached from the left: one may preserve its left exterior and export all risk to at most two right reconnection windows.

### Consequence

The rigid six-set is not a terminal internal obstruction. It is a one-sided splice gadget. Any surviving obstruction after splicing is a bounded two-window reconnection defect on the opposite side.

This does not by itself prove global maximal-band improvement, because the exported side may lose previously matched windows. The correct next step is to classify the two-window reconnection packet using the existing endpoint/neighbor-replacement/threshold-band laws, not to treat the six-set as a recurrent reflection state.
