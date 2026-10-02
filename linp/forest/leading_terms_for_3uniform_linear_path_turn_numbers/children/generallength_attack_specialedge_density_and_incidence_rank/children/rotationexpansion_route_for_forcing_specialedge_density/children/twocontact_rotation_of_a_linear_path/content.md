# Two-contact rotation of a linear path

## Statement

Let P=(e_1,...,e_p) be a linear path and let f be an edge outside P meeting P exactly in e_j and e_p, with 1<=j<p. If j<=p-2, then (e_1,...,e_j,f,e_p,e_{p-1},...,e_{j+2}) is a p-edge linear path. If j=p-1, then (e_1,...,e_{p-1},f) is a p-edge linear path.

## Body

For j<=p-2, the displayed sequence keeps e_1,...,e_j, inserts f, then keeps e_p,e_{p-1},...,e_{j+2}; only e_{j+1} is omitted, so the length remains p. Consecutive intersections are inherited from P except at e_j,f and f,e_p, which meet by hypothesis. Any prefix edge e_i with i<=j and tail edge e_k with k>=j+2 were nonconsecutive in P and are disjoint. The edge f meets P only in e_j and e_p, its two consecutive neighbors in the rotated sequence. Thus the sequence is a linear path. If j=p-1, simply replace e_p by f; the sequence e_1,...,e_{p-1},f has p edges and is linear.