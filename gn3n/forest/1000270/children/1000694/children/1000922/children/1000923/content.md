# Neighborhood-sparse compatibility forces a sharp half-scale incompatibility anchor

## Statement

Let H be a boundary tournament with pc(H)>2, and let D be a set of m>=10 deletion labels with one chosen deletion two-cover F_d for each d in D. Let G be the graph on D in which two labels are adjacent when their chosen covers are fully compatible on their common vertex set. Then some x in D is nonadjacent to at least floor((m-1)/2) other labels. This bound is graph-theoretically sharp under the certified neighborhood condition Delta(G[N_G(v)])<=2.

Consequently, for a minimum counterexample H of order n>10, using all n deletion labels, there is one deletion cover F_x and a set Y of at least floor((n-1)/2) other labels such that every F_y, y in Y, is incompatible with F_x. For each y in Y, either F_y is support-compatible with F_x but has order disagreement on their common vertex set, or F_y is support-incompatible and hence crosses the fixed support cut of F_x in the concrete sense of 1000922. In particular, if no support-compatible pair is order-incompatible, then one fixed anchor cut is crossed by at least floor((n-1)/2) deletion covers.

## Body

Write d for the minimum degree of G and choose x with d_G(x)=d. Put N=N_G(x) and M=D-({x} union N), so |M|=m-1-d.

The certified compatibility-neighborhood theorem compatneighborhood02 gives Delta(G[N_G(v)])<=2 for every v. Suppose for contradiction that d>=floor(m/2)+1.

For u in N, write a_u=d_{G[N]}(u) and b_u=|N_G(u) intersect M|. Since a_u<=2 and d_G(u)>=d,
b_u=d_G(u)-1-a_u>=d-3.
Also
a_u=d_G(u)-1-b_u>=d-1-|M|=2d-m.
Under d>=floor(m/2)+1, this lower bound is positive, so G[N] contains an edge uv.

Both u and v have at least d-3 neighbors in M. Hence
|N_G(u) intersect N_G(v) intersect M|
>=2(d-3)-|M|
=2d-6-(m-1-d)
=3d-m-5.
The vertex x is another common neighbor of u and v, so the compatibility edge uv has codegree at least
3d-m-4.
For m>=10 and d>=floor(m/2)+1 this quantity is at least three: for even m=2r it is at least r-1>=4 when m>=10, and for odd m=2r+1 it is at least r-2>=3 when m>=11. This contradicts the certified edge-codegree-at-most-two consequence used in compatneighborhood02. Therefore d<=floor(m/2).

Thus x has at least
m-1-floor(m/2)=floor((m-1)/2)
nonneighbors, proving the graph claim. The constant is sharp for this graph-theoretic input because a complete bipartite graph with balanced parts satisfies Delta(G[N(v)])=0 and every vertex in a largest part has exactly floor((m-1)/2) nonneighbors.

Now let G be the full compatibility graph of the chosen deletion covers. Nonadjacency of x and y means F_x and F_y are not fully compatible. Either their support partitions agree on the common vertex set but their relative orders disagree, or their support partitions differ. In the latter case, the fixed-cut argument of 1000922 applies verbatim: writing F_x=P|Q on H-x and U=V(H)-{x,y}, some path of F_y contains common vertices from both P-{y} and Q-{y}; hence either a consecutive pair of common vertices lies on opposite sides of the fixed P|Q cut, or the unique transition passes through x, whose two path-neighbors lie on opposite sides and form a tight consecutive triple through x.

For a minimum counterexample, mincex01 gives n>10, so taking D=V(H) yields the stated half-scale anchored family. If support-compatible order disagreement never occurs, every one of the at least floor((n-1)/2) nonneighbors lies in the support-incompatible crossing case.