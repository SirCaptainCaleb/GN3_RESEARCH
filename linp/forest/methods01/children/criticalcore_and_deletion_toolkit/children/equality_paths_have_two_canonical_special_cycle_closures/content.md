# Minimum-potential equality paths have two canonical special cycle closures

## Statement

Assume the minimum-potential equality configuration average(phi)=m/n+1, so the conclusions of f9df80bd57f2 hold. Let v have p=phi(v), and let P=(g_1,...,g_p) be any maximum p-edge path ending at v, with last edge h=g_p. Then h is special, and the other two special edges f_1,f_2 through v each close P to a linear cycle of length p+1:
(g_1,g_2,...,g_p,f_i).
Consequently, if p=ell-1 in a P_ell-free equality obstruction, every maximum p-edge endpoint path lies in at least two distinct linear ell-cycles sharing the same p-edge path.

## Body

By f9df80bd57f2, every maximum p-edge path ending at v has a special last edge h=g_p. The two other special edges f_1,f_2 through v meet P outside v exactly at the two free vertices of g_1, one each, and have no other contact with P.

Fix i. The sequence
g_1,g_2,...,g_p,f_i
has consecutive intersections inherited from P, together with
g_p∩f_i={v}
and
f_i∩g_1={a_i},
where a_i is one of the two free vertices of g_1.

All nonconsecutive pairs are disjoint: f_i has no other contact with P, and P itself is linear. Therefore this sequence is a linear cycle of length p+1.

The two cycles are distinct because f_1≠f_2 and they close through different free vertices of g_1.

If p=ell-1, these are linear cycles of length ell. A linear ell-cycle need not itself contain a P_ell, so this is not yet a contradiction; rather it supplies two canonical closures of every maximum endpoint path, to which cycle-ear/chord arguments can be applied.