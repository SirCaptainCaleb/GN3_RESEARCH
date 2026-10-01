# Certificate-at-either-terminal sublinear congestion closes 43/48

## Statement

Assume there is a function g(p)=o(p) with the following property.

For every relevant choice of maximum endpoint paths, let E be any family of distinct ascending nonspecial edges e={x,u,v} such that:
(1) e is source-clean at its unique entrance x;
(2) e is terminal-single on the chosen maximum endpoint paths at both terminals u,v;
(3) phi(e)<min{phi(u),phi(v)};
(4) e carries a selected common-anchor D+Y switching certificate at at least one of its two terminals, with that certificate terminal retained as part of the data.

Assign every e in E once to a terminal of minimum vertex rank. Suppose that, at every vertex w of rank p, at most g(p) assigned edges occur.

Then no 43/48 near-extremal sequence with S/n_+ tending to infinity exists.

In particular, any o(p) local bound for this certificate-at-either-terminal class is sufficient to force a strict asymptotic improvement below 43/48.

## Body

Assume toward contradiction that a 43/48 near-extremal sequence exists. Apply the lens-free strict-gap extraction e2dcd798f528. It gives, for each member H_j, a set E_j of distinct edges satisfying (1)--(4) and
  |E_j| >= (1/16-o(1))S_j.

Assign every e in E_j once to a terminal of minimum vertex rank. If d_j(w) is the resulting assigned degree at w, the assumed local bound gives
  d_j(w)<=g(phi(w)),
and hence
  |E_j|<=sum_w g(phi(w)).                              (1)

Fix epsilon>0. Since g(p)=o(p), choose P so that
  g(p)<=epsilon p
for p>=P. For p<P, put
  M_P=max_{1<=p<P} g(p).
Then
  sum_w g(phi(w))
  <=epsilon sum_{phi(w)>=P} phi(w)+M_P n_j^+
  <=epsilon S_j+M_P n_j^+.
Because S_j/n_j^+ tends to infinity,
  M_P n_j^+=o(S_j).
Therefore
  sum_w g(phi(w))<=epsilon S_j+o(S_j).
As epsilon is arbitrary,
  sum_w g(phi(w))=o(S_j).

This contradicts |E_j|>=(1/16-o(1))S_j.

The proof uses the minimum-rank terminal only for the counting assignment. The selected switching certificate is not transferred between terminals.
