# Terminal-single reciprocity gives contact-type-free foreign transversality below the rank-sum threshold

## Statement


Let e={x,v,u} be an ascending nonspecial edge of rank q, with unique entrance x and terminals v,u. Let
  P=(g_1,...,g_s)
be a maximum s-edge path with last vertex u, where s=phi(u)>q. Assume e has contact multiplicity one at u on P, i.e.
  |(e\{u}) intersect (V(P)\g_s)|=1.

Let f={y,v,w} be a distinct nonspecial edge of rank r for which v is terminal. If neither y nor w belongs to V(P), then
  q+r >= s+4.

Equivalently, if q+r<=s+3, then f has a non-v vertex on P.

The conclusion is independent of whether the unique off-u contact of e on P is its entrance x or the other terminal v. In particular, for a doubly-terminal-single strict-gap family assigned at a common terminal v of rank p with phi(u)>=p, every foreign edge f of rank r satisfying q+r<=p+3 must meet the chosen maximum u-path away from v.


## Body


Let c be the unique off-u contact of e with the precursor V(P)\g_s. Since e\{u}={x,v}, there are two cases.

Case 1: c=v.

Write [a,b] for the interval of path-edge indices containing v. The singleton central-window bounds for the ascending rank-q edge e on the maximum u-path give
  a<=q-2,
  b>=s-q+2,
and b<=a+1.

Assume f has no non-v vertex on P. Then f meets P only at v. The reversed suffix
  g_s,g_{s-1},...,g_b,f
is a linear path: by the definition of b, the suffix meets f only in its final host edge at v. It ends in f through the terminal v rather than the unique entrance y. Hence its length must be at most r-1:
  s-b+2 <= r-1,
so
  b>=s-r+3.
Combining this with b<=a+1<=q-1 gives
  s-r+3<=q-1,
and therefore q+r>=s+4.

Case 2: c=x.

Now v is absent from P. Indeed v does not lie in the precursor because x is the unique off-u contact; it also cannot lie in the last edge g_s, since g_s and e already share u and linearity forbids a second common vertex.

Write [a,b] for the interval of path-edge indices containing x. The singleton central-window bounds give
  a<=q-1,
  b>=s-q+2,
and again b<=a+1. Thus
  a>=s-q+1.                                      (1)

Assume again that f has no non-v vertex on P. Since v is absent from P, f is disjoint from P. The sequence
  g_1,...,g_a,e,f
is a linear path: the prefix meets e only at x, e meets f only at v, and f misses the prefix. It ends in f through the terminal v rather than the unique entrance y. Hence
  a+2 <= r-1,
so
  a<=r-3.                                        (2)
Combining (1) and (2) yields
  s-q+1<=r-3,
equivalently q+r>=s+4.

Thus the same threshold holds in both reciprocal contact types. The final common-terminal consequence follows from s=phi(u)>=p.
