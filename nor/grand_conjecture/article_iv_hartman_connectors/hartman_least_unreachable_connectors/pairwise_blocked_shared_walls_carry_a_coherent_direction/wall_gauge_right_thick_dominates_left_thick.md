# Wall-normalized blocker dominance theorem

## Development

Statement:
Let T be a tournament, let α(u,v,w)=t(u,v)⊕t(v,w)⊕t(w,u), t(u,v)=1 iff u→v, and let C=(c_1,...,c_m), m≥4, be a monochromatic-α=0 order with forward first and last edges in the original representative. Suppose C has maximum support among monochromatic-α=0 orders with the same two forward endpoint ports and containing designated special vertices (if any). Fix 2≤i≤m−2. Path-normalize C by tournament switching, so c_j→c_{j+1} and c_j→c_{j+2}. Let W_i={a∉C: α(c_i,a,c_{i+1})=0}. Independently switch each a∈W_i uniquely so c_i→a→c_{i+1}. Define L_i={a∈W_i:c_{i−1}→a}, R_i={a∈W_i:a→c_{i+2}} in this joint gauge. Then L_i∩R_i=∅, and every b∈R_i dominates every a∈L_i. This statement and the oriented cross-cut are independent of the two possible global path-normalizing gauges.

Proof:
Since α(c_i,a,c_{i+1})=0 and c_i→c_{i+1}, the incidences c_i→a and c_{i+1}→a have opposite bits. Switching a reverses both, giving one and only one choice c_i→a→c_{i+1}. Independent vertex switches preserve every α-label. Because α(C)=0, after switching c_j to orient successive edges forward, the zero triple condition forces c_j→c_{j+2}. Indeed 0=1⊕1⊕t(c_{j+2},c_j), so t(c_{j+2},c_j)=0. This normalization is unique up to switching all c_j simultaneously.

If a∈L_i∩R_i, the four incidences c_{i−1}→a, c_i→a, a→c_{i+1}, a→c_{i+2} hold. Inserting a into gap i gives a directed square-path, preserves all other α-windows and leaves the two exposed endpoint pairs unchanged (2≤i≤m−2), contradicting the hypothesis. Thus L_i∩R_i=∅.

Take a∈L_i, b∈R_i. If a→b in the joint gauge, the order obtained by inserting (a,b) between c_i and c_{i+1} has its six new distance-one/two incidences directed forward: c_{i−1}→a and c_i→a by L_i and wall normalization; c_i→b and b→c_{i+1} by wall normalization; a→b by the assumed orientation; a→c_{i+1} by wall normalization; and b→c_{i+2} by R_i. The new order is therefore α=0 throughout. Both endpoint pairs remain unchanged. It uses two additional vertices, contradicting support maximality. Finally, switching all c_j simultaneously changes every C–outside edge; the unique down-wall choice changes each a as well, so all mutual a,b orientations are unchanged. QED.
