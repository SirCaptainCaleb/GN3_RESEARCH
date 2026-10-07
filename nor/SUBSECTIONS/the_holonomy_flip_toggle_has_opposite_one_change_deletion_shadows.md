# The holonomy-flip toggle has opposite one-change deletion shadows

## Metadata

- ID: the_holonomy_flip_toggle_has_opposite_one_change_deletion_shadows
- Parent Section: ternary_protected_bridges_and_scan_obstructions
- Position: 50
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

The holonomy-flip phase-toggle has two deletion shadows with the same attachment pairs (x,a),(c,e): deleting b gives the five-order (x,a,d,c,e) with word 001, while deleting d gives (x,a,b,c,e) with word 100. Together with the full 0000 and 1111 toggle states, the interface is a four-state bridge gadget whose exterior data are identical.

This is the cleanest link from the special holonomy interface back to deletion extremality: if either shadow extends through the fixed exterior reconnections to a global one-change deletion carrier, its phase profile is immediately comparable with the globally minimal witness.

## Development

The boundary-preserving phase toggle has two opposite one-change deletion shadows. In the holonomy-flip six-set, the full-support orders (x,a,d,b,c,e) and (x,a,b,d,c,e) share boundary pairs (x,a) and (c,e), with internal words 0000 and 1111 respectively. Delete b from either comparison skeleton. The resulting five-coordinate order is D_b=(x,a,d,c,e). Its statuses are xad=0, adc=0 by alternation from acd=1, and dce=1 by alternation from cde=0. Hence D_b has local word 001. Delete d instead. The common five-coordinate order is D_d=(x,a,b,c,e), with statuses xab=1, abc=0, bce=0, hence local word 100. Both deletion shadows have exactly the same ordered first pair (x,a) and ordered last pair (c,e) as both full-support toggle states. Therefore all four local realizations -- full 0000, full 1111, b-deletion 001, and d-deletion 100 -- attach to the exterior through identical boundary data. The six-set is thus a four-state bridge gadget: two constant phases and two opposite one-change deletion phases. Any surviving global obstruction must be encoded entirely in the common exterior reconnection packets. This gives a direct interface with the minimum-deletion-carrier method: the exterior cannot change when one compares the two deletion shadows, so if either shadow extends to a global one-change deletion carrier its phase profile can be compared immediately with the globally extremal witness.
