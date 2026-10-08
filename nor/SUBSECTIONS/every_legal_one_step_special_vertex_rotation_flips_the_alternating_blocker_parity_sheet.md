# Every legal one-step special-vertex rotation flips the alternating-blocker parity sheet

## Metadata

- ID: every_legal_one_step_special_vertex_rotation_flips_the_alternating_blocker_parity_sheet
- Parent Section: hartman_least_unreachable_connectors
- Position: 24
- Row version: 2
- Development version: 2
- Composition version: 1
- Composition stale: False

## Composition

A realized ambient one-step special-vertex rotation flips χ=|i_z−i_x|+σ_x+σ_z mod 2; its path-normalizing special switch bit is unchanged in the local calculation. This excludes perfect alternation on the new sheet, but does not prove a thick wall, legal collar deletion, or a terminating repair sequence. Exterior-window checks and the unresolved equal-one barrier remain.

## Development

Use the special parity
chi = |i_z-i_x| + sigma_x + sigma_z mod 2
from the preceding subsection, where sigma is the path-normalizing switching vector.

Consider the legal right motion of x from the A2 rotation law:
(p,a,x,b,c) -> (p,b,a,x,c).
For a zero connector in the fixed switching-normalized split, the old adjacent edges satisfy
p->a, a->x, x<-b, b->c.
Hence along the old path-normalizing switching,
sigma_p=sigma_a=sigma_x
and
sigma_b=sigma_c=1-sigma_x.

The right rotation is legal exactly in the branch p->b and c->a. Along the new order
p,b,a,x,c,
all first three adjacent edges are forward in the fixed representative and x<-c. Fix the global complement by keeping sigma'_p=sigma_p. The path-normalizing recurrence then gives
sigma'_x=sigma_p=sigma_x.
Thus x moves one position while its switching bit is unchanged. Therefore chi flips.

The left rotation
(p,a,x,b,c) -> (p,x,b,a,c)
is symmetric. In its legal branch b->p and a->c, fixing sigma'_p=sigma_p again gives sigma'_x=sigma_x, while the position of x changes by one. Hence chi flips there as well.

The same calculation applies to z by the symmetric special-vertex rotation law.

Consequently any realized one-step motion of either special vertex moves the connector between the two special-parity sheets. In particular a perfectly alternating blocker, which can occur only on chi=1, is destroyed as a wall-free blocker after one legal special motion: on the chi=0 state it must acquire a nonthin transition between x and z.

Therefore the exceptional alternating-blocker class is terminal only if both special vertices are locally rotation-blocked. By the collar-removal theorem, such blocking yields a removable special cell in one polarity. The remaining parity-sheet problem is reduced to combining collar removal/reinsertion with motion of the other special vertex.

Elevation audit: the switch/parity calculation applies to a realized ambient monochromatic move, with exterior-window checks from the packet rotation law. It destroys perfect alternation but does not automatically create an oriented wall. The terminal appeal to collar removal is withdrawn for the equal-one barrier: reversing that failed deletion does not make it legal, as the audit of §21 shows. Thus parity-sheet switching is a conditional repair interface, not a global closure or termination theorem.
