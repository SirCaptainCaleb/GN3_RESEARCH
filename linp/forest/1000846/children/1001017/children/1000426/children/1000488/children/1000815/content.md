# Regular path-length fence is a direct test case of the incidence-rank conjecture

## Statement

For a d-regular finite linear 3-graph H, the conjectural statement that H always contains a linear path of length at least d-1 follows immediately from the incidence-rank path conjecture. More sharply, any d-regular H with maximum path length at most d-2 would itself be a counterexample to that incidence-rank conjecture.

## Body

Let H be d-regular on n vertices, with m edges and incidence matrix N. Then 3m=dn, so m=dn/3.

Suppose the maximum linear-path length is L<=d-2, and put ell=L+1. Then H is P_ell-free and ell<=d-1. Since rank_R(N)<=n,
  ell rank_R(N) <= (d-1)n < dn = 3m.
Thus H violates the incidence-rank conjecture 6bea43f4bc16, which predicts ell rank_R(N)>=3m for every P_ell-free linear triple system.

Conversely, applying 6bea43f4bc16 to a d-regular H with first forbidden length ell=L+1 gives
  ell n >= ell rank_R(N) >= 3m = dn,
hence ell>=d and L>=d-1.

Therefore the proposed regular-case path bound is an exact stress test for the algebraic rank route. Endpoint-counting attempts that would prove L>=d-1 in full generality are likely addressing a substantial part of the same obstruction rather than an elementary regularity phenomenon.
