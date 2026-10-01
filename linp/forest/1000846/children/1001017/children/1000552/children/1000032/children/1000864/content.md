# Distance-two private clean entrance contacts are incompatible

## Statement

Let P=(g_1,...,g_p) be a maximum p-edge linear path ending at v, with last edge h=g_p. Let e={x,v,u} and f={y,v,z} be distinct ascending nonspecial edges, neither equal to h. Assume:
- e meets V(P)\h in exactly one vertex, namely its entrance x;
- f meets V(P)\h in exactly one vertex, namely its entrance y;
- x is private to g_j and y is private to g_{j+2}, for some 1<=j<=p-3.

Then this configuration is impossible.

## Body

Because e meets P outside h only at x, and e and h both contain v, linearity gives e∩h={v}. Likewise f∩h={v}.

Consider the sequence
  g_1,...,g_j,e,h,g_{p-1},g_{p-2},...,g_{j+2}.
The prefix and reversed suffix are separated in the original path by the omitted edge g_{j+1}, hence every prefix edge is disjoint from every nonconsecutive suffix edge. The edge e meets the retained path only at x∈g_j and v∈h, so its only intersections in the displayed sequence are with its two consecutive neighbors g_j and h. Thus the displayed sequence is a linear path.

Its length is
  j + 1 + 1 + (p-1-(j+2)+1)
  = p.
Its last edge is g_{j+2}. Since y is private to g_{j+2}, y can be chosen as a last vertex. Hence
  phi(y)>=p.

But f is ascending with entrance y. Therefore
  phi(y)=phi(f)-1.
Since v is terminal for f, phi(f)<=phi(v)=p. Hence
  phi(y)<=p-1,
a contradiction.
