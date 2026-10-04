# An odd auxiliary violation vector with one-change chamber zeros

**Summary:** Pair left/right violations at equal distance from the auxiliary vertex. Any antipodal ±1 gauge—especially the relative order of two fixed vertices—turns these pairs into an odd {-1,0,1}-valued vector whose zero chambers are exactly the directed one-change orders.

## Statement

Let H^+ be an auxiliary extension with distinguished r. For an order pi, let x_d,y_d indicate left-zero and right-one violations at equal distance d from r. Let g(pi) in {±1} satisfy g(pi^rev)=-g(pi), and define F_d=x_d-y_d+g x_d y_d. Then F(pi^rev)=-F(pi), and F(pi)=0 iff pi has no violations, equivalently pi is a directed one-change order. One may take g=g_ab, the sign of the relative order of any fixed pair a,b; this gauge changes under an adjacent transposition only when that transposition swaps a and b.

## Body

# An odd auxiliary violation vector with one-change chamber zeros

Let `H^+` be an auxiliary extension with distinguished vertex `r`. Take a spanning order `pi` and suppose `r` occurs in position `t`. The auxiliary construction forces a tight status immediately before the window centered at `r` and a non-tight status immediately after it.

For each distance `d>=1`, let

`x_d(pi)=1`

when the status `d` steps farther left is a non-tight **left violation**, and let

`y_d(pi)=1`

when the status `d` steps farther right is a tight **right violation**. Missing positions beyond an endpoint are declared nonviolations. Reversal-complement symmetry gives

`x_d(pi^rev)=y_d(pi)`, `y_d(pi^rev)=x_d(pi)`.

Let

`g:{spanning orders}->{+1,-1}`

be any antipodal sign:

`g(pi^rev)=-g(pi)`.

Define

`F_d(pi)=x_d(pi)-y_d(pi)+g(pi)x_d(pi)y_d(pi)`.

For one distance the four possibilities are

- `(x_d,y_d)=(0,0)`: `F_d=0`;
- `(1,0)`: `F_d=+1`;
- `(0,1)`: `F_d=-1`;
- `(1,1)`: `F_d=g(pi)`.

Therefore

`F_d(pi^rev)=-F_d(pi)`

for every `d`, and hence `F(pi^rev)=-F(pi)`. Moreover `F_d(pi)=0` exactly when neither violation occurs at distance `d`. Consequently

`F(pi)=0`

if and only if there are no violations at any distance, which is precisely the directed one-change condition in the auxiliary extension.

## A locality-friendly gauge

Fix two distinct original vertices `a,b` and define

`g_ab(pi)=+1` if `a` occurs before `b`,

`g_ab(pi)=-1` if `b` occurs before `a`.

Reversal reverses their relative order, so `g_ab(pi^rev)=-g_ab(pi)`. More importantly, an adjacent transposition changes `g_ab` only when it directly swaps `a` and `b`. Thus the double-violation tie breaker can be made almost completely inert under the adjacent-transposition geometry of the permutahedron.

The construction needs no minimum-counterexample hypothesis. The auxiliary middle-r tournament is one possible source of an antipodal gauge, but it is not necessary.

## Metadata

- ID: auxiliary_violation_vector_has_exact_chamber_zeros
- Kind: toolkit
- Version: 2
- Math version: 2
- Audit: unaudited
- Refutation: unrefuted
- Toolkit status: Limbo
