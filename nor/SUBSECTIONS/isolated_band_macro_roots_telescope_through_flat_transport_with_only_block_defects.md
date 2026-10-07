# Isolated-band macro roots telescope through flat transport with only block defects

## Metadata

- ID: isolated_band_macro_roots_telescope_through_flat_transport_with_only_block_defects
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 162
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Isolated-band macro roots telescope through flat transport with only block defects

Consider an isolated monochromatic band in a ternary order. Keep its left change fixed and transport its right change outward by the audited flat endpoint repairs.

Let s be the physical coordinate used by the consecutive-change macro root at the fixed left change. At stage j let the right barrier have physical root

rho_j=e_{a_j}-e_{t_j},

where t_j is the entering coordinate three positions beyond the right change. Then the isolated-band macro root is

R_j=e_s-e_{t_j}.

Suppose the next flat repair transports the right barrier to stage j+1. Root §104 gives a new source a_{j+1} in the newly added transport block and defines the within-block defect

delta_{j+1}=e_{a_{j+1}}-e_{t_j}.

Therefore

R_{j+1}-R_j
=
(e_s-e_{t_{j+1}})-(e_s-e_{t_j})
=
e_{t_j}-e_{t_{j+1}}.

On the other hand

rho_{j+1}-delta_{j+1}
=
(e_{a_{j+1}}-e_{t_{j+1}})
-
(e_{a_{j+1}}-e_{t_j})
=
e_{t_j}-e_{t_{j+1}}.

Hence the exact transport identity is

R_{j+1}-R_j = rho_{j+1}-delta_{j+1}.

### Distance-two and distance-three cases

If the repair transports by distance two, root §104 gives a_{j+1}=t_j, so delta_{j+1}=0 and

R_{j+1}=R_j+rho_{j+1}.

If the repair transports by distance three, delta_{j+1} is nonzero but is supported entirely inside the newly added ordered-partition block D_{j+1}. Distinct distance-three steps have disjoint defect supports.

### Telescoping along the whole trajectory

After m rightward transports,

R_m-R_0
=
sum_{j=1}^m rho_j
-
sum_{j=1}^m delta_j.

Thus pushing a witnessed Sperner isolated-band label to its terminal band state changes its macro root by:

1. the sum of the actual protected barrier roots encountered during transport;
2. minus pairwise support-disjoint local defects, one for each distance-three step.

No uncontrolled global correction appears.

### Consequence for the Sperner closing path

In the witnessed one-band Sperner closing relation of root §156, each macro root may therefore be replaced by its terminal transported macro root, at the cost of adding:
- actual protected barrier roots from zero-free monotone transport flags;
- within-block defects supported in disjoint transport blocks.

By root §104, the barrier roots from any one transport flag are linearly independent. Hence cancellation created by this replacement cannot occur internally along one flag. Any new cancellation must involve:
- a gluing between distinct transport flags; or
- cancellation of within-block defects at a shared block/braid residue.

Therefore the topological closing path and the local transport program are algebraically compatible: terminalization does not destroy the closing relation, but localizes all discrepancy to the same gluing cells already identified as the active frontier.

## Frontier

- Development version when composed: None
- Development version now: 1
