# A late t=1 full-flat blocker still gives strict outward defect progress

## Metadata

- ID: a_late_t1_full_flat_blocker_still_gives_strict_outward_defect_progress
- Parent Section: ternary_protected_bridges_and_scan_obstructions
- Position: 30
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development


Consider the residual one-sided E=1 transport issued from an antipodal braid exit. Track the rank j of the exported singleton threshold defect in the protected constant-color phase, and transport it outward by the audited singleton-defect move.

Suppose the first t=1 full-flat blocker is encountered only after m successful one-rank transports, so the defect has moved from rank j to rank j+m.

Use the target-color one-sided resolution of the t=1 full-flat five-set: the resolution which preserves the ordered boundary pair on the outward side and makes the entire five-set monochromatic in the surrounding target color.

By the protected-exit theorem for the full-flat packet, every exterior coordinate on the outward side remains in exactly the same order, and every window strictly beyond the preserved boundary pair is unchanged. If the exit fails to finish, every new threshold mismatch is confined to the two reconnection windows on the inward side of the resolved five-set.

Those two windows lie at most two ranks before the blocked defect position. Therefore every surviving mismatch after the resolution has rank at least

j+m-2.

Consequently:

- if the exit creates no mismatch, the threshold obstruction is finished;
- if m>=3, then j+m-2>j, so even the leftmost surviving defect lies strictly farther outward than the original defect. Thus the minimum outward defect rank is a strict potential despite the possible local reflection.

The mirrored statement holds for the left-moving antipodal exit.

Hence a t=1 full-flat holonomy packet can obstruct monotone defect-position descent only when it is reached after one or two successful elementary transports. All blockers reached after at least three transports either close immediately or give a justified strict outward improvement while preserving the entire outside order on the protected side.

This reduces the remaining combinatorial flat-sector obstruction to the finite short-distance cases m=1 and m=2 for the two antipodal exits.


## Frontier

- Development version when composed: None
- Development version now: 1
