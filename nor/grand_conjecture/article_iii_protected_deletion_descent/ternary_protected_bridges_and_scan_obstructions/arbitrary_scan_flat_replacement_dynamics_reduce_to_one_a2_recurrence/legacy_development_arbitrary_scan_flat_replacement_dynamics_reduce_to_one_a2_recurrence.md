# Arbitrary scan flat replacement dynamics reduce to one A2 recurrence — preserved pre-item development

## Development

## Arbitrary-scan flat replacement dynamics reduce to one A2 recurrence

Work in a minimum coboundary-flat alternating ternary counterexample.

Choose, among all one-change deletion carriers and their reversals/color complements, a carrier
[
O=(v_1,ldots,v_m)
]
with normalized word
[
0^p1^q
]
whose first run (p) is globally minimum.

Let (x) be omitted. The arbitrary-scan replacement theorem shows that every fully insertion-blocking scan admits a good protected replacement on one side of the switch.

Minimum first-run extremality forces the first good replacement to be the right replacement. Its distance is
[
din{2,3},
]
and the new run profile is
[
(p+d,q-d).
]

For the newly omitted coordinate the next branch is forced back to the left, with shortening distance
[
ein{2,3}.
]
The resulting profile is
[
(p+d-e,q-d+e).
]

Minimum first-run extremality gives
[
ele d.
]
Thus only three two-step outcomes survive:
[
(d,e)=(2,2), (3,3), (3,2).
]

### Residual drift is finite

The case
[
(d,e)=(3,2)
]
changes the profile by
[
(p,q)mapsto(p+1,q-1).
]

Because the global minimum defining (p) also ranges over reversals, every run of every normalized deletion carrier is at least (p). Therefore this drift can occur at most (q-p) times. It cannot lie on a directed cycle.

### Distance-three same-profile return is a backtrack

For
[
(d,e)=(3,3),
]
the right replacement inserts (x) exactly at the new switch position. The forced left replacement swaps the previously omitted coordinate back into that same position. The original deletion carrier and omitted coordinate are recovered exactly.

Thus this branch is an immediate two-edge backtrack.

### Distance-two same-profile return is the only recurrence

For
[
(d,e)=(2,2),
]
write the two protected positions as
[
z=v_{p+2},qquad y=v_{p+3}.
]
Represent a state by
[
[z,y; x],
]
meaning (z,y) occupy those positions and (x) is omitted.

One two-step replacement gives
[
[z,y; x]mapsto[y,x; z].
]
Repeating gives
[
[y,x; z]mapsto[x,z; y]
mapsto[z,y; x].
]

Hence the only nontrivial recurrent flat replacement mechanism is the protected three-state cycle
[
[z,y; x]	o[y,x; z]	o[x,z; y]	o[z,y; x].
]

Its omitted-coordinate roots are
[
e_x-e_z,qquad e_z-e_y,qquad e_y-e_x,
]
the minimal directed (A_2) root dependence.

### Current closure frontier

The arbitrary-scan flat sector is therefore reduced to this one (A_2) recurrence.

The recurrence has three deletion carriers with the same prefix, suffix, switch rank, and run profile. It contains a perfect seven-coordinate local threshold weave, leaving only a two-window right-boundary reconnection. The three companion weaves force the residual suffix scans to be coordinatewise nonincreasing across the first reconnection step.

Thus the unconditional flat-sector closure problem is no longer termination of a large repair graph. It is the boundary-preserving elimination of one explicit (A_2) exchange cycle.
