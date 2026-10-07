# The antipodal braid cell has two deletion-witness exits and one residual E1 transport pair

## Metadata

- ID: the_antipodal_braid_cell_has_two_deletion_witness_exits_and_one_residual_e1_transport_pair
- Parent Section: ternary_protected_bridges_and_scan_obstructions
- Position: 20
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Protected-exit theorem for the exact distance-three antipodal backtrack. Use the local order ...P,R,a,b,y,c,d,e,f,... with omitted x. The exact backtrack data are: x-bridge alpha(x,a,b)=alpha(x,b,y)=alpha(x,y,c)=alpha(x,c,d)=0; original y-bridge alpha(a,b,y)=alpha(b,y,c)=alpha(y,c,d)=1; pair-crossing values alpha(x,y,a),alpha(x,y,b),alpha(x,y,c),alpha(x,y,d)=0,1,0,1. Let s=alpha(x,R,a). Blocking around the original switch gives the preceding left scan bit at least s. Let t=alpha(y,d,e); blocking around the return carrier gives t at least the next y-scan bit alpha(y,e,f). Case 1: s=0. Omit b and use the deletion order with local block P,R,a,x,y,c,d,e,f. Its statuses are 0, s=0, alpha(a,x,y)=alpha(x,y,a)=0, alpha(x,y,c)=0, alpha(y,c,d)=1, alpha(c,d,e)=1, alpha(d,e,f)=1. Thus the local word is 0000111. Both outside ordered pairs (P,R) and (e,f) are unchanged, so this is a genuine one-change deletion witness whose threshold is two windows farther right than the original carrier. Case 2: t=1. Omit c and use P,R,a,b,x,y,d,e,f. Its statuses are 0,0,alpha(a,b,x)=0, alpha(b,x,y)=alpha(x,y,b)=1, alpha(x,y,d)=1, t=1, alpha(d,e,f)=1, so the local word is 0001111. Again both outside ordered pairs are unchanged; this is a genuine one-change deletion witness with threshold one window farther right. Hence the only antipodal state not already yielding a protected deletion-witness improvement satisfies s=1 and t=0. The insertion-blocking inequalities then force the neighboring left scan bit alpha(x,P,R)=1 and the next right scan bit alpha(y,e,f)=0. In this residual case the two canonical exits of the braid hexagon are exact opposite E=1 transports. The left exit ...P,R,x,a,b,y,c,d,e,f,... has local statuses 1,0,0,1,1,1,1 after the old zero prefix: exactly one positive threshold defect, alpha(P,R,x)=1, has been exported strictly left of the caged braid cell while the entire right suffix from (c,d) onward is unchanged. The right exit ...P,R,a,b,x,c,d,y,e,f,... has statuses 0,0,0,0,0,1,1,0 followed by the untouched 1-suffix: exactly one negative defect alpha(y,e,f)=0 is exported strictly right of the cell, while the entire left prefix through (a,b) is unchanged. Thus every antipodal backtrack either gives a boundary-safe one-change deletion witness with a strict threshold displacement, or lies in one canonical residual state with two opposite boundary-fixed E=1 exits. This isolates the final antipodal problem to connecting or terminating those two outward defect transports; no hidden outside-coordinate change remains.

## Frontier

- Development version when composed: None
- Development version now: 1
