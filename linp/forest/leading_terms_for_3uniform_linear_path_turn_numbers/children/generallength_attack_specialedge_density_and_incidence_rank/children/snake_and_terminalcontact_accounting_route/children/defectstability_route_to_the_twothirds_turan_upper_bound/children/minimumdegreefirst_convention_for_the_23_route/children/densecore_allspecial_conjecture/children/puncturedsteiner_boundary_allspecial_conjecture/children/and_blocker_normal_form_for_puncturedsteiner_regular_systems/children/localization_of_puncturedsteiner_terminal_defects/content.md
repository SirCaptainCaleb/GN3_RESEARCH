# General early-or-penultimate localization of punctured-Steiner terminal defects

## Statement

In the setting of efe44a01f2dc, let P=(g_1,...,g_{d-1},e) be a maximum d-edge path ending in a nonspecial edge e={x,y,z} through entrance x. Fix a terminal v∈{y,z} and an edge h≠e through v. Then either h meets one of g_1,...,g_{d-3}, or h is the unique single blocker through v and has the form {v,o,p}, where o is the unique vertex outside P and p is the private vertex of the penultimate precursor edge g_{d-1}.

## Body

Let i be the first precursor index for which h meets g_i.

If i=d-2, then by first-contact minimality h is disjoint from g_1,...,g_{d-3}. The sequence
g_1,g_2,...,g_{d-2},h,e
has d edges. Its consecutive intersections are inherited along the path, then h∩g_{d-2}, then h∩e={v}. All nonconsecutive pairs are disjoint: h has no earlier precursor contact by minimality, and e is disjoint from g_1,...,g_{d-2} because P is linear. Thus this is a longest d-edge path ending in e through the terminal label v, contradicting that e is nonspecial with unique entrance x.

Hence i cannot equal d-2.

Suppose h has no contact in g_1,...,g_{d-3}. Since every terminal edge through v must block the globally longest path P somewhere besides v, h must meet g_{d-1}; otherwise it would meet P only at v and could be appended after e to create a (d+1)-edge path.

Because h avoids g_1,...,g_{d-2}, its contact p with g_{d-1} cannot be the joint g_{d-2}∩g_{d-1}; therefore p is the private vertex of g_{d-1}.

There is no second vertex of h\{v} on P. Indeed any such second path vertex would lie either in an earlier precursor edge, contrary to the assumption, or again in g_{d-1}, which would make h share two vertices with g_{d-1}, violating linearity. Thus the third vertex of h is outside P. Since a d-edge linear path uses 2d+1 of the 2d+2 vertices of H, there is a unique outside vertex o. Hence
h={v,o,p}.

Finally, two distinct v-edges of this form would share the pair {v,o}, impossible by linearity. Thus this is the unique single blocker through v.

Therefore every terminal defect is either supported in the genuinely early segment g_1,...,g_{d-3}, or is pinned to the private vertex of the penultimate precursor edge.