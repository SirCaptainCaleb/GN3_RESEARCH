# Equality at density plus one gives an exact three-special-edge blocker normal form

## Statement

Assume equality in c77c818cf1e9:
  average(phi)=m/n+1.
Fix a vertex v with p=phi(v), and let
  P=(g_1,...,g_p)
be any maximum p-edge path ending at v, with h=g_p.

Then:
(1) v lies in exactly three special edges;
(2) if h is nonspecial, then among the 2p-4 tail vertices
    T=(V(g_2 union ... union g_{p-1}))\V(h),
    exactly one is not used as the blocker witness of a nonspecial terminal edge through v; the three special edges through v meet P outside v exactly once each, at the two free vertices of g_1 and at that unique unused tail vertex;
(3) if h is special, then every vertex of T is used by a nonspecial terminal edge through v, and the other two special edges through v meet P outside v exactly once each, at the two free vertices of g_1.

In either case at least two special edges through v have rank p. Consequently all three special edges through v have rank exactly p.

## Body

Equality in c77c818cf1e9 forces equality in both steps
  (1/2)A+B >= (1/2)(A+B) >= n/2.
Hence B=0 and A+B=n. Since every local a(v)+b(v)>=1 and all local slacks are nonnegative integers, for every vertex
  b(v)=0, a(v)=1.
Thus
  d_D^-(v)=2p-1,
  t_ns(v)=2p-4.
The number of special snake incidences at v is therefore
  d_D^-(v)-t_ns(v)=3,
proving (1).

Now fix a maximum p-edge path P ending at v.

The cumulative nonspecial-terminal proof 0e550ff0eadd injects all nonspecial terminal edges through v except a possible last edge h into the 2p-4 tail vertices T.

If h is nonspecial terminal, then 2p-5 remaining nonspecial terminal edges inject into T, leaving exactly one tail vertex unused. If h is not nonspecial terminal, then all 2p-4 nonspecial terminal edges inject into T, hence bijectively fill T.

Every special edge f through v other than h must meet P outside v; otherwise P followed by f is a (p+1)-edge path ending in f, contradicting phi(f)<=phi(v)=p. By linearity f cannot use a tail vertex already used by a nonspecial terminal edge through v, and cannot use another vertex of h.

Therefore:
- when h is nonspecial, the only available P-contacts are the two free vertices of g_1 and the unique unused tail vertex. There are three special edges, each needing a distinct contact, so they use these three vertices bijectively, exactly once each;
- when h is special, all tail vertices are occupied, and the two other special edges must use the two free vertices of g_1, again one each.

Any special edge f using a free vertex of g_1 and no other P-contact gives a linear path
  (g_2,...,g_p,f)
of length p ending in f. Hence phi(f)>=p, while phi(f)<=phi(v)=p, so phi(f)=p.

Thus at least two of the three special edges through v have rank p.

Choose one such rank-p special edge f. Since f is special and v is a terminal for f, there is a maximum p-edge path ending at v with last edge f. Apply the special-last case above to that path. The other two special edges through v then occupy the two far free vertices and therefore also have rank p. Hence all three special edges through v have rank p.
