# A lens-free flat cycle is late-jointed or has one common early rail joint

## Statement

In the lens-free flat-cycle rail system of 960a5153b900, put L=p-2 and let k_i be the aligned level of R_i intersect R_{i+1}. Then exactly one of the following holds:

(1) k_i >= ceil(L/2) for every i; or

(2) there are an index k<ceil(L/2) and a vertex y such that k_i=k and y_i=y for every i. In case (2), every two distinct entrance rails intersect exactly in {y}, and y is the aligned internal joint at level k on every rail.

## Body

Assume some k_i<ceil(L/2). We show that the same joint and level propagate forward around the entire cycle.

Consider R_i,R_{i+1},R_{i+2}. The first two meet uniquely at y_i, at aligned level k_i, and the last two meet uniquely at y_{i+1}, at aligned level k_{i+1}. Since min{k_i,k_{i+1}}<ceil(L/2), the three-rail half-gate lemma 87b1d2ae8b86 implies that R_i and R_{i+2} intersect.

They cannot have two common vertices. Indeed, no entrance endpoint of one rail lies on another rail in the lens-free residual, and two internal common vertices of equal-length maximum endpoint paths yield an elementary lens; the usual replacement argument makes that lens balanced. Thus R_i and R_{i+2} have exactly one common vertex.

Now all three pairs among R_i,R_{i+1},R_{i+2} have unique intersections. By 8e3ab4a34ced these three intersections are one common vertex, at one common aligned level. Hence
  y_{i+1}=y_i and k_{i+1}=k_i<ceil(L/2).

Repeating the same argument with R_{i+1},R_{i+2},R_{i+3}, and so on, propagates this equality around the cyclic index set. Therefore every adjacent pair has the same unique common vertex y at the same level k.

Finally, any two nonadjacent rails already contain y. If they had another common vertex, then, as above, two consecutive common vertices would bound a balanced elementary lens, contrary to the lens-free hypothesis. Thus every pair of distinct entrance rails intersects exactly in {y}.

If no k_i is earlier than ceil(L/2), alternative (1) holds. This proves the dichotomy.