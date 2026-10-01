# Class-II rank-three nonspeciality forces an alternating terminal C6

## Statement

Let H be a 4-regular P_5^(3)-free linear triple system. Suppose e={x,y,z} is nonspecial of rank three with unique entrance x, and let P=(g_1,g_2,e) be a longest path ending in e through x. Then the six edges through the terminal vertices y,z other than e induce two edge-disjoint perfect matchings on the same six-vertex set, whose union is a single alternating 6-cycle.

## Body

Write
g_1={a,b,r},  g_2={r,c,x},  e={x,y,z}.
Thus V(g_1) is disjoint from e, and c is the private vertex of the middle edge g_2.

Let h≠e be any edge through the terminal vertex y. We claim h is disjoint from g_1. Indeed, if h met g_1, then
g_1,h,e
would be a three-edge linear path ending in e through y: g_1 is disjoint from e, while the two consecutive intersections are g_1∩h and {y}. Since phi(e)=3, this would be a longest path ending in e with entrance y, contradicting the unique entrance x.

Also h cannot contain x or z, since h already contains y and e contains the pairs {x,y} and {y,z}; linearity forbids repeating either pair.

Hence the two vertices of h other than y lie in the six-vertex set
S=V(H)\bigl(V(g_1)∪{x,y,z}).
This set has size six because H has twelve vertices, and it contains c.

There are exactly three edges through y other than e because H is 4-regular. Their off-y pairs are pairwise disjoint by linearity, so three disjoint 2-subsets of the six-set S. Therefore they form a perfect matching M_y of S.

The identical argument at the other terminal z gives a perfect matching M_z of the same set S.

The two matchings have no common edge. If {u,v} belonged to both, the hyperedges {y,u,v} and {z,u,v} would share the two vertices u,v, contradicting linearity.

Thus M_y∪M_z is a 2-regular graph on six vertices whose edges alternate between the two matchings. Every component is an even cycle. A 2-cycle would be a common matching edge, which is impossible. Since the total number of vertices is six, the only possibility is one alternating 6-cycle.

Equivalently, the six terminal hyperedges consist of two 3-cliques in the intersection graph (the y-star and z-star), with cross-intersections prescribed by an alternating C_6 on their off-terminal pairs.