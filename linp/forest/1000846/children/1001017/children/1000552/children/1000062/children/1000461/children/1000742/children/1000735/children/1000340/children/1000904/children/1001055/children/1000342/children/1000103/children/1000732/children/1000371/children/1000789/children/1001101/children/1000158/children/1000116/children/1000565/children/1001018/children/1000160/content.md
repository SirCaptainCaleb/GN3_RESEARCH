# Sublinear congestion in the original certificate-centered families alone closes 43/48

## Statement

Assume there is a function g(p)=o(p) with the following property. For every relevant choice of maximum endpoint paths and every vertex v of rank p, any family F_v of distinct ascending nonspecial edges terminal at v in which every e={x,v,u}:
(1) is source-clean at its unique entrance x;
(2) is terminal-single on the chosen maximum endpoint paths at both terminals;
(3) satisfies phi(e)<min{phi(v),phi(u)};
(4) carries at v a selected common-anchor D+Y switching certificate,
has |F_v|<=g(p).

Then no 43/48 near-extremal sequence with S/n_+ tending to infinity exists.

Thus it is enough to prove sublinear congestion directly in the original certificate-centered local families. No quotient to distinct underlying edges, minimum-rank terminal assignment, certificate transfer, or same-terminal/uphill split is needed for this reduction.

## Body

Assume toward contradiction that a 43/48 near-extremal sequence exists. For H_j write S_j=sum_v phi(v).

By e2dcd798f528, starting from the lens-free selected families G_v of 7ddb7afd3083 and deleting the o(S_j) center-edge incidences whose opposite terminal is rank-tight, one obtains center-indexed subfamilies F_v such that every e={x,v,u} in F_v is source-clean, terminal-single at both terminals, has
  phi(e)<min{phi(v),phi(u)},
and retains at the center v its selected common-anchor D+Y certificate. Moreover
  sum_v |F_v| >= S_j/8-o(S_j).

Apply the assumed local bound to each F_v:
  sum_v |F_v| <= sum_v g(phi(v)).

Fix epsilon>0. Since g(p)=o(p), choose P such that g(p)<=epsilon p for p>=P and put
  M_P=max_{1<=p<P} g(p).
Then
  sum_v g(phi(v))
  <= epsilon sum_{phi(v)>=P} phi(v)+M_P n_j^+
  <= epsilon S_j+M_P n_j^+.
Because S_j/n_j^+ tends to infinity, M_P n_j^+=o(S_j). Hence
  sum_v g(phi(v))<=epsilon S_j+o(S_j).
As epsilon is arbitrary,
  sum_v g(phi(v))=o(S_j),
contradicting
  sum_v |F_v|>=S_j/8-o(S_j).

No distinct-edge quotient is used: the contradiction is obtained at the center-incidence level where the selected certificate is already located. In particular no comparison between the two terminal vertex ranks is needed beyond the strict two-terminal edge-rank gap itself.
