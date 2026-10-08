# Minimum middle runs force a shifted two circuit or one crossed local pattern — preserved pre-item development

## Development

## Minimum middle runs force a shifted two-circuit or one crossed local pattern

Work in a directed ternary minimum counterexample. Among all spanning coordinate orders with exactly two changes, choose one whose middle color run has minimum positive length. Using a minimum-counterexample deletion order and endpoint blocking, write such an order in the form
[
O=(x,v_1,ldots,v_m)
]
with status word
[
	au,sigma^p,	au^q,
qquad p,qge1,qquad 	au=1-sigma,
]
and take (p) minimum. Assume (p>1).

Swap the first two coordinates:
[
O'=(v_1,x,v_2,v_3,ldots,v_m).
]
Write
[
A=h(v_1,x,v_2),qquad B=h(x,v_2,v_3).
]
All later statuses are exactly those of the deletion order beginning with its second status, namely
[
sigma^{p-1}	au^q.
]

There are four possibilities.

1. If
[
(A,B)=(sigma,sigma),
]
then (O') has word
[
sigma^p	au^q,
]
with only one change, contradiction.

2. If
[
(A,B)=(	au,	au),
]
then (O') has word
[
	au^2sigma^{p-1}	au^q,
]
which has exactly two changes but middle run length (p-1), contradicting the minimality of (p).

Therefore
[
A
e B.
]

If
[
(A,B)=(	au,sigma),
]
then
[
h(x,v_2,v_3)=h(v_1,v_2,v_3)=sigma,
]
while
[
h(x,v_1,v_2)=h(v_1,x,v_2)=	au.
]
Hence both singleton supports ({x},{v_1}) are (sigma)-feasible at tail ((v_2,v_3)), while both possible two-element orderings fail in their first window. Thus
[
{x,v_1}
]
is a shifted two-element front circuit for color (sigma) at ((v_2,v_3)).

The only remaining possibility is the **crossed pattern**
[
h(v_1,x,v_2)=sigma,
qquad
h(x,v_2,v_3)=	au.
]

### Consequence

Every minimum-middle-run spanning two-change order with (p>1) exposes either:
- the shifted two-circuit frontier; or
- this single crossed local pattern.

Thus proving that the crossed pattern can be repaired, shifted, or converted into a shorter-middle-run order would force (p=1), and the previously proved (p=1) theorem would reduce the full minimum-counterexample problem to a shifted two-circuit.
