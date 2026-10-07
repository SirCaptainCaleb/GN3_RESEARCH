# Same-profile flat replacement cycles are exactly the two minimal A2 root carriers

## Metadata

- ID: same_profile_flat_replacement_cycles_are_exactly_the_two_minimal_a2_root_carriers
- Parent Section: directed_nor_union_closed_bridge
- Position: 207
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development


Continue the minimum-run arbitrary-scan flat replacement dynamics.

A p-minimal deletion carrier first moves right and then left. The two-step dynamics always return to the same run profile. There are two qualitatively different same-profile mechanisms.

### Distance-three: antipodal pair

If the first right replacement has distance d=3, the omitted coordinate x replaces

y=v_{p+3}.

The new switch rank is p+3. The blocker scan of y at the new central position has value 1, so the next replacement is forced left. In this d=3 case the left replacement position is again p+3, namely the position currently occupied by x. Hence the second replacement swaps y back for x and exactly recovers the original deletion order.

Thus the omitted-coordinate dynamics are

x -> y -> x.

Associate to a change of omitted coordinate a->b the root e_a-e_b. The closed two-step orbit has root sum

(e_x-e_y)+(e_y-e_x)=0.

This is precisely the antipodal-pair minimal dependence from the A2 carrier classification.

### Distance-two: directed triangle

If the first right replacement has distance d=2, write the local state near the switch as

[x | z,y],

where x is omitted and z,y occupy positions p+2,p+3.

The right replacement inserts x in place of y, so y becomes omitted. Minimum first-run extremality forces the return left replacement also to have distance 2; otherwise the first run would fall below p.

That left replacement inserts y in place of z. Consequently the net two-step transformation is

[x | z,y] -> [z | y,x].

The run profile is again (p,q), but the omitted coordinate has changed from x to z.

If this same-profile distance-two mechanism repeats, the local triple rotates:

[x | z,y]
-> [z | y,x]
-> [y | x,z]
-> [x | z,y].

The omitted-coordinate roots around the three-state loop are

e_x-e_z,
e_z-e_y,
e_y-e_x,

and therefore

(e_x-e_z)+(e_z-e_y)+(e_y-e_x)=0.

This is exactly the directed-triangle minimal positive dependence in the A2 root system.

### Synthesis

The terminal same-profile cycles of the corrected flat replacement dynamics are not new obstructions.

They coincide exactly with the two minimal root-cancellation species already isolated in the switch-prism topology:

1. antipodal pair;
2. directed A2 triangle.

Thus the dynamic and topological frontiers have merged. Any remaining flat-sector cycle must be resolved at one of these two rank-two root carriers.

A direct local monochromatic splice need not exist: the directed-triangle packet is algebraically consistent. The next closure target is therefore specifically to show that an A2 replacement cycle cannot occur inside a minimum full counterexample, using either the codimension-two pair-defect data for the antipodal case or the directed-triangle/circuit machinery for the three-cycle case.


## Frontier

- Development version when composed: None
- Development version now: 1
