# Doubly extremal bad states have a fully curved target switch — preserved pre-item development

## Composition

(none yet)

## Development

## Doubly extremal bad states have a fully-curved target switch

Continue with the doubly extremal threshold state:
- its target-compatible central band has globally maximum length B;
- among B-maximal states, the distance from the target switch to the nearest unresolved full-curvature boundary is minimum.

Subsection 155 reduces a flat target switch to a full boundary within at most three transition slots. The three-slot case is impossible by subsection 157. We eliminate distances one and two.

Write the target colors locally as x before the cut and 1-x after it.

### Distance one

Suppose the nearest full boundary is one transition slot to the right of the flat target switch. Then the old local status pattern is
[
x, 1-x, x,
]
because the first post-switch window is matched and the next window is the first mismatch.

Repair the flat target switch toward the boundary. The endpoint-repair packet replaces
[
x, 1-x, z
]
by
[
x, x, 1-z.
]
Here z=x, so the new local statuses begin
[
x, x, 1-x.
]

Move the proposed cut one slot to the right, onto the old full-boundary transition. The two statuses before the new cut have target x and the next status has target 1-x, so all three displayed windows are matched. Every previously matched window farther to the left is unchanged.

Thus the central matched band gains at least one window, contradicting global maximality of B.

### Distance two

Suppose the nearest full boundary is two transition slots to the right. The old local statuses begin
[
x, 1-x, 1-x, x.
]
A distance-two transport would land exactly on the occupied full boundary and annihilate two switches, closing NOR. Therefore counterexamplehood forces the repair selector to distance three.

For the distance-three branch, the old transition immediately beyond the full boundary must be absent, so the next status is also x. The old packet is therefore
[
x, 1-x, 1-x, x, x.
]

The audited repair law gives
[
x, x, x, 1-x, x.
]
Now move the proposed cut two slots to the right, onto the old full-boundary transition. The first three displayed statuses lie on the x side of the new threshold and the fourth lies on the 1-x side, so they are all matched. The fifth is the first possible mismatch.

Hence the maximal target-compatible band again gains at least one window, contradicting maximality of B.

### Theorem

A doubly extremal bad threshold state cannot have a flat target switch.

Therefore
[
oxed{	ext{the tetrahedron carrying the proposed target switch is fully curved.}}
]

Combined with the maximal-band normal form, every terminal flat-sector obstruction can be chosen so that:
- the desired switch itself is a fully-curved universal-switch gadget;
- every unresolved boundary of the target-compatible band is also fully curved.

Thus all flat mobility has been eliminated. The remaining ternary coboundary-flat problem is purely a barrier-crossing problem among fully-curved tetrahedra.
