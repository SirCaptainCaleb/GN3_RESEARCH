# Three-block matchings in each cyclic STS(13) orbit have two affine types

## Statement

Up to translation and the order-three multiplier automorphism stabilizing a block orbit, a three-block matching inside O_1 has exactly two types, represented by {A_0,A_2,A_7} and {A_0,A_2,A_8}. Likewise a three-block matching inside O_2 has exactly two types, represented by {B_0,B_1,B_4} and {B_0,B_1,B_10}.

## Body

For O_1, normalize one block to A_0. By 0d23d6f61838, the other two indices lie in C_1={2,5,6,7,8,11} and must have difference in C_1. The compatible unordered pairs are {2,7},{2,8},{5,7},{5,11},{6,8},{6,11}. The multiplier automorphism fixing A_0 acts on indices by i -> 3i. It gives two orbits of compatible pairs:
{2,7}->{6,8}->{5,11}->{2,7},
and
{2,8}->{6,11}->{5,7}->{2,8}.
Thus there are exactly two affine types.

For O_2, normalize one block to B_0. The other indices lie in C_2={1,3,4,9,10,12}; compatibility gives pairs {1,4},{1,10},{3,4},{3,12},{9,10},{9,12}. The order-three affine stabilizer of B_0 acts on indices by multiplication by 9 (equivalently its inverse multiplication by 3). Again there are two orbits:
{1,4}->{9,10}->{3,12}->{1,4},
and
{1,10}->{9,12}->{3,4}->{1,10}.
Hence exactly two affine types occur in O_2.

Therefore in the worst 3+1 matching-deletion split, the three-block part has only two canonical forms on either side. The remaining one block lies in the opposite translation orbit and should be analyzed relative to the stabilizer of the chosen heavy matching type.
