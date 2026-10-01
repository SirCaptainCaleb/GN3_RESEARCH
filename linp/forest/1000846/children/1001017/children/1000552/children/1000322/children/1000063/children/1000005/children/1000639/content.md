# Low-degree endpoint in the fixed-edge rotation closure

## Statement

Let H be a finite linear 3-graph with global maximum path length L. Let e be a nonspecial edge with phi(e)=L and unique entrance x. Fix a globally longest path P ending in e through x, and let R(P,e,x) be the set of vertices that occur as an opposite last vertex of some globally longest path obtained from P by a sequence of length-preserving rotations that keep e as the last edge and keep x as its entrance. Then min_{v in R(P,e,x)} d_H(v) <= floor(2(L+1)/3).

## Body

This is the rotation-closure replacement for the refuted single-path opposite-end degree conjecture. Certified single-blocker rotations show that every opposite-end single blocker gives a transition inside R(P,e,x). The known counterexamples to the single-path bound have low ambient minimum degree and therefore do not refute this closure statement. If true, then any linear 3-graph of minimum degree delta containing a maximum-rank nonspecial edge satisfies delta<=floor(2(L+1)/3), hence 3delta<=2L+2. The remaining obstruction is the double-blocker regime: a high-degree reachable endpoint may have most incident edges double-blocking, so a proof must either extract length-preserving double-blocker rotations/splices or use minimum degree at the blocker vertices to force expansion of the closure.