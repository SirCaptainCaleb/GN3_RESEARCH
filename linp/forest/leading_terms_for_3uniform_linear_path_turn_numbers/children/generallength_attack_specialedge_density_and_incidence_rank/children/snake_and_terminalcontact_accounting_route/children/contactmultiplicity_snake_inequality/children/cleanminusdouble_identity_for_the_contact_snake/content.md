# Clean-minus-double identity for the contact snake

## Statement

Choose a maximum endpoint path P_v for every vertex v and define contact multiplicities mu_v(e) as in c312c26b7c1d. Let C be the number of incidences with mu_v(e)=0 and D the number with mu_v(e)=2. Then 3m-C+D=sum_{v,e contains v}mu_v(e)<=sum_v(2phi(v)-1). In a P_ell-free linear triple system, 3m-C+D<=(2ell-3)n. Every clean incidence is the unique entrance incidence of an ascending nonspecial edge.

## Body

For a fixed vertex v, let c_i(v) be the number of incident edges e with mu_v(e)=i, i=0,1,2. The chosen last edge h_v has mu_v(h_v)=1, so every incident edge belongs to exactly one of these three classes. Hence
  d_H(v)=c_0(v)+c_1(v)+c_2(v),
while
  sum_{e contains v} mu_v(e)=c_1(v)+2c_2(v)
                              =d_H(v)-c_0(v)+c_2(v).
Summing over v gives the exact identity
  sum_v sum_{e contains v}mu_v(e)=3m-C+D,
where C=sum_v c_0(v) and D=sum_v c_2(v).

By the contact-multiplicity snake inequality c312c26b7c1d, the left side is at most
  sum_v(2phi(v)-1).
If H is P_ell-free, phi(v)<=ell-1 for every v, so
  3m-C+D <= (2ell-3)n.

Finally, c312c26b7c1d proves that every incidence with phi(e)<=phi(v) has positive multiplicity. For every edge e, all incidences satisfy phi(e)<=phi(v) except possibly the unique entrance of an ascending nonspecial edge, where phi(e)=phi(v)+1. Thus every clean incidence is exactly of this latter type. In particular each edge contributes to C at most once.