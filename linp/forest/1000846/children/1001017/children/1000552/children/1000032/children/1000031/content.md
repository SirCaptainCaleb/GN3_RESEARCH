# A clean private entrance forbids every private single contact two positions earlier

## Statement

Let P=(g_1,...,g_p) be a maximum p-edge linear path ending at v with last vertex v, with last edge h=g_p. Let e and f be distinct ascending nonspecial edges through v, neither equal to h.

Assume e meets V(P)\\h in exactly one vertex r, private to g_j (r may be either the entrance or the opposite terminal of e). Assume f meets V(P)\\h in exactly one vertex y, where y is the unique entrance of f and is private to g_{j+2}. Then this configuration is impossible.

## Body

Because e has exactly one precursor contact r and also contains v, while h contains v, linearity gives e∩h={v}. The same holds for f and h. The edge e meets the retained precursor path only in r∈g_j.

Consider
  g_1,...,g_j,e,h,g_{p-1},g_{p-2},...,g_{j+2}.

The omitted edge g_{j+1} separates the prefix and reversed suffix, so inherited nonconsecutive path intersections do not occur. The edge e meets the displayed path only at its consecutive neighbors g_j and h. Hence this is a linear p-edge path.

Its last edge is g_{j+2}. Since y is private to g_{j+2}, y is a last vertex, so phi(y)>=p.

But y is the unique entrance of the ascending edge f. Hence
  phi(y)=phi(f)-1.
Since v is terminal for f,
  phi(f)<=phi(v)=p,
so phi(y)<=p-1, contradiction.

No label assumption on the earlier unique contact r was used.
