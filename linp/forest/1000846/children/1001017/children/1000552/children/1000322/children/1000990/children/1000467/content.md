# Equality-layer strict counterexamples are overwhelmingly threshold-degree

## Statement

Let d=floor(2ell/3), k=d+1, and let H be an edge-minimal counterexample to S_ell with |E(H)|>=d|V(H)|+1. For D={v:d(v)=k} and X=V(H)\\D, one has d|X|<=|D|+ell-2. If X is nonempty then |D|>=k. Thus the strict equality-layer counterexample consists overwhelmingly of exact-threshold vertices; the higher-degree exceptional set has size at most (|D|+ell-2)/d and induces only the universal path forest.

## Body

Fix ell>=4, put d=floor(2ell/3) and k=d+1. Assume H is an edge-minimal counterexample to the equality-layer assertion S_ell of dde3d702703d with
  m=|E(H)| >= d|V(H)|+1.
Then every vertex has degree at least k, H contains a nonspecial edge, and for
  D={v:d_H(v)=k}
the threshold-cover conclusion holds: every edge outside any fixed nonspecial witness path meets D.

Fix a nonspecial witness path P. Let X=V(H)\D. Every edge avoiding D belongs to P, so
  m_0:=|E(H-D)| <= |E(P)| <= ell-1.

The number m_D of edges meeting D is at most the total degree of D:
  m_D <= sum_{v in D} d_H(v)=k|D|.
Therefore
  m=m_0+m_D <= (ell-1)+k|D|.

On the other hand,
  m >= d(|D|+|X|)+1.
Combining and using k=d+1,
  d|D|+d|X|+1 <= (ell-1)+(d+1)|D|,
so
  d|X| <= |D|+ell-2.                       (1)

Thus
  |X| <= (|D|+ell-2)/d.
Since d=floor(2ell/3), the additive term (ell-2)/d is less than 3/2 for ell sufficiently large and is always O(1). In particular the proportion of vertices above threshold is at most about 1/d times the threshold set, unless D itself is very small.

There is also a local size floor on D. Since H-D is a finite linear path forest, if X is nonempty it has a vertex x of internal degree at most one. Because x notin D and delta(H)>=k, one has d_H(x)>=k+1=d+2. Distinct edges through x meeting D use distinct D-vertices by linearity. Hence
  |D| >= d_H(x)-d_{H-D}(x) >= d+1=k.
So any nonregular strict equality-layer counterexample satisfies both
  |D|>=k
and (1).

This turns the strict layer into a near-threshold-degree problem: all but at most roughly |D|/d+O(1) vertices have degree exactly d+1, while the exceptional vertices induce only a path forest.
