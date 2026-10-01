# A Hamiltonian four-set need not endpoint-extend an arbitrary Hamiltonian deletion order

## Statement

There exists a boundary tournament on four vertices W={0,1,2,3} such that W is Hamiltonian, but for w=1 the tight path A=(3,2,0) on W-{1} cannot be extended by w at either endpoint: neither (1,3,2,0) nor (3,2,0,1) is tight.

Consequently, in an anchored Hamiltonian four-window W, a deletion two-cover in which W-{w} occurs as one contiguous three-vertex block cannot be eliminated merely from Hamiltonicity of W by asserting that w must prepend or append the displayed block order.

## Body

Define the boundary tournament by declaring the following member of each reversal pair tight:
(1,0,2), (3,0,1), (3,0,2),
(2,1,0), (3,1,0), (3,1,2),
(1,2,0), (3,2,0), (3,2,1),
(1,3,0), (2,3,0), (2,3,1).

This specifies exactly one tight orientation for each choice of middle vertex and unordered pair of endpoints, hence defines a boundary tournament.

The ordering (1,3,0,2) is Hamiltonian because (1,3,0) and (3,0,2) are tight.

After deleting w=1, A=(3,2,0) is tight because (3,2,0) is tight.

Prepending 1 would require (1,3,2) tight. Its reverse (2,3,1) is tight, so (1,3,2) is non-tight. Thus (1,3,2,0) is not tight.

Appending 1 would require (2,0,1) tight. Its reverse (1,0,2) is tight, so (2,0,1) is non-tight. Thus (3,2,0,1) is not tight.

Therefore Hamiltonicity of W does not imply endpoint absorption of an arbitrary Hamilton order on a three-vertex deletion.
