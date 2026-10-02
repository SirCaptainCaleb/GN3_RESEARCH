# Separated singleton contacts force rank sum at least host rank plus four without a contact-type hypothesis

## Statement

Let P=(g_1,...,g_p) be a maximum p-edge path with last vertex v and last edge h=g_p. Let
  e={x,v,u},  f={y,v,z}
be distinct ascending nonspecial edges, neither equal to h, that are terminal at v.

Assume each edge has contact multiplicity one at v on P. Let c_e,c_f be their unique contacts in
  V(P) minus h,
and let
  I(c)=[a(c),b(c)]
be the interval of path-edge indices containing c.

If
  b(c_e)<a(c_f),
then
  phi(e)+phi(f)>=p+4.

No assumption is required on whether either singleton contact is a unique entrance or the opposite terminal.

## Body

Write r=phi(e) and s=phi(f).

By the certified singleton central-window theorem 49080cbf1371 applied to e,
  b(c_e)>=p-r+2.
A path vertex belongs to at most two consecutive path edges, so
  b(c_e)<=a(c_e)+1.
Hence
  a(c_e)>=p-r+1.                                      (1)

We claim that
  a(c_e)<=s-3.                                        (2)

Because c_e is the unique contact of e in V(P) minus h and e,h already meet at v, linearity implies that the other non-v vertex of e is absent from all of P. Therefore the prefix
  g_1,...,g_{a(c_e)}
meets e only in its final edge, at c_e.

The contact interval of f lies strictly later, so c_f is absent from this prefix. The other non-v vertex of f is absent from V(P) minus h by contact multiplicity one and absent from h by linearity, since f and h already meet at v. Thus f is disjoint from the prefix. Also e and f meet only at v.

Consequently
  g_1,...,g_{a(c_e)},e,f
is a linear path of length a(c_e)+2 ending in f through the terminal v.

The unique entrance y of f is absent from the preceding path. If c_f=y, this follows from the strict interval order; if c_f is the opposite terminal, then y is the other non-v vertex of f and is absent from P. In either case y is not in e because e and f already meet at v.

Since f is nonspecial of edge rank s, a path of length s ending in f must enter through its unique entrance y. Hence the displayed wrong-entrance path has length at most s-1:
  a(c_e)+2<=s-1,
which proves (2).

Combining (1) and (2) gives
  p-r+1<=s-3,
or
  r+s>=p+4.