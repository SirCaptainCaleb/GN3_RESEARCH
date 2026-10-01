# Lens-free strict two-terminal-gap paid family with certificate terminal retained

## Statement

Let (H_j) satisfy
  S_j=sum_v phi(v),  S_j/n_j^+ -> infinity,
  |E(H_j)| >= (43/48)S_j-o(S_j).
Choose the lens-free local families G_v from 7ddb7afd3083.

Then all but o(S_j) of the center-edge incidences (v,f), f in G_v, satisfy strict edge-rank gap at both terminals: if u is the other terminal and q=phi(f), then
  q<phi(v) and q<phi(u).

Consequently there is a set Epp of distinct ascending nonspecial edges with
  |Epp| >= (1/16-o(1))S_j
such that every e={x,u,v} in Epp:
(1) is source-clean on the chosen maximum path at its unique entrance;
(2) is terminal-single on the chosen maximum endpoint paths at both terminals;
(3) satisfies q=phi(e)<min{phi(u),phi(v)};
(4) carries a selected D+Y common-anchor switching certificate at at least one of its terminals.

The certificate terminal in (4) is retained as part of the data and is not asserted to be a minimum-rank terminal of e.

## Body

From 7ddb7afd3083,
  sum_v(p_v/8-|G_v|)_+=o(S),
so
  sum_v|G_v|>=S/8-o(S).                               (1)

Each G_v is supported only at active misaligned centers in the common-anchor construction. Hence for every f in G_v, with q=phi(f),
  q<=q(v)<p_v=phi(v).                                 (2)

Let B be the set of incidences (v,f), f in G_v, for which the other terminal u satisfies
  phi(u)=q.
Map (v,f) to the ordered terminal incidence (f,u). This map is injective: the edge f and terminal u determine the other terminal v.

Every image is a rank-tight ascending nonspecial terminal incidence, so the lens-free flat-incidence theorem 8ac145bb8e95 gives
  |B|<=4 sum_w eta_w+O(n_+)=o(S),                     (3)
using the near-equality defect conclusion in 223efeb00c7b.

For any terminal u of an ascending nonspecial edge f, phi(u)>=phi(f)=q; therefore incidences outside B satisfy phi(u)>q. Together with (2), both terminal vertex ranks strictly exceed q.

By (1) and (3), at least (1/8-o(1))S good center incidences remain. One underlying ascending edge can occur in center-indexed families at at most its two terminal vertices. Quotienting by underlying edges therefore leaves at least
  (1/16-o(1))S
distinct edges.

Source-cleanliness, terminal-singleness, and the selected common-anchor D+Y certificate are inherited from G_v at the original certificate center. No claim is made that this certificate transfers if the edge is subsequently assigned to its minimum-rank terminal.
