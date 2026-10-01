# Every universal-star maximum path omits a large higher-potential terminal packet

## Statement

Let v be pair-universal and P a maximum p=phi(v)-edge path ending at v. Then the clean-star count satisfies B_0>=d_H(v)-2p+1, because the final path edge itself contributes to B_2. Every B_0 edge is an ascending nonspecial source edge at v whose two terminals lie outside P. Hence P omits at least 2(d_H(v)-2p+1) vertices of potential at least p+1. In the s=2 equality layer with p=ell-2 this gives 12, 8, or 10 omitted top-potential vertices by residue.

## Body

In the notation of d8167d92002d, the last path edge g_p is itself an edge through the pair-universal vertex v. Its two vertices other than v both lie in V(P)\{v}. Hence its star pair is counted by B_2, so
  B_2>=1.

The exact identity
  B_0-B_2=d_H(v)-2phi(v)
therefore gives
  B_0>=d_H(v)-2phi(v)+1.                            (1)

Every B_0 edge is, by d8167d92002d, an ascending nonspecial edge of rank phi(v)+1 with unique entrance v, and its two terminal vertices both lie outside V(P). Distinct B_0 edges have disjoint terminal pairs by linearity.

Hence every maximum p=phi(v)-edge path ending at a pair-universal v omits at least
  2[d_H(v)-2p+1]
vertices that occur as terminals of clean ascending source edges from v. Each such terminal has endpoint potential at least p+1.

In the equality s=2 setting, d_H(v)=3d+1. If p=ell-2, then the number of clean source edges is at least
  3d+1-2(ell-2)+1
  =3d-2ell+6,
namely 6,4,5 for ell congruent to 0,1,2 modulo 3. Thus every maximum v-ending path omits at least 12,8,10 vertices respectively, all of endpoint potential ell-1.
