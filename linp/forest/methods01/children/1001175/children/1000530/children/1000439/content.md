# A middle source-anchor return closes a rank-budgeted chord cycle

## Statement

Let
  h={y,v,w}
be an ascending nonspecial anchor of rank q with canonical source rail R ending at y, and let
  e={x,v,u}
be a distinct ascending nonspecial whole chord on R of rank r, with canonical clean source rail S ending at x. Thus R avoids v, both x,u lie on R, and S avoids u,v.

Orient R so that x occurs before u. Suppose there is a common vertex
  z in V(S) intersect V(R)
lying strictly on the R-segment between x and u. Choose z closest to u along that segment. Let
  a = number of R-edges from z to u,
  b = number of S-edges from z to x along the S-subpath ending at x.

Then the three pieces
  e, R[u,z], S[z,x]
form a linear cycle of length 1+a+b. Consequently
  a+b <= r-1.

Thus any second source/anchor intersection lying between the entrance x and opposite terminal u carries the same nonspecial rank budget as a return lying beyond u.

## Body

Because z is chosen closest to u among common vertices of S and R on the open x-u segment, the open R-subpath from z to u contains no vertex of S. The canonical source rail S avoids u and v, while R avoids v.

The S-subpath from z to x meets e only at x: source cleanness gives S∩e={x}. The R-subpath from u to z meets e only at u: its vertices lie on the open R-segment between u and x, so x is absent, and R avoids v.

Therefore the three pieces
  e,
  R[u,z],
  S[z,x]
meet cyclically exactly at u,z,x and have no other pairwise intersections. They form a linear cycle. Its edge length is
  1+a+b.

The edge e is nonspecial of rank r. By the certified cycle-rank theorem f2925a904b8e, every linear cycle containing e has length at most r. Hence
  1+a+b <= r,
which is equivalent to
  a+b <= r-1.

The argument uses only the whole-chord geometry and source cleanness; terminal-singleness, payment, and minimum-terminal assignment are not needed.