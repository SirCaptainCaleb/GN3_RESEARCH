# The bad adjacent-gap residue has a support-increasing two-for-one exchange

## Composition

For collars P,L -> a -> M,R and L,M -> b -> R,S with b->a, deleting M and inserting b,a gives P,L,b,a,R,S. The remaining conditions are P->b and a->S. If both hold with the exterior retained, covered support increases by one. Failure specifies outer directed triangles; it does not itself supply a legal next move.

## Development

Work in path-normalized square-path gauge. Let five consecutive connector vertices be P,L,M,R,S. Suppose a is individually insertable at L|M and b at M|R, with chosen collars P,L -> a -> M,R and L,M -> b -> R,S. Assume the unique bad adjacent-gap orientation b->a, so a->M->b->a is the directed-triangle residue. Delete the shared connector vertex M and insert b,a, giving the candidate segment P,L,b,a,R,S. Every consecutive edge and every internal distance-two edge is forced forward by the two insertion collars and b->a. The only new distance-two conditions not already certified are P->b and a->S. Hence the exchange succeeds and increases covered support by one exactly when these two outer incidences hold. If P->b fails, then b->P->L->b is a directed triangle at the left boundary. If a->S fails, then a->R->S->a is a directed triangle at the right boundary. Thus failure of the two-for-one growth move exports the A2 obstruction strictly outward from the shared gap.
