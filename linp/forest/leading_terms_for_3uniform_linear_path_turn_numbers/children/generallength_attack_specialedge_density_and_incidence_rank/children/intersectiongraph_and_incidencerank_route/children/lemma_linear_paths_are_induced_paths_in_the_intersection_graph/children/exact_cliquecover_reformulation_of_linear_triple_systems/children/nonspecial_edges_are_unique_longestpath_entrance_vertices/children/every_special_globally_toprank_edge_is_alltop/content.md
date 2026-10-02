# Every special globally top-rank edge is all-top

## Statement

Let L>=2 be the global maximum linear-path length. If an edge h={a,b,c} has rank phi(h)=L and is special, then phi(a)=phi(b)=phi(c)=L.

## Body

By the certified entrance characterization 7235fdc47d1a, specialness of a rank-at-least-two edge means that at least two distinct entrance labels occur among longest paths ending in h. Say there is an L-edge h-ending path entering through a and another entering through b. For the first path, the final edge h contributes the two new vertices b,c, and either may be chosen as a last vertex; hence phi(b),phi(c)>=L. For the second path, the two new vertices are a,c, so phi(a),phi(c)>=L. By global maximality no endpoint potential exceeds L. Therefore all three equal L.