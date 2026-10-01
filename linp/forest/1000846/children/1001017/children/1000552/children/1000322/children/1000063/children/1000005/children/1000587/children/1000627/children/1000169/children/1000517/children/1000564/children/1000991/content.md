# A two-hole collision across one omitted cell gives the full wrong-entrance lift

## Statement

Let Q=(p_1,...,p_s) be a linear 3-uniform path ending at a prescribed last vertex x, and let a,b lie outside V(Q). Suppose
  f={a,r,w},  g={b,w,t}
are edges, where r,w,t are distinct vertices of V(Q). Let
  i=max{j:r∈p_j},  k=min{j:t∈p_j}.
Assume
  i+2=k,
and every path edge containing w has index strictly between i and k.

Then
  (p_1,...,p_i,f,g,p_k,...,p_s)
is a linear path of length s+1 ending at x.

Consequently, in a two-hole alternate wrong-entrance witness Q of length ell-2, such a configuration yields an (ell-1)-edge path ending in the fixed nonspecial edge through the same wrong entrance, a contradiction.

## Body

Because i is the last index containing r, f meets the retained prefix p_1,...,p_i only at r in p_i. Because every occurrence of w lies strictly between i and k, f has no other retained-prefix or retained-suffix contact through w.

Similarly, since k is the first index containing t, g meets the retained suffix p_k,...,p_s only at t in p_k; its w-contact lies entirely in the omitted interval.

The edges f and g meet exactly at w. They cannot share any second vertex by linearity. Since k=i+2, the retained path edges p_i and p_k are nonconsecutive in Q and therefore disjoint. All other nonconsecutive intersections are inherited from Q, while the only new consecutive intersections are
  p_i∩f={r}, f∩g={w}, g∩p_k={t}.
Hence the displayed sequence is a linear path.

Its length is
  i+2+(s-k+1)=s+3-(k-i)=s+1.
The suffix through p_s is unchanged, so the prescribed last vertex x is preserved.

For an alternate wrong-entrance witness of length s=ell-2, the resulting path has length ell-1 and the same final edge/entrance carried by the unchanged suffix. This contradicts uniqueness of the entrance of the nonspecial top-rank edge.