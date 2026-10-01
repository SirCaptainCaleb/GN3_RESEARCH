# A clean joint entrance forbids the immediately preceding first-contact cell

## Statement

Let P=(g_1,...,g_p) be a maximum p-edge path ending at v with last vertex v, with h=g_p. Let e and f be distinct ascending nonspecial edges through v, neither equal h.

Assume e has exactly one contact vertex r in V(P)\\h, and let j be the first path-edge index containing r. Assume f has exactly one contact vertex y in V(P)\\h, that y is the unique entrance of f, and that y is the joint g_{j+1}∩g_{j+2}. Then this configuration is impossible.

## Body

Since r first occurs on g_j and is the only contact vertex of e in V(P)\\h, after omitting g_{j+1} the edge e meets the prefix g_1,...,g_j only in its last edge g_j and has no contact with the retained suffix. As usual e∩h={v} by linearity.

Consider
  g_1,...,g_j,e,h,g_{p-1},g_{p-2},...,g_{j+2}.

This has p edges. The omitted edge g_{j+1} removes any second occurrence of r when r is the joint g_j∩g_{j+1}. Prefix and reversed suffix otherwise inherit only consecutive path intersections, so the displayed sequence is linear.

Its last edge is g_{j+2}. The vertex
  y=g_{j+1}∩g_{j+2}
occurs in no other displayed edge because g_{j+1} is omitted. Hence y is a last vertex and phi(y)>=p.

But y is the unique entrance of the ascending nonspecial edge f. Therefore
  phi(y)=phi(f)-1<=phi(v)-1=p-1,
because v is a terminal of f. Contradiction.
