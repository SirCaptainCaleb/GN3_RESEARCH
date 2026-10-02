# Original-hypergraph density-core minimum-degree reduction

## Statement

Let H be a nonempty finite 3-uniform hypergraph with n vertices and m>0 edges. There is a nonempty vertex-induced subhypergraph H0 such that |E(H0)|/|V(H0)| >= m/n and delta(H0) >= |E(H0)|/|V(H0)|. In particular, for a linear P_ell-free H, H0 remains linear and P_ell-free.

## Body

Proof. Choose a nonempty vertex set S maximizing rho(S)=|E(H[S])|/|S|, and put H0=H[S], with n0=|S| and m0=|E(H0)|. Then m0/n0>=m/n. If some v in S had d_H0(v)<m0/n0, deleting v would leave m0-d_H0(v) edges on n0-1 vertices, and (m0-d_H0(v))/(n0-1)>m0/n0, contradicting maximality. Thus delta(H0)>=m0/n0. Vertex deletion preserves linearity and P_ell-freeness.