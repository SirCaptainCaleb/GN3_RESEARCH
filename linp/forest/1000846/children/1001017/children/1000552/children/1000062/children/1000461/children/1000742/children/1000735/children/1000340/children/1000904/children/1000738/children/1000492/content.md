# The contact-multiplicity snake and unpaid-edge reduction extend to arbitrary uniformity

## Statement

For every finite linear r-uniform hypergraph, choose one maximum endpoint path P_v at each nonisolated vertex and define contact multiplicities mu_v(e). Let C count clean incidences mu=0 and X=sum max(mu-1,0) be total excess contact multiplicity. Then rm-C+X <= (r-1)sum_v phi(v)-(r-2)n_+. Moreover C-X is bounded by the number of ascending nonspecial edges whose chosen-path signature is (0,1,...,1): clean at the unique entrance and single at all r-1 terminals. Hence rm <= (r-1)S-(r-2)n_+ + N_{0,1^{r-1}}.

## Body


Let H be a finite linear r-uniform hypergraph, r>=3. For every nonisolated vertex v choose a maximum endpoint path
  P_v=(g_1,...,g_p),  p=phi(v),
ending at v, and let h_v=g_p be its last edge.

Define
  mu_v(h_v)=1,
and for e!=h_v incident with v,
  mu_v(e)=|(e minus {v}) intersect (V(P_v) minus h_v)|.

LOCAL CAPACITY.
For e!=h_v, if mu_v(e)>0 then its contact vertices lie in V(P_v)\h_v. Because any two distinct incident edges e,f through v share only v by linearity, their contact sets are pairwise disjoint. Hence
  sum_{e contains v, e!=h_v} mu_v(e)
  <= |V(P_v) minus h_v|
  =(r-1)(p-1).
Adding mu_v(h_v)=1 gives
  sum_{e contains v} mu_v(e)
  <=(r-1)p-(r-2).                                  (1)

CLASSIFICATION OF CLEAN INCIDENCES.
Suppose mu_v(e)=0. Then e!=h_v and e is disjoint from V(P_v)\h_v outside v. Therefore
  P_v,e
is a (p+1)-edge linear path ending in e and entering e through v. Any edge incident with v has rank at most p+1, so phi(e)=p+1.

Thus v is an entrance of a longest e-ending path. If e had another possible entrance, or were special, then v would also be terminal at rank p+1, yielding phi(v)>=p+1, contradiction. Hence e is nonspecial with unique entrance v. Since phi(v)=p=phi(e)-1, e is ascending.

Therefore every zero-multiplicity incidence is the unique entrance incidence of an ascending nonspecial edge, and every edge has at most one such incidence.

GLOBAL IDENTITY.
Let
  C=#{(e,v): v in e, mu_v(e)=0},
and define the total excess multiplicity
  X=sum_{e,v in e} max(mu_v(e)-1,0).

For an incidence with mu>=1, write mu=1+(mu-1); for a zero incidence the baseline 1 is missing. Summing over all rm incidences,
  sum_{e,v in e} mu_v(e)
   =rm-C+X.                                         (2)

Summing (1) over nonisolated vertices and using (2),
  rm-C+X <= (r-1)S-(r-2)n_+,                       (3)
where S=sum_v phi(v).

EDGEWISE DEFECT.
Fix an ascending nonspecial edge e with unique entrance x and terminals
  T=e minus {x},
|T|=r-1.
The contribution of e to C-X can be positive only if:
- mu_x(e)=0, so its source incidence contributes +1 to C;
- every terminal t in T has mu_t(e)=1, so no terminal contributes to X;
- also the source contributes no excess, automatically since mu_x=0.

If any terminal has mu_t(e)>=2, or if the source is not clean, the net contribution of e to C-X is at most zero.

Thus if N_{0,1^{r-1}} denotes the number of ascending nonspecial edges whose chosen-path multiplicity signature is
  (mu_x(e); (mu_t(e))_{t in T})=(0;1,1,...,1),
then
  C-X <= N_{0,1^{r-1}}.                             (4)

Combining (3),(4),
  rm <= (r-1)S-(r-2)n_+ + N_{0,1^{r-1}}.           (5)

This is the arbitrary-uniformity contact-snake defect reduction. For r=3, X is exactly the double-contact incidence count and N_{0,1^{r-1}} is N_011.
