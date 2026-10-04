# Exact one-parity step theorem

Use the finite rainbow Hamilton-path lemma for a collection of n tournaments on n vertices to force an exact one-change pattern on one parity stream of an alternating GN3 order, for an arbitrary prescribed split of the opposite-side mediator colors.

RUN-NORMALIZATION THEOREM.

Let |A|=|B|=r. Fix an ordered partition of the mediator colors

  B=C_1 disjoint union ... disjoint union C_k

with every C_j nonempty, and choose signs sigma_j in {+,-}. Choose a partition

  A=U_1 disjoint union ... disjoint union U_k

with |U_j|=|C_j|.

For each j, if sigma_j=+, apply the finite rainbow Hamilton-path lemma to the |C_j| tournaments {T_c[U_j]: c in C_j}. If sigma_j=-, apply it to their complements. In either case obtain an order of U_j whose |C_j|-1 internal gaps have status sigma_j under distinct colors from C_j, leaving one spare color s_j in C_j.

Concatenate the U_j orders. Use s_j on the junction gap from U_j to U_{j+1} for j<k, and put s_k after the last A-vertex as the one mediator not used on an A-gap.

Then:

1. every A-parity status strictly inside U_j is exactly sigma_j;
2. only the k-1 junction A-statuses are uncontrolled;
3. the B-vertex sequence is block-contiguous: all colors of C_1 appear first, then all of C_2, and so on.

Thus any prescribed run pattern on one parity can be realized exactly away from its run boundaries, for every finite size. The one-parity step theorem is the case k=2 with signs +,-, giving 1^* star 0^*.

This normalization is useful because it converts a structural partition of mediator colors into the same ordered block structure in the opposite-parity vertex sequence. The remaining coupling problem is therefore internal to and between corresponding blocks rather than spread arbitrarily across the whole order.
