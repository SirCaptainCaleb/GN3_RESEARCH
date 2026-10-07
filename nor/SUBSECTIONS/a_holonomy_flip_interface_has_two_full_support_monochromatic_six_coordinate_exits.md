# A holonomy-flip interface has two full-support monochromatic six-coordinate exits

## Metadata

- ID: a_holonomy_flip_interface_has_two_full_support_monochromatic_six_coordinate_exits
- Parent Section: ternary_protected_bridges_and_scan_obstructions
- Position: 46
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

At a special-scan holonomy flip, the six-set {x,a,b,c,d,e} has explicit full-support 0-monochromatic orders (x,a,d,b,c,e) and (a,d,b,c,e,x), independent of the remaining free old-coordinate bit. Reversal supplies corresponding color-1 orders. This proves that the six-set interior itself is not the obstruction.

These exits do not automatically preserve an original deletion-carrier boundary pair; later audit shows that no color-0 full-support order begins with the old pair (a,b) or ends with the old pair (d,e). Their value is internal universality, not one-sided global reconnection.

## Development

The holonomy-flip interface has two full-support monochromatic six-coordinate weaves. Use the six coordinates from the perfect-blocker interface: blocker x and old consecutive coordinates a,b,c,d,e. Choose a reference order x<a<b<c<d<e. The blocker scan gives xab=xbc=xcd=xde=1. The two adjacent residual holonomies give alpha(a,x,d)=1 and alpha(b,x,e)=0; by alternation these are xad=0 and xbe=1 in increasing orientation. The old-coordinate data are abc=bcd=cde=0, abd=acd=1, bce=bde=0, with abe=ace=u and ade=1-u. Coboundary parity on four-sets now yields xac=0 from {x,a,b,c}, xbd=0 from {x,b,c,d}, and xce=0 from {x,c,d,e}; also xae=u from {x,a,b,e}. In particular the following two orders are independent of u. First, W_L=(x,a,d,b,c,e) has consecutive statuses xad=0; adb=0 by alternation from abd=1; dbc=0 by cyclic invariance from bcd=0; bce=0. Second, W_R=(a,d,b,c,e,x) has adb=0, dbc=0, bce=0, and cex=xce=0 by cyclic invariance. Hence both six-coordinate orders are 0-monochromatic and use every coordinate of the interface, including the blocker x. The holonomy flip is therefore not an internal obstruction at all: it admits two opposite full-support 0-exits placing x respectively at the left or right side of the local block. The remaining difficulty is only reconnection to the untouched exterior. This is strictly sharper than the five-old-coordinate weave in §43 and gives an explicit two-exit state on which threshold-band or deletion-extremality arguments can act.
