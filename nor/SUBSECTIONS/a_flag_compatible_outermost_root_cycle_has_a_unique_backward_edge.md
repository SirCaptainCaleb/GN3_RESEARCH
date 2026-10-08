# A flag-compatible outermost-root cycle has a unique backward edge

## Metadata

- ID: a_flag_compatible_outermost_root_cycle_has_a_unique_backward_edge
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 247
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## A flag-compatible outermost-root cycle has a unique backward edge

Continue with a cycle supplied by the preceding conical-degree theorem. Let
rho_*=e_{x_0}-e_{x_1}
be the outermost root of the chosen bad full order, and let
x_1 -> x_2 -> ... -> x_{m-1} -> x_0
be the return path consisting of outermost roots of proper-face witnesses from one nested boundary flag.

Refine that boundary flag, if necessary, to a maximal boundary flag. Its minimal face is a chamber, hence determines a total coordinate order tau. Every other face in the flag is an ordered partition into consecutive intervals of tau.

Take any return-path edge
e_x-e_y=D(pi_F)
coming from a face F in the flag. The proper-face crossing theorem says x lies in a strictly earlier F-block than y. Since the F-blocks are consecutive intervals of tau, it follows that
x <_tau y.

Therefore every return-path edge is strictly forward in the SAME total order tau.

Along the directed return path we obtain
x_1 <_tau x_2 <_tau ... <_tau x_{m-1} <_tau x_0.
Consequently the closing root
rho_*=e_{x_0}-e_{x_1}
is strictly backward in tau and is the unique backward edge of the cycle.

### Monotone-cycle normal form

Every bad full order pi_* therefore has a compatible topological certificate of the following form:

- its outermost defect root is x_0 -> x_1;
- there is a chamber order tau in which x_1 occurs before x_0;
- canonical proper-face witnesses along one flag provide a directed path from x_1 back to x_0;
- the physical vertices on that path occur in strictly increasing tau-order.

Thus the topological obstruction is a monotone chord chain closed by one backward chord.

This normal form removes arbitrary root-cycle geometry from the witnessed-degree route. The remaining splice problem is one-dimensional relative to tau: realize a shortcut along the increasing return chain, or use the unique backward edge to define a strict inversion/alignment descent while preserving the outermost-change witness class.

## Frontier

- Development version when composed: None
- Development version now: 1
