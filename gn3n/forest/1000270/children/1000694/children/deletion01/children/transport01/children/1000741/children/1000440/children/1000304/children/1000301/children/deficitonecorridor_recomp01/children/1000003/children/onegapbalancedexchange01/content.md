# A one-gap unit-surplus corridor reduces to bounded disturbance or one balanced longest-path exchange

## Statement

Let H be a minimum counterexample, let A be a globally longest tight path of order lambda, and let C be a tight A-order-preserving path of order lambda-1 that agrees with A outside one common-vertex gap. Put O=V(A)-V(C) and E=V(C)-V(A), so |O|=|E|+1. Then either |E|<=1, in which case the symmetric-difference kernel has at most three vertices and the whole discrepancy-gap support has order at most five when the gap is internal and at most four when it is an endpoint gap; or |E|>=2 and for any chosen consecutive pair x,y of the displayed E-block at least one of the following occurs: (1) H has a proper Hamiltonian support of order four or five whose complement is non-Hamiltonian with path-cover number two; (2) explicit order disagreement occurs; (3) an explicit reversed tight triple occurs at one of the at most two splice junctions around the edge xy of C; or (4) there is z in O such that replacing xy in C by the tight path (x,z,y) gives a globally longest tight path C_z of order lambda that is A-order-preserving, agrees with A outside the same gap, and satisfies V(A)-V(C_z)=O-{z} and V(C_z)-V(A)=E. Thus the only non-bounded, non-disagreement residue of a large one-gap unit-surplus corridor is a balanced equal-order support exchange confined to that same gap.

## Body


If |E|<=1, apply 0204056412a4 for the stated bounded-gap conclusion. Assume |E|>=2 and choose consecutive vertices x,y of the E-block in the displayed order of C. Both lie outside the globally longest path A and therefore are noninsertable into its displayed order.

The paired-noninsertion reduction used in 0204056412a4 gives one of four outcomes for this chosen pair: a Hamiltonian four-set, a Hamiltonian five-set, a tight cross triple through A, or a direct tight A-interval connector between x and y. In either Hamiltonian-support outcome, the support is proper because a minimum counterexample has order greater than ten; minimum-counterexample calculus then gives a non-Hamiltonian complement of path-cover number two.

If the connector outcome occurs and its A-interval contains at least two vertices, 435125d4ab86 applies because x,y are consecutive in the E-block and reduces it to order disagreement or a reversed tight triple at one of the two splice junctions. If the connector contains only one A-vertex z, it is itself a tight cross triple through z and is handled by d63d3042d1ad.

If the cross-triple outcome occurs, d63d3042d1ad reduces it to order disagreement, a reversed splice-junction triple, or a balanced globally longest path C_z obtained by inserting one z in O between x and y. These alternatives exhaust the paired-noninsertion menu and prove the claim.
