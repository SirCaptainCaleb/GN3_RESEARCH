# A non-endpoint vertex on a maximum endpoint path forces a second intersection with its own maximum endpoint path

## Statement

Let Q be a maximum endpoint path with last vertex x, and let y be a vertex of Q with y!=x. Let P_y be any maximum endpoint path with last vertex y.

Then
  |V(Q) intersect V(P_y)|>=2.

## Body

The two maximum endpoint paths Q and P_y have distinct last vertices x and y and share the vertex y.

Suppose y were their unique common vertex. By the certified unique-intersection theorem 5854d853a44b, the unique common vertex of two maximum endpoint paths with distinct last vertices must be an internal path joint on both paths, at the same path-edge index.

But y is the last vertex of P_y, so it is not an internal joint of P_y. This contradiction proves that Q and P_y have at least two common vertices.