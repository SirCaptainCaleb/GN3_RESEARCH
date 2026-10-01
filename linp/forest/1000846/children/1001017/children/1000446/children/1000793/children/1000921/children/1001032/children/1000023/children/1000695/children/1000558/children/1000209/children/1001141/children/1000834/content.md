# The bottom potential layer forces distance from the seven-sixths floor

## Statement

In the setting of fa7e5e79b905, let h=min_v phi(v) and let L_h={v:phi(v)=h}, r=|L_h|. Then
  eta >= [r(2h-5)]/[6n(2h-3)].
In particular eta >= (r/n)/18 for h>=3, and asymptotically the coefficient tends to (r/n)/6 as h grows.

Thus any sequence of dense cores with eta=o(1) must have a bottom potential layer of size o(n).

## Body

No ascending nonspecial edge can have a terminal v with phi(v)=h. Indeed if e has rank q and is ascending with entrance x, then phi(x)=q-1, while terminality gives q<=phi(v)=h. Hence phi(x)<=h-1, contradicting minimality of h.

Therefore every nonspecial terminal incidence at a vertex of L_h belongs to a nonascending nonspecial edge.

Let E_exc be the number of non-Type-A vertices. By fa7e5e79b905,
  E_exc<=6eta n,
and the number N_na of nonascending nonspecial edges satisfies
  N_na<=6eta n.

Each Type-A vertex v in L_h has
  t_ns(v)=2h-5.
Hence the total number of nonspecial terminal incidences at bottom-level Type-A vertices is at least
  (r-E_exc)(2h-5),
with the expression interpreted as zero if r<E_exc.

Each nonascending nonspecial edge has only two terminal incidences, so
  (r-6eta n)(2h-5)
  <= 2N_na
  <= 12eta n.

Rearranging,
  r(2h-5)
  <= 6eta n(2h-5)+12eta n
  = 6eta n(2h-3),
so
  eta >= r(2h-5)/[6n(2h-3)].

For h>=3, (2h-5)/(6(2h-3)) is at least 1/18.
