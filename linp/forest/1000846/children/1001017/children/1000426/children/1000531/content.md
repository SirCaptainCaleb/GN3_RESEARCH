# Maximum-degree range of the incidence-rank path inequality

## Statement

Let H be a finite linear 3-uniform hypergraph with m edges, incidence matrix N, and maximum degree Delta. For every real L>=Delta+2, one has L rank_R(N)>=3m. Consequently m<=L|V(H)|/3. In particular, if H is P_ell^(3)-free and Delta(H)<=ell-2, then ell rank_R(N)>=3m and hence |E(H)|<=ell|V(H)|/3. Thus every counterexample to the conjectural sharp incidence-rank inequality at length ell must satisfy Delta(H)>=ell-1.

## Body

Let Delta=Delta(H), and fix L>=Delta+2. If m=0 there is nothing to prove. Put
  t=2/(L-Delta).
Then 0<t<=1. Assign the constant weight w_e=t to every edge.

In the notation of the weighted incidence-rank inequality f943915ca731,
  W=sum_e w_e=tm
and, for every vertex v,
  d_w(v)=t d_H(v)<=t Delta.
Thus we may take
  D=t Delta.
By the definition of t,
  D+2=t Delta+2
      =2Delta/(L-Delta)+2
      =2L/(L-Delta)
      =tL.
Applying f943915ca731 gives
  rank_R(N) >= 3W/(D+2)
            = 3tm/(tL)
            = 3m/L.
Equivalently,
  L rank_R(N)>=3m.

Since rank_R(N)<=|V(H)|, also
  m<=L|V(H)|/3.

Taking L=ell, the hypothesis Delta(H)<=ell-2 gives the desired specialization
  ell rank_R(N)>=3m,
which is exactly the incidence-rank path conjecture 6bea43f4bc16 in this maximum-degree range. Therefore any counterexample to that conjecture must have Delta(H)>=ell-1.

No P_ell-freeness is used in the algebraic inequality itself; it enters only when L is interpreted as the forbidden path length ell.
