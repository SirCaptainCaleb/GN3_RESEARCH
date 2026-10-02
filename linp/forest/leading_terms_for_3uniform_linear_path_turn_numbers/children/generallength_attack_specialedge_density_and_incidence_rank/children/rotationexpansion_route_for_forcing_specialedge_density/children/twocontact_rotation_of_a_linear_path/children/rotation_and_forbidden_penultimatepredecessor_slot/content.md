# Single-blocker rotation and forbidden penultimate-predecessor slot

## Statement

Let P=(e_1,...,e_L) be a linear path with last vertex z in e_L, and let f∉P contain z. Suppose f has exactly one further vertex w on V(P)\e_L. Let j be the first index of a path edge containing w. Then if j<=L-2, the sequence (e_1,...,e_j,f,e_L,e_{L-1},...,e_{j+2}) is an L-edge linear path; if j=L-1, then (e_1,...,e_{L-1},f) is an L-edge linear path. If moreover P is globally longest, e_L is nonspecial with unique entrance x, and z≠x is a terminal vertex of e_L, then j≠L-2.

## Body

Because f∩e_L={z} by linearity, w is outside e_L. The path edges containing w form either one edge e_j or two consecutive edges e_j,e_{j+1}. For j<=L-2, omit e_{j+1}, insert f after e_j, and reverse the remaining tail beginning with e_L down through e_{j+2}. The resulting sequence has L edges. Its consecutive intersections are inherited from P except e_j∩f contains w and f∩e_L={z}. The only additional path edge that f might meet is e_{j+1}, when w=e_j∩e_{j+1}, but that edge has been omitted. Hence no nonconsecutive intersection is introduced. If j=L-1, replacing e_L by f gives the stated L-edge path.

Now assume P is globally longest and e_L is nonspecial with unique entrance x while z is terminal. If j=L-2, the rotation is (e_1,...,e_{L-2},f,e_L), a globally longest L-edge path ending in e_L and entering e_L through z=f∩e_L. Since z≠x, this contradicts the unique-longest-entrance characterization of nonspecial edges. Therefore j≠L-2.