# If two rooted graphs intersect in a perfect matching, their remaining edges are complementary 2-factors

## Statement

Let G_e and G_f be the two rooted graphs on the six vertices of X from 84ac56baf953, and suppose M=G_e intersect G_f is a perfect matching and |E(G_e)|,|E(G_f)|>=9. Then (1) |E(G_e)|=|E(G_f)|=9 and G_e union G_f=K_6; (2) G_e and G_f are 3-regular; (3) F_e=G_e-M and F_f=G_f-M are edge-disjoint 2-factors whose union is K_6-M. Consequently each of F_e,F_f is either a six-cycle or two disjoint triangles.

## Body


The rooted-graph theorem 84ac56baf953 gives
|E(G_e)|>=9 and |E(G_f)|>=9.
In the perfect-matching branch of f28243a560f5 their intersection M has exactly three edges. Since both graphs lie in K_6,
|E(G_e union G_f)|
=|E(G_e)|+|E(G_f)|-|M|
<=15.
Therefore
|E(G_e)|+|E(G_f)|<=18.
Together with the two lower bounds this forces
|E(G_e)|=|E(G_f)|=9
and equality in the union bound, so G_e union G_f=K_6.

Each rooted graph has minimum degree at least three by 84ac56baf953. Since a nine-edge graph on six vertices has degree sum eighteen, every vertex has degree exactly three. Thus both G_e and G_f are cubic.

The common graph M is a perfect matching, hence contributes degree one at every vertex. Therefore F_e=G_e-M and F_f=G_f-M are 2-regular spanning graphs on X. Because G_e intersect G_f=M, the two F-graphs are edge-disjoint. Because G_e union G_f=K_6, their union is exactly K_6-M.

Every finite simple 2-regular graph is a disjoint union of cycles. On six vertices with no 2-cycles, the only possibilities are one C_6 or two disjoint C_3's. This proves the claim.
