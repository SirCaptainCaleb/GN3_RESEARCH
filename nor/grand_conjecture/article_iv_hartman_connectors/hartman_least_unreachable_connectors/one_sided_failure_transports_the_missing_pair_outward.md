# One-sided failure transports the missing pair outward

## Composition

A one-sided adjacent-gap candidate can exchange the missing pair a,b for P,M, preserving support size, if its final incidence and endpoint ports are satisfied. If the last incidence fails, it identifies a farther boundary condition. A reversible hole-transport sequence remains a theorem to construct.

## Development

Continue the adjacent-gap notation H,P,L,M,R,S. The bad mutual orientation is b->a. Assume the two-for-one exchange fails only on the left: b->P, while the right boundary condition a->S holds. Delete both P and M and insert b,a, producing H,L,b,a,R,S. All consecutive and internal distance-two constraints are automatic; on the right, a->S is assumed. The only new unchecked distance-two edge is H->b. Thus the connector support size is unchanged: the old missing vertices a,b have been absorbed, while P,M become the new missing pair. If H->b holds, the exchange is complete. If it fails, the obstruction has moved one connector step farther left. The symmetric statement holds for a right-only failure. If the remaining edge holds and the exposed endpoint ports are retained, this is an actual support-preserving exchange, absorbing a,b while omitting P,M. If it fails, the calculation identifies a further boundary incidence; it does not itself produce a legal reversible move. Iterated outward transport requires realized connector states and a well-founded potential, with endpoint clipping checked separately.
