# Each cyclic STS(13) block orbit has matching number three

## Statement

Let O_1={A_i:i in Z_13} and O_2={B_i:i in Z_13}, where A_i={i,i+1,i+4} and B_i={i,i+2,i+7}. Then the largest matching contained in either O_1 or O_2 has size exactly 3.

## Body

For O_1, two blocks A_i,A_j intersect exactly when j-i lies in {±1,±3,±4}; hence they are disjoint exactly when the nonzero difference lies in C_1={±2,±5,±6}={2,5,6,7,8,11}. Suppose four A-blocks were pairwise disjoint. Translating indices, take one to be A_0. The other three indices must lie in C_1. They cannot contain both members of any opposite pair {2,11},{5,8},{6,7}, because those two indices differ by 4,3,1 respectively, all intersection differences. Thus they must choose one element from each opposite pair. Up to negating all indices, assume 2 is chosen from {2,11}. Compatibility with the second pair forces 8 rather than 5, because 8-2=6 is a disjointness difference whereas 5-2=3 is not. Compatibility with the third pair forces 7 rather than 6, because 7-2=5 is a disjointness difference whereas 6-2=4 is not. But 8-7=1 is an intersection difference, contradiction. Thus nu(O_1)<=3. The three blocks A_0,A_2,A_7 are pairwise disjoint, so equality holds.

For O_2, two blocks B_i,B_j intersect exactly when j-i lies in {±2,±5,±6}; hence they are disjoint exactly when the nonzero difference lies in C_2={±1,±3,±4}={1,3,4,9,10,12}. The same argument applies. If four pairwise disjoint B-blocks existed, normalize one index to 0. The remaining three must choose one element from each opposite pair {1,12},{3,10},{4,9}. Up to negation assume 1 is chosen. Compatibility forces 10 rather than 3, since 10-1=9 is allowed while 3-1=2 is not, and forces 4 rather than 9, since 4-1=3 is allowed while 9-1=8 is not. But 10-4=6 is an intersection difference, contradiction. Thus nu(O_2)<=3. The blocks B_0,B_1,B_4 are pairwise disjoint, so equality holds.

Consequently any matching M of at most four blocks in the cyclic STS(13), written p=|M intersect O_1| and q=|M intersect O_2|, satisfies p,q<=3. In particular a four-block matching has split 3+1 or 2+2 between the two translation orbits.
