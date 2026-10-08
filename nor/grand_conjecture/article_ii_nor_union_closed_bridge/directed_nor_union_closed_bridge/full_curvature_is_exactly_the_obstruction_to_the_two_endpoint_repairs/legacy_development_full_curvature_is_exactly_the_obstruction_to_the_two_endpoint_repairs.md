# Full curvature is exactly the obstruction to the two endpoint repairs — preserved pre-item development

## Composition

(none yet)

## Development

## Full curvature is exactly the obstruction to the two endpoint repairs

Let
[
(a,b,c,d)
]
be four consecutive coordinates in a pure alternating triangle orientation. Put
[
x=alpha(a,b,c),qquad
y=alpha(b,c,d),
]
and assume there is a transition:
[
x
e y.
]

Also write
[
u=alpha(a,b,d),qquad
w=alpha(a,c,d).
]

### Last-pair repair

Swap (c,d), obtaining
[
(a,b,d,c).
]
The two central statuses become
[
u,qquad alpha(b,d,c)=1-y.
]
Since (y=1-x), the new central transition bit is
[
uoplus(1-y)
=
uoplus x.
]
Thus swapping the last pair removes the transition exactly when
[
u=x.
	ag{1}
]

### First-pair repair

Swap (a,b), obtaining
[
(b,a,c,d).
]
The central statuses become
[
1-x,qquad w.
]
Hence this swap removes the transition exactly when
[
w=1-x=y.
	ag{2}
]

### Theorem

Both endpoint swaps fail to remove the transition if and only if the tetrahedron ({a,b,c,d}) is fully curved.

#### Proof

Both repairs fail precisely when
[
u
e x,qquad w
e y.
]
Because the values are binary and (y=1-x), this means
[
u=y,qquad w=x.
]
Therefore the four face values in the written order satisfy
[
alpha(a,b,c)=alpha(a,c,d)

e
alpha(a,b,d)=alpha(b,c,d),
]
which is exactly the fully-curved (2)-(2) face pattern.

Conversely that fully-curved pattern gives (u=y) and (w=x), so neither endpoint swap eliminates the transition. (square)

### Consequence

A transition carried by a non-fully-curved tetrahedron always has an elementary local repair direction: one of the two endpoint adjacent transpositions kills the central switch.

Thus the only locally irreducible transition is a universal switch gadget. In a globally minimum-variation order, any non-fully-curved transition can survive only because both possible repairing swaps create compensating variation at their outer reconnection zones.

This sharply separates the global problem:
- fully-curved transitions are intrinsically forced;
- every other transition is extrinsically protected by neighboring data.
