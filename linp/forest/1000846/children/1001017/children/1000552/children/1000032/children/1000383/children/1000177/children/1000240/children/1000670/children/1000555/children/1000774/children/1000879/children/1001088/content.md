# A later terminal-only contact is bounded from the right by the earlier edge rank

## Statement

Let P=(g_1,...,g_p) be a maximum path ending at v. Let e,f be ascending nonspecial terminal-only single-contact edges through v with entrances absent from P. If the last occurrence index of e's terminal contact is smaller than that of f's, then the later contact satisfies l_f>=p-phi(e)+3. This is the reversed-coordinate companion to df8ad4c65be0.

## Body


Let P=(g_1,...,g_p) be a maximum p-edge path ending at v, with h=g_p. Let
  e={x,v,u},  f={y,v,z}
be distinct ascending nonspecial edges, neither equal h, such that relative to V(P)\V(h):
- e has exactly one contact u, its opposite terminal, and entrance x is absent;
- f has exactly one contact z, its opposite terminal, and entrance y is absent.

Let l_u be the last path-edge index containing u and l_z the last path-edge index containing z. Suppose l_u<l_z.

Because l_z is the last occurrence of z, the reversed suffix
  g_{p-1},g_{p-2},...,g_{l_z}
contains z only in its final edge. Since l_u<l_z, the terminal contact u of e is absent from this suffix. The entrances x,y are absent from P by hypothesis. Hence
  g_{p-1},...,g_{l_z},f,e
is a linear path: the reversed suffix is inherited from P; its final edge meets f at z; f meets e at v; e is disjoint from the suffix because its only precursor contact u lies earlier; and f has no other precursor contact.

The number of suffix edges is p-l_z, so the displayed path has length p-l_z+2. It ends in e and enters e through v, which is a terminal label; the unique entrance x is absent from all preceding edges and can be chosen as the last vertex of e.

Since e is nonspecial of rank q_e=phi(e), a path of length q_e entering e through terminal v would already give a second entrance label, and a longer path would exceed the rank. Therefore
  p-l_z+2 <= q_e-1,
hence
  l_z >= p-q_e+3.

Thus, in last-occurrence coordinates: if one terminal-only contact lies strictly later than another, the later contact has last occurrence at least p minus the earlier edge rank plus three.
