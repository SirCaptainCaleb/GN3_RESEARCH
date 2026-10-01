# Any source return on the terminal side of a whole chord pays the nonspecial cycle budget

## Statement

Let h={y,v,w} be an ascending nonspecial anchor and let R be a canonical source precursor for h, so R avoids v. Let e={x,v,u} be a distinct ascending nonspecial edge of rank r terminal at v, with both x,u on R, and let S be a canonical clean source rail ending at x.

Orient R so that x occurs before u. Suppose S has a common vertex with R strictly on the u-side of x. Among all such common vertices choose z minimizing the S-distance from x. Let
  a = |R[u,z]|
be the number of R-edges on the segment between u and z, and
  b = |S[z,x]|.
Then
  a+b <= r-1.

Here R[u,z] is the unique R-segment between u and z, regardless of whether z lies between x and u or beyond u. Consequently, the only source-return pattern not carrying this cycle budget is one in which every common vertex of S and R other than x lies strictly on the R-side of x opposite u.

## Body

By the minimal choice of z in S-distance from x among common vertices lying on the u-side of x, the open S-segment S(z,x) contains no vertex of the R-segment R[u,z]. Indeed any such vertex would itself be a common vertex on the u-side of x and would be closer to x along S.

The R-segment R[u,z] does not contain x: both u and z lie strictly on the same side of x in the R-order. Also R avoids v, while S avoids u,v and meets e only at x. Hence
  e union R[u,z] union S[z,x]
is a linear cycle with consecutive intersections u,z,x and no additional intersections.

Its length is
  1+a+b.
Since e is nonspecial of rank r, f2925a904b8e gives
  1+a+b <= r.
Thus a+b<=r-1.

The last assertion is immediate: by 76a6a3666ad9 there is at least one common vertex besides x, and if any such vertex lies on the u-side then the displayed budget applies.
