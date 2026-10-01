# Longest-path terminal degree with exact double-blocker slack

## Statement

Let P=(e_1,...,e_L) be a globally longest linear 3-uniform path with last vertex z in e_L, and let B_P(z) count incident edges f≠e_L whose two non-z vertices both lie in V(P)\e_L. Then
  d_H(z)+B_P(z) <= 2L-1.
In particular d_H(z)<=2L-1, so every linear 3-graph of minimum degree delta has a path of length at least ceil((delta+1)/2).

## Body

Every edge f≠e_L through z must meet V(P)\e_L; otherwise it could be appended to P. By linearity it meets e_L only at z, and distinct such f use disjoint blocker vertices outside z. An incident edge using one blocker consumes one vertex of V(P)\e_L; a double blocker consumes two. Thus the total number of blocker vertices used is exactly
  (d_H(z)-1)+B_P(z).
Since a 3-uniform L-edge linear path has 2L+1 vertices and e_L contributes three, |V(P)\e_L|=2L-2. Hence
  (d_H(z)-1)+B_P(z)<=2L-2,
which rearranges to the claimed slack inequality.

Dropping B_P(z)>=0 recovers d_H(z)<=2L-1. If H has minimum degree delta, a longest path therefore satisfies delta<=2L-1 and L>=ceil((delta+1)/2). The sharpened form records exactly how every double blocker consumes one additional unit of the terminal blocking budget beyond the ordinary degree count.
