# Short flat phases reduce to one explicit boundary scan — preserved pre-item development

## Composition

(none yet)

## Development

## Short flat phases reduce to one explicit boundary scan

Work in the coboundary-flat alternating ternary sector. Let
[
O=(v_1,ldots,v_m)
]
be a one-change deletion carrier with word
[
0^p1^q
]
and omitted coordinate (x). Put
[
s_i=alpha(x,v_i,v_{i+1}).
]
Assume every insertion of (x) into (O) fails to give a spanning one-change order.

### The case (p=1) is impossible

Prepending (x) gives word
[
s_1,0,1^q.
]
If (s_1=0), this is already one-change, so blocking forces (s_1=1).

Now insert (x) between (v_1) and (v_2). The first two new statuses are
[
alpha(v_1,x,v_2)=1-s_1=0,
qquad
alpha(x,v_2,v_3)=s_2,
]
and every later untouched status is (1).

If (s_2=0), the full word begins (0,0,1^*); if (s_2=1), it begins (0,1^*). Either way there is at most one change. Contradiction.

Hence no blocked deletion carrier has (p=1).

### The case (p=2)

Now
[
w_1=w_2=0,qquad w_i=1quad(ige3).
]

Prepending again forces
[
s_1=1.
]
Insert (x) after (v_1). The local word is
[
0,s_2,0,1^*.
]
If (s_2=0), this is one-change, so
[
s_2=1.
]

For every insertion gap sufficiently inside the old (1)-phase, the unchanged prefix already contains a (0) and the unchanged suffix contains a (1). The insertion packet is
[
(s_{i-1},,1-s_i,,s_{i+1}).
]
For the full word to remain bad, this packet cannot be monotone (0^*1^*). A direct binary check gives
[
s_{i-1}ge s_ige s_{i+1}.
]
Starting at the first such gap yields
[
s_3ge s_4gecdots.
]
Thus the tail scan is nonincreasing.

If (s_3=1), replace (v_2) by (x):
[
O'=(v_1,x,v_3,v_4,ldots,v_m).
]
Flatness on ({x,v_1,v_2,v_3}) gives
[
alpha(x,v_1,v_3)
=
s_1oplus w_1oplus s_2
=
1oplus0oplus1
=
0.
]
Therefore
[
alpha(v_1,x,v_3)=1,
]
while
[
alpha(x,v_3,v_4)=s_3=1,
]
and every later untouched status is also (1). Hence (O') is a monochromatic deletion path. The near-spanning monochromatic-path lemma then closes NOR.

Therefore a surviving blocked (p=2) carrier must have
[
s_3=0.
]
Since the tail scan is nonincreasing,
[
oxed{s=11,0,0cdots0.}
]

### Consequence

The only short first-phase case not already closed is the explicit boundary scan
[
p=2,qquad s=110^*.
]
By reversal/color normalization, the only (q=2) residue is its mirror.

Thus the applicability gap in the arbitrary-scan replacement dynamics is not an uncontrolled family of short phases; it reduces to one explicit endpoint scan and its reverse.
