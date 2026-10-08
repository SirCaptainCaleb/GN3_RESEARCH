# Four vertices cannot support the minimum-shore triangle cover

## Metadata

- ID: four_vertices_cannot_support_the_minimum_shore_triangle_cover
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 351
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Section 345 says every edge of the minimum-shore tournament belongs to a directed triangle. This is impossible on four vertices. Choose a vertex r with at least two outgoing neighbors a,b, with the edge from a to b. The triangle containing the edge from r to a must use the fourth vertex d, forcing edges a to d and d to r. The triangle containing r to b also must use d, forcing b to d. Now the edge from a to b cannot belong to a directed triangle: neither r nor d can complete it. Hence a minimum shortcut-free shore has size at least five, using also the exclusions of sizes at most three.

## Frontier

- Development version when composed: None
- Development version now: 1
