# Quantitative separation between an earlier single blocker and a later clean entrance

## Statement

Let P=(g_1,...,g_p) be a maximum p-edge path ending at v, with last edge h=g_p. Let e and f be distinct ascending nonspecial edges through v, neither equal h. Assume e has exactly one contact vertex r in V(P)\h, and let j be the first path-edge index containing r.

Assume f also has exactly one contact vertex on P, namely its unique entrance y.

(a) If y is private to g_k and k>=j+2, then
  k-j >= p-phi(f)+3.

(b) If y=g_k∩g_{k+1} is a joint and k>=j+1, then
  k-j >= p-phi(f)+2.

## Body

Write q=phi(f), so phi(y)=q-1 because f is ascending.

For (a), consider
  g_1,...,g_j,e,h,g_{p-1},g_{p-2},...,g_k.
The omitted interval starts with g_{j+1}; because k>=j+2, the retained prefix and suffix have no inherited nonconsecutive intersections. If r is a joint of g_j,g_{j+1}, the second edge containing r is omitted, so e meets the retained path only at its consecutive neighbors g_j and h. Since e and h both contain v, e∩h={v}; and f being distinct from e,h ensures its entrance y is not in e or h by linearity. Thus the displayed sequence is linear and ends at y.

Its length is
  j+2+(p-k)=p+j-k+2.
Hence
  p+j-k+2 <= phi(y)=q-1,
which rearranges to
  k-j >= p-q+3.

For (b), use instead
  g_1,...,g_j,e,h,g_{p-1},...,g_{k+1}.
The edge g_k is omitted, so y=g_k∩g_{k+1} occurs only in the final edge and is an endpoint. The same separation argument gives linearity. The length is
  j+2+(p-k-1)=p+j-k+1.
Thus
  p+j-k+1 <= q-1,
so
  k-j >= p-q+2.