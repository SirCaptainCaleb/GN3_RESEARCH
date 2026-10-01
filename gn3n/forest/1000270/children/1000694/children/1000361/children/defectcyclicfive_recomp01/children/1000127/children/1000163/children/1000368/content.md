# Every deletion two-cover in a tournament with path-cover number above two yields a central five-set, an outer five-set, or two opposite four-sets

## Statement

Let H be a boundary tournament with pc(H)>2 and let H-x=P|Q be a deletion two-cover, where P=(p_0,...,p_m), Q=(q_0,...,q_s), and |P|,|Q|>=3. Then at least one of the following holds: (1) (q_1,q_0,x,p_m,p_{m-1}) is a tight five-path; (2) (p_1,p_0,x,q_s,q_{s-1}) is a tight five-path; (3) both (p_1,p_0,q_s,q_{s-1}) and (q_1,q_0,p_m,p_{m-1}) are tight four-paths. If neither five-set in (1) and (2) is Hamiltonian, then both cross triples (p_m,x,q_0) and (q_s,x,p_0) are tight and outcome (3) holds. If H is a minimum counterexample, every proper Hamiltonian support displayed above has non-Hamiltonian complement of path-cover number two; and if |P|,|Q|>=4, the two four-sets in (3) are disjoint.

## Body

Because H has no two-cover, (p_{m-1},p_m,x) and (x,q_0,q_1) are non-tight: otherwise x can be absorbed into P or Q. Boundary antisymmetry therefore gives (x,p_m,p_{m-1}) and (q_1,q_0,x) tight. If (p_m,x,q_0) is non-tight, then (q_0,x,p_m) is tight and (q_1,q_0,x,p_m,p_{m-1}) is a tight five-path, giving (1).

Assume (p_m,x,q_0) is tight. At least one of the two wrap triples at Q|P is non-tight, since if both were tight then QP|{x} would two-cover H. If exactly one wrap triple were non-tight, the two forced defects adjacent to x together with that wrap defect would form three isolated cyclic defects in the span-three ordering P,x,Q, contradicting 33b80d34aad4. Hence both wrap triples are non-tight, and their reversal mates give the tight four-path (p_1,p_0,q_s,q_{s-1}).

Also (p_1,p_0,x) and (x,q_s,q_{s-1}) are tight, since the opposite orientations would again absorb x into P or Q. Exactly one of (p_0,x,q_s) and (q_s,x,p_0) is tight. In the first case (p_1,p_0,x,q_s,q_{s-1}) is a tight five-path, giving (2). In the second case the reverse cross (q_s,x,p_0) is tight. Apply the preceding central-tight argument to the swapped deletion order Q,x,P; it gives the opposite tight four-path (q_1,q_0,p_m,p_{m-1}), hence (3).

If both five-sets are non-Hamiltonian, the first branch is impossible, so (p_m,x,q_0) is tight; the second five-path branch is also impossible, so (q_s,x,p_0) is tight, and the preceding argument gives both four-paths. For a minimum counterexample, the complement conclusion follows from mincex01. Disjointness for component orders at least four is immediate from the displayed endpoint pairs.
