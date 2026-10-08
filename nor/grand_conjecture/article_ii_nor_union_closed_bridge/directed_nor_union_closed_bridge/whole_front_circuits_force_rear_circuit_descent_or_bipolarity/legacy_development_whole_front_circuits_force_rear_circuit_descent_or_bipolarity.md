# Whole-front circuits force rear circuit descent or bipolarity — preserved pre-item development

## Composition

(none yet)

## Development

## Whole-front circuits force rear circuit descent or bipolarity

Work in ternary arity. Let
[
P=(f_1,f_2,ldots,ell_1,ell_2)
]
be a maximal (sigma)-tight path in a directed-NOR counterexample, let
[
F=(f_1,f_2),qquad L=(ell_1,ell_2),qquad 	au=1-sigma,
]
and let
[
X=Vsetminus V(P).
]

Assume that (X) itself is a front circuit for the opposite-color family at (F):
[
X
otinmathcal F_{	au,F},
qquad
Ainmathcal F_{	au,F}quad	ext{for every }Asubsetneq X.
]
Thus every deletion (Xsetminus{x}) has a (	au)-tight witness ending at (F).

### Theorem 1: every omitted vertex is oppositely blocked at the rear

For each (xin X),
[
h(ell_1,ell_2,x)=	au.
]

#### Proof
Choose a (	au)-tight witness
[
W_x=(	ext{an ordering of }Xsetminus{x},F).
]
Splicing (W_x) to the suffix of (P) after (F) gives an order (D_x) of (Vsetminus{x}) whose status word consists of a (	au)-run followed by a (sigma)-run. Hence (D_x) has at most one change.

If
[
h(ell_1,ell_2,x)=sigma,
]
then appending (x) to (D_x) preserves the final (sigma)-run and gives a spanning order with at most one change, contradicting counterexamplehood. Therefore
[
h(ell_1,ell_2,x)=	au.
]
(square)

By reversal antisymmetry,
[
h(x,ell_2,ell_1)=sigma
]
for every (xin X). Thus every singleton of (X) is feasible in the color-(sigma) fixed-tail family at
[
L^{m rev}=(ell_2,ell_1).
]

### Theorem 2: the rear family must contain a circuit

The full support (X) is infeasible in
[
mathcal F_{sigma,L^{m rev}}.
]

#### Proof
Suppose instead that (Xinmathcal F_{sigma,L^{m rev}}). Choose a (sigma)-tight witness
[
Q=(	ext{an ordering of }X,L^{m rev}).
]
The reversal (P^{m rev}) is (	au)-tight and begins with (L^{m rev}). Splicing (Q) to the remainder of (P^{m rev}) gives a spanning order with a (sigma)-run followed by a (	au)-run, hence at most one change. Contradiction. (square)

Since every singleton of (X) is feasible at ((sigma,L^{m rev})) while (X) is not, choose an inclusion-minimal infeasible support
[
Dsubseteq X
]
for (mathcal F_{sigma,L^{m rev}}). Then (|D|ge2), and
[
mathcal F_{sigma,L^{m rev}}|_D=2^Dsetminus{D}.
]

### Corollary 3: strict circuit descent or a bipolar circuit

Exactly one of the following occurs.

1. **Strict rear descent:** (Dsubsetneq X). Then the rear end of (P) exposes a strictly smaller punctured-Boolean front circuit than the original whole-front circuit (X).

2. **Bipolar circuit:** (D=X). Then the same support (X) is a minimal infeasible circuit at both ends of (P), with opposite colors:
   [
   X	ext{ is a }	au	ext{-circuit at }F,
   qquad
   X	ext{ is a }sigma	ext{-circuit at }L^{m rev}.
   ]

In the second case every proper subset of (X) has tight witnesses from both poles, in opposite colors.

### Consequence

This is a terminating improvement mechanism for the clean whole-front-circuit case. Repeatedly pass from a whole-front circuit to the rear circuit supplied by Theorem 2. Whenever its support shrinks, circuit size strictly decreases. Therefore persistent failure of descent can occur only in the bipolar case, where one support is punctured-Boolean from both ends of the same maximal tight path.

The next closure target is correspondingly sharper: rule out bipolar circuits, or show that a bipolar circuit of size (d) yields a smaller whole-front circuit after recentering one of its facet witnesses. For (d=2,3), the previously classified two-hole and cyclic deletion-triple geometries provide the base rigid configurations.
