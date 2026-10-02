# Top-rank rotation outputs split into special, flat-oriented, or top-joint states

## Statement

Let L be the global maximum path length, let P=(g_1,...,g_L) be a maximum L-edge path, and suppose an occupied single-blocker cell C_i produces the rotation
  g_1,...,g_i,f,g_L,g_{L-1},...,g_{i+2}
with i<=L-3. Then phi(g_{i+2})=L. Put
  z_{i+2}=g_{i+2}∩g_{i+3},
the forward joint of g_{i+2} on the original host path.

Exactly one of the following holds:
1. g_{i+2} is special;
2. g_{i+2} is nonspecial ascending, its unique entrance is z_{i+2}, and phi(z_{i+2})=L-1;
3. g_{i+2} is nonspecial nonascending, its unique entrance is z_{i+2}, and phi(z_{i+2})=L.

Consequently, at a low-defect global-top center v with phi(v)=L, the linear packet of rank-L host edges from 68906f1d55c3 decomposes into special edges, forward-oriented flat ascending top-rank edges, and edges whose forward joints are distinct top-potential vertices.

## Body

The rotated path has L edges and last edge g_{i+2}; since L is the global maximum path length,
  phi(g_{i+2})=L.                                     (1)

In the displayed rotated path, the edge immediately preceding g_{i+2} is g_{i+3}. Hence the path enters g_{i+2} through
  z_{i+2}=g_{i+2}∩g_{i+3}.                            (2)

If g_{i+2} is special there is nothing to prove. Suppose it is nonspecial. By the unique-longest-entrance characterization, every longest path ending in g_{i+2} enters through its unique entrance. The displayed rotation is a longest L-edge path by (1), so (2) forces z_{i+2} to be that unique entrance.

The first L-1 edges of the rotated path form an (L-1)-edge path ending at z_{i+2} with z_{i+2} as a last vertex, so
  phi(z_{i+2})>=L-1.                                  (3)
By global maximality of L, phi(z_{i+2})<=L. Therefore
  phi(z_{i+2}) in {L-1,L}.                            (4)

If phi(z_{i+2})=L-1, then
  phi(g_{i+2})=phi(z_{i+2})+1,
so the nonspecial edge is ascending. If phi(z_{i+2})=L, it is nonascending. This gives the trichotomy.

Finally, distinct output edges g_j have distinct forward joints z_j along the linear host path. Combining with 68906f1d55c3 gives the stated packet decomposition at a global-top center.