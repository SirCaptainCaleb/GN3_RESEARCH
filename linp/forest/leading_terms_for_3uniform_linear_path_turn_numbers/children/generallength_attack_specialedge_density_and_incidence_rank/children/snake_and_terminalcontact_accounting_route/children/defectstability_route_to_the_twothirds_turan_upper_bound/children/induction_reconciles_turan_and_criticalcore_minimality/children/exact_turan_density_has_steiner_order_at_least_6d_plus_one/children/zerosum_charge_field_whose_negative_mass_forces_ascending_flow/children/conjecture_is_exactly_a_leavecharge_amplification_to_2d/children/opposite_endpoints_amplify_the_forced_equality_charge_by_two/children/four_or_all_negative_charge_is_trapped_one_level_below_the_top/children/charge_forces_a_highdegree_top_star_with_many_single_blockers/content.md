# Trapped-negative charge forces a high-degree top star with many single blockers

## Statement

In the exceptional trapped-negative two-layer charge state, put a=kappa+2, N={v:k_v<0}, R=sum_{v in N}(-k_v), and let G be the properly edge-colored top-layer terminal graph with support S.

(i) Every u in S has k_u>=a, hence R>=a|S|.
(ii) For each v in N of negative mass r=-k_v, r<=R/(2a)-a; consequently |N|>=2a+1=2kappa+5.
(iii) The graph G has average degree greater than 2a, so some top-layer vertex u has d_G(u)>=2a+1=2kappa+5. Its incident G-edges come from distinct negative source colors and rank-(ell-1) ascending nonspecial hyperedges.
(iv) If additionally max_w k_w<=kappa+3, then for any G-edge h at such a vertex u and any longest p=(ell-1)-edge path P ending in h with last vertex u, the number B_P(u) of other incident terminal edges double-blocking P is at most 3. Hence at least 2kappa+1 other incident G-edges are full-rank equal-potential single blockers of P.

## Body

A used top-layer vertex u is terminal on a rank-(ell-1) nonspecial edge. The incident low-rank capacity bound gives d_H(u)<=2ell-5, hence k_u=3d-d_H(u)>=kappa+2=a. Summing positive charge over S yields R>=a|S|.

For a negative source v of mass r, its color class in G is a matching of size at least a+r, so |S|>=2(a+r). Together with |S|<=R/a this gives r<=R/(2a)-a. Summing over v in N rules out |N|<=2a, hence |N|>=2a+1.

Summing the color-class sizes gives |E(G)|>=a|N|+R. With |S|<=R/a,
2|E(G)|/|S| >= 2a+2a^2|N|/R >2a,
so some u has degree at least 2a+1. Proper coloring makes the corresponding source colors distinct.

Finally assume max_w k_w<=kappa+3. For a longest p-edge path P ending at u, the exact terminal-degree/double-blocker inequality gives d_H(u)+B_P(u)<=2p-1=2ell-3. Since d_H(u)=3d-k_u and 2ell-3=3d-kappa, B_P(u)<=k_u-kappa<=3. Every other incident G-edge must meet P away from u; at most three can double-block, so at least d_G(u)-1-3>=2kappa+1 are single blockers.