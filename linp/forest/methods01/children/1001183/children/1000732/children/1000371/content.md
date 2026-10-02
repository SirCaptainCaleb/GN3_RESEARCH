# The exact global deficit controls gap-one switching and lens mass

## Statement

Let v have p=φ(v)>=8, let T(v) be the ascending nonspecial edges terminal at v, let t=|T(v)|, let q be their maximum edge rank when t>0, and let D_v and
  eta_v=beta(p)-t+D_v,
  beta(p)=floor((11p-16)/8),
be as in the exact identity of a57007500001.

Then:
(1) if q=p, eta_v>=beta(p)-ceil((3p-4)/4)>=(5p-24)/8;
(2) if q<p, eta_v>=beta(p)-gamma(q), where gamma is the exact fixed-entrance bound.

Hence eta_v=0 forces q=p-1, t=gamma(p-1)=beta(p), and D_v=0.

Moreover, in the gap-one case q=p-1, the gap-one switching slack delta_v satisfies delta_v<=eta_v. Therefore every rank-q anchor and the chosen maximum p-edge path produce at least
  floor(5q/8)-eta_v
switching edges that are double on the anchor and single on the maximum path; their retained endpoints give the same number of distinct balanced endpoint lenses on the maximum path.

## Body

Let v be a nonisolated vertex with p=φ(v)>=8. Let T(v) be the family of ascending nonspecial edges terminal at v, let t=|T(v)|, and, when t>0, let q be the maximum edge rank in T(v). Choose the maximum p-edge path P_v as in a57007500001, and let D_v be its total number of incident double contacts. Put
  beta(p)=floor((11p-16)/8),
and
  eta_v=beta(p)-t+D_v.
By a57007500001, eta_v>=0.

First suppose q=p. The aligned fixed-entrance estimate used in a57007500001 gives
  t-D_v <= ceil((3p-4)/4).
Hence
  eta_v >= beta(p)-ceil((3p-4)/4).
In particular eta_v >= (5p-24)/8.

Now suppose q<p. Every member of T(v) has rank at most q, so the exact fixed-entrance theorem gives
  t <= gamma(q),
where gamma(1)=0, gamma(2)=1, gamma(3)=2, and gamma(s)=floor((11s-5)/8) for s>=4. Therefore
  eta_v=beta(p)-t+D_v >= beta(p)-gamma(q).
Since beta(p)=gamma(p-1) for p>=8 and gamma is strictly increasing, eta_v=0 is possible only when q=p-1. In that case eta_v=0 forces simultaneously
  t=gamma(p-1)=beta(p)
and
  D_v=0.

More generally assume q=p-1. Let X_v^T be the excess contact multiplicity contributed on P_v by the ascending terminal family T(v), and define the gap-one slack
  delta_v=gamma(q)-(t-X_v^T).
Because X_v^T<=D_v and beta(p)=gamma(q),
  delta_v
   = beta(p)-t+X_v^T
   = eta_v-D_v+X_v^T
   <= eta_v.

Apply the gap-one switching theorem fecba48a3ffd. For any rank-q ascending terminal anchor h at v, any q-edge longest h-path Q ending at v, and the chosen maximum p-edge path P_v, at least
  gamma(q)-ceil((3q-4)/4)-delta_v
  = floor(5q/8)-delta_v
  >= floor(5q/8)-eta_v
members of T(v) are double on Q but single on P_v. Their non-v pairs form a matching crossing the cut between anchor vertices retained by P_v and anchor vertices omitted by P_v.

Finally, ab7d5ecf773c converts each retained endpoint of this switching matching into a distinct balanced endpoint lens on P_v. Thus P_v supports at least floor(5q/8)-eta_v distinct balanced endpoint-lens states.

Consequently the local deficit eta_v occurring in the exact global identity is already the correct quantitative slack for the gap-one lens machinery. Exact zero deficit forces the unique dangerous shell q=p-1, full local saturation t=gamma(p-1), no double contact on P_v, and at least floor(5(p-1)/8) switching pairs and balanced endpoint lenses.