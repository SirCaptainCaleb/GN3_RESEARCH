# Zero-slack component partitions have rainbow cut expansion

## Statement

In the zero-slack |D|=k critical-core normal form, let a union A of forest components contain R forest-private vertices. The number of distinct D-colors on connectors crossing A to its complement is at least max{0,k-min(R,2k-R)+1}. Consequently every partition of the c forest components into t>=2 nonempty groups has at least k-floor(2k/t)+1>=t-1 distinct colors represented across the partition.

## Body

Assume the zero-slack |D|=k critical-core setting. Let the path-forest components be C_1,...,C_c, and let P_i be the set of forest-degree-one vertices in C_i. If C_i has a_i edges then
  |P_i|=a_i+2.
Since zero slack means m+2c=2k, the total private mass is
  sum_i |P_i| = 2k.

Every private vertex x has exactly one connector of each color d in D, and in zero slack every such connector pairs x with another forest-private vertex. For fixed x the k mates are distinct by linearity.

Let A be any nonempty proper union of forest components, and put
  R=|P(A)|,
the number of forest-private vertices in A. Choose a physical endpoint x of any component in A. Among the k distinct colored mates of x, at most R-1 lie in A. Therefore at least
  k-R+1
mates lie outside A whenever R<=k, and these crossing connectors have distinct colors because the k edges through x have distinct D-colors. Thus the number of distinct colors crossing the cut (A,bar A) is at least
  max{0,k-R+1}.
Applying the same argument from the complementary side gives the symmetric bound
  chi(A,bar A) >= max{0,k-min(R,2k-R)+1}.

Now partition the c components into t>=2 nonempty groups A_1,...,A_t. Some group has private mass
  R_i <= floor(2k/t).
Hence the set of colors occurring on connectors crossing between different groups has size at least
  k-floor(2k/t)+1.

Because every path-forest component has at least one edge,
  m>=c.
Together with m+2c=2k this gives
  3c<=2k.
Hence for every 2<=t<=c, with k>=3,
  k-floor(2k/t)+1 >= t-1.
(The real function t+2k/t is convex on [2,2k/3], and at the two endpoints is at most k+2; flooring only improves the inequality.)

Therefore every partition of the zero-slack component set into t nonempty groups has at least t-1 distinct connector colors represented across the partition.

This is a component-level rainbow-connectivity condition. It does not by itself assert the existence of a rainbow spanning tree or path; that conversion remains a separate obligation.
