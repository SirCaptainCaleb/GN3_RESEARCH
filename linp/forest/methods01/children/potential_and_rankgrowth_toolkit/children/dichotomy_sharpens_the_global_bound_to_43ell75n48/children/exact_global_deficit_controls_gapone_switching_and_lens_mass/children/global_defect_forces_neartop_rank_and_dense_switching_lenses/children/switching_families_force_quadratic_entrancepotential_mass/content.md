# Switching families force quadratic entrance-potential mass

## Statement

Let v be an active misaligned vertex with p=phi(v)>=8, let P_v be the chosen maximum p-edge path, and let F_v be any switching family from b032348c1a8a. For f in F_v write x_f for its unique entrance. Then
  sum_{f in F_v} phi(x_f) >= (p/2)|F_v|-p-5.
Consequently
  sum_{f in F_v} phi(x_f)
  >= (p/2)[beta(p)-eta_v-ceil((3q(v)-4)/4)]-p-5.
In particular, if eta_v=o(p), then
  sum_{f in F_v} phi(x_f) >= (5/16-o(1))p^2.

Moreover, if switching families F_v are chosen simultaneously at several centers, then
  2 sum_{e ascending} phi(x_e)
  >= sum_v sum_{f in F_v} phi(x_f),
because an ascending hyperedge has only two terminal vertices and hence can belong to at most two center-indexed switching families.

## Body

Fix v and partition F_v into two classes according to which off-v vertex lies on P_v.

Class X: the retained vertex is the unique entrance x_f. Let a be the number of such edges. Since f is ascending nonspecial and v is a terminal with phi(v)=p, the certified terminal-rank inequality a7b7670e955a gives
  p<=2phi(f)-2.
As phi(x_f)=phi(f)-1,
  phi(x_f)>=ceil(p/2).
Therefore
  sum_{f in X}phi(x_f)>=a p/2.                          (1)

Class U: the retained vertex is the opposite terminal u_f, so x_f is absent from P_v. Let k=|U|. These are terminal-only singleton ascending edges through v on the same maximum p-edge path. Order them by their terminal contact positions on P_v. The theorem 5bbd8a32451a gives
  sum_{f in U}phi(x_f)
   >= [k(p+3)-2p-10]/2
   >= k p/2-p-5.                                       (2)

Combining (1) and (2), and writing s=|F_v|=a+k,
  sum_{f in F_v}phi(x_f)>=s p/2-p-5.                   (3)

Now invoke b032348c1a8a:
  s>=beta(p)-eta_v-ceil((3q(v)-4)/4).
Substitution into (3) gives the exact displayed bound. Since q(v)<=p-1,
  beta(p)-ceil((3q(v)-4)/4) >= (5/8)p-O(1),
so eta_v=o(p) yields
  sum_{f in F_v}phi(x_f)>=(5/16-o(1))p^2.

For the global multiplicity statement, fix an ascending hyperedge e={x,u,w}. It has exactly two terminals u,w. A center-indexed switching family F_v consists only of edges terminal at its center v. Hence e can occur among all chosen F_v at most twice, once at u and once at w. Each occurrence contributes the same source weight phi(x). Therefore
  sum_v sum_{f in F_v}phi(x_f)
  <=2 sum_{e ascending}phi(x_e),
which is the final claim.