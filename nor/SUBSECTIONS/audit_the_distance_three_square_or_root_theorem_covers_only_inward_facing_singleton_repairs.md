# Audit: the distance-three square-or-root theorem covers only inward-facing singleton repairs

## Metadata

- ID: audit_the_distance_three_square_or_root_theorem_covers_only_inward_facing_singleton_repairs
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 127
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Audit: the distance-three square-or-root theorem covers only inward-facing singleton repairs

Root §126 proves a correct local dichotomy, but its final topological scope was stated too broadly.

An adjacent swap at bond i can serve as an endpoint repair for a transition on either side of that bond:

- as the FIRST-pair repair of the tetrahedron beginning at positions i,i+1;
- or as the LAST-pair repair of the tetrahedron ending at positions i,i+1.

Therefore two legal repair swaps whose bonds differ by three positions need not be the specific pair analyzed in §126.

### What §126 actually proves

The proved configuration is the INWARD-FACING distance-three pair on five consecutive coordinates

(a,b,c,d,e),

where

- swap a,b repairs the left transition on (a,b,c,d);
- swap d,e repairs the right transition on (b,c,d,e).

The local word is then an isolated singleton

u,v,u,

and both bounding transitions are flat.

For exactly this configuration, the five-set bit r=alpha(a,c,e) gives the complete dichotomy:

- r=v: both repairs remain legal and annihilate the singleton at the opposite square corner;
- r=u: after either repair, the other boundary becomes fully curved and emits a protected root.

This theorem is valid.

### What is NOT yet proved

Two repair bonds at distance three may point outward rather than inward, or one may point inward and the other outward. Their repaired transitions need not be the two boundaries of one singleton.

The §126 calculation does not classify those orientation patterns.

Hence the statement

'every unresolved interaction of two flat repair moves is confined to bond distances one or two'

is not yet justified.

The safe conclusion is narrower:

> every INWARD-FACING distance-three convergence around one isolated singleton is solved by square-or-root.

Separated repairs with |i-j|>=4 are still covered independently by root §122.

### Correct remaining overlap frontier

For a complete realized repair-cell complex one must still classify:

1. the remaining orientation patterns at bond distance three;
2. bond-distance-two interactions beyond the same-transition square of roots §§109-110;
3. the genuine bond-distance-one braid/A2 interactions.

This audit concerns only the claimed scope of the gluing classification. It does not challenge the local algebra or square-or-root dichotomy proved in §126.

## Frontier

- Development version when composed: None
- Development version now: 1
