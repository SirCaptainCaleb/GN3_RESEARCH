# Minimum-potential equality forces the special-edge subhypergraph to be a cubic-graph dual

## Statement

Under the hypotheses of ce94930a22e0, suppose
  (1/n)sum_v phi(v)=m/n+5/6.
Then for every vertex v,
  t_ns(v)=2phi(v)-3
and
  d_D^-(v)=2phi(v)-1,
where t_ns(v) is the number of nonspecial edges for which v is a terminal and d_D^-(v) is the total snake indegree.

Consequently every vertex of H lies in exactly two special hyperedges.

Let H_sp be the subhypergraph consisting of the special edges. Then H_sp is a linear 3-uniform 2-regular hypergraph. Equivalently, the intersection graph L(H_sp) is a simple cubic graph: its vertices are the special hyperedges, and every original vertex of H corresponds to the unique graph edge joining the two special hyperedges that contain it. In particular
  3s=2n
and s=2n/3.

## Body

By e503661c0fab, equality in the average-potential bound gives Delta_ns=Delta_sn=0. Both are sums of nonnegative local slacks:
  Delta_ns=sum_v[(2phi(v)-3)-t_ns(v)],
  Delta_sn=sum_v[(2phi(v)-1)-d_D^-(v)].
Hence every summand vanishes, giving the two local equalities.

At a vertex v, the total snake indegree is the number of nonspecial terminal incidences at v plus the number s_v of special hyperedges containing v, because every special edge contributes a snake incidence at each of its three vertices and every nonspecial edge contributes snake incidences exactly at its two terminals. Therefore
  s_v=d_D^-(v)-t_ns(v)
     =(2phi(v)-1)-(2phi(v)-3)
     =2.
Thus every vertex lies in exactly two special edges.

Hence H_sp is 2-regular on its vertex side and 3-uniform on its edge side. Since H is linear, two special hyperedges share at most one original vertex. Construct a graph G whose vertices are the special hyperedges and whose edges are the original vertices: the original vertex v joins the two special hyperedges containing v. There are no loops because the two special edges are distinct, and no parallel graph edges because parallel edges would mean two special hyperedges share two original vertices, violating linearity. Each special hyperedge contains three original vertices, so its corresponding graph vertex has degree three. Thus G is simple and cubic.

Finally the incidence count in H_sp gives 3s=2n, so s=2n/3.
