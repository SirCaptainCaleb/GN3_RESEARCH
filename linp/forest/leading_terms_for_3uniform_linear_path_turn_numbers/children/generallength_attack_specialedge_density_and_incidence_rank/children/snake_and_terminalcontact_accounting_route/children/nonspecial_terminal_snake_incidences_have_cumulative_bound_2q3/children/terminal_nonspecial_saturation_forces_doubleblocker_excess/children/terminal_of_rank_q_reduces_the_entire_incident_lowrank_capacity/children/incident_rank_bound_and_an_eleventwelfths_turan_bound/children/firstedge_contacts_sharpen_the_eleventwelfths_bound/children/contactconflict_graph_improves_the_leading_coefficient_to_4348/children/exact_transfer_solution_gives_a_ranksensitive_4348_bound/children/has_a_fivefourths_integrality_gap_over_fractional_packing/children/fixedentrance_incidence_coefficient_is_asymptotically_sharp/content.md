# The eleven-eighths fixed-entrance incidence coefficient is asymptotically sharp

## Statement

For every k>=1 there is a finite linear 3-graph H_k with maximum linear-path length q=8k+4 and an ascending edge h of rank q, with terminal v, such that |{f containing v: phi(f)<=q}|=11k+1=(11/8)q-9/2. Hence the universal fixed-entrance bound on ALL low-rank incident edges cannot have leading coefficient below 11/8. This is not a lower bound of 43/48 for the Turan problem; the competing incident edges are not assumed ascending.

## Body

For every integer k>=1 put q=8k+4. We construct a finite linear 3-graph H_k with an ascending edge h of rank q and a terminal v such that
 |J_q(v)|=11k+1=(11/8)q-9/2,
where J_q(v)={f containing v: phi(f)<=q}. Consequently no universal bound |J_q(v)|<=c q+O(1) with c<11/8 is possible. This concerns ALL low-rank incident edges, not only ascending edges terminal at v.

CONSTRUCTION.
Begin with a linear q-edge path P=(g_1,...,g_q). Write z_i=g_i cap g_{i+1}, g_1={a_1,b_1,z_1}, and g_i={z_{i-1},b_i,z_i} for 2<=i<=q-1. Put h=g_q={x,v,w}, where x=z_{q-1}. All labels are distinct except these prescribed path intersections.

The internal columns are (b_i,z_i), 2<=i<=q-3=8k+1. Partition them into 2k consecutive blocks of four columns. In each block beginning at i=2+4j, 0<=j<=2k-1, select the three vertices
 b_i, z_i, b_{i+1}.
Let T be the selected set; |T|=6k. For each t in T introduce a distinct new vertex y_t and add the edge {v,t,y_t}.

There are five unselected internal vertices per four-column block. Pair the unselected vertices in the first k blocks with their translated copies in the final k blocks:
 b_i is paired with b_{i+4k}, and z_i with z_{i+4k}.
For each of these 5k pairs {a,b}, add {v,a,b}. There are no other edges. The six W-vertices outside the internal columns, namely a_1,b_1,z_1,b_{q-2},z_{q-2},b_{q-1}, are unused by added edges.

All added edges meet at v and have otherwise disjoint vertices. A two-contact edge uses two positions separated by 4k path indices, so it meets no base edge twice. Single-contact edges also meet base edges at most once. Thus H_k is linear. No added edge meets g_1 or g_{q-1}. An added edge can meet g_{q-2} only at z_{q-3}, which also belongs to g_{q-3}.

GLOBAL PATH-LENGTH BOUND.
Let Q=(g_1,...,g_{q-1}), and let F consist of h and all added edges. Every edge of F contains v, and every edge of F meets V(Q). A linear path uses at most two edges of F, and if it uses two they are consecutive; three would contain nonconsecutive edges sharing v. Removing its F-edges leaves at most two contiguous subpaths of Q.

If two such subpaths occur, they omit at least one Q-edge: otherwise the adjacent base edges at the separation would be nonconsecutive in the new path. Thus they use at most q-2 base edges, and adding at most two F-edges gives length at most q. If only one Q-subpath occurs, length greater than q could only mean all q-1 Q-edges plus two F-edges. Those F-edges form a block at an end, and its outside edge must avoid Q entirely. This is impossible because every F-edge meets Q. Hence every linear path has length at most q. The original P has length q, so phi(h)=q and all added edges have rank at most q.

UNIQUE ENTRANCE OF h.
A q-edge path ending in h through v must have an added edge f immediately before h. It then has exactly q-2 Q-edges before f. Those Q-edges form a contiguous subpath avoiding x, hence are exactly g_1,...,g_{q-2}. Their order must be forward: the other orientation would require f to meet g_1, which no added edge does. But every added-edge contact on g_{q-2} is z_{q-3}, also on the nonconsecutive g_{q-3}. So this is not a linear path. The vertex w belongs only to h and cannot be an entrance. Therefore all longest h-paths enter through x; h is nonspecial, with terminals v,w.

RANK OF x.
The prefix Q gives phi(x)>=q-1. We rule out a q-edge path ending at x. Only g_{q-1} and h contain x. Ending in h at x would require entrance v, already excluded. Thus its last edge is g_{q-1}. It cannot contain h: if h were consecutive with g_{q-1}, their intersection x would prevent x from being a last vertex; otherwise their intersection violates linearity.

Such a path therefore uses zero, one, or two added edges. Zero gives length at most q-1. With one added edge, length q requires all Q-edges. They must form a consecutive block, so the added edge comes first and meets g_1, impossible.

With two added edges, exactly one Q-edge is omitted. If the omitted edge is g_1, the two added edges precede g_2,...,g_{q-1}; the first added edge would have to avoid that entire segment, impossible because all its contacts are internal. The final Q-edge cannot be omitted. Thus the omitted edge is g_{i+1} for some 1<=i<=q-3, and the sequence must be
 g_1,...,g_i,f,f',g_{i+2},...,g_{q-1}.
Here the first Q-component is forward because no added edge meets g_1.

For f to have two contacts, its extra contact must lie in the sole omitted edge g_{i+1}; its retained contact must belong to the forward part of g_i. Such two contacts would both lie within g_i union g_{i+1}. This is impossible for the constructed two-contact edges, whose two positions are separated by 4k>=4. The same argument for f' uses g_{i+1} union g_{i+2}. Hence both f,f' must be single-contact edges.

Their contacts must then form one of the fixed-entrance forbidden pairs: a vertex in {b_i,z_i} (with g_1 used at i=1) and a vertex in {b_{i+2},z_{i+1}}. But T avoids all these pairs. Indeed its column pattern is
 (b,z), (b), empty, empty,
repeated; any occupied column i has z_{i+1} and b_{i+2} unselected. Boundary columns are also unselected where needed. This final possibility is impossible.

Thus phi(x)=q-1, and h is ascending.

COUNT AND CONSEQUENCE.
Every edge incident with v is h or one of the 6k single-contact and 5k double-contact edges. All have rank at most q by the global path-length bound. Therefore
 |J_q(v)|=1+6k+5k=11k+1.
As k grows, |J_q(v)|/q tends to 11/8.

This realizes the contact-transfer leading slope in actual linear hypergraphs with the required ascending last edge. It is stronger than an abstract conflict-graph obstruction: changing the chosen longest h-path, or adding more correct constraints while still seeking a universal bound on all of J_q(v), cannot lower that leading slope. The construction does NOT establish a 43/48 lower bound for the global Turan problem and does NOT assert that all counted edges are ascending terminal edges. A further global improvement may exploit those additional labels or combine this local resource with other incidence information.