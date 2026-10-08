# Nearest-violation selection removes the disjoint two-cycle lifted zero — preserved pre-item development

## Composition

(none yet)

## Development

## Nearest-violation selection removes the disjoint two-cycle lifted zero

Use the honest ternary switch-prism lift with the following fixed reversal-compatible selector: at every bad switch state choose a violating ternary window of minimum distance from the proposed cut, with any deterministic reversal-compatible tie rule.

The degree theorem remains valid for this selector.

Let a support-minimal lifted zero be the union of two vertex-disjoint directed physical cycles on coordinate sets A and B, with

A disjoint B,
A union B=V,

and opposite nonzero side imbalances.

Root §189 shows that the lifted labels span a codimension-one subspace H of W direct-sum R. Their physical projections span exactly

W_A direct-sum W_B.

Hence any honest lifted label whose physical root crosses between A and B is transverse to H.

### Construct a switch state whose nearest violation crosses A|B

By minimum-counterexamplehood, choose NOR-good spanning orders

g(A), g(B)

on the two proper coordinate sets. Form the full coordinate order

pi=g(A) g(B).

There are exactly two ternary windows crossing the concatenation boundary:

L=(last two coordinates of A, first coordinate of B),
R=(last coordinate of A, first two coordinates of B).

All other windows sufficiently near the boundary lie wholly in one side.

Fix the global threshold polarity eta of the switch prism.

First put the cut between the ranks of L and R. Then L is on the pre side with target eta and R is on the post side with target 1-eta.

If either L or R violates, a nearest violating window is one of these crossing windows, because both are at distance zero/one from the cut while every purely internal window is farther. Its physical first-minus-last root has one endpoint in A and one in B, so its lifted label is transverse to H.

Suppose instead both crossing windows match. Then

color(L)=eta,
color(R)=1-eta.

Move the cut one window rank to the LEFT, immediately before L. Now L lies on the post side, whose target is 1-eta. Since color(L)=eta, L becomes a violation.

It is the nearest possible violating window to the new cut and is crossing. Therefore the nearest-violation selector chooses a crossing window (or, under a tie, may choose another equally nearest crossing window; there is no internal window closer).

Thus in all cases one of these two adjacent cut positions yields an honest selected lifted label

widehat sigma=(sigma,t)

with sigma notin W_A direct-sum W_B.

Hence widehat sigma notin H.

### Local removal

The disjoint two-cycle lifted zero is support-minimal and lies in the codimension-one subspace H. Subdivide its zero simplex by an interior vertex carrying the transverse genuine switch-state label widehat sigma and cone its boundary to that vertex.

Projection to (W direct-sum R)/H excludes zeros on every cone simplex containing the new vertex; the old proper faces are zero-free by support minimality.

Therefore the disjoint two-cycle lifted zero is locally removable relative to its boundary.

### Consequence

Under nearest-violation selection, all support-minimal lifted zero types from §§187-189 are removable except the dimension-saturated case of two opposite-imbalance physical cycles covering V and meeting in exactly one coordinate.

The one-vertex figure-eight is the sole remaining support-minimal lifted circuit shape.
