# Edge-transitive Steiner systems have a sharp deletion barrier

## Statement

Let S be an edge-transitive Steiner triple system on v=2ell+1 vertices. If S contains one spanning linear path P_ell, then every block set meeting every spanning P_ell has size at least v/3. Consequently no deletion from a Hamiltonian edge-transitive STS can produce a P_ell-free component whose density exceeds the generic (ell-1)/3 benchmark.

## Body


Let m=|E(S)|=v(v-1)/6=ell*v/3. Fix one spanning linear path P with ell blocks and let Gamma be an edge-transitive subgroup of Aut(S). Choose gamma uniformly from Gamma. Then gamma(P) is again a spanning linear path.

For a fixed block e, edge transitivity makes Pr[e in gamma(P)] independent of e. Summing over the m blocks,
  m Pr[e in gamma(P)] = E|E(gamma(P))| = ell,
so Pr[e in gamma(P)]=ell/m=3/v.

If D meets every spanning path, then gamma(P) meets D for every gamma. Therefore
  1 <= E|D intersect E(gamma(P))|
    = sum_{e in D} Pr[e in gamma(P)]
    = 3|D|/v.
Hence |D|>=v/3.

Deleting D leaves at most
  ell*v/3 - v/3 = (ell-1)v/3
blocks. Thus the only way an edge-transitive STS(2ell+1) can improve the generic lower benchmark is to be intrinsically P_ell-free; once it has one spanning path, sparse surgery cannot rescue it.

For PG(4,2), the explicit spanning P_15 in 7faba12a7542 and edge transitivity imply that at least ceil(31/3)=11 blocks must be deleted to destroy all spanning P_15. An improvement over the generic 14/3 density on 31 vertices would require deleting at most 10, so deletion-based modifications of PG(4,2) cannot improve the P_15 lower bound.
 