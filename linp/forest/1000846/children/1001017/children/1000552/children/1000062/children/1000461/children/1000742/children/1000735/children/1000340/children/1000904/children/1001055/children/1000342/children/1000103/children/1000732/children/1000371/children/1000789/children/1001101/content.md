# Lens-free dense switching theorem

## Statement

Let v have p=phi(v)>=8. Let T(v) be the ascending nonspecial edges terminal at v, let t=|T(v)|, and when t>0 let q be their maximum edge rank. Choose the maximum p-edge path P_v as in a57007500001. Let D_v count incident double contacts on P_v and put
  beta(p)=floor((11p-16)/8),
  eta_v=beta(p)-t+D_v.

Then eta_v>=0. If q=p, then
  eta_v>=beta(p)-ceil((3p-4)/4)>=(5p-24)/8.

If q<p, write gamma for the exact fixed-entrance bound and a(q)=ceil((3q-4)/4). Then
  eta_v>=beta(p)-gamma(q).
Moreover, for every rank-q ascending terminal anchor h and every q-edge longest h-path Q ending at v, at least
  beta(p)-eta_v-a(q)
members of T(v) are double on Q but single on P_v.

For each such switching edge e={x,v,u}, both x,u lie in the anchor precursor V(Q)\h, while exactly one lies in V(P_v)\last(P_v). Distinct switching edges have disjoint non-v pairs. Hence they form a matching between anchor vertices retained by P_v and anchor vertices omitted by P_v.

Since all these switching edges are single ascending terminal edges of rank at most q on P_v,
  beta(p)-eta_v-a(q) <= max(0,4q-2p-3).

In particular, eta_v=o(p) forces q=p-o(p) and produces (5/8-o(1))p anchor-double / host-single switching edges, with a disjoint retained/omitted matching on the anchor precursor.

## Body

The nonnegativity eta_v>=0 and the aligned q=p estimate are the exact local-deficit conclusions already certified in 513a28536c66.

Assume q<p. The fixed-entrance terminal bound gives
  t<=gamma(q),
and therefore
  eta_v=beta(p)-t+D_v>=beta(p)-gamma(q).

Fix a rank-q anchor h and a q-edge longest h-path Q ending at v. By 243723939a85, if d_Q(T) is the number of members of T(v)\{h} whose two non-v vertices both lie in the precursor V(Q)\h, then
  d_Q(T)>=t-a(q).

Every member of T(v) has at least one off-v contact with P_v because its edge rank is at most q<p. At most D_v members can be double on P_v, since every double member contributes at least one unit to D_v. Hence at least
  d_Q(T)-D_v
  >=t-a(q)-D_v
  =beta(p)-eta_v-a(q)
members are double on Q but single on P_v.

For such an edge e={x,v,u}, anchor-double means x,u both lie in V(Q)\h. Host-single means exactly one of x,u lies in V(P_v)\last(P_v): at least one contact is forced because phi(e)<p, and a second contact would make e double on P_v. Distinct edges through v have disjoint non-v pairs by linearity. Therefore these pairs form a matching crossing the retained/omitted cut of the anchor precursor.

Finally, every switching edge is an ascending terminal edge of rank at most q that is single on P_v. The central-window packing theorem 49080cbf1371 therefore gives
  beta(p)-eta_v-a(q)<=max(0,4q-2p-3).

If eta_v=o(p), the inequality eta_v>=beta(p)-gamma(q) and the exact asymptotics
  beta(p)=(11/8)p+O(1),
  gamma(q)=(11/8)q+O(1)
force q=p-o(p). Substituting into the switching lower bound gives
  beta(p)-eta_v-a(q)=(5/8-o(1))p.

No endpoint-lens existence statement is used anywhere. In particular this theorem is independent of b35b0fd4e4cd and survives the counterexample 23fac5740304.
