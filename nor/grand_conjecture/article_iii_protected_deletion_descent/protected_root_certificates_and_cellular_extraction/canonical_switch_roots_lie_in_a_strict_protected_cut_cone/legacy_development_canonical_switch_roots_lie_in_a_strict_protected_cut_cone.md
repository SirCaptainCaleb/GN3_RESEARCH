# Canonical switch roots lie in a strict protected cut cone — preserved pre-item development

## Composition

(none yet)

## Development

## Canonical switch roots lie in a strict protected cut cone

Let
[
O=(v_1,ldots,v_m)
]
be a one-change deletion order with word
[
0^p1^q
]
in a minimum coordinate counterexample of ordered-tuple arity (r), and let (x) be the omitted coordinate.

Insert (x) immediately after (v_p):
[
F=(v_1,ldots,v_p,x,v_{p+1},ldots,v_m).
]

By the switch-insertion theorem, (F) has an internal protected descent
[
10
]
between two consecutive (r)-windows which both contain (x).

Let those windows start at consecutive ranks (i,i+1). Sliding from the first to the second drops one old coordinate (a) and enters one old coordinate (c), giving the protected root
[
ho=e_a-e_c.
]

### Theorem: strict cut orientation

Every such canonical switch root satisfies
[
ain{v_1,ldots,v_p},
qquad
cin{v_{p+1},ldots,v_m}.
]

In particular (ho_x=0).

### Proof

In (F), the inserted coordinate (x) occupies position (p+1).

For both consecutive (r)-windows starting at (i) and (i+1) to contain (x), one must have
[
ile p+1le i+r-1
]
and
[
i+1le p+1le i+r.
]
Hence
[
p-r+2le ile p.
]

The coordinate dropped in the slide is the coordinate of (F) at position (i). Since (ile p), this is an old coordinate among
[
v_1,ldots,v_p.
]

The entering coordinate is the coordinate of (F) at position (i+r). Since
[
i+rge p+2,
]
it lies strictly to the right of (x), among
[
v_{p+1},ldots,v_m.
]

Thus every canonical root crosses the protected deletion cut from left to right. QED.

### Strict cone

Let
[
L={v_1,ldots,v_p},
qquad
R={v_{p+1},ldots,v_m}.
]
All canonical switch roots for this witness lie in
[
C_{L|R}
=
operatorname{cone}{e_a-e_c:ain L, cin R}.
]

Pair with the cut functional
[
phi_{L|R}(e_v)=
egin{cases}
+1,&vin L,\
-1,&vin R,\
0,&v=x.
end{cases}
]
Then every nonzero canonical root satisfies
[
phi_{L|R}(ho)=2>0.
]

Therefore no positive Radon dependence can use only canonical roots from one fixed deletion witness.

### Reversal

Reversing the deletion order exchanges (L) and (R), complements the window colors, and sends the corresponding physical root to
[
-ho.
]

Thus the canonical root certificates naturally form antipodal strict cut cones.

### Consequence for extraction

Any positive dependence
[
sum_jlambda_jho_j=0,
qquadlambda_j>0,
]
among canonical protected roots must involve at least two genuinely different protected cuts. Interpreting each root as the directed physical edge
[
c_j	o a_j,
]
the dependence is a circulation and decomposes into coordinate cycles.

Hence the general-uniformity topology no longer needs to prove root existence. Its exact job is:

> force a compatible cycle across several protected cut cones, then convert a shortest physical root cycle into a monotone replacement bridge.

This is the protected-root analogue of extracting a spanning path from the switch-prism carrier.
