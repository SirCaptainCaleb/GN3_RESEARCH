# Audit the even cycle Z2 repair charge is identically zero — preserved pre-item development

## Composition

(none yet)

## Development

## Audit: the even-cycle Z2 repair charge is identically zero

This audits the proposed invariant I=J2 xor P from subsection 134.

Let a cyclic ternary status word have even length m. Write its binary statuses as
[
w_0,ldots,w_{m-1}
]
with cyclic indices, and let
[
d_i=w_ioplus w_{i+1}
]
be the transition indicator on slot i.

Subsection 134 defines
[
P=sum_{i:d_i=1} i pmod 2.
]
Equivalently,
[
P=igoplus_{i {m odd}} d_i.
]
Because m is even, the odd cyclic edges form a perfect matching of the m status positions. Therefore
[
P
=igoplus_{i {m odd}}(w_ioplus w_{i+1})
=igoplus_{j=0}^{m-1}w_j.
	ag{1}
]

Now fix any tournament representative t of the coboundary-flat switching class. For a cyclic coordinate order write
[
e_i=t(v_i,v_{i+1}),qquad
r_i=t(v_i,v_{i+2}).
]
Up to the fixed global convention already used in subsection 99, the triangle status has the form
[
w_i=e_ioplus e_{i+1}oplus r_i.
]
XOR over all cyclic i. Every adjacent-edge bit e_i occurs exactly twice, hence cancels:
[
igoplus_i w_i
=
igoplus_i r_i
=
J_2.
	ag{2}
]

Combining (1) and (2),
[
oxed{P=J_2}
]
for every even cyclic status word, independently of repairs. Consequently
[
oxed{I=J_2oplus P=0}
]
identically.

Thus subsection 134 does not supply a nontrivial component charge. Its edgewise conservation calculation is correct but tautological: both quantities are the same global parity.

The useful invariant remains subsection 133's repair law
[
Delta J_2=lambda,
]
which says every closed repair loop has even parity of distance-three transports. Any no-cycle theorem must use that parity together with additional winding, tail, or holonomy data; XORing with transition-slot parity adds no information in even length.
