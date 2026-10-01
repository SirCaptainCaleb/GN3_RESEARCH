# A forward whole-chord reintersection pays a nonspecial cycle budget

## Statement

Retain the hypotheses and notation of ed412ed8e3b1 and suppose branch (B) occurs. Let z be the first vertex of S that lies on the far suffix of R from u toward y, when that suffix is traversed starting at u. Let
  a = number of R-edges from u to z along that suffix,
  b = number of S-edges from z to x along S toward its endpoint x.

Then
  a+b <= r-1.

Equivalently, the first reintersection that allows a forward whole chord to evade the deficit-shallow alternative cannot be simultaneously far from u on the host rail and far from x on the clean source rail.

## Body

By the choice of z, the open R-subpath from u to z contains no vertex of S. The source path S avoids u, and source cleanness gives S∩e={x}; the host path R avoids v, while the R-subpath from u to z lies after x and therefore does not contain x. Hence the three pieces
  e,
  R[u,z],
  S[z,x]
form a linear cycle: consecutive pieces meet at u,z,x respectively, and there are no other intersections.

Its length is
  1+a+b.
The edge e is nonspecial of rank r. By f2925a904b8e, every linear cycle containing a nonspecial edge of rank r has length at most r. Therefore
  1+a+b <= r,
which is the claimed inequality.
