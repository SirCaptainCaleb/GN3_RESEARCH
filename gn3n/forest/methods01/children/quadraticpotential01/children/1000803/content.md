# At a quadratic-minimal relocation state a large size gap gives a barrier or opposite endpoint extensions

## Statement

Assume a trapped contiguous-block relocation component contains no ordering with c<=2, and choose a displayed three-block state minimizing Phi. Let X=(x_1,...,x_p) and Y=(y_1,...,y_q) be two displayed blocks with p>=q+2 and q>=2. Then either one of the ordered interfaces X|Y or Y|X is a double-non-tight barrier, or both (X,y_1) and (y_q,X) are tight paths. Equivalently, if neither orientation is a barrier, the two endpoints of the smaller block Y extend the two opposite ends of the larger block X.

## Body

By whole-block permutation freedom, inspect both ordered interfaces while staying in the same relocation component and preserving Phi. For X|Y, the local interface trichotomy excludes a merge, since that would give c<=2. If exactly one join triple is tight, then either the cut shifts right, changing (p,q) to (p+1,q-1), or it shifts left, changing (p,q) to (p-1,q+1). The corresponding Phi changes are 2(p-q)+2 and 2(q-p)+2. Since p-q>=2, the left shift strictly decreases Phi and is impossible at a Phi-minimum. Therefore, if X|Y is not a barrier, only the right shift can occur; its tight join triple is (x_{p-1},x_p,y_1), so (X,y_1) is tight. Now inspect Y|X. Again merging is impossible. Here the slide transferring a vertex from the larger X into the smaller Y would strictly decrease Phi and is forbidden. Thus, if Y|X is not a barrier, the only slide transfers y_q from the smaller Y into the larger X; equivalently the join triple (y_q,x_1,x_2) is tight, so (y_q,X) is tight. Hence absence of a barrier in both orientations gives opposite endpoint extensions of X by y_1 and y_q.
