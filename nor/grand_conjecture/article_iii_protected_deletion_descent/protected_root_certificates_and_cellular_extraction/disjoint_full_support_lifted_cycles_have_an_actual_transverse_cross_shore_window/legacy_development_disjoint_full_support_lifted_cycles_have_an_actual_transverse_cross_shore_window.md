# Disjoint full-support lifted cycles have an actual transverse cross-shore window — preserved pre-item development

## Development

## Full-support disjoint two-cycle lifted circuits have an actual transverse cross-shore window

Work in one honest switch-prism product carrier cell. Suppose a support-minimal lifted zero has physical support equal to two vertex-disjoint directed cycles on coordinate sets A and B, with A disjoint union B=V, and with opposite nonzero side imbalance.

By the cycle-rank calculation, the lifted support span is
[
H=(W_Aoplus W_B)oplus mathbb R_{m side},
]
of dimension n-1 inside Woplus R. Thus any honest state label whose physical root crosses between A and B is transverse to H.

We show that such a label exists in the SAME carrier cell.

### Carrier blocks

Let F be the ordered-partition face underlying the product cell.

For any block-rank functional beta_F, every physical support root is weakly forward. Since the roots on each directed cycle sum to zero, the sum of their nonnegative block increments is zero. Hence every edge of each cycle is block-neutral.

Therefore all vertices of A lie in one tied F-block, and all vertices of B lie in one tied F-block. These two blocks may coincide. If they are distinct, because A union B=V and there are no other physical vertices, they are the only two nonempty blocks.

### Construct a cross-shore ternary window

Choose distinct a,m in A and b in B. This is possible because a directed simple physical cycle has at least two vertices.

If A and B lie in different carrier blocks, assume the face order is A|B; the reverse case is symmetric. Refine the face so that a,m are the last two A-coordinates and b is the first B-coordinate. Then
[
(a,m,b)
]
is a consecutive ternary window crossing the two shores.

The adjacent refinement obtained by swapping the tied A-coordinates a,m is also legal:
[
(m,a,b).
]

If A and B lie in the same tied carrier block, arrange the same two refinements directly inside that block.

By alternation,
[
alpha(m,a,b)=1-alpha(a,m,b).
]

The threshold target at this fixed window rank and fixed vertical switch state is identical in the two refinements. Therefore exactly one of the two cross-shore windows is a violation.

Choose that state in the honest labeling rule (and choose its reversed window at the reversal-mate state, preserving reversal equivariance). Its genuine honest label has physical component either
[
e_a-e_b
quad	ext{or}quad
e_m-e_b.
]

In either case the physical root crosses from A to B.

### Transversality

Every physical vector in W_Aoplus W_B has zero total coordinate sum separately on A and on B.

A cross-shore root e_u-e_b with u in A and b in B has A-sum +1 and B-sum -1, so
[
e_u-e_b
otin W_Aoplus W_B.
]

Hence its lifted honest label is not in H, irrespective of its side sign.

### Local blow-up

The support-minimal disjoint-cycle zero simplex lies in H and has zero only in its relative interior; every proper face is zero-free.

Subdivide the zero simplex by a new vertex carrying the actual transverse cross-shore honest label constructed above, and cone the old boundary to it. Every new simplex is zero-free:
- with positive coefficient on the new label, projection to (Woplus R)/H is nonzero;
- with zero coefficient, the point lies on a proper face of the old support-minimal zero simplex.

Thus the disjoint full-support two-cycle lifted zero is locally removable relative to its boundary.

### Consequence

After the balanced-single-cycle removal and this theorem, a dimension-saturated full-support honest lifted zero must have CONNECTED physical support of cycle rank two.

By the correct bicyclic classification, the only remaining physical support types are:
- a figure-eight;
- a theta graph.

These connected bicyclic cases have n+1 lifted labels in the n-dimensional honest target and can carry genuine local degree. They are the remaining multi-cycle extraction frontier.
