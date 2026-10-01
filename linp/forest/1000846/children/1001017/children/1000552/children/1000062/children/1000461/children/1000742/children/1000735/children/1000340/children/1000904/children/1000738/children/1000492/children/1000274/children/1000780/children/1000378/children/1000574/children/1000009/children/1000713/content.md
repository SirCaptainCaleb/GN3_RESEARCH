# Hybrid central-window and Astra bound for r=3 singleton terminal mass

## Statement

Let H be a finite linear 3-graph and fix a nonisolated vertex v with p=phi(v). Let t(v)>0 count ascending nonspecial edges terminal at v, let q=q(v) be their maximum rank, and let P_v be any maximum p-edge endpoint path at v. Let X_v be the excess contact multiplicity on P_v. If q<p, then
t(v)-X_v <= min{ gamma(q), max(0,4q-2p-3) },
where gamma(1)=0, gamma(2)=1, gamma(3)=2 and gamma(q)=floor((11q-5)/8) for q>=4.
If q=p and P_v is chosen through a top-rank ascending terminal edge, then
t(v)-X_v <= ceil((3p-4)/4).
Thus for misaligned vertices the local cost is the minimum of the Astra fixed-entrance bound and the path-relative central-window packing bound. In the positive central-window regime, asymptotically that term is stronger for q/p<16/21, while Astra is stronger for q/p>16/21.

## Body

Because H is 3-uniform, every ascending terminal edge at v has chosen-path contact multiplicity one or two on P_v. Hence X_v is exactly the number of double contacts, and t(v)-X_v is exactly the number of single contacts.

The exact fixed-entrance theorem eb40ddcc33ca gives
  t(v)<=gamma(q),
so
  t(v)-X_v<=gamma(q).

Independently, 49080cbf1371 applied to P_v bounds the number of single-contact ascending terminal edges of rank at most q by
  max(0,4q-2p-3).
All edges counted by t(v) have rank at most q, and t(v)-X_v is precisely their single-contact count. Therefore
  t(v)-X_v <= max(0,4q-2p-3),
which proves the misaligned minimum bound.

If q=p, choose P_v to end in a rank-p ascending terminal edge. The aligned multiplicity cancellation of 3b170b2ae6ae gives
  t(v)-X_v <= ceil((3p-4)/4)
in the three-uniform case.

Finally, in the regime where the central-window term is positive and lower-order constants are ignored, compare the two misaligned costs (11/8)q and 4q-2p. Equality of their p-normalized slopes occurs at
  (11/8)theta=4theta-2,
so theta=16/21.
