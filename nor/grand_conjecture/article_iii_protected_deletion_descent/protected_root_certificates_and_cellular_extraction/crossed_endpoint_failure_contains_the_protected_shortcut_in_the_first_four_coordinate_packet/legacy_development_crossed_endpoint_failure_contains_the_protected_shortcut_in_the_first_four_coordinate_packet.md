# Crossed endpoint failure contains the protected shortcut in the first four-coordinate packet — preserved pre-item development

## Development

## Crossed endpoint failure contains the protected shortcut immediately

Continue from §304. In either crossed endpoint type,
[
A=alpha(x,w_1,w_2),qquad
B=alpha(z,w_1,w_2)
]
satisfy
[
A
e B,
]
and the pair bit
[
E=alpha(x,z,w_1)
]
satisfies
[
E=A.
]

Indeed Type I is
[
(A,B;E)=(1,0;1),
]
while Type II is
[
(A,B;E)=(0,1;0).
]

Put
[
R_1=E,qquad R_2=alpha(x,z,w_2).
]
Tetrahedral parity gives
[
R_2oplus R_1=Aoplus B=1.
]
Since (R_1=A), this yields
[
R_2=B.
]

Now consider the four-coordinate full-order packet
[
oxed{(x,w_1,w_2,z)}.
]

Its two consecutive statuses are
[
alpha(x,w_1,w_2)=A,
qquad
alpha(w_1,w_2,z)=B
]
by cyclic invariance. Thus it is a genuine transition.

Its physical transition root is therefore
[
oxed{x	o z}.
]

### Curvature

The two off-faces are
[
alpha(x,w_1,z)=1-alpha(x,z,w_1)=1-R_1=B,
]
and
[
alpha(x,w_2,z)=1-alpha(x,z,w_2)=1-R_2=A.
]

Hence the off-face pair is
[
(B,A),
]
the reverse of the transition pair ((A,B)). This is exactly the fully-curved pattern.

Therefore
[
oxed{(x,w_1,w_2,z)	ext{ is a fully-curved carrier of the protected root }x	o z.}
]

### Theorem

The crossed two-coordinate endpoint residue of §304 never requires ladder transport, pair insertion, or a later extraction theorem to realize the certified shortcut.

Its first middle edge already gives a four-coordinate fully-curved carrier of the desired ordered shortcut (x	o z).

Thus the entire crossed shortcut branch closes locally.

### General rail-disagreement audit

More generally, with
[
X_i=alpha(x,w_i,w_{i+1}),quad
Z_i=alpha(z,w_i,w_{i+1}),quad
R_i=alpha(x,z,w_i),
]
any disagreement
[
X_i
e Z_i
]
makes
[
(x,w_i,w_{i+1},z)
]
a transition carrier with root (x	o z).

Its off-faces are
[
1-R_i,qquad 1-R_{i+1}.
]
Using
[
R_{i+1}=R_ioplus X_ioplus Z_i=1-R_i,
]
the off-face pair is
[
1-R_i, R_i.
]

Therefore:
- if (X_i=R_i), the carrier is fully curved;
- if (X_i
e R_i), the carrier is flat.

This corrects the curvature assignment stated in §322: misaligned disagreements still realize the physical shortcut (x	o z), but as flat carriers; aligned disagreements are the protected fully-curved ones.

At the crossed endpoint of §304 one always has (X_1=R_1), so the shortcut is protected immediately.
