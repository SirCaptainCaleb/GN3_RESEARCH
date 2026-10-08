# Every blocked A2 special-vertex cell is collar-removable in one polarity

## Metadata

- ID: every_blocked_a2_special_vertex_cell_is_collar_removable_in_one_polarity
- Parent Section: hartman_least_unreachable_connectors
- Position: 21
- Row version: 2
- Development version: 2
- Composition version: 1
- Composition stale: False

## Composition

In a zero packet p,a,x,b,c, equal-zero exterior rotation bits permit deleting x while preserving the first and last ordered pairs and every exterior window. Equal-one bits do not permit that deletion, and reversal cannot rescue it because reversal complements both the original and the post-deletion statuses. The equal-one A2 deletion barrier remains open.

## Development

Let a zero connector contain p,a,x,b,c with p,a,b,c in the shore. Zero monochromaticity gives p->a, b->a, and b->c. The two A2 rotation bits are u=t(p,b) and v=t(a,c). If both rotations are blocked then u=v. In the case u=v=0, also b->p and c->a. Hence both triples (p,a,b) and (a,b,c) have ternary color zero. Replacing p,a,x,b,c by p,a,b,c therefore preserves the zero word and preserves the same first ordered pair (p,a) and last ordered pair (b,c), so every exterior ternary window is unchanged. Thus x is collar-removable. If u=v=1, reverse the whole connector. The reversed local cell has the corresponding two barrier bits equal to zero, so the same collar-removal applies on the opposite monochromatic polarity sheet. Consequently a special vertex trapped by the two-bit A2 rotation law is never intrinsically pinned in the two-polarity repair complex: one polarity admits an exact frozen-collar deletion.

Elevation audit: the u=v=0 deletion is valid with its stated zero word and frozen collar. The claimed rescue at u=v=1 by reversing the connector is invalid. Reversal complements both the original and the post-deletion ternary statuses; it cannot turn a non-monochromatic deletion into a monochromatic one. Indeed u=v=1 makes both newly exposed shore triples color one while the old connector is zero; reversal makes these triples zero while the old connector is one. Thus the equal-one barrier remains unresolved in this deletion argument. Two polarity sheets alone do not remove it.
