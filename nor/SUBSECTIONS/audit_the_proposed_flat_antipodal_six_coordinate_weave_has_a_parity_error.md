# Audit: the proposed flat antipodal six-coordinate weave has a parity error

## Metadata

- ID: audit_the_proposed_flat_antipodal_six_coordinate_weave_has_a_parity_error
- Parent Section: directed_nor_union_closed_bridge
- Position: 219
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Audit of subsection 217. Let c_b=alpha(x,y,b)=1 in the antipodal-backtrack normalization. Cyclic invariance gives alpha(b,x,y)=1, but alpha(x,b,y) is obtained by swapping b and y in (x,y,b), so alpha(x,b,y)=0. Therefore the proposed full weave a,x,b,y,c,d has internal statuses alpha(a,x,b)=1, alpha(x,b,y)=0, alpha(b,y,c)=1, alpha(y,c,d)=1, i.e. 1,0,1,1 rather than 1,1,1,1. The claimed closure of the d=e=3 antipodal backtrack is invalid. The preceding forced data remain valid: x has bridge 000, y has bridge 111, and flatness plus failure of the central pair insertion force pair-crossing values alpha(x,y,a),alpha(x,y,b),alpha(x,y,c),alpha(x,y,d)=0,1,0,1. This packet forms a fully-curved tetrahedron {a,b,x,y}; using the unique-predecessor theorem with terminal pair (b,y) and continuation c yields the valid local order (x,a,b,y,c,d) with word 0,1,1,1, but it changes two windows at the left reconnection. Thus the antipodal branch remains open as a protected-boundary transport problem rather than an immediate splice.

## Frontier

- Development version when composed: None
- Development version now: 1
