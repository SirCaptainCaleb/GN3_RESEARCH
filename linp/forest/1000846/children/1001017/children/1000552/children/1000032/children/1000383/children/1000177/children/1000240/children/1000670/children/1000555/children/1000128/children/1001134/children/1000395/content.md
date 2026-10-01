# Near-dangerous gap-one states force two near-top source rails with eleven-sixteenths overlap

## Statement

Let v lie in the gap-one shell phi(v)=q+1, q(v)=q>=4. Let T be the family of ascending nonspecial edges terminal at v, let k=|T|, and let
delta=gamma(q)-(k-X_v^T),
where X_v^T>=0 is the number of T-edges double on a chosen maximum (q+1)-path and gamma is the exact fixed-entrance bound. Then k>=gamma(q)-delta.

Fix an integer m with 3<=m<k. Let D be any integer with 0<=D<q-3 such that
gamma(q)-gamma(q-D)>delta+m.
Then at least m edges of T have rank greater than q-D.

Choose canonical maximum source rails for any m such top-rank edges. Some pair of these rails shares at least
(k-m) floor((m-1)^2/4) / C(m,2)
distinct distinguished source-or-opposite-terminal vertices belonging to the other edges of T.

Consequently, for any near-dangerous sequence with delta=o(q), one may choose m tending to infinity with
m=o(q) and delta=o(m), obtaining two ascending edges of ranks q-o(q) whose canonical maximum source rails share
(11/16-o(1))q
distinct distinguished vertices.

## Body

The inequality k>=gamma(q)-delta is immediate from
delta=gamma(q)-(k-X_v^T)
and X_v^T>=0.

Order the edges of T by nondecreasing rank. For any integer s, the number of T-edges of rank at most s is at most gamma(s): if the subfamily is nonempty, choose one of maximum rank r<=s; the whole subfamily lies in J_r(v), and the exact fixed-entrance theorem gives size at most gamma(r)<=gamma(s).

Suppose fewer than m edges have rank greater than q-D. Then at least k-m+1 edges have rank at most q-D. Hence
k-m+1<=gamma(q-D).
But k>=gamma(q)-delta, so
gamma(q)-delta-m+1<=gamma(q-D),
contradicting the assumed strict inequality
gamma(q)-gamma(q-D)>delta+m.
Thus at least m edges have rank greater than q-D.

Take those m edges among the final rank-ordered rails, and put h=k-m. Every chosen rail belongs to an index greater than h. Apply f9b8f7df1398 to the first h edges as distinguished coordinates. It gives a pair of the chosen rails sharing at least
h floor((m-1)^2/4)/C(m,2)
distinct distinguished vertices, which is the displayed bound.

Finally assume delta=o(q). Choose m=m(q) with m->infinity, m=o(q), and delta=o(m). Since
gamma(q)-gamma(q-D)=(11/8)D+O(1),
one may take D=O(m+delta)=o(q). Also
k>=gamma(q)-delta=(11/8)q-o(q),
while
floor((m-1)^2/4)/C(m,2)=1/2-o(1).
Therefore the overlap lower bound is
(1/2-o(1))((11/8)q-o(q))
=(11/16-o(1))q,
and both rail ranks are q-o(q).
