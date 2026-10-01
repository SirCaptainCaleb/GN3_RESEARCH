# Any sublinear local bound on the paid two-terminal-gap subclass breaks 43/48 saturation

## Statement

Assume there is a function g(p)=o(p) with the following property. For every relevant choice of maximum paths, at each vertex v of rank p, at most g(p) source-clean, doubly-terminal-single, paid-certified ascending nonspecial edges can be assigned to v as a minimum-rank terminal while having edge rank strictly below both terminal vertex ranks. Then no 43/48 near-extremal sequence with S/n_+ -> infinity exists. In particular, an O(log p) bound on this narrow local class is sufficient to force a strict asymptotic improvement below the 43/48 leading coefficient.

## Body

Suppose a 43/48 near-extremal sequence existed. By 9fba15f1495c, for each member of the sequence there is a set Epp of distinct paid-certified source-clean doubly-terminal-single ascending nonspecial edges with
  |Epp| >= (1/16-o(1))S,
and both terminal vertex ranks are strictly larger than the edge rank.

Assign every e={x,u,v} in Epp to a terminal of minimum vertex rank, breaking ties arbitrarily. If e is assigned to v, then the other terminal u satisfies phi(u)>=phi(v), while
  phi(e)<phi(v).
Thus e lies in the local class covered by the assumed bound, and therefore
  |Epp| <= sum_v g(phi(v)).                                           (1)

It remains to show the right side is o(S). Fix epsilon>0. Since g(p)=o(p), choose P so that g(p)<=epsilon p for p>=P. Put M=max_{1<=p<P} g(p). Then
  sum_v g(phi(v))
  <= M n_+ + epsilon sum_{v:phi(v)>=P} phi(v)
  <= M n_+ + epsilon S.
Because S/n_+ -> infinity, M n_+=o(S). Since epsilon is arbitrary,
  sum_v g(phi(v))=o(S).
This contradicts |Epp| >= (1/16-o(1))S.

Hence such a sublinear local bound excludes asymptotic saturation of the current 43/48 coefficient. The special case g(p)=O(log p) is immediate.
