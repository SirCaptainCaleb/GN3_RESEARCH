# Two forward crossings and one reciprocal crossing force a three-edge forest exchange

## Statement

Let J=R_1|R_2|R_3 be a spanning three-path cover of a vertex set W, and let T be a spanning two-path cover of W. Assume that within each T-component the vertices inherited from each R_i occur in the displayed relative order. Let t be the number of ordinary T-edges joining different R_i classes, and let s be the number of ordinary J-edges whose endpoints lie in different T-components. If t=2 and s=1, then T is obtained from J by deleting exactly the unique reciprocal-crossing inherited edge e and adding exactly the two cross-class T-edges. Equivalently, every same-class ordinary edge of T is an ordinary edge of J, and the symmetric difference of the two ordinary path forests has exactly three edges: two in T-J and one in J-T.

## Body

Every cross-class T-edge is absent from J, so t=2 contributes two edges to T-J. Suppose T had any additional edge f in T-J with both endpoints in one inherited class R_i. Since relative order is preserved, f joins r_p to r_q with q>=p+2 in the displayed R_i order. By shortcut_forces_two_recip, this would force at least two inherited J-edges to cross the T support partition, contradicting s=1. Hence T-J consists exactly of the two cross-class edges, so |T-J|=2. On |W| vertices, J has |W|-3 ordinary edges and T has |W|-2, hence |T-J|-|J-T|=1. Therefore |J-T|=1. Every inherited J-edge crossing the T support partition is certainly absent from T, so the unique such edge e belongs to J-T. Since J-T has size one, J-T={e}. Thus the forest exchange is exactly one old edge out and two cross-class edges in.
