# A whole edge yields a rank-bounded cycle or an equal-length entrance-side exchange

## Statement

Let
  h={y,v,w}
be an ascending nonspecial edge of edge rank q with unique entrance y, and let
  R=(g_1,...,g_{q-1})
be a maximum endpoint path with last vertex y such that R,h is a longest q-edge path with last edge h and R avoids v,w.

Let
  e={x,v,u}
be a distinct ascending nonspecial edge of edge rank r terminal at e at v. Assume both x and u lie on R. Let S be a maximum endpoint path with last vertex x such that S,e is a longest r-edge path with last edge e and S avoids u,v.

Orient R so that x occurs before u. Then exactly one of the following alternatives is available:

(A) S has a common vertex z with R on the u-side of x. Choosing such z to minimize the S-distance to x, the union of e, the R-segment between u and z, and the S-segment between z and x is a linear cycle of length at most r.

(B) Every common vertex of S and R other than x lies strictly on the side of x opposite u. Let z be the common vertex closest to x on that side in the R-order. Then the R-segment R[z,x] and the S-segment S[z,x] are internally vertex-disjoint, distinct, and have the same number of edges. Replacing either segment by the other preserves maximum path length at the corresponding last vertex.

Thus every whole edge on the common q-1-edge precursor yields either a rank-bounded cycle through e or an explicit equal-length two-path exchange entirely on the entrance side of x.

## Body

By 76a6a3666ad9, S and R have at least one common vertex besides x.

If some common vertex lies on the u-side of x, alternative (A) is exactly 18b367c33be6: choosing z with minimum S-distance from x gives a linear cycle
  e union R[u,z] union S[z,x]
and the cycle-rank bound gives
  |R[u,z]|+|S[z,x]|+1 <= r.

Assume instead that every common vertex other than x lies on the side of x opposite u. Choose z to be the one closest to x in the R-order.

By this choice, the open R-segment R(z,x) contains no vertex of S. Hence R[z,x] and the S-subpath from z to x are internally vertex-disjoint; they are distinct because otherwise they would share internal vertices.

It remains to compare their lengths. The paths R and S are maximum endpoint paths, ending at the distinct vertices y and x respectively. The two common vertices z,x bound a clean internal two-path exchange. The certified balance theorem 390e818020e1 applies and gives
  |R[z,x]|=|S[z,x]|.
Equivalently, splicing the S-side into R or the R-side into S preserves the total edge length and hence produces another maximum endpoint path with the same last vertex as the path being modified.

No terminal-single hypothesis at u or v, no minimum-terminal assignment, and no D+Y certificate is needed once the whole-edge condition and the chosen maximum source path are available.