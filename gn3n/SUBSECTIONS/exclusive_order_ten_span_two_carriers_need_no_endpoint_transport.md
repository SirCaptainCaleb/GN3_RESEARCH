# Exclusive order-ten span-two carriers need no endpoint transport

## Metadata

- ID: exclusive_order_ten_span_two_carriers_need_no_endpoint_transport
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 44
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## The order-ten exclusive span-two branch has a protected frozen carrier without endpoint transport

The exception in [[balanced_ten_position_repairs_have_explicit_protected_endpoint_orbits]] is removable once the rank-one coupling theorem [[positive_exclusive_disjoint_span_two_carriers_have_rank_one_coupling]] is used correctly.

Let (F_*) be a protected exclusive disjoint span-two zero face at depth (r). Its two determining windows are adjacent, their full positional span
[
J
]
has order ten, and the only sign-changing face freedom is the order of the two vertices in the central coupling block. Every other face-block factor is sign-neutral.

Choose any (5|5) two-cover of the induced boundary tournament on the ten vertices occupying (J), and let
[
omega
]
be the spanning order obtained by inserting the normalized order (P,Q^{m rev}) on (J) while leaving all positions outside (J) fixed as in one reference chamber of (F_*).

Because (P,Q^{m rev}) is a two-cover order, its internal status word on (J) avoids
[
001,qquad011,qquad0101.
]
Every determining window for the current reflected span-two edge, and every determining window for a strictly more central positive witness edge, lies inside the full ten-position span (J). Hence (omega) has no selected witness of depth at most (r) whose determining window is internal to (J). Any positive forbidden window meeting a boundary of (J) extends beyond one of the two current determining windows, so it belongs to a strictly farther-out witness edge. Thus
[
omegain X_{r+1}.
]

Now do **not** transport either endpoint-crossing generator. Let (A_*) be the union of active Coxeter components of (F_*) whose positional supports are completely disjoint from (J). Every active generator touching (J)—including the central sign-flip generator, all sign-neutral internal generators, and both endpoint-crossing generators—is collapsed.

For every subface (Gsubseteq F_*), use the inherited mask
[
A_G=S_Gcap A_*
]
and define
[
C(G)={omega w:win W_{A_G}},
]
including the full corresponding permutahedron face.

Every retained generator acts in a component completely disjoint from (J). Hence the ten positions of (J) remain frozen in every chamber of (C(G)). Any status changes caused by the exterior action occur outside (J) or in windows extending beyond its ends; by the preceding depth comparison these cannot create a positive witness of depth at most (r). Therefore
[
C(G)subseteq X_{r+1}.
]

Moreover:

1. (C(G)) is a product of permutahedron faces and hence contractible;
2. if (Gsubseteq Hsubseteq F_*), then (A_Gsubseteq A_H) and therefore
   [
   C(G)subseteq C(H);
   ]
3. reversal sends the construction to the reversed normalized repair, so choosing one representative from each reversal orbit of ambient faces gives an equivariant pair of carriers.

Thus the no-slack endpoint problem is an artifact of insisting on endpoint transport. For the exclusive order-ten span-two branch, endpoint generators may simply be collapsed. The entire branch admits a nested protected frozen-window carrier inside (X_{r+1}).

This uses the positive-word depth rule consistently throughout: no dual-polarity avoidance is invoked.

### Remaining local frontier

After this repair, the only unbounded positive terminal branch is the span-two reflected-double branch of [[positive_reflected_double_carriers_have_unbounded_local_spans]]. The alternating double branch is bounded by eight, the exclusive alternating branch is impossible, and the exclusive span-two branch is handled above.

Therefore the genuinely new local theorem still needed is the reflected-double corridor/interface repair, together with global compatibility of the resulting frozen carriers across ambient zero faces.

## Frontier

- Development version when composed: None
- Development version now: 1
