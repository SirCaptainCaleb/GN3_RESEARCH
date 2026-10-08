# Fully curved tetrahedra are universal switch gadgets — preserved pre-item development

## Fully curved tetrahedra are universal switch gadgets

Let (Q={a,b,c,d}) be a four-set in a pure alternating triangle orientation (alpha). Recall that (Q) is **fully curved** when, for every pivot (xin Q), the link tournament (G_x) on (Qsetminus{x}) is a directed triangle.

### Theorem

If (Q) is fully curved, then every linear ordering
[
(x_1,x_2,x_3,x_4)
]
of its four vertices has opposite consecutive statuses:
[
alpha(x_1,x_2,x_3)

e
alpha(x_2,x_3,x_4).
]

Thus every order of a fully-curved tetrahedron has exactly one color change.

### Proof

Fix an ordering
[
(a,b,c,d).
]
Look at the link tournament (G_b) on ({a,c,d}). Since (Q) is fully curved, this is a directed 3-cycle.

Now
[
alpha(a,b,c)=alpha(b,c,a)
]
by cyclic invariance. Hence the first status records the direction of the edge between (c) and (a) in (G_b).

The second status
[
alpha(b,c,d)
]
records the direction of the edge between (c) and (d) in the same link tournament.

At a vertex (c) of a directed triangle, exactly one of the two incident edges to (a,d) points outward and the other inward. Therefore the two bits are opposite:
[
alpha(a,b,c)oplusalpha(b,c,d)=1.
]
Since the chosen ordering was arbitrary, the conclusion holds for every ordering. (square)

### Consequences

A fully-curved tetrahedron is an unavoidable local switch: whenever its four vertices occur consecutively in a coordinate order, the NOR word changes color between the two associated windows.

Therefore any one-change spanning order can contain at most one consecutive four-window whose underlying four-set is fully curved.

This identifies the nonlinear part of the tetrahedral curvature decomposition combinatorially:
- singly-curved tetrahedra are the mod-2 coboundary defects;
- fully-curved tetrahedra are order-independent switch-forcing 4-hyperedges.

The remaining pure-orientation problem may therefore be viewed as an ordering problem that simultaneously routes around the coboundary defects and avoids more than one consecutive fully-curved tetrahedron.
