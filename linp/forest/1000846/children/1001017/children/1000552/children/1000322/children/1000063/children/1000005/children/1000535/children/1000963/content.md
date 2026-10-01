# High terminal degree forces outside single-blocker expansion

## Statement

Let P be a globally longest L-edge path ending in a maximum-rank nonspecial edge e, and let v be a terminal vertex of e. If S_v is the number of incident terminal edges that meet the precursor in exactly one vertex, then S_v>=2d(v)-2L and S_v<=|V(H)\\V(P)|. Hence d(v)<=L+|V(H)\\V(P)|/2. For the two terminals y,z, S_y+S_z>=2d(y)+2d(z)-4L>=4delta(H)-4L.

## Body


Let H be a finite linear 3-uniform hypergraph with global maximum path length L. Let
  P=(g_1,...,g_{L-1},e)
be a globally longest path ending in a nonspecial edge e={x,y,z}, entered through x, so y,z are terminal vertices of e. Put
  W=V(P)\e,
so |W|=2L-2, and let O=V(H)\V(P).

Fix a terminal v in {y,z}. Every edge f!=e through v must meet W. Otherwise f meets P only at v (its two other vertices lie outside V(P)), and P,f is an (L+1)-edge linear path, impossible.

Because H is linear, the off-v pairs f\{v} over edges f!=e through v are pairwise disjoint. Classify them as:
- double blockers, with both off-v vertices in W;
- single blockers, with exactly one off-v vertex in W and one in O.
Let B_v,S_v be their counts. Then
  B_v+S_v=d_H(v)-1.
Their contacts in W are all distinct, so
  2B_v+S_v <= |W|=2L-2.
Substituting B_v=d_H(v)-1-S_v gives
  2d_H(v)-2-S_v <= 2L-2,
hence
  S_v >= 2d_H(v)-2L.
Since distinct single blockers through v use distinct outside vertices, also
  S_v <= |O|.

Therefore
  2d_H(v)-2L <= S_v <= |O|.
Equivalently
  d_H(v) <= L + |O|/2.

For both terminals,
  S_y+S_z >= 2d_H(y)+2d_H(z)-4L >= 4delta(H)-4L.
Thus a maximum-rank nonspecial edge in a high-minimum-degree hypergraph necessarily emits many terminal single blockers whenever delta(H) is close to or exceeds L.

The conclusion is a structural dichotomy rather than yet the desired 3delta<=2L+2 inequality: a maximum-rank nonspecial obstruction with few outside vertices is forced toward double-blocker saturation and alternating cycles, while one with substantial terminal degree relative to L must have a proportionally large family of single blockers into outside vertices. Those single blockers are the natural endpoint-expansion/rotation resources.
