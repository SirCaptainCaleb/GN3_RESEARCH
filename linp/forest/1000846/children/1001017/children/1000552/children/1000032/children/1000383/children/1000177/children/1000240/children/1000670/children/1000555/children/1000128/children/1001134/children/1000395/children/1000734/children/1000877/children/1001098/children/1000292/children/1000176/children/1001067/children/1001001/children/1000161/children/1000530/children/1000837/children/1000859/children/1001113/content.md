# Large narrow-rank exchange families reduce to repeated source overlap or laminar host intervals

## Statement

Let R be a linear path and let F be a family of N equal-length path exchanges of the form
  I_i=R[z_i,x_i],
  A_i=S_i[z_i,x_i],
where each S_i is a maximum endpoint path with last vertex x_i, I_i and A_i are internally vertex-disjoint and have the same number of edges, and the x_i are distinct unique entrances of distinct ascending nonspecial edges terminal at one common vertex. Assume all corresponding edge ranks lie in an integer interval of width D.

Assume further that every pair S_i,S_j has exactly one common vertex. Then there is a subfamily of size at least
  K=floor(N/(6(D+1)))
whose host intervals have pairwise distinct endpoints, and this subfamily contains at least one of:

(1) ceil(sqrt(K)) pairwise disjoint host intervals;
(2) ceil(K^(1/4)) pairwise nested host intervals;
(3) ceil(K^(1/4)) pairwise crossing host intervals.

Moreover every pairwise crossing subfamily has size at most D+1. Hence if
  K^(1/4)>D+1,
outcome (3) is impossible and a quantitatively large pairwise disjoint or pairwise nested subfamily is forced.

Thus, unless two maximum source paths already have at least two common vertices, sufficiently large narrow-rank exchange families reduce to a laminar host-interval family.

## Body

Under the hypothesis that every pair S_i,S_j has exactly one common vertex, apply c0e80055b547 at each fixed return vertex z. For one side of z on R, at most D+1 exchanges can use z; allowing both sides gives at most
  2(D+1)
members of F with the same return vertex.

Choose one exchange for each distinct return vertex. This leaves at least
  M >= N/(2(D+1))
intervals with distinct z_i. The x_i are already pairwise distinct by linearity of the underlying common-terminal hyperedges. A vertex can therefore occur as an endpoint of at most two selected intervals: once as some z_i and once as some x_j. The graph joining intervals that share an endpoint has maximum degree at most two, so it has an independent set of size at least M/3. Hence there is a subfamily of size
  K >= floor(N/(6(D+1)))
whose host intervals have all endpoints distinct.

Consider these K intervals. Let alpha be the maximum size of a pairwise disjoint subfamily and omega the maximum size of a pairwise intersecting subfamily. The intersection graph of intervals is perfect; equivalently it can be colored with omega colors. Hence
  K <= alpha*omega.
If alpha>=sqrt(K), outcome (1) holds.

Otherwise omega>sqrt(K). Choose omega pairwise intersecting intervals. By the Helly property for intervals they have a common host point. Order them by increasing left endpoint. Their right endpoints are distinct. By the Erdos-Szekeres monotone subsequence theorem, there is a subfamily of size at least
  ceil(sqrt(omega)) >= ceil(K^(1/4))
whose right endpoints are monotone. If they decrease, the intervals are pairwise nested, giving (2). If they increase, the common-point condition makes them pairwise crossing, giving (3).

Finally, 0b61bef44e7f shows that under the standing assumption that every pair S_i,S_j has exactly one common vertex, any pairwise crossing subfamily from an edge-rank band of width D has size at most D+1. Therefore if K^(1/4)>D+1, alternative (3) cannot occur, leaving (1) or (2).
