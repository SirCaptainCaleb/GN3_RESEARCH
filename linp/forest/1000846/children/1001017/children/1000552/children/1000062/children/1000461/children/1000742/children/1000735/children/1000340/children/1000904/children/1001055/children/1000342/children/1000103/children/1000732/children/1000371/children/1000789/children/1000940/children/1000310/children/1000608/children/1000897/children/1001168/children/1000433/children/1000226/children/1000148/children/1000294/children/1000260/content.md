# Triangle collisions force distinct host edges at half the owner edge rank

## Statement

Retain the family T and host edges g_j from 3f165c52a1a6. Suppose every colliding owner E_i in T has edge rank at least R.

Then T contains a subfamily T' of size at least ceil(|T|/2) such that:
(1) the distinguished parent-edge pairs are pairwise disjoint;
(2) every fixed host hyperedge occurs for at most four members of T';
(3) every host hyperedge g_j has edge rank at least ceil(R/2).

Consequently T produces at least
  ceil(ceil(|T|/2)/4)
distinct hyperedges of edge rank at least ceil(R/2).

## Body

Choose T' as in 3f165c52a1a6; only the edge-rank assertion remains.

For a collision with owner rank r_i, its chosen maximum path R_i has
  p=r_i-1
edges. Let the triangle host g_j be the t-th edge of R_i.

The prefix of R_i through g_j is a t-edge linear path whose last edge is g_j, so
  phi(g_j)>=t.
Reversing the suffix from g_j to the last edge of R_i gives a
  p-t+1
edge linear path whose last edge is again g_j, so
  phi(g_j)>=p-t+1=r_i-t.

Therefore
  phi(g_j)>=max{t,r_i-t}>=ceil(r_i/2)>=ceil(R/2).
The distinct-host count is exactly the bound from 3f165c52a1a6.
