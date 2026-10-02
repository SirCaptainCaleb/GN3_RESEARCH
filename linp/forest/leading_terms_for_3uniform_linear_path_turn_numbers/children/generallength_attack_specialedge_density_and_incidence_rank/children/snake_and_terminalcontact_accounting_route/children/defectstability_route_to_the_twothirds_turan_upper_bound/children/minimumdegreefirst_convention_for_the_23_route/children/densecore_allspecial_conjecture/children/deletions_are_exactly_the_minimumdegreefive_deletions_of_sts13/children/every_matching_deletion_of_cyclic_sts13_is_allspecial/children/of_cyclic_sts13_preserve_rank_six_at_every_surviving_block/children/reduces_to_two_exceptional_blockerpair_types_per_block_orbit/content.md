# Matching-deletion specialness reduces to two exceptional blocker-pair types per block orbit

## Statement

For a surviving block e in a matching deletion of cyclic STS(13), the six explicit rank-six endpoint paths from fb007f7c4b89 already exhibit two distinct entrance labels unless the deleted matching contains one of two stabilizer-orbits of exceptional disjoint same-orbit block pairs.

## Body


Keep the notation and six endpoint-path families from fb007f7c4b89.

For A_0, the six paths have entrance labels
S0:1, S1:4, S2:0, T0:0, T1:1, T2:4.
Their high-frequency blocker indices are K={2,5,6,7,8,11}, whose disjointness graph is
2-7-5-11-6-8-2.
The unique low-frequency blockers are respectively
1,3,9,12,10,4.

Let M be a matching with A_0 not in M.

If M contains no K-indexed A-block, each deleted A-block hits at most one of the six paths. To leave only one entrance label among the surviving six paths, M would have to contain the four unique low blockers belonging to the other two entrance labels. For the three possible surviving labels these four-index sets are
{1,10,3,4}, {9,12,3,4}, {9,12,1,10}.
None is a matching: in the first set A_1 meets A_10, while in the latter two A_9 meets A_12.

If M contains exactly one K-indexed A-block A_h, then A_h hits four of the six paths. The two paths it misses have distinct entrance labels. Moreover their unique low blockers both intersect A_h (this is immediate from the blocker table in fb007f7c4b89), so neither missed path can be killed by another deleted A-block compatible with the matching. Thus two entrance labels survive.

If M contains two K-indexed A-blocks, they must be adjacent in the displayed 6-cycle, and they hit five of the six paths. The unique surviving path is the row whose omitted K-pair is precisely those two indices; its unique low blocker intersects both selected high blocks. Therefore this is the only way the six-path family can fail to display two entrance labels.

Consequently, if A_0 is nonspecial in S\M, then M contains one of the six exceptional disjoint pairs
{A_2,A_7}, {A_7,A_5}, {A_5,A_11},
{A_11,A_6}, {A_6,A_8}, {A_8,A_2}.
Under the stabilizer f(x)=3x+1 these fall into two orbits, represented by
{A_2,A_7} and {A_5,A_7}.

For B_0 the identical argument applies with high-frequency set
L={1,3,4,9,10,12}
and high-block disjointness cycle
1-4-3-12-9-10-1.
The six entrance labels are
S0':2, S1':7, S2':0, T0':0, T1':2, T2':7,
and the unique low blockers are
2,5,6,11,8,7.
Thus a failure of the six-path family to display two entrances forces M to contain an adjacent pair in the B-cycle. Under the stabilizer h(x)=9x+2 there are again only two pair orbits.

By translating an arbitrary surviving A_i or B_i to A_0 or B_0, any counterexample to the matching-deletion all-special statement is therefore reduced to two local exceptional deletion-pair types in each block orbit. In all other matching configurations, the explicit rank-six paths from fb007f7c4b89 already prove specialness.
