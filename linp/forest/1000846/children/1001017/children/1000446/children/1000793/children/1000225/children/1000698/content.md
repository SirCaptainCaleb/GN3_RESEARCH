# Potential superlevel cuts are controlled by the exact induced-core density defect

## Statement

For every potential threshold t, let E_t=|E(H[V_t])| and xi_t=E_t-d|V_t|. Then
  A_t >= M_{>=t}-E_t
      = M_{>=t}-d|V_t|-xi_t.
If H is vertex-minimal for S_ell and V_t is proper, a nonnegative xi_t cannot be excluded by minimality alone: when H[V_t] contains a nonspecial edge, minimality instead guarantees a vertex of degree at most d inside that core; when the core is all-special, xi_t<0. Thus the earlier universal +1 boundary-flow term requires an additional induced-core deficit hypothesis.

## Body

Fix ell>=4 and d=floor(2ell/3). Let H be a P_ell-free linear 3-graph with endpoint potential phi. For t>=1 put
  V_t={v:phi(v)>=t},
  M_{>=t}=|{e:phi(e)>=t}|,
and let A_t be the number of ascending nonspecial edges of rank exactly t. Write
  E_t=|E(H[V_t])|
and
  xi_t=E_t-d|V_t|.

By the certified potential-cut classification 321022a601f7, among edges of rank at least t the only edges not wholly contained in V_t are the ascending nonspecial edges of rank exactly t. Therefore
  M_{>=t}-A_t
counts rank-at-least-t edges contained in H[V_t], and in particular
  M_{>=t}-A_t <= E_t.

Equivalently,
  A_t >= M_{>=t}-E_t
      = M_{>=t}-d|V_t|-xi_t.                         (1)

This is the exact unconditional potential-cut inequality.

Now suppose additionally that H is vertex-minimal for the strengthened equality-layer assertion S_ell. If V_t is a proper nonempty subset and xi_t>=0, then H[V_t] has density at least d. If H[V_t] contains a nonspecial edge, minimality of S_ell does not force xi_t<0; rather, it forces H[V_t] to contain a vertex of degree at most d. If every edge of H[V_t] is special, then the certified all-special snake bound gives E_t<d|V_t|, so xi_t<0.

Thus a nonnegative superlevel density defect is possible only together with a low-degree witness inside a nonspecial induced core. The former claim
  A_t >= M_{>=t}-d|V_t|+1
is valid only when one separately knows xi_t<=-1; it does not follow from vertex-minimality alone.
