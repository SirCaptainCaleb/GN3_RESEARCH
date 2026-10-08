# Audit: alternate-middle A3 extraction changes the tracked Tucker coordinate — preserved pre-item development

## Composition

(none yet)

## Development

## Audit: the alternate-middle reduction changes the tracked middle coordinate

Subsection 98 claims that every honest lifted A3 zero contains a controlled repair. Its local cycle calculations are useful, but the first reduction step does not currently justify invoking the arbitrary complementary-cell extraction theorem.

The reduction says: for an oriented physical edge u->v, if a selected violating window (u,m,v) has the alternative middle window (u,m',v) satisfied at the same internal rank, connect the two chamber states inside the product cell; then the tracked violation must first disappear, so the arbitrary-cell extraction theorem yields a controlled repair.

The issue is that the arbitrary-cell theorem tracks one FIXED middle coordinate b along a path. Here the initial defect is centered at m, while the terminal satisfied window is centered at m'. Satisfaction of (u,m',v) says nothing by itself about the status of the m-centered window in the terminal chamber.

This distinction matters in an A3 Coxeter block embedded in a larger coordinate order. Replacing the internal middle m by the fourth block coordinate m' pushes m to a block boundary, not necessarily to a global endpoint. The new m-centered ternary window may then use one exterior coordinate. It can remain a violation on the same switch side. In that case there is no guaranteed first disappearance or side change of the FIXED signed-middle label m, so root 81 cannot yet be invoked.

Therefore the implication

"one alternative middle is satisfied" => "the cell contains a controlled repair"

needs an additional boundary-provenance statement. A sufficient repair would be one of:

1. construct a path whose terminal state has the original middle m globally uncentered or provably satisfied;
2. prove a block-boundary handoff theorem controlling the exterior m-centered window when m exits the A3 block interior;
3. replace fixed-middle Tucker extraction by a carrier whose label is the physical endpoint root rather than the middle coordinate and prove the corresponding local path theorem.

What remains valid from Subsection 98 without this step:

- conditional on BOTH possible middle triples being violations for every edge of a simple directed cycle, the triangle calculation contradicts coboundary flatness;
- under the same condition a repair-free directed four-cycle has all four violations on one side;
- the two-cycle algebra forces opposite sides.

But those conditional calculations do not establish that arbitrary lifted A3 zeros satisfy the "both middles violate" hypothesis whenever no legal repair exists.

Independent progress survives this audit. Subsection 101 proves directly, without changing the tracked middle, that any side-balanced simple A3 four-cycle forces an internal switch-compatible chamber. It also identifies the no-internal-chamber 2+2 residue as the crossed-diagonal packet. Thus the safe A3 frontier remains narrower than before, but A3 should not yet be declared completely extracted from the alternate-middle argument alone.
