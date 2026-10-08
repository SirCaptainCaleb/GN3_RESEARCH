# Endpoint partner defects are Johnson square holonomy

## Composition

(none yet)

## Development

Consider the endpoint-induced rank-two protected cycle
rho_i=e_{x_i}-e_{x_{i+1}},
C_i={x_i,a_i},
with forced successor
C_i^+={x_{i+1},a_i}
and next attained cut
C_{i+1}={x_{i+1},a_{i+1}}.

Thus each chronological step in the cut data is a two-edge path in J(n,2):
{x_i,a_i}
 -> {x_{i+1},a_i}
 -> {x_{i+1},a_{i+1}}.
The first edge is the ACTUAL protected endpoint root direction. The second edge is the unit cut-defect/partner exchange.

Assume first that x_i,x_{i+1},a_i,a_{i+1} are four distinct coordinates. Then these two edges are two adjacent sides of the canonical Johnson square with fourth vertex
M_i={x_i,a_{i+1}}.
The opposite two-edge route is
{x_i,a_i}
 -> {x_i,a_{i+1}}
 -> {x_{i+1},a_{i+1}}.
Geometrically, the square simply commutes the partner exchange past the physical root exchange.

If one of the four coordinates coincides subject to the endpoint exclusions a_i notin {x_i,x_{i+1}}, the square degenerates to a Johnson triangle. Those are precisely the low-support cases where A2/A3 local extraction may apply.

Therefore the partner-defect circulation has an exact holonomy interpretation: the physical x-cycle is the base motion, the partner a is a rank-two fiber coordinate, and every change a_i->a_{i+1} measures failure to commute base transport with fiber transport.

This identifies a sharp witness-realization lemma.

ENDPOINT SQUARE-LIFT LEMMA (missing). Given consecutive endpoint witnesses realizing the first and third corners
{x_i,a_i}, {x_{i+1},a_{i+1}}
together with the protected horizontal edge through {x_{i+1},a_i}, either:
1. the missing corner {x_i,a_{i+1}} is realized by a legal endpoint/deletion witness in a way that realizes the commuted square; or
2. the local four/five-coordinate surgery gives a strict protected improvement or full one-change order.

If this lemma holds, any partner change can be pushed one step backward through the physical cycle by a legal square move. Repeatedly commute one chosen partner jump around the cycle. Because the total partner defect telescopes, the transported jumps eventually meet inverse jumps and cancel, unless a degenerate triangle is encountered; the latter is a local low-rank extraction problem. Consequently a minimal witness-supported endpoint cycle would have constant partner and hence exact zero cut defect.

This consequence is CONDITIONAL on witness-supported square lifting. The abstract Johnson square always exists, but tangent-cone and successor-realization audits forbid treating its missing corner as automatically attained. The point of the formulation is precisely to isolate the required actual-exchange theorem.

The square-lift lemma is substantially narrower than a general carrier theorem. It asks only for a four-corner exchange in the endpoint rank-two class and directly returns the compatible witness demanded by the current strategy broadcast.
