# Separated mixed singleton contacts force rank sum at least host rank plus four

## Statement

Let P=(g_1,...,g_p) be a maximum p-edge path with last vertex v and last edge h=g_p. Let
  e={x,v,u},  f={y,v,z}
be distinct ascending nonspecial edges, neither equal to h, that are terminal at v and each have exactly one off-v contact with V(P)\h.

For a contact vertex c on P\h, let I(c)=[a(c),b(c)] be the interval of path-edge indices containing c. Suppose the two contact intervals are disjoint, with
  b(c_e) < a(c_f).
If at least one of the two contacts is the opposite terminal of its edge rather than its unique entrance, then
  phi(e)+phi(f) >= p+4.

Thus any pair of singleton ascending terminal edges with disjoint ordered contact intervals and rank sum at most p+3 must have both contacts equal to their unique entrances.

## Body

Write r=phi(e) and s=phi(f).

First suppose the earlier contact c_e is the opposite terminal u of e. The singleton central-window bounds give
  a(c_e) >= p-r+1.
We claim also
  a(c_e) <= s-3.
Indeed, because c_e is the only off-v contact of e with P\h, the prefix
  g_1,...,g_{a(c_e)}
meets e only in its final edge; if c_e is a joint, its second occurrence is on the omitted next path edge. Since the contact interval of f lies strictly later, f is disjoint from this prefix. Also e and f meet only at v by linearity. Therefore
  g_1,...,g_{a(c_e)},e,f
is a linear path of length a(c_e)+2 ending in f through the terminal v. The unique entrance y of f is absent from the preceding path: if c_f=y then it lies strictly later on P, while if c_f=z then y is absent from P altogether. Hence a path of length s ending in f would use a wrong entrance, and a longer one would exceed the edge rank. Thus
  a(c_e)+2 <= s-1,
so a(c_e)<=s-3. Combining the two inequalities gives
  p-r+1 <= s-3,
hence r+s>=p+4.

Now suppose instead that the later contact c_f is the opposite terminal z of f. The terminal-only singleton bound gives
  a(c_f) <= s-2,
and because a path vertex belongs to at most two consecutive path edges,
  b(c_f) <= s-1.
We claim
  b(c_f) >= p-r+3.
Consider the reversed suffix
  g_{p-1},g_{p-2},...,g_{b(c_f)},f,e.
The edge h=g_p is omitted. By the choice of b(c_f), the suffix meets f only in its final edge at z. Since the contact interval of e lies strictly earlier, e has no contact with the suffix; moreover its unique entrance x is absent from the suffix, whether x=c_e or x is absent from P. Again f and e meet only at v. Hence the displayed sequence is a linear path of length
  p-b(c_f)+2
ending in e through the terminal v. Nonspecialness of e therefore gives
  p-b(c_f)+2 <= r-1,
or b(c_f)>=p-r+3. Combining with b(c_f)<=s-1 yields r+s>=p+4.

If both contacts are terminal-only, either argument applies. No source-clean hypothesis, opposite-terminal single-contact hypothesis, minimum-terminal orientation, paid certificate, or near-extremal assumption is used.