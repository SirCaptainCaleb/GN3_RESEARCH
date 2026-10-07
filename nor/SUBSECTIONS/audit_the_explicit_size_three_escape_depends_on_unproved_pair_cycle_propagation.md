# Audit: the explicit size-three escape depends on unproved pair-cycle propagation

## Metadata

- ID: audit_the_explicit_size_three_escape_depends_on_unproved_pair_cycle_propagation
- Parent Section: directed_nor_union_closed_bridge
- Position: 93
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Audit correction to subsection 91. The proposed escape order (f_m,...,f_3,a,c,f_2,f_1,b) uses identities alpha(a,c,f_3)=sigma and alpha(a,c,f_2)=sigma. Those identities came from the claimed propagation of the size-three pair cycle from pivot f_1 to later pivots. Subsection 92 has identified a dropped-coordinate gap in that propagation proof: the witness used to forbid an edge flip omits f_1 and is only a deletion order. Therefore pair-cycle persistence at f_2,f_3,... has not been established, and the explicit escape is conditional on that unproved persistence. The calculations of the escape itself are correct under the persistence hypothesis, but they do not currently close the branch. The safe information is only the original front circuit plus one-step singleton propagation alpha(u,f_2,f_3)=tau, together with any endpoint conditions separately proved by full-support arguments. Future use of the curvature-tube language must distinguish these valid identities from the unproved no-edge-flip induction.

## Frontier

- Development version when composed: None
- Development version now: 1
