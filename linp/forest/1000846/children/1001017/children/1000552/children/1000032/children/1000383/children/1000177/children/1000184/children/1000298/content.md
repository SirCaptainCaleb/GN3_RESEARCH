# A right-joint high entrance pushes the low terminal to the first path edge

## Statement

In the top-boundary q,(q+1)^3 setup, suppose the right joint d=g_q∩g_{q+1} is a visible rank-(q+1) entrance, so phi(d)=q. If the low rank-q edge's opposite terminal u occurs in the left prefix, then u is forced to be private in g_1. More generally, if j is its last occurrence index, the rotation g_1,...,g_j,e,g_p,...,g_{q+1} gives phi(d)>=j+q-1, hence j<=1.

## Body

Use the top-boundary notation:
  p=2q-2,
  P=(g_1,...,g_p) ending physically at v,
  e={x,v,u} rank q with x=g_{q-1} cap g_q,
and let
  d=g_q cap g_{q+1}
be the right-joint slot.

Assume d is the unique entrance of a rank-(q+1) charged competitor, so phi(d)=q.

Suppose u occurs in the left prefix g_1,...,g_{q-2}. Let j be the last path-edge index containing u. Because e and g_{q-1} already share x, linearity forbids u from lying in g_{q-1}; hence j<=q-2.

Consider
  g_1,...,g_j, e, g_p,g_{p-1},...,g_{q+1}.

This is a linear path. The prefix and reversed suffix are separated in P by the omitted central block. The prefix meets e only at its final u-contact: x is central and v is absent, while last-occurrence choice omits any second u-edge. The reversed suffix meets e only at v in g_p: x lies in g_{q-1},g_q and u has no occurrence after j. Thus all nonconsecutive intersections are absent.

The suffix g_p,...,g_{q+1} has p-q=q-2 edges. Hence the path has length
  j + 1 + (q-2) = j+q-1.

Its final edge is g_{q+1}. The vertex d belongs to g_{q+1} but not to its predecessor g_{q+2} when present, and d is not in e; for q=3 the final edge is g_p and e meets it at v, again d is a valid physical last vertex. Therefore
  phi(d) >= j+q-1.

Since d is an ascending rank-(q+1) entrance,
  phi(d)=q.
Thus j<=1.

Consequently, if the low opposite terminal u occurs in the left prefix at all while d is a visible high entrance, its last occurrence is on g_1. Since a joint g_1 cap g_2 would have last occurrence 2, u must in fact be private in g_1.
