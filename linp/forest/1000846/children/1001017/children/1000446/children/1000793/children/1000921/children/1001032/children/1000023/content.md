# A vertex cannot simultaneously saturate nonspecial-terminal and total snake capacities

## Statement

Let H be a finite linear 3-graph and let v have p=phi(v)>=2. Put
  delta_ns(v)=(2p-3)-t_ns(v),
  delta_sn(v)=(2p-1)-d_D^-(v),
where t_ns(v) is the number of nonspecial edges for which v is a terminal and d_D^-(v) is total snake indegree.

Then delta_ns(v) and delta_sn(v) cannot both be zero.

Equivalently, for every vertex with phi(v)>=2,
  [(2phi(v)-3)-t_ns(v)] + [(2phi(v)-1)-d_D^-(v)] >= 1.

## Body

Suppose for contradiction that delta_ns(v)=delta_sn(v)=0. Then
  t_ns(v)=2p-3,
  d_D^-(v)=2p-1.
Hence exactly two snake-incoming incidences at v are special.

Choose an arbitrary maximum p-edge path
  P=(g_1,...,g_p)
ending at v, with v private to h=g_p.

Apply the proof of the cumulative nonspecial-terminal bound 0e550ff0eadd with q=p. Since t_ns(v)=2p-3, the last edge h must itself be a nonspecial terminal edge at v; otherwise all 2p-3 nonspecial terminal edges would inject into only 2p-4 available tail vertices. The remaining 2p-4 nonspecial terminal edges therefore inject bijectively onto the 2p-4 vertices of
  V(g_2 union ... union g_{p-1}) \ V(h).
Thus every such tail vertex lies in a nonspecial terminal edge through v.

Let f be one of the two special edges through v. Since f is special and v is a snake terminal for f, phi(f)<=p. If f met P only at v, then appending f to P would produce a (p+1)-edge path ending in f, impossible. Therefore f contains some vertex of V(P)\{v}.

By linearity, f cannot contain any of the 2p-4 saturated tail vertices: each already lies with v in a distinct nonspecial terminal edge. It also cannot contain another vertex of h, since f and h already share v. Hence its only possible P-contacts outside v are the two free vertices of g_1 that do not occur in g_2.

Choose such a contact a∈f∩g_1. The third vertex of f cannot lie elsewhere on P by the preceding exclusion; and f cannot contain both free vertices of g_1 because then f and g_1 would share two vertices. Therefore f meets the subpath
  (g_2,...,g_p)
only at v.

Consequently
  (g_2,...,g_p,f)
is a linear p-edge path ending in f, so phi(f)>=p.

Together with phi(f)<=p, the constructed path gives phi(f)=p. Because f is special, v is a snake terminal of f, so there exists a maximum p-edge path ending at v whose last edge is f. But the same saturated-terminal injection argument above applies to every maximum p-edge path ending at v and forces its last edge to be a nonspecial terminal edge, contradicting that f is special.

Therefore delta_ns(v),delta_sn(v) cannot both vanish.