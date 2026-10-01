# Lens-free flat cycles have disjoint distance-two rails and late distance-three terminal joints

## Statement

In the entrance-rail lens-free flat gap-one terminal cycle, every pair R_i,R_{i+2} is vertex-disjoint. Moreover, if h_i is the aligned joint level of
  V(R_i) intersect V(R_{i+3})={t_{i+2}},
then
  ceil((p-2)/2) <= h_i <= p-4.
Consequently, a lens-free flat terminal cycle cannot have length five.

## Body

First we prove the distance-two disjointness. Fix i and suppose R_{i+1} meets R_{i+3}. In the lens-free residual it cannot have two common vertices with R_{i+3}, since two common internal vertices of equal-length maximum endpoint paths yield a balanced elementary lens. Thus their intersection is unique.

The other two pairs in the triple R_i,R_{i+1},R_{i+3} are also uniquely intersecting:
  V(R_i) intersect V(R_{i+1})={y_i}
by 960a5153b900, while
  V(R_i) intersect V(R_{i+3})={t_{i+2}}
by 8777d2ccd614.
The vertex y_i is not t_{i+2} by 960a5153b900. But 8e3ab4a34ced says that three equal-length maximum endpoint paths whose three pairwise intersections are unique must have one common intersection vertex. This contradiction proves
  V(R_{i+1}) intersect V(R_{i+3})=emptyset.
Shifting indices gives V(R_i) intersect V(R_{i+2})=emptyset for every i.

Now apply 87b1d2ae8b86 to
  A=R_{i+1}, B=R_i, C=R_{i+3}.
The A-B intersection is the aligned joint y_i at level k_i, the B-C intersection is t_{i+2} at level h_i, and A,C are disjoint by the preceding paragraph. Hence
  min{k_i,h_i} >= ceil((p-2)/2).
In particular h_i>=ceil((p-2)/2). The upper bound h_i<=p-4 is part of 8777d2ccd614.

Finally suppose c=5. Then R_i and R_{i+2} are distance three in the reverse cyclic orientation, so 8777d2ccd614 says they intersect. This contradicts the distance-two disjointness just proved. Hence no lens-free flat terminal 5-cycle exists.