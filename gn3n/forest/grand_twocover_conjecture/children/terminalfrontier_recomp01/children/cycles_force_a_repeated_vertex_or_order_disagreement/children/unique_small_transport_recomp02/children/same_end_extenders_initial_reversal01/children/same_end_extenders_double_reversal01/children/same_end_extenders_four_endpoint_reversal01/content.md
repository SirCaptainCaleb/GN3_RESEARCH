# Universal same-end extenders force four synchronized endpoint reversals

## Statement

Let H be a boundary 3-tournament with pc(H)>2. Let A_1,...,A_q be pairwise vertex-disjoint tight paths of order at least two whose supports, together with distinct vertices x,y, partition V(H), and assume x and y both initial-extend every A_j. Let T=R|S be any exact two-cover of H-{x,y} having no order disagreement with any displayed A_j. Then one of the following holds. (I) One extender z in {x,y} cannot be attached to either end of either R or S; consequently the first and last ordinary edges of both R and S are cross-core and all four corresponding boundary-reversed endpoint triples through z are tight. (II) One residual component U in {R,S} cannot be extended at either end by either x or y; consequently both endpoint edges of U are cross-core and their four boundary-reversed triples through x and y are tight. The terminal-extender version is symmetric.

## Body

For z in {x,y} and U in {R,S}, call z attachable to U if either prepending z to U or appending z to U gives a tight path. Form the bipartite attachment graph B with left class {x,y}, right class {R,S}, and edge zU exactly when z is attachable to U.

If B has a perfect matching, attach the matched extender to the matched residual component at whichever end certifies that edge. The two resulting tight paths are vertex-disjoint and span H, contradicting pc(H)>2. Thus B has no perfect matching. Since B is 2-by-2, Hall's theorem says that either some extender z has no neighbor or some residual component U has no neighbor.

It remains to translate a missing incidence zU. Write U=(u_1,...,u_m), m>=2. If z cannot be prepended, then (z,u_1,u_2) is non-tight. Boundary flip gives (u_2,u_1,z) tight. If u_1,u_2 lay in one displayed core A_j, the tight path (u_2,u_1,z) would place their common pair in the opposite relative order from A_j, contrary to the assumed absence of order disagreement. Hence u_1,u_2 lie in different displayed cores, and (u_2,u_1,z) is a reverse cross-core initial-end triple.

Likewise, failure to append z means (u_{m-1},u_m,z) is non-tight, so boundary flip gives (z,u_m,u_{m-1}) tight. If u_{m-1},u_m belonged to one displayed core, this would reverse their common pair relative to that core and give order disagreement. Hence the terminal edge is cross-core and (z,u_m,u_{m-1}) is the corresponding reverse terminal-end triple.

Therefore every missing incidence zU supplies two positioned reverse endpoint triples, one at each end of U. In Hall alternative (I), the two missing incidences zR,zS give four triples, one at each end of both residual components, all through the same extender z. In alternative (II), the two missing incidences xU,yU give four triples, both ends of one residual component reversed through both extenders. This proves the claim.

The proof uses no size information beyond residual component order at least two and no local case analysis. It strictly strengthens the initial-end Hall obstruction by exploiting both endpoint attachment choices.