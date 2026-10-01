# Bounded matching number gives only a one-quarter path lower coefficient

## Statement

Hou, Yu, Gao and Liu determined asymptotically/exactly for sufficiently large n the maximum number of edges in a 3-uniform hypergraph with bounded codegree and matching number. Specializing their theorem to codegree at most one: for fixed positive integer nu and sufficiently large n, every n-vertex linear 3-graph H with matching number at most nu satisfies |E(H)| <= (nu/2)n+O(nu^2), with the exact bound given by their function f(n,nu,1). Consequently, any P_ell-free construction certified solely by nu(H)<=ceil(ell/2)-1 has |E(H)| <= ((ceil(ell/2)-1)/2)n+O(ell^2) = (ell/4+O(1))n+O(ell^2), and therefore cannot improve the one-third leading lower coefficient.

## Body


Source: Xinmin Hou, Lei Yu, Jun Gao, Boyuan Liu, "The size of 3-uniform hypergraphs with given matching number and codegree", arXiv:1709.07208 (2017).

Their Theorem 2 states: for fixed positive integers Delta_2 and nu, and sufficiently large n, if a 3-uniform hypergraph H has maximum codegree at most Delta_2 and matching number at most nu, then
  e(H) <= f(n,nu,Delta_2),
with equality attainable. Their displayed definition is
  f(n,nu,Delta_2)
   = floor(nu(n-nu)Delta_2/2)
     + g(nu,Delta_2,s),
where the final parameter s is either 0 or floor(nu/2), depending on parity. For fixed nu, g(nu,1,s)=O(nu^2). Hence for Delta_2=1,
  e(H) <= (nu/2)n+O(nu^2).

A linear 3-graph has maximum codegree at most one. Also every linear path P_ell contains a matching of ceil(ell/2) hyperedges, namely its odd-indexed edges. Thus imposing
  nu(H) <= ceil(ell/2)-1
is a sufficient certificate for P_ell-freeness. Put
  q=ceil(ell/2)-1.
The theorem gives, for sufficiently large n at each fixed ell,
  e(H) <= (q/2)n+O(q^2)
        <= (ell/4)n+O(n)+O(ell^2),
with the exact linear coefficient equal to (ceil(ell/2)-1)/2.

Therefore bounded matching number cannot support a lower construction with leading coefficient above one third; in fact its natural ceiling is one quarter. This applies without requiring a small transversal, high maximum degree, regularity, or any particular construction architecture.
