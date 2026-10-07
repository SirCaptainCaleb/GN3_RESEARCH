# Successor-closed minimum-first cuts force a telescoping protected-root dependence

## Metadata

- ID: successor_closed_realized_shores_force_a_zero_defect_protected_root_cycle
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 66
- Row version: 3
- Development version: 3
- Composition version: 1
- Composition stale: False

## Composition

On the oriented minimum-first p-layer, if every realized cut's forced canonical Johnson successor is also realized, finite iteration gives a closed realized-shore walk and the selected protected roots telescope to a positive dependence. The physical root circulation of that walk need not be one simple coordinate cycle, and extracting a physical subcycle can destroy exact shore concatenation. The rigorous dichotomy is missing forced neighbor versus a telescoping realized-shore circulation.

## Development

Fix the oriented minimum-FIRST-phase p-layer. Let R be its finite set of realized physical p-cuts. For each S in R choose one canonical protected root rho_S=e_a-e_c and its forced Johnson successor sigma(S)=S-{a}+{c}.

If sigma(S) lies in R for every S, iteration gives a directed cycle of realized cuts
S_0 -> S_1 -> ... -> S_{k-1} -> S_0.
For its selected roots,
rho_i = z_{S_i}-z_{S_{i+1}},
so
sum_i rho_i=0.
Thus successor closure forces a genuine positive protected-root dependence supported on realized states.

This conclusion is exact, but it must not be overstated. The endpoint roots rho_i of the shore cycle need not themselves form one simple directed cycle on physical coordinates: the entering coordinate of rho_i need not be the dropped coordinate of rho_{i+1}. The physical circulation may decompose into several coordinate cycles. Consequently the one-token Johnson normal form for a SIMPLE PHYSICAL root cycle does not follow merely from a closed shore walk.

Likewise, if one extracts a support-minimal physical cycle from the telescoping dependence, discarding the other roots generally destroys the exact shore-successor concatenation. Zero cut defect is a property of the full shore walk, not automatically of an extracted physical subcycle.

Therefore the rigorous dichotomy is:

1. some realized extremal p-cut has a forced Johnson successor not realized in the minimum-first layer; or
2. there is a telescoping positive dependence of canonical protected roots whose associated attained cuts concatenate exactly as Johnson edges.

The second branch is stronger than an arbitrary root dependence because it retains an ordered realized-shore walk, but weaker than the previously claimed one-token cycle. Further extraction must preserve both the physical circulation and the shore-walk provenance.
