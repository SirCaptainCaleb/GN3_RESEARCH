# Singleton facets force a directed cycle of endpoint outermost roots

## Metadata

- ID: singleton_facets_force_a_directed_cycle_of_endpoint_outermost_roots
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 283
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Assume a minimum counterexample. For each coordinate x, let pi_x be the canonical singleton-facet order x followed by a fixed NOR-good order of V\{x}. Since the ambient instance is a counterexample, pi_x is bad. By the proper-face crossing theorem for the outermost-root carrier, the source of D(pi_x) lies in the earlier facet block {x} and the target lies in V\{x}. Hence the first change rank is exactly 1, and D(pi_x)=e_x-e_{f(x)} for some f(x) != x. Thus f is a fixed-point-free self-map of the finite coordinate set. Iterating f yields a directed cycle x_0 -> x_1 -> ... -> x_{m-1} -> x_0. Every edge of this cycle is realized by an actual endpoint-defect full order x_i g(V\{x_i}), and the corresponding roots sum to zero. Therefore a minimum counterexample automatically supplies a positive physical root cycle of canonical endpoint deletion/reinsertion witnesses. This bypasses the degree-cone extraction for the purpose of producing a root cycle and narrows the remaining realization problem to endpoint-defect witnesses whose deletion tails are already NOR-good.

## Frontier

- Development version when composed: None
- Development version now: 1
