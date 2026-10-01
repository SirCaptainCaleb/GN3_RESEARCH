# Every order-twelve deletion state enters codimension four/five or a longest-path endpoint disturbance

## Statement

Let H be a minimum counterexample of order 12 and let H-x=P|Q be any deletion two-cover, with p=|P|<=q=|Q|. Then 3<=p<=5 and q=11-p>=6. Put C=V(P) union {x}. One of the following holds.

(1) H contains a globally longest tight path A whose non-Hamiltonian complement has order four or five.

(2) Q itself is globally longest, C is non-Hamiltonian and has at least four Hamiltonian vertex deletions, and arbitrary deletion two-covers at the two displayed endpoints of Q expose either a direct ordinary edge joining the surviving part of C to the surviving part of Q, or explicit relative-order disagreement; in the latter case one obtains a reversed common ordered edge, a reversing tight triple, or a vertex-simple tight cycle.

Thus order twelve admits no structureless 4|4|4 residue: every deletion state feeds either the codimension-four/five frontier or the standard longest-path endpoint-transport disturbance interface.

## Body

Minimum-counterexample calculus gives p,q>=3, and p+q=11, so p<=5 and q>=6. Let C=V(P) union {x}. Since C together with Q partitions V(H), H[C] cannot be Hamiltonian, else a Hamilton path on C together with Q would two-cover H. By 6f72075b0b54, because 3<=p<=5, the non-Hamiltonian set C has at least four labels t for which C-{t} is Hamiltonian.

If Q is globally longest, apply astra004manygoodmixed with A=Q, U=C, and this four-label set. It gives outcome (2).

Suppose Q is not globally longest. Let A be a globally longest tight path, so |A|>=q+1. Its complement U has order
|U|=12-|A|<=11-q=p<=5.
The complement of a proper tight path in a minimum counterexample is non-Hamiltonian and two-coverable; moreover every tight path in a minimum counterexample leaves at least four vertices outside it. Hence 4<=|U|<=5. This is outcome (1), namely the codimension-four or codimension-five Hamiltonian-side frontier.