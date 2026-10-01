# A reciprocal fundamental-cycle terminal lies within the aligned-gate distance budget

## Statement

Retain the hard unique-intersection residual of d0a41dede20a for
  e={x,v,u}
of edge rank r, and let f be the fundamental-cycle neighbor of e sharing terminal v. Let R_e,R_f be maximum endpoint paths ending at the unique entrances of e,f. Assume
  V(R_e) intersect V(R_f)={s},
and let t be the aligned joint index of s on both paths. Thus R_e has length r-1 and, by f4f2089110b2, u belongs to R_f while x does not.

Let d_f(s,u) denote the number of R_f-edges in the path segment between s and u. Then
  d_f(s,u) <= t.

Equivalently, the reciprocal terminal u lies within t path edges of the unique aligned gate s on the neighboring maximum source path. The symmetric statement holds for the other fundamental-cycle neighbor at terminal u.

## Body

The path R_e ends at x, avoids u,v, and has length r-1. Since s is the aligned joint after t path edges, the R_e-segment from s to x contains
  r-1-t
edges.

By f4f2089110b2, R_f contains u and does not contain x; by construction R_f avoids v. Because R_e and R_f meet only at s, the three pieces
  R_e[s,x],  e,  R_f[u,s]
form a linear cycle containing e. Indeed R_e meets e only at x, R_f meets e only at u, and the two path segments meet only at s.

The cycle length is
  (r-1-t)+1+d_f(s,u)
  = r-t+d_f(s,u).
The nonspecial cycle-rank theorem f2925a904b8e says every linear cycle containing e has length at most phi(e)=r. Therefore
  r-t+d_f(s,u) <= r,
which gives
  d_f(s,u)<=t.

The other terminal side is identical.