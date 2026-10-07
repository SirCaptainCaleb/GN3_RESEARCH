# Audit: the claimed one-holonomy closure has an orientation-parity error

## Metadata

- ID: audit_the_claimed_one_holonomy_closure_has_an_orientation_parity_error
- Parent Section: directed_nor_union_closed_bridge
- Position: 129
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Audit: subsection 127's claimed closing order has a parity error

Subsection 127 claimed that in the normalized double-full singleton five-set with
alpha(0,1,2)=0,
alpha(1,2,3)=1,
alpha(2,3,4)=0,
and residual bit t=0, the order
(1,2,0,3,4)
is monochromatic 0.

This is false.

From the fully-curved left tetrahedron one has
alpha(0,2,3)=0.
The second status of the proposed order is
alpha(2,0,3).
The permutation taking (0,2,3) to (2,0,3) is a single transposition, so alternation gives
alpha(2,0,3)=1-alpha(0,2,3)=1.
Thus the proposed word begins
0,1,...
rather than 0,0,...

Indeed:
alpha(1,2,0)=alpha(0,1,2)=0 by cyclic invariance,
alpha(2,0,3)=1,
and when t=0,
alpha(0,3,4)=t=0.
So the actual internal word is
0,1,0,
not monochromatic.

Therefore subsection 127 does not close the t=0 holonomy class, and its conclusion that every all-four-curved counterexample is forced into t=1 is unsupported.

The valid local cancellation statements remain those of subsections 123--125: the five-set does admit monochromatic reorderings, but they change boundary pairs and require reconnection analysis. Any argument that uses 127's holonomy elimination must be withdrawn unless repaired with a different block order whose statuses are checked with full permutation parity.

This audit restores both residual five-set classes as live possibilities in the all-curved terminal state.

## Frontier

- Development version when composed: None
- Development version now: 1
