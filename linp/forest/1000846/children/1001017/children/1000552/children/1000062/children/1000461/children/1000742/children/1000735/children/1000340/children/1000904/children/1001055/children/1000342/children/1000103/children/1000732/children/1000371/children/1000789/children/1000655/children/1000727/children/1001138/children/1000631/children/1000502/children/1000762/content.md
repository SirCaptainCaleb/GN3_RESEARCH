# Terminal-retained edges force repeated maximum-path intersections without lens conversion

## Statement

Let e={x,v,u} be an ascending nonspecial edge with unique entrance x and terminals v,u. Let P_v be a maximum endpoint path ending at v such that u belongs to V(P_v) and x does not. Let P_u and P_x be arbitrary maximum endpoint paths ending at u and x respectively.

Then:

(1) P_v and P_u have at least two common vertices.

(2) At least one of x,v lies on P_u.

(3) If x lies on P_u, then P_u and P_x have at least two common vertices.

(4) If v lies on P_u, then P_v and P_u contain the two distinct common vertices u and v.

Hence every terminal-retained ascending edge produces either a source-recapture repeated-intersection pair P_u,P_x or an explicit reciprocal terminal-terminal overlap P_v,P_u through {u,v}; in all cases P_v,P_u already have at least two common vertices.

If in addition phi(u)>phi(e) and e is terminal-single on P_u, then exactly one of x,v lies on P_u, so the two alternatives in (3),(4) are exclusive.

## Body

The paths P_v and P_u share u. Suppose they shared no other vertex. They are maximum endpoint paths with distinct last vertices v and u. By the certified unique-intersection theorem 5854d853a44b, their unique common vertex u would have to be an internal joint of both paths. But u is the last vertex of P_u, contradiction. Thus
  |V(P_v) intersect V(P_u)|>=2,
proving (1).

Assertion (2) is exactly the reciprocal two-point transversal theorem 8f040f62964a: every maximum path ending at the terminal u of an ascending nonspecial edge contains the unique entrance x or the other terminal v.

Suppose x lies on P_u. Then P_u and P_x share x. If x were their unique common vertex, 5854d853a44b would force x to be an internal joint of P_x, contradicting that x is its last vertex. Hence they have at least two common vertices, proving (3).

If v lies on P_u, then u belongs to both P_v and P_u by hypothesis/endpoint status, and v belongs to both because v is the last vertex of P_v. Since u!=v, this gives (4).

Finally assume phi(u)>phi(e) and e is terminal-single on P_u. Then e cannot be the last edge of P_u. The terminal-single condition says exactly one of x,v occurs in the precursor of P_u; because the last edge already contains u, linearity prevents the other vertex from appearing only in that last edge. Thus exactly one of x,v lies anywhere on P_u, making the alternatives exclusive.

No balanced-lens assertion is used.
