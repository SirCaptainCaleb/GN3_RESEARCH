# Longest directed paths force complementary source/rainbow endpoint degrees

## Statement

In the source-oriented setup above, suppose d_F(x)≥d for all x and let P=v_0v_1...v_p be a longest directed path in D. Then
h(v_0)≤p,   s(v_0)≥d-p,
s(v_p)≤p/2, h(v_p)≥d-p/2.

## Body

For the terminal vertex v_p, every out-neighbor lies on P, otherwise P extends. Since d_D^+(v_p)=2s(v_p) and P has only p other vertices,
2s(v_p)≤p.
Thus s(v_p)≤p/2, and s(v_p)+h(v_p)=d_F(v_p)≥d gives
h(v_p)≥d-p/2.

For the initial vertex v_0, take any H-edge v_0x colored u. The corresponding source triple gives an arc u→v_0 in D. If u were outside V(P), then
u,v_0,v_1,...,v_p
would be a directed path of length p+1, contradiction. Thus every color appearing at v_0 belongs to V(P)\{v_0}. Since H is properly edge-colored, incident H-edges at v_0 have distinct colors, so h(v_0)≤p. Then
s(v_0)=d_F(v_0)-h(v_0)≥d-p.