# Devine–Milans general linear-path upper bound

## Statement

For all r>=2 and ell>=2, ex_L(n,P_ell^(r)) <= (ell - 2 + 1/(r-1)) n. In particular, ex_L(n,P_ell^(3)) <= (ell - 3/2)n.

## Body

Ported from the supplied current source linear_paths.tex. Let G have m edges and no P_ell^(r), and let D be its snake digraph. Reordering the final r-1 vertices of a longest path ending in an edge e shows that every edge contributes at least r-1 incidences to D, so |E(D)| >= (r-1)m. Hence some z has d_D^-(z) >= (r-1)m/n. Applying the snake indegree lemma and phi(z)<=ell-1 gives d_D^-(z) <= (ell-2)(r-1)+1. Combining yields m <= (ell-2+1/(r-1))n. For r=3 this is (ell-3/2)n.