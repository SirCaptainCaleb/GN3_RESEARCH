# Companion A2 weaves forbid an immediate zero to one rise in every residual scan — preserved pre-item development

## Companion A2 weaves forbid an immediate zero-to-one rise in every residual scan

Continue the recurrent flat (A_2) replacement cycle and its three companion seven-coordinate threshold weaves.

Write the common suffix as
[
(C,D,E,F,ldots),
]
and for each residual coordinate (uin{x,y,z}) define
[
s_u(D,E)=alpha(u,D,E),
qquad
s_u(E,F)=alpha(u,E,F).
]

Choose the companion weave which ends with (u):
[
(A,B,	ext{the other two residuals},C,D,u,E,F,ldots).
]

The internal protected block through (C,D,u) has already been proved to have threshold word
[
0,1,1,1,1.
]

The two new right-boundary statuses are
[
alpha(D,u,E)=1-alpha(u,D,E)=1-s_u(D,E)
]
and
[
alpha(u,E,F)=s_u(E,F).
]

After these two windows the untouched suffix returns to color (1).

### Proposition

In a surviving counterexample,
[
s_u(E,F)le s_u(D,E)
qquad
	ext{for every }uin{x,y,z}.
]

### Proof

If
[
s_u(D,E)=0,
qquad
s_u(E,F)=1,
]
then the two right-boundary statuses are
[
1-s_u(D,E)=1,
qquad
s_u(E,F)=1.
]
Hence the entire spanning order has a 0-prefix followed only by 1s. It is a one-change order, contradiction.

Thus the scan pattern (01) is forbidden across these two suffix edges for each of the three residual vertices. QED.

### Vector form

Let
[
S_1=(s_x(D,E),s_y(D,E),s_z(D,E)),
]
[
S_2=(s_x(E,F),s_y(E,F),s_z(E,F)).
]
Then every surviving (A_2) cycle satisfies the coordinatewise inequality
[
oxed{S_2le S_1.}
]

Since the common front value is
[
(s_x(C,D),s_y(C,D),s_z(C,D))=(1,1,1),
]
the protected seven-coordinate weave has converted the first part of the suffix into a monotone scan constraint.

This is stronger than the raw Klein-group holonomy statement: the actual representatives of the switching classes, not merely their classes modulo global complement, are constrained.

The next target is to propagate this coordinatewise monotonicity through a constant-holonomy corridor or show that the first violation produces a translated seven-coordinate weave and closes NOR.
