# An early endpoint blocker forces opposite-endpoint prefix escape

## Statement

Let Q=(p_1,...,p_s) be a linear path with first edge p_1={u,v,c}, where u,v are the two free opposite endpoints. Let f={u,r,w} be an edge different from p_1 whose two non-u vertices lie in V(Q)\p_1. Let i be the first index >=2 of a path edge containing either r or w. Then
  C=(p_1,p_2,...,p_i,f)
is a linear cycle of length i+1.

Assume moreover that H has minimum degree at least delta. At the private cycle vertex v of p_1, classify edges h!=p_1 by the number 0,1,2 of vertices of h\{v} lying in V(C), and call the counts C_0,C_1,C_2. Then
  2C_0+C_1 >= 2delta-2i-1.

In particular, if i<=delta-2, at least three weighted units of the v-star escape the prefix cycle. In a two-hole wrong-entrance witness, every such escaping v-edge is a single/double blocker on the full path Q whose blocker set is not wholly contained in V(C); thus an early u-blocker quantitatively forces the opposite endpoint matching to send contacts beyond the same prefix.

## Body

By the definition of i, exactly one of r,w first appears on p_i and neither occurs on p_1,...,p_{i-1}. The other of r,w appears on p_i or later. If both lay in p_i, then f and p_i would share two vertices, impossible by linearity. Hence f meets the initial segment p_1,...,p_i only in u on p_1 and exactly one of {r,w} on p_i. Therefore p_1,...,p_i,f is a linear cycle of length i+1.

Within this cycle, p_1 meets p_2 at the usual path joint and f at u. Its third cycle vertex v is private to p_1.

Apply the certified private-vertex ear-surplus lemma 64823c8c54de to this cycle with c=i+1 and minimum degree delta. It yields
  2C_0+C_1 >= 2delta-2(i+1)+1
             = 2delta-2i-1.

If i<=delta-2, the right side is at least 3.

Finally, in the two-hole wrong-entrance setting, every edge through v other than p_1 is already known to be a single or double blocker on the full path Q. An edge counted by C_0 has no blocker contact in the initial cycle, while an edge counted by C_1 has at most one; in either case its full blocker data cannot be wholly contained in V(C). Hence the inequality measures forced escape of the opposite-endpoint star beyond the prefix.
