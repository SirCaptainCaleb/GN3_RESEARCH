# Twisted cubical Tucker route for status words

The full 0/1 status word of a spanning order has dimension n-2, exactly the dimension of the centered permutahedron boundary. Investigate whether the strong local consistency of these status labels upgrades the existing root-balance/Borsuk-Ulam argument to a cubical Tucker/Kuhn theorem that forces a two-cover.

# Twisted cubical Tucker route for status words

Let (m=n-2). For a spanning order (pi), define the sign status vector
[
lambda(pi)_i=2epsilon_i(pi)-1in{-1,+1},qquad 1le ile m.
]
Thus (lambda(pi)) is a vertex of the (m)-cube. This is dimensionally exact: the centered permutahedron has boundary dimension (m).

## Locality under adjacent transpositions

If (pi') is obtained from (pi) by swapping the entries in positions (k,k+1), then every consecutive triple outside the windows beginning at
[
k-2, k-1, k, k+1
]
is unchanged. Hence
[
lambda_i(pi')=lambda_i(pi)
]
for every (i
otin{k-2,k-1,k,k+1}cap[m]).

This is the natural discrete-continuity property of the raw status labeling. It is stronger information than the extreme coordinates (p,q). In particular (p) and (q) themselves are not locally Lipschitz: changing one of the four affected statuses can delete the first zero or last one and make the corresponding extreme index jump arbitrarily far.

## Twisted antipodality

Let (J) reverse the (m) status coordinates:
[
(Jz)_i=z_{m+1-i}.
]
Boundary antisymmetry gives
[
lambda(pi^{m rev})=-Jlambda(pi).
]
Thus the raw cubical labeling is not an ordinary Tucker labeling, for which one would require (lambda(pi^{m rev})=-lambda(pi)).

The involution (-J) on (mathbb R^m) decomposes into an odd subspace and a fixed subspace. The odd subspace is the (J)-symmetric subspace, of dimension (lceil m/2ceil); the fixed subspace is the (J)-antisymmetric subspace, of dimension (lfloor m/2floor). Therefore antipodality alone cannot force a zero of an interpolation of the full status vector.

For even (m), this failure is visible combinatorially: a constant anti-palindromic status word such as
[
00cdots 0011cdots 11
]
is fixed by the twisted involution and may be bad for the two-cover criterion. A constant labeling of this form satisfies the twisted symmetry and adjacent-edge locality abstractly. Thus those two axioms alone are insufficient; the fact that the coordinates come from one common boundary-tournament triple function is essential.

## A canonical odd half-dimensional status map

For (1le i<m+1-i), define
[
s_i(pi)=lambda_i(pi)+lambda_{m+1-i}(pi)in{-2,0,2}.
]
If (m) is odd, retain the middle coordinate (s_{(m+1)/2}=lambda_{(m+1)/2}). Then
[
s(pi^{m rev})=-s(pi).
]
Thus (s) is a canonical ordinary odd labeling into (mathbb R^{lceil m/2ceil}).

After an equivariant piecewise-linear extension over the centered permutahedron boundary, Bourgin--Yang gives a zero set of dimension at least
[
m-lceil m/2ceil=lfloor m/2floor.
]
So the raw status geometry forces a large family of carrier faces on which all mirrored status-pair sums balance simultaneously.

At a zero carrier, for each mirrored pair (i,j=m+1-i), positive chamber weights balance
[
lambda_i+lambda_j.
]
Hence either some occurring chamber has opposite statuses at (i,j), or the carrier contains both an all-tight witness (11) and an all-nontight witness (00) at that pair. This is a much more literal (0/1)-balance statement than the root circulation.

## Locality of the mirrored-pair coordinates

If (j-i>3), no adjacent transposition can affect both status positions (i) and (j). Therefore along an actual permutahedron edge the coordinate (s_i) cannot jump directly from (-2) to (+2) or vice versa: one of the two bits would have to pass through the mixed value (s_i=0).

This is closely analogous to the no-opposite-directions-on-neighboring-grid-points hypothesis in discrete direction-preserving fixed-point theorems.

A natural Tucker label is to choose, from (s(pi)), the first nonzero coordinate together with its sign. Reversal gives the opposite label. If a Tucker-type theorem could force opposite labels on an actual permutahedron edge, then every such edge at a mirrored pair farther than distance three from the center would be impossible by the locality just proved. The forced complementary edge would therefore have to occur at one of only (O(1)) central mirrored pairs, where the two status positions are close enough to be altered together.

The present technical obstruction is that ordinary triangulations of the permutahedron introduce diagonal edges. Tucker's complementary edge may therefore join two permutations that are not adjacent transpositions, and the four-coordinate locality no longer applies directly. A useful theorem would need to work on the permutahedral cell complex itself, on its dual Coxeter complex with chamber labels, or otherwise preserve adjacency/cell distance strongly enough to exploit the local window rule.

## Relation to the current root topology

The inversion root
[
psi(pi)=e_{p(pi)}-e_{c(pi)}
]
is a nonlinear full-dimensional compression of the status word that restores ordinary oddness:
[
psi(pi^{m rev})=-psi(pi).
]
Its labels are type-(A) roots. A zero convex combination of such roots is a positive circulation, and minimal positive dependencies of type-(A) roots are directed cycles. Consequently a Tucker/Borsuk-Ulam theorem formulated only for the root polytope is expected to reproduce essentially the existing directed-cycle conclusion rather than strengthen it.

The possible gain comes from retaining the full (0/1) status data and combining it with adjacency locality.

## Why the memory lift does not immediately solve the twist

The memory lift projects antipodally to the original cube and its edge colors are complemented by the antipodal involution, but the color of an edge depends on the preceding and following directions stored in the lift. There is no immediate canonical sign vector attached to a base cube vertex whose antipode is coordinatewise negation. Thus applying an ordinary cubical fixed-point theorem directly to the base cube would discard the two-step memory that defines GN3 tightness.

## Research targets

1. Find or prove a Tucker/Ky Fan lemma for a centrally symmetric simple cell decomposition, or for chamber labels on the dual Coxeter complex, whose forced opposite labels are adjacent chambers rather than arbitrary diagonal vertices of a triangulation.
2. Apply it to the odd mirrored-status labeling (s), using the fact that far mirrored coordinates cannot reverse sign in one adjacent transposition.
3. Translate the resulting forced central mixed-status configuration back into the inversion-window criterion (qle p+1), or at least into a new bounded-width structural conclusion.
4. Use full triple consistency, not merely twisted antipodality plus locality; the latter are provably too weak in even dimension.
