# At least 922 good full Q6 geodesics from pentagon connectors and six-path forcing

# Quantitative six-dimensional NORI closure: at least 922 good directed full geodesics

Let c(F,(a,b,c)) be a physical ordered-three-face coloring of Q_6 satisfying c(bar F,(c,b,a))=1+c(F,(a,b,c)) over F_2. A directed full geodesic is (x,p) with x in Q_6 and p a permutation of the six directions. It is good if the four colors of its consecutive three-direction windows have at most one change. There are 64*720=46080 directed full geodesics.

THEOREM. At least 922 distinct directed full geodesics are good (equivalently at least 461 reversal pairs), for every legal Q_6 NORI coloring.

Proof. First count four-edge equal-color connectors. Fix a vertex z and a five-element direction set W. For a cyclic ordering of W, inspect the five ordered triples obtained by taking three consecutive directions cyclically; use the actual physical three-faces through z. A binary cyclic five-word has an adjacent equality. Each such adjacent equality corresponds to an ordered four-tuple (a,b,c,d) with physical centered ordered faces (a,b,c) and (b,c,d) through z of equal color. Double-counting the 120 linear representations of cyclic five-orders gives at least 24 such four-tuples among the 120 on each W (the established centered pentagon inequality). In Q_6 there are six five-subsets W, and each ordered four-tuple belongs to exactly two of them, hence at least 6*24/2=72 equal-color four-tuples at each z. Every one determines exactly one four-edge seed with root x=z xor e_a: its first two ordered-face windows both contain z. Across all 64 vertices z there are at least 4608 distinct such four-edge seeds.

Apply the established literal physical six-geodesic forcing certificate: for every seed with directions (a,b,c,d), and remaining directions labeled (e,f), at least one of its six explicit six-edge geodesics is good. To make the certificate assignment deterministic, order the two remaining directions by their fixed numeric coordinate labels so that e<f.

Now pair each rooted full geodesic (y,p) with (y,reverse(p)). These two paths have the same goodness status: for every i, the window of the reversed direction order is the antipodal reversal of the corresponding window of the original path (the outside bits of the ordered face are complemented), so its four-color word is the complemented reversed original word. Hence every good directed full geodesic occurs in a distinct pair, and the number of good directed paths is twice the number of good pairs.

We bound how many seeds can produce either member of any fixed pair through the six-path forcing table. Fix p=(p_1,...,p_6). In the certificate's six rows the positions of the labels (e,f) are respectively (5,6),(5,6),(6,5),(5,4),(2,3),(2,3). For each row and each output (y,p), the ordered labels (a,b,c,d,e,f) and the seed root x are uniquely recoverable from that row's direction permutation and starting-bit flip vector. Such a preimage is admissible only if e<f. Its further equal-window condition can only decrease the number of admissible preimages.

Let [P] denote 1 when P holds and 0 otherwise. The number of potentially admissible preimages across (y,p) and (y,reverse(p)) is exactly
  2 + [p_5<p_6] + [p_2<p_1] + 3[p_5<p_4] + 3[p_2<p_3],
which is at most 10. Indeed the three rows with (e,f)=(5,6),(5,6),(6,5) contribute 1+[p_5<p_6] for p and 1+[p_2<p_1] for its reversal; row four contributes [p_5<p_4]+[p_2<p_3]; rows five and six contribute 2[p_2<p_3]+2[p_5<p_4]. Thus every reversal pair can serve as a candidate from at most ten equal-color seeds.

Assign to each of the at least 4608 seeds one good output pair from its six-path forcing certificate. Every output pair receives at most ten seeds. There are therefore at least ceil(4608/10)=461 good output pairs, or at least 922 good directed full geodesics. QED.

The immediate bound without reversal pairing is 4608/6=768 directed good geodesics. The reversal-pair count sharpens it to 922 via a deterministic e<f convention. This is a genuine positive-density theorem for the fully position-dependent physical model. It does not itself establish one-switch closure for Q_n with n>=7, because six-coordinate restrictions need not satisfy the full-cube oddness law.
