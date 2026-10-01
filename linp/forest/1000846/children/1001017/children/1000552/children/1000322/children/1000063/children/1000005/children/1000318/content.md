# Local degree bound on a nonspecial edge is false

## Statement

It is false that every nonspecial edge e must contain a vertex of degree at most floor(2(phi(e)+1)/3).

## Body

Counterexample: the linear triple system with edges (2,4,7),(0,2,6),(0,4,8),(0,1,7),(1,4,6),(3,5,9),(1,2,8),(3,6,7),(5,6,8). The edges (0,2,6) and (1,4,6) are nonspecial with phi(e)=3, but their degree triples are respectively (3,3,4) and (3,3,4). Hence min_{v in e} d(v)=3>floor(2(3+1)/3)=2. This rules out a proof of the dense-core all-special conjecture based only on a per-edge bound in terms of phi(e); surrounding low-degree vertices elsewhere in the component matter, so the minimum-degree/core hypothesis must be used globally.
