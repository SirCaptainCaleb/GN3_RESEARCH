# Fixed-cut backward collisions force square-root many edge-disjoint nonspecial cycles

## Statement

Let M backward color-terminal collision chords of a rainbow terminal-pair path of ascending nonspecial edges with nondecreasing edge ranks all cross one fixed cut.

Then the hypergraph contains at least
ceil((ceil(sqrt(M))-1)/2)
pairwise edge-disjoint linear cycles, each consisting entirely of ascending nonspecial edges and each having length at least three.

## Body

Apply 76b25cb9c09b to the M collision chords. It yields a pairwise nested or pairwise crossing subfamily of size
m>=ceil(sqrt(M)).

Nested case. Extend the nested subfamily to a saturated nested chain in the full collision poset. Any interval inserted between two members still crosses the fixed cut because it contains the smaller crossing interval. The saturated chain therefore has at least m members. By ac827276704f it yields at least ceil((m-1)/2) pairwise edge-disjoint nonspecial linear cycles.

Crossing case. Order the pairwise crossing subfamily as
j_1<...<j_m<t<i_1<...<i_m.
If there is a collision interval [u,w] with
j_a<u<j_{a+1} and i_a<w<i_{a+1},
insert it between I_a and I_{a+1}. It still crosses the fixed cut and crosses every member in the ordered family: its left endpoint lies in the corresponding left gap and its right endpoint in the matching right gap. Repeating finitely gives a saturated crossing family with at least m members. Apply aa8c37b64784 to obtain at least ceil((m-1)/2) pairwise edge-disjoint nonspecial linear cycles.

In either case the number of cycles is at least
ceil((ceil(sqrt(M))-1)/2).
