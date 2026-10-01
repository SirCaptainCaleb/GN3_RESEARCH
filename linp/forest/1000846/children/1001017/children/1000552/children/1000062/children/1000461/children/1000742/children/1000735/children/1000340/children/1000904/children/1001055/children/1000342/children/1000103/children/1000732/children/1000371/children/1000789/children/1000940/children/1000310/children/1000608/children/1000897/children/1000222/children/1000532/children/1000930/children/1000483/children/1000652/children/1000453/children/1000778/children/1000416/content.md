# Fixed-cut collision congestion gives a large crossing family or many edge-disjoint cycles

## Statement

Let M backward color-terminal collision chords of a rainbow nondecreasing-rank terminal path all cross one fixed cut.

Then at least one of the following holds:
(1) there are at least ceil(sqrt(M)) pairwise crossing collision chords;
(2) the hypergraph contains at least
ceil((ceil(sqrt(M))-1)/2)
pairwise edge-disjoint linear cycles consisting entirely of ascending nonspecial edges.

Thus fixed-cut collision congestion reduces, with square-root loss, to the genuinely crossing case or to linear cycle packing.

## Body

By 76b25cb9c09b, the M chords contain a pairwise crossing subfamily or a pairwise nested subfamily of size
m>=ceil(sqrt(M)).
If the crossing alternative occurs, we have (1).

Otherwise let I_1 strictly contain ... strictly contain I_m be the nested subfamily. Extend it, if necessary, to a saturated chain in the poset of all collision intervals. Every interval inserted between two members of the original chain still crosses the fixed cut, because it contains the smaller interval, which crosses that cut. In particular the saturated chain has at least m members.

Apply ac827276704f to this saturated chain. It supplies at least
ceil((m-1)/2)
pairwise edge-disjoint linear cycles of ascending nonspecial edges. Since m>=ceil(sqrt(M)), this is at least the quantity in (2).
