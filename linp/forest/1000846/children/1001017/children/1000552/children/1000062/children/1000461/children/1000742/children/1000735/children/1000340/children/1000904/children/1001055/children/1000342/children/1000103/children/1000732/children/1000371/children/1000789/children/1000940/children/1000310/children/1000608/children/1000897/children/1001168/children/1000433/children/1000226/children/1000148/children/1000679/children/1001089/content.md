# The even half-rank central collision has one surviving two-entrance pattern and a full-length rotation

## Statement

Retain the even central case of 9b023ed3d700:
  r_i=2m with m>=3,
  r_j=r_{j+1}=m+1,
  R_i=(g_1,...,g_{2m-1}),
and neither adjacent parent is the host last edge.

Let
  L=g_{m-1}∩g_m,
  B=the private vertex of g_m,
  R=g_m∩g_{m+1}.
Then the two genuine exact contacts of E_j,E_{j+1} are exactly B and R, in some order, and both contacts are the unique entrances of their parent edges.

Let F be the parent edge whose exact contact is B. Then F meets R_i exactly at B and the last vertex x_i, and
  g_1,...,g_m,F,g_{2m-1},g_{2m-2},...,g_{m+2}
is a (2m-1)-edge linear path.

Consequently
  phi(g_{m+2})>=2m-1=r_i-1,
and both g_{m+1}∩g_{m+2} and the private vertex of g_{m+2} have vertex rank at least 2m-1.

## Body

By the even central case of 9b023ed3d700, m>=3 and the two exact contacts are two distinct members of {L,B,R}.

The contacts B and R cannot be opposite terminals. For either one the first occurrence index is m, while the stronger opposite-terminal bound in 49080cbf1371 would require
  a<=r_j-2=m-1.
Thus any parent edge using B or R has that contact as its unique entrance.

We exclude the pair {L,R}. Let F_L,F_R be the corresponding parent edges, with R the unique entrance of F_R. The path
  g_1,...,g_{m-1},F_L,F_R
is linear: F_L meets the prefix only at L, F_R has no prefix contact, and the two parent edges meet at x_i. Its length is m+1 and its last vertex may be R, which is absent from the preceding path. Hence
  phi(R)>=m+1.
But R is the unique entrance of the ascending rank-(m+1) edge F_R, so phi(R)=m, contradiction.

The pair {L,B} is excluded identically, using the parent edge whose unique entrance is B. Hence the contact pair is exactly {B,R}, and both are unique entrances.

Let F be the parent edge with contact B. Since B is private to g_m, exactness says F meets R_i only at B and x_i. Apply a51a7f9cff95 with p=2m-1 and j=m. Because m>=3, j<=p-2, and the rotation yields
  g_1,...,g_m,F,g_{2m-1},g_{2m-2},...,g_{m+2},
a (2m-1)-edge linear path with last edge g_{m+2}. Thus phi(g_{m+2})>=2m-1.

The private vertex of g_{m+2} and the backward joint g_{m+1}∩g_{m+2} are absent from all preceding edges of the rotated path: g_{m+1} is omitted, and F has only its two exact R_i-contacts B,x_i. Either may therefore be chosen as the last vertex, so both have vertex rank at least 2m-1.
