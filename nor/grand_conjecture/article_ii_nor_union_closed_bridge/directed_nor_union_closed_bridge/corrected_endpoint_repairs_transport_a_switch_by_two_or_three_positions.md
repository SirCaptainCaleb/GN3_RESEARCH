# Corrected endpoint repairs transport a switch by two or three positions

## Composition

This sharpens the corrected endpoint-repair calculation in endpoint_repair_never_increases_cyclic_variation. Work in a pure alternating ternary orientation, with enough distinct surrounding coordinates for the displayed packet. A successful last-pair repair changes the consecutive statuses (L,x,1-x,z,R,S) to (L,x,x,1-z,V,S). Let the central transition have index i, so it is deleted. The transition at i+1 is unchanged. Only the two later transition bits at i+2,i+3 can change: their old values are a=z xor R, b=R xor S, and their new values are a'=(1-z) xor V, b'=V xor S.

Proposition. Exactly one of a,b toggles. Indeed a xor b=z xor S while a' xor b'=1 xor z xor S. The parity of the pair changes, so their Hamming distance is odd; with two bits it must be one. All other transition bits, apart from the deleted central bit, are unchanged.

Consequently there is j in {i+2,i+3} such that d'_i=0, d'_j=1-d_j, and d'_k=d_k at all other indices. If d_j=0, the move transports the central switch by two or three positions. If d_j=1, it deletes that switch and the central switch, reducing variation by two. This gives a positional repair of the earlier false distance-two-only transport statement while retaining the fourth changed status.

The choice of distance is determined by the far triangle: if V=R, then b'=b and a'=1-a, so the target is i+2. If V!=R, then a'=a and b'=1-b, so the target is i+3. Thus the additional window is precisely a binary selector between the two transport distances.

Reversing the coordinate order gives the corresponding leftward rule. A graph whose vertices are full-support cyclic orders and whose edges are these repairs therefore carries an explicit evolution of marked transition positions. At minimum variation all available repairs are transports; an edge targeting an occupied position would contradict minimality. A connector proof must still exclude a closed collection of transport states or force a collision. Existence of an outgoing repair alone does not exclude cycles, and a move can pass another switch without landing on it.

This is a full-support statement. It does not require deleting a coordinate, and it does not assume that the curvature type remains unchanged after transport. The target-distance selector V xor R must be retained in any triangulation or cell structure built from these moves.

## Development

This sharpens the corrected endpoint-repair calculation in endpoint_repair_never_increases_cyclic_variation. Work in a pure alternating ternary orientation, with enough distinct surrounding coordinates for the displayed packet. A successful last-pair repair changes the consecutive statuses (L,x,1-x,z,R,S) to (L,x,x,1-z,V,S). Let the central transition have index i, so it is deleted. The transition at i+1 is unchanged. Only the two later transition bits at i+2,i+3 can change: their old values are a=z xor R, b=R xor S, and their new values are a'=(1-z) xor V, b'=V xor S.

Proposition. Exactly one of a,b toggles. Indeed a xor b=z xor S while a' xor b'=1 xor z xor S. The parity of the pair changes, so their Hamming distance is odd; with two bits it must be one. All other transition bits, apart from the deleted central bit, are unchanged.

Consequently there is j in {i+2,i+3} such that d'_i=0, d'_j=1-d_j, and d'_k=d_k at all other indices. If d_j=0, the move transports the central switch by two or three positions. If d_j=1, it deletes that switch and the central switch, reducing variation by two. This gives a positional repair of the earlier false distance-two-only transport statement while retaining the fourth changed status.

The choice of distance is determined by the far triangle: if V=R, then b'=b and a'=1-a, so the target is i+2. If V!=R, then a'=a and b'=1-b, so the target is i+3. Thus the additional window is precisely a binary selector between the two transport distances.

Reversing the coordinate order gives the corresponding leftward rule. A graph whose vertices are full-support cyclic orders and whose edges are these repairs therefore carries an explicit evolution of marked transition positions. At minimum variation all available repairs are transports; an edge targeting an occupied position would contradict minimality. A connector proof must still exclude a closed collection of transport states or force a collision. Existence of an outgoing repair alone does not exclude cycles, and a move can pass another switch without landing on it.

This is a full-support statement. It does not require deleting a coordinate, and it does not assume that the curvature type remains unchanged after transport. The target-distance selector V xor R must be retained in any triangulation or cell structure built from these moves.
