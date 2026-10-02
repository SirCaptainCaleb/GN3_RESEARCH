# Shared entrances on one higher-rank source path force quadratic edge-rank mass

## Statement


Let
  e_1,...,e_M
be distinct ascending nonspecial edges with unique entrances
  x_1,...,x_M
and edge ranks
  r_1<=...<=r_M.
Let A be a canonical maximum source path for another ascending edge of edge rank Q, so A has Q-1 edges. Assume every x_j lies on A and every r_j<=Q.

Then for each j=1,...,M,
  r_j >= ceil((2Q+j+1)/4).

Consequently
  sum_{j=1}^M r_j
  >= (MQ)/2 + M(M+3)/8.

Equivalently, relative to the baseline Q/2 per edge, M distinct entrance labels lying on one Q-source path force a quadratic rank-mass bonus of at least M(M+3)/8.


## Body


Each entrance x_j has vertex rank
  phi(x_j)=r_j-1.
Fix j. Among x_1,...,x_j, all j vertices have vertex rank at most r_j-1.

If r_j<Q, apply 5cee9bfe483f to the (Q-1)-edge path A with cutoff R=r_j-1. It gives
  j <= 4(r_j-1)-2(Q-1)+1
    = 4r_j-2Q-1.
Thus
  r_j >= ceil((2Q+j+1)/4).

If r_j=Q, the same displayed lower bound is automatic. Indeed A has 2Q-1 vertices, so M<=2Q-1 and hence j+1<=2Q, which gives
  (2Q+j+1)/4<=Q.

Summing the pointwise lower bounds and dropping ceilings,
  sum_j r_j
  >= sum_j (2Q+j+1)/4
  = MQ/2 + (M(M+1)/2+M)/4
  = MQ/2 + M(M+3)/8.
