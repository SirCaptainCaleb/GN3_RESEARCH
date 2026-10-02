# Switching rotations force a linear packet of high-rank host edges

## Statement

In the setting of 465568d6d8dc, every occupied interior blocker cell C_i forces the host edge g_{i+2} to satisfy phi(g_{i+2})>=p. Distinct occupied cells give distinct such edges. Hence if F is a single-blocker family on a maximum p-path, then at least
  |F|/2-O(1)
distinct path edges have edge rank at least p.

For a low-defect active misaligned center v with phi(v)=p and switching family F_v from b032348c1a8a,
  #{g in E(P_v): phi(g)>=p}
  >= (5/16)p-(1/2)eta_v-O(1).
Thus eta_v=o(p) forces (5/16-o(1))p rank-at-least-p edges on the chosen maximum path. If p is the global maximum path length, these are all globally top-rank edges.

## Body

Let C_i be an occupied interior blocker cell. The rotation constructed in 465568d6d8dc is a p-edge linear path whose last edge is g_{i+2}. By definition of edge rank, the existence of a p-edge path ending in g_{i+2} implies
  phi(g_{i+2})>=p.
Different cell indices i give different path edges g_{i+2}. Since every cell contains at most two contact vertices and distinct blockers through v have distinct precursor contacts, a blocker family F occupies at least |F|/2-O(1) interior cells. This proves the first assertion.

For a switching family at an active misaligned center, b032348c1a8a gives
  |F_v| >= (5/8)p-eta_v-O(1).
Substitution yields
  #{g in E(P_v):phi(g)>=p}
  >= |F_v|/2-O(1)
  >= (5/16)p-(1/2)eta_v-O(1).
If p equals the global maximum possible edge/path rank, every edge counted above has rank exactly p.