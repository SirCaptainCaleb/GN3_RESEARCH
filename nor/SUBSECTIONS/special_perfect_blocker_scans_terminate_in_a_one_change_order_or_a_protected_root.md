# Special perfect-blocker scans terminate in a one-change order or a protected root

## Metadata

- ID: special_perfect_blocker_scans_terminate_in_a_one_change_order_or_a_protected_root
- Parent Section: ternary_protected_bridges_and_scan_obstructions
- Position: 60
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

Under the special perfect-blocker hypotheses, the last-holonomy-drop analysis now terminates completely. Endpoint positions j=1,2 close with spanning one-change orders and j=3 gives a one-change deletion carrier. For j>=4, middle-coordinate deletion either closes immediately or leaves one earlier defect; forced repairs then either hit a fully-curved protected root or create a contiguous 1-band whose right boundary advances monotonically by the threshold-band potential. Hence the special branch always produces a one-change full/deletion order or a protected physical root; no local recurrence remains.

## Development

Under the special perfect-blocker hypotheses, choose the last holonomy drop. The endpoint cases j=1,2 give a spanning one-change order, and j=3 gives a one-change deletion carrier. For j>=4, delete v_{j-2}; the recursive 010 packet collapses to 00 and the only new left bit is h_{j-4}. If that bit is 0, a one-change deletion carrier results. If it is 1, a forced forward repair leads either immediately to a fully-curved protected root when lambda=1, or, when lambda=0, to a contiguous 1-band inside the old zero phase. The audited threshold-band potential then strictly advances the right edge of this band through every flat boundary. Hence the finite process ends either when the band reaches the original one phase, giving a global one-change word, or at a fully-curved boundary carrying a protected physical root. Thus recurrent local transport is eliminated in the special scan branch. This conclusion uses the special scan and its holonomy/full-curvature provenance and does not apply to arbitrary blocking scans.
