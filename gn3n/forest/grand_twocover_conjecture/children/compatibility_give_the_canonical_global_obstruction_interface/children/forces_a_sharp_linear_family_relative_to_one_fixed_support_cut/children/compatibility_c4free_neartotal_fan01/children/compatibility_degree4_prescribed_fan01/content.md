# Deletion-cover compatibility has maximum degree four, forcing prescribed-anchor crossing fans

## Statement

Let H have path-cover number greater than 2, and let D be m>=4 deletion labels with chosen two-covers F_d of H-d. Assume there is no pair of deletion covers that is support-compatible but order-incompatible. Then the full-compatibility graph C on D has maximum degree at most 4. More precisely, for any anchor x with F_x=P|Q, the compatible neighbors of x split according to whether their restored label lies on P or Q; each side-class is a clique and therefore has size at most 2, since four mutually compatible deletion covers are forbidden. Hence every prescribed anchor x has at least m-5 support-incompatible covers. Relative to F_x, each such cover has the crossing witness from forces_a_sharp_linear_family_relative_to_one_fixed_support_cut. Consequently e(C)<=2m and C has an independent set of size at least ceil(m/5), giving a linear pairwise support-incompatible subfamily.

## Body

Fix x and write F_x=P|Q. For every y compatible with x, pairwise compatibility determines which anchor support class contains y: after deleting x and y, the two covers have the same two support classes, and restoring x in F_y and y in F_x occurs in the same class. Partition N_C(x)=N_P union N_Q accordingly.

Take y,z in N_P. On the common vertex set V(H)-{y,z}, the support partition induced by F_y is ((P-{y,z}) union {x}) | Q, and the support partition induced by F_z is the same. Thus F_y and F_z are support-compatible. By the standing hypothesis, support-compatible/order-incompatible pairs do not occur, so F_y and F_z are fully compatible. Therefore N_P is a clique. The same argument shows N_Q is a clique.

If |N_P|>=3, then x together with any three vertices of N_P would form four mutually compatible deletion covers, contradicting the four-cover gluing obstruction from compatibility_give_the_canonical_global_obstruction_interface because pc(H)>2. Hence |N_P|<=2, and similarly |N_Q|<=2. Thus deg_C(x)<=4. Since x was arbitrary, Delta(C)<=4.

Therefore every anchor x has at least (m-1)-4=m-5 nonneighbors. Under the standing hypothesis, a nonneighbor cannot be support-compatible, so every nonneighbor is support-incompatible. Applying the certified first-crossing conclusion of forces_a_sharp_linear_family_relative_to_one_fixed_support_cut to each such y gives, relative to F_x=P|Q, either an ordinary F_y edge crossing between common P- and Q-side vertices, or x internal in an F_y path with its two neighbors on opposite anchor sides, yielding a tight triple through x across the cut.

The degree bound also gives e(C)<=2m. Finally, greedily selecting a vertex and deleting it together with its at most four neighbors produces an independent set of size at least ceil(m/5). This is a pairwise support-incompatible deletion-cover subfamily.

This strictly strengthens the earlier C4-free/O(sqrt(m)) estimate: the crossing fan is now m-5 and is available from every prescribed anchor, while the mutually incompatible family is linear rather than order sqrt(m).