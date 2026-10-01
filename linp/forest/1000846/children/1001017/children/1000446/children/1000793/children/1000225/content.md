# Potential superlevel cuts isolate ascending edges while retaining all special edges

## Statement

Let H be a finite linear 3-graph with endpoint potential phi. For t>=1 put
  V_t={v:phi(v)>=t}.
Consider an edge e with rank q=phi(e)>=t.

If q>t, then every vertex of e lies in V_t.

If q=t, then exactly one of the following holds:
(i) e is ascending nonspecial, with unique entrance x satisfying phi(x)=t-1; then e has exactly one vertex outside V_t (namely x) and its two terminal vertices lie in V_t;
(ii) e is special or nonspecial nonascending; then all three vertices of e lie in V_t.

Consequently, among all edges of rank at least t, the edges crossing the cut (V_t,V(H)\V_t) are exactly the ascending nonspecial edges of rank t, and every such crossing edge has type 1-outside/2-inside.

## Body

Let e have rank q.

If e is special, the certified entrance-label characterization 7235fdc47d1a implies that every vertex of e is a snake terminal: each vertex is the last vertex of some q-edge path ending in e. Hence phi(v)>=q for every v∈e.

If e is nonspecial with unique entrance x and terminals y,z, then deleting e from a longest q-edge path entering through x gives phi(x)>=q-1, while y,z are last vertices of q-edge paths ending in e, so phi(y),phi(z)>=q.

Now suppose q>t. Then q-1>=t, so even the unique entrance of a nonspecial edge lies in V_t. Hence e⊂V_t.

Suppose q=t. For a nonspecial edge, the terminals lie in V_t. Its entrance lies outside V_t exactly when phi(x)=t-1, which is exactly the definition of an ascending nonspecial edge. If it is nonascending then phi(x)>=t and e⊂V_t. A special edge is already entirely in V_t.

This proves the classification.