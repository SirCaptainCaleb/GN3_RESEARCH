# Three-quarters potential-oriented local bound gives Astra 11/12 coefficient

## Statement

For every vertex v with p=phi(v), at most floor(3p/4) ascending nonspecial edges e={x,v,u} have v terminal and phi(u)>=p. This implies A<=3/4 sum_v phi(v) by assigning each ascending terminal pair to its lower-potential endpoint, hence m<=11/12 sum_v phi(v)-n/3 and m<=((11ell-15)/12)n for P_ell-free systems. The target is already established at p=2,3 and p=4; p=5 is exactly the current four-charged-edge elimination problem.

## Body

Let H be a finite linear 3-graph. For a vertex v with p=phi(v), let c_+(v) denote the number of ascending nonspecial edges e={x,v,u} such that v is a terminal of e and phi(u)>=p.

Conjectural local inequality:
  c_+(v) <= floor(3p/4).                              (1)

This is exactly sufficient for Astra's interrupted weighted ascending-edge bound. For every ascending edge with terminal pair {u,v}, orient/assign the edge to a terminal of smaller endpoint potential, breaking ties arbitrarily. If it is assigned to v, then the opposite terminal has potential at least phi(v), so it is counted by c_+(v). Every ascending edge is assigned exactly once. Hence (1) implies
  A <= sum_v c_+(v)
    <= sum_v floor(3phi(v)/4)
    <= (3/4)sum_v phi(v).                            (2)

Combining (2) with certified 419519f0efa5,
  3m-A <= 2 sum_v phi(v)-n,
gives
  m <= (11/12)sum_v phi(v)-n/3,
and in a P_ell-free system,
  m <= ((11ell-15)/12)n.

The small potentials align with the exact coefficient:
- p=2: every charged ascending terminal edge has rank 2. The q=2 nonspecial terminal capacity gives c_+(v)<=1=floor(6/4).
- p=3: every charged edge has rank 3. The stronger rank-three low-rank incident/terminal capacity gives c_+(v)<=2=floor(9/4).
- p=4: a34f823e8f22 proves c_+(v)<=3=floor(12/4).
- p=5: (1) again asks c_+(v)<=3. This is exactly the live p=5 charged four-edge elimination program (4445,4455,4555,5555) that Astra was inspecting immediately before reporting the 11/12 route.
- p>=6: the target relaxes linearly, allowing floor(3p/4) charged edges. This is consistent with Astra's remark that linearly many disjoint pairs of nearby path positions each create one unit of deficit.

Thus the interrupted 11/12 argument is most naturally reconstructed as the floor-three-quarters potential-oriented local bound (1), not the much stronger old conjecture c_+(v)<=3 for all p.

Known fences to respect: unrestricted common-terminal ascending degree is unbounded, but those examples are downhill in terminal potential; consecutive arbitrary private single blockers can coexist (2712f65b5d5e), so the large-p pairing proof must use the potential-charged/ascending/clean structure.
