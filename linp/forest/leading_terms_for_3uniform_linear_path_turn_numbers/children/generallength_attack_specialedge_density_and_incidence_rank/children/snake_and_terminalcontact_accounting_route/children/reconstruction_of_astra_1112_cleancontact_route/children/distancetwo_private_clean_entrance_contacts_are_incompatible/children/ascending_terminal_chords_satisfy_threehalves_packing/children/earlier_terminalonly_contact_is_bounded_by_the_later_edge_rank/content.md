# An earlier terminal-only contact is bounded by the later edge rank

## Statement

Let P=(g_1,...,g_p) be a maximum p-edge path ending at v, with h=g_p. Let e={x,v,u} and f={y,v,z} be distinct ascending nonspecial edges, neither equal h, such that relative to V(P)\V(h), e has exactly one contact u (its opposite terminal) with x absent, and f has exactly one contact z with y absent. Let j be the first path-edge index containing u and k the first path-edge index containing z, with j<k. If q_f=phi(f), then
  j <= q_f-3.

The reversed-path analogue is valid when formulated using the last occurrence index of the earlier/later terminal contact; no unconditional first-index reciprocal inequality is asserted.

## Body

Because e has no P-contact outside h except u, the prefix g_1,...,g_j meets e only at its final contact u; if u is a joint, the second path edge containing u is g_{j+1}, which is omitted. Since f's sole P-contact z first occurs later at k>j, f is disjoint from g_1,...,g_j. Also e∩f={v} by linearity, and y is absent from P.

Hence
  (g_1,...,g_j,e,f)
is a linear path of length j+2. Its last edge f is entered through v, a terminal label of f, while its unique entrance y is a last vertex because y occurs in no preceding edge.

If j+2>q_f=phi(f), this exceeds the rank of f. If j+2=q_f, it is a longest f-ending path entering through the terminal v rather than the unique entrance y. Both are impossible. Therefore
  j+2<=q_f-1,
so j<=q_f-3.

Applying the same argument to a reversed path segment gives a reciprocal restriction in last-contact coordinates. Because a joint terminal may occupy two consecutive path edges, translating that reciprocal statement into first-contact coordinates incurs a one-step correction; we deliberately do not include such a first-index bound in the theorem statement.