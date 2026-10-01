# Reciprocal type X is a short nonspecial chord cycle

## Statement


Let e={x,v,u} be an ascending nonspecial edge of rank r, with unique entrance x and terminals v,u. Assume r<phi(u), and let P_u be a maximum endpoint path ending at u on which e is terminal-single. Suppose the unique off-u contact of e on P_u is x rather than v.

Then e is not an edge of P_u, and if d is the number of P_u-edges on the segment between x and u, then
  d <= r-1.

Equivalently, every reciprocal terminal-single type-X state closes a linear cycle of length d+1 through e, and this cycle has length at most r.


## Body


Since r<phi(u)=|P_u|, the edge e cannot be the last edge of P_u. It cannot occur earlier either: e contains the endpoint u, while an earlier occurrence of e would place u before the terminal edge and hence repeat u later on the path. Thus e is not an edge of P_u.

By the type-X assumption, P_u contains x and does not contain v. Let P_u[x,u] be the path segment between x and the endpoint u. The edge e meets this segment exactly at x and u. Therefore
  P_u[x,u] union {e}
is a linear cycle. Its length is d+1.

The edge e is nonspecial of rank r, so f2925a904b8e implies
  d+1 <= r.
Hence d<=r-1.
