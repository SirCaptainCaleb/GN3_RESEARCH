# Contact-multiplicity snake inequality

## Statement

Let H be a finite linear 3-graph. For each nonisolated vertex v choose a maximum p_v=phi(v) edge path P_v with last vertex v and last edge h_v. For e incident with v define mu_v(h_v)=1, and for e!=h_v put mu_v(e)=|(e\\{v}) intersect (V(P_v)\\h_v)|. Then sum_{e contains v} mu_v(e)<=2phi(v)-1. Moreover every incidence with phi(e)<=phi(v) has mu_v(e)>=1; the only incidences not forced to have positive multiplicity are ascending nonspecial entrance incidences with phi(e)=phi(v)+1. Consequently, if A is the number of ascending nonspecial edges and X is the total multiplicity excess beyond the baseline 3m-A, then 3m-A+X<=sum_{v:d_H(v)>0}(2phi(v)-1).

## Body

Fix a nonisolated vertex v and write p=phi(v), P=(g_1,...,g_p), h=g_p. For every incident edge e!=h, the two-set e\{v} is disjoint from the corresponding two-set of every other incident edge, by linearity. Hence all vertices counted by
  mu_v(e)=|(e\{v}) intersect (V(P)\h)|
are distinct as e varies, and they all lie in the 2p-2 vertices of V(P)\h. Therefore
  sum_{e!=h, e contains v} mu_v(e) <= 2p-2.
With mu_v(h)=1 this gives
  sum_{e contains v} mu_v(e) <= 2p-1.

Now let e contain v and suppose phi(e)<=phi(v)=p. If e=h then mu_v(e)=1. Otherwise, if mu_v(e)=0, then e meets P only at v: its other two vertices lie outside V(P), since e and h already share v and linearity forbids another intersection inside h. Appending e to P through v gives a (p+1)-edge linear path ending in e, so phi(e)>=p+1, contradicting phi(e)<=p. Thus mu_v(e)>=1.

For any edge e of rank q=phi(e), a longest path ending in e has one entrance vertex and two terminal vertices. Both terminal vertices have vertex potential at least q. If e is special, all three vertices have potential at least q. If e is nonspecial with unique entrance x, deleting e from a longest q-edge witness gives phi(x)>=q-1; equality is exactly the ascending case. Hence every incidence of e is rank-admissible (phi(e)<=phi(v)) except possibly the unique entrance incidence of an ascending nonspecial edge, where phi(e)=phi(v)+1.

It follows that the baseline contribution to sum_{v,e} mu_v(e) is at least 3 for every nonascending or special edge and at least 2 for every ascending nonspecial edge, i.e.
  3m-A.
Define the nonnegative excess
  X = sum_{v:d_H(v)>0} sum_{e contains v} mu_v(e) - (3m-A).
Summing the local capacity inequality yields
  3m-A+X <= sum_{v:d_H(v)>0}(2phi(v)-1).
For a P_ell-free system the right side is at most (2ell-3)n.

This is a path-state generalization of the snake digraph: ordinary snake counting remembers only whether an incidence is maximal; mu records how many off-v vertices of the edge are forced onto one chosen maximum endpoint witness. Double blockers, nonascending entrance compensation, and any chosen-path contact of an ascending entrance all appear as positive excess X.
