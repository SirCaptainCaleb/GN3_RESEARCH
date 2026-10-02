# Class-III rank-five nonspeciality reduces to a nine-vertex residual matching obstruction

## Statement

Let H be a 12-vertex 5-regular linear triple system and let e={x,y,z} be a nonspecial edge of global maximum rank five with unique entrance x. Put R=H-{x,y,z}. Then R has 9 vertices, 7 edges, and degree multiset (3,3,3,2,2,2,2,2,2); its three degree-three vertices are exactly the uncovered mates x*,y*,z* of x,y,z. The four edges through y other than e induce a perfect matching F_y on V(R)\{y*}, and the four edges through z other than e induce a perfect matching F_z on V(R)\{z*}. For every pair {u,v} in F_y, R contains no three-edge linear path ending at u with u as a last vertex while avoiding v, and none ending at v with v as a last vertex while avoiding u. The analogous statement holds for every pair of F_z.

## Body

Because H is 5-regular and linear on 12 vertices, each vertex has a unique uncovered mate: its five incident triples cover ten of the other eleven vertices. The uncovered pairs form a perfect matching.

Delete x,y,z. Since e is the unique edge containing any pair from {x,y,z}, the union of the three stars at x,y,z has
5+5+5-2=13
edges: e is counted three times and every other star edge is distinct. Hence
|E(R)|=20-13=7.

Let x*,y*,z* be the uncovered mates of x,y,z. These are distinct because x,y,z are pairwise covered together in e and hence are not uncovered mates of one another.

A residual vertex w not in {x*,y*,z*} is paired in H with each of x,y,z, necessarily in three distinct edges by linearity. Deleting x,y,z removes those three edges, so
d_R(w)=5-3=2.
By contrast x* has no edge with x but has one edge with y and one with z, so deleting x,y,z removes exactly two of its five incident edges and d_R(x*)=3. Likewise d_R(y*)=d_R(z*)=3.
Thus the degree multiset of R is exactly
(3,3,3,2,2,2,2,2,2).

Now consider the four edges through y other than e. Their off-y pairs are pairwise disjoint by linearity. They cover exactly the eight vertices other than y and its uncovered mate y*. Since x and z have been deleted, each such off-y pair lies entirely in V(R). Hence these four pairs form a perfect matching F_y of V(R)\{y*}. The identical argument gives a perfect matching F_z of V(R)\{z*}.

Finally take {u,v} in F_y, so H contains f={y,u,v}. Suppose R had a three-edge linear path Q ending at u with u as a last vertex and avoiding v. Because R avoids x,y,z and Q avoids v, the edge f meets Q exactly in the last vertex u. Therefore
Q,f,e
is a five-edge linear path ending in e through the entrance label y. Since phi(e)=5 and e is nonspecial with unique entrance x, this is impossible.

The same argument with u and v interchanged excludes a three-edge path ending at v with v as a last vertex while avoiding u. The proof for pairs of F_z is identical.