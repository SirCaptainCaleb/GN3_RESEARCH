# Whole common-anchor chords give a cycle, a clean equal exchange, or a return-order inversion

## Statement

Let
  h={y,v,w}
be an ascending nonspecial edge of rank q with canonical maximum source rail
  R=(g_1,...,g_{q-1})
ending at y, so R,h is a longest q-edge h-path and R avoids v,w.

Let
  e={x,v,u}
be a distinct ascending nonspecial whole chord on R, of rank r, with canonical clean maximum source rail S ending at x. Thus x,u lie on R and S avoids u,v. Orient R so that x occurs before u.

Then at least one of the following holds.

(A) TERMINAL-SIDE CYCLE. Some common vertex of S and R other than x lies on the u-side of x. Then one can choose such a vertex z so that
  e union R[u,z] union S[z,x]
is a linear cycle containing e, hence
  |R[u,z]|+|S[z,x]|+1 <= r.

(B) CLEAN EQUAL EXCHANGE. Every common vertex other than x lies on the side of x opposite u, and the common vertex z nearest x in the R-order is also the common vertex nearest x in the S-order. Then
  R[z,x] and S[z,x]
form a genuine clean two-path exchange, and
  |R[z,x]|=|S[z,x]|.

(C) ORDER INVERSION. Every common vertex other than x lies on the side of x opposite u, but the R-nearest return z_R and the S-nearest return z_S are distinct. Then their order is reversed:
  z_R lies strictly between z_S and x on R,
while
  z_S lies strictly between z_R and x on S.
Thus R and S contain an explicit two-common-vertex braid inversion.

This trichotomy is valid without assuming compatible order of all common vertices.

## Body

By 76a6a3666ad9, R and S have at least one common vertex besides x.

Suppose first that there is a common vertex on the u-side of x in R. Among those vertices choose z minimizing distance to x along S. The S-segment S[z,x] contains no other u-side R-contact in its interior. Since S avoids u and v, and e meets R exactly at x,u while R avoids v, the union
  e union R[u,z] union S[z,x]
has exactly the intended consecutive intersections at x,z,u and no nonconsecutive intersection on the R[u,z] side: any such interior intersection would be another u-side common vertex closer to x on S. Hence it is a linear cycle. The nonspecial cycle-rank bound f2925a904b8e gives the displayed inequality. This is (A).

Now assume every common vertex besides x lies on the side of x opposite u. Let z_R be the common vertex nearest x in the R-order, and z_S the common vertex nearest x along S when S is oriented toward its endpoint x. Both exist.

If z_R=z_S=z, then the open R-segment R(z,x) contains no S-vertex by definition of z_R, while the open S-segment S(z,x) contains no R-vertex by definition of z_S. Therefore each replacement side is internally disjoint from the other full path outside its boundary: R[z,x] and S[z,x] form a genuine clean exchange. Replacing the R-side by the S-side preserves a path ending at y, and replacing the S-side by the R-side preserves a path ending at x. Since R and S are maximum endpoint paths, the two inequalities force
  |R[z,x]|=|S[z,x]|.
This is (B).

Finally suppose z_R!=z_S. Since z_R is R-nearest to x and z_S is another common vertex on the same entrance side,
  z_R lies strictly between z_S and x on R.
Since z_S is S-nearest to x and z_R is another common vertex,
  z_S lies strictly between z_R and x on S.
This is exactly the order inversion in (C).

No assertion is made that arbitrary consecutive common vertices have compatible order. In particular the proof does not use the failed endpoint-lens claim b35b0fd4e4cd.