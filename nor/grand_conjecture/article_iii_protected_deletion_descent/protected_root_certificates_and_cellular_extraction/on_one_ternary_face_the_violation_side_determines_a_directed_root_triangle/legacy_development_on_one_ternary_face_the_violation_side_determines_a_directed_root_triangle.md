# On one ternary face the violation side determines a directed root triangle — preserved pre-item development

## On one ternary face the violation side determines a directed root triangle

Fix an unordered triple F={a,b,c} and choose the reference orientation (a,b,c). Put t=alpha(a,b,c).

For any ordering (u,m,v) of F, attach the window root e_u-e_v.

A direct alternation check gives:

- the three orderings with color t have roots
  e_a-e_c, e_b-e_a, e_c-e_b;
- the three orderings with color 1-t have the opposite roots
  e_c-e_a, e_a-e_b, e_b-e_c.

Thus the six possible ordered windows on one physical triangle split into TWO opposite directed root 3-cycles, and the window color chooses which directed triangle contains its root.

Now normalize a switch target so the pre-switch target color is 0 and the post-switch target color is 1. A violating pre-switch window has actual color 1, while a violating post-switch window has actual color 0.

Therefore, on any fixed physical triangle F:

- all pre-switch violating roots lie in one directed 3-cycle on F;
- all post-switch violating roots lie in the opposite directed 3-cycle.

Equivalently, the side sign of an honest lifted violation label determines which orientation class of the face-root triangle the physical root occupies.

This retains exactly the middle-coordinate information lost by endpoint-root projection. In an A3 block, a lifted root should therefore be viewed as an oriented edge of one of the four triangular facets, with side sign selecting one of the two cyclic orientations of that facet.

This observation is intended for the remaining multi-edge A3 lifted-zero analysis. It does not by itself force a repair.
