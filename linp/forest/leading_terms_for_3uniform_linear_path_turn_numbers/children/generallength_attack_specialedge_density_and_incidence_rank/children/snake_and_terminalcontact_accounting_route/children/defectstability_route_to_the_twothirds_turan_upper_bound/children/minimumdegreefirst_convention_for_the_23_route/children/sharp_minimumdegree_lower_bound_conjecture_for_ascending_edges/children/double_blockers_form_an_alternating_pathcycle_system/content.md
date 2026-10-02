# Two-terminal double blockers form an alternating path-cycle system

## Statement

Let P=(g_1,...,g_{L-1},e) be a globally longest linear path in a linear 3-graph, where e={x,y,z} is nonspecial and g_{L-1}∩e={x}, so y,z are the two terminal vertices of e. Put W=V(P)\e, |W|=2L-2. For v∈{y,z}, let M_v consist of the unordered blocker pairs (f\{v})⊂W arising from edges f≠e through v whose two non-v vertices both lie in W. Then M_y and M_z are matchings on W, they are edge-disjoint, and M_y∪M_z is a simple graph of maximum degree at most two whose nontrivial components are alternating paths and even cycles. Moreover |M_v|=B_P(v). If p is the number of path components of M_y∪M_z, isolated vertices included, then p=(2L-2)-(B_P(y)+B_P(z)).

## Body

Fix v=y or z. Two distinct edges through v cannot share any further vertex, so the blocker pairs of double blockers are pairwise disjoint and M_v is a matching on W. If the same pair {u,w} belonged to both M_y and M_z, the corresponding hyperedges {y,u,w} and {z,u,w} would intersect in two vertices, violating linearity. Hence the matchings are edge-disjoint. Their union has maximum degree at most two and at each degree-two vertex the incident edges have different colors, so each nontrivial component is an alternating path or an even alternating cycle. The edge counts are |M_v|=B_P(v). In any finite graph of maximum degree at most two whose components are paths and cycles, |V|-|E| equals the number of path components when isolated vertices count as paths. Therefore p=|W|-(|M_y|+|M_z|)=2L-2-B_P(y)-B_P(z).