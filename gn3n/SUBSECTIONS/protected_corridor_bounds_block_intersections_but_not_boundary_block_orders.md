# Protected corridor bounds block intersections but not boundary block orders

## Metadata

- ID: protected_corridor_bounds_block_intersections_but_not_boundary_block_orders
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 53
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Let F be an ordered-partition face protected at a positive span-two witness edge whose reflected starts are a<b. Set C=[a+1,b+3], the vertex interval whose internal statuses are [a+1,b+1]. Every chamber of F avoids 001,011,0101 wholly inside that status interval.

Then every positional face block B satisfies |B intersect C|<=4. Indeed the intersection is an interval. If it had at least five positions, choose five consecutive positions i,...,i+4 inside it. Here a+1<=i<=b-1. Freeze all other positions and freely permute the five vertices in these positions, which is permitted by the face block. Protectedness forbids positive 001 and 011 in the three internal statuses of each of the 120 orders. This contradicts the five-position obstruction in [[verified_five_position_obstruction_and_ordered_tuple_compression]]. Thus the intersection has at most four positions.

Consequently every block wholly contained in C has order at most four, and its permutahedral factor has rank at most three. At most two blocks can meet both C and its exterior, one at each boundary. A block meeting both exterior sides would contain all of C, and is impossible whenever |C|>=5.

This is a bound on the intersection with the protected corridor, not on the full order of a boundary block. Large blocks extending outward may meet a determining window and change its predicate; they cannot be declared exterior sign-neutral factors solely because they fail to couple both reflected windows. The explicit construction in [[arbitrarily_large_boundary_blocks_can_change_the_selected_positive_witness_sign]] supplies that distinction.

Thus the source face decomposes into bounded interior block factors and at most two potentially unbounded boundary factors. No bound on total rank follows: there may be many interior factors, and either boundary factor may itself have arbitrarily large rank. To obtain a bounded non-product interaction theorem, one must prove that the chosen repair and transport factor through the boundary-block data in a compatible way; the intersection inequality alone does not establish it.
