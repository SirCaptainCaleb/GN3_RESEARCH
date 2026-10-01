# Local one-eighth strict-gap paid mass survives as clean fundamental-cycle chords

## Statement

Let (H_j) satisfy the 43/48 near-extremal hypotheses, write
  S_j = sum_v phi(v),
and assume S_j/n_j^+ -> infinity. For each vertex v let G_v be the paid-certified source-clean, doubly-terminal-single family supplied by e6137a4bc902, and put p_v=phi(v).

Let J_j be the terminal-pair graph consisting of all ascending nonspecial hyperedges that are source-clean on the chosen maximum path at their unique entrance and terminal-single on the chosen maximum endpoint path at both terminals. Weight each edge of J_j by its edge rank, and choose in every component a spanning tree of maximum total edge rank; let F_j be the union of these trees.

Then there are subfamilies H_v subseteq G_v such that
  sum_v (p_v/8-|H_v|)_+ = o(S_j),
and every center-edge incidence (v,e) with e={x,v,u} in H_v simultaneously satisfies:
(1) e carries its paid-cell switching certificate at v and is source-clean and terminal-single at both terminals;
(2) e has strict edge-rank gap at both terminals,
    phi(e)<min{phi(v),phi(u)};
(3) the terminal-pair edge vu is not in F_j, so its fundamental cycle C_e lies entirely in J_j and e has minimum edge rank on C_e;
(4) at each terminal of e, the cycle-neighbor hyperedge has edge rank at least phi(e), and e has an additional blocker contact with every corresponding maximum terminal witness for that neighbor.

Consequently
  sum_v |H_v| >= S_j/8-o(S_j),
and the union of the H_v contains at least
  (1/16-o(1))S_j
distinct hyperedges. Thus almost all of the local one-eighth paid mass can simultaneously be required to have strict rank gap and a canonical clean fundamental-cycle certificate.

## Body

The local stability theorem e6137a4bc902 gives families G_v with
  sum_v (p_v/8-|G_v|)_+ = o(S_j).
The first assertion of 9fba15f1495c says that all but o(S_j) of the center-edge incidences (v,e), e in G_v, already satisfy the strict two-terminal edge-rank gap. Let b_v be the number of incidences deleted from G_v for failing that strict-gap condition. Then
  sum_v b_v=o(S_j).

Now choose the maximum-total-edge-rank forest F_j of the clean graph J_j. A forest on at most n_j^+ nonisolated terminal vertices has fewer than n_j^+ edges. Moreover an ascending nonspecial hyperedge can belong to G_v for at most its two terminal vertices. Hence, if c_v counts the incidences (v,e) with e in G_v whose terminal-pair edge belongs to F_j, then
  sum_v c_v <= 2|E(F_j)| <= 2n_j^+ = o(S_j).

Define H_v by deleting from G_v both the b_v bad strict-gap incidences and the c_v forest incidences. For every v,
  (p_v/8-|H_v|)_+
  <= (p_v/8-|G_v|)_+ + b_v+c_v.
Summing proves
  sum_v (p_v/8-|H_v|)_+ = o(S_j).

Fix e in H_v. Since e is a nonforest edge of J_j, it has a fundamental cycle C_e entirely in J_j. If a tree edge g on C_e had phi(g)<phi(e), replacing g by e would give a spanning tree of the same component with strictly larger total edge rank, contradicting the choice of F_j. Thus every tree edge on C_e has edge rank at least phi(e), and e is a minimum-edge-rank member of C_e.

Let g be either cycle neighbor of e and let w be their common terminal. Then phi(g)>=phi(e). Choose any maximum path witnessing w as a terminal of g. By 94c19ac52776, if e met that path only at w, appending e would force phi(e)>=phi(g)+1, impossible. Therefore e has a second contact with the witness path. The same argument applies at the other terminal. This proves the cycle and blocker assertions while all cycle edges remain in the source-clean, doubly-terminal-single graph J_j.

Finally,
  sum_v |H_v| >= sum_v p_v/8-o(S_j)=S_j/8-o(S_j).
Each underlying ascending nonspecial hyperedge has exactly two terminal vertices and therefore occurs in at most two H_v. Dividing the center-edge incidence count by two gives at least (1/16-o(1))S_j distinct underlying hyperedges.
