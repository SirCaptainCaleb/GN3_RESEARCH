# A cross triple on consecutive exterior corridor vertices yields disturbance or a balanced longest-path exchange

## Statement

Let A be a globally longest tight path of order lambda and C a tight A-order-preserving path of order lambda-1 agreeing with A outside one common-vertex gap. Put O=V(A)-V(C) and E=V(C)-V(A), and let x,y be consecutive vertices of the E-block in the displayed C-order, with x before y. Suppose the paired-noninsertion menu supplies a tight cross triple through some z in V(A), namely (x,z,y) or (y,z,x). Then at least one of the following holds: (1) explicit order disagreement between C and a tight three-vertex path on {x,y,z}; (2) a reversed tight triple at one of the at most two splice junctions around the edge xy of C; or (3) z lies in O and replacing the edge xy of C by (x,z,y) gives a globally longest tight path C_z of order lambda. In outcome (3), C_z is A-order-preserving, agrees with A outside the same gap, and satisfies V(A)-V(C_z)=O-{z} and V(C_z)-V(A)=E, so the one-gap support exchange is balanced.

## Body

Orient x,y by their displayed order in C. If the tight cross triple is (y,z,x), then the tight path (y,z,x) orders the common vertices x,y oppositely from C, so outcome (1) holds. Hence assume (x,z,y) is tight.

If z belongs to A cap C, then z is a common A-vertex outside the interior E-block of the unique discrepancy gap. Thus in C it occurs either before both x,y or after both, whereas the tight path (x,z,y) places it strictly between them. Again there is order disagreement.

It remains that z belongs to O. Since x,y are consecutive in the E-block, they are adjacent in C. Replace this edge by the tight path (x,z,y). The only potentially new consecutive triples are (p,x,z) when x has a predecessor p in C and (z,y,q) when y has a successor q in C. If one is non-tight, boundary antisymmetry gives the reversed tight triple (z,x,p) or (q,y,z), giving outcome (2).

If every existing junction is tight, the splice is a tight path C_z. It has order |C|+1=lambda and hence is globally longest. Because z belongs to the omitted A-block in the unique gap, inserting z between x,y does not disturb the relative order of any common A-vertices; endpoint-gap cases are identical. Thus C_z remains A-order-preserving and agrees with A outside the same gap. Its support differences are exactly O-{z} and E, which have equal size because |O|=|E|+1. This is outcome (3).
