# Correction: consecutive failed-interface hooks do not imply the rooted 5|4 packet — preserved pre-item development

## Composition

(none yet)

## Development

## Correction: the proposed consecutive-interface (5|4) theorem is invalid

Development version 1 is withdrawn.

The failed-interface hypotheses at two consecutive corridor edges give
[
h(c_1,c_0,v)=1,qquad h(c_2,c_1,v)=1
]
for the relevant packet labels (v).

The attempted proof applied Proposition 1.1 of [[localextend01]]. That proposition instead requires, for two exterior labels (s,t),
[
h(c_1,s,c_0)=h(c_1,t,c_0)=1,
]
[
h(c_2,s,c_1)=h(c_2,t,c_1)=1.
]
These triples have the packet label in the middle position. The failed-interface hooks have the packet label in the third position.

There is no boundary-tournament axiom converting
[
h(c_1,c_0,v)
]
to
[
h(c_1,v,c_0).
]
They belong to different boundary-reversal orbits. Such a conversion would be a cyclic permutation, precisely the invalid operation identified in [[audit_cyclic_rotation_invalidates_the_new_descent_and_second_layer_claims]].

Therefore the claimed rooted five-path
[
(c_2,s,c_1,t,c_0)
]
is not established, and no (5|4) cover follows from the stated hypotheses.

### Valid residue

What remains valid is only:
- each failed interface forces at least four good-deletion labels (v) satisfying the wrong-way hook (h(c_{i+1},c_i,v)=1);
- consecutive failed interfaces therefore give the same good-deletion labels as common **third-position** reversers of consecutive corridor edges, if the six-packet is unchanged.

A new theorem must use these hooks in their actual orientation. Proposition 1.1 cannot be invoked unless independent middle-position triples (h(c_{i+1},v,c_i)) are proved.

No claim of a (5|4) packet is retained.
