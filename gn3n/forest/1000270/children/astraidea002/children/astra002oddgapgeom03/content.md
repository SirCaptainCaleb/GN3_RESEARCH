# Odd balanced-cover failures inherit one-gap compatibility geometry

## Statement

Let H be a minimum-order counterexample to the balanced two-cover conjecture of odd order n=2k+1, and choose one balanced k|k deletion cover F_x of H-x for each label x under consideration. Then the pair-state compatibility geometry has the same one-gap form as in the grand-counterexample route. In particular: (i) every compatible triangle F_a,F_b,F_c has a fixed Hamilton path Q of order k and a common ordered base R of order k-2, with a,b,c all inserted into one identical gap of R in the three deletion states; (ii) a fourth cover compatible with two triangle states can only delete one of the at most two vertices of R adjacent to that gap, with the side determined by source/sink precedence; (iii) every compatibility edge lies in at most two triangles; (iv) cyclic triangles are edge-isolated, while every transitive triangle has its source-sink edge in no other triangle.

## Body

# Proof

Fix three pairwise-compatible balanced deletion covers F_a,F_b,F_c.

Let W=V(H)-{a,b,c}. Pairwise compatibility gives one common pair-state on W, hence a common support partition into at most two ordered classes.

Because every F_d has two components of order k, the class sizes and placements of the two surviving special labels are forced.

If the common W-classes had sizes k-1 and k-1, then in each deletion cover the two surviving labels would have to split, one into each class. Compatibility makes the class of each label independent of which of the two covers containing it is used. Thus a,b,c would have to be pairwise in opposite classes, impossible with only two classes.

Hence the W-classes have sizes k-2 and k. Call the small ordered class R and the large class Q. In every deletion cover both surviving labels are inserted into R, while Q remains a fixed Hamilton path of order k.

Compatibility makes each label x in {a,b,c} occupy a well-defined insertion gap of the common order R.

If the three gaps are not all equal, insert all three labels simultaneously into R at their prescribed gaps, ordering any pair sharing a gap as in the deletion cover containing that pair. Because not all three labels occupy one gap, every consecutive triple in the resulting order omits at least one of a,b,c and is inherited from one of F_a,F_b,F_c. Hence it is tight. This gives a Hamilton path on R union {a,b,c}, of order k+1, together with the fixed k-path Q: a balanced cover of H, contradiction.

Thus every compatible triangle is localized to one common gap.

Now let d be a fourth deletion label whose cover F_d is compatible with, say, F_a and F_b. The triple F_a,F_b,F_d also has the just-proved common-gap form. In the common restriction of F_a,F_b to H-{a,b}, the two support classes have sizes k-1 and k: the smaller class is R with c inserted at the original gap, and the larger is Q.

If d lay in Q, then after deleting a,b,d the two common support classes for the triangle {a,b,d} would both have order k-1, which is impossible by the preceding two-class argument. Hence d lies in R.

For the triangle {a,b,d}, deleting d from R must make the insertion positions of a and b collapse to one common gap. Deleting one vertex of a linear order merges only the two slots adjacent to that vertex. Therefore d must be one of the at most two vertices of R immediately neighboring the original triangle gap.

If d is the left neighbor, both a and b lie before c in the original precedence tournament; if d is the right neighbor, c lies before both a and b. This is the same direct slot comparison as in the ordinary common-gap geometry.

Consequences follow immediately.

For a fixed compatibility edge ab and a third common neighbor c, there is at most one further common neighbor d, namely the appropriate physical gap-neighbor when c is a source or sink. Thus every edge lies in at most two triangles.

If the triangle precedence is cyclic, no label is a source or sink, so no outside cover is compatible with two triangle states; all three triangle edges are isolated from further triangles.

If the precedence is transitive, the source-sink edge has the middle label as its third triangle vertex. That label is neither source nor sink, so the source-sink edge has no second triangle.

Finally, if a transitive triangle gap were an endpoint gap, the usual boundary-antisymmetry splice produces a Hamilton path on the exceptional support R union {a,b,c}, again of order k+1, together with Q of order k. Hence endpoint-gap triangles are cyclic, exactly as in the grand-counterexample geometry.

All contradictions use only the absence of a balanced (k+1)|k cover, not pc(H)>2.
