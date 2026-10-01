# Low-vertex-rank labels occupy a bounded central window on a linear path

## Statement


Let P=(g_1,...,g_L) be an L-edge linear path in a linear 3-uniform hypergraph, and let R be an integer with 0<=R<L.

Then the number of vertices z in V(P) with
  phi(z)<=R
is at most
  max{0, 4R-2L+1}.

More precisely, if such a vertex z is private to one path edge g_i, then
  L-R+1 <= i <= R.
If z is the joint g_i intersect g_{i+1}, then
  L-R <= i <= R.

Consequently, when R>=ceil(L/2), all vertices of P with vertex rank at most R consist of at most
  2R-L
eligible private vertices and
  2R-L+1
eligible joints.


## Body


Apply 8b1790d79d74.

If z is private to g_i, then
  phi(z)>=max{i,L-i+1}.
Thus phi(z)<=R implies
  i<=R
and
  L-i+1<=R,
hence
  L-R+1<=i<=R.
Because R<L, all these eligible edges are internal path edges, and each has exactly one private vertex. There are
  R-(L-R+1)+1=2R-L
such edges, when this number is positive.

If z=g_i intersect g_{i+1} is a path joint, then
  phi(z)>=max{i,L-i}.
Thus phi(z)<=R implies
  L-R<=i<=R.
There are
  R-(L-R)+1=2R-L+1
such joints, when this number is positive.

Adding the two capacities gives
  (2R-L)+(2R-L+1)=4R-2L+1.
If R<ceil(L/2), 8b1790d79d74 already shows that no vertex of P can have vertex rank at most R.
