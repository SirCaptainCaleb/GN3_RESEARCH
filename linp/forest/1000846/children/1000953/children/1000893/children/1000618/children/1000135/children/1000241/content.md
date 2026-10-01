# The new projective proof explains exactly the d=3 and d=4 exceptional dimensions

## Statement

For the full projective additive system H_d on F_2^d\{0}, any spanning path has joint XOR zero. For d=3 this is already impossible because a spanning P_3 would have two distinct joints. For d=4 rank-nullity forces the six joints to split into two complementary lines, and the 3-by-3 residue grid gives the endpoint contradiction. Beginning at d=5 this proof mechanism cannot yield a universal obstruction: PG(4,2) has a spanning P_15, and in the displayed witness its 14-joint set even contains a zero-sum triple {2,31,29}; the remaining 11 joints also sum to zero, showing precisely why the two-line collapse disappears.

## Body

Let H_d be the additive triple system on F_2^d\{0}. Its total vector sum is zero for d>=2, so the joint-residue normal form gives XOR(J)=0 for every spanning path.

For d=3, H_3 has 7 vertices and a spanning path would have ell=3 and exactly two joints. Two distinct nonzero vectors cannot sum to zero, so H_3 is P_3-free.

For d=4, there are six joints. The rank-nullity lemma forces a zero-sum triple and a zero-sum complementary triple. These are the nonzero points of complementary 2-spaces U and W. Therefore the allowable joint graph is K_{3,3}: pairs within one line are forbidden because their sum is the third joint on that line, while every cross pair has sum outside J. Any joint Hamilton path must alternate between the two lines. Its five internal colors occupy a staircase in the 3-by-3 grid U^*+W^*, leaving four residual grid points. The endpoint-pairing condition of the joint-residue normal form fails, exactly as in d593f8024a92.

For d=5 the conclusion is false. The project object bfc5f55c4e7d exhibits a spanning P_15 with successive endpoint/joint labels
  1,2,4,8,16,21,31,11,17,13,22,15,29,14,9,23.
Thus the 14 joints are
  2,4,8,16,21,31,11,17,13,22,15,29,14,9.
They still have XOR zero, and indeed already contain the zero-sum triple
  {2,31,29},
since 2+31=29 under XOR. Its 11-point complement therefore also has XOR zero. The line is harmless because its three vertices occur far apart in the joint order rather than consecutively. The rank-nullity step has produced a small circuit but no complementary line and hence no bipartite/grid rigidity.

Thus the genuinely general part of the new proof is the joint-XOR/joint-residue machinery. The non-Hamiltonicity conclusion is a small-dimension collapse: d=3 fails at the XOR step, d=4 fails after the forced 3+3 circuit split, while d>=5 requires additional structure and in the full projective family such a structure cannot exist universally because spanning paths do exist.
