# Every deletion state has a canonical bounded central-bridge three-cover

## Statement

Let H be a minimum counterexample and H-x=P|Q an exact deletion two-cover with P=(p0,...,pm), Q=(q0,...,qs). Then H has a spanning three-path cover whose central component is supported on the join window and has order either three or five: if (pm,x,q0) is tight, use (p0,...,p_{m-1}) | (pm,x,q0) | (q1,...,qs); if it is non-tight, use (p0,...,p_{m-2}) | (q1,q0,x,pm,p_{m-1}) | (q2,...,qs).

## Body

Let (H) be a minimum counterexample and let
[
H-x=P|Q
]
be an exact two-path cover, where
[
P=(p_0,ldots,p_m),qquad Q=(q_0,ldots,q_s).
]
Every component of a one-vertex deletion cover in a minimum counterexample has order at least three, so (m,sge2).

The two outer join triples are non-tight:
[
(p_{m-1},p_m,x)quad	ext{and}quad(x,q_0,q_1).
]
Otherwise (x) could be appended to (P) or prepended to (Q), giving a spanning two-cover.

By boundary antisymmetry their reversal mates are tight:
[
(x,p_m,p_{m-1})
quad	ext{and}quad
(q_1,q_0,x).
]

Now distinguish the middle join triple.

### Case 1: ((p_m,x,q_0)) is tight

Then
[
C=(p_m,x,q_0)
]
is a tight three-path. The inherited contiguous subpaths
[
P^-=(p_0,ldots,p_{m-1}),
qquad
Q^+=(q_1,ldots,q_s)
]
are tight, pairwise disjoint from (C), and their supports partition (V(H)).

Hence
[
P^-|C|Q^+
]
is a spanning three-path cover with central component of order three.

### Case 2: ((p_m,x,q_0)) is non-tight

Boundary antisymmetry gives
[
(q_0,x,p_m)
]
tight. Together with the two already forced reversed outer joins,
[
(q_1,q_0,x),qquad (x,p_m,p_{m-1}),
]
this makes
[
C=(q_1,q_0,x,p_m,p_{m-1})
]
a tight five-path.

The inherited contiguous subpaths
[
P^{--}=(p_0,ldots,p_{m-2}),
qquad
Q^{++}=(q_2,ldots,q_s)
]
are tight and nonempty, and together with (C) partition (V(H)).

Hence
[
P^{--}|C|Q^{++}
]
is a spanning three-path cover with central component of order five.

Therefore every exact deletion state admits a canonical spanning three-cover obtained by replacing its width-three defect window by one bounded tight bridge component of order (3) or (5). No reversal of a tight path is used.
