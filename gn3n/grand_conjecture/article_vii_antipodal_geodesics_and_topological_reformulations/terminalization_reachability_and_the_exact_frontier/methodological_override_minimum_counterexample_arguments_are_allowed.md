# Methodological correction: minimum-counterexample descent is not a closure mechanism

## Composition

(none yet)

## Development

## Shared worker guidance correction

The previous override was too permissive and is withdrawn as a proof strategy.

Minimum-counterexample reasoning may be used only when minimality yields an immediate contradiction in the same structural configuration. It must NOT be used merely to replace a branch by a smaller induced counterexample and then treat that smaller graph as solved, bounded, or harmless.

In particular, the inference
“proper Hamiltonian support K => pc(H-K)<=2 by minimum-counterexample minimality”
must not be used as a generic seam-closure or reseeding device. That move hides the original order dependence: the smallest possible counterexample order is not fixed, and any later finite/small-order check can simply migrate upward.

Active Article VII work should therefore prefer arbitrary-order, structurally monotone arguments:
- interval-preserving saturation;
- explicit rail-length or support potentials;
- direct endpoint/reversal transport;
- comparison-cover disturbances;
- protected-carrier localization;
- hereditary statements whose hypotheses and conclusions remain meaningful at arbitrary order.

Minimum-counterexample arguments remain admissible only when the smaller-object step itself immediately contradicts another already-proved invariant and does not hand the unresolved theorem to an unspecified smaller graph.

Accordingly, recent results whose essential step is generic minimality-to-pc<=2 are conditional diagnostics, not closure lemmas. The arbitrary-order seam and peeling results remain the active frontier.
