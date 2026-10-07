# Audit tournament two chord reduction is sufficient not equivalent

## Metadata

- ID: audit_tournament_two_chord_reduction_is_sufficient_not_equivalent
- Parent Section: directed_nor_union_closed_bridge
- Position: 67
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

In the coboundary-flat representation alpha(a,b,c)=1 xor t(a,b) xor t(b,c) xor t(c,a), restricting to a directed Hamilton path of the representing tournament makes every adjacent edge bit zero and yields alpha(v_i,v_{i+1},v_{i+2})=t(v_i,v_{i+2}). This is a useful sufficient reduction. It is not literally equivalent to NOR in the coboundary-flat sector, because an arbitrary NOR-good coordinate order need not be a directed Hamilton path of that tournament. For a general order, if e_i=t(v_i,v_{i+1}) and r_i=t(v_i,v_{i+2}), then alpha_i=e_i xor e_{i+1} xor r_i. Thus the tournament two-chord theorem would prove the sector, but failure of that theorem would not refute NOR. The subsection wording claiming equivalence should be read with this correction.

## Frontier

- Development version when composed: None
- Development version now: 1
