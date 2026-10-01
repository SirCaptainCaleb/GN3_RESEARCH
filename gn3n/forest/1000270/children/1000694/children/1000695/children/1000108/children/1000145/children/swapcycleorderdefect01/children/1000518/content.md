# A deletion-cover order defect survives all but at most two further deletions

## Statement

Let F_a and F_b be support-compatible but not fully compatible deletion covers, and restrict both to their common domain W=V(H)-{a,b}. Regard the two restrictions as partitions of W into the same two support classes with linear orders on each class. Then there are at most two vertices x in W such that deleting x makes the two restricted covers fully compatible. If two such vertices x,y exist, the original pair-state disagreement between F_a and F_b is concentrated on the single pair {x,y}. Consequently the order defect forced on a singleton-swap cycle survives every further deletion except possibly two labels.

## Body

Support compatibility ensures the two common-domain structures have the same block partition; failure of full compatibility means they are distinct as ordered-block structures. Apply the certified two-deletion reconstruction theorem pairdeletionreconstruct01 to those two structures. Its exceptional set Z of labels whose deletion erases every pair-state disagreement has size at most two; if |Z|=2, the only disagreeing pair is exactly Z. Thus the cocycle order defect is not a fragile artifact that can disappear under many one-vertex restrictions.