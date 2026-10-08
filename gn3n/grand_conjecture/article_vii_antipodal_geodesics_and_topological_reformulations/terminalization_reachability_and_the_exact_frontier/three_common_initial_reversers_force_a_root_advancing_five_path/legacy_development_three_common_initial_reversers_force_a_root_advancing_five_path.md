# Three common initial reversers force a root-advancing five-path — preserved pre-item development

## Composition

(none yet)

## Development

Let
[
P=(p_1,p_2,ldots),qquad Q=(q_1,q_2,ldots)
]
be vertex-disjoint tight paths, and let (z_1,z_2,z_3) be distinct vertices outside them. Assume
[
h(p_2,p_1,z_i)=h(q_2,q_1,z_i)=1
qquad(i=1,2,3).
]

Then two of the (z_i), say (z,w), satisfy one of
[
(p_2,p_1,z,q_1,w),qquad
(p_2,p_1,w,q_1,z),
]
or one of the symmetric paths
[
(q_2,q_1,z,p_1,w),qquad
(q_2,q_1,w,p_1,z),
]
and the displayed order is a tight Hamiltonian five-path.

Proof. For each (z_i), let
[
	heta_i=h(p_1,z_i,q_1).
]
Two values agree by pigeonhole. If (	heta_z=	heta_w=1), then
[
(p_1,z,q_1),qquad(p_1,w,q_1)
]
are tight. Exactly one of
[
(z,q_1,w),qquad(w,q_1,z)
]
is tight by boundary antisymmetry. Prepending (p_2,p_1) gives one of the first two displayed five-paths, using (h(p_2,p_1,z)=h(p_2,p_1,w)=1).

If the common value is (0), boundary antisymmetry gives
[
(q_1,z,p_1),qquad(q_1,w,p_1)
]
tight. Exactly one of ((z,p_1,w),(w,p_1,z)) is tight, and prepending (q_2,q_1) gives one of the symmetric five-paths.

Thus three common reversers of the two initial exposed edges force a five-path which consumes both first vertices and the second vertex of one corridor component. In particular the six-set
[
{p_1,p_2,q_1,q_2,z,w}
]
has a (5|1) two-cover.

This is stronger than unrooted Hamiltonicity of an endpoint packet: the path has an explicit corridor-facing root (p_2) or (q_2). It still does not concatenate to the untouched tail, because the reverser relation blocks the naive next junction. Its value is as a root-advance primitive for connector-free packet arguments.
