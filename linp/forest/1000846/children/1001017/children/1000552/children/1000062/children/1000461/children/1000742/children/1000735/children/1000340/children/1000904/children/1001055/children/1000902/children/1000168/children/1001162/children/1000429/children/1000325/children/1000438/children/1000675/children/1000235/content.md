# Distinct doubly occupied switching cells give edge-disjoint local triangles

## Statement

Let P=(g_1,...,g_p) be a maximum p-edge path ending at v, and let F be a family of distinct edges through v, each with exactly one off-v contact with P. Use the interior two-slot cells C_i={b_i,z_i}, 1<=i<=p-3, as in 9a6be27912e0.

For every doubly occupied cell C_i, let f_i^1,f_i^2 be its two blocker edges. Then
  {g_i,f_i^1,f_i^2}
is a linear 3-cycle, and the 3-cycles arising from distinct doubly occupied cells are pairwise edge-disjoint.

Consequently, if D cells are doubly occupied, the hypergraph contains D pairwise edge-disjoint linear 3-cycles supported by those cells.

## Body

The fact that one doubly occupied cell C_i gives the linear 3-cycle
  g_i,f_i^1,f_i^2
is the last assertion of 9a6be27912e0.

It remains only to check disjointness between different cells. Let i!=j be doubly occupied.

First, g_i!=g_j because they are different edges of the path P.

Second, the four blocker edges attached to C_i and C_j are distinct. Indeed every member of F has exactly one off-v contact with P, so one blocker cannot occupy contacts in two different cells.

Third, no interior host edge g_i can equal any blocker edge. Every blocker contains v. Since i<=p-3, the path edge g_i does not contain the last vertex v of P. Hence g_i is not a blocker; similarly for g_j.

Therefore the two triangle edge sets are disjoint. This applies to every pair of distinct doubly occupied cells, proving the claim.

Strengthening pass: neither the rotation-output classification nor payment status is used beyond the already certified single-cell triangle fact. The packing conclusion needs only the one-contact family and the interior-cell geometry.
