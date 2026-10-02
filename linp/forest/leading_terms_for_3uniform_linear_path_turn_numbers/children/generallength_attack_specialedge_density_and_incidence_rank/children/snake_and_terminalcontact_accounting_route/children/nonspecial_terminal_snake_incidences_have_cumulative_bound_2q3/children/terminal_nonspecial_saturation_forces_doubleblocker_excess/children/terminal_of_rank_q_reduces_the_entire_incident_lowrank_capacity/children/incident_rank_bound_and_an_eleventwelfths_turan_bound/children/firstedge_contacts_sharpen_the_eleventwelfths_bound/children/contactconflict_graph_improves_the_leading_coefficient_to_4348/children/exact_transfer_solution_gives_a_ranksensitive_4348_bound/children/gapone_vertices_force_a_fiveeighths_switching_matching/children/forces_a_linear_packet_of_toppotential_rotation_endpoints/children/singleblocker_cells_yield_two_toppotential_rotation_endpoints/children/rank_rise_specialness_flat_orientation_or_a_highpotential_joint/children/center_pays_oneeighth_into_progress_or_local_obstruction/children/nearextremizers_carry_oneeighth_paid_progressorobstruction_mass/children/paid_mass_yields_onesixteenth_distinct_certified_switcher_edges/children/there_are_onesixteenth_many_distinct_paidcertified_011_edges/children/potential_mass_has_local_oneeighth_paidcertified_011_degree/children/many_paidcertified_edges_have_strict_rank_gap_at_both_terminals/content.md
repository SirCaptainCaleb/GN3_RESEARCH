# Near 43/48, linearly many paid-certified edges have strict rank gap at both terminals

## Statement

Let (H_j) satisfy the 43/48 near-extremal hypotheses, with S_j=sum_v phi(v) and S_j/n_j^+ -> infinity. Choose the families G_v from e6137a4bc902. Then all but o(S_j) of the center-edge incidences (v,f) with f in G_v have the following property: if u is the other terminal of f, then phi(f)<phi(v) and phi(f)<phi(u). Consequently there is a set Epp of distinct ascending nonspecial edges with |Epp| >= (1/16-o(1))S_j such that for every e={x,u,v} in Epp, both terminal vertex ranks strictly exceed the edge rank: min{phi(u),phi(v)} >= phi(e)+1. Every edge in Epp remains source-clean, terminal-single at both terminals, and paid-certified at at least one terminal.

## Body

Write p_v=phi(v). By e6137a4bc902,
  sum_v (p_v/8-|G_v|)_+ = o(S_j).
Hence
  sum_v |G_v| >= S_j/8-o(S_j).                                      (1)

By construction in e6137a4bc902, G_v is nonempty only on the active misaligned centers from the switching-family construction. Thus if f is in G_v and q=phi(f), then
  q <= q(v) < p_v=phi(v).                                            (2)

Let B be the set of incidences (v,f), f in G_v, for which the other terminal u of f satisfies phi(u)=q. Map such an incidence to the ordered terminal incidence (f,u). This map is injective: an ascending nonspecial edge has exactly two terminals, so from (f,u) the other terminal v is determined.

Every image pair (f,u) is an ascending nonspecial terminal incidence satisfying phi(f)=phi(u). Therefore the global flat-incidence estimate 619d7583671c applies. It gives
  |B| <= 4 sum_w eta_w + O(n_j^+) = o(S_j),                           (3)
because d287da5967d5 gives sum_w eta_w=o(S_j) and n_j^+=o(S_j).

Combining (1) and (3), at least (1/8-o(1))S_j incidences (v,f) in the chosen families satisfy phi(u)>q. Together with (2), both terminals of every such incidence have vertex rank strictly larger than q.

Finally, one underlying ascending edge can occur in G_v for at most its two terminal vertices. Quotienting the good incidences by the underlying edge therefore loses a factor of at most two, leaving at least (1/16-o(1))S_j distinct edges with strict rank gap at both terminals. All source-clean, terminal-single, and paid-certificate properties are inherited from the defining G_v family.