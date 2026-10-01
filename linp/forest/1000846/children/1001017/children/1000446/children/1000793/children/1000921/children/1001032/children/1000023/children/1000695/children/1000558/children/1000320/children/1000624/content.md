# Type-A equality vertices have at most one deficient special incidence

## Statement

Assume a vertex v with p=phi(v)>=3 has Type-A local slack
  a(v)=2, b(v)=0.
Then v lies in exactly four special edges.

For every maximum p-edge path P ending at v:
- if the last edge h is nonspecial, the four special edges through v meet P outside v exactly at the two free vertices of g_1 and the two critical vertices
  C=g_{p-2}\g_{p-3};
  the two far-contact special edges have rank p, and the two critical-contact special edges have rank at least p-1;
- if the last edge h is special, then h and the two special edges using the far free vertices all have rank p.

Consequently at least three of the four special edges through v have rank p. Equivalently, at most one special edge e through v can satisfy phi(e)<phi(v), and any such deficient incidence has phi(e)=phi(v)-1.

## Body

Type A gives
  t_ns(v)=2p-5,
  d_D^-(v)=2p-1.
By 3a0d8866aba9, b(v)=0 forces B_v=0 for every chosen maximum endpoint path, so every incoming edge other than the last has exactly one P-contact outside the last edge.

First suppose the last edge h is nonspecial terminal at v. Then there are t_ns(v)-1=2p-6 other nonspecial terminal edges. In the proof of 672725540541 their latest blockers inject into the tail set S of size 2p-4. The two critical vertices
  C=g_{p-2}\g_{p-3}
cannot receive such a nonspecial blocker, because 672725540541 proves that any nonspecial edge assigned to C must be double-blocking, contradicting B_v=0. Since |S\C|=2p-6, the nonspecial blockers biject exactly onto S\C.

The remaining incoming edges are the four special edges through v. Each needs a distinct P-contact outside h. The only unused vertices are precisely C together with the two free vertices of g_1. Hence the four special edges occupy those four vertices bijectively.

A special edge f using a free vertex of g_1 and no other P-contact yields the p-edge path
  (g_2,...,g_p,f),
so phi(f)=p. A special edge f using a critical vertex c∈C yields
  (g_1,...,g_{p-2},f),
a (p-1)-edge path ending in f, hence phi(f)>=p-1. Since every special incidence satisfies phi(f)<=phi(v)=p, these two edges have rank p-1 or p.

Now suppose h is special. The other incoming edges consist of 2p-5 nonspecial terminal edges and three special edges. Since B_v=0 and total snake indegree is saturated, their single blocker contacts biject all 2p-2 vertices outside h. The nonspecial terminal injection uses 2p-5 tail vertices, leaving one tail vertex plus the two free vertices of g_1 for the three remaining special edges. Hence two of those special edges use the far free vertices and have rank p. Together with h itself, whose rank is p because P is a maximum p-edge path ending in h, at least three special edges through v have rank p.

Finally, if some special edge through v has rank below p, the preceding cases show its rank is at least p-1. Thus it has rank exactly p-1, and there can be at most one such edge because at least three of the four special edges have rank p.