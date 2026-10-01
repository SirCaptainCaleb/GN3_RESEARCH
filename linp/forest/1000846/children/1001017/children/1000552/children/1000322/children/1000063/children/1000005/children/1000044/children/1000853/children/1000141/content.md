# Class-II rank-four nonspeciality forces a crossed terminal rectangle

## Statement

Let H be a 4-regular linear 3-graph with no five-edge linear path. Suppose e={x,y,z} is a nonspecial edge of rank four with unique entrance x, and let P=(g_1,g_2,g_3,e) be a longest path ending in e through x. Write g_1={r,a,b} and g_2={r,c,d}. Then, after swapping c,d, H contains the four forced edges
{y,a,c}, {y,b,d}, {z,a,d}, {z,b,c}.
In particular these four edges are pairwise intersecting and form a K_4 in the intersection graph.

## Body

Orient P so that e is last and g_3∩e={x}; then y,z are the two terminal vertices of e.

Fix one terminal, say y, and let h≠e be an edge through y. We claim h meets g_1.

If h met none of g_1,g_2,g_3, then
g_1,g_2,g_3,e,h
would be a five-edge linear path, impossible.

If the first precursor edge met by h were g_3, then
g_1,g_2,g_3,h,e
would again be a five-edge linear path: h meets e at y and, by the first-contact assumption, is disjoint from g_1,g_2.

If the first precursor edge met by h were g_2, then
g_1,g_2,h,e
would be a four-edge linear path ending in e through y. Since phi(e)=4 and x is the unique longest-path entrance, this is impossible.

Therefore every edge through y other than e meets g_1.

Because H is 4-regular, there are exactly three such y-edges. They are pairwise disjoint away from y by linearity, while g_1 has exactly three vertices. Hence they meet g_1 bijectively: one at r, one at a, and one at b.

Let Y_a be the y-edge meeting g_1 at a. If Y_a were disjoint from g_2, then
g_2,g_1,Y_a,e
would be a four-edge linear path ending in e through y: g_2 is disjoint from Y_a by assumption and from e because P is linear, while g_1 is disjoint from e. This again contradicts the unique entrance x. Thus Y_a also meets g_2.

Its g_2-contact cannot be r, because then Y_a would share both a and r with g_1. Hence it meets c or d. The same argument applies to the y-edge Y_b meeting g_1 at b. Since Y_a and Y_b already share y, linearity forces their g_2-contacts to be distinct. After swapping c,d we therefore have
Y_a={y,a,c},  Y_b={y,b,d}.

Apply the identical argument at the other terminal z. The z-edges Z_a,Z_b meeting g_1 at a,b must meet c,d bijectively. But Z_a cannot use c, because Y_a and Z_a already meet at a and would then share a second vertex c. Hence Z_a uses d, and similarly Z_b uses c:
Z_a={z,a,d},  Z_b={z,b,c}.

Finally every pair among Y_a,Y_b,Z_a,Z_b intersects exactly once:
the same-terminal pairs meet at y or z, while the cross-terminal pairs meet at one of a,b,c,d. Thus they induce a K_4 in the intersection graph.