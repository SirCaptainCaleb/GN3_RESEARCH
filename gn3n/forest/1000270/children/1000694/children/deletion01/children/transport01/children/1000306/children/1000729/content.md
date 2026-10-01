# Endpoint restoration localizes a one-edge-for-two exchange to a bounded reverse boundary window

## Statement

Let H,d,J,T,R_1,L be as in 6431dd7d1ef2, and suppose the endpoint-adjacent inherited block L=(r_1,...,r_j) is not initial in its T-path. Let u be the T-vertex immediately preceding L, and let v be the predecessor of u when it exists. If j>=2, then at least one of the tight reverse triples (d,u,v), when v exists, or (r_1,d,u) occurs. If j=1 and L is terminal, the same conclusion holds using the predecessor-side triples that exist. If j=1 and L is internal with next T-vertex w after r_1, then at least one of (d,u,v), when v exists, (r_1,d,u), or (w,r_1,d) is tight. Thus every endpoint-oriented one-edge-for-two exchange supplies an explicit reverse triple inside a constant-size window consisting of d, the endpoint-adjacent inherited block boundary, and at most two neighboring vertices of T.

## Body

Insert d into the displayed T-path immediately before L and leave the other T-path unchanged. If the resulting path were tight, the two paths would span H, impossible. Hence one of the newly created consecutive triples is non-tight.

Let u be the vertex immediately preceding r_1 in the whole T-path and let v be the predecessor of u if it exists. If j>=2, the new triples are (v,u,d) when v exists, (u,d,r_1), and (d,r_1,r_2). The last is tight because R_1 is inherited from the displayed tight path (d,r_1,...,r_m). Therefore one of the first two existing triples is non-tight. Boundary antisymmetry gives respectively (d,u,v) or (r_1,d,u) tight.

If j=1 and L is terminal, there is no successor triple, so the predecessor-side list is complete. If j=1 and L is internal and w is the next T-vertex after r_1, the new triples are (v,u,d) when v exists, (u,d,r_1), and (d,r_1,w). At least one is non-tight; reversing it gives respectively (d,u,v), (r_1,d,u), or (w,r_1,d). This argument uses the actual neighboring vertices in the whole T-path, so it also covers the case in which the maximal inherited block preceding L has order one.
