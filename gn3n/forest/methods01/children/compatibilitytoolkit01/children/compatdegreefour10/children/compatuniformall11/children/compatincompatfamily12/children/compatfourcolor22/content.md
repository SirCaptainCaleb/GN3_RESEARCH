# The low-degree compatibility branch is four-colorable

## Statement

Assume the low-degree branch of compatdegreefour10 for a minimum counterexample, and let G be the compatibility graph on m chosen deletion covers. Then G is K_4-free and has maximum degree at most four. Hence G is 4-colorable. Consequently G contains an independent set of size at least ceil(m/4), so there are at least ceil(m/4) pairwise incompatible chosen deletion covers. In particular, if m>=21 there are six pairwise incompatible chosen deletion covers, and coloring each incompatible pair by support-incompatibility versus support-compatible order-incompatibility yields, by R(3,3)=6, a triple whose three pairwise incompatibilities all have the same broad type.

## Body

# Proof

By compatdegreefour10, the low-degree branch gives Delta(G)<=4.

The certified global compatibility interface d43a7c9e2f61 says that four pairwise compatible two-cover deletion states in a counterexample glue to a spanning two-cover. Since H is a counterexample, G therefore contains no K_4.

Apply Brooks' theorem componentwise. Every connected component C of G has maximum degree at most four. A component with maximum degree at most three is 4-colorable trivially. If Delta(C)=4, Brooks gives chi(C)<=4 unless C is K_5 or an odd cycle. The K_5 exception is impossible because G is K_4-free, while an odd cycle is 3-colorable. Hence every component is 4-colorable, so chi(G)<=4.

One of the four color classes has size at least ceil(m/4). A color class is independent in G, hence indexes pairwise incompatible deletion covers.

If m>=21, then ceil(m/4)>=6. Choose six labels from one independent set. For each pair, incompatibility is either support-incompatibility or support-compatible order-incompatibility. Color the pair by these two types. Since R(3,3)=6, some three labels form a monochromatic triangle, giving three deletion covers whose three pairwise incompatibilities all have the same broad type.

The factor 1/4 cannot be improved from the abstract graph hypotheses Delta<=4 and K_4-free alone: there exist 4-chromatic K_4-free graphs of maximum degree four. Thus any stronger bound must use additional compatibility geometry, not only these two graph-theoretic constraints.
