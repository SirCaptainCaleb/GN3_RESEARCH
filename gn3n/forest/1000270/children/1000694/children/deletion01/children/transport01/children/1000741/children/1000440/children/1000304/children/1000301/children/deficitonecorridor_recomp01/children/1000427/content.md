# Deficit-one order-preserving comparisons have no unbounded neutral corridor residue

## Statement

Let H be a minimum counterexample, let A be a globally longest tight path, and let C be an A-order-preserving tight path of order |A|-1 with the noncrossing charging of deficitonecorridor_recomp01. Then at least one of the following occurs: (1) the binary-balance potential strictly decreases under a certified charged replacement; (2) explicit order disagreement, an A-edge reversal, or an explicit bounded reversed tight triple occurs; (3) H contains a proper Hamiltonian support of order four or five whose complement is non-Hamiltonian with path-cover number two; or (4) after the certified prefix-suffix localization, the entire remaining discrepancy lies in one gap with at most one C-only vertex, hence with symmetric difference of order at most three and gap support of order at most five when internal and at most four at an endpoint. In particular no one-gap residue with at least two C-only vertices is neutral.

## Body

Apply the certified deficit-one corridor theorem deficitonecorridor_recomp01. If a charge is strict, its charged replacement gives strict binary-balance descent, an A-edge reversal, or one of the certified bounded reversed-triple obstructions, giving (1) or (2). Otherwise, after at most two prefix-suffix splices, either a reversed mixed-junction triple already occurs or there is a tight A-order-preserving path C* of order |A|-1 agreeing with A outside one gap. Write O=V(A)-V(C*) and E=V(C*)-V(A), so |O|=|E|+1.

If |E|<=1, then |O|<=2 and the symmetric difference has order at most three. Adding the two common anchors of an internal gap gives support order at most five; an endpoint gap has at most one anchor, giving order at most four. This is (4).

Assume |E|>=2 and choose consecutive vertices x,y of the E-block in the displayed C*-order. Both are outside the globally longest path A, so the certified longest-path paired-noninsertion theorem 6839f08d0cf8 applies. Its Hamiltonian four- or five-support outcomes give (3), with the complement conclusion by minimum-counterexample calculus.

If the paired theorem gives a direct connector from x to y through an A-interval containing at least two A-vertices, 435125d4ab86 gives order disagreement or a reversed splice-junction triple. A one-A-vertex connector is a cross triple and is included in the next case.

If the paired theorem gives a tight cross triple through z in V(A), d63d3042d1ad gives order disagreement, a reversed splice-junction triple, or a successful splice producing a globally longest path B of order |A|. In the successful case B is A-order-preserving, agrees with A outside the same gap, and has V(B)-V(A)=E and |V(A)-V(B)|=|E|. Thus A and B are an equal-order one-gap comparison with |E|>=2. Apply the certified equal-order closure theorem equalorderonegapclosure01. Its bounded-kernel alternative is unavailable because |E|>=2, so it gives a Hamiltonian four/five-support with path-cover-two complement, order disagreement, or an explicit reversed splice-junction triple. These are (2) or (3).

The paired-noninsertion menu is exhausted. Therefore every unbounded one-gap branch is converted to one of the stated closure inputs, and only the stated at-most-five-vertex local discrepancy can remain neutral.
