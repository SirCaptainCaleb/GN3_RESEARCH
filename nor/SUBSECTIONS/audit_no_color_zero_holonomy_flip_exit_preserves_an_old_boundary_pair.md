# Audit: no color-zero holonomy-flip exit preserves an old boundary pair

## Metadata

- ID: audit_no_color_zero_holonomy_flip_exit_preserves_an_old_boundary_pair
- Parent Section: ternary_protected_bridges_and_scan_obstructions
- Position: 49
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

Complete six-set forcing shows that no 0-monochromatic full-support order at the holonomy flip starts with the old left ordered pair (a,b), and none ends with the old right ordered pair (d,e). Therefore the tempting claim “choose x on the outward side and all damage is outward” is false. The valid phase-toggle attachment pairs are the new pairs (x,a) and (c,e). Any global closure argument must explicitly reconnect those fixed new pairs to the old exterior.

## Development

Audit: the holonomy-flip switch gadget cannot preserve either old boundary pair in color 0. Use the complete six-set triangle table with reference order x<a<b<c<d<e: xab=1,xac=0,xad=0,xae=u,xbc=1,xbd=0,xbe=1,xcd=1,xce=0,xde=1; abc=0,abd=1,abe=u,acd=1,ace=u,ade=1-u,bcd=0,bce=0,bde=0,cde=0. First suppose a 0-monochromatic Hamilton order starts with the old left ordered pair (a,b). The third coordinate must be c, except when u=0 it may also be e. If it is e, no unused fourth coordinate gives alpha(b,e,*)=0. If it is c, the fourth coordinate is d or e. Choosing d forces e fifth and x last, but alpha(d,e,x)=1. Choosing e forces x fifth and d last, but alpha(e,x,d)=1. Hence no all-zero full-support order begins (a,b). Now suppose an all-zero Hamilton order ends with the old right pair (d,e). The predecessor is c or b, and when u=1 possibly a. If it is c, backwards forcing gives ...a,b,c,d,e with x preceding a,b, but alpha(x,a,b)=1. If it is b, backwards forcing gives c,a,x,b,d,e (up to the forced choices), whose first triple has color 1. If u=1 and the predecessor is a, the three possible preceding choices b,c,x each force a unique continuation and the remaining first triple is color 1. Thus no all-zero full-support order ends (d,e). Therefore every color-0 realization of the holonomy-flip six-set changes both old ordered boundary pairs. Merely choosing whether x is the left or right endpoint does not confine damage to the outward side. The strategic claim in the preceding switch-gadget subsection that one may obtain 'monochromatic interior -> outward boundary only' requires additional structure and must not be used as proved. The boundary-preserving phase toggle with common pairs (x,a) and (c,e) remains valid, but those are new pairs, not the old deletion-carrier pairs.
