# The one-slot mixed flat-full barrier corridor is impossible

## Metadata

- ID: the_one_slot_mixed_flat_full_barrier_corridor_is_impossible
- Parent Section: directed_nor_union_closed_bridge
- Position: 159
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development


Work in the globally maximal threshold-band state of the coboundary-flat ternary sector. Suppose the target switch is flat and the nearest unresolved full-curvature boundary lies exactly one transition slot to the right.

Normalize the five consecutive coordinates as 0,1,2,3,4 and the three local statuses as

alpha(0,1,2)=A,
alpha(1,2,3)=1-A,
alpha(2,3,4)=A.

Thus the first tetrahedron {0,1,2,3} carries the flat target switch, while the second tetrahedron {1,2,3,4} is the full-curvature barrier. The middle status is the matched post-switch color; the last status is the first mismatch beyond the maximal band.

Full curvature of {1,2,3,4} gives

alpha(1,2,4)=A.

By alternation,

alpha(2,4,3)=1-alpha(2,3,4)=1-A.

Now swap the last two coordinates:

(0,1,2,3,4) -> (0,1,2,4,3).

The three local statuses become

A, A, 1-A.

Hence if the target cut is simultaneously moved one window rank to the right, these three windows are all target-compatible.

The swap preserves the ordered left boundary pair (0,1), so every window strictly to the left is unchanged. An adjacent swap of 3 and 4 changes only one further ternary window on the right, namely the first exterior crossing window; that window is complemented because the ordered pair 3,4 is reversed. All farther windows are unchanged.

Therefore the old first mismatch at alpha(2,3,4) is repaired, and any new mismatch can occur only one rank farther outward. The maximal target-compatible band around the moved cut has strictly larger length than before.

This contradicts global maximality of the threshold band.

Consequently a globally maximal bad threshold state cannot have a flat target switch with a full-curvature boundary exactly one transition slot away.

Together with the three-slot exclusion, the only residual flat-target corridor in the doubly extremal normal form is distance two.


## Frontier

- Development version when composed: None
- Development version now: 1
