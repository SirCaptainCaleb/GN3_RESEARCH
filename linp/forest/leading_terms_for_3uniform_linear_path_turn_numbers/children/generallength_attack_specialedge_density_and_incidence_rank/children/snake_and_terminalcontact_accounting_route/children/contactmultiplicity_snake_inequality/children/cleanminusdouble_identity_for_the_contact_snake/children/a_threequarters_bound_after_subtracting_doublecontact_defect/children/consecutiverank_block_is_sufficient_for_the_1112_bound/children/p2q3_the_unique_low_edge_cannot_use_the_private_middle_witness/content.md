# At p=2q-3 the unique low edge cannot use the private middle witness

## Statement

Let p=phi(v)=2q-3 with q>=4 and fix a maximum p-edge path P=(g_1,...,g_p) ending at v. Suppose four assigned charged ascending edges of ranks in {q,q+1} are all single-contact on P, with exactly one rank-q edge e.

Use
 A=g_{q-3}∩g_{q-2},
 B=private(g_{q-2}),
 C=g_{q-2}∩g_{q-1},
 D=private(g_{q-1}),
 E=g_{q-1}∩g_q.

Then the rank-q edge cannot have witness D.

## Body

If the rank-q edge has witness D, terminal-only rank-q localization shows D must be its visible unique entrance. Thus
  e={D,v,u}
with phi(D)=q-1 and u absent from P.

First A cannot be occupied by another single-contact edge. Apply 65894e91ed50(a) with the earlier A-contact, whose first path-edge index is j=q-3, and the later clean private entrance D on g_{q-1}, so k=q-1. The required separation is
  k-j >= p-q+3 = q,
whereas k-j=2. Since q>=4, contradiction. Hence A is empty.

By f378e6022301/8d1adea102fe the four all-single contacts are confined to A,...,E, so with A empty the remaining three contacts are B,C,E. In particular B is occupied by a rank-(q+1) high edge h_B (the unique rank-q edge is e).

Because h_B is single-contact and B is private to g_{q-2}, the sequence
  g_1,...,g_{q-2}, h_B, e
is linear: h_B meets the prefix only at B; h_B∩e={v}; and e's only P-contact is its entrance D on the omitted edge g_{q-1}. Its length is
  (q-2)+2=q.
It ends in e through terminal v, while D is a last vertex of e. Since e is nonspecial of rank q with unique entrance D, this is a longest e-path with the wrong entrance label v, contradiction.

Therefore the unique rank-q edge cannot occupy D.