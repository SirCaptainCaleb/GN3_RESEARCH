# Gap-one local slack splits exactly into anchor slack, foreign low-rank edges, and maximum-path doubles

## Statement

Let v lie in the gap-one shell phi(v)=q+1 with q(v)=q>=4. Let T be the family of ascending nonspecial edges terminal at v, t=|T|, and let P be any maximum (q+1)-edge path ending at v. Let X_v^T be the number of T-edges double on P. Put
J=J_q(v)={f containing v: phi(f)<=q},
M=gamma(q)=floor((11q-5)/8),
and
delta=M-(t-X_v^T).

Then
delta=(M-|J|)+(|J|-t)+X_v^T.
All three summands are nonnegative. Consequently:
1. M-|J|<=delta;
2. |J|-t<=delta;
3. X_v^T<=delta.

Thus a near-dangerous gap-one local state is simultaneously near-extremal for the fixed-entrance Astra system, contains at most delta low-rank incident edges outside the ascending-terminal family, and has at most delta ascending-terminal doubles on the maximum path.

Combining with the periodic stability theorem, all but O(delta+1) cells of the anchor contact pattern lie on the critical period-four cycle, and all but O(delta) of the corresponding incident edges are ascending-terminal edges at v.

## Body

Because q(v)=q, every edge of T has rank at most q, so T is a subset of J. The exact fixed-entrance theorem gives |J|<=M. Finally X_v^T>=0. Therefore each of
M-|J|, |J|-t, X_v^T
is nonnegative.

Their sum telescopes:
(M-|J|)+(|J|-t)+X_v^T
=M-t+X_v^T
=M-(t-X_v^T)
=delta.
This proves the exact identity and the three individual bounds.

Now put r=M-|J|. Then r<=delta. Applying 88db9b4e8337 to J shows that the number of noncritical state transitions and exceptional contact cells is O(r+1)=O(delta+1). Since at most |J|-t<=delta members of J fail to belong to T, all but O(delta) of the edges occupying the remaining periodic contact pattern are ascending nonspecial edges terminal at v.