# Ascending edges are reciprocal two-point transversals of terminal maximum paths

## Statement

Let e={x,u,v} be any ascending nonspecial edge of rank r, with unique entrance x and terminals u,v. Then every maximum endpoint path ending at u contains x or v. Symmetrically, every maximum endpoint path ending at v contains x or u.

More precisely, if a maximum u-ending path P_u uses e, then phi(u)=r, e is the last edge of P_u, and P_u enters e through x, so x belongs to P_u. If P_u does not use e, then P_u cannot avoid both x and v.

## Body

Put s=phi(u). Since u is a terminal of the rank-r edge e, some r-edge path ending in e has u as a last vertex, so s>=r.

Let P_u be any maximum s-edge path ending at u.

First suppose P_u uses e. Because u is a last vertex and u lies in e, the edge e must be the last edge of P_u: otherwise u would occur in a nonfinal path edge, contradicting that u is a last vertex of the linear path. Thus P_u is an s-edge path ending in e. Since phi(e)=r, s<=r. Together with s>=r this gives s=r. As e is nonspecial, every longest r-edge path ending in e enters e through its unique entrance x. Hence x lies on P_u.

Now suppose P_u does not use e. If P_u avoided both x and v, then e would meet P_u exactly at u. Therefore
  P_u,e
would be a linear (s+1)-edge path ending in e through terminal u. Since s>=r, this has length at least r+1, contradicting phi(e)=r. Thus P_u contains x or v.

The argument with u and v interchanged proves the symmetric assertion. No switching, charging, or rank-gap hypothesis is used.
