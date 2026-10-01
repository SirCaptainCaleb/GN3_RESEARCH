# Maximum-path central windows sharpen the Astra multiplicity master inequality

## Statement

Let p(v)=phi(v), let t(v) count ascending nonspecial edges terminal at v, and let q(v) be their maximum rank when t(v)>0. Choose a maximum endpoint path P_v, choosing it to end in a rank-p(v) ascending terminal edge when q(v)=p(v). Let D_v count double contacts on P_v and D=sum_v D_v.

Define B(v)=0 if t(v)=0; B(v)=ceil((3p(v)-4)/4) if q(v)=p(v); and if 0<q(v)<p(v), put
B(v)=min{gamma(q(v)), max(0,4q(v)-2p(v)-3)},
where gamma(2)=1, gamma(3)=2, and gamma(q)=floor((11q-5)/8) for q>=4.

Then
2A-D <= sum_v B(v),
A-D <= (1/2)sum_v B(v),
and
3m <= 2S-n_+ +(1/2)sum_v B(v).

## Body

At an aligned active vertex q=p, the exact fixed-entrance singleton-versus-double inequality gives t(v)-D_v<=ceil((3p-4)/4).

If 0<q<p, every ascending edge counted by t(v) has rank at most q. Hence t(v)-D_v is at most the number of those incidences that are single on P_v. By 49080cbf1371 this is at most max(0,4q-2p-3). Independently t(v)-D_v<=t(v)<=gamma(q), by the exact fixed-entrance theorem at a maximum-rank ascending terminal edge. Thus t(v)-D_v<=B(v).

Summing and using sum_v t(v)=2A gives 2A-D<=sum_v B(v). Since D>=0, 2(A-D)<=2A-D, hence A-D<=(1/2)sum_v B(v). Finally the certified contact identity gives 3m<=2S-n_+ +(C-D), and C<=A, proving the last inequality.
