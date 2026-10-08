# The rooted singleton middle case is caged at both ends — preserved pre-item development

## Composition

(none yet)

## Development

## The rooted singleton-middle case is caged at both ends

Work in a minimum directed ternary counterexample. Let
[
D=(v_1,ldots,v_m)
]
be a one-change deletion order for the omitted vertex (x), with word
[
sigma,	au^q,qquad 	au=1-sigma,quad qge1.
]
Endpoint blocking at the front gives
[
h(x,v_1,v_2)=	au.
]
Hence
[
O=(x,v_1,v_2,ldots,v_m)
]
has linear word
[
	au,sigma,	au^q.
]

The (p=1) swap lemma gives
[
h(v_1,x,v_2)=	au,qquad h(x,v_2,v_3)=sigma,
]
so
[
O'=(v_1,x,v_2,v_3,ldots,v_m)
]
has the same linear word
[
	au,sigma,	au^q.
]

Endpoint blocking on the original deletion order gives
[
h(v_{m-1},v_m,x)=sigma.
	ag{1}
]

### Proposition

Counterexamplehood forces
[
h(v_m,x,v_1)=	au,
	ag{2}
]
[
h(v_{m-1},v_m,v_1)=sigma,
	ag{3}
]
and
[
h(v_m,v_1,x)=	au.
	ag{4}
]

Consequently the two cyclic orders
[
C=(x,v_1,v_2,ldots,v_m),
qquad
C'=(v_1,x,v_2,ldots,v_m)
]
have identical cyclic status words.

### Proof

For (C), the cyclic statuses are
[
	au,sigma,	au^q,sigma,w,
]
where the penultimate displayed (sigma) is (1) and
[
w=h(v_m,x,v_1).
]
Cut the cyclic coordinate order so that the first two statuses (	au,sigma) are precisely the two omitted wrap windows. The resulting spanning linear order has word
[
	au^q,sigma,w.
]
A counterexample requires at least two changes. Since the prefix is constant (	au), this is possible only when
[
w=	au.
]
This proves (2).

Apply the same argument to (C'). Its cyclic word is
[
	au,sigma,	au^q,z_1,z_2,
]
with
[
z_1=h(v_{m-1},v_m,v_1),
qquad
z_2=h(v_m,v_1,x).
]
Deleting the first two cyclic statuses gives the spanning linear word
[
	au^q,z_1,z_2.
]
For this binary word to have at least two changes, necessarily
[
z_1=sigma,qquad z_2=	au.
]
This proves (3)--(4).

Hence both cyclic orders have the same cyclic status sequence
[
	au,sigma,	au^q,sigma,	au.
]
(square)

### Interpretation

The shifted two-circuit
[
{x,v_1}
]
at tail ((v_2,v_3)) is not a purely front-local obstruction. The two circuit vertices are indistinguishable at the rear interface as well:
[
h(v_{m-1},v_m,x)=h(v_{m-1},v_m,v_1)=sigma,
]
and both cyclic closures return through color (	au):
[
h(v_m,x,v_1)=h(v_m,v_1,x)=	au.
]

Thus the rooted singleton-middle case is a two-ended cage whose two cyclic realizations are status-identical under swapping the circuit vertices.

A plausible next closure move is to apply the full-support interval-reversal inequalities simultaneously to these two status-identical cycles. The two cycles differ only by the transposition of (x,v_1); comparing the same reversal in both may force incompatible colors on a shared reconnection triangle.
