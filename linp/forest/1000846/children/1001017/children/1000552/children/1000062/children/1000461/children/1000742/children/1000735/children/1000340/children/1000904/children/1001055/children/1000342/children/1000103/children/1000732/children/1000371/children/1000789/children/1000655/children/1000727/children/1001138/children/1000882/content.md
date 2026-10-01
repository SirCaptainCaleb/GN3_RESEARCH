# Terminal-only singleton ranks have a cumulative four-slot bound

## Statement

Let P=(g_1,...,g_p) be a maximum p-edge path ending at v. Let U be a family of ascending nonspecial edges e={x,v,u} terminal at v such that each e has exactly one off-v contact with P, that contact is the opposite terminal u, and the unique entrance x is absent from P.

For an integer R<p, let U_{<=R}={e in U: phi(e)<=R}. Then
  |U_{<=R}| <= max{0,4R-2p-4}.

Consequently, if the ranks in U are ordered
  rho_1<=...<=rho_k,
then
  rho_i >= ceil((2p+i+4)/4).
Writing x_i for the absent entrance of the edge of rank rho_i,
  sum_{i=1}^k phi(x_i)
  >= (p/2)k + k(k+1)/8.

Thus a long terminal-retained singleton family forces quadratic, not merely linear, total endpoint potential on its distinct omitted entrances.

## Body

Fix e={x,v,u} in U_{<=R}, with rank r<=R. Let a be the first path-edge index containing u. By 028c2c3f7167, terminal-only singleton localization gives
  p-r+1 <= a <= r-2.
Hence
  p-R+1 <= a <= R-2.                                  (1)

For every internal path index j, exactly two path vertices have first occurrence index j: the private vertex of g_j and the forward joint g_j intersect g_{j+1}. Distinct edges through v have distinct opposite terminals by linearity. Therefore (1) gives at most
  2[(R-2)-(p-R+1)+1]
  =4R-2p-4
possible terminal contacts. This proves the cumulative bound (with zero when the interval is empty).

Now order the U-ranks. Applying the cumulative bound with R=rho_i gives
  i <= 4rho_i-2p-4,
hence
  rho_i >= ceil((2p+i+4)/4).

Since each edge is ascending, phi(x_i)=rho_i-1. Dropping only the harmless ceiling,
  phi(x_i)>=p/2+i/4.
Summing i=1,...,k gives
  sum_i phi(x_i)
  >= (p/2)k + k(k+1)/8.

The entrance vertices x_i are distinct because distinct edges through v already share v and linearity forbids a second common vertex.
