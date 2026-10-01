# A saturated crossing collision family packs linearly many edge-disjoint cycles

## Statement

Let
I_a=[j_a,i_a], a=1,...,m,
be a pairwise crossing family of backward collision intervals on a rainbow nondecreasing-rank terminal path, ordered so that
j_1<...<j_m<t<i_1<...<i_m
for some fixed cut t.

Assume the family is saturated: for each a<m there is no additional collision interval [u,w] with
j_a<u<j_{a+1}
and
i_a<w<i_{a+1}.

Then the hypergraph contains at least
ceil((m-1)/2)
pairwise edge-disjoint linear cycles, each consisting entirely of ascending nonspecial edges and each having length at least three.

## Body

For each consecutive pair
I_a=[j_a,i_a], I_{a+1}=[j_{a+1},i_{a+1}],
apply 1c694ba91adc.

If its crossing shortcut is a linear cycle, choose that cycle C_a. Its support consists of the left annulus
E_{j_a+1},...,E_{j_{a+1}}
and the reversed right annulus
E_{i_{a+1}},E_{i_{a+1}-1},...,E_{i_a}.

Otherwise 1c694ba91adc produces an additional collision either in the left flank [j_a,j_{a+1}], in the right flank [i_a,i_{a+1}], or inside the crossing rectangle with
j_a<u<j_{a+1}<i_a<w<i_{a+1}.
The rectangle alternative is excluded by saturation. Thus a failed shortcut has a flank collision. Choose an inclusion-minimal collision interval inside that flank; any proper collision subinterval remains in the same flank, so it is globally inclusion-minimal. By 6aba8c1331b7 it gives a genuine primitive linear cycle. Choose this as C_a.

Hence every level a supplies a witness cycle C_a supported in the union of its two annuli, with a shortcut cycle possibly using the boundary edge E_{i_a} as well. Supports for levels whose indices differ by at least two are edge-disjoint: consecutive left annuli are disjoint except at terminal vertices, consecutive right annuli meet only in the boundary hyperedge E_{i_{a+1}}, and nonconsecutive annuli are disjoint.

Therefore the cycles C_a over all odd a are pairwise edge-disjoint, as are those over all even a. One parity class contains at least ceil((m-1)/2) levels. Every chosen cycle has length at least three and uses only ascending nonspecial edges.
