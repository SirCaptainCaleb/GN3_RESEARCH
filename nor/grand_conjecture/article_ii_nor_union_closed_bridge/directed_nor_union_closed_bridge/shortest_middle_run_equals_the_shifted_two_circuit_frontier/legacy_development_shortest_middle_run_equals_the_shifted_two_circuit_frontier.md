# Shortest middle run equals the shifted two-circuit frontier — preserved pre-item development

## Shortest middle run equals the shifted two-circuit frontier

Work in a minimum directed ternary counterexample. Delete a vertex (x), and choose a one-change order
[
D=(v_1,ldots,v_m)
]
with status word
[
sigma^p	au^q,qquad 	au=1-sigma,quad p,qge1.
]
Endpoint blocking forces
[
h(x,v_1,v_2)=	au.
]
Thus the spanning order
[
O=(x,v_1,ldots,v_m)
]
has two-change word
[
	au,sigma^p	au^q.
]

Assume the middle run has minimum possible length among all spanning two-change orders obtainable in the counterexample, and consider the base case (p=1). Then
[
O
]
has word
[
	au,sigma,	au^q.
]

Swap the first two coordinates:
[
O'=(v_1,x,v_2,v_3,ldots,v_m).
]
Write
[
A=h(v_1,x,v_2),qquad B=h(x,v_2,v_3).
]
Every later status is (	au). If ((A,B)) were any of
[
(	au,	au),quad(sigma,sigma),quad(sigma,	au),
]
the word (A,B,	au,	au,ldots) would have at most one change. Counterexamplehood therefore forces
[
A=	au,qquad B=sigma.
]

Since the original deletion order has
[
h(v_1,v_2,v_3)=sigma,
]
we obtain
[
h(x,v_2,v_3)=h(v_1,v_2,v_3)=sigma,
]
while
[
h(x,v_1,v_2)=h(v_1,x,v_2)=	au.
]

Therefore the support
[
{x,v_1}
]
is a two-element minimal infeasible support for the color-(sigma) fixed-tail family at
[
(v_2,v_3).
]
Indeed both singletons are (sigma)-feasible there, but the only two possible pair orders fail in their first window.

So the minimum-middle-run case (p=1) is not a new obstruction: it is exactly the shifted two-circuit frontier already isolated by Article II's insertion-sliding analysis.

This gives a useful equivalence between the full-support extremal-cycle language and the local support-circuit language. A closure proof can therefore target either:
- eliminate shifted two-circuits in the presence of their ambient one-change deletion tail; or
- prove that a minimum two-change order must have middle run (p=1), thereby reducing the full minimum-counterexample problem to the two-circuit case.
