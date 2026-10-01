# A terminal-retained strict-gap edge forces a cycle, a forward return, or a flat shared last edge

## Statement

Let e={x,v,u} be an ascending nonspecial edge with unique entrance x and edge rank q. Let
  P=(g_1,...,g_p)
be a maximum endpoint path with last vertex v such that u belongs to V(P) and x does not. Assume
  q<p<=phi(u).

Choose a maximum endpoint path
  Q=(f_1,...,f_s)
with last vertex u, where s=phi(u). Suppose e is single-contact at u on Q.

Then at least one of the following holds.

(C) P union Q contains a linear cycle.

(R) The last edge h=f_s of Q is an internal edge g_j of P, and Q has a common vertex with the forward suffix
  g_{j+1},...,g_p
outside V(h).

(H) The last edge h=f_s equals an internal edge g_j of P, Q enters h through the forward joint
  z=g_j intersect g_{j+1},
and either
  phi(h)>p
or
  V(h) subseteq {w:phi(w)>=p}.

(F) One has s=p, h=g_j is nonspecial ascending of edge rank p, its unique entrance is
  z=g_j intersect g_{j+1},
and phi(z)=p-1.

Thus, after excluding cycles, further forward intersections, edge-rank rise, and host edges contained in V_{>=p}, the only remaining shared-last-edge state is the flat rank-p ascending orientation.

## Body

By a959e02faa1b, P and Q have at least two common vertices. Apply 41100a9882dd with endpoint u of Q lying on P. Either P union Q contains a linear cycle, giving (C), or the last edge h=f_s of Q is an edge of P. Since u is a last vertex of Q, u belongs to h. The edge h cannot be g_p: both e and g_p contain v, while u belongs to e; if u also belonged to g_p, the distinct edges e and g_p would share u and v, contrary to linearity. Hence h=g_j for some j<p.

Let
  z=g_j intersect g_{j+1}
be the forward joint of P at h, and let w be the vertex through which Q enters its last edge h.

Suppose w is not z. If Q had no common vertex with the suffix g_{j+1},...,g_p outside V(h), then
  f_1,...,f_s,g_{j+1},...,g_p
would be a linear path: the only inherited intersection between h and the suffix is z; because w!=z, the penultimate edge f_{s-1} does not contain z, and by assumption no earlier edge of Q meets the suffix outside h. This path ends at v and has length
  s+(p-j)>p,
since s>=p and j<p. This contradicts phi(v)=p. Therefore (R) holds.

It remains to consider w=z. The path Q shows
  phi(h)>=s>=p.
If phi(h)>p, outcome (H) holds. Hence suppose phi(h)=p. Then s=p as well, because p<=s<=phi(h)=p. Thus Q is a longest path ending in h and enters h through z.

If h is special, every vertex of h is terminal at h, so each has vertex rank at least phi(h)=p; hence V(h) is contained in V_{>=p}, giving (H).

Suppose h is nonspecial. Since Q is a longest h-ending path entering through z, z is the unique entrance of h. The other two vertices are terminal at h and therefore have vertex rank at least p. Also Q without h is a (p-1)-edge path ending at z, so phi(z)>=p-1.

If phi(z)>=p, then all three vertices of h have vertex rank at least p, giving (H). Otherwise phi(z)=p-1. By definition, h is then ascending, and we are in (F).
