# Every order-twelve minimum counterexample exposes a longest-path mixed crossing or order disagreement

## Statement

Let H be a minimum counterexample of order 12. Then there is a globally longest tight path A with non-Hamiltonian complement U such that U has at least four Hamiltonian vertex deletions. Consequently, for arbitrary deletion two-covers at the two displayed endpoints of A, there is a label t in U for which at least one endpoint cover contains an ordinary edge directly joining U-{t} to the surviving part of A, or the endpoint probes expose explicit relative-order disagreement. In the latter case H contains a reversed common ordered edge, a reversing tight triple, or a vertex-simple tight cycle. Thus order twelve reduces entirely to the standard longest-path endpoint-transport / defect-compression interface.

## Body

Start with any deletion two-cover H-x=P|Q and label so |P|<=|Q|. By minimum-counterexample calculus, 3<=|P|<=5 and |Q|>=6. Put C=V(P) union {x}. By 6f72075b0b54, C is non-Hamiltonian and has at least four Hamiltonian vertex deletions.

If Q is globally longest, take A=Q and U=C. The conclusion follows immediately from astra004manygoodmixed.

If Q is not globally longest, let A be any globally longest tight path. As in 96aa7439b5a9, its complement U is non-Hamiltonian and has order four or five. If |U|=4, every three-vertex deletion U-{t} is Hamiltonian, so all four labels are good. If |U|=5, the certified small-set theorem gives at least four Hamiltonian four-vertex deletions. Thus in either case U has at least four good deletion labels, and astra004manygoodmixed again gives the stated direct mixed crossing or relative-order disagreement. The reversed-edge/reversing-triple/tight-cycle refinement is the certified conclusion of the same theorem.