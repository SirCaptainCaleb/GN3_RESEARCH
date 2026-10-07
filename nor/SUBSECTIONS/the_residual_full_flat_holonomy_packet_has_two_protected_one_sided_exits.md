# The residual full-flat holonomy packet has two protected one-sided exits

## Metadata

- ID: the_residual_full_flat_holonomy_packet_has_two_protected_one_sided_exits
- Parent Section: ternary_protected_bridges_and_scan_obstructions
- Position: 27
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## The residual full-flat holonomy packet has two protected one-sided exits

Normalize the five consecutive coordinates as
[
0,1,2,3,4
]
with singleton-defect word
[
alpha(0,1,2)=0,qquad
alpha(1,2,3)=1,qquad
alpha(2,3,4)=0.
]
Assume the left transition tetrahedron is fully curved, the right transition tetrahedron is flat, and the residual holonomy is
[
t=alpha(0,1,4)=1.
]

The full/flat identities give the increasing-order triangle table
[
012=0, 013=1, 014=1, 023=0, 024=0, 034=0,
]
[
123=1, 124=1, 134=0, 234=0.
]

Then there are two complementary one-sided resolutions.

### Right-boundary-preserving exit

The order
[
(1,2,0,3,4)
]
has statuses
[
alpha(1,2,0)=0,qquad
alpha(2,0,3)=0,qquad
alpha(0,3,4)=0.
]
Thus it is monochromatic in color 0 and ends in the original ordered right boundary pair ((3,4)). Every exterior ternary window strictly to the right is therefore unchanged. Any failure of this exit is confined to the two left reconnection windows.

### Left-boundary-preserving exit

The order
[
(0,1,4,3,2)
]
has statuses
[
alpha(0,1,4)=1,qquad
alpha(1,4,3)=1,qquad
alpha(4,3,2)=1.
]
Thus it is monochromatic in color 1 and starts in the original ordered left boundary pair ((0,1)). Every exterior ternary window strictly to the left is unchanged. Any failure of this exit is confined to the two right reconnection windows.

### Interpretation

The residual t=1 full-flat packet is not a terminal local wall. It is another protected two-exit cell: one exit preserves the right boundary and resolves the packet in the old 0-color, while the other preserves the left boundary and resolves it in the opposite color.

For the color-complemented pattern (1,0,1), the same statement holds with colors interchanged. Thus the final combinatorial task is not local existence of a resolution, but to classify the two exported boundary packets and prove that at least one gives a strict protected improvement rather than reflecting the E=1 defect back into the same transport tube.

## Frontier

- Development version when composed: None
- Development version now: 1
