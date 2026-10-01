# Class-III maximum-rank nonspecial edges have only one or two alternating blocker chains

## Statement

Let H be a 12-vertex 5-regular linear triple system and let P=(g_1,g_2,g_3,g_4,e) be a maximum five-edge path ending in a nonspecial edge e={x,y,z} through entrance x. Put W=V(P)\e and let r be the unique vertex outside P. For the two terminal vertices y,z, the double-blocker matchings M_y,M_z on W have total size 6 or 7. Equivalently, M_y∪M_z has exactly two or one path components (isolated vertices counted), with every other component an even alternating cycle.

## Body

Because H is 5-regular on 12 vertices, every vertex has a unique uncovered mate: its five incident triples pair it with exactly ten of the other eleven vertices. Thus the uncovered-pair graph is a perfect matching.

Fix the maximum P_5
P=(g_1,g_2,g_3,g_4,e),
where e={x,y,z} is nonspecial with unique entrance x and y,z are terminal. The path uses 11 vertices, so there is a unique vertex r outside V(P). Put
W=V(P)\e,
so |W|=8.

Consider a terminal vertex v∈{y,z}. Besides e, exactly four edges contain v. By linearity, their two-vertex sets away from v are pairwise disjoint, and none uses either of the other two vertices of e. Hence these four pairs cover eight of the nine vertices in V(H)\e, omitting exactly the uncovered mate v* of v.

Global maximality of P implies that every one of these four edges meets W: if one had both non-v vertices outside W, then since the only vertex outside V(P) is r and the other vertices of e cannot occur by linearity, it would meet P only at v and could be appended after e.

There is only one vertex r outside P. Therefore every edge through v other than e is of one of two types:
- a double blocker, whose two non-v vertices both lie in W;
- a single blocker, whose non-v pair is {r,w} for some w∈W.

Because the four pairs are disjoint, at most one is a single blocker. More precisely:
- if v*=r, then r is the omitted vertex, so all four pairs lie in W and B_P(v)=4;
- if v*≠r, then r is covered by exactly one of the four pairs, giving exactly one single blocker and B_P(v)=3.

The leave is a perfect matching, so r cannot be the uncovered mate of both y and z. Hence
(B_P(y),B_P(z)) is either (3,3), (4,3), or (3,4),
and therefore
B_P(y)+B_P(z)∈{6,7}.

Now apply the certified two-terminal blocker-system lemma 765d552ff81d. The double blockers through y and z form edge-disjoint matchings M_y,M_z on W, their union is an alternating path/even-cycle system, and the number p of path components, isolated vertices included, is
p=|W|-|M_y|-|M_z|=8-(B_P(y)+B_P(z)).
Thus p=2 when the blocker count is 6 and p=1 when it is 7.

So any maximum-rank nonspecial edge in Class III has an exact residual topology: one or two open alternating chains, plus even alternating cycles. Moreover each terminal with blocker count 3 has a unique single blocker, and that edge is precisely the unique terminal edge using the outside vertex r.
