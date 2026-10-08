# Adjacent swapping across a fully curved transition toggles the two outer change bits — preserved pre-item development

## Composition

(none yet)

## Development

## Adjacent swapping across a fully curved transition toggles the two outer change bits

Let
[
C=(ldots,p,a,b,c,d,q,ldots)
]
be a cyclic coordinate order in a pure alternating triangle orientation. Write
[
c_i=alpha(a,b,c),qquad
c_{i+1}=alpha(b,c,d),
]
and suppose the tetrahedron
[
Q={a,b,c,d}
]
is fully curved. Then necessarily
[
c_i
e c_{i+1}.
]

Swap the adjacent coordinates (c,d), obtaining locally
[
(ldots,p,a,b,d,c,q,ldots).
]

### Lemma 1: the central status pair is swapped

The two statuses supported entirely on (Q) become
[
c'_i=alpha(a,b,d)=c_{i+1},
]
[
c'_{i+1}=alpha(b,d,c)=c_i.
]

The second identity follows from reversal of the last two entries and (c_i
e c_{i+1}); the first is the corresponding face relation in a fully-curved tetrahedron.

The next status changes by a transposition:
[
c'_{i+2}
=
alpha(d,c,q)
=
1-alpha(c,d,q)
=
1-c_{i+2}.
]
All statuses before (c_i) except the immediately adjacent boundary status, and all statuses after (c_{i+2}), are unchanged.

Equivalently, on the local status triple
[
(c_i,c_{i+1},c_{i+2})
=
(a,b,z),
qquad a
e b,
]
the swap acts as
[
(a,b,z)longmapsto(b,a,1-z).
	ag{1}
]

### Lemma 2: transition-bit transport

Let
[
d_j=c_joplus c_{j+1}
]
be the cyclic transition bits. Under the swap:

- the transition carried by the fully-curved tetrahedron remains (1);
- the next transition bit is unchanged;
- the two transition bits immediately outside this local pair are toggled.

In particular the change in total cyclic variation is
[
Delta q
=
2-2(d_{m left}+d_{m right}),
]
where (d_{m left},d_{m right}in{0,1}) are the two outer transition bits toggled by the move.

Hence:
- if both outer bits are (1), then (q) drops by (2);
- if exactly one is (1), (q) is unchanged;
- if neither is (1), (q) rises by (2).

### Corollary: extremal four-change cycles constrain fully-curved transitions

If (C) has globally minimum cyclic variation (q(C)=4) in a counterexample, then no fully-curved transition may have both outer toggled transition bits equal to (1). Otherwise the adjacent swap produces a full-support cyclic order of variation (2), which can be cut to a spanning one-change linear order.

Thus universal-switch tetrahedra are not stationary in an extremal four-change cycle: their neighboring change pattern is constrained by the adjacent-swap transport rule.
