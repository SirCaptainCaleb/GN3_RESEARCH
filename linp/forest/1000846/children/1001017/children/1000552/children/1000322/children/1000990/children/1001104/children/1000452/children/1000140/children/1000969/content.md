# A pair-universal star converts degree-potential defect exactly into clean ascending sources

## Statement

Let v be pair-universal and P a maximum p=phi(v)-edge path ending at v. If B_j counts star pairs through v with exactly j contacts in V(P)\{v}, then B_0-B_2=d_H(v)-2p. Every B_0 edge is necessarily an ascending nonspecial edge of rank p+1 with unique entrance v. Hence every maximum v-ending path exposes at least d_H(v)-2phi(v) clean ascending source edges, with exact surplus B_2.

## Body

Let H be a finite linear 3-graph and let v be pair-universal: every pair {v,x}, x!=v, lies in a unique hyperedge. Equivalently the d_H(v)=(n-1)/2 edges through v induce a perfect matching on V(H)\{v}.

Choose a maximum p-edge path
  P=(g_1,...,g_p)
ending physically at v, so p=phi(v). For each edge f={v,a,b} through v, let its star pair be {a,b}. Let B_j be the number of star pairs having exactly j vertices in V(P)\{v}, j=0,1,2.

Because the star pairs partition V(H)\{v},
  B_0+B_1+B_2=d_H(v),
and because |V(P)\{v}|=2p,
  B_1+2B_2=2p.
Subtracting gives the exact identity
  B_0-B_2=d_H(v)-2p.                                (1)

Now take a clean star edge f={v,a,b} counted by B_0. Then a,b are outside V(P), so
  P,f
is a (p+1)-edge linear path ending in f and entering f through v. Hence
  phi(f)>=p+1.
But every edge incident with a vertex of endpoint potential p has rank at most p+1 (the elementary incident-rank bound used in e766796773d9), so
  phi(f)=p+1.

We claim f is nonspecial. If f were special, then at rank p+1 there would be a witness entering f through a (or through b). In that witness v is a terminal vertex of f, so there would be a (p+1)-edge path ending physically at v. This contradicts phi(v)=p.

Thus f is nonspecial, its rank is p+1, and the displayed path P,f shows v is an entrance. Since f is nonspecial the entrance is unique. Therefore
  phi(v)=p=phi(f)-1,
so f is ascending with unique entrance v.

Consequently every clean star pair contributes an ascending nonspecial source edge at v, and
  c(v)>=B_0>=d_H(v)-2phi(v),                         (2)
where the second inequality follows from (1) and B_2>=0.

More precisely,
  B_0=c_P(v)
is the number of v-source ascending edges clean relative to the chosen maximum path P, and
  c_P(v)-B_2=d_H(v)-2phi(v).
Thus double-blocking star pairs pay exactly for any clean-source count above the baseline degree-potential defect.
