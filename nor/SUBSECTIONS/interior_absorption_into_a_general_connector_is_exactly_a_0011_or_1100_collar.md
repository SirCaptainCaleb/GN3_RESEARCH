# Interior absorption into a general connector is exactly a 0011 or 1100 collar

## Metadata

- ID: interior_absorption_into_a_general_connector_is_exactly_a_0011_or_1100_collar
- Parent Section: monochromatic_connector_blocks
- Position: 15
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

In path-normalized gauge, a missing vertex inserts at an interior gap exactly when its four incidences are 1100 or 0011. Interior insertion preserves both original endpoint ports. This adjacency-free criterion is the one-vertex instance of collective block absorption.

## Development

Let C=(c_1,...,c_m) be any compatible monochromatic-zero connector; x and z may occur anywhere. Switch the tournament along C so that every consecutive edge c_i->c_{i+1} is forward. Since C is monochromatic zero, every distance-two edge c_i->c_{i+2} is then also forward. Fix a missing shore vertex a and, before choosing the switch bit of a, define r_i=1 when c_i dominates a in this normalized tournament. Switching a alone complements the entire word r. Insert a between c_i and c_{i+1}. The new order is again a directed square-path exactly when c_{i-1} and c_i both dominate a while a dominates c_{i+1} and c_{i+2}; after complementing a this is the opposite orientation. Therefore an interior absorption is legal exactly when (r_{i-1},r_i,r_{i+1},r_{i+2}) is 1100 or 0011. This criterion automatically preserves monochromaticity and does not constrain the positions of x,z. Thus a support-maximal compatible connector forces every missing shore vertex to have an incidence word along C avoiding both 0011 and 1100.
