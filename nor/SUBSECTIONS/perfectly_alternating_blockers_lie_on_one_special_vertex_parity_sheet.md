# Perfectly alternating blockers lie on one special-vertex parity sheet

## Metadata

- ID: perfectly_alternating_blockers_lie_on_one_special_vertex_parity_sheet
- Parent Section: hartman_least_unreachable_connectors
- Position: 22
- Row version: 2
- Development version: 2
- Composition version: 1
- Composition stale: False

## Composition

Perfect alternation between x,z requires χ=1 for the gauge-invariant parity χ=|i_z−i_x|+σ_x+σ_z mod 2. On χ=0 at least one adjacent pair is equal. This need not be a thick transition or an oriented wall; directed-wall transport and pairwise coherence require additional hypotheses.

## Development

Let C=(c_1,...,c_m) be a monochromatic-zero connector in path-normalized square-path gauge. Fix an uncovered shore vertex a and take its switch bit to be zero when defining the incidence word r_i=t'(c_i,a).

Let x and z occur at positions i_x and i_z. In the fixed switching-normalized split, x loses to every shore vertex and z dominates every shore vertex. If sigma_x,sigma_z are the connector path-normalizing switch bits, then
r_{i_x}=sigma_x,
r_{i_z}=1 xor sigma_z.

Suppose r is perfectly alternating on the whole interval between x and z. Then
r_{i_x} xor r_{i_z} = |i_z-i_x| mod 2.
Therefore a necessary condition for a wall-free alternating blocker between the two special vertices is
|i_z-i_x| + sigma_x + sigma_z = 1 mod 2.

This condition is independent of the global complement ambiguity of the connector switching vector.

Consequently, on the opposite special-vertex parity sheet
|i_z-i_x| + sigma_x + sigma_z = 0 mod 2,
every individually blocked incidence word must contain a nonthin transition between x and z, hence at least one oriented thick wall. In a pairwise-blocked family, shared thick walls obey the coherence theorem of the preceding subsections.

Thus the Hartman frontier splits cleanly:
1. the thick-wall sheet, where directed-wall transport is available;
2. one exceptional parity sheet on which a perfectly alternating blocker can survive.

Independent motion of x and z is therefore strategically relevant: any realized repair changing this special parity destroys the wall-free blocker class and forces an oriented wall.

Elevation audit: the parity obstruction to perfect alternation is valid. Its opposite sheet forces a nonalternating adjacent pair between the special vertices, not necessarily a nonthin transition or a directed wall: the interval may, for example, be constant. Directed-wall transport and family coherence require their independent wall and pair-normalization hypotheses. Keep the parity certificate without promoting those stronger conclusions.
