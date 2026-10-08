# Three-step curvature transport requires a distance-four memory bit — preserved pre-item development

## Composition

(none yet)

## Development

## Three-step curvature transport requires one new memory coordinate

Continue in Hamilton-normalized tournament coordinates. Let
(...,a,b,c,d,q,r,s,...)
have a flat central transition, and write the old consecutive ternary statuses
x,1-x,z,R,S.
A successful right endpoint repair swaps c,d.

On the distance-three transport branch one has
V=alpha(c,q,r) != R,
and the newly created transition is between V and S. Since it is created by toggling the old transition bit R xor S, necessarily
R=S.

The new target transition is supported on the consecutive quadruple
(c,q,r,s)
in the repaired order.

Let
U=alpha(c,r,s).
A direct renormalization calculation gives the new distance-three chord across that target quadruple:
z_target_new = V xor U.

Therefore:
- the new target switch is fully curved iff U=V;
- it is flat iff U!=V.

### Memory consequence
The bit U is not determined by the old consecutive status word x,1-x,z,R,S and the old distance-three chord layer alone. In the old Hamilton-normalized tournament,
U depends on the distance-four chord t(c,s).

Equivalently, the two-layer state
(consecutive distance-two chords x_i, consecutive distance-three chords z_i)
is dynamically closed under 2-step flat transports, but not under 3-step transports. A 3-step move consults one additional memory coordinate.

This explains why the repair graph resists reduction to a finite local automaton on status and curvature alone. The exceptional 3-step branch is exactly where higher ordered-tail information enters.

It also aligns with the general switch-prism frontier: extracting a compatible spanning path requires retaining enough ordered-tail data to survive these 3-step transitions. Any proposed three-coordinate carrier must encode at least the skipped-triangle bit U (or an equivalent distance-four chord), not merely the status word and current curvature labels.
