# Every q-step flat transfer walk contains a labeled linear cycle

## Statement

Let H be a linear 3-graph and fix q. Any walk of q consecutive flat equal-rank-q ascending transfers contains, among its transfer hyperedges, a linear cycle of length at most q. The cycle is of one of the two types in f7c3ab40c059: either a terminal-cycle whose entrance labels are pairwise distinct private vertices, or a color-closure cycle with one low-potential entrance joint and all remaining joints terminal.

## Body

All rank-q ascending transfer edges lie in the threshold graph R_q: their entrance colors have potential q-1<q and their terminal vertices have potential at least q. If during the first q transfer edges a terminal vertex or entrance color repeats, f7c3ab40c059 gives the asserted labeled linear cycle. If neither repeats, the q terminal-pair edges form a simple rainbow q-edge path in R_q, contradicting the certified theorem 1f65fa538544 that R_q has no rainbow P_q.
