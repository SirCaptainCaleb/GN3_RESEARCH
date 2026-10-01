# Paid 0-1-1 edges are overwhelmingly canonical terminal-cycle chords

## Statement

Let (H_j) satisfy the 43/48 near-extremal hypotheses, with S_j=sum_v phi(v) and S_j/n_j^+ -> infinity. Let T_j be the terminal-pair graph of all nonspecial hyperedges, weighted by hyperedge rank, and choose a spanning forest F_j of T_j of maximum total rank.

Then there is a set E_cyc of distinct ascending nonspecial hyperedges with
  |E_cyc| >= (1/16-o(1))S_j
such that every e in E_cyc simultaneously:
(1) is source-clean on the chosen maximum path at its unique entrance;
(2) is terminal-single on the chosen maximum endpoint path at each terminal (hence lies in U_11);
(3) carries a paid-cell switching certificate at at least one terminal;
(4) its terminal-pair edge is not in F_j, so it is a minimum-rank edge on its canonical fundamental cycle C_e in T_j;
(5) the two cycle-neighbor hyperedges at the two terminal endpoints of e have rank at least phi(e), and e satisfies the canonical two-sided blocker obligations supplied by the maximum-rank-forest theorem.

Thus near 43/48, a linear-sized distinct family carries both the paid 0-1-1 local certificate and a canonical global terminal-cycle certificate.

## Body

By 7ac951de82f4 there is a set E_paid of distinct ascending nonspecial hyperedges with
  |E_paid| >= (1/16-o(1))S_j
having properties (1)--(3).

Choose a maximum-total-rank spanning forest F_j of the full nonspecial terminal-pair graph T_j. A forest on at most n_j^+ nonisolated vertices has fewer than n_j^+ edges. Hence
  |E_paid intersect E(F_j)| <= n_j^+ = o(S_j).
Delete these forest edges and put
  E_cyc=E_paid minus E(F_j).
Then
  |E_cyc| >= (1/16-o(1))S_j,
and properties (1)--(3) are preserved.

For every e in E_cyc, its terminal-pair edge is a nonforest edge of F_j. The certified maximum-rank-forest theorem ad344ad2a913 therefore gives a canonical fundamental cycle C_e on which e has minimum hyperedge rank. In particular each of the two tree edges adjacent to e on C_e corresponds to a nonspecial hyperedge of rank at least phi(e), and the same theorem supplies the blocker obligation at each terminal side: e must make the required additional contact with the relevant longest-path witness for the adjacent cycle edge.

This is exactly (4)--(5). No multiplicity issue remains because E_cyc consists of distinct underlying hyperedges.