# Largest Hamiltonian supports in minimum counterexamples have half order

## Metadata

- ID: largest_hamiltonian_supports_in_minimum_counterexamples_have_half_order
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 212
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Let H be a minimum-order counterexample on n vertices and let S be a proper Hamiltonian support of maximum cardinality s. For every vertex z, minimality gives a spanning two-cover of H-z. Every component of that deletion cover is itself a proper Hamiltonian support of H, so each component has order at most s. Since the two components cover n-1 vertices, n-1<=2s. Therefore s>=ceil((n-1)/2). In particular, if H-S=P|Q is any two-cover of the complement of a globally largest support, then |P|+|Q|=n-s<=s+1. This scale constraint is independent of small-order verification and is compatible with the universal endpoint noninsertability of a globally largest support.

## Frontier

- Development version when composed: None
- Development version now: 1
