# Radon zeros of protected roots are physical coordinate cycles

## Metadata

- ID: radon_zeros_of_protected_roots_are_physical_coordinate_cycles
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 7
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

For every protected replacement bridge, an adjacent 10 descent gives a physical root rho=e_a-e_c, where a is the dropped coordinate and c the entering coordinate.

Suppose a positive dependence occurs:
sum_j lambda_j (e_{a_j}-e_{c_j}) = 0,
with all lambda_j > 0.

Orient a weighted physical-coordinate edge c_j -> a_j with weight lambda_j. The coefficient of e_v in the dependence is total incoming weight at v minus total outgoing weight at v. Hence the dependence is exactly a circulation, and its support decomposes into directed cycles of physical coordinates.

Inside one fixed protected deletion fiber, every root points across the same protected cut: its positive endpoint lies on the left side and its negative endpoint lies on the right side. Pairing with the cut functional that is +1 on the left and -1 on the right is strictly positive on every such nonzero root. Therefore no positive Radon dependence can be supported entirely in one fixed deletion fiber.

Consequently any compatible Radon zero must involve multiple protected fibers and already contains a directed physical-coordinate cycle.

Combined with the established Coxeter-block localization theorem, if the roots are carried in one ordered-partition permutohedral cell, every directed cycle in the circulation lies inside one Coxeter block. The outside coordinate order is therefore fixed throughout the local extraction problem.

Closure target: choose a shortest directed protected-root cycle and prove a boundary-preserving surgery that either produces a threshold-compatible replacement bridge or replaces the cycle by a strictly shorter one. The two-cycle e_a-e_c, e_c-e_a is the protected-root analogue of a complementary signed-middle pair and is the natural base case.

## Frontier

- Development version when composed: None
- Development version now: 1
