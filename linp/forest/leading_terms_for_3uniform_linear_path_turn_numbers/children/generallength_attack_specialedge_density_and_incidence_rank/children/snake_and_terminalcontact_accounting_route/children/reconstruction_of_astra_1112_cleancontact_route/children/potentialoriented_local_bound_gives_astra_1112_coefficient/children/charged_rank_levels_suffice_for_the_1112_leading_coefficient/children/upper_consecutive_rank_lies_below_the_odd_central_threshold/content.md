# Any four-edge counterexample with occupied upper consecutive rank lies below the odd central threshold

## Statement

Fix v with p=phi(v), and suppose four potential-charged ascending nonspecial edges are terminal at v, all with ranks in {q,q+1}, and at least one has rank q+1. Then
  q+1 <= p <= 2q-2.
Moreover:
(i) if p=2q-2, at most one of the four edges has rank q, and every rank-q edge among them has opposite terminal u with phi(u)=p;
(ii) if p=2q-3, at most two of the four edges have rank q.
Thus at p=2q-2 the only possible ordered rank patterns are
  (q,q+1,q+1,q+1) and (q+1,q+1,q+1,q+1),
while at p=2q-3 at least two edges have rank q+1.
The all-rank-q case is handled only after reindexing q as the occupied upper level; it is not covered by the displayed hypothesis with the original q.

## Body

Fix v with p=phi(v), and suppose four potential-charged ascending nonspecial edges are terminal at v, all with ranks in {q,q+1}, with at least one edge of rank q+1. Then p>=q+1 because every charged edge terminal at v has rank at most p.

If p>=2q-1, apply a570b0ad0001 with Q=q+1. Since
  p>=2(q+1)-3,
at most two ascending nonspecial edges terminal at v have rank at most q+1, contradicting the four assumed edges. Therefore p<=2q-2.

Now suppose p=2q-2. Applying a570b0ad0001 at rank q gives the middle case
  phi(v)=2q-2,
so at most one ascending terminal edge has rank at most q. Hence at most one of the four has rank q.

For such a rank-q edge e={x,v,u}, potential charging gives phi(u)>=p. If phi(u)>p, then the strict-rise rank floor a4fb7e7b171e would give
  q>=ceil((p+3)/2)
   =ceil((2q+1)/2)
   =q+1,
impossible. Hence phi(u)=p.

Finally if p=2q-3, the first case of a570b0ad0001 at rank q gives at most two rank-at-most-q edges. Hence at most two of the four have rank q.

Thus, when q+1 is the occupied upper level of a four-edge consecutive-rank obstruction,
  q+1<=p<=2q-2,
with the stated sharper boundary restrictions.

If all four edges instead have rank q, this statement should be applied after reindexing the occupied upper level as q=(q-1)+1; the earlier version silently performed this reindexing without stating it.