# Flat shared-last-edge states have half-density in the terminal-contact window

## Statement


Let P=(g_1,...,g_p) be a maximum endpoint path with last vertex v. Let F be a family of distinct ascending nonspecial edges
  e_i={x_i,v,u_i}
such that:
- v is terminal at e_i;
- phi(e_i)=q_i<p<=phi(u_i);
- the unique off-v contact of e_i with P is u_i;
- for each i there is a maximum p-edge path Q_i ending at u_i whose last edge is an internal host edge g_{j_i}, and Q_i enters g_{j_i} through the forward joint
    z_{j_i}=g_{j_i} intersect g_{j_i+1};
- g_{j_i} is nonspecial ascending of edge rank p with unique entrance z_{j_i}.

For Q<p let
  F_{<=Q}={e_i in F:q_i<=Q}.
Then
  |F_{<=Q}| <= max(0,2Q-p-1).

Consequently, if q_1<=...<=q_k are the edge ranks in F, then
  q_i >= ceil((p+i+1)/2)
for every i.

In particular, the host edges g_{j_i} supporting these flat states occupy pairwise nonconsecutive indices.


## Body


First note that two consecutive host edges cannot both have the stated flat orientation. Suppose g_j and g_{j+1} both have edge rank p and are nonspecial ascending with unique entrances
  z_j=g_j intersect g_{j+1},
  z_{j+1}=g_{j+1} intersect g_{j+2}.
Because z_j is the unique entrance of g_j,
  phi(z_j)=p-1.
But z_j is not the unique entrance of g_{j+1}; it is one of the two terminal vertices of that nonspecial edge. Hence
  phi(g_{j+1},z_j)=phi(g_{j+1})=p,
so phi(z_j)>=p, a contradiction. Thus the supporting indices j_i form an independent set of integers.

Fix e_i of rank q_i<=Q. Since Q_i enters its last edge g_{j_i} through z_{j_i} and ends at u_i, the last vertex u_i is a terminal vertex of g_{j_i}, hence
  u_i in {b_{j_i}, z_{j_i-1}},
where b_j denotes the private vertex of g_j.

The edge e_i has exactly one off-v contact on P, namely u_i. Apply the singleton-contact localization 49080cbf1371.

If u_i=b_{j_i}, then
  p-q_i+2 <= j_i <= q_i-2.

If u_i=z_{j_i-1}, then its occurrence interval on P is {j_i-1,j_i}. The same localization gives
  p-q_i+2 <= j_i <= q_i-1.

Thus in all cases
  p-Q+2 <= j_i <= Q-1.                         (1)

There are
  N=max(0,2Q-p-2)
integer positions in the interval (1). Since the distinct supporting host edges occupy nonconsecutive positions, there are at most ceil(N/2) distinct supporting edges.

A fixed supporting edge g_j can serve at most two members of F: their distinct last vertices u_i must be among its two terminal vertices b_j and z_{j-1}. Therefore
  |F_{<=Q}| <= 2 ceil(N/2) <= N+1
             <= max(0,2Q-p-1),
where the empty-window case is immediate.

Finally, for the i-th ordered rank q_i, apply the bound with Q=q_i:
  i <= 2q_i-p-1,
hence
  q_i >= ceil((p+i+1)/2).
