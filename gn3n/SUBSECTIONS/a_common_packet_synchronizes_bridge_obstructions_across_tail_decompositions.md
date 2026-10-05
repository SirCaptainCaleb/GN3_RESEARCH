# A common packet synchronizes bridge obstructions across tail decompositions

## Metadata

- ID: a_common_packet_synchronizes_bridge_obstructions_across_tail_decompositions
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 71
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Lemma (six-vertex packet). Let S be a six-vertex set in a boundary tournament H, and let D be any family of two-path covers T|U of H-S, with both displayed paths having order at least two. For a cover D_0, call v in S a bridge if either (T,v,U) or (U,v,T) is tight, with the actual displayed path orientations. Let G be the union of these bridge labels over all covers in D.

If |G|>=3, H has a two-cover. More exactly, any v in G for which S-v is Hamiltonian supplies a two-cover.

Proof. Four-of-six in [[smallset01]] says at most two vertices v in S have a non-Hamiltonian deletion S-v. Therefore some v in a union of at least three labels has a Hamiltonian deletion. Choose the tail decomposition witnessing that v is a bridge; its concatenation is one tight path and S-v is the other. QED.

Consequently, if H has no two-cover, all decompositions in D have their bridge labels contained in one fixed set
B(S)={v in S:S-v is non-Hamiltonian},
of order at most two. It is not enough to bound each separate bridge set by two: their union must satisfy the same bound. The packet and its deletion obstructions, rather than the individual tail decomposition, determine the permissible labels.

There is a corresponding five-vertex packet lemma. Let |S|=5 and let D be a family of Hamilton orders Q of H-S, all of order at least two. Allow either a terminal bridge h(q_{last-1},q_last,v)=1 or an initial bridge h(v,q_1,q_2)=1. If S is Hamiltonian, H already has the cover S|Q. Otherwise at most one deletion S-v is non-Hamiltonian by the non-Hamiltonian-five-set theorem. Thus two distinct bridge labels occurring anywhere in this family, even at opposite ends or in different orders, force a two-cover. In a failed instance every such bridge is the same exceptional bad-deletion label.

Application to the mobile-cut monotone corridor in [[mobile_corridor_cuts_give_a_twenty_vertex_tail_joining_certificate]]. Use the fixed initial-pair packet
S={x,y,c_1,c_2,c_{N-1},c_N}.
For j=u,u+1,u+2 the remaining paths are
T_j=(c_3,...,c_j), U_j=(c_{N-2},...,c_{j+1}).
These are three different covers of the same complement of the same packet. Hence three distinct bridge labels across the three cuts suffice for repair. If there is no two-cover, their union is contained in B(S).

In a genuine deletion-distance-two residue x,y cannot bridge any of these covers, since their terminal ordered pairs are the original corridor terminal pairs. Therefore at least two of the four corridor packet vertices c_1,c_2,c_{N-1},c_N never bridge either direction in any of the three cuts. Every label that ever does bridge has the same bad five-deletion across all cuts. This is an additional necessary synchronization condition, stronger than the separate at-most-two conditions recorded earlier.

The lemma supplies a sufficient repair certificate and a coupled failure condition. It does not prove that three distinct candidates must occur, nor does it resolve global compatibility of the resulting outward carriers.
