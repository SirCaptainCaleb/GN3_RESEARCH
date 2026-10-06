# Audit: the rank-parity example is outside directed tuple NOR

## Metadata

- ID: rank_parity_counterexample_to_unrestricted_directed_nor
- Parent Section: higher_memory_norine_geodesics
- Position: 3
- Row version: 3
- Development version: 3
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development


The rank-parity construction
\[
\chi(X_0,\ldots,X_k)=|X_0|\pmod2
\]
is a valid counterexample only to the larger class of basepoint-dependent ordered cube-window colorings.

It is not a directed tuple coloring, because two windows with the same ordered flipped coordinates can receive different colors when their initial vertices have opposite rank parity.

Accordingly, any statement that rank parity “refutes unrestricted directed NOR” is misleading under the current terminology. Directed NOR means the coloring is a function of the ordered distinct coordinates
\[
h(v_1,\ldots,v_k)
\]
with reversal antisymmetry.

This node supersedes its earlier wording and exists to prevent that formulation error from propagating.
