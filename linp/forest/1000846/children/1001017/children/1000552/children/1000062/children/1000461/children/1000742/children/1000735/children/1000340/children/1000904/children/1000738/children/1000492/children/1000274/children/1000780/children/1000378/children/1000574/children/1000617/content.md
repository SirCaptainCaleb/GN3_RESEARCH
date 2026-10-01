# A two-envelope local inequality isolates the near-top rank shell

## Statement

For a vertex v with p=phi(v) and maximum ascending-terminal rank q<p, one has t(v)-X_v <= min{gamma(q), max(0,4q-2p-3)}, where X_v is excess contact multiplicity on any chosen maximum p-path and gamma is the exact fixed-entrance bound. In particular q/p<=16/21 is controlled more strongly by the maximum-path window, and if p>=2q-1 then t(v)-X_v<=0. Thus the only asymptotically dangerous misaligned regime lies in the near-top band 16p/21<q<p.

## Body

Let H be a finite linear 3-graph. Fix a nonisolated vertex v and put
  p=phi(v).
Let t(v) be the number of ascending nonspecial edges terminal at v. If t(v)>0 let
  q=q(v)
be their maximum edge rank. Choose any maximum p-edge path P_v ending at v and let X_v be its excess contact multiplicity.

Assume q<p.

First, by the exact fixed-entrance terminal count at a maximum-rank ascending terminal edge,
  t(v)<=gamma(q),
where
  gamma(1)=0, gamma(2)=1, gamma(3)=2,
  gamma(q)=floor((11q-5)/8) for q>=4.               (1)

Second, relative to P_v, every ascending terminal edge counted by t(v) has rank at most q<p. If such an edge has contact multiplicity c on P_v, then its contribution to
  1-max(c-1,0)
is:
  1 for c=1,
  0 for c=2,
  <=0 for c>=3.
Hence
  t(v)-X_v
  <= number of counted ascending terminal edges that are single on P_v.  (2)

By 49080cbf1371, every such single-contact edge of rank at most q has its unique precursor contact in one common central window of size
  W(p,q)=max(0,4q-2p-3).
Distinct incident edges use distinct contact vertices by linearity. Therefore
  t(v)-X_v<=W(p,q).                                  (3)

Combining (1),(3),
  t(v)-X_v
  <= min{ gamma(q), max(0,4q-2p-3) }.               (4)

For q=p, the aligned estimate of 7f7e4ce0045c remains
  t(v)-X_v<=ceil((3p-4)/4).

ASYMPTOTIC ENVELOPES.
For q,p large with x=q/p<1,
  gamma(q)=(11/8)xp+O(1),
while
  W(p,q)=(4x-2)p+O(1).
The two slopes cross at
  11x/8 = 4x-2,
i.e.
  x=16/21.

Thus for q/p<=16/21 the maximum-path window is at least as strong as the fixed-entrance envelope. If p>=2q-1 then W=0, so
  t(v)-X_v<=0:
all ascending terminal incidences are fully paid by multiplicity excess on every maximum v-ending path.

The only asymptotically hard misaligned regime for the 43/48 coefficient is therefore
  16p/21 < q < p,
with the worst shell q=p-O(1).
