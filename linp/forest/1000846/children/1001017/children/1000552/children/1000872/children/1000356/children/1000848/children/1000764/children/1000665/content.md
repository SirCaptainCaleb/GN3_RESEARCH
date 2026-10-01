# At p=2q-3 terminal-only non-double witnesses are pushed to the left central slots

## Statement

Let phi(v)=2q-3 and fix a maximum v-ending path P. For a charged ascending edge through terminal v that is non-double on P: (i) if its rank is q and its entrance is absent, its opposite-terminal witness is forced to the unique joint g_{q-2}∩g_{q-1}; (ii) if its rank is q+1 and its entrance is absent, its opposite-terminal witness can occur only privately in g_{q-2} or g_{q-1}, or at one of the joints g_{q-3}∩g_{q-2}, g_{q-2}∩g_{q-1}, g_{q-1}∩g_q. In particular the private g_q slot and joint g_q∩g_{q+1} are entrance-only for non-double high edges.

## Body

Let v have
  p=phi(v)=2q-3,
and let
  P=(g_1,...,g_p)
be a maximum p-edge path ending at v. Consider an assigned charged ascending nonspecial edge
  e={x,v,u}
which is non-double on P, so exactly one of x,u lies on P outside the last edge.

(A) Rank q.

Assume phi(e)=q and the entrance x is absent. Then the selected path-relative witness is u. By 220a14637b5f, for rank q at path length p=2q-3:
- the only private witness position is g_{q-1};
- the only joint witness positions are
    g_{q-2} cap g_{q-1}
  and
    g_{q-1} cap g_q.

The private g_{q-1} position is impossible. If u is private in g_{q-1}, then
  g_1,...,g_{q-1},e
is a q-edge linear path ending in e through terminal u, with entrance x absent and therefore available as a last vertex. Since phi(e)=q and e is nonspecial with unique entrance x, this is a longest e-path with wrong entrance u, contradiction.

Likewise u cannot be the joint g_{q-1} cap g_q: the path
  g_1,...,g_{q-1},e
again has q edges and enters e through terminal u, contradiction.

Therefore the sole possible terminal-only witness of a non-double rank-q edge is
  u=g_{q-2} cap g_{q-1}.                              (1)

(B) Rank q+1.

Assume phi(e)=q+1 and x is absent. By 220a14637b5f, the possible witness positions before the wrong-entrance prefix restriction are:
- private positions g_{q-2},g_{q-1},g_q;
- joint positions
    g_{q-3} cap g_{q-2},
    g_{q-2} cap g_{q-1},
    g_{q-1} cap g_q,
    g_q cap g_{q+1}.

A terminal witness private in g_q is impossible, because
  g_1,...,g_q,e
has q+1 edges and enters e through terminal u, producing a longest e-path with wrong entrance.

The same argument excludes the joint g_q cap g_{q+1}: the prefix through g_q followed by e again has q+1 edges and enters e through u.

Hence a terminal-only non-double rank-(q+1) edge can use only
- private g_{q-2} or g_{q-1}, or
- one of the three joints
    g_{q-3} cap g_{q-2},
    g_{q-2} cap g_{q-1},
    g_{q-1} cap g_q.                                  (2)

Thus at p=2q-3 every terminal-only witness lies on the left side of the central window. In particular the private g_q slot and the right joint g_q cap g_{q+1}, when selected by a non-double rank-(q+1) edge, are necessarily visible entrances.
