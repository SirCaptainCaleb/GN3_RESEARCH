# Type-A rotation expansion forces linearly many near-top-potential vertices on one witness path

## Statement

Let v be Type A with p=phi(v)>=7. In the saturated rank-(p-1) witness setting of a9ce4e3cd5da, there exists a longest
  P=(g_1,...,g_{p-1}=h)
ending at v such that at least
  2p-12
distinct vertices of V(P) have endpoint potential at least p-1.

More precisely, there are at least p-6 distinct indices
  j∈{1,...,p-4}
for which an early private-contact blocker yields a Posa rotation, and for every such j both vertices of
  g_{j+2}\g_{j+3}
have endpoint potential at least p-1. These two-vertex sets are pairwise disjoint as j varies.

## Body

By a9ce4e3cd5da, at least p-5 genuine early private-contact blockers exist, with contact indices j<=p-4.

For j>=2, the edge g_j has exactly one private vertex, so at most one of these blockers can have a private contact on g_j. The first edge g_1 has two free vertices and can support at most two such blockers. Therefore p-5 blockers use at least
  p-6
distinct contact indices j.

Fix one such index j and an associated blocker f. By a9ce4e3cd5da, f meets P exactly in g_j and the last edge h. The certified two-contact rotation gives the (p-1)-edge path
  (g_1,...,g_j,f,h,g_{p-2},g_{p-3},...,g_{j+2}).

Its last edge is g_{j+2}. Its predecessor is g_{j+3} when j<=p-5, and is h=g_{p-1} when j=p-4; in either case the two vertices of
  g_{j+2}\g_{j+3}
(with g_{p-1}=h in the endpoint case)
are the two possible last vertices. Hence each has endpoint potential at least p-1.

For distinct indices j, the sets
  g_{j+2}\g_{j+3}
are pairwise disjoint: each consists of the private vertex of g_{j+2} together with its left path joint g_{j+1}∩g_{j+2}, and these vertices belong to distinct path positions.

Thus at least p-6 disjoint two-vertex packets have potential at least p-1, giving at least 2p-12 distinct such vertices.