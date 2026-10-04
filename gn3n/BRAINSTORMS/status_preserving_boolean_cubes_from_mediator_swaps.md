# Status-preserving Boolean cubes from mediator swaps

In a connected robust mediator-swap regime, use disjoint agreement P3 gadgets to build actual families of interleavings in which one parity status word is frozen while selected coordinates of the opposite parity can be independently toggled.

Let X be one parity side and C the mediator colors from the other side. Suppose the t-robust swap graph on C is connected and 9t<=|X|+4.

Its complement is triangle-free, hence its independence number is at most two. A maximal matching therefore leaves at most two colors unmatched. Choose q robust matched pairs with 3q<t.

For each chosen color pair choose one agreement P3, with all q triples vertex-disjoint. This can be done greedily because the candidate family for each pair contains t disjoint triples and fewer than 3q vertices have been used.

Arrange the q triples as consecutive three-vertex blocks in an X-order and assign the paired mediator colors to the two internal gaps of their block. Put at least one fixed mediator gap between successive controlled pairs. Complete the rest of the X-order and mediator assignment arbitrarily.

Within each controlled block, swapping its two mediator colors preserves both X-side status signs because the two colors agree on both P3 edges. Hence all 2^q swap choices have the identical complete X-side status word.

In the opposite parity stream, toggling one controlled block swaps two adjacent mediator vertices. Boundary antisymmetry forces the central opposite-parity status between them to flip. Only the two neighboring opposite-parity statuses can also change. With one fixed mediator between controlled pairs, these radius-one influence windows are disjoint.

Therefore the projection of this family onto the q central opposite-parity coordinates is exactly the full cube {0,1}^q while the entire X-side status word remains fixed.

For t=floor((|X|+4)/9), one may take q on the order of |X|/27. Thus the connected robust-swap branch contains a linear-dimensional status-preserving Boolean cube inside the actual spanning-order state space.

A stronger directed version is available when an agreement P3 is oriented x->z->y in both mediator tournaments. The three-vertex block x,z,y then has two independent local switches: mediator swap flips the central opposite-parity status while preserving the two X-statuses; reversing the block to y,z,x flips both X-statuses from ++ to -- while keeping the same middle X-vertex z. Absence of directed agreement P3s forces the common-agreement digraph into a pure-source/pure-sink cut structure. This gives another flexibility-versus-cut dichotomy.
