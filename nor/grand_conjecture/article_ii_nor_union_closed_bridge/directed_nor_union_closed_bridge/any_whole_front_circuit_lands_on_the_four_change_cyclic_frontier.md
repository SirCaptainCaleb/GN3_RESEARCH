# Any whole-front circuit lands on the four-change cyclic frontier

## Composition

(none yet)

## Development

## Any whole-front circuit lands on the four-change cyclic frontier

Work in a minimum counterexample to directed ternary NOR. Let
[
P=(f_1,f_2,ldots,r_1,r_2)
]
be a maximal (sigma)-tight path, let
[
X=Vsetminus V(P),qquad 	au=1-sigma,
]
and assume that the whole omitted set (X) is a minimal infeasible support in the opposite-color front family:
[
mathcal F_{	au,(f_1,f_2)}|_X=2^Xsetminus{X}.
]
Put
[
d=|X|ge2,qquad p=|P|-2.
]

Fix (xin X). Choose a (	au)-tight facet witness
[
W_x=(u_1,ldots,u_{d-1},f_1,f_2)
]
for (Xsetminus{x}).

Because (X) itself is infeasible, (x) is blocked at the exposed front:
[
h(x,u_1,u_2)=sigma
]
(with the evident (d=2) interpretation (h(x,u_1,f_1)=sigma)).

Hence the spanning order
[
S_x=(x,u_1,ldots,u_{d-1},P)
]
has linear status word
[
sigma,	au^{d-1},sigma^p.
	ag{1}
]

Now delete the initial vertex (x). The remaining order
[
D_x=(u_1,ldots,u_{d-1},P)
]
is a one-change order of (Vsetminus{x}), with word
[
	au^{d-1}sigma^p.
]
Endpoint blocking for the omitted vertex (x) at the rear gives
[
h(r_1,r_2,x)=	au.
	ag{2}
]

Regard (S_x) as a cyclic order. Besides its linear statuses, the two wrap statuses are
[
z_1=h(r_1,r_2,x)=	au,
qquad
z_2=h(r_2,x,u_1)in{sigma,	au}.
]
Thus the cyclic word is
[
sigma, 	au^{d-1}, sigma^p, 	au, z_2.
	ag{3}
]

If (z_2=	au), the cyclic run lengths are
[
1, d-1, p, 2.
]
If (z_2=sigma), the final (sigma) merges cyclically with the initial singleton (sigma), giving
[
2, d-1, p, 1.
]
After cyclic rotation and reversal, both cases have canonical run profile
[
1, p, d-1, 2.
	ag{4}
]

In particular the cyclic variation is exactly four. It cannot be two, because a two-change cyclic word can be cut at a change boundary to give a spanning linear order with at most one change.

### Consequence

The bipolar hypothesis is unnecessary for reaching Article I's canonical four-change frontier. A single whole-front punctured-Boolean circuit already produces that geometry, with one middle run length equal to
[
|X|-1.
]

Thus:
- (|X|=2) lands in the singleton-middle-run regime;
- (|X|=3) lands in the two-window middle-run regime;
- arbitrary whole-front circuits land on the same interval-reversal frontier with residual run length (|X|-1).

The remaining issue is therefore not bipolarity but **promotion**: given an arbitrary proper front circuit (Usubsetneq X), can one recenter or enlarge the monochromatic core so that (U) becomes the whole omitted set? A positive promotion theorem would reduce every Article-II circuit obstruction directly to Article I's four-change cyclic problem.
