# Every properly six-colored K6,6 has a rainbow five-edge path

## Statement

Every proper edge-coloring of K_{6,6} with six colors contains a rainbow path of length at least five.

## Body

Take a longest rainbow path P.

It cannot have length at most three. Indeed, orient P so that x is one endpoint. If P has k<=3 edges, then at most two vertices of the opposite bipartition lie on P, so at least four opposite-side vertices lie outside P. Any edge from x to an outside vertex whose color is not already used on P would extend P. Hence all those at least four edges would have to use colors already present on P. But the coloring is proper, so they have distinct colors, while at most k<=3 colors are already used, contradiction.

Thus P has length at least four. Suppose it has exactly four edges. Its endpoints lie in the same bipartition. Fix one endpoint x. The path uses exactly two vertices in the opposite bipartition, so four opposite-side vertices lie outside P. Again, every edge from x to one of those four vertices must use a color already on P, or P extends to a rainbow 5-edge path.

There are four used colors, but the path edge incident with x already uses one of them, and properness forbids that color on any other edge at x. Therefore the four edges from x to the four outside opposite-side vertices would have to receive four distinct colors chosen from only the remaining three used colors, impossible.

Hence a longest rainbow path has at least five edges.