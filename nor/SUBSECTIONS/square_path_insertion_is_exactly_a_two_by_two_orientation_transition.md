# Square-path insertion is exactly a two-by-two orientation transition

## Metadata

- ID: square_path_insertion_is_exactly_a_two_by_two_orientation_transition
- Parent Section: monochromatic_connector_blocks
- Position: 16
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

The square-path insertion collar requires two predecessors to dominate the new vertex and the new vertex to dominate two successors, up to its switching complement. Its incidence word therefore has an admissible 1100 or 0011 substring. Endpoint-compatible insertion has additional fixed-gauge parity conditions.

## Development


Let C=(c_1,...,c_m) be a compatible monochromatic zero connector. Pass to its path-normalized switching representative, so every distance-one and distance-two edge of C points forward.

Fix an outside shore vertex a. Choose one of the two possible switching states of a, and write
h_j=1 iff c_j -> a
in the resulting representative.

Insert a between c_i and c_{i+1}. The new order is again a directed square-path exactly when the four new required incidences are
c_{i-1}->a,
c_i->a,
a->c_{i+1},
a->c_{i+2}.
Thus, for the chosen switching state,
(h_{i-1},h_i,h_{i+1},h_{i+2})=(1,1,0,0).

Toggling a complements every h_j. Therefore, allowing either switching state of the new vertex, an interior insertion exists exactly at a four-bit pattern
1100 or 0011.

This is the square-path form of the 010 ternary insertion criterion, but it has two advantages:
1. it does not refer to a fixed adjacent x,z edge;
2. it remains valid while x and z move independently anywhere in the connector.

Hence a vertex blocked from every interior insertion has an orientation word h with no occurrence of 1100 or 0011. Equivalently, at every boundary between two constant runs, at least one of the two adjacent runs has length one. Two consecutive runs of lengths at least two are forbidden.

Endpoint-compatible insertion adds the corresponding endpoint switching-parity condition; the interior obstruction itself is exactly the forbidden two-by-two transition above.

Thus a maximal-support connector converts every uncovered shore vertex into a binary orientation word with this restricted alternating-run structure. This is a natural finite-state input for collective exchange: growth fails only when every uncovered vertex alternates through the connector with no thick-to-thick polarity transition.
