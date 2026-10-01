# Terminal defect accounting and opposite-terminal splice dichotomy

## Statement

In the setting of the two-terminal alternating blocker system of 765d552ff81d, for each terminal v in {y,z}, 2L-2-2B_v=S_v+U_v and 2d_H(v)=2L+S_v-U_v; hence S_y+S_z+U_y+U_z=2p and d_H(y)+d_H(z)=2L+S_y+S_z-p, where p is the number of alternating path components. Moreover, for opposite-terminal single blockers f_y,f_z with first/last blocker positions j<k<=L-2: if they intersect then f_y,e,f_z form a linear 3-cycle; if disjoint and k>=j+2 there is an exact bridge splice of length L+2-(k-j); if disjoint and k=j+1 then at least one blocker is the joint g_j∩g_{j+1}.

## Body

Fix W=V(P)\e in the setting of 765d552ff81d. For a terminal v, the B_v double blockers use 2B_v vertices of W in disjoint pairs. The S_v single blockers use S_v further vertices, disjoint from those pairs and from one another by linearity. If U_v vertices of W are unused by the v-star, then
2L-2-2B_v=S_v+U_v.
Summing over y,z and using p=(2L-2)-(B_y+B_z) yields
S_y+S_z+U_y+U_z=2p.
Equivalently, the 2p endpoint incidences of the alternating path components are exactly the color-defects: unmatched in color v means occupied by one single blocker through v or unused by that terminal star.

No edge f≠e through a terminal v can avoid W, since otherwise it could be appended after the globally longest path. Thus
d_H(v)=1+S_v+B_v.
Substituting the defect identity gives
2d_H(v)=2L+S_v-U_v,
and summing gives
d_H(y)+d_H(z)=2L+S_y+S_z-p.
Hence degree above the baseline L is carried exactly by an excess of single-blocker defects over unused defects.

Now let f_y,f_z be single blockers through y,z with blocker vertices w_y,w_z. Let j be the first precursor edge containing w_y and k the last precursor edge containing w_z, with j<k<=L-2. If f_y and f_z intersect, linearity forces one intersection outside e and the three edges f_y,e,f_z form a linear 3-cycle.

Assume they are disjoint. If k>=j+2, first/last occurrence minimality implies any second occurrence of w_y can only lie in g_{j+1}, and any other occurrence of w_z can only lie in g_{k-1}; these lie in the omitted middle. Therefore
(g_1,...,g_j,f_y,e,f_z,g_k,...,g_{L-2})
is linear and has length L+2-(k-j). In particular k=j+2 gives another globally longest L-edge path.

If k=j+1 and neither blocker vertex is the joint g_j∩g_{j+1}, the same intersection check gives an (L+1)-edge linear path, contradicting maximality. Thus at least one blocker is forced onto the common joint. These alternatives exhaust the opposite-terminal single-defect geometry.
