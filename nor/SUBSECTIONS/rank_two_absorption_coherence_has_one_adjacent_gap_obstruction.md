# Rank-two absorption coherence has one adjacent-gap obstruction

## Metadata

- ID: rank_two_absorption_coherence_has_one_adjacent_gap_obstruction
- Parent Section: hartman_least_unreachable_connectors
- Position: 6
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

For interior insertions in one fixed gauge, same-gap absorption fills and distinct nonadjacent gaps commute. Adjacent gaps add one mutual-edge condition; its bad orientation is a directed triangle with the shared coordinate. Endpoint cases and global witness-selection coherence require separate checks.

## Development

In path-normalized square-path gauge, two individually insertable missing vertices fill a rank-two cell automatically when they use the same gap, and they commute when their gaps are separated. The only nontrivial case is adjacent gaps. If a inserts at gap i and b at gap i+1, the simultaneous interleaving is legal exactly when the switched mutual edge points from a to b. In the opposite orientation, the two added vertices together with the shared connector vertex form a directed triangle. Hence every rank-two coherence failure is localized to one adjacent-gap directed-triangle residue.
