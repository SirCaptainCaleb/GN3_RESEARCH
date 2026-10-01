# Type-A potential levels have a two-level predecessor-capacity recurrence

## Statement

Assume every vertex has endpoint potential at least three. Let E be the set of non-Type-A vertices and, for each integer p, let
  T_p={v: v is Type A and phi(v)=p}.
If T_p is nonempty, then
  |E| + sum_{q<=p-2}|T_q| >= 2p-5.

More precisely, for every v∈T_p the 2p-5 nonspecial terminal edges through v have pairwise distinct unique entrances, all lying in
  E ∪ (union_{q<=p-2} T_q).

## Body

Fix v∈T_p. Since v is Type A,
  t_ns(v)=2p-5.

By a57057ab0001, every nonspecial terminal edge e through v has rank at most p-1. Let x be its unique entrance. Since e is ascending,
  phi(x)=phi(e)-1<=p-2.

If x is Type A, then x∈T_q for some q<=p-2. Otherwise x∈E. Thus every nonspecial terminal edge through v has entrance in
  E ∪ union_{q<=p-2}T_q.

These entrances are pairwise distinct. Indeed, if two distinct hyperedges through v had the same entrance x, they would both contain the pair {x,v}, contradicting linearity.

There are exactly 2p-5 such terminal edges, hence at least 2p-5 distinct vertices in the stated predecessor reservoir. Therefore
  |E|+sum_{q<=p-2}|T_q|>=2p-5
whenever T_p is nonempty.
