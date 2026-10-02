# The d-free abc top-boundary pattern also has a crossed blocker moat

## Statement

Assume q>=4 and the all-visible top-boundary q,(q+1)^3 configuration with occupied high entrances
  a=g_{q-2}∩g_{q-1},
  b=private(g_{q-1}),
  c=private(g_q),
while d=g_q∩g_{q+1} is unoccupied.
Write
  h_a={a,v,z_a}, h_b={b,v,z_b}, h_c={c,v,z_c}.

Then
  z_a,z_b ∈ V(g_{q+1}∪...∪g_{2q-3}),
and
  last_P(z_c)<=q-4.

Thus abc also has a genuine two-right/one-left terminal split across the central block. In particular no opposite terminal of an occupied high edge lies in g_{q-1}∪g_q.

## Body

By eddd8ad49835, every occupied left-central entrance y∈{a,b} sends its opposite terminal across the cut:
  z_a,z_b ∈ V(g_q∪...∪g_{2q-3}).

For z_a, 4b2eb2497cf0 sharpens this to
  z_a∉g_q,
hence z_a lies in g_{q+1},...,g_{2q-3}.

For z_b, the only possible occurrence in g_q would be d, since
  g_q={x,c,d},
and linearity excludes x because h_b and the low edge e share v, while it excludes c because h_b and h_c share v.
Suppose z_b=d. Then consider
  g_1,...,g_{q-2}, h_a, h_b, g_{q+1}.
Here g_{q-2} meets h_a at a; h_a,h_b meet at v; h_b meets g_{q+1} at d. The omitted edges g_{q-1},g_q separate the retained path pieces. Also z_a lies strictly in the right suffix. If z_a occurs in g_{q+1}, the displayed splice is blocked; choose instead its first occurrence index k and retain the reverse suffix from g_k after h_a,h_b. The exact bridge count gives a q-edge path ending at x unless k is beyond the central moat. In all cases the rank-q entrance bound forces k>=q+1 and rules out z_b=d as the unique central escape. [This last elimination requires the bridge-count subcase to be checked before certification.]

Independently, apply the ac conflict in 872bb5f4effc. Since z_a is absent from the left prefix and from g_q, its second alternative is impossible, so
  z_c∈V(g_1∪...∪g_{q-2}).
Let j be its last occurrence. Because z_a lies on the right,
  g_1,...,g_j,h_c,h_a,g_{q-1}
is linear, has length j+3, and ends physically at
  x=g_{q-1}∩g_q.
Therefore
  j+3<=phi(x)=q-1,
so j<=q-4.