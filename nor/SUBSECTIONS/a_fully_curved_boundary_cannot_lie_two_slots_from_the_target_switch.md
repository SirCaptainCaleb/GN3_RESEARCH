# A fully-curved boundary cannot lie two slots from the target switch

## Metadata

- ID: a_fully_curved_boundary_cannot_lie_two_slots_from_the_target_switch
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 220
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Width-two full-full corridors are impossible by endpoint relocation

Work in the coboundary-flat alternating ternary sector. Let a bad switch state have globally maximal target-compatible band. Suppose the target switch is followed on the right by exactly two matched post-switch windows before the first unresolved boundary, and suppose that boundary is fully curved.

Normalize the six consecutive coordinates as
(0,1,2,3,4,5)
and the local status word as
A,B,B,A,
where B=1-A. Thus the target cut lies between the first two displayed window ranks, and the final A is the first mismatch on the post side.

The right boundary tetrahedron is {2,3,4,5}, with consecutive statuses B,A, and is fully curved. For a fully-curved B->A transition its B-shadow off-face is
alpha(2,4,5)=B.

On the middle four-set {1,2,3,4}, the two consecutive faces both have color B:
alpha(1,2,3)=alpha(2,3,4)=B.
Coboundary parity therefore gives
alpha(1,2,4)=alpha(1,3,4).
Put
t=alpha(1,2,4) in {A,B}.

Now REMOVE coordinate 3 from its present position and reinsert it at the global right endpoint of the full coordinate order. This is still a full spanning coordinate order; no deletion-instance argument is being used.

Near the old corridor, the three surviving consecutive statuses are exactly
alpha(0,1,2)=A,
alpha(1,2,4)=t,
alpha(2,4,5)=B.
Every window strictly to the left of this packet is unchanged. Every window beginning with the old ordered pair (4,5) and continuing into the old right exterior is also unchanged; moving 3 to the global endpoint alters only the final endpoint windows far to the right.

There are two cases.

1. t=B.
Keep the original cut. The local word is A,B,B, so all three displayed ranks are target-compatible. In particular the old first mismatching rank has disappeared and the compatible band extends strictly farther right.

2. t=A.
Move the proposed cut one window rank to the right. The local word is A,A,B, again exactly target-compatible. Every old matched rank to the left remains matched, and the old first mismatching rank has again disappeared. The compatible band extends strictly farther right.

In either case the only new windows created by reinserting coordinate 3 occur at the global right endpoint, strictly beyond the old unresolved right boundary. They therefore cannot prevent the maximal target-compatible band around the displayed cut from containing the entire old band plus the old boundary rank.

This contradicts global maximality of the band.

### Theorem

A globally maximal target-compatible bad switch state cannot have a fully-curved unresolved boundary exactly two matched transition slots from the target switch.

Combined with the one-slot full-full exclusion, the nearest fully-curved boundary in an all-curvature extremal state must lie at distance at least three.

The mechanism is worth retaining: a fully-curved boundary has a canonical target-color deletion shadow, and instead of actually deleting that coordinate one may relocate it to a remote global endpoint. This preserves full support while exporting all reinsertion risk beyond the boundary being improved.

## Frontier

- Development version when composed: None
- Development version now: 1
