# Lens-free low-defect centers still force near-top rank and five-eighths switching

## Statement

Let v be a nonisolated vertex with p=phi(v)>=8. Let T(v) be the ascending nonspecial edges terminal at v, let t=|T(v)|, and when t>0 let q be their maximum edge rank. Choose the maximum p-edge path P_v used in the exact defect identity a57007500001. Let D_v be the number of incident double contacts on P_v and put
  beta(p)=floor((11p-16)/8),
  eta_v=beta(p)-t+D_v.
Then eta_v>=0.

If q=p, then
  eta_v>=beta(p)-ceil((3p-4)/4)>=(5p-24)/8.

If q<p, let gamma be the exact fixed-entrance bound and a(q)=ceil((3q-4)/4). Then
  eta_v>=beta(p)-gamma(q).
Moreover, for every rank-q ascending terminal anchor h and every q-edge longest h-path Q ending at v, at least
  beta(p)-eta_v-a(q)
members of T(v) are double on Q but single on P_v. Their non-v pairs form a matching between vertices of the anchor precursor retained by P_v and vertices omitted by P_v.

Since these switching edges are single ascending terminal edges of rank at most q on P_v,
  beta(p)-eta_v-a(q) <= max(0,4q-2p-3).

Consequently eta_v=o(p) forces q=p-o(p) and, at every active misaligned v, produces (5/8-o(1))p anchor-double / maximum-path-single switching edges. No endpoint-lens conclusion is asserted.

## Body

The aligned case q=p is exactly the local estimate in a57007500001:
  t-D_v<=ceil((3p-4)/4).
Hence
  eta_v>=beta(p)-ceil((3p-4)/4)>=(5p-24)/8.

Assume q<p. The rank-sensitive local estimate in a57007500001 gives
  t<=gamma(q),
so
  eta_v=beta(p)-t+D_v>=beta(p)-gamma(q).                 (1)
For p>=8, beta(p)=gamma(p-1). For q>=4 the floor formula gives
  gamma(p-1)-gamma(q)>=11(p-1-q)/8-1,
while q<4 already makes the right side of (1) linear in p. Thus eta_v=o(p) implies q=p-o(p).

Fix a rank-q anchor h and a q-edge longest h-path Q ending at v. Put a(q)=ceil((3q-4)/4). By 243723939a85, if d_Q(T) counts the members of T(v)\{h} whose two non-v vertices lie in the precursor of Q, then
  d_Q(T)>=t-a(q).                                       (2)

Every member of T(v) has at least one off-v contact on the maximum path P_v because its edge rank is at most q<p=phi(v). Among the d_Q(T) edges counted in (2), at most D_v are double on P_v. Therefore at least
  d_Q(T)-D_v
  >=t-a(q)-D_v
  =beta(p)-eta_v-a(q)                                  (3)
are double on Q but single on P_v.

For each edge counted in (3), both non-v vertices lie in the precursor of Q, exactly one lies on P_v, and the other is omitted by P_v. Distinct edges through v have disjoint non-v pairs by linearity, so these pairs form a matching across the retained/omitted cut of the anchor precursor.

Finally every edge counted in (3) is a single ascending terminal edge of rank at most q on P_v. The central-window theorem 49080cbf1371 bounds the total number of such edges by
  max(0,4q-2p-3).
This proves the displayed inequality.

Since beta(p)=(11/8)p+O(1), a(q)=(3/4)q+O(1), and eta_v=o(p) implies q=p-o(p), (3) yields
  (5/8-o(1))p
switching edges. The argument contains no endpoint-lens conversion and therefore does not use the failed lemma b35b0fd4e4cd.