# Near-saturated short anchors force linear overlap with every maximum terminal path

## Statement

Let v be a vertex of a finite linear 3-graph, and let h be an ascending edge of rank q>=4 terminal at v. Let
Q=(g_1,...,g_q=h)
be a longest h-path ending at v. Let T be any family of ascending edges terminal at v whose ranks are at most q and which contains h, and write t=|T|.

Let d_Q(T) be the number of edges e in T minus {h} for which both vertices of e minus {v} lie in V(Q) minus h. Then
d_Q(T) >= t-ceil((3q-4)/4).

Now let P be any maximum p=phi(v) edge path ending at v, with p>=q. Then
|(V(Q) minus h) intersect (V(P) minus last(P))|
>= t-ceil((3q-4)/4).

In particular, if T is the full family of ascending terminal edges at v and t is within r of the exact local maximum floor((11q-5)/8), then every maximum v-path shares at least floor(5q/8)-r vertices with the precursor of every maximum-rank ascending anchor h.

## Body

Put J=J_q(v). Relative to Q, every edge of J minus {h} has a contact set of size one or two. By cac6635878e5,
|J|-d_Q(J)<=ceil((3q-4)/4),
where d_Q(J) counts the double-contact edges of J minus {h}.

Every edge of T is in J. The number of non-double members of T is at most the number of non-double members of J, namely |J|-d_Q(J). Therefore
t-d_Q(T)<=ceil((3q-4)/4),
which proves the first inequality.

Fix now any maximum p-edge path P ending at v. For each e in T minus {h} counted by d_Q(T), write e={v,a_e,b_e}; both a_e,b_e lie in V(Q) minus h. Since phi(e)<=q<=p=phi(v), the contact-multiplicity lemma for the maximum path P gives
(e minus {v}) intersect (V(P) minus last(P)) nonempty.
Hence at least one of a_e,b_e belongs to both V(Q) minus h and V(P) minus last(P).

For distinct edges e,e' through v, the pairs {a_e,b_e} and {a_e',b_e'} are disjoint by linearity. Thus the chosen common vertices are distinct, proving
|(V(Q) minus h) intersect (V(P) minus last(P))|>=d_Q(T).

For the final statement, if t>=floor((11q-5)/8)-r, then
d_Q(T)>=floor((11q-5)/8)-r-ceil((3q-4)/4)
=floor(5q/8)-r,
using the same floor-ceiling identity as cac6635878e5.
