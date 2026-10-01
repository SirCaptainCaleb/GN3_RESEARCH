# High-degree-only edges form a universal core of all nonspecial witness paths

## Statement

In the setting of 1e01357bf9c3, let D={v:d_H(v)=k}, where k=floor(2ell/3)+1, and let C={f in E(H): f∩D=∅}. Then for every nonspecial edge e and every longest witness path P ending in e, one has C⊆E(P). Hence every edge of C lies in the intersection of all longest witness paths for every nonspecial edge. In particular, if P and P' are two longest witness paths for the same nonspecial edge and a rotation or splice passes from P to P' by omitting an edge g of P, then g meets D.

## Body

By 1e01357bf9c3, for every nonspecial edge e and every longest witness path P ending in e, each edge f outside E(P) contains a vertex of D.

Therefore an edge f with f∩D=∅ cannot lie outside P. Hence f∈E(P).

Since e and P were arbitrary, every edge in
C={f:f∩D=∅}
belongs to every longest witness path for every nonspecial edge.

For the final assertion, suppose P' is another longest witness path for the same nonspecial edge and g∈E(P)\E(P'). Since g is outside P', the cover property applied to P' implies g∩D≠∅. Thus every edge actually ejected by a witness-path move is D-supported.
