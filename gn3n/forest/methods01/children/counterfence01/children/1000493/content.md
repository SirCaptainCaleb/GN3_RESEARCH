# The sharp-shell transversal dichotomy is support-theoretically sharp via balanced trees

## Statement

Let lambda>=1 and let T be a tree with 2lambda+1 edges whose two ordinary bipartition classes both have lambda+1 vertices. Identify the ground set V with E(T). For each tree vertex s define
S_s={e in E(T): dist_T(s,e) is odd},
where dist_T(s,e) is the minimum distance from s to an endpoint of e. Then |S_s|=lambda for every s, and for every tree edge e=st,
S_s intersect S_t is empty
and
S_s union S_t = E(T)-{e}.
Moreover the map s -> S_s is injective unless T is a path; when T is a path its two endpoints have the same support and all other supports are distinct, so identifying those endpoints turns T into the (2lambda+1)-cycle. Consequently the forest-or-odd-cycle conclusion of ff3284e79394 is sharp using support incidence alone: every balanced non-path tree occurs as an abstract label-faithful sharp-shell deletion-cover transversal, while the balanced path collapses to the full odd cycle.

## Body

Root T at a vertex s. Every edge f has one endpoint nearer s; if that nearer endpoint is at depth d then dist_T(s,f)=d. The edges at odd distance from s are therefore in bijection with the non-root vertices at even depth: each such vertex contributes its parent edge, and conversely an edge at odd distance has its child at even depth.

Because T is bipartite and its two bipartition classes both have lambda+1 vertices, the class containing s has lambda+1 vertices. Removing the root leaves exactly lambda even-depth vertices. Hence |S_s|=lambda.

Now let e=st be an edge. The label e itself has distance zero from both s and t, so e lies in neither S_s nor S_t. For any other edge f, the unique path from f to the adjacent pair s,t enters through exactly one of s,t; therefore dist_T(s,f) and dist_T(t,f) differ by one. Their parities are opposite, so exactly one of S_s,S_t contains f. This proves
S_s intersect S_t=empty
and
S_s union S_t=E(T)-{e}.

It remains to determine when two tree vertices receive the same support. Across one edge e=xy the preceding paragraph gives
S_x symmetric_difference S_y = E(T)-{e}.
Let s=s_0,s_1,...,s_d=t be the unique s-t path, with path-edge set P={e_1,...,e_d}. XORing the adjacent symmetric-difference identities gives
S_s symmetric_difference S_t =
P, if d is even,
E(T)-P, if d is odd.
If d is even and s!=t, then P is nonempty, so the supports differ. If d is odd, equality can occur only when P=E(T), meaning the s-t path contains every edge of T. That happens exactly when T itself is a path and s,t are its two endpoints.

Thus for a non-path balanced tree all S_s are distinct and the edge identities above embed T itself as an abstract sharp-shell support transversal. For a path, only its two endpoints coincide; identifying them converts the path of 2lambda+1 edges into the cycle of that same odd length. ∎
