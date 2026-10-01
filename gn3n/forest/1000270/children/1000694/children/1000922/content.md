# Deletion-cover compatibility forces a sharp linear family relative to one fixed support cut

## Statement

Let H be a boundary tournament with pc(H)>2. Let D be a set of m>=4 vertices, and for each d in D choose a two-cover F_d of H-d. Then either two chosen covers are support-compatible but order-incompatible on their common vertex set, or there is an anchor x in D and a set Y subset D-{x} with |Y|>=ceil((m-3)/3) such that for every y in Y some path of F_y either contains a consecutive pair of common vertices lying in opposite component supports of F_x, or contains x internally with its two neighbors lying in opposite component supports of F_x. In the latter case that consecutive triple through x is tight. The bound ceil((m-3)/3) is the sharp degree guarantee obtainable from K4-free compatibility alone.

## Body

Assume no support-compatible pair is order-incompatible. Let G be the graph on D whose edges are support-compatible pairs. Then every edge is full compatibility. Four pairwise adjacent labels would give four pairwise fully compatible deletion two-covers, and the compatibility-gluing theorem would produce a spanning two-cover of H, contradicting pc(H)>2. Thus G is K4-free; no minimum-counterexample minimality is used.

By Turan's theorem, e(G)<=floor(m^2/3), so the complement has average degree at least (m-3)/3. Hence some x has complement-degree at least ceil((m-3)/3). Let Y be its non-neighbors and fix F_x=P|Q.

Both P and Q have at least two vertices. Indeed, if one component of F_x were a singleton {z}, then the other component together with the two-vertex tight path (x,z) would form a spanning two-cover of H, contradicting pc(H)>2. Therefore, for every y in Y, both P-{y} and Q-{y} are nonempty on U=V(H)-{x,y}.

Fix y in Y. Since x and y are nonadjacent in G, the restrictions of F_x and F_y to U are support-incompatible. Because the two nonempty anchor classes P-{y} and Q-{y} partition U, if every path of F_y met at most one anchor class then its restriction to U would induce exactly the same two support classes, a contradiction. Thus some path R of F_y contains common vertices from both anchor classes.

If a class transition in R uses two consecutive vertices of U, this gives the first asserted alternative. Otherwise every transition between the two anchor classes must pass through x, the unique vertex of F_y outside U. Since x occurs only once on R, it is internal at the unique such transition and its two neighbors lie in opposite anchor classes. Those three consecutive vertices of the tight path R form a tight triple.

Thus all y in Y give the asserted alternatives relative to one fixed support cut of F_x. A balanced complete 3-partite K4-free graph shows the complement-degree bound is graph-theoretically sharp; improving it requires additional boundary-tournament structure.