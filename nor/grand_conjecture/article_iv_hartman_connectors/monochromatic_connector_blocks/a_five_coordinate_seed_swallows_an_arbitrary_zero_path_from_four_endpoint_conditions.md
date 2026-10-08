# A five-coordinate seed swallows an arbitrary zero path from four endpoint conditions

## Composition

The seed (u,x,z,a,b) with a->b absorbs a disjoint zero path of length at least two between x,z when both path endpoint edges are forward, its first vertex dominates u, and a dominates its last. This is an arbitrary-length collective move and a special case of three-path gluing.

## Development

Let P=(p1,...,pr) be a zero shore path with r at least 2. Choose three disjoint shore vertices u,a,b outside P with a->b. The universal seed (u,x,z,a,b) is a compatible zero connector. Replacing the adjacent x,z by x,P,z gives (u,x,P,z,a,b). This enlarged order is monochromatic zero exactly when p1->u, the first edge p1->p2 is forward, the last edge p_{r-1}->p_r is forward, and a->p_r. All other windows are inherited from P or from the universal connector relations. Its exposed endpoint pairs u->x and a->b remain forward. Hence an arbitrarily long zero path can be absorbed collectively using only two cross-shore dominance witnesses and its two endpoint-edge bits. This is a concrete whole-path growth move with x and z separated by the absorbed path.
