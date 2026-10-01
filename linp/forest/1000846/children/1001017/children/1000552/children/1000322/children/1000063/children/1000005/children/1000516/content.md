# Refuted: maximum-rank nonspecial edge degree conjecture

## Statement

Refuted. A globally maximum-rank nonspecial edge need not contain a vertex of degree at most floor(2(L+1)/3). The certified counterexample bab307b92caa has maximum path length L=5 and maximum-rank nonspecial edges all of whose vertices have degree 5>4.

## Body

This is a sharpened local conjecture motivated by the dense-core all-special threshold. The analogous statement for an arbitrary nonspecial edge is false (fence 439b3c1844c8), but adding the hypothesis that e has globally maximum path rank has survived current testing. If H is P_ell-free then L<=ell-1, so the conjecture gives min_{v in e}d(v)<=floor(2ell/3) for every maximum-rank nonspecial edge. The ell=6 equality obstruction d9ee4adc37d3 has a unique nonspecial edge of global rank L=5 with degree triple (5,4,5), attaining floor(2(L+1)/3)=4. This conjecture alone does not prove the dense-core all-special conjecture, because nonspeciality need not occur at maximum rank.