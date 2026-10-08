# Non full transitions transport by two or annihilate — preserved pre-item development

## Development

## Non-full transitions transport by two or annihilate

Let
[
C=(ldots,p,a,b,c,d,q,r,ldots)
]
be a cyclic coordinate order in a pure alternating triangle orientation. Write the consecutive status bits
[
L=alpha(p,a,b),qquad
x=alpha(a,b,c),qquad
y=alpha(b,c,d),qquad
z=alpha(c,d,q),qquad
R=alpha(d,q,r),
]
and assume
[
x
e y,
]
so the tetrahedron (Q={a,b,c,d}) carries a transition.

Suppose the last-pair endpoint repair is available, i.e.
[
u:=alpha(a,b,d)=x.
]
By the endpoint-repair theorem this occurs whenever the transition is non-fully-curved in that repair direction.

Swap (c,d), producing
[
(ldots,p,a,b,d,c,q,r,ldots).
]

The new affected statuses are:
[
L,qquad
u=x,qquad
alpha(b,d,c)=1-y=x,qquad
alpha(d,c,q)=1-z,qquad
R.
]

Thus the local status string changes from
[
(L, x, 1-x, z, R)
]
to
[
(L, x, x, 1-z, R).
]

Let
[
d_j=c_joplus c_{j+1}
]
denote cyclic transition bits, with the central transition (d_i=1) between (x) and (1-x).

Then:
[
d'_{i-1}=d_{i-1},
qquad
d'_i=0,
qquad
d'_{i+1}=d_{i+1},
qquad
d'_{i+2}=1-d_{i+2}.
]

Therefore
[
q(C')-q(C)
=
-1+igl((1-d_{i+2})-d_{i+2}igr)
=
-2d_{i+2}.
]

### Theorem: transport-or-annihilate law

Under a successful last-pair repair of a non-full transition:

- if (d_{i+2}=1), then
  [
  q(C')=q(C)-2;
  ]
  the repaired transition collides with the transition two steps to its right and the pair annihilates;

- if (d_{i+2}=0), then
  [
  q(C')=q(C);
  ]
  the central transition disappears and a new transition appears two positions to the right.

So the move transports one unit of cyclic variation by exactly two transition slots unless it collides with another unit, in which case variation drops by two.

By reversing the cyclic order, the symmetric first-pair repair has the mirror law: it kills the central transition and toggles the transition bit two positions to the left.

### Corollary for minimum four-change cycles

If (C) is a globally minimum-variation cycle in a counterexample, with
[
q(C)=4,
]
then every available endpoint repair at a non-full transition must point toward a zero transition bit at distance two. Otherwise the repair produces a full-support cycle of variation (2), which cuts to a spanning one-change order and closes NOR.

Equivalently, in an extremal four-change cycle, non-full transition particles may move by two but may never have an available repair directed into another transition two slots away.

### Significance

This converts the full-support interval-reversal problem into local transition dynamics.

- Fully-curved tetrahedra are pinned universal switch particles, governed by the separate outer-bit toggle law.
- Non-fully-curved transitions are mobile particles: an endpoint repair moves them by two.
- A collision of mobile transition particles closes the conjecture immediately.

The canonical four-change profile (1,p,q,2) therefore becomes a four-particle configuration on a cycle. Closure can be attacked by showing that one of its particles is mobile toward another particle at distance two, or that repeated legal transport eventually forces such a collision.
