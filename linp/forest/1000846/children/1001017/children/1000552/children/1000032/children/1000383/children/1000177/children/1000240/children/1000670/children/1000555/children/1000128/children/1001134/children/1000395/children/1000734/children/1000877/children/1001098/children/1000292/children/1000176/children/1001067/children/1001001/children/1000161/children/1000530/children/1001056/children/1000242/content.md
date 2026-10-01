# Reciprocal V-type terminal-single edges close a canonical terminal cycle

## Statement

Let e={x,v,u} be an ascending nonspecial edge of rank r with terminals v,u. Let
  P=(g_1,...,g_s)
be a maximum endpoint path ending at u, with s=phi(u)>r. Assume e is terminal-single on P and its unique off-u contact with the precursor is the other terminal v (reciprocal type V).

Let b be the last path-edge index for which v lies in g_b. Then
  e,g_b,g_{b+1},...,g_s
is a linear cycle of length
  s-b+2.
Consequently
  s-b+2 <= r,
or equivalently
  b >= s-r+2.

Thus every reciprocal V-type strict-gap edge carries a canonical terminal cycle containing e, cut from the final segment of its opposite-terminal maximum path.

## Body

Because s>r=phi(e), the edge e is not the last edge g_s of P. The last vertex u belongs to g_s. By linearity, v cannot also belong to g_s, since then the distinct edges e and g_s would share both u and v. Hence b<s.

Choose b as the last index of a path edge containing v. Then among the suffix
  g_b,g_{b+1},...,g_s,
the edge e meets g_b at v and meets g_s at u. It meets no intermediate suffix edge: terminal-singleness says v is the unique off-u vertex of e occurring on the precursor, x is absent from P, and by the choice of b the vertex v has no occurrence after g_b. Thus
  e,g_b,g_{b+1},...,g_s
has exactly the intended cyclic consecutive intersections at v, the usual path joints, and u, with no other pairwise intersections. It is a linear cycle.

The suffix contains s-b+1 path edges, so the cycle length is s-b+2. Since e is nonspecial of rank r, the certified cycle-rank theorem f2925a904b8e gives
  s-b+2<=r.
Rearranging yields b>=s-r+2.

The statement is independent of payment, common-anchor structure, or minimum-terminal assignment.
