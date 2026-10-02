# A saturated nested collision chain yields shortcut cycles or edge-disjoint primitive flank cycles

## Statement

Let
I_a=[j_a,i_a],  a=1,...,m,
be a saturated strictly nested chain of backward color-terminal collision intervals on a rainbow nondecreasing-rank terminal path:
j_1<j_2<...<j_m<i_m<...<i_2<i_1,
and there is no collision interval J with
I_a strictly containing J strictly containing I_{a+1}
for any a.

For each adjacent pair I_a superset I_{a+1}, one of the following holds.

(S_a) The nested shortcut from 94579ab0aabc is a linear cycle of length
L_a=(j_{a+1}-j_a)+1+(i_a-i_{a+1}),
and the outer colliding rank satisfies
r_{i_a}>=L_a+1.

(F_a) One of the two flanks
[j_a,j_{a+1}] or [i_{a+1},i_a]
contains a backward collision interval. Consequently that flank contains an inclusion-minimal collision interval, which by 6aba8c1331b7 closes a genuine linear cycle.

Moreover, primitive cycles chosen from the flanks for distinct indices a are edge-disjoint. Thus if f of the m-1 adjacent pairs fail to shortcut, the terminal path contains at least f pairwise edge-disjoint primitive nonspecial cycles, each of length at least three.

## Body

Apply 94579ab0aabc to the adjacent nested pair
I_a=[j_a,i_a], I_{a+1}=[j_{a+1},i_{a+1}].
If its shortcut sequence is a linear cycle, we are in (S_a), including the displayed rank inequality.

Otherwise 94579ab0aabc produces an additional collision interval J of one of three types: in the left flank [j_a,j_{a+1}], in the right flank [i_{a+1},i_a], or spanning the inner interval with
I_a strictly containing J strictly containing I_{a+1}.
The third type is impossible because the chain is saturated. Hence a failed shortcut produces a collision in one of the two flanks, proving the first part of (F_a).

Inside that finite flank family choose an inclusion-minimal collision interval. It is inclusion-minimal among all collisions as well: any proper collision subinterval would remain inside the same flank. Therefore 6aba8c1331b7 turns it into a genuine linear cycle of length at least three.

It remains to check disjointness. For different levels a, the open annular index regions
(j_a,j_{a+1}] and [i_{a+1},i_a)
are pairwise disjoint as edge-index sets: the left flanks partition the left boundary growth of the nested chain, the right flanks partition its right boundary shrinkage, and every left flank lies strictly before every right flank. A primitive collision interval [p,q] contained in a flank uses exactly the cycle edges E_{p+1},...,E_q. Therefore primitive cycles chosen from different levels use disjoint sets of hyperedges.