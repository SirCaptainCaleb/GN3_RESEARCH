# A reciprocal common-terminal contact forces foreign-edge transversality below the rank-sum threshold

## Statement

Let
  e={x,v,u}
be an ascending nonspecial edge of edge rank q, with unique entrance x and terminals v,u. Let
  P=(g_1,...,g_s)
be a maximum s-edge path with last vertex u, where s=phi(u). Assume e is single-contact at u on P and its unique off-u contact with V(P)\g_s is the other terminal v; in particular x is absent from P.

Let
  f={y,v,w}
be any distinct ascending nonspecial edge of edge rank r terminal at v. If neither y nor w lies on V(P), then
  q+r >= s+4.

Equivalently, if q+r<=s+3, every such f must have a non-v vertex on P. In particular, when phi(u)>=p, the inequality q+r<=p+3 forces f to make an additional non-v contact with the chosen maximum u-path.

## Body

Let [a,b] be the interval of path-edge indices containing v on P. Since v is the unique off-u contact of e and is a terminal of e, the singleton central-window bounds give
  a<=q-2,
  b>=s-q+2.
Also b<=a+1 because a vertex of a linear path belongs to at most two consecutive edges.

Assume for contradiction that neither non-v vertex of f lies on P. Then f meets P only at v.

The prefix
  g_1,...,g_a,f
is a linear path: by the definition of a, v first appears on g_a, and f has no other P-contact. It ends in f through the terminal v rather than the unique entrance y. Therefore it cannot have length at least r, so
  a+1<=r-1,
hence
  a<=r-2.                                           (1)

Now use the reversed suffix
  g_s,g_{s-1},...,g_b,f.
By the definition of b, v occurs in the final edge g_b of this reversed suffix and in no earlier edge of the reversed sequence; f has no other P-contact. Thus this is again a linear path ending in f through terminal v. Its length is
  (s-b+1)+1=s-b+2,
so nonspecialness gives
  s-b+2<=r-1,
hence
  b>=s-r+3.                                         (2)

Combining (2) with b<=a+1 and a<=q-2 gives
  s-r+3 <= b <= a+1 <= q-1,
so
  q+r>=s+4.

No source-clean assumption on f, no minimum-terminal orientation, no paid certificate, and no contact assumption at the other terminal of f is used.