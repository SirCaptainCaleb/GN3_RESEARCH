# The nonboundary odd half-rank tight collision is one-sided at the middle joint

## Statement

Retain the odd central case of 9b023ed3d700:
  r_i=2m+1 with m>=2,
  r_j=m+1,
  r_{j+1}=m+2,
  R_i=(g_1,...,g_{2m}).
Assume the nonboundary case E_{j+1}!=h, where h=g_{2m} is the host last edge.

Then:
(1) the exact contact of E_j is its unique entrance
    x_j=g_m∩g_{m+1};
(2) the genuine exact contact c_{j+1} of E_{j+1} lies on g_m and is distinct from x_j, hence it is either
    g_{m-1}∩g_m
    or the private vertex of g_m;
(3) consequently
    g_m,E_j,E_{j+1}
    is the unique local 3-cycle host among the two middle edges g_m,g_{m+1}.

Thus every nonboundary tight odd collision is oriented: the rank-(m+1) parent enters at the middle joint, while the rank-(m+2) parent returns on the left middle edge. The sole boundary case m=2, E_{j+1}=h is handled separately in 9b023ed3d700.

## Body

By 9b023ed3d700 the contact c_j is the joint g_m∩g_{m+1}. Since E_{j+1}!=h, both adjacent parents have genuine exact contacts.

If c_j were the opposite terminal of E_j, the stronger bound in 49080cbf1371 would give
  a(c_j)<=r_j-2=m-1.
But its first occurrence is m, contradiction. Hence c_j is the unique entrance x_j of E_j.

The prefix
  Q=(g_1,...,g_m)
is an m-edge linear path ending at x_j. Since E_j is ascending of edge rank m+1, phi(x_j)=m, so Q is maximum at x_j.

Suppose c_{j+1} were absent from V(Q). Exactness gives
  E_j∩V(R_i)={x_i,x_j},
  E_{j+1}∩V(R_i)={x_i,c_{j+1}}.
The endpoint x_i is not in Q, so
  Q,E_j,E_{j+1}
is a linear path of length m+2=r_{j+1} ending in E_{j+1} through the terminal x_i, not its unique entrance x_{j+1}. This contradicts nonspeciality. Hence c_{j+1}∈V(Q).

By 9b023ed3d700, c_{j+1} lies on g_m or g_{m+1} and its occurrence interval overlaps [m,m+1]. Since it lies in Q and is distinct from x_j, it must be either g_{m-1}∩g_m or the private vertex of g_m.

Both contacts therefore lie on g_m and are distinct, while E_j∩E_{j+1}={x_i}; hence g_m,E_j,E_{j+1} is a linear 3-cycle. The edge g_{m+1} contains x_j but not c_{j+1}, so it is not a host for this local triangle.