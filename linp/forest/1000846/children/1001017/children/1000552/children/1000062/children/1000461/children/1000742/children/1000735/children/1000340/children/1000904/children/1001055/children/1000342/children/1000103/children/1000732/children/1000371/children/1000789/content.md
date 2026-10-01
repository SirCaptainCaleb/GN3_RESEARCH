# Low global defect forces near-top rank and dense switching lenses

## Statement

Let v have p=φ(v)>=8. Let T(v) be the ascending nonspecial edges terminal at v, let t=|T(v)|, and when t>0 let q be their maximum edge rank. Choose the maximum p-edge path P_v as in a57007500001. Let D_v count incident double contacts on P_v and put
  beta(p)=floor((11p-16)/8),
  eta_v=beta(p)-t+D_v.
Then eta_v>=0.

If q=p, then
  eta_v>=beta(p)-ceil((3p-4)/4)>=(5p-24)/8.

If q<p, write gamma for the exact fixed-entrance bound and a(q)=ceil((3q-4)/4). Then
  eta_v>=beta(p)-gamma(q).
Moreover, for every rank-q ascending terminal anchor h and every q-edge longest h-path Q ending at v, at least
  beta(p)-eta_v-a(q)
members of T(v) are double on Q but single on P_v. Their non-v pairs form a matching between vertices of the anchor precursor retained by P_v and vertices omitted by P_v. Hence P_v supports at least the same number of distinct balanced endpoint-lens states.

Since all these switching edges are single ascending terminal edges of rank at most q on P_v,
  beta(p)-eta_v-a(q) <= max(0,4q-2p-3).

In particular, eta_v=o(p) forces q=p-o(p) and produces (5/8-o(1))p switching edges and balanced endpoint lenses.

## Body

The aligned case q=p is the local estimate already used in a57007500001:
  t-D_v<=ceil((3p-4)/4).
This gives the displayed aligned lower bound on eta_v.

Assume q<p. Every edge of T(v) has rank at most q. The exact fixed-entrance theorem gives
  t<=gamma(q),
so
  eta_v=beta(p)-t+D_v>=beta(p)-gamma(q).                 (1)
For p>=8, beta(p)=gamma(p-1). If q>=4, the floor formula gives
  gamma(p-1)-gamma(q)>=11(p-1-q)/8-1.
Hence
  p-1-q<=(8/11)(eta_v+1).                               (2)
If q<4, (1) already makes eta_v linear in p. Thus eta_v=o(p) implies q=p-o(p).

Fix a rank-q anchor h and a q-edge longest h-path Q ending at v. Put a(q)=ceil((3q-4)/4). By 243723939a85, if d_Q(T) is the number of members of T(v)\{h} whose two non-v vertices both lie in the precursor of Q, then
  d_Q(T)>=t-a(q).                                       (3)

On P_v every member of T(v) has at least one off-v contact, since its rank is at most q<p. At most D_v members of T(v) are double on P_v. Therefore at least
  d_Q(T)-D_v
  >=t-a(q)-D_v
  =beta(p)-eta_v-a(q)                                  (4)
members are double on Q but single on P_v.

For each such edge, both non-v vertices lie in the precursor of Q, while exactly one lies on P_v and the other is absent from P_v. Distinct edges through v have disjoint non-v pairs by linearity, so they form a matching crossing the retained/omitted cut of the anchor precursor.

If c is the retained vertex of a switching pair, then c lies on the maximum path P_v and c≠v. Apply b35b0fd4e4cd to P_v and any maximum endpoint path ending at c. This gives a balanced elementary endpoint lens attached at c. Distinct switching pairs have distinct retained vertices, so (4) gives the same lower bound on distinct balanced endpoint-lens states.

Finally every switching edge is a single ascending terminal edge of rank at most q on P_v. By 49080cbf1371, the number of such edges is at most
  W=max(0,4q-2p-3).
Together with (4),
  beta(p)-eta_v-a(q)<=W.                               (5)

If eta_v=o(p), (2) gives q=p-o(p), while beta(p)=(11/8)p+O(1) and a(q)=(3/4)q+O(1). Thus (4) gives (5/8-o(1))p switching edges and hence the same number of balanced endpoint lenses.
