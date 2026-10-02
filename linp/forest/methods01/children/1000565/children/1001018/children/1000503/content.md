# Lens-free selected strict-gap mass survives as clean fundamental-cycle chords

## Statement

Let (H_j) satisfy
  S_j=sum_v phi(v),  S_j/n_j^+ -> infinity,
  |E(H_j)| >= (43/48)S_j-o(S_j),
and let G_v be the lens-free selected common-anchor families from 7ddb7afd3083.

Form the terminal-pair graph J_j consisting of all ascending nonspecial hyperedges that are source-clean on the chosen maximum path at their unique entrance and terminal-single on the chosen maximum endpoint paths at both terminals. Weight each graph edge by the rank of its parent hyperedge, and in every component choose a spanning tree of maximum total rank; let F_j be the resulting forest.

Then there are subfamilies H_v subseteq G_v such that
  sum_v (phi(v)/8-|H_v|)_+ = o(S_j),
and every center-edge incidence (v,e), e={x,v,u} in H_v, satisfies simultaneously:

(1) e retains its selected D+Y common-anchor certificate at v;
(2) e is source-clean and terminal-single at both terminals;
(3) phi(e)<min{phi(v),phi(u)};
(4) vu is not a forest edge, so its fundamental cycle C_e lies entirely in J_j;
(5) e is minimum-rank on C_e; in particular its two cycle-neighbor hyperedges have rank at least phi(e), and e has the canonical additional blocker contact on maximum terminal witnesses for those two neighbors.

Consequently
  sum_v |H_v| >= S_j/8-o(S_j),
and the union of the H_v contains at least
  (1/16-o(1))S_j
distinct underlying hyperedges.

Thus the full local one-eighth lens-free selected strict-gap mass can be retained while adding a canonical clean-U11 fundamental-cycle certificate.

## Body

From e2dcd798f528, all but o(S_j) center-edge incidences (v,e), e in G_v, satisfy strict edge-rank gap at both terminals. Let b_v count the incidences deleted for failing this condition. Then
  sum_v b_v=o(S_j).                                     (1)

The graph J_j contains every edge of every G_v, because 7ddb7afd3083 gives source-cleanliness and terminal-singleness at both terminals. A spanning forest of J_j has fewer than n_j^+ edges. Since an ascending nonspecial hyperedge has exactly two terminal vertices, one underlying forest edge can occur in center-indexed families G_v for at most two centers. If c_v counts incidences (v,e) with e in G_v whose terminal-pair edge belongs to F_j, then
  sum_v c_v <= 2|E(F_j)| <= 2n_j^+ = o(S_j),            (2)
using S_j/n_j^+ -> infinity.

Define H_v by deleting from G_v the b_v strict-gap failures and the c_v forest incidences. Since 7ddb7afd3083 gives
  sum_v (phi(v)/8-|G_v|)_+=o(S_j),
we have pointwise
  (phi(v)/8-|H_v|)_+
  <= (phi(v)/8-|G_v|)_+ + b_v+c_v.
Summing and using (1),(2) proves
  sum_v (phi(v)/8-|H_v|)_+=o(S_j).                      (3)

Fix e in H_v. Its terminal-pair edge is nonforest in J_j, so it has a fundamental cycle C_e entirely in J_j. By maximality of the total forest rank, if a tree edge g on C_e had phi(g)<phi(e), replacing g by e would increase the total forest rank. Therefore every tree edge on C_e has rank at least phi(e), and e is minimum-rank on C_e.

Let g be either cycle neighbor of e, sharing terminal w with e. Both parent hyperedges are nonspecial and terminal at w, and phi(g)>=phi(e). The terminal-adjacency blocker argument used in ad344ad2a913 applies inside J_j: if e met a maximum witness for g only at w, appending e would force phi(e)>=phi(g)+1, impossible. Hence e has an additional contact with that witness. This holds independently at both terminal sides.

All properties (1)-(3) are inherited from G_v and the strict-gap deletion.

Finally (3) implies
  sum_v|H_v|>=S_j/8-o(S_j).
Each underlying ascending nonspecial edge has exactly two terminal vertices, so it can occur in at most two center-indexed H_v. Dividing by two yields at least
  (1/16-o(1))S_j
distinct underlying edges.

No endpoint-lens assertion is used.